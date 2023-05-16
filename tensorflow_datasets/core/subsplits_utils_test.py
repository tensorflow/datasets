# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for subsplits_utils."""

import pytest
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import subsplits_utils


def _filename_template(split: str) -> naming.ShardedFileTemplate:
  return naming.ShardedFileTemplate(
      dataset_name='mnist',
      split=split,
      filetype_suffix='tfrecord',
      data_dir='/path',
  )


@pytest.mark.parametrize(
    'num_examples, n, drop_remainder, expected',
    [
        (9, 1, True, ['']),  # Full split selected
        (9, 2, True, ['[:4]', '[4:8]']),
        (9, 3, True, ['[:3]', '[3:6]', '[6:9]']),
        (9, 4, True, ['[:2]', '[2:4]', '[4:6]', '[6:8]']),  # Last ex dropped
        (11, 2, True, ['[:5]', '[5:10]']),
        (11, 3, True, ['[:3]', '[3:6]', '[6:9]']),  # Last 2 exs dropped
        (9, 1, False, ['']),
        (9, 2, False, ['[:5]', '[5:9]']),  # split0 has extra ex
        (9, 3, False, ['[:3]', '[3:6]', '[6:9]']),
        (9, 4, False, ['[:3]', '[3:5]', '[5:7]', '[7:9]']),  # 0 has extra ex
        (11, 3, False, ['[:4]', '[4:8]', '[8:11]']),  # 0, 1 have extra ex
        (11, 4, False, ['[:3]', '[3:6]', '[6:9]', '[9:11]']),
    ],
)
def test_even_splits(num_examples, n, drop_remainder, expected):
  split_infos = splits_lib.SplitDict(
      split_infos=[
          splits_lib.SplitInfo(
              name='train',
              shard_lengths=[num_examples],
              num_bytes=0,
              filename_template=_filename_template('train'),
          ),
      ]
  )

  subsplits = subsplits_utils.even_splits(
      'train', n, drop_remainder=drop_remainder
  )

  file_instructions = [split_infos[s].file_instructions for s in subsplits]
  expected_file_instructions = [
      split_infos[f'train{s}'].file_instructions for s in expected
  ]
  assert file_instructions == expected_file_instructions


def test_even_splits_subsplit():
  split_infos = splits_lib.SplitDict(
      split_infos=[
          splits_lib.SplitInfo(
              name='train',
              shard_lengths=[2, 3, 2, 3],  # 10
              num_bytes=0,
              filename_template=_filename_template('train'),
          ),
          splits_lib.SplitInfo(
              name='test',
              shard_lengths=[8],
              num_bytes=0,
              filename_template=_filename_template('test'),
          ),
      ]
  )

  # Test to split multiple splits
  subsplits = subsplits_utils.even_splits('train+test[50%:]', 3)

  expected = [
      'train[:4]+test[4:6]',
      'train[4:7]+test[6:7]',
      'train[7:]+test[7:8]',
  ]

  file_instructions = [split_infos[s].file_instructions for s in subsplits]
  expected_file_instructions = [
      split_infos[s].file_instructions for s in expected
  ]
  assert file_instructions == expected_file_instructions


def test_even_splits_add():
  # Compatibility of even_splits with other splits

  split_infos = splits_lib.SplitDict(
      split_infos=[
          splits_lib.SplitInfo(
              name='train',
              shard_lengths=[2, 3, 2, 3],  # 10
              num_bytes=0,
              filename_template=_filename_template('train'),
          ),
          splits_lib.SplitInfo(
              name='test',
              shard_lengths=[8],
              num_bytes=0,
              filename_template=_filename_template('test'),
          ),
          splits_lib.SplitInfo(
              name='validation',
              shard_lengths=[8],
              filename_template=_filename_template('validation'),
              num_bytes=0,
          ),
      ]
  )

  # Test to split multiple splits
  split = subsplits_utils.even_splits('train', 3, drop_remainder=True)[0]
  split = split + 'test'

  expected = 'train[:3]+test'

  file_instructions = split_infos[split].file_instructions
  expected_file_instructions = split_infos[expected].file_instructions
  assert file_instructions == expected_file_instructions

  # Test nested `even_splits`
  splits = subsplits_utils.even_splits('validation', n=2)
  splits = subsplits_utils.even_splits(splits[1], n=2)
  assert (
      split_infos[splits[0]].file_instructions
      == split_infos['validation[4:6]'].file_instructions
  )
  assert (
      split_infos[splits[1]].file_instructions
      == split_infos['validation[6:8]'].file_instructions
  )


def test_split_for_jax_process():
  split = subsplits_utils.split_for_jax_process('train')
  assert isinstance(split, subsplits_utils._EvenSplit)
  assert split.split == 'train'
  assert split.index == 0
  assert split.count == 1
