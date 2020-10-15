"""GPath wrapper around the gfile API"""

import os
import pathlib
import typing
from typing import Union, Iterator, Optional, Any, AnyStr
import tensorflow as tf
from tensorflow_datasets.core.utils import type_utils

PathArg = Union[str, pathlib.Path, 'GPath']


class GPath(pathlib.PurePosixPath, type_utils.ReadWritePath):

  def __new__(cls, *parts: PathArg):
    if not parts:
      return pathlib.Path()
    full_path = '/'.join(parts)
    if full_path.startswith(('gs://')):
      return super().__new__(cls, full_path.replace('gs://', '/gs/', 1))
    if full_path.startswith(('/gs/')):
      return super().__new__(cls, *parts)
    else:
      return pathlib.Path(*parts)

  def __fpath__(self) -> str:
    return str(self)

  def __str__(self) -> str:
    value = super().__str__()
    if value.startswith('/gs/'):
      return value.replace('/gs/', 'gs://', 1)
    return value

  def exists(self) -> bool:
    return tf.io.gfile.exists(str(self))

  def iterdir(self) -> Iterator['GPath']:
    for f in tf.io.gfile.listdir(self):
      yield GPath(f)

  def is_dir(self) -> bool:
    """Returns True if self is a directory."""
    return tf.io.gfile.isdir(self)

  def glob(self, pattern: str) -> Iterator['GPath']:
    """Yielding all matching files (of any kind)."""
    # Might be able to implement using `iterdir` (recursivelly for `rglob`).
    path = os.path.join(str(self), pattern)

    for f in tf.io.gfile.glob(str(path)):
      yield GPath(f)

  def mkdir(
      self,
      mode: int = 0o777,
      parents: bool = False,
      exist_ok: bool = False,
  ) -> None:
    """Create a new directory at this given path."""
    if self.exists() and not exist_ok:
      raise FileExistsError(f'{str(self)} already exists.')

    if not self.is_dir():
      raise NotADirectoryError(f'{str(self)} is not a directory.')

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
    return tf.io.gfile.GFile(self, mode)

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



if __name__ == '__main__':

  PATH = "gs://tfds-data/datasets/mnist/3.0.0/"

  gpath = GPath(PATH)
  print(gpath.exists())

  f = gpath.glob("*json")
  print(list(f))