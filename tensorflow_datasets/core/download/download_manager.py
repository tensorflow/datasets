# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Download manager interface."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import concurrent.futures
import hashlib
import os
import sys
from typing import Optional, Union
import uuid

from absl import logging
import promise
import six
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import checksums
from tensorflow_datasets.core.download import downloader
from tensorflow_datasets.core.download import extractor
from tensorflow_datasets.core.download import resource as resource_lib
from tensorflow_datasets.core.download import util


class NonMatchingChecksumError(Exception):
  """The downloaded file doesn't have expected checksum."""

  def __init__(self, url, tmp_path):
    msg = (
        'Artifact {}, downloaded to {}, has wrong checksum. This might '
        'indicate:\n'
        ' * The website may be down (e.g. returned a 503 status code). Please '
        'check the url.\n'
        ' * For Google Drive URLs, try again later as Drive sometimes rejects '
        'downloads when too many people access the same URL. See '
        'https://github.com/tensorflow/datasets/issues/1482\n'
        ' * The original datasets files may have been updated. In this case '
        'the TFDS dataset builder should be updated to use the new files '
        'and checksums. Sorry about that. Please open an issue or send us a PR '
        'with a fix.\n'
        ' * If you\'re adding a new dataset, don\'t forget to register the '
        'checksums as explained in: '
        'https://www.tensorflow.org/datasets/add_dataset#2_run_download_and_prepare_locally\n'
    ).format(url, tmp_path)
    Exception.__init__(self, msg)


class DownloadConfig(object):
  """Configuration for `tfds.core.DatasetBuilder.download_and_prepare`."""

  def __init__(
      self,
      extract_dir=None,
      manual_dir=None,
      download_mode=None,
      compute_stats=None,
      max_examples_per_split=None,
      register_checksums=False,
      force_checksums_validation=False,
      beam_runner=None,
      beam_options=None,
      try_download_gcs=True,
  ):
    """Constructs a `DownloadConfig`.

    Args:
      extract_dir: `str`, directory where extracted files are stored.
        Defaults to "<download_dir>/extracted".
      manual_dir: `str`, read-only directory where manually downloaded/extracted
        data is stored. Defaults to `<download_dir>/manual`.
      download_mode: `tfds.GenerateMode`, how to deal with downloads or data
        that already exists. Defaults to `REUSE_DATASET_IF_EXISTS`, which will
        reuse both downloads and data if it already exists.
      compute_stats: `tfds.download.ComputeStats`, whether to compute
        statistics over the generated data. Defaults to `AUTO`.
      max_examples_per_split: `int`, optional max number of examples to write
        into each split (used for testing).
      register_checksums: `bool`, defaults to False. If True, checksum of
        downloaded files are recorded.
      force_checksums_validation: `bool`, defaults to False. If True, raises
        an error if an URL do not have checksums.
      beam_runner: Runner to pass to `beam.Pipeline`, only used for datasets
        based on Beam for the generation.
      beam_options: `PipelineOptions` to pass to `beam.Pipeline`, only used for
        datasets based on Beam for the generation.
      try_download_gcs: `bool`, defaults to True. If True, prepared dataset
        will be downloaded from GCS, when available. If False, dataset will be
        downloaded and prepared from scratch.
    """
    self.extract_dir = extract_dir
    self.manual_dir = manual_dir
    self.download_mode = util.GenerateMode(
        download_mode or util.GenerateMode.REUSE_DATASET_IF_EXISTS)
    self.compute_stats = util.ComputeStatsMode(
        compute_stats or util.ComputeStatsMode.AUTO)
    self.max_examples_per_split = max_examples_per_split
    self.register_checksums = register_checksums
    self.force_checksums_validation = force_checksums_validation
    self.beam_runner = beam_runner
    self.beam_options = beam_options
    self.try_download_gcs = try_download_gcs


