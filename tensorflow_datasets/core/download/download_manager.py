# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Download manager interface."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import uuid

from absl import logging
import promise
import six
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import downloader
from tensorflow_datasets.core.download import extractor
from tensorflow_datasets.core.download import resource as resource_lib
from tensorflow_datasets.core.download import util


class NonMatchingChecksumError(Exception):
  """The downloaded file doesn't have expected checksum."""

  def __init__(self, url, tmp_path):
    msg = 'Artifact %s, downloaded to %s, has wrong checksum.' % (url, tmp_path)
    Exception.__init__(self, msg)


class DownloadConfig(object):
  """Configuration for `tfds.core.DatasetBuilder.download_and_prepare`."""

  def __init__(self,
               extract_dir=None,
               manual_dir=None,
               download_mode=None,
               compute_stats=None,
               max_examples_per_split=None):
    """Constructs a `DownloadConfig`.

    Args:
      extract_dir: `str`, directory where extracted files are stored.
        Defaults to "<download_dir>/extracted".
      manual_dir: `str`, read-only directory where manually downloaded/extracted
        data is stored. Defaults to
        "<download_dir>/manual".
      download_mode: `tfds.GenerateMode`, how to deal with downloads or data
        that already exists. Defaults to `REUSE_DATASET_IF_EXISTS`, which will
        reuse both downloads and data if it already exists.
      compute_stats: `tfds.download.ComputeStats`, whether to compute
        statistics over the generated data. Defaults to `AUTO`.
      max_examples_per_split: `int`, optional max number of examples to write
        into each split.
    """
    self.extract_dir = extract_dir
    self.manual_dir = manual_dir
    self.download_mode = util.GenerateMode(
        download_mode or util.GenerateMode.REUSE_DATASET_IF_EXISTS)
    self.compute_stats = util.ComputeStatsMode(
        compute_stats or util.ComputeStatsMode.AUTO)
    self.max_examples_per_split = max_examples_per_split


