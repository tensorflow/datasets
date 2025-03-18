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

"""Classes to specify download or extraction information."""

import base64
import codecs
import enum
import itertools
import json
import os
import re
from typing import Any
import urllib

from etils import epath
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import checksums as checksums_lib

Json = dict[str, Any]

_hex_codec = codecs.getdecoder('hex_codec')


def _decode_hex(hexstr: str):
  """Returns binary digest, given str hex digest."""
  return _hex_codec(hexstr)[0]  # pytype: disable=wrong-arg-types


class ExtractMethod(enum.Enum):
  """The extraction method to use to pre-process a downloaded file."""

  NO_EXTRACT = 1
  TAR = 2
  TAR_GZ = 3  # Deprecated: use TAR.
  GZIP = 4
  ZIP = 5
  BZIP2 = 6
  TAR_STREAM = 7
  TAR_GZ_STREAM = 8  # Deprecated: use TAR_STREAM


_EXTRACTION_METHOD_TO_EXTS = [
    (ExtractMethod.TAR_GZ, ['.tar.gz', '.tgz']),
    (ExtractMethod.TAR, ['.tar', '.tar.bz2', '.tbz2', '.tbz', '.tb2']),
    (ExtractMethod.ZIP, ['.zip']),
    (ExtractMethod.GZIP, ['.gz']),
    (ExtractMethod.BZIP2, ['.bz2']),
]

_KNOWN_EXTENSIONS = list(
    itertools.chain(  # pylint: disable=g-complex-comprehension
        *[extensions_ for _, extensions_ in _EXTRACTION_METHOD_TO_EXTS]
    )
)

_NETLOC_COMMON_PREFIXES = [
    'www.',
    'storage.googleapis.com',
    'drive.google.com',
    'github.com',
]

_NETLOC_COMMON_SUFFIXES = [
    '.github.io',
    '.s3-website.eu-central-1.amazonaws.com',
    '.amazonaws.com',  # Must be kept after the other amazonaws.com subdomains.
]

_URL_COMMON_PARTS = [
    '_data_',
    '_dataset_',
    '_static_',
    '_of_',
    '-of-',
]


def guess_extract_method(fname) -> ExtractMethod:
  """Guess extraction method, given file name (or path)."""
  for method, extensions in _EXTRACTION_METHOD_TO_EXTS:
    for ext in extensions:
      if fname.endswith(ext):
        return method
  return ExtractMethod.NO_EXTRACT


def _sanitize_url(url: str, max_length: int) -> tuple[str, str]:
  """Sanitize and shorten url to fit in max_length.

  Function is stable: same input MUST ALWAYS give same result, accros changes
  in code as well. Different URLs might give same result.
  As much as possible, the extension should be kept.

  Heuristics are applied to only keep useful info from url.

  1- Drop generic [sub]domains.
    'www.cs.toronto.edu/...' -> 'cs.toronto.edu/...'
    'storage.googleapis.com/foo/...' -> 'foo/...'
    'drive.google.com/bar/...' -> 'bar/...'
    'github.com/baz/...' -> 'baz/...'

  2- Remove leading '0's from url components:
    'foo/train-00004-of-00010.tfrecords' -> 'foo/train-4-of-10.tfrecords'

  3- Truncate each component of url until total size fits or each component is
     left with 4 chars (or total size is <= limit):
     'MoveUnitToBorder_64x64_png/train-4-of-10.tfrecords'
     (here truncate components to 4 chars per component max)
      -> 'Move_64x6_png/trai-4-of-10.tfrecords'

  4- Truncate result, keeping prefix: 'abc_def_ghi_jkl' -> 'abc_def'

  Args:
    url: Url to sanitize and shorten.
    max_length: Max length of result.

  Returns:
    Sanitized and shorted url, file extension.
  """
  url = urllib.parse.urlparse(url)
  netloc = url.netloc
  for prefix in _NETLOC_COMMON_PREFIXES:
    if netloc.startswith(prefix):
      netloc = netloc[len(prefix) :]
  for suffix in _NETLOC_COMMON_SUFFIXES:
    if netloc.endswith(suffix):
      netloc = netloc[: -len(suffix)]
  url = f'{netloc}{url.path}{url.params}{url.query}'
  # Get the extension:
  for ext in _KNOWN_EXTENSIONS:
    if url.endswith(ext):
      extension = ext
      url = url[: -len(extension)]
      break
  else:
    url, extension = os.path.splitext(url)
  max_length -= len(extension)
  # Replace non authorized chars (including '/') by '_':
  url = re.sub(r'[^a-zA-Z0-9\.\-_]+', '_', url)
  # Remove parts with no info:
  for common_part in _URL_COMMON_PARTS:
    url = url.replace(common_part, '_')
  url = url.strip('_')
  # Remove leading zeros in groups of numbers:
  url = re.sub('(?<![0-9])0+(?=[0-9])', '', url)
  # Decrease max size of URL components:
  c_size = max(len(c) for c in re.split(r'[\.\-_]', url))
  while c_size > 4 and len(url) > max_length:
    c_size -= 1
    url = re.sub(r'[^\.\-_]{4,}', lambda match: match.group(0)[:c_size], url)
  return url[:max_length], extension


