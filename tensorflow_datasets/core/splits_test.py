# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Tests for the Split API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import test_utils
import tensorflow_datasets.public_api as tfds


RANGE_TRAIN = list(range(0, 2000))
RANGE_TEST = list(range(3000, 3200))
RANGE_VAL = list(range(6000, 6010))


class DummyDataset(tfds.core.GeneratorBasedDatasetBuilder):
  """Dataset used for the tests."""

  def _info(self):
    return tfds.core.DatasetInfo(
        features=tfds.features.FeaturesDict({'value': tf.int64})
    )

  def _split_generators(self, dl_manager):
    del dl_manager
    return [
        tfds.core.SplitGenerator(
            tfds.Split.TRAIN,
            num_shards=10,
            gen_kwargs=dict(data=RANGE_TRAIN),
        ),
        tfds.core.SplitGenerator(
            tfds.Split.TEST,
            num_shards=2,
            gen_kwargs=dict(data=RANGE_TEST),
        ),
        tfds.core.SplitGenerator(
            tfds.Split.VALIDATION,
            num_shards=2,
            gen_kwargs=dict(data=RANGE_VAL),
        ),
    ]

  def _generate_samples(self, data):
    for i in data:
      yield self.info.features.encode_sample({
          'value': i,
      })

  def values(self, split):
    return [v['value'] for v in self.numpy_iterator(split=split)]


class SplitsUnitTest(tf.test.TestCase):

  @classmethod
  def setUpClass(cls):
    cls._splits = tfds.core.SplitDict()
    cls._splits.add(tfds.core.SplitInfo(name='train', num_shards=10))
    cls._splits.add(tfds.core.SplitInfo(name='test', num_shards=2))
    cls._splits.add(tfds.core.SplitInfo(name='validation', num_shards=2))

  def test_split_slice_merge(self):

    # Slice, then merge
    split = tfds.Split.TEST[30:40] + tfds.Split.TRAIN

    read_instruction = split.get_read_instruction(self._splits)

    # List sorted so always deterministic
    self.assertEqual(read_instruction.get_list_sliced_split_info(), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='test', num_shards=2),
            slice_value=slice(30, 40),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='train', num_shards=10),
            slice_value=None,
        ),
    ])

  def test_split_merge_slice(self):

    # Merge, then slice (then merge)
    split = (tfds.Split.TEST + tfds.Split.TRAIN)[30:40]
    split = split + tfds.Split.VALIDATION[:15]

    read_instruction = split.get_read_instruction(self._splits)

    # List sorted so always deterministic
    self.assertEqual(read_instruction.get_list_sliced_split_info(), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='test', num_shards=2),
            slice_value=slice(30, 40),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='train', num_shards=10),
            slice_value=slice(30, 40),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='validation', num_shards=2),
            slice_value=slice(None, 15),
        ),
    ])

  def test_split_equality(self):

    with self.assertRaisesWithPredicateMatch(
        NotImplementedError, 'Equality is not implemented'):
      _ = tfds.Split.TEST[10:] == tfds.Split.TEST[10:]

    with self.assertRaisesWithPredicateMatch(
        NotImplementedError, 'Equality is not implemented'):
      _ = (
          (tfds.Split.TEST + tfds.Split.TRAIN) ==
          (tfds.Split.TEST + tfds.Split.TRAIN)
      )

    self.assertEqual(tfds.Split.TEST, tfds.Split.TEST)
    self.assertEqual(tfds.Split.TEST, 'test')
    self.assertEqual('test', tfds.Split.TEST)
    self.assertEqual(tfds.Split.ALL, 'all')

    self.assertNotEqual(tfds.Split.ALL, 'test')
    self.assertNotEqual(tfds.Split.ALL, tfds.Split.TEST)
    self.assertNotEqual(tfds.Split.TRAIN, tfds.Split.TEST)
    self.assertNotEqual(tfds.Split.TRAIN, tfds.Split.TRAIN[:50])
    self.assertNotEqual(tfds.Split.TRAIN[50:], tfds.Split.TRAIN)


class SliceToMaskTest(tf.test.TestCase):

  def __getitem__(self, slice_value):
    return slice_value

  def test_slice_to_mask(self):
    s2p = splits.slice_to_percent_mask

    self.assertEqual(s2p(self[:]), [True] * 100)
    self.assertEqual(s2p(self[:60]), [True] * 60 + [False] * 40)
    self.assertEqual(s2p(self[60:]), [False] * 60 + [True] * 40)
    self.assertEqual(
        s2p(self[10:20]), [False] * 10 + [True] * 10 + [False] * 80)
    self.assertEqual(s2p(self[:-20]), [True] * 80 + [False] * 20)