class DownloadManager(object):
  """Manages the download and extraction of files, as well as caching.

  Downloaded files are cached under `download_dir`. The file name of downloaded
   files follows pattern "{sanitized_url}{content_checksum}.{ext}". Eg:
   'cs.toronto.edu_kriz_cifar-100-pythonJDF[...]I.tar.gz'.

  While a file is being downloaded, it is placed into a directory following a
  similar but different pattern:
  "{sanitized_url}{url_checksum}.tmp.{uuid}".

  When a file is downloaded, a "{fname}.INFO.json" file is created next to it.
  This INFO file contains the following information:
  {"dataset_names": ["name1", "name2"],
   "urls": ["http://url.of/downloaded_file"]}

  Extracted files/dirs are stored under `extract_dir`. The file name or
  directory name is the same as the original name, prefixed with the extraction
  method. E.g.
   "{extract_dir}/TAR_GZ.cs.toronto.edu_kriz_cifar-100-pythonJDF[...]I.tar.gz".

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
  def __init__(
      self,
      download_dir: str,
      extract_dir: Optional[str] = None,
      manual_dir: Optional[str] = None,
      manual_dir_instructions: Optional[str] = None,
      dataset_name: Optional[str] = None,
      force_download: bool = False,
      force_extraction: bool = False,
      force_checksums_validation: bool = False,
      register_checksums: bool = False,
  ):
    """Download manager constructor.

    Args:
      download_dir: Path to directory where downloads are stored.
      extract_dir: Path to directory where artifacts are extracted.
      manual_dir: Path to manually downloaded/extracted data directory.
      manual_dir_instructions: Human readable instructions on how to
        prepare contents of the manual_dir for this dataset.
      dataset_name: Name of dataset this instance will be used for. If
        provided, downloads will contain which datasets they were used for.
      force_download: If True, always [re]download.
      force_extraction: If True, always [re]extract.
      force_checksums_validation: If True, raises an error if an URL do not
        have checksums.
      register_checksums: If True, dl checksums aren't
        checked, but stored into file.
    """
    self._dataset_name = dataset_name
    self._download_dir = os.path.expanduser(download_dir)
    self._extract_dir = os.path.expanduser(
        extract_dir or os.path.join(download_dir, 'extracted'))
    self._manual_dir = manual_dir and os.path.expanduser(manual_dir)
    self._manual_dir_instructions = manual_dir_instructions
    tf.io.gfile.makedirs(self._download_dir)
    tf.io.gfile.makedirs(self._extract_dir)
    self._force_download = force_download
    self._force_extraction = force_extraction
    self._force_checksums_validation = force_checksums_validation
    self._register_checksums = register_checksums
    # All known URLs: {url: (size, checksum)}
    self._url_infos = checksums.get_all_url_infos()
    # To record what is being used: {url: (size, checksum)}
    self._recorded_url_infos = {}
    # These attributes are lazy-initialized since they must be cleared when this
    # object is pickled for Beam. They are then recreated on each worker.
    self.__downloader = None
    self.__extractor = None
    # Executor to avoid blocking other download/extractions when running I/O
    # operations (reading/renaming download file).
    # Only use a single thread as the read/ops are locked by the
    # `build_synchronize_decorator`.
    # Note: This thread is in additions of the download and extraction
    # executors threads.
    self._executor = concurrent.futures.ThreadPoolExecutor(1)

  def __getstate__(self):
    """Remove un-pickleable attributes and return the state."""
    if self._register_checksums:
      # Currently, checksums registration from Beam not supported.
      raise NotImplementedError(
          '`register_checksums` must be disabled in a parallelized '
          'DownloadManager. Please open a PR if you would like this feature.')
    state = self.__dict__.copy()
    state['_DownloadManager__downloader'] = None
    state['_DownloadManager__extractor'] = None
    state['_executor'] = None
    return state

  @property
  def _downloader(self):
    if not self.__downloader:
      self.__downloader = downloader.get_downloader()
    return self.__downloader

  @property
  def _extractor(self):
    if not self.__extractor:
      self.__extractor = extractor.get_extractor()
    return self.__extractor

  @property
  def downloaded_size(self):
    """Returns the total size of downloaded files."""
    return sum(url_info.size for url_info in self._recorded_url_infos.values())

  def _get_final_dl_path(self, url, sha256):
    return os.path.join(self._download_dir,
                        resource_lib.get_dl_fname(url, sha256))

  @property
  def register_checksums(self):
    """Returns whether checksums are being computed and recorded to file."""
    return self._register_checksums

  @utils.build_synchronize_decorator()
  def _record_url_infos(self):
    """Store in file when recorded size/checksum of downloaded files."""
    checksums.store_checksums(self._dataset_name,
                              self._recorded_url_infos)

  def _handle_download_result(
      self,
      resource: resource_lib.Resource,
      tmp_dir_path: str,
      url_path: str,
      url_info: checksums.UrlInfo,
  ) -> str:
    """Post-processing of the downloaded file.

    * Write `.INFO` file
    * Rename `tmp_dir/file.xyz` -> `url_path`
    * Validate/record checksums
    * Eventually rename `url_path` -> `file_path` when `record_checksums=True`

    Args:
      resource: The url to download.
      tmp_dir_path: Temporary dir where the file was downloaded.
      url_path: Destination path.
      url_info: File checksums, size, computed during download.

    Returns:
      dst_path: `url_path` (or `file_path` when `register_checksums=True`)

    Raises:
      NonMatchingChecksumError:
    """
    # Extract the file name, path from the tmp_dir
    fnames = tf.io.gfile.listdir(tmp_dir_path)
    if len(fnames) != 1:
      raise ValueError(
          'Download not found for url {} in: {}. Found {} files, but expected '
          '1.'.format(resource.url, tmp_dir_path, len(fnames)))
    original_fname, = fnames  # Unpack list
    tmp_path = os.path.join(tmp_dir_path, original_fname)

    # Write `.INFO` file and rename `tmp_dir/file.xyz` -> `url_path`
    resource_lib.write_info_file(
        resource=resource,
        path=url_path,
        dataset_name=self._dataset_name,
        original_fname=original_fname,
        url_info=url_info,
    )
    # Unconditionally overwrite because either file doesn't exist or
    # FORCE_DOWNLOAD=true
    tf.io.gfile.rename(tmp_path, url_path, overwrite=True)
    tf.io.gfile.rmtree(tmp_dir_path)

    # After this checkpoint, the url file is cached, so should never be
    # downloaded again, even if there are error in registering checksums.

    # Even if `_handle_download_result` is executed asyncronously, Python
    # built-in ops are atomic in CPython (and Pypy), so it should be safe
    # to update `_recorded_url_infos`.
    self._recorded_url_infos[resource.url] = url_info

    # Validate the download checksum, or register checksums
    dst_path = url_path
    if self._register_checksums:
      # Change `dst_path` from `url_path` -> `file_path`
      dst_path = self._save_url_info_and_rename(
          url=resource.url, url_path=url_path, url_info=url_info)
    elif resource.url not in self._url_infos:
      if self._force_checksums_validation:
        raise ValueError(
            'Missing checksums url: {}, yet `force_checksums_validation=True`. '
            'Did you forgot to register checksums ?')
      # Otherwise, missing checksums, do nothing
    elif url_info != self._url_infos.get(resource.url, None):
      raise NonMatchingChecksumError(resource.url, tmp_path)

    return dst_path

  def _save_url_info_and_rename(
      self,
      url: str,
      url_path: str,
      url_info: checksums.UrlInfo,
  ) -> str:
    """Saves the checksums on disk and renames `url_path` -> `file_path`.

    This function assume the file has already be downloaded in `url_path`.

    Args:
      url: Url downloaded
      url_path: Path of the downloaded file.
      url_info: Downloaded file information.

    Returns:
      file_path: The downloaded file after renaming.
    """
    # Record checksums/download size
    # As downloads are cached even without checksum, we could
    # avoid recording the checksums for each urls, and record them once
    # globally at the end.
    assert url in self._recorded_url_infos
    self._record_url_infos()

    # Rename (after checksum got saved succesfully)
    file_path = self._get_final_dl_path(url, url_info.checksum)
    tf.io.gfile.rename(url_path, file_path, overwrite=True)
    resource_lib.rename_info_file(url_path, file_path, overwrite=True)
    return file_path

  def _find_existing_path(self, url: str, url_path: str) -> Optional[str]:
    """Returns the downloaded file path if it exists.

    The file can be located in two different locations:

    * `file_path = f(url, hash(file))`
    * `url_path = f(url, hash(url))`

    `file_path` can only be computed if the file checksum is known in
    advance. Otherwise, `url_path` is used as fallback.

    Args:
      url: Downloaded url
      url_path: File path when the file checksums is unknown

    Returns:
      existing_path: `file_path` or `url_path` if the file was already
        downloaded. `None` otherwise.
    """
    existing_path = None
    # If download is forced, then have to re-download in all cases
    if not self._force_download:
      # File checksum is registered (`file_path` known)
      if url in self._url_infos:
        expected_file_checksum = self._url_infos[url].checksum
        file_path = self._get_final_dl_path(url, expected_file_checksum)
        if resource_lib.Resource.exists_locally(file_path):
          existing_path = file_path
          # Info restored from `checksums/dataset.txt` files.
          self._recorded_url_infos[url] = self._url_infos[url]

      # If `file_path` isn't found (or unknown), fall back to `url_path`
      if not existing_path and resource_lib.Resource.exists_locally(url_path):
        existing_path = url_path
        # Info restored from `.INFO` file
        self._recorded_url_infos[url] = _read_url_info(url_path)
    return existing_path

  def download_checksums(self, checksums_url):
    """Downloads checksum file from the given URL and adds it to registry."""
    checksums_path = self.download(checksums_url)
    with tf.io.gfile.GFile(checksums_path) as f:
      self._url_infos.update(checksums.parse_url_infos(f))

  # Synchronize and memoize decorators ensure same resource will only be
  # processed once, even if passed twice to download_manager.
  @utils.build_synchronize_decorator()
  @utils.memoize()
  def _download(self, resource: Union[str, resource_lib.Resource]):
    """Download resource, returns Promise->path to downloaded file.

    Args:
      resource: The URL to download.

    Returns:
      path: The path to the downloaded resource.
    """
    # Normalize the input
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(url=resource)
    url = resource.url

    # Compute the existing path if the file was previously downloaded
    url_path = self._get_final_dl_path(
        url, hashlib.sha256(url.encode('utf-8')).hexdigest())
    existing_path = self._find_existing_path(url=url, url_path=url_path)

    # If register checksums and file already downloaded, then:
    # * Record the url_infos of the downloaded file
    # * Rename the filename `url_path` -> `file_path`, and return it.
    if self._register_checksums and existing_path == url_path:
      logging.info(
          'URL %s already downloaded: Recording checksums from %s.',
          url,
          existing_path,
      )
      future = self._executor.submit(
          self._save_url_info_and_rename,
          url=url,
          url_path=url_path,
          url_info=self._recorded_url_infos[url],
      )
      return promise.Promise.resolve(future)
    # Otherwise, url_infos are either already registered, or will be registered
    # in the `_handle_download_result` callback.

    # If the file file already exists (`file_path` or `url_path`), return it.
    if existing_path:
      logging.info('URL %s already downloaded: reusing %s.', url, existing_path)
      return promise.Promise.resolve(existing_path)

    # Otherwise, download the file, and eventually computing the checksums.
    # There is a slight difference between downloader and extractor here:
    # the extractor manages its own temp directory, while the DownloadManager
    # manages the temp directory of downloader.
    download_dir_path = os.path.join(
        self._download_dir,
        '%s.tmp.%s' % (resource_lib.get_dl_dirname(url), uuid.uuid4().hex))
    tf.io.gfile.makedirs(download_dir_path)
    logging.info('Downloading %s into %s...', url, download_dir_path)
    def callback(url_info):
      return self._handle_download_result(
          resource=resource,
          tmp_dir_path=download_dir_path,
          url_path=url_path,
          url_info=url_info,
      )
    return self._downloader.download(url, download_dir_path).then(callback)

  @utils.build_synchronize_decorator()
  @utils.memoize()
  def _extract(self, resource):
    """Extract a single archive, returns Promise->path to extraction result."""
    if isinstance(resource, six.string_types):
      resource = resource_lib.Resource(path=resource)
    path = resource.path
    extract_method = resource.extract_method
    if extract_method == resource_lib.ExtractMethod.NO_EXTRACT:
      logging.info('Skipping extraction for %s (method=NO_EXTRACT).', path)
      return promise.Promise.resolve(path)
    method_name = resource_lib.ExtractMethod(extract_method).name
    extract_path = os.path.join(self._extract_dir,
                                '%s.%s' % (method_name, os.path.basename(path)))
    if not self._force_extraction and tf.io.gfile.exists(extract_path):
      logging.info('Reusing extraction of %s at %s.', path, extract_path)
      return promise.Promise.resolve(extract_path)
    return self._extractor.extract(path, extract_method, extract_path)

  @utils.build_synchronize_decorator()
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
    if not self._manual_dir:
      raise AssertionError(
          'Manual directory was enabled. '
          'Did you set MANUAL_DOWNLOAD_INSTRUCTIONS in your dataset?')
    if (not tf.io.gfile.exists(self._manual_dir) or
        not list(tf.io.gfile.listdir(self._manual_dir))):
      raise AssertionError(
          'Manual directory {} does not exist or is empty. Create it and '
          'download/extract dataset artifacts in there. Additional '
          'instructions: {}'.format(
              self._manual_dir, self._manual_dir_instructions))
    return self._manual_dir


def _read_url_info(url_path: str) -> checksums.UrlInfo:
  """Loads the `UrlInfo` from the `.INFO` file."""
  file_info = resource_lib.read_info_file(url_path)
  if 'url_info' not in file_info:
    raise ValueError(
        'Could not found `url_info` in {}. This likelly indicates that '
        'the files where downloaded with a previous version of TFDS (<=3.1.0). '
    )
  return checksums.UrlInfo(**file_info['url_info'])


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
