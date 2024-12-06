# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from collections.abc import Iterator, Sequence
import math
import os
import struct
from typing import Optional
import uuid
from absl import logging
from etils import epath
from tensorflow_datasets.core import hashing
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

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

HKEY_SIZE = 128  # Hash of keys is 128 bits (md5).
HKEY_SIZE_BYTES = HKEY_SIZE // 8


class DuplicatedKeysError(Exception):

  def __init__(self, item1, item2):
    super(DuplicatedKeysError, self).__init__()
    self.item1 = item1
    self.item2 = item2


def _hkey_to_bytes(hkey: int) -> bytes:
  """Converts 128 bits integer hkey to binary representation."""
  max_int64 = 0xFFFFFFFFFFFFFFFF
  return struct.pack('=QQ', (hkey >> 64) & max_int64, hkey & max_int64)


def _read_hkey(buff: bytes) -> int:
  """Reads from fobj and returns hkey (128 bits integer)."""
  a, b = struct.unpack('=QQ', buff)
  return (a << 64) | b


def _increase_open_files_limit():
  """Attempts to increase the maximum number of open file descriptors on UNIX."""
  try:
    import resource  # pylint: disable=g-import-not-at-top
  except ModuleNotFoundError:
    logging.error(
        "Missing `resource` module, can't automatically increase the maximum"
        ' number of open file descriptors on your system. Try increasing it'
        ' manually.'
    )
    return

  soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_NOFILE)
  if soft_limit < hard_limit:
    new_soft_limit = min(soft_limit + BUCKETS_NUMBER, hard_limit)
    resource.setrlimit(resource.RLIMIT_NOFILE, (new_soft_limit, hard_limit))
    logging.warning(
        'Soft limit for the maximum number of open file descriptors for'
        ' the current process increased from %d to %d',
        soft_limit,
        new_soft_limit,
    )
  else:
    logging.error(
        'Soft and hard limits for the maximum number of open file descriptors'
        ' for the current process are identical.'
    )


def get_bucket_number(
    hkey: int,
    num_buckets: int,
    max_hkey: Optional[int] = None,
) -> int:
  """Returns bucket (shard) number (int) for given hashed key (int)."""
  # We purposely do not use modulo (%) to keep global order across shards.
  # floor(key * num_buckets / HKEYS_NUMBER), with HKEYS_NUMBER = 2**HKEY_SIZE.
  max_hkey = max_hkey or 2**HKEY_SIZE
  # Make sure that we do not return `bucket_number`.
  return min(math.trunc((hkey * num_buckets) / max_hkey), num_buckets - 1)


class _Bucket(object):
  """Holds (key, binary value) tuples to disk, fast.

  Bucket instances are designed to be used either:
    1. Many buckets are written in parallel, then they are read one by one. When
    reading, the data can be fully loaded in memory to be sorted.
    This is how buckets are currently used in Shuffler.
    2. Buckets are being written one at a time (or on different machines/jobs).
    Before writing the data, it is sorted in memory. Many bucket are read in
    parallel.
    This is not currently used, but could be if we decide do parallelize the
    writing of final sharded tfrecord files.

  File format (assuming a key of 16 bytes):
    key1 (16 bytes) | size1 (8 bytes) | data1 (size1 bytes) |
    key2 (16 bytes) | size2 (8 bytes) | data2 (size2 bytes) |
    ...
  """

  def __init__(self, path: epath.Path):
    """Initialize a _Bucket instance.

    Args:
      path: Path to bucket file, where to write to or read from.
    """
    self._path = path
    self._fobj = None
    self._length = 0
    self._size = 0

  @property
  def size(self) -> int:
    return self._size

  def __len__(self) -> int:
    return self._length

  def add(self, key: type_utils.Key, data: bytes):
    """Adds (key, data) to bucket.

    Args:
      key (int): the key.
      data (binary): the data.
    """
    if not self._fobj:
      file_utils.makedirs_cached(os.path.dirname(self._path))
      self._fobj = tf.io.gfile.GFile(self._path, mode='wb')
    data_size = len(data)

    try:
      self._fobj.write(_hkey_to_bytes(key))
    except tf.errors.ResourceExhaustedError as error:
      # catch "Too many open files"
      if error.message.endswith('Too many open files'):
        _increase_open_files_limit()
        self._fobj.write(_hkey_to_bytes(key))
      else:
        raise error
    # http://docs.python.org/3/library/struct.html#byte-order-size-and-alignment
    # The equal sign ("=") is important here, has it guarantees the standard
    # size (Q: 8 bytes) is used, as opposed to native size, which can differ
    # from one platform to the other. This way we know exactly 8 bytes have been
    # written, and we can read that same amount of bytes later.
    # We do not specify endianess (platform dependent), but this is OK since the
    # temporary files are going to be written and read by the same platform.
    self._fobj.write(struct.pack('=Q', data_size))
    self._fobj.write(data)
    self._length += 1
    self._size += data_size

  def flush(self):
    if self._fobj:
      self._fobj.flush()
      self._fobj.close()

  def read_values(self):
    """Yields (hkey, data) tuples stored in bucket."""
    self.flush()
    path = self._path
    if not tf.io.gfile.exists(path):
      # In case bucket was created but nothing was ever added.
      # This is likely to happen if the number of buckets is large compared to
      # the number of generated examples.
      return
    with tf.io.gfile.GFile(path, 'rb') as fobj:
      while True:
        buff = fobj.read(HKEY_SIZE_BYTES)
        if not buff:
          break
        hkey = _read_hkey(buff)
        size_bytes = fobj.read(8)
        size = struct.unpack('=Q', size_bytes)[0]
        data = fobj.read(size)
        yield hkey, data

  def del_file(self):
    if tf.io.gfile.exists(self._path):
      tf.io.gfile.remove(self._path)