class SplitsIntegrationTest(tf.test.TestCase):

  @classmethod
  def setUpClass(cls):
    cls._builder = DummyDataset(data_dir=test_utils.make_tmp_dir())
    cls._builder.download_and_prepare()

  def test_split_all(self):
    split = tfds.Split.ALL
    all_values = self._builder.values(split=split)

    self.assertEqual(
        list(sorted(all_values)),
        list(sorted(RANGE_TRAIN + RANGE_TEST + RANGE_VAL)),
    )

  def test_split_merge(self):
    split = tfds.Split.TRAIN + tfds.Split.TEST
    all_values = self._builder.values(split=split)

    self.assertEqual(
        list(sorted(all_values)),
        list(sorted(RANGE_TRAIN + RANGE_TEST)),
    )

  def test_sub_split(self):
    split_00_19 = tfds.Split.TRAIN[:20]  # 20% of the testing set
    split_20_39 = tfds.Split.TRAIN[20:40]  # 20% of the testing set
    split_40_99 = tfds.Split.TRAIN[40:]  # 60% of the testing set

    values_00_19 = self._builder.values(split=split_00_19)
    values_20_39 = self._builder.values(split=split_20_39)
    values_40_99 = self._builder.values(split=split_40_99)

    # All the training set should be covered
    self.assertEqual(
        list(sorted(values_00_19 + values_20_39 + values_40_99)),
        list(sorted(RANGE_TRAIN)),
    )

    # None of the split should intersect with each other
    self.assertEqual(set(values_00_19) & set(values_20_39), set())
    self.assertEqual(set(values_20_39) & set(values_40_99), set())
    self.assertEqual(set(values_40_99) & set(values_00_19), set())

    # The number of sample in each split match the defined subsplit
    self.assertEqual(len(values_00_19), len(RANGE_TRAIN) // 5)  # 20%
    self.assertEqual(len(values_20_39), len(RANGE_TRAIN) // 5)  # 20%
    self.assertEqual(len(values_40_99), len(RANGE_TRAIN) * 3 // 5)  # 60%

  def test_merge_sub_split(self):
    # Merge then subsplit
    split_pos = (tfds.Split.TRAIN + tfds.Split.TEST)[:1]  # 1% of the data
    split_neg = (tfds.Split.TRAIN + tfds.Split.TEST)[1:]  # 99% of the data

    values_pos = self._builder.values(split=split_pos)
    values_neg = self._builder.values(split=split_neg)

    # All the training set should be covered
    self.assertEqual(
        list(sorted(values_pos + values_neg)),
        list(sorted(RANGE_TRAIN + RANGE_TEST)),
    )

    # None of the two splits should intersect
    self.assertEqual(set(values_pos) & set(values_neg), set())

    # The number of sample in each split match the defined subsplit
    self.assertEqual(len(values_pos), len(RANGE_TRAIN + RANGE_TEST) // 100)
    self.assertEqual(len(values_neg), len(RANGE_TRAIN + RANGE_TEST) * 99 // 100)

  def test_sub_merge_split(self):
    # Subsplit, then merge
    split_pos = tfds.Split.TRAIN[50:] + tfds.Split.TEST[:10]
    split_neg = tfds.Split.TRAIN[:50] + tfds.Split.TEST[10:]

    values_pos = self._builder.values(split=split_pos)
    values_neg = self._builder.values(split=split_neg)

    # All the training set should be covered
    self.assertEqual(
        list(sorted(values_pos + values_neg)),
        list(sorted(RANGE_TRAIN + RANGE_TEST)),
    )

    # None of the two splits should intersect
    self.assertEqual(set(values_pos) & set(values_neg), set())

    # The number of sample in each split match the defined subsplit
    self.assertEqual(
        len(values_pos), len(RANGE_TRAIN) // 2 + len(RANGE_TEST) // 10)
    self.assertEqual(
        len(values_neg), len(RANGE_TRAIN) // 2 + len(RANGE_TEST) * 9 // 10)

  def test_split_invalid(self):
    # Cannot add a split with himself

    with self.assertRaisesWithPredicateMatch(ValueError, 'added with itself'):
      split = tfds.Split.TEST + tfds.Split.TEST
      self._builder.values(split=split)

    with self.assertRaisesWithPredicateMatch(ValueError, 'added with itself'):
      split = tfds.Split.TEST + tfds.Split.ALL
      self._builder.values(split=split)

    with self.assertRaisesWithPredicateMatch(ValueError, 'added with itself'):
      split = tfds.Split.TEST[:10] + tfds.Split.TEST[10:]
      self._builder.values(split=split)

    # Cannot slice a split twice

    with self.assertRaisesWithPredicateMatch(
        ValueError, 'has already been sliced'):
      split = tfds.Split.TEST[10:][:10]
      self._builder.values(split=split)

    with self.assertRaisesWithPredicateMatch(
        ValueError, 'has already been sliced'):
      split = tfds.Split.TEST[10:] + tfds.Split.TRAIN
      split = split[:50]
      self._builder.values(split=split)

    # TODO(epot): Add tests if slice values are incorrect (not between 0-100)


if __name__ == '__main__':
  tf.test.main()
