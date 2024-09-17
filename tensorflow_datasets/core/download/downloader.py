# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from collections.abc import Iterable, Iterator
import concurrent.futures
import contextlib
import dataclasses
import functools
import hashlib
import io
import os
import re
import typing
from typing import Any, ContextManager
import urllib

from etils import epath
from tensorflow_datasets.core import units
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import checksums as checksums_lib
from tensorflow_datasets.core.download import resource as resource_lib
from tensorflow_datasets.core.download import util as download_utils_lib
from tensorflow_datasets.core.utils import tqdm_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import promise
from tensorflow_datasets.core.utils.lazy_imports_utils import requests
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


_DRIVE_URL = re.compile(r'^https://drive\.google\.com/')
MAX_RETRIES = 10

if typing.TYPE_CHECKING:
  # Response interface. Has `.url` and `.headers` attribute
  Response = requests.Response | urllib.response.addinfourl
else:
  Response = Any


@dataclasses.dataclass(eq=False, frozen=True)
class DownloadResult:
  path: epath.Path | None
  url_info: checksums_lib.UrlInfo | None


@utils.memoize()
def get_downloader(*args: Any, **kwargs: Any) -> '_Downloader':
  return _Downloader(*args, **kwargs)


def _read_url_info(url_path: epath.Path) -> checksums_lib.UrlInfo:
  """Loads the `UrlInfo` from the `.INFO` file."""
  file_info = resource_lib.read_info_file(url_path)
  if 'url_info' not in file_info:
    raise ValueError(
        'Could not find `url_info` in {}. This likely indicates that '
        'the files where downloaded with a previous version of TFDS (<=3.1.0). '
    )
  url_info = file_info['url_info']
  url_info.setdefault('filename', None)
  url_info['size'] = utils.Size(url_info['size'])
  return checksums_lib.UrlInfo(**url_info)


def get_cached_path(
    manually_downloaded_path: epath.Path | None,
    registered_path: epath.Path | None,
    unregistered_path: epath.Path,
    registered_url_info: checksums_lib.UrlInfo | None,
) -> DownloadResult:
  """Returns the downloaded path and computed url-info.

  If the path is not cached, or that `url_path` does not match checksums,
  the file will be downloaded again.

  Path can be cached at three different locations:

  Args:
    manually_downloaded_path: Manually downloaded in `dl_manager.manual_dir`
    registered_path: Cached at the final destination (if checksum known)
    unregistered_path: Cached at the tmp destination (if checksum unknown).
    registered_url_info: Registered checksum (if known)
  """
  # User has manually downloaded the file.
  if manually_downloaded_path and manually_downloaded_path.exists():
    return DownloadResult(path=manually_downloaded_path, url_info=None)

  # Download has been cached (checksum known)
  elif registered_path and resource_lib.Resource.exists_locally(
      registered_path
  ):
    # `path = f(checksum)` was found, so url_info match
    return DownloadResult(path=registered_path, url_info=registered_url_info)

  # Download has been cached (checksum unknown)
  elif resource_lib.Resource.exists_locally(unregistered_path):
    # Info restored from `.INFO` file
    url_info = _read_url_info(unregistered_path)
    # If checksums are now registered but do not match, trigger a new
    # download (e.g. previous file corrupted, checksums updated)
    if registered_url_info and url_info != registered_url_info:
      return DownloadResult(path=None, url_info=None)
    else:
      return DownloadResult(path=unregistered_path, url_info=url_info)

  # Else file not found (or has bad checksums). (re)download.
  else:
    return DownloadResult(path=None, url_info=None)


