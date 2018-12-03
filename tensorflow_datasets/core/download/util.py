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

"""Utils functions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import hashlib
import io
import os
import threading

import enum
from six.moves import urllib

import tensorflow as tf


class GenerateMode(enum.Enum):
  """Enum for the different version conflict resolution modes."""

  # The generations modes:
  #                          |     Cache     |    Dataset
  # -----------------------------------------------
  # Reuse dataset if exists  |     Reuse     |     Reuse
  # Reuse cache if exists    |     Reuse     |  New version
  # Force Re-Download        |  Re-download  |  New version

  # Generate a new version of the dataset from scratch (download included)
  FORCE_REDOWNLOAD = 'force_redownload'
  # Generate a new version of the dataset, but reuse cached downloads if
  # they exists
  REUSE_CACHE_IF_EXISTS = 'reuse_cache_if_exists'
  # Do nothing if the dataset already exists (default mode)
  REUSE_DATASET_IF_EXISTS = 'reuse_dataset_if_exists'


# TODO(epot): Move some of those functions into core.py_utils


def build_synchronize_decorator():
  """Returns a decorator which prevent concurents calls to functions.

  Usage:
    synchronized = build_synchronize_decorator()

    @synchronized
    def read_value():
      ...

    @synchronized
    def write_value(x):
      ...

  Returns:
    make_threadsafe (fct): The decorator which lock all functions to which it
      is applied under a same lock
  """
  lock = threading.Lock()

  def lock_decorator(fn):

    @functools.wraps(fn)
    def lock_decorated(*args, **kwargs):
      with lock:
        return fn(*args, **kwargs)

    return lock_decorated

  return lock_decorator


def get_file_name(url):
  """Returns file name of file at given url."""
  return os.path.basename(urllib.parse.urlparse(url).path) or 'unknown_name'


def read_checksum_digest(path, checksum_cls=hashlib.sha256):
  """Given a hash constructor, returns checksum digest of file at path."""
  checksum = checksum_cls()
  with tf.gfile.Open(path, 'rb') as f:
    while True:
      block = f.read(io.DEFAULT_BUFFER_SIZE)
      if not block:
        break
      checksum.update(block)
  return checksum.hexdigest()
