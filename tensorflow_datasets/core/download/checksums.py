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

"""Methods to retrieve and store size/checksums associated to URLs.

"""

import os
from typing import Any, Dict, Iterable, List

import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import utils


_ROOT_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))

_CHECKSUM_DIRS = [
    os.path.join(_ROOT_DIR, 'url_checksums'),
]
_CHECKSUM_SUFFIX = '.txt'


class UrlInfo(object):  # TODO(tfds): Use dataclasses
  """Small wrapper around the url metadata (checksum, size).

  Attributes:
    size: Download size of the file
    checksum: Checksum of the file
  """

  def __init__(self, size: int, checksum: str):
    self.size = size
    self.checksum = checksum

  def asdict(self) -> Dict[str, Any]:
    """Returns the dict representation of the dataclass."""
    # TODO(tfds): Replace by `dataclasses.asdict(self)`
    return {
        'size': self.size,
        'checksum': self.checksum,
    }

  def __eq__(self, other) -> bool:
    return (
        type(self) == type(other) and  # pylint: disable=unidiomatic-typecheck
        self.size == other.size and
        self.checksum == other.checksum
    )

  def __ne__(self, other) -> bool:  # Required in Py2
    return not self == other

  def __repr__(self) -> str:
    return '{}(size={}, checksum={})'.format(
        type(self).__name__, self.size, self.checksum)


def add_checksums_dir(checksums_dir: str) -> None:
  """Registers a new checksums dir.

  This function allow external datasets not present in the tfds repository to
  define their own checksums_dir containing the dataset downloads checksums.

  Note: When redistributing your dataset, you should distribute the checksums
  files with it and set `add_checksums_dir` when the user is importing your
  `my_dataset.py`.

  ```
  # Set-up the folder containing the 'my_dataset.txt' checksums.
  checksum_dir = os.path.join(os.path.dirname(__file__), 'checksums/')
  checksum_dir = os.path.normpath(checksum_dir)

  # Add the checksum dir (will be executed when the user import your dataset)
  tfds.download.add_checksums_dir(checksum_dir)

  class MyDataset(tfds.core.DatasetBuilder):
    ...
  ```

  Args:
    checksums_dir: `str`, checksums dir to add to the registry
  """
  if checksums_dir in _CHECKSUM_DIRS:  # Avoid duplicate
    return
  _CHECKSUM_DIRS.append(checksums_dir)


def _list_dir(path: str) -> List[str]:
  return tf.io.gfile.listdir(path)




@utils.memoize()
def _checksum_paths() -> Dict[str, str]:
  """Returns dict {'dataset_name': 'path/to/checksums/file'}."""
  dataset2path = {}
  for dir_path in _CHECKSUM_DIRS:
    for fname in _list_dir(dir_path):
      if not fname.endswith(_CHECKSUM_SUFFIX):
        continue
      fpath = os.path.join(dir_path, fname)
      dataset_name = fname[:-len(_CHECKSUM_SUFFIX)]
      dataset2path[dataset_name] = fpath
  return dataset2path


def _get_path(dataset_name: str) -> str:
  """Returns path to where checksums are stored for a given dataset."""
  path = _checksum_paths().get(dataset_name, None)
  if path:
    return path
  msg = (
      'No checksums file could be find for dataset {}. Please '
      'create one in one of:\n{}'
      'If you are developing your own dataset outsite tfds, you can register '
      'your own checksums_dir with `tfds.download.add_checksums_dir('
      'checksums_dir)` or pass it to the download_and_prepare script with '
      '`--checksums_dir=`'
  ).format(
      dataset_name,
      ''.join(['* {}\n'.format(c) for c in _CHECKSUM_DIRS]))
  raise AssertionError(msg)


def _get_url_infos(checksums_path: str) -> Dict[str, UrlInfo]:
  """Returns {URL: (size, checksum)}s stored within file at given path."""
  with tf.io.gfile.GFile(checksums_path) as f:
    content = f.read()
  return parse_url_infos(content.splitlines())


def parse_url_infos(checksums_file: Iterable[str]) -> Dict[str, UrlInfo]:
  """Returns {URL: (size, checksum)}s stored within given file."""
  url_infos = {}
  for line in checksums_file:
    line = line.strip()  # Remove the trailing '\r' on Windows OS.
    if not line or line.startswith('#'):
      continue
    # URL might have spaces inside, but size and checksum will not.
    url, size, checksum = line.rsplit(' ', 2)
    url_infos[url] = UrlInfo(size=int(size), checksum=checksum)
  return url_infos


@utils.memoize()
def get_all_url_infos() -> Dict[str, UrlInfo]:
  """Returns dict associating URL to (size, sha256)."""
  url_infos = {}
  for path in _checksum_paths().values():
    dataset_url_infos = _get_url_infos(path)
    for url, url_info in dataset_url_infos.items():
      if url_infos.get(url, url_info) != url_info:
        raise AssertionError(
            'URL {} is registered with 2+ distinct size/checksum tuples. '
            '{} vs {}'.format(url, url_info, url_infos[url]))
    url_infos.update(dataset_url_infos)
  return url_infos


def store_checksums(dataset_name: str, url_infos: Dict[str, UrlInfo]) -> None:
  """Store given checksums and sizes for specific dataset.

  Content of file is never disgarded, only updated. This is to ensure that if
  process is killed right after first download finishes, checksums registered
  during previous runs aren't lost.

  It is the responsibility of the caller not to call function multiple times in
  parallel for a given dataset.

  Only original file content is updated. This means the entire set of new sizes
  and checksums must be given at every call.

  Args:
    dataset_name: string.
    url_infos: dict, {url: (size_in_bytes, checksum)}.
  """
  path = _get_path(dataset_name)
  original_data = _get_url_infos(path)
  new_data = original_data.copy()
  new_data.update(url_infos)
  if original_data == new_data:
    return
  with tf.io.gfile.GFile(path, 'w') as f:
    for url, url_info in sorted(new_data.items()):
      f.write('{} {} {}\n'.format(url, url_info.size, url_info.checksum))
