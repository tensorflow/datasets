# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.utils.shard_utils."""

from tensorflow_datasets import testing
from tensorflow_datasets.core.utils import shard_utils


class GetReadInstructionsTest(testing.TestCase):

  def test_read_all_even_sharding(self):
    # Even sharding
    res = shard_utils.get_file_instructions(
        0, 12, ['f1', 'f2', 'f3'], [4, 4, 4])
    self.assertEqual(res, [
        shard_utils.FileInstruction(
            filename='f1', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f2', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f3', skip=0, take=-1, num_examples=4),
    ])

  def test_read_all_empty_shard(self):
    res = shard_utils.get_file_instructions(
        0, 12, ['f1', 'f2', 'f3', 'f4'], [4, 4, 0, 4])
    self.assertEqual(res, [
        shard_utils.FileInstruction(
            filename='f1', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f2', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f4', skip=0, take=-1, num_examples=4),
    ])

  def test_from1_to10(self):
    res = shard_utils.get_file_instructions(
        1, 10, ['f1', 'f2', 'f3', 'f4'], [4, 4, 0, 4])
    self.assertEqual(res, [
        shard_utils.FileInstruction(
            filename='f1', skip=1, take=-1, num_examples=3),
        shard_utils.FileInstruction(
            filename='f2', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f4', skip=0, take=2, num_examples=2),
    ])

  def test_nothing_to_read(self):
    res = shard_utils.get_file_instructions(
        0, 0, ['f1', 'f2', 'f3', 'f4'], [0, 3, 0, 2])
    self.assertEqual(res, [])
    res = shard_utils.get_file_instructions(
        4, 4, ['f1', 'f2', 'f3', 'f4'], [0, 3, 0, 2])
    self.assertEqual(res, [])
    res = shard_utils.get_file_instructions(
        5, 5, ['f1', 'f2', 'f3', 'f4'], [0, 3, 0, 2])
    self.assertEqual(res, [])


if __name__ == '__main__':
  testing.test_main()
