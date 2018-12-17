# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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
import uuid

import promise
import six
import tensorflow as tf

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


class DownloadManager(object):
  """Manages the download and extraction of files, as well as caching.

  Downloaded files are cached under `download_dir`. The file name is:
    - if there is a sha256 associated with the url: "${sha256_of_content}s".
    - otherwise: "url.%(sha256_of_url)s".

  The sha256 of content (if any) associated to each URL are given through the
  `checksum_file` given to constructor.

  When a file is downloaded, a "%{fname}s.INFO.json" file is created next to it.
  This INFO file contains the following information:
  {"dataset_names": ["name1", "name2"],
   "urls": ["http://url.of/downloaded_file"]}
  The INFO files are used by `create_checksum_files.py` script.

  Extracted files/dirs are stored under `extract_dir`. The file name or
  directory name is the same as the original name, prefixed with the extraction
  method. E.g. "${extract_dir}/ZIP.%(sha256_of_zipped_content)s" or
               "${extract_dir}/TAR.url.%(sha256_of_url)s".

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
  ...), you can pass `resource.Resource` as argument.
  """

  def __init__(self,
               dataset_name,
               download_dir=None,
               extract_dir=None,
               manual_dir=None,
               checksums=None,
               force_download=False,
               force_extraction=False):
    """Download manager constructor.

    Args:
      dataset_name: `str`, name of dataset this instance will be used for.
      download_dir: `str`, path to directory where downloads are stored.
      extract_dir: `str`, path to directory where artifacts are extracted.
      manual_dir: `str`, path to manually downloaded/extracted data directory.
      checksums: `dict<str url, str sha256>`, url to sha256 of resource.
        Only URLs present are checked.
      force_download: `bool`, default to False. If True, always [re]download.
      force_extraction: `bool`, default to False. If True, always [re]extract.
    """
    self._dataset_name = dataset_name
    self._checksums = checksums or {}
    self._recorded_download_checksums = {}
    self._download_sizes = {}
    self._download_dir = os.path.expanduser(download_dir)
    self._extract_dir = os.path.expanduser(extract_dir)
    self._manual_dir = os.path.expanduser(manual_dir)
    tf.gfile.MakeDirs(self._download_dir)
    tf.gfile.MakeDirs(self._extract_dir)
    self._force_download = force_download
    self._force_extraction = force_extraction
    self._extractor = extractor.get_extractor()
    self._downloader = downloader.get_downloader()

  def _validate_checksum(self, url, checksum):
    """Returns True if url matches with checksum."""
    # TODO(pierrot): decide if we want to support partial checksum validation
    # by default and silently. If not, fail when _checksums exist and url is not
    # present.
    if url not in self._checksums:  # URL not to be checked.
      return True
    return self._checksums[url] == checksum

  @property
  def recorded_download_checksums(self):
    """Returns checksums for downloaded urls."""
    return dict(self._recorded_download_checksums)

  @property
  def download_sizes(self):
    """Returns sizes (in bytes) for downloaded urls."""
    return dict(self._download_sizes)

  def _handle_download_result(self, resource, tmp_dir_path, sha256, dl_size,
                              existing=False):
    """Store dled file to definitive place, write INFO file, return path."""
    self._download_sizes[resource.url] = dl_size
    self._recorded_download_checksums[resource.url] = sha256
    if existing:
      if not self._validate_checksum(resource.url, sha256):
        raise NonMatchingChecksumError(resource.url, resource.path)
      return resource.path
    fnames = tf.gfile.ListDirectory(tmp_dir_path)
    if len(fnames) > 1:
      raise AssertionError('More than one file in %s.' % tmp_dir_path)
    original_fname = fnames[0]
    tmp_path = os.path.join(tmp_dir_path, original_fname)
    if not self._validate_checksum(resource.url, sha256):
      raise NonMatchingChecksumError(resource.url, tmp_path)
    resource.write_info_file(self._dataset_name, original_fname)
    # Unconditionally overwrite because either file doesn't exist or
    # FORCE_DOWNLOAD=true
    tf.gfile.Rename(tmp_path, resource.path, overwrite=True)
    tf.gfile.DeleteRecursively(tmp_dir_path)
    return resource.path

  def _download(self, resource):
    """Download resource, returns Promise->path to downloaded file."""
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(url=resource)
    if not resource.path:
      resource.path = os.path.join(self._download_dir, resource.fname)
    if not self._force_download and resource.exists_locally():
      tf.logging.info(
          'URL %s already downloaded: reusing %s.' % (resource.url,
                                                      resource.path))
      checksum, dl_size = util.read_checksum_digest(resource.path)
      self._handle_download_result(resource, None, checksum, dl_size,
                                   existing=True)
      return promise.Promise.resolve(resource.path)
    # There is a slight difference between downloader and extractor here:
    # the extractor manages its own temp directory, while the DownloadManager
    # manages the temp directory of downloader.
    tmp_dir_path = '%s.tmp.%s' % (resource.path, uuid.uuid4().hex)
    tf.gfile.MakeDirs(tmp_dir_path)
    tf.logging.info('Downloading %s into %s...' % (resource.url, tmp_dir_path))
    def callback(val):
      checksum, dl_size = val
      return self._handle_download_result(resource, tmp_dir_path, checksum,
                                          dl_size)
    return self._downloader.download(resource, tmp_dir_path).then(callback)

  def _extract(self, resource):
    """Extract a single archive, returns Promise->path to extraction result."""
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(path=resource)
    if resource.extract_method == resource_lib.ExtractMethod.NO_EXTRACT:
      tf.logging.info(
          'Skipping extraction for %s (method=NO_EXTRACT).' % resource.path)
      return promise.Promise.resolve(resource.path)
    extract_path = os.path.join(self._extract_dir, resource.extract_fname)
    if not self._force_extraction and tf.gfile.Exists(extract_path):
      tf.logging.info('Reusing extraction of %s at %s.' % (
          resource.path, extract_path))
      return promise.Promise.resolve(extract_path)
    return self._extractor.extract(resource, extract_path)

  def _download_extract(self, resource):
    """Download-extract `Resource` or url, returns Promise->path."""
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(url=resource)
    def callback(path):
      resource.path = path
      return self._extract(resource)
    return self._download(resource).then(callback)

  def download(self, url_or_urls, async_=False):
    """Download given url(s).

    Args:
      url_or_urls: url or `list`/`dict` of urls to download and extract. Each
        url can be a `str` or `Resource`.
      async_: `bool`, default to False. If True, returns promise on result.

    Returns:
      downloaded_path(s): `str`, The downloaded paths matching the given input
        url_or_urls.
    """
    return _map_promise(self._download, url_or_urls, async_=async_)

  def iter_archive(self, resource):
    """Returns iterator over files within archive.

    Args:
      resource: path to archive or `resource_lib.Resource`.

    Returns:
      Generator yielding tuple (path_within_archive, file_obj).
      Important: read files as they are yielded. Reading out of order is slow.
    """
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(path=resource)
    return extractor.iter_archive(resource.path, resource.extract_method)

  def extract(self, path_or_paths, async_=False):
    """Extract given path(s).

    Args:
      path_or_paths: path or `list`/`dict` of path of file to extract. Each
        path can be a `str` or `Resource`.
      async_: `bool`, default to False. If True, returns promise on result.

    If not explicitly specified in `Resource`, the extraction method is deduced
    from downloaded file name.

    Returns:
      extracted_path(s): `str`, The extracted paths matching the given input
        path_or_paths.
    """
    return _map_promise(self._extract, path_or_paths, async_=async_)

  def download_and_extract(self, url_or_urls, async_=False):
    """Downlaod and extract given url_or_urls.

    Is roughly equivalent to:

    ```
    extracted_paths = dl_manager.extract(dl_manager.download(url_or_urls))
    ```

    Args:
      url_or_urls: url or `list`/`dict` of urls to download and extract. Each
        url can be a `str` or `Resource`.
      async_: `bool`, defaults to False. If True, returns promise on result.

    If not explicitly specified in `Resource`, the extraction method will
    automatically be deduced from downloaded file name.

    Returns:
      extracted_path(s): `str`, extracted paths of given URL(s).
    """
    return _map_promise(self._download_extract, url_or_urls, async_=async_)

  @property
  def manual_dir(self):
    """Returns the directory containing the manually extracted data."""
    if not tf.gfile.Exists(self._manual_dir):
      raise AssertionError(
          'Manual directory {} does not exist. Create it and download/extract'
          'dataset artifacts in there.'.format(self._manual_dir))
    return self._manual_dir


def _map_promise(map_fn, all_inputs, async_):
  """Map the function into each element and resolve the promise."""
  all_promises = utils.map_nested(map_fn, all_inputs)  # Apply the function

  if isinstance(all_promises, dict):
    merged_promise = promise.Promise.for_dict(all_promises)
  elif isinstance(all_promises, list):
    merged_promise = promise.Promise.all(all_promises)
  else:
    merged_promise = all_promises

  return merged_promise if async_ else merged_promise.get()
