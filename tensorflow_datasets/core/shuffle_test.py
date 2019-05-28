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

from absl.testing.absltest import mock
from tensorflow_datasets import testing
from tensorflow_datasets.core import shuffle

_ITEMS = [
    (1, b'The quick brown fox'),
    ('2', b'jumps over'),
    (b'3', b'the lazy dog'),
]

_ORDERED_ITEMS = [
    b'jumps over',
    b'The quick brown fox',
    b'the lazy dog',
]

_TOTAL_SIZE = sum(len(rec) for rec in _ORDERED_ITEMS)


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


if __name__ == '__main__':
  testing.test_main()
