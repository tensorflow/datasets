# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

from absl.testing import parameterized
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core.utils import shard_utils


class ShardConfigTest(parameterized.TestCase):

  @parameterized.named_parameters(
      dict(
          testcase_name='imagenet train, 137 GiB',
          total_size=137 << 30,
          num_examples=1281167,
          uses_precise_sharding=True,
          max_size=None,
          expected_num_shards=1024,
      ),
      dict(
          testcase_name='imagenet evaluation, 6.3 GiB',
          total_size=6300 * (1 << 20),
          num_examples=50000,
          uses_precise_sharding=True,
          max_size=None,
          expected_num_shards=64,
      ),
      dict(
          testcase_name='very large, but few examples, 52 GiB',
          total_size=52 << 30,
          num_examples=512,
          uses_precise_sharding=True,
          max_size=None,
          expected_num_shards=512,
      ),
      dict(
          testcase_name='xxl, 10 TiB',
          total_size=10 << 40,
          num_examples=10**9,
          uses_precise_sharding=True,
          max_size=None,
          expected_num_shards=11264,
      ),
      dict(
          testcase_name='xxl, 10 PiB, 100B examples',
          total_size=10 << 50,
          num_examples=10**11,
          uses_precise_sharding=True,
          max_size=None,
          expected_num_shards=10487808,
      ),
      dict(
          testcase_name='xs, 100 MiB, 100K records',
          total_size=10 << 20,
          num_examples=100 * 10**3,
          uses_precise_sharding=True,
          max_size=None,
          expected_num_shards=1,
      ),
      dict(
          testcase_name='m, 499 MiB, 200K examples',
          total_size=400 << 20,
          num_examples=200 * 10**3,
          uses_precise_sharding=True,
          max_size=None,
          expected_num_shards=4,
      ),
      dict(
          testcase_name='100GiB, even example sizes',
          num_examples=1e9,  # 1B examples
          total_size=1e9 * 1000,  # On average 1000 bytes per example
          max_size=1000,  # Max example size is 4000 bytes
          uses_precise_sharding=True,
          expected_num_shards=1024,
      ),
      dict(
          testcase_name='100GiB, uneven example sizes',
          num_examples=1e9,  # 1B examples
          total_size=1e9 * 1000,  # On average 1000 bytes per example
          max_size=4 * 1000,  # Max example size is 4000 bytes
          uses_precise_sharding=True,
          expected_num_shards=4096,
      ),
      dict(
          testcase_name='100GiB, very uneven example sizes',
          num_examples=1e9,  # 1B examples
          total_size=1e9 * 1000,  # On average 1000 bytes per example
          max_size=16 * 1000,  # Max example size is 16x the average bytes
          uses_precise_sharding=True,
          expected_num_shards=15360,
      ),
  )
  def test_get_number_shards_default_config(
      self,
      total_size: int,
      num_examples: int,
      uses_precise_sharding: bool,
      max_size: int,
      expected_num_shards: int,
  ):
    shard_config = shard_utils.ShardConfig()
    self.assertEqual(
        expected_num_shards,
        shard_config.get_number_shards(
            total_size=total_size,
            num_examples=num_examples,
            max_example_size=max_size,  # max(1, total_size // num_examples),
            uses_precise_sharding=uses_precise_sharding,
        ),
    )

  def test_get_number_shards_if_specified(self):
    shard_config = shard_utils.ShardConfig(num_shards=42)
    self.assertEqual(
        42,
        shard_config.get_number_shards(
            total_size=100,
            max_example_size=100,
            num_examples=1,
            uses_precise_sharding=True,
        ),
    )


def test_get_shard_boundaries_no_examples():
  with pytest.raises(AssertionError, match='No examples were yielded.'):
    shard_utils.get_shard_boundaries(num_examples=0, number_of_shards=3)


def test_get_shard_boundaries_not_enough_examples():
  with pytest.raises(
      AssertionError, match=r'num_examples \(2\) < number_of_shards \(3\)'
  ):
    shard_utils.get_shard_boundaries(num_examples=2, number_of_shards=3)


@pytest.mark.parametrize(
    'num_examples,number_of_shards,expected',
    [
        (3, 3, [1, 2, 3]),
        (4, 3, [1, 3, 4]),
        (5, 3, [2, 3, 5]),
        (6, 3, [2, 4, 6]),
    ],
)
def test_shard_boundaries(num_examples, number_of_shards, expected):
  assert (
      shard_utils.get_shard_boundaries(num_examples, number_of_shards)
      == expected
  )


