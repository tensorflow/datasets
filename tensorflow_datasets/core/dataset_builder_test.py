# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

from absl.testing import absltest
from absl.testing import parameterized
import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils

tf.compat.v1.enable_eager_execution()

DummyDatasetSharedGenerator = testing.DummyDatasetSharedGenerator


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
          supported_versions=["0.0.1"],
          description="Add 2 to the records",
          increment=2),
  ]

  def _split_generators(self, dl_manager):
    # Split the 30 examples from the generator into 2 train shards and 1 test
    # shard.
    del dl_manager
    return [
        splits_lib.SplitGenerator(
            name=splits_lib.Split.TRAIN,
            num_shards=2,
            gen_kwargs={"range_": range(20)},
        ),
        splits_lib.SplitGenerator(
            name=splits_lib.Split.TEST,
            num_shards=1,
            gen_kwargs={"range_": range(20, 30)},
        ),
    ]

  def _info(self):

    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"x": tf.int64}),
        supervised_keys=("x", "x"),
    )

  def _generate_examples(self, range_):
    for i in range_:
      if self.builder_config:
        i += self.builder_config.increment
      yield {"x": i}


class InvalidSplitDataset(DummyDatasetWithConfigs):

  def _split_generators(self, _):
    return [
        splits_lib.SplitGenerator(
            name=splits_lib.Split.ALL,  # Error: ALL cannot be used as Split key
            num_shards=5,
        )
    ]


