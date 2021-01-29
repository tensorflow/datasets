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

"""Module to use to extract archives. No business logic."""

import abc
import bz2
import concurrent.futures
import contextlib
import gzip
import io
import os
import tarfile
import typing
from typing import Iterator, Tuple
import uuid
import zipfile

from absl import logging
import promise
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import constants
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import resource as resource_lib


@utils.memoize()
def get_extractor(*args, **kwargs):
  return _Extractor(*args, **kwargs)


class ExtractError(Exception):
  """There was an error while extracting the archive."""


class UnsafeArchiveError(Exception):
  """The archive is unsafe to unpack, e.g. absolute path."""


class _Extractor(object):
  """Singleton (use `get_extractor()` module fct) to extract archives."""

  def __init__(self, max_workers=12):
    self._executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=max_workers)
    self._pbar_path = None

  @contextlib.contextmanager
  def tqdm(self):
    """Add a progression bar for the current extraction."""
    with utils.async_tqdm(
        total=0, desc='Extraction completed...', unit=' file') as pbar_path:
      self._pbar_path = pbar_path
      yield

  def extract(self, path, extract_method, to_path):
    """Returns `promise.Promise` => to_path."""
    path = os.fspath(path)
    to_path = os.fspath(to_path)
    if extract_method not in _EXTRACT_METHODS:
      raise ValueError('Unknown extraction method "%s".' % extract_method)
    future = self._executor.submit(
        self._sync_extract, path, extract_method, to_path
    )
    return promise.Promise.resolve(future)

  def _sync_extract(self, from_path, method, to_path):
    """Returns `to_path` once resource has been extracted there."""
    to_path_tmp = '%s%s_%s' % (to_path, constants.INCOMPLETE_SUFFIX,
                               uuid.uuid4().hex)
    path = None
    dst_path = None  # To avoid undefined variable if exception is raised
    try:
      arch_iter = iter_archive(from_path, method)
      self._pbar_path.update_total(len(arch_iter))
      for path, handle in arch_iter:
        path = tf.compat.as_text(path)
        dst_path = os.path.join(to_path_tmp, path) if path else to_path_tmp
        _copy(handle, dst_path)
        self._pbar_path.update(1)
    except BaseException as err:
      msg = 'Error while extracting {} to {} (file: {}) : {}'.format(
          from_path, to_path, path, err)
      # Check if running on windows
      if os.name == 'nt' and dst_path and len(dst_path) > 250:
        msg += (
            '\n'
            'On windows, path lengths greater than 260 characters may '
            'result in an error. See the doc to remove the limitation: '
            'https://docs.python.org/3/using/windows.html#removing-the-max-path-limitation'
        )
      raise ExtractError(msg) from err
    # `tf.io.gfile.Rename(overwrite=True)` doesn't work for non empty
    # directories, so delete destination first, if it already exists.
    if tf.io.gfile.exists(to_path):
      tf.io.gfile.rmtree(to_path)
    tf.io.gfile.rename(to_path_tmp, to_path)
    return utils.as_path(to_path)


def _copy(src_file, dest_path):
  """Copy data read from src file obj to new file in dest_path."""
  tf.io.gfile.makedirs(os.path.dirname(dest_path))
  with tf.io.gfile.GFile(dest_path, 'wb') as dest_file:
    while True:
      data = src_file.read(io.DEFAULT_BUFFER_SIZE)
      if not data:
        break
      dest_file.write(data)


def _normpath(path):
  path = os.path.normpath(path)
  if (path.startswith('.')
      or os.path.isabs(path)
      or path.endswith('~')
      or os.path.basename(path).startswith('.')):
    return None
  return path


@contextlib.contextmanager
def _open_or_pass(path_or_fobj):
  if isinstance(path_or_fobj, utils.PathLikeCls):
    with tf.io.gfile.GFile(path_or_fobj, 'rb') as f_obj:
      yield f_obj
  else:
    yield path_or_fobj


class _ArchiveIterator(abc.ABC):
  """
  Base iterator class for Archive files
  Also provides len() functionality
  """

  def __init__(self, arch_f):
    self._open_cm = _open_or_pass(arch_f)
    self.fobj = self._open_cm.__enter__()
    self._iter = self._iter_archive()

  def __iter__(self):
    return self

  def __next__(self):
    for path, extract_file in self._iter:
      return (path, extract_file)
    self._open_cm.__exit__(None, None, None)
    raise StopIteration

  @utils.memoize()
  def __len__(self) -> int:
    """Return no of files in this archive"""
    return self._get_num_files()

  @abc.abstractmethod
  def _get_num_files(self) -> int:
    """Return no of files in this archive"""

  @abc.abstractmethod
  def _iter_archive(self) -> Iterator[Tuple[str, typing.BinaryIO]]:
    """Return iterator which yields (path, extract_file_object) for all files"""