class DownloadManager(object):
  """Manages the download and extraction of files, as well as caching.

  Downloaded files are cached under `download_dir`. The file name of downloaded
   files follows pattern "${sanitized_url}${content_checksum}.${ext}". Eg:
   'cs.toronto.edu_kriz_cifar-100-pythonJDF[...]I.tar.gz'.

  While a file is being downloaded, it is placed into a directory following a
  similar but different pattern:
  "%{sanitized_url}${url_checksum}.tmp.${uuid}".

  When a file is downloaded, a "%{fname}s.INFO.json" file is created next to it.
  This INFO file contains the following information:
  {"dataset_names": ["name1", "name2"],
   "urls": ["http://url.of/downloaded_file"]}

  Extracted files/dirs are stored under `extract_dir`. The file name or
  directory name is the same as the original name, prefixed with the extraction
  method. E.g.
   "${extract_dir}/TAR_GZ.cs.toronto.edu_kriz_cifar-100-pythonJDF[...]I.tar.gz".

  The function members accept either plain value, or values wrapped into list
  or dict. Giving a data structure will parallelize the downloads.

  Example of usage:

  ```
  # Sequential download: str -> str
  train_dir = dl_manager.download_and_extract('https://abc.org/train.tar.gz')
  test_dir = dl_manager.download_and_extract('https://abc.org/test.tar.gz')

  # Parallel download: list -> list
  image_files = dl_manager.download(
      ['https://a.org/1.jpg', 'https://a.org/2.jpg', ...])

  # Parallel download: dict -> dict
  data_dirs = dl_manager.download_and_extract({
     'train': 'https://abc.org/train.zip',
     'test': 'https://abc.org/test.zip',
  })
  data_dirs['train']
  data_dirs['test']
  ```

  For more customization on the download/extraction (ex: passwords, output_name,
  ...), you can pass a `tfds.download.Resource` as argument.
  """

  @api_utils.disallow_positional_args
  def __init__(self,
               download_dir,
               extract_dir=None,
               manual_dir=None,
               dataset_name=None,
               checksums=None,
               force_download=False,
               force_extraction=False):
    """Download manager constructor.

    Args:
      download_dir: `str`, path to directory where downloads are stored.
      extract_dir: `str`, path to directory where artifacts are extracted.
      manual_dir: `str`, path to manually downloaded/extracted data directory.
      dataset_name: `str`, name of dataset this instance will be used for. If
        provided, downloads will contain which datasets they were used for.
      checksums: `dict<str url, str sha256>`, url to sha256 of resource.
        Only URLs present are checked.
        If empty, checksum of (already) downloaded files is computed and can
        then be retrieved using `recorded_download_checksums` property.
      force_download: `bool`, default to False. If True, always [re]download.
      force_extraction: `bool`, default to False. If True, always [re]extract.
    """
    self._dataset_name = dataset_name
    self._checksums = checksums or {}
    self._record_checksum_size = not checksums
    self._recorded_download_checksums = {}
    self._download_sizes = {}
    self._download_dir = os.path.expanduser(download_dir)
    self._extract_dir = os.path.expanduser(
        extract_dir or os.path.join(download_dir, 'extracted'))
    self._manual_dir = manual_dir and os.path.expanduser(manual_dir)
    tf.io.gfile.makedirs(self._download_dir)
    tf.io.gfile.makedirs(self._extract_dir)
    self._force_download = force_download
    self._force_extraction = force_extraction
    self._extractor = extractor.get_extractor()
    self._downloader = downloader.get_downloader()

  @property
  def recorded_download_checksums(self):
    """Returns checksums for downloaded urls."""
    return dict(self._recorded_download_checksums)

  @property
  def download_sizes(self):
    """Returns sizes (in bytes) for downloaded urls."""
    return dict(self._download_sizes)

  def _handle_download_result(self, resource, tmp_dir_path, sha256, dl_size):
    """Store dled file to definitive place, write INFO file, return path."""
    fnames = tf.io.gfile.listdir(tmp_dir_path)
    if len(fnames) > 1:
      raise AssertionError('More than one file in %s.' % tmp_dir_path)
    original_fname = fnames[0]
    tmp_path = os.path.join(tmp_dir_path, original_fname)
    if self._record_checksum_size:
      resource.sha256 = sha256
      self._download_sizes[resource.url] = dl_size
      self._recorded_download_checksums[resource.url] = sha256
    elif self._checksums[resource.url] != sha256:
      raise NonMatchingChecksumError(resource.url, tmp_path)
    resource.write_info_file(self._dataset_name, original_fname)
    # Unconditionally overwrite because either file doesn't exist or
    # FORCE_DOWNLOAD=true
    tf.io.gfile.rename(tmp_path, resource.path, overwrite=True)
    tf.io.gfile.rmtree(tmp_dir_path)
    return resource.path

  # synchronize and memoize decorators ensure same resource will only be
  # processed once, even if passed twice to download_manager.
  @util.build_synchronize_decorator()
  @utils.memoize()
  def _download(self, resource):
    """Download resource, returns Promise->path to downloaded file."""
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(url=resource)
    resource.sha256 = self._checksums.get(resource.url, None)
    if not resource.path:
      resource.path = os.path.join(self._download_dir, resource.fname)
    if (not self._force_download and resource.sha256 and
        resource.exists_locally()):
      logging.info('URL %s already downloaded: reusing %s.', resource.url,
                   resource.path)
      self._recorded_download_checksums[resource.url] = resource.sha256
      self._download_sizes[resource.url] = (
          tf.io.gfile.stat(resource.path).length)
      return promise.Promise.resolve(resource.path)
    # There is a slight difference between downloader and extractor here:
    # the extractor manages its own temp directory, while the DownloadManager
    # manages the temp directory of downloader.
    tmp_dir_path = '%s.tmp.%s' % (resource.path, uuid.uuid4().hex)
    tf.io.gfile.makedirs(tmp_dir_path)
    logging.info('Downloading %s into %s...', resource.url, tmp_dir_path)

    def callback(val):
      checksum, dl_size = val
      return self._handle_download_result(resource, tmp_dir_path, checksum,
                                          dl_size)
    return self._downloader.download(resource, tmp_dir_path).then(callback)

  @util.build_synchronize_decorator()
  @utils.memoize()
  def _extract(self, resource):
    """Extract a single archive, returns Promise->path to extraction result."""
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(path=resource)
    if resource.extract_method == resource_lib.ExtractMethod.NO_EXTRACT:
      logging.info(
          'Skipping extraction for %s (method=NO_EXTRACT).', resource.path)
      return promise.Promise.resolve(resource.path)
    extract_path = os.path.join(self._extract_dir, resource.extract_fname)
    if not self._force_extraction and tf.io.gfile.exists(extract_path):
      logging.info('Reusing extraction of %s at %s.', resource.path,
                   extract_path)
      return promise.Promise.resolve(extract_path)
    return self._extractor.extract(resource, extract_path)

  @util.build_synchronize_decorator()
  @utils.memoize()
  def _download_extract(self, resource):
    """Download-extract `Resource` or url, returns Promise->path."""
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(url=resource)
    def callback(path):
      resource.path = path
      return self._extract(resource)
    return self._download(resource).then(callback)

  def download_kaggle_data(self, competition_name):
    """Download data for a given Kaggle competition."""
    with self._downloader.tqdm():
      kaggle_downloader = self._downloader.kaggle_downloader(competition_name)
      urls = kaggle_downloader.competition_urls
      files = kaggle_downloader.competition_files
      return _map_promise(self._download,
                          dict((f, u) for (f, u) in zip(files, urls)))

  def download(self, url_or_urls):
    """Download given url(s).

    Args:
      url_or_urls: url or `list`/`dict` of urls to download and extract. Each
        url can be a `str` or `tfds.download.Resource`.

    Returns:
      downloaded_path(s): `str`, The downloaded paths matching the given input
        url_or_urls.
    """
    # Add progress bar to follow the download state
    with self._downloader.tqdm():
      return _map_promise(self._download, url_or_urls)

  def iter_archive(self, resource):
    """Returns iterator over files within archive.

    **Important Note**: caller should read files as they are yielded.
    Reading out of order is slow.

    Args:
      resource: path to archive or `tfds.download.Resource`.

    Returns:
      Generator yielding tuple (path_within_archive, file_obj).
    """
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(path=resource)
    return extractor.iter_archive(resource.path, resource.extract_method)

  def extract(self, path_or_paths):
    """Extract given path(s).

    Args:
      path_or_paths: path or `list`/`dict` of path of file to extract. Each
        path can be a `str` or `tfds.download.Resource`.

    If not explicitly specified in `Resource`, the extraction method is deduced
    from downloaded file name.

    Returns:
      extracted_path(s): `str`, The extracted paths matching the given input
        path_or_paths.
    """
    # Add progress bar to follow the download state
    with self._extractor.tqdm():
      return _map_promise(self._extract, path_or_paths)

  def download_and_extract(self, url_or_urls):
    """Download and extract given url_or_urls.

    Is roughly equivalent to:

    ```
    extracted_paths = dl_manager.extract(dl_manager.download(url_or_urls))
    ```

    Args:
      url_or_urls: url or `list`/`dict` of urls to download and extract. Each
        url can be a `str` or `tfds.download.Resource`.

    If not explicitly specified in `Resource`, the extraction method will
    automatically be deduced from downloaded file name.

    Returns:
      extracted_path(s): `str`, extracted paths of given URL(s).
    """
    # Add progress bar to follow the download state
    with self._downloader.tqdm():
      with self._extractor.tqdm():
        return _map_promise(self._download_extract, url_or_urls)

  @property
  def manual_dir(self):
    """Returns the directory containing the manually extracted data."""
    if not tf.io.gfile.exists(self._manual_dir):
      raise AssertionError(
          'Manual directory {} does not exist. Create it and download/extract '
          'dataset artifacts in there.'.format(self._manual_dir))
    return self._manual_dir


# ============================================================================
# In Python 2.X, threading.Condition.wait() cannot be interrupted by SIGINT,
# unless it's given a timeout. Here we artificially give a long timeout to
# allow ctrl+C.
# This code should be deleted once python2 is no longer supported.
if sys.version_info[0] > 2:

  def _wait_on_promise(p):
    return p.get()

else:

  def _wait_on_promise(p):
    while True:
      result = p.get(sys.maxint)  # pylint: disable=g-deprecated-member-used
      if p.is_fulfilled:
        return result

# ============================================================================


def _map_promise(map_fn, all_inputs):
  """Map the function into each element and resolve the promise."""
  all_promises = utils.map_nested(map_fn, all_inputs)  # Apply the function
  res = utils.map_nested(_wait_on_promise, all_promises)
  return res
