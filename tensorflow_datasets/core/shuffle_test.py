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

"""Tests for tensorflow_datasets.core.shuffle."""

import collections
import contextlib
import logging
import resource
import tempfile

from absl.testing.absltest import mock
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import shuffle
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

_ITEMS = [
    (1, b'The'),
    (2, b'quick '),
    (3, b'brown'),
    (4, b' fox '),
    (5, b'jumps'),
    ('6', b'over'),
    (b'7', b' the '),
    (8, b'lazy'),
    (9, b' dog.'),
]

_ORDERED_ITEMS_SPLIT1 = [
    b' fox ',
    b'The',
    b'over',
    b'quick ',
    b'lazy',
    b'jumps',
    b' the ',
    b' dog.',
    b'brown',
]

_ORDERED_ITEMS_SPLIT2 = [
    b' dog.',
    b'quick ',
    b'jumps',
    b' fox ',
    b' the ',
    b'brown',
    b'over',
    b'lazy',
    b'The',
]

_SORTED_ITEMS = [
    (1, b'The'),
    (2, b'quick '),
    (3, b'brown'),
    (4, b' fox '),
    (5, b'jumps'),
    (6, b'over'),
    (7, b' the '),
    (8, b'lazy'),
    (9, b' dog.'),
]

_TOTAL_SIZE = sum(len(rec) for rec in _ORDERED_ITEMS_SPLIT1)


@contextlib.contextmanager
def disable_opening_files():
  """Context manager to disable opening new files."""
  soft_limit, hard_limit = resource.getrlimit(resource.RLIMIT_NOFILE)
  try:
    resource.setrlimit(resource.RLIMIT_NOFILE, (1, hard_limit))
    yield
  finally:
    resource.setrlimit(resource.RLIMIT_NOFILE, (soft_limit, hard_limit))


@pytest.mark.parametrize(
    [
        'num_keys',
        'num_buckets',
        'max_hkey',
        'expected_non_empty_shards',
        'expected_min_bucket_size',
        'expected_max_bucket_size',
    ],
    [
        (10, 2, 9, 2, 5, 5),
        (10, 3, 9, 3, 3, 4),
        (1024, 10, 1023, 10, 102, 103),
        (10, 2, 99, 1, 0, 10),
    ],
)
def test_get_bucket_number(
    num_keys,
    num_buckets,
    max_hkey,
    expected_non_empty_shards,
    expected_min_bucket_size,
    expected_max_bucket_size,
):
  shards = [
      shuffle.get_bucket_number(
          hkey=k, num_buckets=num_buckets, max_hkey=max_hkey
      )
      for k in range(num_keys)
  ]
  # Check shard(x) <= shard(y) if x < y.
  previous_shard = 0
  for shard in shards:
    assert shard >= previous_shard
    previous_shard = shard
  # Check distribution: all shards are used.
  counts = collections.Counter(shards)
  assert len(counts) == expected_non_empty_shards
  for bucket_size in counts.values():
    assert bucket_size >= expected_min_bucket_size
    assert bucket_size <= expected_max_bucket_size


def test_get_bucket_number_large_hkey():
  bucket = shuffle.get_bucket_number(
      hkey=314755909755515592000481005244904880883,
      num_buckets=5,
      max_hkey=314755909755515592000481005244904880883,
  )
  assert bucket == 4


def test_increase_open_files_limit(caplog):
  with disable_opening_files():
    with pytest.raises(OSError) as exc_info:
      tempfile.TemporaryFile()
    assert exc_info.value.strerror == 'Too many open files'

    shuffle._increase_open_files_limit()
    assert caplog.record_tuples == [(
        'absl',
        logging.WARNING,
        (
            'Soft limit for the maximum number of open file descriptors for the'
            ' current process increased from 1 to 1001'
        ),
    )]
    tempfile.TemporaryFile()

  _, hard_limit = resource.getrlimit(resource.RLIMIT_NOFILE)
  resource.setrlimit(resource.RLIMIT_NOFILE, (hard_limit, hard_limit))
  caplog.clear()
  shuffle._increase_open_files_limit()
  assert caplog.record_tuples == [(
      'absl',
      logging.ERROR,
      (
          'Soft and hard limits for the maximum number of open file descriptors'
          ' for the current process are identical.'
      ),
  )]


def test_shuffler_with_limited_open_files(tmp_path, monkeypatch, caplog):
  monkeypatch.setattr(shuffle, 'MAX_MEM_BUFFER_SIZE', 0)
  shuffler = shuffle.Shuffler(tmp_path, 'salt', disable_shuffling=False)
  # trigger Tensorflow imports before disabling opening files
  tf.io.gfile.GFile  # pylint: disable=pointless-statement
  tf.errors.ResourceExhaustedError  # pylint: disable=pointless-statement

  with disable_opening_files():
    shuffler.add(1, b'The')

  assert caplog.record_tuples == [(
      'absl',
      logging.WARNING,
      (
          'Soft limit for the maximum number of open file descriptors for the'
          ' current process increased from 1 to 1001'
      ),
  )]


class ShuffleTest(testing.TestCase):

  def _test_items(self, salt, items, expected_order, disable_shuffling=False):
    shuffler = shuffle.Shuffler(self.get_temp_dir(), salt, disable_shuffling)
    for key, item in items:
      shuffler.add(key, item)
    self.assertEqual(shuffler.size, _TOTAL_SIZE)
    if not shuffler._in_memory:  # Check size of temporary bucket files
      expected_size = (16 + 8) * len(items) + sum(len(t[1]) for t in items)
      size = 0
      for bucket in shuffler._buckets:
        if not bucket._fobj:
          continue
        bucket._fobj.close()
        with open(bucket._path, 'rb') as f:
          size += len(f.read())
      self.assertEqual(size, expected_size)
    # Check records can be read as expected:
    records = list(ex for _, ex in shuffler)
    self.assertEqual(records, expected_order)

  def test_all_mem(self):
    self._test_items('split1', _ITEMS, _ORDERED_ITEMS_SPLIT1)
    self._test_items('split2', _ITEMS, _ORDERED_ITEMS_SPLIT2)

  @mock.patch.object(shuffle, 'MAX_MEM_BUFFER_SIZE', 0)
  def test_disk(self):
    self._test_items('split1', _ITEMS, _ORDERED_ITEMS_SPLIT1)
    self._test_items('split2', _ITEMS, _ORDERED_ITEMS_SPLIT2)

  def test_sorted_by_key(self):
    self._test_items(
        'split1',
        _SORTED_ITEMS,
        [value for _, value in _SORTED_ITEMS],
        disable_shuffling=True,
    )

  def test_nonbytes(self):
    shuffler = shuffle.Shuffler(self.get_temp_dir(), 'split1')
    with self.assertRaisesWithPredicateMatch(AssertionError, 'Only bytes'):
      shuffler.add(1, 'a')
    with self.assertRaisesWithPredicateMatch(AssertionError, 'Only bytes'):
      shuffler.add(1, 123)

  def test_duplicate_key(self):
    shuffler = shuffle.Shuffler(self.get_temp_dir(), 'split1')
    shuffler.add(1, b'a')
    shuffler.add(2, b'b')
    shuffler.add(1, b'c')
    iterator = iter(shuffler)
    self.assertEqual(
        next(iterator), (86269847664267119453139349052967691808, b'a')
    )
    with self.assertRaises(shuffle.DuplicatedKeysError):
      next(iterator)


if __name__ == '__main__':
  testing.test_main()