def get_dl_fname(url: str, checksum: str | None = None) -> str:
  """Returns name of file for (url, checksum).

  The max length of linux and windows filenames is 255 chars.
  Windows however expects short paths (260 chars), so we limit the file name
  to an arbitrary 90 chars.

  Naming pattern: '{url}{checksum}'.
   - url: url sanitized and shortened to 46 chars.
   - checksum: base64url encoded sha256: 44 chars (removing trailing '=').

  Args:
    url: Url of the file.
    checksum: The sha256 hexdigest of file or url.

  Returns:
    string of 90 chars max.
  """
  if not checksum:
    checksum = checksums_lib.sha256(url)
  checksum = base64.urlsafe_b64encode(_decode_hex(checksum))
  checksum = checksum.decode()[:-1]
  name, extension = _sanitize_url(url, max_length=46)
  return f'{name}{checksum}{extension}'


def get_info_path(path: epath.Path) -> epath.Path:
  """Returns path of INFO file associated with resource at path."""
  return path.with_suffix(path.suffix + '.INFO')


def is_locally_cached(path: epath.Path) -> bool:
  """Returns whether the path is locally cached."""
  # If INFO file doesn't exist, consider path NOT cached.
  return path.exists() and get_info_path(path).exists()


def _read_info(info_path: epath.Path) -> Json:
  """Returns info dict."""
  return json.loads(info_path.read_text()) if info_path.exists() else {}


# TODO(pierrot): one lock per info path instead of locking everything.
synchronize_decorator = utils.build_synchronize_decorator()


def replace_info_file(src_path: epath.Path, dst_path: epath.Path) -> None:
  get_info_path(src_path).replace(get_info_path(dst_path))


@synchronize_decorator
def read_info_file(info_path: epath.Path) -> Json:
  return _read_info(get_info_path(info_path))


def _add_value_to_list(info: Json, key: str, value: str) -> None:
  """Adds `value` to list `key` in `info` dict."""
  if value and value not in (stored_values := info.get(key, [])):
    info[key] = stored_values + [value]


def _set_value(info_path: epath.Path, info: Json, key: str, value: Any) -> None:
  """Sets `value` to `key` in `info` dict."""
  if (stored_value := info.get(key)) and stored_value != value:
    raise ValueError(
        f'File info "{info_path}" contains a different "{key}" than the'
        f' downloaded one: Stored: {stored_value}; Expected: {value}'
    )
  info[key] = value


@synchronize_decorator
def write_info_file(
    url: str,
    path: epath.Path,
    dataset_name: str,
    original_fname: str,
    url_info: checksums_lib.UrlInfo,
) -> None:
  """Write the INFO file next to local file.

  Although the method is synchronized, there is still a risk two processes
  running at the same time overlap here. Risk accepted, since potentially lost
  data (`dataset_name`) is only for human consumption.

  Args:
    url: Url for which to write the INFO file.
    path: path of downloaded file.
    dataset_name: data used to dl the file.
    original_fname: name of file as downloaded.
    url_info: checksums/size info of the url
  """
  info_path = get_info_path(path)
  info = _read_info(info_path)

  _add_value_to_list(info, 'urls', url)
  _add_value_to_list(info, 'dataset_names', dataset_name)
  _set_value(info_path, info, 'original_fname', original_fname)
  _set_value(info_path, info, 'url_info', url_info.asdict())

  with utils.atomic_write(info_path, 'w') as info_f:
    json.dump(info, info_f, sort_keys=True)


def _get_extract_method(path: epath.Path) -> ExtractMethod:
  """Returns `ExtractMethod` to use on resource at path. Cannot be None."""
  info = _read_info(get_info_path(path))
  fname = info.get('original_fname', os.fspath(path))
  return guess_extract_method(fname)


class Resource:
  """Represents a resource to download, extract, or both."""

  def __init__(
      self,
      *,
      url: str | None = None,
      extract_method: ExtractMethod | None = None,
      path: epath.PathLike | None = None,
      relative_download_dir: epath.PathLike = '',
  ):
    """Resource constructor.

    Args:
      url: The URL at which to download the resource.
      extract_method: `ExtractMethod` to be used to extract resource. If not
        set, will be guessed from downloaded file name `original_fname`.
      path: Path of resource on local disk. Can be None if resource has not be
        downloaded yet. In such case, `url` must be set.
      relative_download_dir: Optional directory for downloading relative to
        `download_dir`.
    """
    self._url = url
    self._extract_method = extract_method
    self.path: epath.Path = epath.Path(path) if path else None  # pytype: disable=annotation-type-mismatch  # attribute-variable-annotations
    self.relative_download_dir = relative_download_dir

  @property
  def url(self) -> str:
    """Returns the URL at which to download the resource."""
    if not self._url:
      raise ValueError('URL is undefined from resource.')
    return self._url

  @property
  def extract_method(self) -> ExtractMethod:
    """Returns `ExtractMethod` to use on resource."""
    return self._extract_method or _get_extract_method(self.path)
