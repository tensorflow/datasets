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

"""To shuffle records (stable)."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import os
import struct
import uuid

import six
import tensorflow as tf

from tensorflow_datasets.core import hashing

HKEY_SIZE = 64  # Hash of keys is 64 bits.

# Approximately how much data to store in memory before writing to disk.
# If the amount of data to shuffle is < MAX_MEM_BUFFER_SIZE, no intermediary
# data is written to disk.
MAX_MEM_BUFFER_SIZE = 1000 << 20  # 1GB

# If data to shuffle is too large for memory. Records are split among 1K
# buckets stored on disk, then each bucket is sorted in memory.
# For a dataset split of about 1TB, each bucket is going to
# be about 1GB. Larger datasets will likely be handled by Beam.
#
# Increasing the number of buckets would decrease the size of each bucket.
# Current implementation relies on having one open file per bucket.
# Windows has a limit of ~2K open files per process (Linux ~32K); so increasing
# the number of buckets might warrant some changes in implementation.
BUCKETS_NUMBER = 1000  # Number of buckets to pre-sort and hold generated data.


def _get_shard(hkey, shards_number):
  """Returns shard number (int) for given hashed key (int)."""
  # We purposely do not use modulo (%) to keep global order across shards.
  # floor(key * shards_number / HKEYS_NUMBER), with HKEYS_NUMBER = 2**HKEY_SIZE.
  return math.trunc((hkey * shards_number)>>HKEY_SIZE)


class _Bucket(object):
  """Holds (8 bytes key, binary value) tuples to disk, fast.

  The assumption is that many _Bucket instances will be written in parallel,
  while only one will be read at any given time, and a full _Bucket data can
  hold in memory. Data is written once and read once.

  File format:
    key1 (8 bytes) | size1 (8 bytes) | data1 (size1 bytes) |
    key2 (8 bytes) | size2 (8 bytes) | data2 (size2 bytes) |
    ...
  """

  def __init__(self, path):
    """Initialize a _Bucket instance.

    Args:
      path (str): where to write the bucket file.
    """
    self._path = path
    self._fobj = None
    self._length = 0
    self._size = 0

  @property
  def size(self):
    return self._size

  def add(self, key, data):
    """Adds (key, data) to bucket.

    Args:
      key (int): the key.
      data (binary): the data.
    """
    if not self._fobj:
      self._fobj = tf.io.gfile.GFile(self._path, mode='wb')
    data_size = len(data)
    self._fobj.write(struct.pack('LL', key, data_size))
    self._fobj.write(data)
    self._length += 1
    self._size += data_size

  def read_values(self):
    """Returns all data stored in bucket as a list of (hkey, data) tuples."""
    if not self._fobj:
      return []  # Nothing was written to this bucket.
    self._fobj.close()
    path = self._path
    res = []
    with tf.io.gfile.GFile(path, 'rb') as fobj:
      while True:
        buff = fobj.read(16)
        if not buff:
          break
        hkey, size = struct.unpack('LL', buff)
        data = fobj.read(size)
        res.append((hkey, data))
    return res

  def del_file(self):
    if tf.io.gfile.exists(self._path):
      tf.io.gfile.remove(self._path)


class Shuffler(object):
  """Stores data in temp buckets, restitute it shuffled.

  Args:
    dirpath: directory in which to store temporary files.
  """

  def __init__(self, dirpath):
    grp_name = uuid.uuid4()
    self._buckets = [
        _Bucket(os.path.join(dirpath, 'bucket_%s_%03d.tmp' % (grp_name, i)))
        for i in range(BUCKETS_NUMBER)]
    self._read_only = False
    self._total_bytes = 0
    # To keep data in memory until enough data has been gathered.
    self._in_memory = True
    self._mem_buffer = []

  @property
  def size(self):
    """Return total size in bytes of records (not keys)."""
    return self._total_bytes

  def _add_to_bucket(self, hkey, data):
    bucket_number = _get_shard(hkey, BUCKETS_NUMBER)
    self._buckets[bucket_number].add(hkey, data)

  def _add_to_mem_buffer(self, hkey, data):
    self._mem_buffer.append((hkey, data))
    if self._total_bytes > MAX_MEM_BUFFER_SIZE:
      for hkey, data  in self._mem_buffer:
        self._add_to_bucket(hkey, data)
      self._mem_buffer = None
      self._in_memory = False

  def add(self, key, data):
    """Add (key, data) to shuffler."""
    if self._read_only:
      raise AssertionError('add() cannot be called after __iter__.')
    if not isinstance(data, six.binary_type):
      raise AssertionError('Only bytes (not %s) can be stored in Shuffler!' % (
          type(data)))
    hkey = hashing.hash_key(key)
    self._total_bytes += len(data)
    if self._in_memory:
      self._add_to_mem_buffer(hkey, data)
    else:
      self._add_to_bucket(hkey, data)

  def __iter__(self):
    self._read_only = True
    previous_hkey = None
    iterator = self._iter_mem() if self._in_memory else self._iter_buckets()
    for hkey, data in iterator:
      if hkey == previous_hkey:
        raise AssertionError('Two records share the same hashed key!')
      previous_hkey = hkey
      yield data

  def _iter_mem(self):
    for hkey, data in sorted(self._mem_buffer):
      yield hkey, data

  def _iter_buckets(self):
    for bucket in self._buckets:
      bucket_data = sorted(bucket.read_values())
      bucket.del_file()
      for hkey, data in bucket_data:
        yield hkey, data
