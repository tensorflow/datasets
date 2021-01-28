# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Pathlib-like generic abstraction."""

import os
import typing
from typing import Callable, Dict, Tuple, Type, Union, TypeVar

from tensorflow_datasets.core.utils import gpath
from tensorflow_datasets.core.utils import type_utils

PathLike = type_utils.PathLike
ReadOnlyPath = type_utils.ReadOnlyPath
ReadWritePath = type_utils.ReadWritePath

PathLikeCls = Union[Type[ReadOnlyPath], Type[ReadWritePath]]
T = TypeVar('T')


_PATHLIKE_CLS: Tuple[PathLikeCls, ...] = (
    gpath.PosixGPath,
    gpath.WindowsGPath,
)
_URI_PREFIXES_TO_CLS: Dict[str, PathLikeCls] = {
    # Even on Windows, `gs://`,... are PosixPath
    uri_prefix: gpath.PosixGPath for uri_prefix in gpath.URI_PREFIXES
}


# pylint: disable=g-wrong-blank-lines
@typing.overload
def register_pathlike_cls(path_cls_or_uri_prefix: str) -> Callable[[T], T]:
  ...
@typing.overload
def register_pathlike_cls(path_cls_or_uri_prefix: T) -> T:
  ...
def register_pathlike_cls(path_cls_or_uri_prefix):
  """Register the class to be forwarded as-is in `as_path`.

  ```python
  @utils.register_pathlike_cls('my_path://')
  class MyPath(pathlib.PurePosixPath):
    ...

  my_path = tfds.core.as_path('my_path://some-path')
  ```

  Args:
    path_cls_or_uri_prefix: If a uri prefix is given, then passing calling
      `tfds.core.as_path('prefix://path')` will call the decorated class.

  Returns:
    The decorator or decoratorated class
  """
  global _PATHLIKE_CLS
  if isinstance(path_cls_or_uri_prefix, str):

    def register_pathlike_decorator(cls: T) -> T:
      _URI_PREFIXES_TO_CLS[path_cls_or_uri_prefix] = cls
      return register_pathlike_cls(cls)

    return register_pathlike_decorator
  else:
    _PATHLIKE_CLS = _PATHLIKE_CLS + (path_cls_or_uri_prefix,)
    return path_cls_or_uri_prefix
# pylint: enable=g-wrong-blank-lines


def as_path(path: PathLike) -> ReadWritePath:
  """Create a generic `pathlib.Path`-like abstraction.

  Depending on the input (e.g. `gs://`, `github://`, `ResourcePath`,...), the
  system (Windows, Linux,...), the function will create the right pathlib-like
  abstraction.

  Args:
    path: Pathlike object.

  Returns:
    path: The `pathlib.Path`-like abstraction.
  """
  is_windows = os.name == 'nt'
  if isinstance(path, str):
    uri_splits = path.split('://', maxsplit=1)
    if len(uri_splits) > 1:  # str is URI (e.g. `gs://`, `github://`,...)
      # On windows, `PosixGPath` is created for `gs://` paths
      return _URI_PREFIXES_TO_CLS[uri_splits[0] + '://'](path)  # pytype: disable=bad-return-type
    elif is_windows:
      return gpath.WindowsGPath(path)
    else:
      return gpath.PosixGPath(path)
  elif isinstance(path, _PATHLIKE_CLS):
    return path  # Forward resource path, gpath,... as-is  # pytype: disable=bad-return-type
  elif isinstance(path, os.PathLike):  # Other `os.fspath` compatible objects
    path_cls = gpath.WindowsGPath if is_windows else gpath.PosixGPath
    return path_cls(path)
  else:
    raise TypeError(f'Invalid path type: {path!r}')
