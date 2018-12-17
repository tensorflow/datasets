# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Classes to specify download or extraction information."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import json
import os

import enum
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core.download import util
from tensorflow_datasets.core.utils import py_utils


class ExtractMethod(enum.Enum):
  """The extraction method to use to pre-process a downloaded file."""
  NO_EXTRACT = 1
  TAR = 2
  TAR_GZ = 3
  GZIP = 4
  ZIP = 5


_EXTRACTION_METHOD_TO_EXTS = [
    (ExtractMethod.TAR_GZ, ['.tar.gz', '.tgz']),
    (ExtractMethod.TAR, ['.tar', '.tar.bz2', '.tbz2', '.tbz', '.tb2']),
    (ExtractMethod.ZIP, ['.zip']),
    (ExtractMethod.GZIP, ['.gz']),
]


def _guess_extract_method(fname):
  """Guess extraction method, given file name (or path)."""
  for method, extensions in _EXTRACTION_METHOD_TO_EXTS:
    for ext in extensions:
      if fname.endswith(ext):
        return method
  return ExtractMethod.NO_EXTRACT


class Resource(object):
  """Represents a resource to download, extract, or both."""

  @api_utils.disallow_positional_args()
  def __init__(self,
               url=None,
               extract_method=None,
               path=None):
    """Resource constructor.

    Args:
      url: `str`, the URL at which to download the resource.
      extract_method: `ExtractMethod` to be used to extract resource. If
        not set, will be guessed from downloaded file name `original_fname`.
      path: `str`, path of resource on local disk. Can be None if resource has
        not be downloaded yet. In such case, `url` must be set.
    """
    self.url = url
    self.path = path
    self._extract_method = extract_method
    self._fname = None
    self._original_fname = None  # Name of the file as downloaded.
    self._info = None  # The INFO dict, once known.

  @property
  def fname(self):
    """Name of downloaded file (not as downloaded, but as stored)."""
    if self.path:
      return os.path.basename(self.path)
    if not self._fname:
      self._fname = hashlib.sha256(self.url.encode('utf8')).hexdigest()
    return self._fname

  @property
  def extract_fname(self):
    """Name of extracted archive (file or directory)."""
    return '%s.%s' % (self.extract_method_name, self.fname)

  @property
  def extract_method(self):
    """Returns `ExtractMethod` to use on resource. Cannot be None."""
    if not self._extract_method:
      self._extract_method = _guess_extract_method(
          # no original_fname if extract is called directly (no URL).
          self._get_info() and self._get_original_fname() or self.fname)
    return self._extract_method

  @property
  def extract_method_name(self):
    """Returns the name (`str`) of the extraction method."""
    return ExtractMethod(self.extract_method).name

  @property
  def info_path(self):
    """Returns path (`str`) of INFO file associated with resource."""
    return '%s.INFO' % self.path

  def _get_info(self):
    """Returns info dict or None."""
    if not self._info:
      if not tf.gfile.Exists(self.info_path):
        tf.logging.info('INFO file %s not found.' % self.info_path)
        return None
      tf.logging.info('Reading INFO file %s ...' % self.info_path)
      with tf.gfile.Open(self.info_path) as info_f:
        self._info = json.load(info_f)
    return self._info

  def exists_locally(self):
    """Returns whether the resource exists locally, at `resource.path`."""
    # If INFO file doesn't exist, consider resource does NOT exist, as it would
    # prevent guessing the `extract_method`.
    return tf.gfile.Exists(self.path) and tf.gfile.Exists(self.info_path)

  def _get_original_fname(self):
    # We rely on the INFO file because some urls (eg: drive) do not contain the
    # name of original file.
    info = self._get_info()
    if not info:
      raise AssertionError('INFO file %s doe not exist.' % self.info_path)
    return info['original_fname']

  # TODO(pierrot): one lock per info path instead of locking everything.
  @util.build_synchronize_decorator()
  def write_info_file(self, dataset_name, original_fname):
    """Write the INFO file next to local file.

    Although the method is synchronized, there is still a risk two processes
    running at the same time overlap here. Risk accepted, since potentially lost
    data (`dataset_name`) is only for human consumption.

    Args:
      dataset_name: data used to dl the file.
      original_fname: name of file as downloaded.
    """
    info = self._get_info() or {}
    urls = set(info.get('urls', []) + [self.url])
    dataset_names = set(info.get('dataset_names', []) + [dataset_name])
    if 'original_fname' in info and info['original_fname'] != original_fname:
      raise AssertionError(
          '`original_fname` "%s" stored in %s does NOT match "%s".' % (
              info['original_fname', self.info_path, original_fname]))
    info = dict(urls=list(urls), dataset_names=list(dataset_names),
                original_fname=original_fname)
    tf.logging.info('Writing INFO file %s ...' % self.info_path)
    with py_utils.atomic_write(self.info_path, 'w') as info_f:
      json.dump(info, info_f, sort_keys=True)
    self._info = info
