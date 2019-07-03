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

"""Tests for tensorflow_datasets.core.shuffle."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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

_ORDERED_ITEMS = [
    b' dog.',
    b'over',
    b'brown',
    b'The',
    b' fox ',
    b' the ',
    b'lazy',
    b'quick ',
    b'jumps',
]

_TOTAL_SIZE = sum(len(rec) for rec in _ORDERED_ITEMS)


class GetShardTest(testing.TestCase):

  @mock.patch.object(shuffle, 'HKEY_SIZE', 10)  # 1024 keys.
  def test_order(self):
    shards_number = 10
    shards = [shuffle._get_shard(k, shards_number) for k in range(1024)]
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

  def test_all_mem(self):
    shuffler = shuffle.Shuffler(self.get_temp_dir())
    for key, item in _ITEMS:
      shuffler.add(key, item)
    self.assertEqual(shuffler.size, _TOTAL_SIZE)
    records = list(iter(shuffler))
    self.assertEqual(records, _ORDERED_ITEMS)

  @mock.patch.object(shuffle, 'MAX_MEM_BUFFER_SIZE', 0)
  def test_disk(self):
    self.test_all_mem()

  def test_nonbytes(self):
    shuffler = shuffle.Shuffler(self.get_temp_dir())
    with self.assertRaisesWithPredicateMatch(AssertionError, 'Only bytes'):
      shuffler.add(1, u'a')
    with self.assertRaisesWithPredicateMatch(AssertionError, 'Only bytes'):
      shuffler.add(1, 123)

  def test_duplicate_key(self):
    shuffler = shuffle.Shuffler(self.get_temp_dir())
    shuffler.add(1, b'a')
    shuffler.add(2, b'b')
    shuffler.add(1, b'c')
    iterator = iter(shuffler)
    self.assertEqual(next(iterator), b'a')
    with self.assertRaisesWithPredicateMatch(
        AssertionError, 'Two records share the same hashed key!'):
      next(iterator)


if __name__ == '__main__':
  testing.test_main()
