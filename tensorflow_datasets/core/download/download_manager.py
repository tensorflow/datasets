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

import hashlib
import json
import os
import uuid

import promise
import six
import tensorflow as tf

from tensorflow_datasets.core.download import downloader
from tensorflow_datasets.core.download import extractor
from tensorflow_datasets.core.download import util
from tensorflow_datasets.core.proto import download_generated_pb2 as download_pb2

AUTO_EXTRACT = download_pb2.ExtractInfo.AUTO_EXTRACT
NO_EXTRACT = download_pb2.ExtractInfo.NO_EXTRACT
TAR = download_pb2.ExtractInfo.TAR
TAR_GZ = download_pb2.ExtractInfo.TAR_GZ
GZIP = download_pb2.ExtractInfo.GZIP
ZIP = download_pb2.ExtractInfo.ZIP

_EXTRACTION_METHOD_TO_EXTS = [
    (TAR_GZ, ['.tar.gz', '.tgz']),
    (TAR, ['.tar', '.tar.bz2', '.tbz2', '.tbz', '.tb2']),
    (ZIP, ['.zip']),
    (GZIP, ['.gz']),
]


def _guess_extract_method(fname):
  """Guess extraction method, given file name (or path)."""
  for method, extensions in _EXTRACTION_METHOD_TO_EXTS:
    for ext in extensions:
      if fname.endswith(ext):
        return method
  return NO_EXTRACT


