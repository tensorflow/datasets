# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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
from absl.testing import parameterized
from tensorflow_datasets import testing
from tensorflow_datasets.core.utils import shard_utils


class ShardConfigTest(parameterized.TestCase):

  @parameterized.named_parameters(
      ('imagenet train, 137 GiB', 137 << 30, 1281167, True, 1024),
      ('imagenet evaluation, 6.3 GiB', 6300 * (1 << 20), 50000, True, 64),
      ('very large, but few examples, 52 GiB', 52 << 30, 512, True, 512),
      ('xxl, 10 TiB', 10 << 40, 10**9, True, 11264),
      ('xxl, 10 PiB, 100B examples', 10 << 50, 10**11, True, 10487808),
      ('xs, 100 MiB, 100K records', 10 << 20, 100 * 10**3, True, 1),
      ('m, 499 MiB, 200K examples', 400 << 20, 200 * 10**3, True, 4),
  )
  def test_get_number_shards_default_config(self, total_size, num_examples,
                                            uses_precise_sharding,
                                            expected_num_shards):
    shard_config = shard_utils.ShardConfig()
    self.assertEqual(
        expected_num_shards,
        shard_config.get_number_shards(
            total_size=total_size,
            num_examples=num_examples,
            uses_precise_sharding=uses_precise_sharding))

  def test_get_number_shards_if_specified(self):
    shard_config = shard_utils.ShardConfig(num_shards=42)
    self.assertEqual(
        42,
        shard_config.get_number_shards(
            total_size=100, num_examples=1, uses_precise_sharding=True))


class GetReadInstructionsTest(testing.TestCase, parameterized.TestCase):

  def test_read_all_even_sharding(self):
    # Even sharding
    res = shard_utils.get_file_instructions(0, 12, ['f1', 'f2', 'f3'],
                                            [4, 4, 4])
    self.assertEqual(res, [
        shard_utils.FileInstruction(
            filename='f1', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f2', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f3', skip=0, take=-1, num_examples=4),
    ])

  def test_read_all_empty_shard(self):
    res = shard_utils.get_file_instructions(0, 12, ['f1', 'f2', 'f3', 'f4'],
                                            [4, 4, 0, 4])
    self.assertEqual(res, [
        shard_utils.FileInstruction(
            filename='f1', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f2', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f4', skip=0, take=-1, num_examples=4),
    ])

  def test_from1_to10(self):
    res = shard_utils.get_file_instructions(1, 10, ['f1', 'f2', 'f3', 'f4'],
                                            [4, 4, 0, 4])
    self.assertEqual(res, [
        shard_utils.FileInstruction(
            filename='f1', skip=1, take=-1, num_examples=3),
        shard_utils.FileInstruction(
            filename='f2', skip=0, take=-1, num_examples=4),
        shard_utils.FileInstruction(
            filename='f4', skip=0, take=2, num_examples=2),
    ])

  def test_nothing_to_read(self):
    res = shard_utils.get_file_instructions(0, 0, ['f1', 'f2', 'f3', 'f4'],
                                            [0, 3, 0, 2])
    self.assertEqual(res, [])
    res = shard_utils.get_file_instructions(4, 4, ['f1', 'f2', 'f3', 'f4'],
                                            [0, 3, 0, 2])
    self.assertEqual(res, [])
    res = shard_utils.get_file_instructions(5, 5, ['f1', 'f2', 'f3', 'f4'],
                                            [0, 3, 0, 2])
    self.assertEqual(res, [])

  def test_split_file_instruction(self):
    filename = 'data.tfrecord'
    file_instruction = shard_utils.FileInstruction(
        filename=filename, skip=0, take=-1, num_examples=10)
    actual_splits = shard_utils.split_file_instruction(
        file_instruction=file_instruction, num_splits=3)
    self.assertEqual(actual_splits, [
        shard_utils.FileInstruction(
            filename=filename, skip=0, take=4, num_examples=10),
        shard_utils.FileInstruction(
            filename=filename, skip=4, take=4, num_examples=10),
        shard_utils.FileInstruction(
            filename=filename, skip=8, take=2, num_examples=10)
    ])

  def test_split_file_instruction_one_example_many_splits(self):
    # Test when more splits are requested than there are examples.
    filename = 'data.tfrecord'
    file_instruction = shard_utils.FileInstruction(
        filename=filename, skip=0, take=-1, num_examples=1)
    actual_splits = shard_utils.split_file_instruction(
        file_instruction=file_instruction, num_splits=9999)
    self.assertEqual(actual_splits, [
        shard_utils.FileInstruction(
            filename=filename, skip=0, take=1, num_examples=1),
    ])

  @parameterized.parameters(
      ('/a/b', '/a'),
      ('a', ''),
      ('', ''),
      ('/a/b/c/d', '/a/b/c'),
  )
  def test_file_instruction_dirname(self, filename, expected):
    file_instruction = shard_utils.FileInstruction(filename, 0, -1, 1)
    self.assertEqual(file_instruction.dirname(), expected)

  @parameterized.parameters(
      ('/a/b', 'b'),
      ('a', 'a'),
      ('', ''),
      ('/a/b/c/d', 'd'),
  )
  def test_file_instruction_basename(self, filename, expected):
    file_instruction = shard_utils.FileInstruction(filename, 0, -1, 1)
    self.assertEqual(file_instruction.basename(), expected)


if __name__ == '__main__':
  testing.test_main()
