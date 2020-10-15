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

"""Utils to handle resources."""

import itertools
import pathlib
import sys
import types
from typing import Union

from tensorflow_datasets.core.utils import type_utils

# pylint: disable=g-import-not-at-top
if sys.version_info >= (3, 9):
  import importlib.resources as importlib_resources
  import zipfile
else:
  import importlib_resources
  import zipp as zipfile
# pylint: enable=g-import-not-at-top

PathLike = type_utils.PathLike
ReadOnlyPath = type_utils.ReadOnlyPath
ReadWritePath = type_utils.ReadWritePath


class ResourcePath(zipfile.Path):
  """Wrapper around `zipfile.Path` compatible with `os.PathLike`.

  Note: Calling `os.fspath` on the path will extract the file so should be
  discouraged.

  """

  def __fspath__(self) -> str:
    """Path string for `os.path.join`, `open`,... compatibility.

    Note: Calling `os.fspath` on the path extract the file, so should be
    discouraged. Prefer using `read_bytes`,... This only works for files,
    not directories.

    Returns:
      the extracted path string.
    """
    raise NotImplementedError('zipapp not supported. Please send us a PR.')

  # Required due to: https://bugs.python.org/issue42043
  def _next(self, at) -> 'ResourcePath':
    return type(self)(self.root, at)


class _Path(type(pathlib.Path())):
  """Small wrapper around `pathlib.Path` to prevent bad usages of `os.fspath`.

  This prevent calling `os.fspath` on directories, thus improving
  compatibility with `zipapp`.

  """

  def __fspath__(self) -> str:
    if not self.is_file():
      raise ValueError(
          'For resources, `os.fspath` should only be called on files, not '
          'directories. Please use `.joinpath`, `.iterdir` and other '
          f'`pathlib.Path` method instead: {self}'
      )
    return super().__fspath__()


def resource_path(package: Union[str, types.ModuleType]) -> ReadOnlyPath:
  """Returns `importlib.resources.files`."""
  path = importlib_resources.files(package)  # pytype: disable=module-attr
  if isinstance(path, pathlib.Path):
    return _Path(path)
  elif isinstance(path, zipfile.Path):
    return ResourcePath(path.root, path.at)
  else:
    raise TypeError(f'Unknown resource path: {type(path)}: {path}')


def to_write_path(path: ReadOnlyPath) -> ReadWritePath:
  """Cast the path to a read-write Path."""
  if not isinstance(path, pathlib.Path):
    raise ValueError(
        f'Can\'t write {path!r}. Make sure you\'re not running from a '
        'zipapp.'
    )
  path = pathlib.Path(path)  # Convert `_Path` -> `Path`
  return path


def tfds_path(*relative_path: PathLike) -> ReadOnlyPath:
  """Path to `tensorflow_datasets/` root dir.

  The following examples are equivalent:

  ```py
  path = tfds.core.tfds_path() / 'path/to/data.txt'
  path = tfds.core.tfds_path('path/to/data.txt')
  path = tfds.core.tfds_path('path', 'to', 'data.txt')
  ```

  Note: Even if `/` is used, those examples are compatible with Windows, as
  pathlib will automatically normalize the paths.

  Args:
    *relative_path: Relative path, eventually to concatenate.

  Returns:
    path: The absolute TFDS path.
  """
  return resource_path('tensorflow_datasets').joinpath(*relative_path)


def tfds_write_path(*relative_path: PathLike) -> ReadWritePath:
  """Path to `tensorflow_datasets/` root dir (read-write).

  Contrary to `tfds.core.tfds_path`, path returned here support write
  operations. As tradeoff, it can't be executed from a `zipapp`.

  Args:
    *relative_path: Relative path, eventually to concatenate.

  Returns:
    tfds_dir: The root TFDS path.
  """
  return to_write_path(tfds_path(*relative_path))
