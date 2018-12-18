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

"""Tests for tensorflow_datasets.core.dataset_builder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl.testing import parameterized
import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import test_utils


DummyDatasetSharedGenerator = test_utils.DummyDatasetSharedGenerator


class DummyBuilderConfig(dataset_builder.BuilderConfig):

  def __init__(self, increment=0, **kwargs):
    super(DummyBuilderConfig, self).__init__(**kwargs)
    self.increment = increment


class DummyDatasetWithConfigs(dataset_builder.GeneratorBasedBuilder):
  BUILDER_CONFIGS = [
      DummyBuilderConfig(
          name="plus1",
          version="0.0.1",
          description="Add 1 to the records",
          increment=1),
      DummyBuilderConfig(
          name="plus2",
          version="0.0.2",
          description="Add 2 to the records",
          increment=2),
  ]

  def _split_generators(self, dl_manager):
    # Split the 30 examples from the generator into 2 train shards and 1 test
    # shard.
    del dl_manager
    return [
        splits_lib.SplitGenerator(
            name=[splits_lib.Split.TRAIN, splits_lib.Split.TEST],
            num_shards=[2, 1],
        )
    ]

  def _info(self):

    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"x": tf.int64}),
        supervised_keys=("x", "x"),
    )

  def _generate_examples(self):
    for i in range(30):
      if self.builder_config:
        i += self.builder_config.increment
      yield self.info.features.encode_example({"x": i})


class DatasetBuilderTest(tf.test.TestCase):

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_shared_generator(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = DummyDatasetSharedGenerator(data_dir=tmp_dir)
      builder.download_and_prepare()

      written_filepaths = [
          os.path.join(builder._data_dir, fname)
          for fname in tf.gfile.ListDirectory(builder._data_dir)
      ]
      # The data_dir contains the cached directory by default
      expected_filepaths = builder._build_split_filenames(
          split_info_list=builder.info.splits.values())
      expected_filepaths.append(
          os.path.join(builder._data_dir, "dataset_info.json"))
      self.assertEqual(sorted(expected_filepaths), sorted(written_filepaths))

      splits_list = [
          splits_lib.Split.TRAIN, splits_lib.Split.TEST
      ]
      train_data, test_data = [
          [el["x"] for el in builder.as_numpy(split=split)]
          for split in splits_list
      ]

      self.assertEqual(20, len(train_data))
      self.assertEqual(10, len(test_data))
      self.assertEqual(list(range(30)), sorted(train_data + test_data))

      # Builder's info should also have the above information.
      self.assertTrue(builder.info.initialized)
      self.assertEqual(20,
                       builder.info.splits[splits_lib.Split.TRAIN].num_examples)
      self.assertEqual(10,
                       builder.info.splits[splits_lib.Split.TEST].num_examples)
      self.assertEqual(30, builder.info.num_examples)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_load(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      dataset = registered.load(
          name="dummy_dataset_shared_generator",
          data_dir=tmp_dir,
          download=True,
          as_numpy=True,
          split=splits_lib.Split.TRAIN)
      data = list(dataset)
      self.assertEqual(20, len(data))
      self.assertLess(data[0]["x"], 30)

  def test_get_data_dir(self):
    # Test that the dataset load the most recent dir
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = DummyDatasetSharedGenerator(data_dir=tmp_dir)
      builder_data_dir = os.path.join(tmp_dir, builder.name)

      # The dataset folder contains multiple versions
      tf.gfile.MakeDirs(os.path.join(builder_data_dir, "14.0.0.invalid"))
      tf.gfile.MakeDirs(os.path.join(builder_data_dir, "10.0.0"))
      tf.gfile.MakeDirs(os.path.join(builder_data_dir, "9.0.0"))

      # The last valid version is chosen by default
      most_recent_dir = os.path.join(builder_data_dir, "10.0.0")
      v9_dir = os.path.join(builder_data_dir, "9.0.0")
      self.assertEqual(builder._get_data_dir(), most_recent_dir)
      self.assertEqual(builder._get_data_dir(version="9.0.0"), v9_dir)

  def test_get_data_dir_with_config(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      config_name = "plus1"
      builder = DummyDatasetWithConfigs(config=config_name, data_dir=tmp_dir)

      builder_data_dir = os.path.join(tmp_dir, builder.name, config_name)
      version_data_dir = os.path.join(builder_data_dir, "0.0.1")

      tf.gfile.MakeDirs(version_data_dir)
      self.assertEqual(builder._get_data_dir(), version_data_dir)

  def test_config_construction(self):
    self.assertSetEqual(
        set(["plus1", "plus2"]),
        set(DummyDatasetWithConfigs.builder_configs.keys()))
    plus1_config = DummyDatasetWithConfigs.builder_configs["plus1"]
    builder = DummyDatasetWithConfigs(config="plus1", data_dir=None)
    self.assertIs(plus1_config, builder.builder_config)
    builder = DummyDatasetWithConfigs(config=plus1_config, data_dir=None)
    self.assertIs(plus1_config, builder.builder_config)
    self.assertIs(builder.builder_config,
                  DummyDatasetWithConfigs.BUILDER_CONFIGS[0])

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_with_configs(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder1 = DummyDatasetWithConfigs(config="plus1", data_dir=tmp_dir)
      builder2 = DummyDatasetWithConfigs(config="plus2", data_dir=tmp_dir)
      # Test that builder.builder_config is the correct config
      self.assertIs(builder1.builder_config,
                    DummyDatasetWithConfigs.builder_configs["plus1"])
      self.assertIs(builder2.builder_config,
                    DummyDatasetWithConfigs.builder_configs["plus2"])
      builder1.download_and_prepare()
      builder2.download_and_prepare()
      data_dir1 = os.path.join(tmp_dir, builder1.name, "plus1", "0.0.1")
      data_dir2 = os.path.join(tmp_dir, builder2.name, "plus2", "0.0.2")
      # Test that subdirectories were created per config
      self.assertTrue(tf.gfile.Exists(data_dir1))
      self.assertTrue(tf.gfile.Exists(data_dir2))
      # 2 train shards, 1 test shard, plus metadata files
      self.assertGreater(len(tf.gfile.ListDirectory(data_dir1)), 3)
      self.assertGreater(len(tf.gfile.ListDirectory(data_dir2)), 3)

      # Test that the config was used and they didn't collide.
      splits_list = [splits_lib.Split.TRAIN, splits_lib.Split.TEST]
      for builder, incr in [(builder1, 1), (builder2, 2)]:
        train_data, test_data = [
            [el["x"] for el in builder.as_numpy(split=split)]
            for split in splits_list
        ]

        self.assertEqual(20, len(train_data))
        self.assertEqual(10, len(test_data))
        self.assertEqual([incr + el for el in range(30)],
                         sorted(train_data + test_data))


class DatasetBuilderReadTest(tf.test.TestCase):

  @classmethod
  def setUpClass(cls):
    cls._tfds_tmp_dir = test_utils.make_tmp_dir()
    builder = DummyDatasetSharedGenerator(data_dir=cls._tfds_tmp_dir)
    builder.download_and_prepare()

  @classmethod
  def tearDownClass(cls):
    test_utils.rm_tmp_dir(cls._tfds_tmp_dir)

  def setUp(self):
    self.builder = DummyDatasetSharedGenerator(data_dir=self._tfds_tmp_dir)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_all_splits(self):
    splits = self.builder.as_numpy(batch_size=-1)
    self.assertSetEqual(set(splits.keys()),
                        set([splits_lib.Split.TRAIN, splits_lib.Split.TEST]))

    # Test that enum and string both access same object
    self.assertIs(splits["train"], splits[splits_lib.Split.TRAIN])
    self.assertIs(splits["test"], splits[splits_lib.Split.TEST])

    train_data = splits[splits_lib.Split.TRAIN]["x"]
    test_data = splits[splits_lib.Split.TEST]["x"]
    self.assertEqual(20, len(train_data))
    self.assertEqual(10, len(test_data))
    self.assertEqual(sum(range(30)), int(train_data.sum() + test_data.sum()))

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_with_batch_size(self):
    items = list(self.builder.as_numpy(
        split=splits_lib.Split.TRAIN + splits_lib.Split.TEST, batch_size=10))
    # 3 batches of 10
    self.assertEqual(3, len(items))
    x1, x2, x3 = items[0]["x"], items[1]["x"], items[2]["x"]
    self.assertEqual(10, x1.shape[0])
    self.assertEqual(10, x2.shape[0])
    self.assertEqual(10, x3.shape[0])
    self.assertEqual(sum(range(30)), int(x1.sum() + x2.sum() + x3.sum()))

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_as_numpy(self):
    items = self.builder.as_numpy(split=splits_lib.Split.TRAIN, batch_size=-1)
    self.assertEqual(items["x"].shape[0], 20)
    self.assertLess(items["x"][0], 30)

    count = 0
    for _ in self.builder.as_numpy(split=splits_lib.Split.TRAIN):
      count += 1
    self.assertEqual(count, 20)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_supervised_keys(self):
    x, _ = self.builder.as_numpy(
        split=splits_lib.Split.TRAIN, as_supervised=True, batch_size=-1)
    self.assertEqual(x.shape[0], 20)


if __name__ == "__main__":
  tf.test.main()