class DatasetBuilderTest(testing.TestCase):

  @testing.run_in_graph_and_eager_modes()
  def test_load(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      dataset = registered.load(
          name="dummy_dataset_shared_generator",
          data_dir=tmp_dir,
          download=True,
          split=splits_lib.Split.TRAIN)
      data = list(dataset_utils.as_numpy(dataset))
      self.assertEqual(20, len(data))
      self.assertLess(data[0]["x"], 30)

  @testing.run_in_graph_and_eager_modes()
  def test_determinism(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      ds = registered.load(
          name="dummy_dataset_shared_generator",
          data_dir=tmp_dir,
          split=splits_lib.Split.TRAIN,
          as_dataset_kwargs=dict(shuffle_files=False))
      ds_values = list(dataset_utils.as_numpy(ds))

      # Ensure determinism. If this test fail, this mean that numpy random
      # module isn't always determinist (maybe between version, architecture,
      # ...), and so our datasets aren't guaranteed either.
      l = list(range(20))
      np.random.RandomState(42).shuffle(l)
      self.assertEqual(l, [
          0, 17, 15, 1, 8, 5, 11, 3, 18, 16, 13, 2, 9, 19, 4, 12, 7, 10, 14, 6
      ])

      # Ensure determinism. If this test fails, this mean the dataset are not
      # deterministically generated.
      self.assertEqual(
          [e["x"] for e in ds_values],
          [16, 1, 2, 3, 10, 17, 0, 11, 14, 7, 4, 9, 18, 15, 8, 19, 6, 13, 12,
           5],
      )

  @testing.run_in_graph_and_eager_modes()
  def test_multi_split(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      ds_train, ds_test = registered.load(
          name="dummy_dataset_shared_generator",
          data_dir=tmp_dir,
          split=[splits_lib.Split.TRAIN, splits_lib.Split.TEST],
          as_dataset_kwargs=dict(shuffle_files=False))

      data = list(dataset_utils.as_numpy(ds_train))
      self.assertEqual(20, len(data))

      data = list(dataset_utils.as_numpy(ds_test))
      self.assertEqual(10, len(data))

  def test_build_data_dir(self):
    # Test that the dataset loads the data_dir for the builder's version
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = DummyDatasetSharedGenerator(data_dir=tmp_dir)
      self.assertEqual(str(builder.info.version), "1.0.0")
      builder_data_dir = os.path.join(tmp_dir, builder.name)
      version_dir = os.path.join(builder_data_dir, "1.0.0")

      # The dataset folder contains multiple other versions
      tf.io.gfile.makedirs(os.path.join(builder_data_dir, "14.0.0.invalid"))
      tf.io.gfile.makedirs(os.path.join(builder_data_dir, "10.0.0"))
      tf.io.gfile.makedirs(os.path.join(builder_data_dir, "9.0.0"))
      tf.io.gfile.makedirs(os.path.join(builder_data_dir, "0.1.0"))

      # The builder's version dir is chosen
      self.assertEqual(builder._build_data_dir(), version_dir)

  def test_get_data_dir_with_config(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      config_name = "plus1"
      builder = DummyDatasetWithConfigs(config=config_name, data_dir=tmp_dir)

      builder_data_dir = os.path.join(tmp_dir, builder.name, config_name)
      version_data_dir = os.path.join(builder_data_dir, "0.0.1")

      tf.io.gfile.makedirs(version_data_dir)
      self.assertEqual(builder._build_data_dir(), version_data_dir)

  def test_config_construction(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      self.assertSetEqual(
          set(["plus1", "plus2"]),
          set(DummyDatasetWithConfigs.builder_configs.keys()))
      plus1_config = DummyDatasetWithConfigs.builder_configs["plus1"]
      builder = DummyDatasetWithConfigs(config="plus1", data_dir=tmp_dir)
      self.assertIs(plus1_config, builder.builder_config)
      builder = DummyDatasetWithConfigs(config=plus1_config, data_dir=tmp_dir)
      self.assertIs(plus1_config, builder.builder_config)
      self.assertIs(builder.builder_config,
                    DummyDatasetWithConfigs.BUILDER_CONFIGS[0])

  @testing.run_in_graph_and_eager_modes()
  def test_with_configs(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
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
      self.assertTrue(tf.io.gfile.exists(data_dir1))
      self.assertTrue(tf.io.gfile.exists(data_dir2))
      # 2 train shards, 1 test shard, plus metadata files
      self.assertGreater(len(tf.io.gfile.listdir(data_dir1)), 3)
      self.assertGreater(len(tf.io.gfile.listdir(data_dir2)), 3)

      # Test that the config was used and they didn't collide.
      splits_list = [splits_lib.Split.TRAIN, splits_lib.Split.TEST]
      for builder, incr in [(builder1, 1), (builder2, 2)]:
        train_data, test_data = [   # pylint: disable=g-complex-comprehension
            [el["x"] for el in   # pylint: disable=g-complex-comprehension
             dataset_utils.as_numpy(builder.as_dataset(split=split))]
            for split in splits_list
        ]

        self.assertEqual(20, len(train_data))
        self.assertEqual(10, len(test_data))
        self.assertEqual([incr + el for el in range(30)],
                         sorted(train_data + test_data))

  def test_with_supported_version(self):
    DummyDatasetWithConfigs(config="plus1", version="0.0.1")

  def test_latest_experimental_version(self):
    builder1 = DummyDatasetSharedGenerator()
    self.assertEqual(str(builder1._version), "1.0.0")
    builder2 = DummyDatasetSharedGenerator(version="experimental_latest")
    self.assertEqual(str(builder2._version), "2.0.0")

  def test_with_unsupported_version(self):
    expected = "Dataset dummy_dataset_with_configs cannot be loaded at version"
    with self.assertRaisesWithPredicateMatch(AssertionError, expected):
      DummyDatasetWithConfigs(config="plus1", version="0.0.2")
    with self.assertRaisesWithPredicateMatch(AssertionError, expected):
      DummyDatasetWithConfigs(config="plus1", version="0.1.*")

  def test_previous_supported_version(self):
    default_builder = DummyDatasetSharedGenerator()
    self.assertEqual(str(default_builder.info.version), "1.0.0")
    older_builder = DummyDatasetSharedGenerator(version="0.0.*")
    self.assertEqual(str(older_builder.info.version), "0.0.9")

  def test_invalid_split_dataset(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      with self.assertRaisesWithPredicateMatch(ValueError, "ALL is a special"):
        # Raise error during .download_and_prepare()
        registered.load(
            name="invalid_split_dataset",
            data_dir=tmp_dir,
        )


class BuilderRestoreGcsTest(testing.TestCase):

  def setUp(self):
    super(BuilderRestoreGcsTest, self).setUp()

    def load_mnist_dataset_info(self):
      mnist_info_path = os.path.join(
          utils.tfds_dir(),
          "testing/test_data/dataset_info/mnist/1.0.0",
      )
      mnist_info_path = os.path.normpath(mnist_info_path)
      self.read_from_directory(mnist_info_path)

    patcher = absltest.mock.patch.object(
        dataset_info.DatasetInfo,
        "initialize_from_bucket",
        new=load_mnist_dataset_info
    )
    patcher.start()
    self.patch_gcs = patcher
    self.addCleanup(patcher.stop)

    patcher = absltest.mock.patch.object(
        dataset_info.DatasetInfo, "compute_dynamic_properties",
    )
    self.compute_dynamic_property = patcher.start()
    self.addCleanup(patcher.stop)

  def test_stats_restored_from_gcs(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = testing.DummyMnist(data_dir=tmp_dir)
      self.assertEqual(builder.info.splits.total_num_examples, 70000)
      self.assertFalse(self.compute_dynamic_property.called)

      builder.download_and_prepare()

      # Statistics shouldn't have been recomputed
      self.assertEqual(builder.info.splits.total_num_examples, 70000)
      self.assertFalse(self.compute_dynamic_property.called)

  def test_stats_not_restored_gcs_overwritten(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # If split are different that the one restored, stats should be recomputed
      builder = testing.DummyMnist(data_dir=tmp_dir, num_shards=5)
      self.assertEqual(builder.info.splits.total_num_examples, 70000)
      self.assertFalse(self.compute_dynamic_property.called)

      builder.download_and_prepare()

      # Statistics should have been recomputed (split different from the
      # restored ones)
      self.assertTrue(self.compute_dynamic_property.called)

  def test_gcs_not_exists(self):
    # By disabling the patch, and because DummyMnist is not on GCS, we can
    # simulate a new dataset starting from scratch
    self.patch_gcs.stop()
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = testing.DummyMnist(data_dir=tmp_dir)
      # No dataset_info restored, so stats are empty
      self.assertEqual(builder.info.splits.total_num_examples, 0)
      self.assertFalse(self.compute_dynamic_property.called)

      builder.download_and_prepare()

      # Statistics should have been recomputed
      self.assertTrue(self.compute_dynamic_property.called)
    self.patch_gcs.start()

  def test_skip_stats(self):
    # Test when stats do not exists yet and compute_stats='skip'

    # By disabling the patch, and because DummyMnist is not on GCS, we can
    # simulate a new dataset starting from scratch
    self.patch_gcs.stop()
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # No dataset_info restored, so stats are empty
      builder = testing.DummyMnist(data_dir=tmp_dir, num_shards=5)
      self.assertEqual(builder.info.splits.total_num_examples, 0)
      self.assertFalse(self.compute_dynamic_property.called)

      download_config = download.DownloadConfig(
          compute_stats=download.ComputeStatsMode.SKIP,
      )
      builder.download_and_prepare(download_config=download_config)

      # Statistics computation should have been skipped
      self.assertEqual(builder.info.splits.total_num_examples, 0)
      self.assertFalse(self.compute_dynamic_property.called)
    self.patch_gcs.start()

  def test_force_stats(self):
    # Test when stats already exists but compute_stats='force'

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # No dataset_info restored, so stats are empty
      builder = testing.DummyMnist(data_dir=tmp_dir, num_shards=5)
      self.assertEqual(builder.info.splits.total_num_examples, 70000)
      self.assertFalse(self.compute_dynamic_property.called)

      download_config = download.DownloadConfig(
          compute_stats=download.ComputeStatsMode.FORCE,
      )
      builder.download_and_prepare(download_config=download_config)

      # Statistics computation should have been recomputed
      self.assertTrue(self.compute_dynamic_property.called)


class DatasetBuilderReadTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DatasetBuilderReadTest, cls).setUpClass()
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    builder = DummyDatasetSharedGenerator(data_dir=cls._tfds_tmp_dir)
    builder.download_and_prepare()

  @classmethod
  def tearDownClass(cls):
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  def setUp(self):
    self.builder = DummyDatasetSharedGenerator(data_dir=self._tfds_tmp_dir)

  @testing.run_in_graph_and_eager_modes()
  def test_in_memory(self):
    train_data = dataset_utils.as_numpy(
        self.builder.as_dataset(split="train", in_memory=True))
    train_data = [el for el in train_data]
    self.assertEqual(20, len(train_data))

  def test_in_memory_with_device_ctx(self):
    # Smoke test to ensure that the inner as_numpy call does not fail when under
    # an explicit device context.
    # Only testing in graph mode. Eager mode would actually require job:foo to
    # exist in the cluster.
    with tf.Graph().as_default():
      # Testing it works even if a default Session is active
      with tf.compat.v1.Session() as _:
        with tf.device("/job:foo"):
          self.builder.as_dataset(split="train", in_memory=True)

  @testing.run_in_graph_and_eager_modes()
  def test_all_splits(self):
    splits = dataset_utils.as_numpy(
        self.builder.as_dataset(batch_size=-1))
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

  @testing.run_in_graph_and_eager_modes()
  def test_with_batch_size(self):
    items = list(dataset_utils.as_numpy(self.builder.as_dataset(
        split=splits_lib.Split.TRAIN + splits_lib.Split.TEST, batch_size=10)))
    # 3 batches of 10
    self.assertEqual(3, len(items))
    x1, x2, x3 = items[0]["x"], items[1]["x"], items[2]["x"]
    self.assertEqual(10, x1.shape[0])
    self.assertEqual(10, x2.shape[0])
    self.assertEqual(10, x3.shape[0])
    self.assertEqual(sum(range(30)), int(x1.sum() + x2.sum() + x3.sum()))

    # By default batch_size is None and won't add a batch dimension
    ds = self.builder.as_dataset(split=splits_lib.Split.TRAIN)
    self.assertEqual(0, len(ds.output_shapes["x"]))
    # Setting batch_size=1 will add an extra batch dimension
    ds = self.builder.as_dataset(split=splits_lib.Split.TRAIN, batch_size=1)
    self.assertEqual(1, len(ds.output_shapes["x"]))
    # Setting batch_size=2 will add an extra batch dimension
    ds = self.builder.as_dataset(split=splits_lib.Split.TRAIN, batch_size=2)
    self.assertEqual(1, len(ds.output_shapes["x"]))

  @testing.run_in_graph_and_eager_modes()
  def test_supervised_keys(self):
    x, _ = dataset_utils.as_numpy(self.builder.as_dataset(
        split=splits_lib.Split.TRAIN, as_supervised=True, batch_size=-1))
    self.assertEqual(x.shape[0], 20)



if __name__ == "__main__":
  testing.test_main()
