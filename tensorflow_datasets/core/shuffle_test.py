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

"""Tests for tensorflow_datasets.core.shuffle."""

import collections

from absl.testing.absltest import mock
from tensorflow_datasets import testing
from tensorflow_datasets.core import shuffle

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


class GetShardTest(testing.TestCase):

  @mock.patch.object(shuffle, 'HKEY_SIZE', 10)  # 1024 keys.
  def test_order(self):
    shards_number = 10
    shards = [shuffle.get_bucket_number(k, shards_number) for k in range(1024)]
    # Check max(shard_x) < min(shard_y) if x < y.
    previous_shard = 0
    for shard in shards:
      self.assertGreaterEqual(shard, previous_shard)
      previous_shard = shard
    # Check distribution: all shards are used.
    counts = collections.Counter(shards)
    self.assertEqual(len(counts), shards_number)
    # And all shards contain same number of elements (102 or 102 in that case).
    self.assertEqual(len(set(counts.values())), 2)


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
        _SORTED_ITEMS, [value for key, value in _SORTED_ITEMS],
        disable_shuffling=True)

  def test_nonbytes(self):
    shuffler = shuffle.Shuffler(self.get_temp_dir(), 'split1')
    with self.assertRaisesWithPredicateMatch(AssertionError, 'Only bytes'):
      shuffler.add(1, u'a')
    with self.assertRaisesWithPredicateMatch(AssertionError, 'Only bytes'):
      shuffler.add(1, 123)

  def test_duplicate_key(self):
    shuffler = shuffle.Shuffler(self.get_temp_dir(), 'split1')
    shuffler.add(1, b'a')
    shuffler.add(2, b'b')
    shuffler.add(1, b'c')
    iterator = iter(shuffler)
    self.assertEqual(
        next(iterator), (86269847664267119453139349052967691808, b'a'))
    with self.assertRaises(shuffle.DuplicatedKeysError):
      next(iterator)


if __name__ == '__main__':
  testing.test_main()