class GetReadInstructionsTest(testing.TestCase, parameterized.TestCase):

  def test_read_all_even_sharding(self):
    # Even sharding
    res = shard_utils.get_file_instructions(
        0, 12, ['f1', 'f2', 'f3'], [4, 4, 4]
    )
    self.assertEqual(
        res,
        [
            shard_utils.FileInstruction(
                filename='f1', skip=0, take=-1, examples_in_shard=4
            ),
            shard_utils.FileInstruction(
                filename='f2', skip=0, take=-1, examples_in_shard=4
            ),
            shard_utils.FileInstruction(
                filename='f3', skip=0, take=-1, examples_in_shard=4
            ),
        ],
    )

  def test_read_all_empty_shard(self):
    res = shard_utils.get_file_instructions(
        0, 12, ['f1', 'f2', 'f3', 'f4'], [4, 4, 0, 4]
    )
    self.assertEqual(
        res,
        [
            shard_utils.FileInstruction(
                filename='f1', skip=0, take=-1, examples_in_shard=4
            ),
            shard_utils.FileInstruction(
                filename='f2', skip=0, take=-1, examples_in_shard=4
            ),
            shard_utils.FileInstruction(
                filename='f4', skip=0, take=-1, examples_in_shard=4
            ),
        ],
    )

  def test_from1_to10(self):
    res = shard_utils.get_file_instructions(
        1, 10, ['f1', 'f2', 'f3', 'f4'], [4, 4, 0, 4]
    )
    self.assertEqual(
        res,
        [
            shard_utils.FileInstruction(
                filename='f1', skip=1, take=3, examples_in_shard=4
            ),
            shard_utils.FileInstruction(
                filename='f2', skip=0, take=4, examples_in_shard=4
            ),
            shard_utils.FileInstruction(
                filename='f4', skip=0, take=2, examples_in_shard=4
            ),
        ],
    )

  def test_nothing_to_read(self):
    res = shard_utils.get_file_instructions(
        0, 0, ['f1', 'f2', 'f3', 'f4'], [0, 3, 0, 2]
    )
    self.assertEqual(res, [])
    res = shard_utils.get_file_instructions(
        4, 4, ['f1', 'f2', 'f3', 'f4'], [0, 3, 0, 2]
    )
    self.assertEqual(res, [])
    res = shard_utils.get_file_instructions(
        5, 5, ['f1', 'f2', 'f3', 'f4'], [0, 3, 0, 2]
    )
    self.assertEqual(res, [])

  def test_split_file_instruction(self):
    filename = 'data.tfrecord'
    file_instruction = shard_utils.FileInstruction(
        filename=filename, skip=0, take=-1, examples_in_shard=10
    )
    actual_splits = shard_utils.split_file_instruction(
        file_instruction=file_instruction, num_splits=3
    )
    self.assertEqual(
        actual_splits,
        [
            shard_utils.FileInstruction(
                filename=filename, skip=0, take=4, examples_in_shard=10
            ),
            shard_utils.FileInstruction(
                filename=filename, skip=4, take=4, examples_in_shard=10
            ),
            shard_utils.FileInstruction(
                filename=filename, skip=8, take=2, examples_in_shard=10
            ),
        ],
    )

  def test_split_file_instruction_one_example_many_splits(self):
    # Test when more splits are requested than there are examples.
    filename = 'data.tfrecord'
    file_instruction = shard_utils.FileInstruction(
        filename=filename, skip=0, take=-1, examples_in_shard=1
    )
    actual_splits = shard_utils.split_file_instruction(
        file_instruction=file_instruction, num_splits=9999
    )
    self.assertEqual(
        actual_splits,
        [
            shard_utils.FileInstruction(
                filename=filename, skip=0, take=1, examples_in_shard=1
            ),
        ],
    )

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


class FileInstructionTest(testing.TestCase, parameterized.TestCase):

  @parameterized.parameters(
      ('a', 0, 1, 1, shard_utils.FileInstruction('a', 0, 1, 1)),
      ('a', 0, 1, 2, shard_utils.FileInstruction('a', 0, 1, 2)),
      ('a', 0, -1, 1, shard_utils.FileInstruction('a', 0, 1, 1)),
      ('a', 1, -1, 10, shard_utils.FileInstruction('a', 1, 9, 10)),
  )
  def test_init(self, filename, skip, take, examples_in_shard, expected):
    actual = shard_utils.FileInstruction(
        filename, skip, take, examples_in_shard
    )
    self.assertEqual(expected, actual)

  @parameterized.parameters(
      ('a', 0, 1, -42, 'examples_in_shard should be >= 0!.+'),
      ('a', -42, 1, 2, 'skip should be between 0 and.+'),
      ('a', 0, 2, 1, 'skip .+take .+should be <= examples_in_shard.+'),
  )
  def test_incorrect_values(self, filename, skip, take, examples_in_shard, msg):
    with self.assertRaisesRegex(ValueError, expected_regex=msg):
      shard_utils.FileInstruction(filename, skip, take, examples_in_shard)

if __name__ == '__main__':
  testing.test_main()
