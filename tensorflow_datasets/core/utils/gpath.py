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
    return tf.io.gfile.exists(self._get_path_str())

  def iterdir(self) -> Iterator['GcsPath']:
    """Iterates over the directory."""
    for f in tf.io.gfile.listdir(self._get_path_str()):
      yield GcsPath(f)

  def is_dir(self) -> bool:
    """Returns True if self is a directory."""
    return tf.io.gfile.isdir(self._get_path_str())

  def glob(self, pattern: str) -> Iterator['GcsPath']:
    """Yielding all matching files (of any kind)."""
    path = os.path.join(self._get_path_str(), pattern)
    for f in tf.io.gfile.glob(path):
      yield GcsPath(f)

  def mkdir(
      self,
      mode: int = 0o777,
      parents: bool = False,
      exist_ok: bool = False,
  ) -> None:
    """Create a new directory at this given path."""
    if self.exists() and not exist_ok:
      raise FileExistsError(f'{self._get_path_str()} already exists.')

    if parents:
      tf.io.gfile.makedirs(self._get_path_str())
    else:
      tf.io.gfile.mkdir(self._get_path_str())

  def open(
      self,
      mode: str = 'r',
      encoding: Optional[str] = None,
      errors: Optional[str] = None,
      **kwargs: Any,
  ) -> typing.IO[AnyStr]:
    """Opens the file."""
    return tf.io.gfile.GFile(str(self), mode, **kwargs)

  def rename(self, target: type_utils.PathLike) -> None:
    """Rename file or directory to the given target """
    tf.io.gfile.rename(self._get_path_str(), target)

  def replace(self, target: type_utils.PathLike) -> None:
    """Replace file or directory to the given target """
    # TODO: tf.io.gfile.rename(self._get_path_str(), target, overwrite=True)

