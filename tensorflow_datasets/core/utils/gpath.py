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

"""GPath wrapper around the gfile API."""

import os
import pathlib
import posixpath

import typing
from typing import Any, AnyStr, Iterator, Optional, Type, TypeVar

import tensorflow as tf

from tensorflow_datasets.core.utils import type_utils


_P = TypeVar('_P')


class _GPath(pathlib.PurePath, type_utils.ReadWritePath):
  """Pathlib like api around `tf.io.gfile`."""

  def __new__(cls: Type[_P], *parts: type_utils.PathLike) -> _P:
    full_path = '/'.join(os.fspath(p) for p in parts)
    if full_path.startswith('gs://'):
      root = '/gs/'
      return super().__new__(cls, full_path.replace('gs://', root, 1))
    else:
      return super().__new__(cls, *parts)

  def _new(self: _P, *parts: type_utils.PathLike) -> _P:
    """Create a new `Path` child of same type."""
    return type(self)(*parts)

  # Could try to use `cached_property` when beam is compatible (currently
  # raise mutable input error).
  @property
  def _is_gcs(self) -> bool:
    return self.parts[:2] == ('/', 'gs')

  @property
  def _path_str(self) -> str:
    """Returns the `__fspath__` string representation."""
    value = posixpath.join(*self.parts) if self.parts else '.'
    if self._is_gcs:  # pylint: disable=using-constant-test
      return value.replace('/gs/', 'gs://', 1)
    else:
      return value

  def __fspath__(self) -> str:
    return self._path_str

  def __str__(self) -> str:  # pylint: disable=invalid-str-returned
    return self._path_str

  def __repr__(self) -> str:
    return f'{type(self).__name__}({self._path_str!r})'

  def exists(self) -> bool:
    """Returns True if self exists."""
    return tf.io.gfile.exists(self._path_str)

  def is_dir(self) -> bool:
    """Returns True if self is a directory."""
    return tf.io.gfile.isdir(self._path_str)

  def iterdir(self: _P) -> Iterator[_P]:
    """Iterates over the directory."""
    for f in tf.io.gfile.listdir(self._path_str):
      yield self._new(self, f)

  def expanduser(self: _P) -> _P:
    """Returns a new path with expanded `~` and `~user` constructs."""
    return self._new(posixpath.expanduser(self._path_str))

  def resolve(self: _P, strict: bool = False) -> _P:
    """Returns the abolute path."""
    return self._new(posixpath.abspath(self._path_str))

  def glob(self: _P, pattern: str) -> Iterator[_P]:
    """Yielding all matching files (of any kind)."""
    for f in tf.io.gfile.glob(posixpath.join(self._path_str, pattern)):
      yield self._new(f)

  def mkdir(
      self,
      mode: int = 0o777,
      parents: bool = False,
      exist_ok: bool = False,
  ) -> None:
    """Create a new directory at this given path."""
    if self.exists() and not exist_ok:
      raise FileExistsError(f'{self._path_str} already exists.')

    if parents:
      tf.io.gfile.makedirs(self._path_str)
    else:
      tf.io.gfile.mkdir(self._path_str)

  def rmdir(self) -> None:
    """Remove the empty directory."""
    if not self.is_dir():
      raise NotADirectoryError(f'{self._path_str} is not a directory.')
    if list(self.iterdir()):
      raise ValueError(f'Directory {self._path_str} is not empty')
    tf.io.gfile.rmtree(self._path_str)

  def open(
      self,
      mode: str = 'r',
      encoding: Optional[str] = None,
      errors: Optional[str] = None,
      **kwargs: Any,
  ) -> typing.IO[AnyStr]:
    """Opens the file."""
    if errors:
      raise NotImplementedError
    if encoding and not encoding.lower().startswith(('utf8', 'utf-8')):
      raise ValueError(f'Only UTF-8 encoding supported. Not: {encoding}')
    gfile = tf.io.gfile.GFile(self._path_str, mode, **kwargs)
    gfile = typing.cast(typing.IO[AnyStr], gfile)  # pytype: disable=invalid-typevar
    return gfile

  def rename(self: _P, target: type_utils.PathLike) -> _P:
    """Rename file or directory to the given target."""
    target = os.fspath(self._new(target))  # Normalize gs:// URI
    tf.io.gfile.rename(self._path_str, target)
    return self._new(target)

  def replace(self: _P, target: type_utils.PathLike) -> _P:
    """Replace file or directory to the given target."""
    target = os.fspath(self._new(target))  # Normalize gs:// URI
    tf.io.gfile.rename(self._path_str, target, overwrite=True)
    return self._new(target)


class PosixGPath(_GPath, pathlib.PurePosixPath):
  """Pathlib like api around `tf.io.gfile`."""


class WindowsGPath(_GPath, pathlib.PureWindowsPath):
  """Pathlib like api around `tf.io.gfile`."""