def _filename_from_content_disposition(
    content_disposition: str,
) -> str | None:
  """Extract the filename from the content disposition.

  Parse the content_definition as defined in:
  https://tools.ietf.org/html/rfc2616

  Note:

   * If both encoded (`filename*=`) and ascii (filename=) name are defined,
     the function returns the ascii name, as encoding might create issue on
     some systems
   * If only the encoded name is defined (e.g.
     `filename*=UTF-8''%e2%82%ac.txt`), the function return None as this is
     not yet supported.

  Args:
      content_disposition: String to parse.

  Returns:
      filename: The filename, or None if filename could not be parsed
  """
  match = re.findall(
      # Regex (see unittests for examples):
      # ` *` : Strip eventual whitespaces
      # `['"]?` : Filename is optionally wrapped in quote
      # `([^;\r\n"']+)` : Filename can be any symbol except those
      # `;?` : Stop when encountering optional `;`
      r"""filename= *['"]?([^;\r\n"']+)['"]? *;?""",
      content_disposition,
      flags=re.IGNORECASE,
  )
  if not match:
    return None
  elif len(match) != 1:
    raise ValueError(
        f'Error while parsing filename for: {content_disposition}\n'
        f'Multiple filename detected: {list(match)}'
    )
  return os.path.basename(match[0].rstrip())


def _get_filename(response: Response) -> str:
  content_disposition = response.headers.get('content-disposition', None)
  if content_disposition:
    filename = _filename_from_content_disposition(content_disposition)
    if filename:
      return filename
  # Otherwise, fallback on extracting the name from the url.
  return utils.basename_from_url(response.url)


class _Downloader:
  """Class providing async download API with checksum validation.

  Do not instantiate this class directly. Instead, call `get_downloader()`.
  """

  _DEFAULT_MAX_SIMULTANEOUS_DOWNLOADS = 50
  _pbar_url: tqdm_utils._TqdmPbarAsync
  _pbar_dl_size: tqdm_utils._TqdmPbarAsync

  def __init__(
      self,
      max_simultaneous_downloads: (
          int | None
      ) = _DEFAULT_MAX_SIMULTANEOUS_DOWNLOADS,
      checksumer=None,
  ):
    """Init _Downloader instance.

    Args:
      max_simultaneous_downloads: Optional max number of simultaneous downloads.
        If None then it defaults to `self._DEFAULT_MAX_SIMULTANEOUS_DOWNLOADS`.
      checksumer: `hashlib.HASH`. Defaults to `hashlib.sha256`.
    """
    self._executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=max_simultaneous_downloads
        or self._DEFAULT_MAX_SIMULTANEOUS_DOWNLOADS
    )
    self._checksumer_cls = checksumer or hashlib.sha256

  @contextlib.contextmanager
  def tqdm(self) -> Iterator[None]:
    """Add a progression bar for the current download."""
    async_tqdm = utils.async_tqdm
    with async_tqdm(
        total=0, desc='Dl Completed...', unit=' url', mininterval=1.0
    ) as pbar_url:
      with async_tqdm(
          total=0, desc='Dl Size...', unit=' MiB', mininterval=1.0
      ) as pbar_dl_size:
        self._pbar_url = pbar_url
        self._pbar_dl_size = pbar_dl_size
        yield

  def increase_tqdm(self, dl_result: DownloadResult) -> None:
    """Update the tqdm bars to visually indicate the dl_result is downloaded."""
    self._pbar_url.update_total(1)
    self._pbar_url.update(1)
    if dl_result.url_info:  # Info unknown for manually downloaded files
      self._pbar_dl_size.update_total(dl_result.url_info.size)
      self._pbar_dl_size.update(dl_result.url_info.size)

  def download(
      self, url: str, destination_path: str, verify: bool = True
  ) -> promise.Promise[concurrent.futures.Future[DownloadResult]]:
    """Download url to given path.

    Returns Promise -> sha256 of downloaded file.

    Args:
      url: Address of resource to download.
      destination_path: Path to directory where to download the resource.
      verify: Whether to verify ssl certificates

    Returns:
      Promise obj -> Download result.
    """
    destination_path = os.fspath(destination_path)
    self._pbar_url.update_total(1)
    future = self._executor.submit(
        self._sync_download, url, destination_path, verify
    )
    return promise.Promise.resolve(future)

  def _sync_file_copy(
      self,
      filepath: str,
      destination_path: epath.Path,
  ) -> DownloadResult:
    """Downloads the file through `tf.io.gfile` API."""
    filename = os.path.basename(filepath)
    out_path = destination_path / filename
    tf.io.gfile.copy(filepath, out_path)
    url_info = checksums_lib.compute_url_info(
        out_path, checksum_cls=self._checksumer_cls
    )
    self._pbar_dl_size.update_total(url_info.size)
    self._pbar_dl_size.update(url_info.size)
    self._pbar_url.update(1)
    return DownloadResult(path=out_path, url_info=url_info)

  def _sync_download(
      self, url: str, destination_path: str, verify: bool = True
  ) -> DownloadResult:
    """Synchronous version of `download` method.

    To download through a proxy, the `HTTP_PROXY`, `HTTPS_PROXY`,
    `REQUESTS_CA_BUNDLE`,... environment variables can be exported, as
    described in:
    https://requests.readthedocs.io/en/master/user/advanced/#proxies

    Args:
      url: Url to download.
      destination_path: Path where to write it.
      verify: Whether to verify ssl certificates.

    Returns:
      Download result.

    Raises:
      DownloadError: when download fails.
    """
    destination_path = epath.Path(destination_path)
    try:
      # If url is on a filesystem that gfile understands, use copy. Otherwise,
      # use requests (http) or urllib (ftp).
      if not url.startswith('http'):
        return self._sync_file_copy(url, destination_path)
    except tf.errors.UnimplementedError:
      pass

    with _open_url(url, verify=verify) as (response, iter_content):
      fname = _get_filename(response)
      path = destination_path / fname
      size = 0

      # Initialize the download size progress bar
      size_mb = 0
      unit_mb = units.MiB
      total_size = int(response.headers.get('Content-length', 0)) // unit_mb
      self._pbar_dl_size.update_total(total_size)
      with path.open('wb') as file_:
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
    return DownloadResult(
        path=path,
        url_info=checksums_lib.UrlInfo(
            checksum=checksum.hexdigest(),
            size=utils.Size(size),
            filename=fname,
        ),
    )