def _get_extract_method(extract_info):
  """Returns extraction_method for given artifact, if needed, guess it."""
  if extract_info.extraction_method != AUTO_EXTRACT:
    return extract_info.extraction_method
  return _guess_extract_method(extract_info.path)


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

  Example of usage:

    # Sequential download: str -> str
    train_dir = dl_manager.download_and_extract('https://abc.org/train.tar.gz')
    test_dir = dl_manager.download_and_extract('https://abc.org/test.tar.gz')

    # Parallel download: dict -> dict
    data_dirs = dl_manager.download_and_extract({
       'train': 'https://abc.org/train.zip',
       'test': 'https://abc.org/test.zip',
    })
    data_dirs['train']
    data_dirs['test']

  For more customization on the download/extraction (ex: passwords, output_name,
  ...), you can pass UrlInfo() ExtractInfo() or UrlExtractInfo as arguments.
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
      `bool`, if True, validate checksums of files if url is
        present in the checksums file. If False, no checks are done.
      force_download: `bool`, default to False. If True, always [re]download.
      force_extraction: `bool`, default to False. If True, always [re]extract.
    """
    self._dataset_name = dataset_name
    self._checksums = checksums or {}
    self._download_dir = os.path.expanduser(download_dir)
    self._extract_dir = os.path.expanduser(extract_dir)
    self._manual_dir = os.path.expanduser(manual_dir)
    tf.gfile.MakeDirs(self._download_dir)
    tf.gfile.MakeDirs(self._extract_dir)
    self._force_download = force_download
    self._force_extraction = force_extraction
    self._extractor = extractor.get_extractor()
    self._downloader = downloader.get_downloader()

  @util.build_synchronize_decorator()
  def _write_info_file(self, fpath, url_info):
    """Write the INFO file next to downloaded file.

    Although the method is synchronized, there is still a risk two processes
    running at the same time overlap here. Risk accepted, since those INFO files
    are mostly targeted to human users.

    Args:
      fpath: path to downloaded file.
      url_info: data used to dl the file.
    """
    info_path = fpath + '.INFO'
    if tf.gfile.Exists(info_path):
      with tf.gfile.Open(info_path) as info_f:
        info = json.load(info_f)
    else:
      info = {}
    # TODO(epot): add original filename in INFO file.
    urls = set(info.get('urls', []))
    urls.add(url_info.url)
    dataset_names = set(info.get('dataset_names', []))
    dataset_names.add(self._dataset_name)
    info = dict(urls=list(urls), dataset_names=list(dataset_names))
    with tf.gfile.Open(info_path, 'w') as info_f:
      json.dump(info, info_f)

  def _validate_checksum(self, url, checksum):
    """Returns True if url matches with checksum."""
    # TODO(pierrot): decide if we want to support partial checksum validation
    # by default and silently. If not, fail when _checksums exist and url is not
    # present.
    if url not in self._checksums:  # URL not to be checked.
      return True
    return self._checksums[url] == checksum

  def _downloaded_path(self, url_info):
    """Returns path to which should be stored downloaded file.

    Args:
      url_info: `download_pb2.UrlInfo`, url_info used to download file.
    """
    url = url_info.url
    sha256 = self._checksums.get(url, None)
    if sha256:
      fname = sha256
    else:
      fname = 'url.%s' % hashlib.sha256(url.encode('utf8')).hexdigest()
    return os.path.join(self._download_dir, fname)

  def _extracted_path(self, path, method):
    """Returns path to which should be extracted given path."""
    if not path.startswith(self._download_dir):
      # This would probably require to compute the hash of file to extract...
      # or to not cache extraction.
      raise NotImplementedError('%s is not located under %s' % (
          path, self._download_dir))
    # For downloaded files, we reused the filename.
    fname = os.path.basename(path)
    return os.path.join(self._extract_dir, '%s.%s' % (method, fname))

  def _handle_download_result(self, url_info, tmp_dir_path, sha256):
    """Store dled file to definitive place, write INFO file, return path."""
    fnames = tf.gfile.ListDirectory(tmp_dir_path)
    if len(fnames) > 1:
      raise AssertionError('More than one file in %s.' % tmp_dir_path)
    tmp_path = os.path.join(tmp_dir_path, fnames[0])
    if not self._validate_checksum(url_info.url, sha256):
      raise NonMatchingChecksumError(url_info.url, tmp_path)
    final_path = self._downloaded_path(url_info)
    self._write_info_file(final_path, url_info)
    tf.gfile.Rename(tmp_path, final_path, overwrite=True)
    tf.gfile.DeleteRecursively(tmp_dir_path)
    return final_path

  def _download(self, url_info):
    """Download url, returns Promise->path to downloaded file."""
    if isinstance(url_info, six.string_types):
      url_info = download_pb2.UrlInfo(url=url_info)
    path = self._downloaded_path(url_info)
    if not self._force_download and tf.gfile.Exists(path):
      tf.logging.info(
          'URL %s already downloaded: reusing %s.' % (url_info.url, path))
      return promise.Promise.resolve(path)
    # There is a slight difference between downloader and extractor here:
    # the extractor manages its own temp directory, while the DownloadManager
    # manages the temp directory of downloader.
    uid = uuid.uuid4().hex
    tmp_dir_path = os.path.join(self._download_dir, 'tmp', uid)
    tf.gfile.MakeDirs(tmp_dir_path)
    tf.logging.info('Downloading %s into %s...' % (url_info.url, tmp_dir_path))
    def callback(checksum):
      return self._handle_download_result(url_info, tmp_dir_path, checksum)
    return self._downloader.download(url_info, tmp_dir_path).then(callback)

  def _extract(self, extract_info):
    """Extract a single archive, returns Promise->path to extraction result."""
    if isinstance(extract_info, six.string_types):
      extract_info = download_pb2.ExtractInfo(path=extract_info)
    extraction_method = _get_extract_method(extract_info)
    if extraction_method == NO_EXTRACT:
      tf.logging.info(
          'Skipping extraction for %s (method=NO_EXTRACT).' % extract_info.path)
      return promise.Promise.resolve(extract_info.path)
    to_path = self._extracted_path(extract_info.path, extraction_method)
    if not self._force_extraction and tf.gfile.Exists(to_path):
      tf.logging.info(
          'Reusing extraction of %s at %s.' % (extract_info.path, to_path))
      return promise.Promise.resolve(to_path)
    tf.logging.info('Extracting %s to %s...' % (extract_info.path, to_path))
    return self._extractor.extract(extract_info.path, to_path,
                                   extraction_method).then(lambda _: to_path)

  def _download_extract(self, url_extract_info):
    """Download-extract `UrlExtractInfo` or url, returns Promise->path."""
    if isinstance(url_extract_info, download_pb2.UrlExtractInfo):
      url_info = url_extract_info.url_info
      extract_info = url_extract_info.extract_info
    else:  # string, url
      url_info = url_extract_info
      fname = util.get_file_name(url_info)
      extract_info = download_pb2.ExtractInfo(
          extraction_method=_guess_extract_method(fname))
    def callback(path):
      extract_info.path = path
      return self._extract(extract_info)
    return self._download(url_info).then(callback)

  def download(self, urls, async_=False):
    """Download given artifacts, returns {'name': 'path'} or 'path'.

    Args:
      urls: A single URL (str or UrlInfo) or a `Dict[str, UrlInfo]`.
        The URL(s) to download.
      async_: `bool`, default to False. If True, returns promise on result.

    Returns:
      `str` or `Dict[str, str]`: path or {name: path}.
    """
    if isinstance(urls, dict):  # A dict or URL (`str`) or `UrlInfo` objects.
      paths = {name: self._download(url) for name, url in urls.items()}
      prom = promise.Promise.for_dict(paths)
    else:  # A single URL, `str` or `UrlInfo` object.
      prom = self._download(urls)
    return async_ and prom or prom.get()

  def extract(self, paths, async_=False):
    """Extract path(s).

    Args:
      paths: `Dict[str, str|ExtractInfo]` or a single str|ExtractInfo.
      async_: `bool`, default to False. If True, returns promise on result.

    Returns:
      `Dict[str, str]` or `str`: {'name': 'out_path'} or 'out_path'.
    """
    if isinstance(paths, dict):  # A dict of paths, `str` or `ExtractInfo` objs.
      paths = {name: self._extract(path) for name, path in paths.items()}
      prom = promise.Promise.for_dict(paths)
    else:  # A single path, `str` or `ExtractInfo` object.
      prom = self._extract(paths)
    return async_ and prom or prom.get()

  def download_and_extract(self, url_extract_info, async_=False):
    """Downlaod and extract given resources, returns path or {name: path}.

    Args:
      url_extract_info: `Dict[str, str|DownloadExtractInfo]` or a single
        str|DownloadExtractInfo.
      async_: `bool`, defaults to False. If True, returns promise on result.

    If URL(s) are given (no `DownloadExtractInfo`), the extraction method is
    guessed from the extension of file on URL path.

    Returns:
      `Dict[str, str]` or `str`: {'name': 'out_path'} or 'out_path' of
      downloaded AND extracted resource.
    """
    if isinstance(url_extract_info, dict):
      paths = {name: self._download_extract(uei)
               for name, uei in url_extract_info.items()}
      prom = promise.Promise.for_dict(paths)
    else:
      prom = self._download_extract(url_extract_info)
    return async_ and prom or prom.get()

  @property
  def manual_dir(self):
    """Returns the directory containing the manually extracted data."""
    if not tf.gfile.Exists(self._manual_dir):
      raise AssertionError(
          'Manual directory {} does not exist. Create it and download/extract'
          'dataset artifacts in there.'.format(self._manual_dir))
    return self._manual_dir