class Shuffler(object):
  """Stores data in temp buckets, restitute it shuffled."""

  def __init__(
      self,
      dirpath: epath.PathLike,
      hash_salt: str | bytes,
      disable_shuffling: bool = False,
      ignore_duplicates: bool = False,
  ):
    """Initialize Shuffler.

    Args:
      dirpath: Path to the directory in which to store temporary files.
      hash_salt: Salt to hash keys.
      disable_shuffling: Specifies whether to shuffle by hashing the key.
      ignore_duplicates: Whether to ignore duplicated examples with the same
        key. If there are multiple examples with the same key, the first one is
        kept. If this is False, then a `DuplicatedKeysError` is raised.
    """
    grp_name = uuid.uuid4()
    self._hasher = hashing.Hasher(hash_salt)
    self._disable_shuffling = disable_shuffling
    self._ignore_duplicates = ignore_duplicates
    self._buckets: list[_Bucket] = []
    for i in range(BUCKETS_NUMBER):
      bucket_name = 'bucket_%s_%03d.tmp' % (grp_name, i)
      path = epath.Path(dirpath) / bucket_name
      self._buckets.append(_Bucket(path))
    self._read_only = False
    self._total_bytes = 0
    # To keep data in memory until enough data has been gathered.
    self._in_memory = True
    self._mem_buffer = []
    self._seen_keys: set[int] = set()
    self._num_examples = 0

  @property
  def size(self) -> int:
    """Return total size in bytes of records (not keys)."""
    return self._total_bytes

  @property
  def bucket_lengths(self) -> Sequence[int]:
    if self._in_memory:
      return [len(self._mem_buffer)]
    return [len(b) for b in self._buckets]

  @property
  def num_examples(self) -> int:
    return self._num_examples

  def _add_to_bucket(self, hkey: int, data: bytes) -> None:
    bucket_number = get_bucket_number(hkey=hkey, num_buckets=BUCKETS_NUMBER)
    self._buckets[bucket_number].add(hkey, data)

  def _add_to_mem_buffer(self, hkey: int, data: bytes) -> None:
    self._mem_buffer.append((hkey, data))
    if self._total_bytes > MAX_MEM_BUFFER_SIZE:
      for hkey, data in self._mem_buffer:
        self._add_to_bucket(hkey, data)
      self._mem_buffer = None
      self._in_memory = False

  def add(self, key: type_utils.Key, data: bytes) -> bool:
    """Add (key, data) to shuffler."""
    if self._read_only:
      raise AssertionError('add() cannot be called after __iter__.')
    if not isinstance(data, bytes):
      raise AssertionError(
          f'Only bytes (not {type(data)}) can be stored in Shuffler!'
      )
    hkey = self._hasher.hash_key(key)
    if self._ignore_duplicates:
      if hkey in self._seen_keys:
        return  # pytype: disable=bad-return-type
      self._seen_keys.add(hkey)
    if self._disable_shuffling:
      # Use the original key and not the hashed key to maintain the order.
      hkey = key
    self._total_bytes += len(data)
    if self._in_memory:
      self._add_to_mem_buffer(hkey, data)
    else:
      self._add_to_bucket(hkey, data)
    self._num_examples += 1  # pytype: disable=bad-return-type

  def __iter__(self) -> Iterator[type_utils.KeySerializedExample]:
    self._read_only = True
    previous_hkey = None
    previous_data = None
    iterator = self._iter_mem() if self._in_memory else self._iter_buckets()
    for hkey, data in iterator:
      if hkey == previous_hkey:
        raise DuplicatedKeysError(data, previous_data)
      previous_hkey = hkey
      yield hkey, data
      previous_data = data

  def _iter_mem(self):
    for hkey, data in sorted(self._mem_buffer):
      yield hkey, data

  def _iter_buckets(self):
    for bucket in self._buckets:
      bucket_data = sorted(bucket.read_values())
      bucket.del_file()
      for hkey, data in bucket_data:
        yield hkey, data
