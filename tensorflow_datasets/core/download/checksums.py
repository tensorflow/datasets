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
"""Methods to retrieve and store size/checksums associated to URLs.

"""

import io
import os

import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import utils
from typing import Any, List, Optional, Dict, Tuple

_ROOT_DIR: str = os.path.normpath(os.path.join(os.path.dirname(__file__), '../..'))

_CHECKSUM_DIRS: List[str] = [
    os.path.join(_ROOT_DIR, 'url_checksums'),
]
_CHECKSUM_SUFFIX: str = '.txt'


def add_checksums_dir(checksums_dir: str) -> Optional[List[str]]:
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
  dataset2path: Dict[str, str] = {}
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
  path: Optional[str] = _checksum_paths().get(dataset_name, None)
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


def _read_file(path: str) -> str:
  return tf.io.gfile.GFile(path).read()




def _get_sizes_checksums(checksums_path: str) -> Dict[str, Tuple[int, str]]:
  """Returns {URL: (size, checksum)}s stored within file at given path."""
  checksums_file: List[str] = _read_file(checksums_path).split('\n')
  return parse_sizes_checksums(checksums_file)


def parse_sizes_checksums(checksums_file: List[str]) -> Dict[str, Tuple[int, str]]:
  """Returns {URL: (size, checksum)}s stored within given file."""
  checksums: Dict[int, Tuple[str, str]] = {}
  for line in checksums_file:
    line = line.strip()  # Remove the trailing '\r' on Windows OS.
    if not line or line.startswith('#'):
      continue
    # URL might have spaces inside, but size and checksum will not.
    url, size, checksum = line.rsplit(' ', 2)
    checksums[url] = (int(size), checksum)
  return checksums


@utils.memoize()
def get_all_sizes_checksums() -> Dict[str, Tuple[int, Any]]:
  """Returns dict associating URL to (size, sha256)."""
  sizes_checksums: Dict[str, Tuple[str, Any]] = {}
  for path in _checksum_paths().values():
    data = _get_sizes_checksums(path)
    for url, size_checksum in data.items():
      if (url in sizes_checksums and
          sizes_checksums[url] != size_checksum):
        raise AssertionError(
            'URL %s is registered with 2+ distinct size/checksum tuples.' % url)
    sizes_checksums.update(data)
  return sizes_checksums


def store_checksums(dataset_name: str, sizes_checksums: Dict[str, Tuple[str, Any]]) -> Optional[io.TextIOBase]:
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
    sizes_checksums: dict, {url: (size_in_bytes, checksum)}.
  """
  path: str = _get_path(dataset_name)
  original_data: Dict[str, Tuple[int, str]] = _get_sizes_checksums(path)
  new_data: Dict[str, Tuple[int, str]] = original_data.copy()
  new_data.update(sizes_checksums)
  if original_data == new_data:
    return
  with tf.io.gfile.GFile(path, 'w') as f:
    for url, (size, checksum) in sorted(new_data.items()):
      f.write('%s %s %s\n' % (url, size, checksum))
