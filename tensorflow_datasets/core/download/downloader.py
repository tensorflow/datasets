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

"""Async download API with checksum verification. No business logic."""

import concurrent.futures
import contextlib
import functools
import hashlib
import io
import os
import re
from typing import Any, ContextManager, Iterable, Iterator, Tuple, Union
import promise
import requests

from six.moves import urllib
import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import units
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import checksums as checksums_lib

_DRIVE_URL = re.compile(r'^https://drive\.google\.com/')


# Response interface. Has `.url` and `.headers` attribute
Response = Union[requests.Response, urllib.response.addinfourl]


@utils.memoize()
def get_downloader(*args: Any, **kwargs: Any) -> '_Downloader':
  """Returns the _Downloader object."""
  return _Downloader(*args, **kwargs)


def _get_filename(response: Response) -> str:
  """Returns the file name given the response:

  Args:
    response: HTTP request response.

  Returns:
    File name.
  """
  content_disposition = response.headers.get('content-disposition', None)
  if content_disposition:
    match = re.findall('filename="(.+?)"', content_disposition)
    if match:
      return match[0]
  return utils.basename_from_url(response.url)


class DownloadError(Exception):
  """Exception class for download errors."""
  pass


class _Downloader(object):
  """Class providing async download API with checksum validation.

  Do not instantiate this class directly. Instead, call `get_downloader()`.
  """

  def __init__(self, max_simultaneous_downloads: int = 50, checksumer=None):
    """Init _Downloader instance.

    Args:
      max_simultaneous_downloads: `int`, max number of simultaneous downloads.
      checksumer: `hashlib.HASH`. Defaults to `hashlib.sha256`.
    """
    self._executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=max_simultaneous_downloads)
    self._checksumer_cls = checksumer or hashlib.sha256
    self._pbar_url = None
    self._pbar_dl_size = None

  @contextlib.contextmanager
  def tqdm(self) -> Iterator[None]:
    """Add a progression bar for the current download."""
    async_tqdm = utils.async_tqdm
    with async_tqdm(total=0, desc='Dl Completed...', unit=' url') as pbar_url:
      with async_tqdm(total=0, desc='Dl Size...', unit=' MiB') as pbar_dl_size:
        self._pbar_url = pbar_url
        self._pbar_dl_size = pbar_dl_size
        yield

  def download(self, url: str, destination_path: str):
    """Download url to given path.

    Returns Promise -> sha256 of downloaded file.

    Args:
      url: address of resource to download.
      destination_path: `str`, path to directory where to download the resource.

    Returns:
      Promise obj -> (`str`, int): (downloaded object checksum, size in bytes).
    """
    self._pbar_url.update_total(1)
    future = self._executor.submit(self._sync_download, url, destination_path)
    return promise.Promise.resolve(future)

  def _sync_file_copy(
      self, filepath: str, destination_path: str) -> checksums_lib.UrlInfo:
    """Copy files from source to destination.

    Args:
      filepath: Source path.
      destination_path: Destination path.

    Returns:
      Url checksum.
    """
    out_path = os.path.join(destination_path, os.path.basename(filepath))
    tf.io.gfile.copy(filepath, out_path)
    hexdigest, size = utils.read_checksum_digest(
        out_path, checksum_cls=self._checksumer_cls)
    return checksums_lib.UrlInfo(checksum=hexdigest, size=size)

  def _sync_download(
      self, url: str, destination_path: str) -> checksums_lib.UrlInfo:
    """Synchronous version of `download` method.

    To download through a proxy, the `HTTP_PROXY`, `HTTPS_PROXY`,
    `REQUESTS_CA_BUNDLE`,... environement variables can be exported, as
    described in:
    https://requests.readthedocs.io/en/master/user/advanced/#proxies

    Args:
      url: url to download
      destination_path: path where to write it

    Returns:
      None

    Raises:
      DownloadError: when download fails.
    """
    try:
      # If url is on a filesystem that gfile understands, use copy. Otherwise,
      # use requests (http) or urllib (ftp).
      if not url.startswith('http'):
        return self._sync_file_copy(url, destination_path)
    except tf.errors.UnimplementedError:
      pass

    with _open_url(url) as (response, iter_content):
      fname = _get_filename(response)
      path = os.path.join(destination_path, fname)
      size = 0

      # Initialize the download size progress bar
      size_mb = 0
      unit_mb = units.MiB
      total_size = int(response.headers.get('Content-length', 0)) // unit_mb
      self._pbar_dl_size.update_total(total_size)
      with tf.io.gfile.GFile(path, 'wb') as file_:
        checksum = self._checksumer_cls()
        for block in iter_content:
          size += len(block)
          checksum.update(block)
          file_.write(block)

          # Update the download size progress bar
          size_mb += len(block)
          if size_mb > unit_mb:
            self._pbar_dl_size.update(size_mb // unit_mb)
            size_mb %= unit_mb
    self._pbar_url.update(1)
    return checksums_lib.UrlInfo(checksum=checksum.hexdigest(), size=size)


def _open_url(url: str) -> ContextManager[Tuple[Response, Iterable[bytes]]]:
  """Context manager to open an url.

  Args:
    url: The url to open

  Returns:
    response: The url response with `.url` and `.header` attributes.
    iter_content: A `bytes` iterator which yields the content.
  """
  # Download FTP urls with `urllib`, otherwise use `requests`
  open_fn = _open_with_urllib if url.startswith('ftp') else _open_with_requests
  return open_fn(url)


@contextlib.contextmanager
def _open_with_requests(url: str) -> Iterator[Tuple[Response, Iterable[bytes]]]:
  """Open url using the requests package.

  Args:
    url: Url to open.

  Returns:
    Iterator[Tuple[Response, Iterable[bytes]]]
  """
  with requests.Session() as session:
    if _DRIVE_URL.match(url):
      url = _get_drive_url(url, session)
    with session.get(url, stream=True) as response:
      _assert_status(response)
      yield (response, response.iter_content(chunk_size=io.DEFAULT_BUFFER_SIZE))


@contextlib.contextmanager
def _open_with_urllib(url: str) -> Iterator[Tuple[Response, Iterable[bytes]]]:
  """Open url using the urllib package.

  Args:
    url: Url to open.

  Returns:
    Iterator[Tuple[Response, Iterable[bytes]]]
  """
  with urllib.request.urlopen(url) as response:  # pytype: disable=attribute-error
    yield (
        response,
        iter(functools.partial(response.read, io.DEFAULT_BUFFER_SIZE), b''),
    )


def _get_drive_url(url: str, session: requests.Session) -> str:
  """Returns the drive url, possibly with confirmation token.

  Args:
    url: Drive url.
    session: Requests Session object.

  Returns:
    Drive url.
  """
  with session.get(url, stream=True) as response:
    _assert_status(response)
    for k, v in response.cookies.items():
      if k.startswith('download_warning'):
        return url + '&confirm=' + v  # v is the confirm token
  # No token found, let's try with original URL:
  return url


def _assert_status(response: requests.Response) -> None:
  """Ensure the URL response is 200.

  Args:
    response: Requests Response object.

  Raises:
    DownloadError: If the response code is not 200.
  """
  if response.status_code != 200:
    raise DownloadError('Failed to get url {}. HTTP code: {}.'.format(
        response.url, response.status_code))
