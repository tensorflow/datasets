# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import gzip
import io
import os
import tarfile
import uuid
import zipfile

import concurrent.futures
import promise
import six
import tensorflow as tf

from tensorflow_datasets.core import constants
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import resource as resource_lib

if six.PY3:
  import bz2  # pylint:disable=g-import-not-at-top
else:
  # py2's built-in bz2 package does not support reading from file objects.
  import bz2file as bz2  # pylint:disable=g-import-not-at-top


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
    self._pbar_path.update_total(1)
    if extract_method not in _EXTRACT_METHODS:
      raise ValueError('Unknown extraction method "%s".' % extract_method)
    future = self._executor.submit(self._sync_extract,
                                   path, extract_method, to_path)
    return promise.Promise.resolve(future)

  def _sync_extract(self, from_path, method, to_path):
    """Returns `to_path` once resource has been extracted there."""
    to_path_tmp = '%s%s_%s' % (to_path, constants.INCOMPLETE_SUFFIX,
                               uuid.uuid4().hex)
    try:
      for path, handle in iter_archive(from_path, method):
        _copy(handle, path and os.path.join(to_path_tmp, path) or to_path_tmp)
    except BaseException as err:
      msg = 'Error while extracting %s to %s : %s' % (from_path, to_path, err)
      raise ExtractError(msg)
    # `tf.io.gfile.Rename(overwrite=True)` doesn't work for non empty
    # directories, so delete destination first, if it already exists.
    if tf.io.gfile.exists(to_path):
      tf.io.gfile.rmtree(to_path)
    tf.io.gfile.rename(to_path_tmp, to_path)
    self._pbar_path.update(1)
    return to_path


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
  if path.startswith('.') or os.path.isabs(path):
    raise UnsafeArchiveError('Archive at %s is not safe.' % path)
  if path.endswith('~') or os.path.basename(path).startswith('.'):
    return None
  return path


@contextlib.contextmanager
def _open_or_pass(path_or_fobj):
  if isinstance(path_or_fobj, six.string_types):
    with tf.io.gfile.GFile(path_or_fobj, 'rb') as f_obj:
      yield f_obj
  else:
    yield path_or_fobj


def iter_tar(arch_f, gz=False):
  """Iter over tar archive, yielding (path, object-like) tuples."""
  read_type = 'r:gz' if gz else 'r:'
  with _open_or_pass(arch_f) as fobj:
    tar = tarfile.open(mode=read_type, fileobj=fobj)
    for member in tar.getmembers():
      extract_file = tar.extractfile(member)
      if extract_file:  # File with data (not directory):
        path = _normpath(member.path)
        if not path:
          continue
        yield [path, extract_file]


def iter_tar_gz(arch_f):
  return iter_tar(arch_f, gz=True)


def iter_gzip(arch_f):
  with _open_or_pass(arch_f) as fobj:
    gzip_ = gzip.GzipFile(fileobj=fobj)
    yield ('', gzip_)  # No inner file.


def iter_bzip2(arch_f):
  with _open_or_pass(arch_f) as fobj:
    bz2_ = bz2.BZ2File(filename=fobj)
    yield ('', bz2_)  # No inner file.


def iter_zip(arch_f):
  with _open_or_pass(arch_f) as fobj:
    z = zipfile.ZipFile(fobj)
    for member in z.infolist():
      extract_file = z.open(member)
      if extract_file:  # File with data (not directory):
        path = _normpath(member.filename)
        if not path:
          continue
        yield [path, extract_file]


_EXTRACT_METHODS = {
    resource_lib.ExtractMethod.TAR: iter_tar,
    resource_lib.ExtractMethod.TAR_GZ: iter_tar_gz,
    resource_lib.ExtractMethod.GZIP: iter_gzip,
    resource_lib.ExtractMethod.ZIP: iter_zip,
    resource_lib.ExtractMethod.BZIP2: iter_bzip2,
}


def iter_archive(path, method):
  """Yields (path_in_archive, f_obj) for archive at path using `tfds.download.ExtractMethod`."""  # pylint: disable=line-too-long
  return _EXTRACT_METHODS[method](path)