class _TarIterator(_ArchiveIterator):
  """ArchiveIterator for tar files"""

  def __init__(self, arch_f, stream=False):
    super().__init__(arch_f)
    self.stream = stream

    read_type = 'r' + ('|' if self.stream else ':') + '*'
    self.tar = tarfile.open(mode=read_type, fileobj=self.fobj)

  def _get_num_files(self) -> int:
    num_files = sum(1 for member in self.tar if member.isfile())
    if self.stream:
      # In stream mode, once we iterate over the file we can't go back
      # So instead of opening the file again, we seek to 0,
      # and reinstantiate the tar file
      self.fobj.seek(0)
      self.tar = tarfile.open(mode='r|*', fileobj=self.fobj)
    return num_files

  def _iter_archive(self) -> Iterator[Tuple[str, typing.BinaryIO]]:
    for member in self.tar:
      if self.stream and (member.islnk() or member.issym()):
        # Links cannot be dereferenced in stream mode.
        logging.warning('Skipping link during extraction: %s', member.name)
        continue

      try:
        extract_file = self.tar.extractfile(member)
      except KeyError:
        if not (member.islnk() or member.issym()):
          raise  # Forward exception non-link files which couldn't be extracted
        # The link could not be extracted, which likely indicates a corrupted
        # archive.
        logging.warning(
            'Skipping extraction of invalid link: %s -> %s',
            member.name,
            member.linkname,
        )
        continue

      if extract_file:  # File with data (not directory):
        path = _normpath(member.path)  # pytype: disable=attribute-error
        if not path:
          continue
        yield (path, extract_file)

def iter_tar(arch_f, stream=False):
  return _TarIterator(arch_f, stream)

def iter_tar_stream(arch_f):
  return _TarIterator(arch_f, stream=True)


class _GzipIterator(_ArchiveIterator):
  """ArchiveIterator for gzip(.gz) files"""

  def _get_num_files(self) -> int:
    return 1

  def _iter_archive(self) -> Iterator[Tuple[str, typing.BinaryIO]]:
    gzip_ = gzip.GzipFile(fileobj=self.fobj)
    yield ('', gzip_)  # No inner file.

def iter_gzip(arch_f):
  return _GzipIterator(arch_f)


class _Bzip2Iterator(_ArchiveIterator):
  """ArchiveIterator for bzip2(.bz2) files"""

  def _get_num_files(self) -> int:
    return 1

  def _iter_archive(self) -> Iterator[Tuple[str, typing.BinaryIO]]:
    bz2_ = bz2.BZ2File(filename=self.fobj)
    yield ('', bz2_)  # No inner file.

def iter_bzip2(arch_f):
  return _Bzip2Iterator(arch_f)


class _ZipIterator(_ArchiveIterator):
  """ArchiveIterator for zip files"""

  def __init__(self, arch_f):
    super().__init__(arch_f)
    self.z = zipfile.ZipFile(self.fobj)

  def _get_num_files(self) -> int:
    z = self.z
    num_files = sum(1 for member in z.infolist() if not member.is_dir())
    return num_files

  def _iter_archive(self) -> Iterator[Tuple[str, typing.BinaryIO]]:
    z = self.z
    for member in z.infolist():
      extract_file = z.open(member)
      if member.is_dir():  # pytype: disable=attribute-error
        # Filter directories
        continue
      path = _normpath(member.filename)
      if not path:
        continue
      yield (path, extract_file)

def iter_zip(arch_f):
  """Iterate over zip archive."""
  return _ZipIterator(arch_f)


_EXTRACT_METHODS = {
    resource_lib.ExtractMethod.BZIP2: iter_bzip2,
    resource_lib.ExtractMethod.GZIP: iter_gzip,
    resource_lib.ExtractMethod.TAR: iter_tar,
    resource_lib.ExtractMethod.TAR_GZ: iter_tar,
    resource_lib.ExtractMethod.TAR_GZ_STREAM: iter_tar_stream,
    resource_lib.ExtractMethod.TAR_STREAM: iter_tar_stream,
    resource_lib.ExtractMethod.ZIP: iter_zip,
}


def iter_archive(
    path: utils.PathLike,
    method: resource_lib.ExtractMethod,
) -> Iterator[Tuple[str, typing.BinaryIO]]:
  """Iterate over an archive.

  Args:
    path: `str`, archive path
    method: `tfds.download.ExtractMethod`, extraction method

  Returns:
    An iterator of `(path_in_archive, f_obj)`
  """
  if method == resource_lib.ExtractMethod.NO_EXTRACT:
    raise ValueError(
        f'Cannot `iter_archive` over {path}. Invalid or unrecognised archive.'
    )
  return _EXTRACT_METHODS[method](path)  # pytype: disable=bad-return-type
