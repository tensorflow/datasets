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
from tensorflow_datasets.core import proto
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import test_utils
import tensorflow_datasets.public_api as tfds

RANGE_TRAIN = list(range(0, 2000))
RANGE_TEST = list(range(3000, 3200))
RANGE_VAL = list(range(6000, 6010))


class DummyDataset(tfds.core.GeneratorBasedBuilder):
  """Dataset used for the tests."""

  def _info(self):
    return tfds.core.DatasetInfo(
        features=tfds.features.FeaturesDict({"value": tf.int64})
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

  def _generate_examples(self, data):
    for i in data:
      yield self.info.features.encode_example({
          "value": i,
      })

  def values(self, split):
    return [v["value"] for v in self.numpy_iterator(split=split)]


class SplitsUnitTest(tf.test.TestCase):

  @classmethod
  def setUpClass(cls):
    cls._splits = tfds.core.SplitDict()
    cls._splits.add(tfds.core.SplitInfo(name="train", num_shards=10))
    cls._splits.add(tfds.core.SplitInfo(name="test", num_shards=2))
    cls._splits.add(tfds.core.SplitInfo(name="validation", num_shards=2))

  def test_split_slice_merge(self):

    # Slice, then merge
    train = tfds.Split.TRAIN
    test = tfds.Split.TEST
    split = test.subsplit(tfds.percent[30:40]) + train

    # List sorted so always deterministic
    self.assertEqual(self._info(split), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="test", num_shards=2),
            slice_value=slice(30, 40),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="train", num_shards=10),
            slice_value=None,
        ),
    ])

  def test_split_merge_slice(self):

    # Merge, then slice (then merge)
    split = tfds.Split.TEST + tfds.Split.TRAIN
    split = split.subsplit(tfds.percent[30:40])
    split = split + tfds.Split.VALIDATION.subsplit(tfds.percent[:15])

    # List sorted so always deterministic
    self.assertEqual(self._info(split), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="test", num_shards=2),
            slice_value=slice(30, 40),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="train", num_shards=10),
            slice_value=slice(30, 40),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="validation", num_shards=2),
            slice_value=slice(None, 15),
        ),
    ])

  def test_split_k(self):
    split = tfds.Split.TEST + tfds.Split.TRAIN
    split1, split2, split3 = split.subsplit(k=3)

    self.assertEqual(self._info(split1), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="test", num_shards=2),
            slice_value=slice(0, 33),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="train", num_shards=10),
            slice_value=slice(0, 33),
        ),
    ])

    self.assertEqual(self._info(split2), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="test", num_shards=2),
            slice_value=slice(33, 66),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="train", num_shards=10),
            slice_value=slice(33, 66),
        ),
    ])

    self.assertEqual(self._info(split3), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="test", num_shards=2),
            slice_value=slice(66, 100),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="train", num_shards=10),
            slice_value=slice(66, 100),
        ),
    ])

  def test_split_weighted(self):
    split = tfds.Split.TEST + tfds.Split.TRAIN
    split1, split2 = split.subsplit(weighted=[2, 1])

    self.assertEqual(self._info(split1), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="test", num_shards=2),
            slice_value=slice(0, 66),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="train", num_shards=10),
            slice_value=slice(0, 66),
        ),
    ])

    self.assertEqual(self._info(split2), [
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="test", num_shards=2),
            slice_value=slice(66, 100),
        ),
        splits.SlicedSplitInfo(
            split_info=tfds.core.SplitInfo(name="train", num_shards=10),
            slice_value=slice(66, 100),
        ),
    ])

  def test_split_equivalence(self):
    split = tfds.Split.TRAIN + tfds.Split.TEST

    # Different way of splitting should all return the same results

    # Take first half of the split
    a = self._info(split.subsplit(k=2)[0])
    b = self._info(split.subsplit([1, 1])[0])
    c = self._info(split.subsplit([5, 5])[0])
    d = self._info(split.subsplit(tfds.percent[0:50]))

    self.assertEqual(a, b)
    self.assertEqual(b, c)
    self.assertEqual(c, d)
    self.assertEqual(d, a)

    # Take the last third of the split
    a = self._info(split.subsplit(k=3)[-1])
    b = self._info(split.subsplit([2, 1])[-1])
    b = self._info(split.subsplit([33, 11, 22, 34])[-1])
    c = self._info(split.subsplit(tfds.percent[66:100]))

    self.assertEqual(a, b)
    self.assertEqual(b, c)
    self.assertEqual(c, a)

    train = tfds.Split.TRAIN
    # 20%, 20% and 60% of the training set (using weighted)
    split1_1, split1_2, split1_3 = train.subsplit([2, 2, 6])
    split1_1 = self._info(split1_1)
    split1_2 = self._info(split1_2)
    split1_3 = self._info(split1_3)
    # 20%, 20% and 60% of the training set (using percent)
    split2_1 = self._info(train.subsplit(tfds.percent[0:20]))
    split2_2 = self._info(train.subsplit(tfds.percent[20:40]))
    split2_3 = self._info(train.subsplit(tfds.percent[40:100]))
    self.assertEqual(split1_1, split2_1)
    self.assertEqual(split1_2, split2_2)
    self.assertEqual(split1_3, split2_3)

  def test_split_equality(self):
    test = tfds.Split.TEST
    train = tfds.Split.TRAIN

    with self.assertRaisesWithPredicateMatch(
        NotImplementedError, "Equality is not implemented"):
      _ = test.subsplit(tfds.percent[10:]) == test.subsplit(tfds.percent[10:])

    with self.assertRaisesWithPredicateMatch(
        NotImplementedError, "Equality is not implemented"):
      _ = test + train == test + train

    self.assertEqual(tfds.Split.TEST, tfds.Split.TEST)
    self.assertEqual(tfds.Split.TEST, "test")
    self.assertEqual("test", tfds.Split.TEST)
    self.assertEqual(tfds.Split.ALL, "all")

    self.assertNotEqual(tfds.Split.ALL, "test")
    self.assertNotEqual(tfds.Split.ALL, test)
    self.assertNotEqual(train, test)
    self.assertNotEqual(train, train.subsplit(tfds.percent[:50]))
    self.assertNotEqual(train.subsplit(tfds.percent[:50]), train)

  def _info(self, split):
    read_instruction = split.get_read_instruction(self._splits)
    return read_instruction.get_list_sliced_split_info()


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
    cls._builder.download_and_prepare(compute_stats=False)

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
    train = tfds.Split.TRAIN
    split_00_19 = train.subsplit(tfds.percent[:20])  # 20% of the testing set
    split_20_39 = train.subsplit(tfds.percent[20:40])  # 20% of the testing set
    split_40_99 = train.subsplit(tfds.percent[40:])  # 60% of the testing set

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

    # The number of example in each split match the defined subsplit
    self.assertEqual(len(values_00_19), len(RANGE_TRAIN) // 5)  # 20%
    self.assertEqual(len(values_20_39), len(RANGE_TRAIN) // 5)  # 20%
    self.assertEqual(len(values_40_99), len(RANGE_TRAIN) * 3 // 5)  # 60%

  def test_merge_sub_split(self):
    # Merge then subsplit (1% / 99% of the data)
    train = tfds.Split.TRAIN
    test = tfds.Split.TEST
    split_pos, split_neg = (train + test).subsplit([1, 99])

    values_pos = self._builder.values(split=split_pos)
    values_neg = self._builder.values(split=split_neg)

    # All the training set should be covered
    self.assertEqual(
        list(sorted(values_pos + values_neg)),
        list(sorted(RANGE_TRAIN + RANGE_TEST)),
    )

    # None of the two splits should intersect
    self.assertEqual(set(values_pos) & set(values_neg), set())

    # The number of example in each split match the defined subsplit
    self.assertEqual(len(values_pos), len(RANGE_TRAIN + RANGE_TEST) // 100)
    self.assertEqual(len(values_neg), len(RANGE_TRAIN + RANGE_TEST) * 99 // 100)

  def test_sub_merge_split(self):
    # Subsplit, then merge
    train = tfds.Split.TRAIN
    test = tfds.Split.TEST
    split_pos = (train.subsplit(tfds.percent[50:]) +
                 test.subsplit(tfds.percent[:10]))
    split_neg = (train.subsplit(tfds.percent[:50]) +
                 test.subsplit(tfds.percent[10:]))

    values_pos = self._builder.values(split=split_pos)
    values_neg = self._builder.values(split=split_neg)

    # All the training set should be covered
    self.assertEqual(
        list(sorted(values_pos + values_neg)),
        list(sorted(RANGE_TRAIN + RANGE_TEST)),
    )

    # None of the two splits should intersect
    self.assertEqual(set(values_pos) & set(values_neg), set())

    # The number of example in each split match the defined subsplit
    self.assertEqual(
        len(values_pos), len(RANGE_TRAIN) // 2 + len(RANGE_TEST) // 10)
    self.assertEqual(
        len(values_neg), len(RANGE_TRAIN) // 2 + len(RANGE_TEST) * 9 // 10)

  def test_split_invalid(self):
    # Cannot add a split with himself
    test = tfds.Split.TEST

    with self.assertRaisesWithPredicateMatch(ValueError, "added with itself"):
      split = test + test
      self._builder.values(split=split)

    with self.assertRaisesWithPredicateMatch(ValueError, "added with itself"):
      split = test + tfds.Split.ALL
      self._builder.values(split=split)

    with self.assertRaisesWithPredicateMatch(ValueError, "added with itself"):
      split = (test.subsplit(tfds.percent[:10]) +
               test.subsplit(tfds.percent[10:]))
      self._builder.values(split=split)

    # Cannot slice a split twice

    with self.assertRaisesWithPredicateMatch(
        ValueError, "has already been sliced"):
      split = test.subsplit(tfds.percent[:10]).subsplit(tfds.percent[:10])
      self._builder.values(split=split)

    with self.assertRaisesWithPredicateMatch(
        ValueError, "has already been sliced"):
      split = test.subsplit(tfds.percent[10:]) + tfds.Split.TRAIN
      split = split.subsplit(tfds.percent[:50])
      self._builder.values(split=split)


class SplitsDictTest(tf.test.TestCase):

  @property
  def split_dict(self):
    sd = splits.SplitDict()
    sd.add(tfds.core.SplitInfo(name="train", num_shards=10))
    sd.add(tfds.core.SplitInfo(name="test", num_shards=1))
    return sd

  # .add is implicitly tested, since s was created by calling .add
  def test_get(self):
    s = self.split_dict["train"]
    self.assertEqual("train", s.name)
    self.assertEqual(10, s.num_shards)

  def test_from_proto(self):
    sd = splits.SplitDict.from_proto(
        [proto.SplitInfo(name="validation", num_shards=5)])
    self.assertTrue("validation" in sd)
    self.assertFalse("train" in sd)
    self.assertFalse("test" in sd)

  def test_to_proto(self):
    sd = self.split_dict
    sdp = sd.to_proto()

    self.assertEqual("test", sdp[0].name)
    self.assertEqual(1, sdp[0].num_shards)

    self.assertEqual("train", sdp[1].name)
    self.assertEqual(10, sdp[1].num_shards)

if __name__ == "__main__":
  tf.test.main()
