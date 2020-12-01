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

"""Tests for the Split API."""

from tensorflow_datasets import testing
from tensorflow_datasets.core import proto
from tensorflow_datasets.core import splits
from tensorflow_datasets.core.utils import shard_utils
import tensorflow_datasets.public_api as tfds

RANGE_TRAIN = list(range(0, 2000))
RANGE_TEST = list(range(3000, 3200))
RANGE_VAL = list(range(6000, 6010))


class SplitDictTest(testing.TestCase):

  def test_num_shards(self):
    sd = splits.SplitDict("ds_name")
    sd.add(tfds.core.SplitInfo(
        name="train", shard_lengths=[1, 2, 3], num_bytes=0,
    ))
    self.assertEqual(sd["train"].num_shards, 3)


class SplitsDictTest(testing.TestCase):

  @property
  def split_dict(self):
    sd = splits.SplitDict("ds_name")
    sd.add(tfds.core.SplitInfo(
        name="train", shard_lengths=[10, 10], num_bytes=0
    ))
    sd.add(tfds.core.SplitInfo(name="test", shard_lengths=[1], num_bytes=0))
    return sd

  # .add is implicitly tested, since s was created by calling .add
  def test_get(self):
    s = self.split_dict["train"]
    self.assertEqual("train", s.name)
    self.assertEqual(2, s.num_shards)

  def test_from_proto(self):
    sd = splits.SplitDict.from_proto(
        "ds_name", [
            proto.SplitInfo(name="validation", shard_lengths=[5], num_bytes=0)
        ])
    self.assertIn("validation", sd)
    self.assertNotIn("train", sd)
    self.assertNotIn("test", sd)

  def test_to_proto(self):
    sd = self.split_dict
    sdp = sd.to_proto()

    self.assertEqual("test", sdp[0].name)
    self.assertEqual([1], sdp[0].shard_lengths)

    self.assertEqual("train", sdp[1].name)
    self.assertEqual([10, 10], sdp[1].shard_lengths)

  def test_bool(self):
    sd = splits.SplitDict("ds_name")
    self.assertFalse(sd)  # Empty split is False
    sd.add(tfds.core.SplitInfo(name="train", shard_lengths=[5], num_bytes=0))
    self.assertTrue(sd)  # Non-empty split is True

  def test_check_splits_equals(self):
    s1 = splits.SplitDict("ds_name")
    s1.add(tfds.core.SplitInfo(name="train", shard_lengths=[10], num_bytes=0))
    s1.add(tfds.core.SplitInfo(name="test", shard_lengths=[3], num_bytes=0))

    s2 = splits.SplitDict("ds_name")
    s2.add(tfds.core.SplitInfo(name="train", shard_lengths=[10], num_bytes=0))
    s2.add(tfds.core.SplitInfo(name="test", shard_lengths=[3], num_bytes=0))

    s3 = splits.SplitDict("ds_name")
    s3.add(tfds.core.SplitInfo(name="train", shard_lengths=[10], num_bytes=0))
    s3.add(tfds.core.SplitInfo(name="test", shard_lengths=[3], num_bytes=0))
    s3.add(tfds.core.SplitInfo(name="valid", shard_lengths=[0], num_bytes=0))

    s4 = splits.SplitDict("ds_name")
    s4.add(tfds.core.SplitInfo(name="train", shard_lengths=[11], num_bytes=0))
    s4.add(tfds.core.SplitInfo(name="test", shard_lengths=[3], num_bytes=0))

    self.assertTrue(splits.check_splits_equals(s1, s1))
    self.assertTrue(splits.check_splits_equals(s1, s2))
    self.assertFalse(splits.check_splits_equals(s1, s3))  # Not same names
    self.assertFalse(splits.check_splits_equals(s1, s4))  # Nb of shards !=


class SplitsTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(SplitsTest, cls).setUpClass()
    cls._builder = testing.DummyDatasetSharedGenerator(
        data_dir=testing.make_tmp_dir())
    cls._builder.download_and_prepare()

  def test_sub_split_num_examples(self):
    s = self._builder.info.splits
    self.assertEqual(s["train[75%:]"].num_examples, 5)
    self.assertEqual(s["train[:75%]"].num_examples, 15)
    self.assertEqual(
        s["train"].num_examples,
        s["train[75%:]"].num_examples + s["train[:75%]"].num_examples,
    )

    self.assertEqual(s["test[75%:]"].num_examples, 2)
    self.assertEqual(s["test[:75%]"].num_examples, 8)
    self.assertEqual(
        s["test"].num_examples,
        s["test[75%:]"].num_examples + s["test[:75%]"].num_examples,
    )

  def test_sub_split_file_instructions(self):
    fi = self._builder.info.splits["train[75%:]"].file_instructions
    self.assertEqual(fi, [shard_utils.FileInstruction(
        filename="dummy_dataset_shared_generator-train.tfrecord-00000-of-00001",
        skip=15,
        take=-1,
        num_examples=5,
    )])

  def test_split_file_instructions(self):
    fi = self._builder.info.splits["train"].file_instructions
    self.assertEqual(fi, [shard_utils.FileInstruction(
        filename="dummy_dataset_shared_generator-train.tfrecord-00000-of-00001",
        skip=0,
        take=-1,
        num_examples=20,
    )])

  def test_sub_split_filenames(self):
    self.assertEqual(self._builder.info.splits["train"].filenames, [
        "dummy_dataset_shared_generator-train.tfrecord-00000-of-00001",
    ])
    self.assertEqual(self._builder.info.splits["train[75%:]"].filenames, [
        "dummy_dataset_shared_generator-train.tfrecord-00000-of-00001",
    ])

  def test_sub_split_wrong_key(self):
    with self.assertRaisesWithPredicateMatch(
        ValueError, "Unknown split \"unknown\""):
      _ = self._builder.info.splits["unknown"]

  def test_split_enum(self):
    self.assertEqual(repr(splits.Split.TRAIN), "Split('train')")
    self.assertIsInstance(splits.Split.TRAIN, splits.Split)

  def test_even_splits(self):
    self.assertEqual(
        ["train[0%:33%]", "train[33%:67%]", "train[67%:100%]"],
        splits.even_splits("train", n=3),
    )
    self.assertEqual([
        "train[0%:25%]", "train[25%:50%]", "train[50%:75%]", "train[75%:100%]"
    ], splits.even_splits("train", 4))
    with self.assertRaises(ValueError):
      splits.even_splits("train", 0)
    with self.assertRaises(ValueError):
      splits.even_splits("train", 101)


if __name__ == "__main__":
  testing.test_main()
