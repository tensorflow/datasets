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


RANGE_TRAIN = list(range(0, 100))
RANGE_TEST = list(range(100, 150))
RANGE_VAL = list(range(200, 210))


class DummyDataset(tfds.core.GeneratorBasedDatasetBuilder):
  """Dataset used for the tests."""

  def _info(self):
    return tfds.core.DatasetInfo(
        specs=tfds.features.SpecDict({'value': tf.int64})
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
      yield self.info.specs.encode_sample({
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

    self.assertEqual(read_instruction._splits, {
        'test': splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='test', num_shards=2),
            slice_value=slice(30, 40),
        ),
        'train': splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='train', num_shards=10),
            slice_value=None,
        ),
    })
    # List sorted so always deterministic
    self.assertEqual(read_instruction.split_info_list, [
        tfds.core.SplitInfo(name='test', num_shards=2),
        tfds.core.SplitInfo(name='train', num_shards=10),
    ])

  def test_split_merge_slice(self):

    # Merge, then slice (then merge)
    split = (tfds.Split.TEST + tfds.Split.TRAIN)[30:40]
    split = split + tfds.Split.VALIDATION[:15]

    read_instruction = split.get_read_instruction(self._splits)

    self.assertEqual(read_instruction._splits, {
        'test': splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='test', num_shards=2),
            slice_value=slice(30, 40),
        ),
        'train': splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='train', num_shards=10),
            slice_value=slice(30, 40),
        ),
        'validation': splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name='validation', num_shards=2),
            slice_value=slice(None, 15),
        ),
    })
    # List sorted so always deterministic
    self.assertEqual(read_instruction.split_info_list, [
        tfds.core.SplitInfo(name='test', num_shards=2),
        tfds.core.SplitInfo(name='train', num_shards=10),
        tfds.core.SplitInfo(name='validation', num_shards=2),
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
