"""GcsPath wrapper around the gfile API"""

import os
import pathlib
import typing
from typing import Any, AnyStr, Iterator, Optional, Union

import tensorflow as tf

from tensorflow_datasets.core.utils import type_utils

PathArg = Union[str, pathlib.Path, 'GcsPath']


class GcsPath(pathlib.PurePosixPath, type_utils.ReadWritePath):
  """Pathlib like api of tf.io.gfile"""
  def __new__(cls, *parts: type_utils.PathLike):
    full_path = '/'.join(os.fspath(p) for p in parts)
    if full_path.startswith(('gs://')):
      return super().__new__(cls, full_path.replace('gs://', '/gs/', 1))
    if full_path.startswith(('/gs/')):
      return super().__new__(cls, *parts)
    else:
      raise ValueError('Invalid path')


  def _get_path_str(self) -> str:
    value = super().__str__()
    if value.startswith('/gs/'):
      return value.replace('/gs/', 'gs://', 1)
    return value  # TODO: Could cache the value


  def __fpath__(self) -> str:
    return self._get_path_str()


  def __str__(self) -> str:
    return self._get_path_str()


  def exists(self) -> bool:
    """Returns True if self exists."""
    return tf.io.gfile.exists(str(self))


  def iterdir(self) -> Iterator['GcsPath']:
    """Iterates over the directory."""
    for f in tf.io.gfile.listdir(str(self)):
      yield GcsPath(f)


  def is_dir(self) -> bool:
    """Returns True if self is a directory."""
    return tf.io.gfile.isdir(str(self))


  def glob(self, pattern: str) -> Iterator['GcsPath']:
    """Yielding all matching files (of any kind)."""
    path = os.path.join(str(self), pattern)
    for f in tf.io.gfile.glob(str(path)):
      yield GcsPath(f)


  def mkdir(
      self,
      mode: int = 0o777,
      parents: bool = False,
      exist_ok: bool = False,
  ) -> None:
    """Create a new directory at this given path."""
    if self.exists() and not exist_ok:
      raise FileExistsError(f'{str(self)} already exists.')

    if parents:
      tf.io.gfile.makedirs(str(self))
    else:
      tf.io.gfile.mkdir(str(self))


  def open(
      self,
      mode: str = 'r',
      encoding: Optional[str] = None,
      errors: Optional[str] = None,
      **kwargs: Any,
  ) -> typing.IO[AnyStr]:
    """Opens the file."""
    return tf.io.gfile.GFile(str(self), mode, **kwargs)


  def read_bytes(self) -> bytes:
    """Reads contents of self as bytes."""
    with tf.io.gfile.GFile(str(self), 'rb') as f:
      return f.read()


  def read_text(self, encoding: Optional[str] = None) -> str:
    """Reads contents of self as str."""
    with tf.io.gfile.GFile(str(self), 'r') as f:
      return f.read()


  def write_bytes(self, data: bytes) -> None:
    """Writes content as bytes."""
    with tf.io.gfile.GFile(str(self), 'wb') as f:
      return f.write(data)


  def write_text(self,
                 data: str,
                 encoding: Optional[str] = None,
                 errors: Optional[str] = None) -> None:
    """Writes content as str."""
    with tf.io.gfile.GFile(str(self), 'w') as f:
      return f.write(data)


  def rename(self, target) -> None:
    """Rename file or directory to the given target """
    tf.io.gfile.rename(str(self), target)


  def replace(self, target) -> None:
    """Replace file or directory to the given target """
    tf.io.gfile.rename(str(self), target, overwrite=True)