def _open_url(
    url: str,
    **kwargs: Any,
) -> ContextManager[tuple[Response, Iterable[bytes]]]:
  """Context manager to open an url.

  Args:
    url: The url to open
    **kwargs: Additional kwargs to forward to `request.get`.

  Returns:
    response: The url response with `.url` and `.header` attributes.
    iter_content: A `bytes` iterator which yield the content.
  """
  # Download FTP urls with `urllib`, otherwise use `requests`
  open_fn = _open_with_urllib if url.startswith('ftp') else _open_with_requests
  return open_fn(url, **kwargs)


@contextlib.contextmanager
def _open_with_requests(
    url: str,
    **kwargs: Any,
) -> Iterator[tuple[Response, Iterable[bytes]]]:
  """Open url with request."""
  with requests.Session() as session:
    retries = requests.packages.urllib3.util.retry.Retry(
        total=MAX_RETRIES,
        backoff_factor=0.2,
        status_forcelist=[500, 502, 503, 504],
        raise_on_redirect=True,
        raise_on_status=True,
    )
    session.mount('http://', requests.adapters.HTTPAdapter(max_retries=retries))
    session.mount(
        'https://', requests.adapters.HTTPAdapter(max_retries=retries)
    )
    if _DRIVE_URL.match(url):
      url = _normalize_drive_url(url)
    with session.get(url, stream=True, **kwargs) as response:
      _assert_status(response)
      yield (response, response.iter_content(chunk_size=io.DEFAULT_BUFFER_SIZE))


@contextlib.contextmanager
def _open_with_urllib(
    url: str,
    **kwargs: Any,
) -> Iterator[tuple[Response, Iterable[bytes]]]:
  del kwargs
  with urllib.request.urlopen(url) as response:  # pytype: disable=attribute-error
    yield (
        response,
        iter(functools.partial(response.read, io.DEFAULT_BUFFER_SIZE), b''),
    )


def _normalize_drive_url(url: str) -> str:
  """Returns Google Drive url with confirmation token."""
  # This bypasses the "Google Drive can't scan this file for viruses" warning
  # when dowloading large files.
  return url + '&confirm=t'


def _assert_status(response: requests.Response) -> None:
  """Ensure the URL response is 200."""
  if response.status_code != 200:
    raise download_utils_lib.DownloadError(
        'Failed to get url {}. HTTP code: {}.'.format(
            response.url, response.status_code
        )
    )
