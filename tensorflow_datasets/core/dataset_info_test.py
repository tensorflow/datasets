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

"""Tests for tensorflow_datasets.core.dataset_info."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import test_utils
from tensorflow_datasets.core.utils import py_utils


_TFDS_DIR = py_utils.tfds_dir()
_INFO_DIR = os.path.join(_TFDS_DIR, "dataset_info", "mnist", "1.0.0")
_NON_EXISTENT_DIR = os.path.join(_TFDS_DIR, "non_existent_dir")


class DummyDatasetSharedGenerator(dataset_builder.GeneratorBasedBuilder):

  def _split_generators(self, dl_manager):
    # Split the 30 examples from the generator into 2 train shards and 1 test
    # shard.
    del dl_manager
    return [splits.SplitGenerator(
        name=[splits.Split.TRAIN, splits.Split.TEST],
        num_shards=[2, 1],
    )]

  def _info(self):
    return dataset_info.DatasetInfo(
        features=features.FeaturesDict({"x": tf.int64}),
        supervised_keys=("x", "x"),
    )

  def _generate_examples(self):
    for i in range(30):
      yield self.info.features.encode_example({"x": i})


class RandomShapedImageGenerator(DummyDatasetSharedGenerator):

  def _info(self):
    return dataset_info.DatasetInfo(
        features=features.FeaturesDict({"im": features.Image()}),
        supervised_keys=("im", "im"),
    )

  def _generate_examples(self):
    for _ in range(30):
      height = np.random.randint(5, high=10)
      width = np.random.randint(5, high=10)
      yield self.info.features.encode_example({
          "im":
              np.random.randint(
                  0, 255, size=(height, width, 3), dtype=np.uint8)
      })


class DatasetInfoTest(tf.test.TestCase):

  def test_undefined_dir(self):
    with self.assertRaisesWithPredicateMatch(ValueError,
                                             "undefined dataset_info_dir"):
      info = dataset_info.DatasetInfo()
      info.read_from_directory(None)

  def test_non_existent_dir(self):
    info = dataset_info.DatasetInfo()
    info.read_from_directory(_NON_EXISTENT_DIR)

    self.assertFalse(info.initialized)

  def test_reading(self):
    info = dataset_info.DatasetInfo()
    info.read_from_directory(_INFO_DIR)

    # Assert that we read the file and initialized DatasetInfo.
    self.assertTrue(info.initialized)
    self.assertTrue("mnist", info.name)

    # Test splits are initialized properly.
    split_dict = info.splits

    # Assert they are the correct number.
    self.assertTrue(len(split_dict), 2)

    # Assert on what they are
    self.assertTrue("train" in split_dict)
    self.assertTrue("test" in split_dict)

    # Assert that this is computed correctly.
    self.assertEqual(70000, info.num_examples)

    self.assertEqual("image", info.supervised_keys[0])
    self.assertEqual("label", info.supervised_keys[1])

  def test_writing(self):
    # First read in stuff.
    info = dataset_info.DatasetInfo()
    info.read_from_directory(_INFO_DIR)

    # Read the json file into a string.
    with tf.gfile.Open(info._dataset_info_filename(_INFO_DIR)) as f:
      existing_json = json.load(f)

    # Now write to a temp directory.
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      info.write_to_directory(tmp_dir)

      # Read the newly written json file into a string.
      with tf.gfile.Open(info._dataset_info_filename(tmp_dir)) as f:
        new_json = json.load(f)

    # Assert what was read and then written and read again is the same.
    self.assertEqual(existing_json, new_json)

  def test_reading_from_package_data(self):
    # We have mnist's 1.0.0 checked in the package data, so this should work.
    info = dataset_info.DatasetInfo(name="mnist", version="1.0.0")
    self.assertTrue(info.initialize_from_package_data())

    # A nominal check to see if we read it.
    self.assertTrue(info.initialized)
    self.assertEqual(10000, info.splits["test"].num_examples)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes
  def test_statistics_generation(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = DummyDatasetSharedGenerator(data_dir=tmp_dir)
      builder.download_and_prepare(compute_stats=True)

      # Overall
      self.assertEqual(30, builder.info.num_examples)

      # Per split.
      test_split = builder.info.splits["test"].get_proto()
      train_split = builder.info.splits["train"].get_proto()
      self.assertEqual(10, test_split.statistics.num_examples)
      self.assertEqual(20, train_split.statistics.num_examples)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes
  def test_statistics_generation_variable_sizes(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = RandomShapedImageGenerator(data_dir=tmp_dir)
      builder.download_and_prepare(compute_stats=True)

      # Get the expected type of the feature.
      schema_feature = builder.info.as_proto.schema.feature[0]
      self.assertEqual("im", schema_feature.name)

      self.assertEqual(-1, schema_feature.shape.dim[0].size)
      self.assertEqual(-1, schema_feature.shape.dim[1].size)
      self.assertEqual(3, schema_feature.shape.dim[2].size)

if __name__ == "__main__":
  tf.test.main()
