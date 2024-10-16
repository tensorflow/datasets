# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from collections.abc import Iterator, Mapping, Sequence
import dataclasses
import functools
import os
import tempfile
from unittest import mock

from absl.testing import parameterized
import dill
from etils import epath
import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import download
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import load
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import split_builder
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.data_sources import array_record
from tensorflow_datasets.core.download import download_manager
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.testing.dummy_config_based_datasets.dummy_ds_1 import dummy_ds_1_dataset_builder


DummyDatasetSharedGenerator = testing.DummyDatasetSharedGenerator


@dataclasses.dataclass
class DummyBuilderConfig(dataset_builder.BuilderConfig):
  increment: int = 0


class DummyDatasetWithConfigs(dataset_builder.GeneratorBasedBuilder):
  BUILDER_CONFIGS = [
      DummyBuilderConfig(
          name="plus1",
          version=utils.Version("0.0.1"),
          description="Add 1 to the records",
          tags=["foo:bar"],
          increment=1,
      ),
      DummyBuilderConfig(
          name="plus2",
          version=utils.Version("0.0.2"),
          supported_versions=[utils.Version("0.0.1")],
          description="Add 2 to the records",
          tags=["foo:baz"],
          increment=2,
      ),
  ]

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"x": np.int64}),
        supervised_keys=("x", "x"),
    )

  def _split_generators(self, dl_manager):
    del dl_manager
    return {
        "train": self._generate_examples(range(20)),
        "test": self._generate_examples(range(20, 30)),
    }

  def _generate_examples(self, range_):
    for i in range_:
      x = i
      if self.builder_config:
        x += self.builder_config.increment
      yield i, {"x": x}


class DummyDatasetWithBlockedVersions(DummyDatasetWithConfigs):

  BLOCKED_VERSIONS = utils.BlockedVersions(
      versions={"0.0.1": "Version 0.0.1 is blocked"},
      configs={"0.0.2": {"plus2": "plus2 is blocked for version 0.0.2"}},
  )


class DummyDatasetWithDefaultConfig(DummyDatasetWithConfigs):
  DEFAULT_BUILDER_CONFIG_NAME = "plus2"


class DummyDatasetWithVersionedConfigs(dataset_builder.GeneratorBasedBuilder):
  """Builder that has multiple versions of the same config name."""

  SUPPORTED_VERSIONS = [utils.Version("0.0.1"), utils.Version("0.0.2")]
  BUILDER_CONFIGS = [
      DummyBuilderConfig(
          name="cfg1",
          version=utils.Version("0.0.1"),
          increment=0,
      ),
      DummyBuilderConfig(
          name="cfg1",
          version=utils.Version("0.0.2"),
          increment=1,
      ),
  ]

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"x": np.int64}),
        supervised_keys=("x", "x"),
    )

  def _split_generators(self, dl_manager):
    del dl_manager
    return {"train": self._generate_examples(range(20))}

  def _generate_examples(self, range_):
    for i in range_:
      x = i + self.builder_config.increment
      yield i, {"x": x}


class InvalidSplitDataset(DummyDatasetWithConfigs):

  def _split_generators(self, _):
    # Error: ALL cannot be used as Split key
    return {"all": self._generate_examples(range(5))}


class ShardBuilder(dataset_builder.ShardBasedBuilder):
  VERSION = utils.Version("0.0.1")
  BUILDER_CONFIGS = [DummyBuilderConfig(name="cfg1")]

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"x": np.int64}),
    )

  def _shard_iterators_per_split(
      self, dl_manager: download_manager.DownloadManager
  ) -> Mapping[str, Sequence[Iterator[split_builder.KeyExample]]]:
    del dl_manager

    def gen_examples(
        start: int, end: int
    ) -> Iterator[split_builder.KeyExample]:
      for i in range(start, end):
        yield i, {"x": i}

    return {
        # train split has 2 shards
        "train": [
            functools.partial(gen_examples, start=0, end=10),
            functools.partial(gen_examples, start=10, end=20),
        ],
        "test": [functools.partial(gen_examples, start=100, end=110)],
    }


class ShardBuilderTest(testing.TestCase):

  def test_download_and_prepare(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = ShardBuilder(data_dir=tmp_dir, config="cfg1", version="0.0.1")
      builder.download_and_prepare(file_format="array_record")
      actual_data = list(builder.as_data_source(split="train"))
      self.assertEqual(
          actual_data,
          [{"x": i} for i in range(20)],
      )


class GetBuilderDatadirPathTest(testing.TestCase):

  def test_builder_data_dir_path_is_correct(self):
    with mock.patch.object(
        epath, "resource_path", return_value=epath.Path("/base/path")
    ):
      path = dataset_builder._get_builder_datadir_path(
          dummy_ds_1_dataset_builder.Builder
      )
    self.assertEqual(
        os.fspath(path),
        "/base/path/testing/dummy_config_based_datasets/dummy_ds_1",
    )


class ConfigBasedBuilderTest(testing.TestCase):

  def test_get_metadata(self):
    builder_cls = dummy_ds_1_dataset_builder.Builder()
    metadata = builder_cls.get_metadata()
    self.assertEqual(metadata.tags, ["content.data-type.image"])

  def test_dummy_ds_1_read_from_config(self):
    ds_builder = dummy_ds_1_dataset_builder.Builder()
    info = ds_builder._info()
    self.assertEqual(
        info.description,
        "Description of `dummy_ds_1` dummy config-based dataset.",
    )
    self.assertEqual(
        info.citation,
        """@Article{google22tfds,
author = "The TFDS team",
title = "TFDS: a collection of ready-to-use datasets for use with TensorFlow, Jax, and other Machine Learning frameworks.",
journal = "ML gazette",
year = "2022"
}""",
    )


class DatasetBuilderTest(parameterized.TestCase, testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DatasetBuilderTest, cls).setUpClass()
    cls.builder = DummyDatasetSharedGenerator(
        data_dir=os.path.join(tempfile.gettempdir(), "tfds")
    )
    cls.builder.download_and_prepare()

  @testing.run_in_graph_and_eager_modes()
  def test_load(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      dataset = load.load(
          name="dummy_dataset_with_configs",
          data_dir=tmp_dir,
          download=True,
          split=splits_lib.Split.TRAIN,
      )
      data = list(dataset_utils.as_numpy(dataset))
      self.assertLen(data, 20)
      self.assertLess(data[0]["x"], 30)

  # Disable test until dependency on Riegeli is fixed.
  # @testing.run_in_graph_and_eager_modes()
  # def test_load_with_specified_format(self):
  #   with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
  #     dataset, ds_info = load.load(
  #         name="dummy_dataset_with_configs",
  #         with_info=True,
  #         data_dir=tmp_dir,
  #         download=True,
  #         split=splits_lib.Split.TRAIN,
  #         download_and_prepare_kwargs={"file_format": "riegeli"})
  #     self.assertEqual(ds_info.file_format.name, "RIEGELI")
  #     files = tf.io.gfile.listdir(
  #         os.path.join(tmp_dir, "dummy_dataset_with_configs",
  #                      "plus1", "0.0.1"))
  #     self.assertSetEqual(
  #         set(files), {
  #             "dummy_dataset_with_configs-test.riegeli-00000-of-00001",
  #             "dummy_dataset_with_configs-test.riegeli-00000-of-00001_index.json",
  #             "dummy_dataset_with_configs-train.riegeli-00000-of-00001",
  #             "dummy_dataset_with_configs-train.riegeli-00000-of-00001_index.json",
  #             "features.json",
  #             "dataset_info.json",
  #         })
  #     data = list(dataset_utils.as_numpy(dataset))
  #     self.assertEqual(20, len(data))
  #     self.assertLess(data[0]["x"], 30)

  @testing.run_in_graph_and_eager_modes()
  def test_determinism(self):
    ds = self.builder.as_dataset(
        split=splits_lib.Split.TRAIN, shuffle_files=False
    )
    ds_values = list(dataset_utils.as_numpy(ds))

    # Ensure determinism. If this test fail, this mean that numpy random
    # module isn't always determinist (maybe between version, architecture,
    # ...), and so our datasets aren't guaranteed either.
    l = list(range(20))
    np.random.RandomState(42).shuffle(l)
    self.assertEqual(
        l,
        [0, 17, 15, 1, 8, 5, 11, 3, 18, 16, 13, 2, 9, 19, 4, 12, 7, 10, 14, 6],
    )

    # Ensure determinism. If this test fails, this mean the dataset are not
    # deterministically generated.
    self.assertEqual(
        [e["x"] for e in ds_values],
        [6, 16, 19, 12, 14, 18, 5, 13, 15, 4, 10, 17, 0, 8, 3, 1, 9, 7, 11, 2],
    )

  @testing.run_in_graph_and_eager_modes()
  def test_load_from_gcs(self):
    from tensorflow_datasets.image_classification import mnist  # pylint:disable=import-outside-toplevel,g-import-not-at-top

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      with mock.patch.object(
          mnist.MNIST, "_download_and_prepare", side_effect=NotImplementedError
      ):
        # Make sure the dataset cannot be generated.
        with self.assertRaises(NotImplementedError):
          load.load(name="mnist", data_dir=tmp_dir)
        # Enable GCS access so that dataset will be loaded from GCS.
        with testing.enable_gcs_access():
          _, info = load.load(name="mnist", data_dir=tmp_dir, with_info=True)
      self.assertSetEqual(
          set([
              "dataset_info.json",
              "features.json",
              "image.image.json",
              "mnist-test.tfrecord-00000-of-00001",
              "mnist-train.tfrecord-00000-of-00001",
          ]),
          set(tf.io.gfile.listdir(os.path.join(tmp_dir, "mnist/3.0.1"))),
      )

      self.assertEqual(set(info.splits.keys()), set(["train", "test"]))

  @testing.run_in_graph_and_eager_modes()
  def test_multi_split(self):
    ds_train, ds_test = self.builder.as_dataset(
        split=["train", "test"], shuffle_files=False
    )

    data = list(dataset_utils.as_numpy(ds_train))
    self.assertLen(data, 20)

    data = list(dataset_utils.as_numpy(ds_test))
    self.assertLen(data, 10)

  def test_build_data_dir(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = DummyDatasetSharedGenerator(data_dir=tmp_dir)
      self.assertEqual(str(builder.info.version), "1.0.0")

      builder_dir = file_utils.get_dataset_dir(
          data_dir=tmp_dir, builder_name=builder.name
      )
      version_dir = builder_dir / "1.0.0"

      # The dataset folder contains multiple other versions
      (builder_dir / "14.0.0.invalid").mkdir(parents=True, exist_ok=True)
      (builder_dir / "10.0.0").mkdir(parents=True, exist_ok=True)
      (builder_dir / "9.0.0").mkdir(parents=True, exist_ok=True)
      (builder_dir / "0.1.0").mkdir(parents=True, exist_ok=True)

      # The builder's version dir is chosen
      self.assertEqual(builder.data_path, version_dir)

  def test_get_data_dir_with_config(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      config_name = "plus1"
      builder = DummyDatasetWithConfigs(config=config_name, data_dir=tmp_dir)

      version_dir = file_utils.get_dataset_dir(
          data_dir=tmp_dir,
          builder_name=builder.name,
          config_name=config_name,
          version="0.0.1",
      )

      self.assertEqual(builder.data_path, version_dir)

  def test_config_construction(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      self.assertSetEqual(
          set(["plus1", "plus2"]),
          set(DummyDatasetWithConfigs.builder_configs.keys()),
      )
      plus1_config = DummyDatasetWithConfigs.builder_configs["plus1"]
      builder = DummyDatasetWithConfigs(config="plus1", data_dir=tmp_dir)
      self.assertIs(plus1_config, builder.builder_config)
      builder = DummyDatasetWithConfigs(config=plus1_config, data_dir=tmp_dir)
      self.assertIs(plus1_config, builder.builder_config)
      self.assertIs(
          builder.builder_config, DummyDatasetWithConfigs.default_builder_config
      )

  @testing.run_in_graph_and_eager_modes()
  def test_with_configs(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder1 = DummyDatasetWithConfigs(config="plus1", data_dir=tmp_dir)
      builder2 = DummyDatasetWithConfigs(config="plus2", data_dir=tmp_dir)
      # Test that builder.builder_config is the correct config
      self.assertIs(
          builder1.builder_config,
          DummyDatasetWithConfigs.builder_configs["plus1"],
      )
      self.assertIs(
          builder2.builder_config,
          DummyDatasetWithConfigs.builder_configs["plus2"],
      )
      builder1.download_and_prepare()
      builder2.download_and_prepare()
      data_dir1 = os.path.join(tmp_dir, builder1.name, "plus1", "0.0.1")
      data_dir2 = os.path.join(tmp_dir, builder2.name, "plus2", "0.0.2")
      # Test that subdirectories were created per config
      self.assertTrue(tf.io.gfile.exists(data_dir1))
      self.assertTrue(tf.io.gfile.exists(data_dir2))
      # 1 train shard, 1 test shard, plus metadata files
      self.assertGreater(len(tf.io.gfile.listdir(data_dir1)), 2)
      self.assertGreater(len(tf.io.gfile.listdir(data_dir2)), 2)

      # Test that the config was used and they didn't collide.
      splits_list = ["train", "test"]
      for builder, incr in [(builder1, 1), (builder2, 2)]:
        train_data, test_data = [  # pylint: disable=g-complex-comprehension
            [
                el["x"]
                for el in dataset_utils.as_numpy(  # pylint: disable=g-complex-comprehension
                    builder.as_dataset(split=split)
                )
            ]
            for split in splits_list
        ]

        self.assertLen(train_data, 20)
        self.assertLen(test_data, 10)
        self.assertCountEqual(
            [incr + el for el in range(30)], train_data + test_data
        )

  def test_default_builder_config(self):
    self.assertEqual(
        DummyDatasetWithConfigs.default_builder_config.name, "plus1"
    )
    self.assertEqual(
        DummyDatasetWithDefaultConfig.default_builder_config.name, "plus2"
    )

  def test_builder_configs_configs_with_multiple_versions(self):
    self.assertSetEqual(
        set(["cfg1:0.0.1", "cfg1:0.0.2"]),
        set(DummyDatasetWithVersionedConfigs.builder_configs.keys()),
    )

  def test_get_builder_config(self):
    plus1 = DummyDatasetWithConfigs.get_builder_config("plus1")
    self.assertEqual(plus1.name, "plus1")
    plus2 = DummyDatasetWithConfigs.get_builder_config("plus2")
    self.assertEqual(plus2.name, "plus2")

    plus1_001 = DummyDatasetWithConfigs.get_builder_config(
        "plus1", version="0.0.1"
    )
    self.assertEqual(plus1_001.name, "plus1")
    self.assertEqual(str(plus1_001.version), "0.0.1")

    plus2_002 = DummyDatasetWithConfigs.get_builder_config(
        "plus2", version="0.0.2"
    )
    self.assertEqual(plus2_002.name, "plus2")
    self.assertEqual(str(plus2_002.version), "0.0.2")

    self.assertIsNone(
        DummyDatasetWithConfigs.get_builder_config(
            "i_dont_exist", version="0.0.1"
        )
    )

    # DummyDatasetWithVersionedConfigs
    cfg1_001 = DummyDatasetWithVersionedConfigs.get_builder_config(
        "cfg1", version="0.0.1"
    )
    self.assertEqual(cfg1_001.name, "cfg1")
    self.assertEqual(str(cfg1_001.version), "0.0.1")

    cfg1_002 = DummyDatasetWithVersionedConfigs.get_builder_config(
        "cfg1", version="0.0.2"
    )
    self.assertEqual(cfg1_002.name, "cfg1")
    self.assertEqual(str(cfg1_002.version), "0.0.2")

    self.assertIsNone(
        DummyDatasetWithVersionedConfigs.get_builder_config(
            "cfg1", version="0.0.3"
        )
    )

  def test_is_blocked(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      tmp_dir = epath.Path(tmp_dir)
      builder_1 = DummyDatasetWithBlockedVersions(
          config="plus1", version="0.0.1", data_dir=tmp_dir
      )
      builder_2 = DummyDatasetWithBlockedVersions(
          config="plus2", version="0.0.2", data_dir=tmp_dir
      )
      not_blocked_builder = DummyDatasetWithConfigs(
          config="plus1", version="0.0.1", data_dir=tmp_dir
      )
      assert builder_1.is_blocked()
      assert builder_2.is_blocked()
      assert not not_blocked_builder.is_blocked()

  def test_assert_is_not_blocked(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      tmp_dir = epath.Path(tmp_dir)
      builder_1 = DummyDatasetWithBlockedVersions(
          config="plus1", version="0.0.1", data_dir=tmp_dir
      )
      builder_2 = DummyDatasetWithBlockedVersions(
          config="plus2", version="0.0.2", data_dir=tmp_dir
      )
      builder_3 = DummyDatasetWithBlockedVersions(
          config="plus2", version="0.0.1", data_dir=tmp_dir
      )
      not_blocked_builder = DummyDatasetWithConfigs(
          config="plus1", version="0.0.1", data_dir=tmp_dir
      )

      assert builder_1.blocked_versions is not None
      assert builder_2.blocked_versions is not None
      assert builder_3.blocked_versions is not None
      assert not_blocked_builder.blocked_versions is None

      with pytest.raises(
          utils.DatasetVariantBlockedError, match="Version 0.0.1 is blocked"
      ):
        assert builder_1.assert_is_not_blocked()
      with pytest.raises(
          utils.DatasetVariantBlockedError,
          match="plus2 is blocked for version 0.0.2",
      ):
        assert builder_2.assert_is_not_blocked()
      with pytest.raises(
          utils.DatasetVariantBlockedError, match="Version 0.0.1 is blocked"
      ):
        assert builder_3.assert_is_not_blocked()
      assert not_blocked_builder.assert_is_not_blocked() is None

  def test_blocked_as_dataset_and_as_data_source(self):
    for config, version, expected_msg in [
        ("plus1", "0.0.1", "Version 0.0.1 is blocked"),
        ("plus2", "0.0.2", "plus2 is blocked for version 0.0.2"),
    ]:
      with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
        tmp_dir = epath.Path(tmp_dir)
        blocked_builder = DummyDatasetWithBlockedVersions(
            config=config, version=version, data_dir=tmp_dir
        )
        with pytest.raises(
            utils.DatasetVariantBlockedError, match=expected_msg
        ):
          blocked_builder.as_dataset()
        with pytest.raises(
            utils.DatasetVariantBlockedError, match=expected_msg
        ):
          blocked_builder.as_data_source()

  def test_versioned_configs(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      tmp_dir = epath.Path(tmp_dir)
      builder1 = DummyDatasetWithVersionedConfigs(
          config="cfg1", version="0.0.1", data_dir=tmp_dir
      )
      builder2 = DummyDatasetWithVersionedConfigs(
          config="cfg1", version="0.0.2", data_dir=tmp_dir
      )
      builder1.download_and_prepare()
      builder2.download_and_prepare()
      data_dir1 = tmp_dir / builder1.name / "cfg1" / "0.0.1"
      data_dir2 = tmp_dir / builder2.name / "cfg1" / "0.0.2"
      # 1 train shard plus metadata files
      self.assertGreaterEqual(len(list(data_dir1.iterdir())), 3)
      self.assertGreaterEqual(len(list(data_dir2.iterdir())), 3)
      ds1 = builder1.as_dataset(split="train")
      total1 = sum(el["x"] for el in dataset_utils.as_numpy(ds1))
      ds2 = builder2.as_dataset(split="train")
      total2 = sum(el["x"] for el in dataset_utils.as_numpy(ds2))
      self.assertEqual(total1, 190)
      self.assertEqual(total2, 210)

  def test_read_config(self):
    is_called = []

    def interleave_sort(lists):
      is_called.append(True)
      return lists

    read_config = read_config_lib.ReadConfig(
        experimental_interleave_sort_fn=interleave_sort,
    )
    read_config.options.experimental_slack = True
    ds = self.builder.as_dataset(
        split="train",
        read_config=read_config,
        shuffle_files=True,
    )

    # Check that the ReadConfig options are properly set
    self.assertTrue(ds.options().experimental_slack)

    # The instruction function should have been called
    self.assertEqual(is_called, [True])

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

  def test_generate_old_versions(self):
    class MultiVersionDataset(dataset_builder.GeneratorBasedBuilder):
      VERSION = utils.Version("1.0.0")
      SUPPORTED_VERSIONS = [
          utils.Version("2.0.0"),
          utils.Version("1.9.0"),  # Cannot be generated
          utils.Version("0.0.8"),  # Cannot be generated
      ]

      def _info(self):
        return dataset_info.DatasetInfo(builder=self)

      def _split_generators(self, dl_manager):
        return []

      def _generate_examples(self):
        yield "", {}

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = MultiVersionDataset(version="0.0.8", data_dir=tmp_dir)
      with self.assertRaisesWithPredicateMatch(ValueError, "0.0.8) is too old"):
        builder.download_and_prepare()

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = MultiVersionDataset(version="1.9.0", data_dir=tmp_dir)
      with self.assertRaisesWithPredicateMatch(ValueError, "1.9.0) is too old"):
        builder.download_and_prepare()

    # `experimental_latest` version can be installed
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = MultiVersionDataset(version="2.0.0", data_dir=tmp_dir)
      builder.download_and_prepare()

  def test_invalid_split_dataset(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      with self.assertRaisesWithPredicateMatch(
          ValueError, "`all` is a reserved keyword"
      ):
        # Raise error during .download_and_prepare()
        load.load(
            name="invalid_split_dataset",
            data_dir=tmp_dir,
        )

  def test_global_version(self):
    global_version = utils.Version("1.0.0")
    global_release_notes = {
        "1.0.0": "Global release",
    }
    config_version = utils.Version("1.1.0")
    config_release_notes = {
        "1.1.0": "Some update",
    }

    class VersionDummyDataset(DummyDatasetWithConfigs):
      BUILDER_CONFIGS = [
          dataset_builder.BuilderConfig(
              name="default",
              description="Add 1 to the records",
          ),
          dataset_builder.BuilderConfig(
              name="custom",
              description="Add 2 to the records",
              version=config_version,
              release_notes=config_release_notes,
          ),
      ]
      VERSION = global_version
      RELEASE_NOTES = global_release_notes

    tmp_path = "/tmp/non-existing-dir/"

    # If version is not specified at the BuilderConfig level, then
    # the default global values are used.
    builder = VersionDummyDataset(config="default", data_dir=tmp_path)
    self.assertEqual(builder.version, global_version)
    self.assertEqual(builder.release_notes, global_release_notes)

    builder = VersionDummyDataset(config="custom", data_dir=tmp_path)
    self.assertEqual(builder.version, config_version)
    self.assertEqual(builder.release_notes, config_release_notes)

  def test_get_reference(self):
    tmp_dir = self.get_temp_dir()
    builder = DummyDatasetWithConfigs(config="plus1", data_dir=tmp_dir)
    reference = builder.get_reference()
    expected_reference = naming.DatasetReference(
        dataset_name="dummy_dataset_with_configs",
        config="plus1",
        version="0.0.1",
        data_dir=epath.Path(tmp_dir),
    )
    self.assertEqual(reference, expected_reference)

  def test_get_file_spec(self):
    builder = DummyDatasetWithConfigs(
        config="plus1", data_dir=self.get_temp_dir()
    )
    builder.download_and_prepare()
    self.assertEndsWith(
        builder.get_file_spec("train"),
        "dummy_dataset_with_configs/plus1/0.0.1/dummy_dataset_with_configs-train.tfrecord@1",
    )
    self.assertEndsWith(
        builder.get_file_spec("test"),
        "dummy_dataset_with_configs/plus1/0.0.1/dummy_dataset_with_configs-test.tfrecord@1",
    )

  def test_load_as_data_source(self):
    data_dir = self.get_temp_dir()
    builder = DummyDatasetWithConfigs(
        data_dir=data_dir,
        config="plus1",
        file_format=file_adapters.FileFormat.ARRAY_RECORD,
    )
    builder.download_and_prepare()

    data_source = builder.as_data_source()
    assert isinstance(data_source, dict)
    assert isinstance(data_source["train"], array_record.ArrayRecordDataSource)
    assert isinstance(data_source["test"], array_record.ArrayRecordDataSource)
    assert len(data_source["test"]) == 10
    assert data_source["test"][0]["x"] == 28
    assert len(data_source["train"]) == 20
    assert data_source["train"][0]["x"] == 7

    data_source = builder.as_data_source(split="test")
    assert isinstance(data_source, array_record.ArrayRecordDataSource)
    assert len(data_source) == 10
    assert data_source[0]["x"] == 28

  def test_load_as_data_source_alternative_file_format(self):
    data_dir = self.get_temp_dir()
    builder = DummyDatasetWithConfigs(
        data_dir=data_dir,
        config="plus1",
        file_format=file_adapters.FileFormat.ARRAY_RECORD,
    )
    builder.download_and_prepare()
    # Change the default file format and add alternative file format.
    builder.info.as_proto.file_format = "tfrecord"
    builder.info.add_alternative_file_format("array_record")

    data_source = builder.as_data_source()
    assert isinstance(data_source, dict)
    assert isinstance(data_source["train"], array_record.ArrayRecordDataSource)
    assert isinstance(data_source["test"], array_record.ArrayRecordDataSource)
    assert len(data_source["test"]) == 10
    assert data_source["test"][0]["x"] == 28
    assert len(data_source["train"]) == 20
    assert data_source["train"][0]["x"] == 7

    data_source = builder.as_data_source(split="test")
    assert isinstance(data_source, array_record.ArrayRecordDataSource)
    assert len(data_source) == 10
    assert data_source[0]["x"] == 28

  @parameterized.named_parameters(
      *[
          {"file_format": file_format, "testcase_name": file_format.value}
          for file_format in file_adapters.FileFormat
          if file_format not in file_adapters.FileFormat.with_random_access()
          and file_format != file_adapters.FileFormat.RIEGELI
      ],
  )
  def test_unsupported_file_formats_raise_error(self, file_format):
    data_dir = self.get_temp_dir()
    builder = DummyDatasetWithConfigs(
        data_dir=data_dir,
        config="plus1",
        file_format=file_format,
    )
    builder.download_and_prepare()
    with pytest.raises(
        NotImplementedError,
        match="Random access data source for file format",
    ):
      builder.as_data_source(split="train")


class DatasetBuilderMultiDirTest(testing.TestCase):
  """Tests for multi-dir."""

  @classmethod
  def setUpClass(cls):
    super(DatasetBuilderMultiDirTest, cls).setUpClass()
    cls.builder = DummyDatasetSharedGenerator()

  def setUp(self):
    super(DatasetBuilderMultiDirTest, self).setUp()
    # Sanity check to make sure that no dir is registered
    file_utils.clear_registered_data_dirs()
    # Create a new temp dir
    self.other_data_dir = os.path.join(self.get_temp_dir(), "other_dir")
    # Overwrite the default data_dir (as files get created)

    self._original_data_dir = constants.DATA_DIR
    constants.DATA_DIR = os.path.join(self.get_temp_dir(), "default_dir")
    self.default_data_dir = constants.DATA_DIR

  def tearDown(self):
    super(DatasetBuilderMultiDirTest, self).tearDown()
    # Restore to the default `_registered_data_dir`
    file_utils._registered_data_dir = set()
    # Clear-up existing dirs
    if tf.io.gfile.exists(self.other_data_dir):
      tf.io.gfile.rmtree(self.other_data_dir)
    if tf.io.gfile.exists(self.default_data_dir):
      tf.io.gfile.rmtree(self.default_data_dir)
    # Restore the orgininal data dir
    constants.DATA_DIR = self._original_data_dir

  def test_load_data_dir(self):
    """Ensure that `tfds.load` also supports multiple data_dir."""
    file_utils.add_data_dir(self.other_data_dir)

    class MultiDirDataset(DummyDatasetSharedGenerator):  # pylint: disable=unused-variable
      VERSION = utils.Version("1.2.0")

    data_dir = os.path.join(self.other_data_dir, "multi_dir_dataset", "1.2.0")
    tf.io.gfile.makedirs(data_dir)

    with mock.patch.object(dataset_info.DatasetInfo, "read_from_directory"):
      _, info = load.load("multi_dir_dataset", split=[], with_info=True)
    self.assertEqual(info.data_dir, data_dir)


class DummyOrderedDataset(dataset_builder.GeneratorBasedBuilder):
  VERSION = utils.Version("1.0.0")

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"x": np.int64}),
        disable_shuffling=True,
    )

  def _split_generators(self, dl_manager):
    del dl_manager
    return {"train": self._generate_examples(range_=range(500))}

  def _generate_examples(self, range_):
    for i in range_:
      yield i, {"x": i}


class OrderedDatasetBuilderTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(OrderedDatasetBuilderTest, cls).setUpClass()
    cls.builder = DummyOrderedDataset(
        data_dir=os.path.join(tempfile.gettempdir(), "tfds")
    )
    cls.builder.download_and_prepare(
        download_config=download.DownloadConfig(num_shards=10)
    )

  @testing.run_in_graph_and_eager_modes()
  def test_sorted_by_key(self):
    # For ordered dataset ReadConfig.interleave_cycle_length=1 by default
    read_config = read_config_lib.ReadConfig()
    ds = self.builder.as_dataset(
        split=splits_lib.Split.TRAIN,
        shuffle_files=False,
        read_config=read_config,
    )
    ds_values = list(dataset_utils.as_numpy(ds))
    self.assertListEqual(
        self.builder.info.splits["train"].shard_lengths, [50] * 10
    )
    self.assertEqual(
        [e["x"] for e in ds_values],
        list(range(500)),
    )


class BuilderPickleTest(testing.TestCase):

  def test_load_dump(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = testing.DummyMnist(data_dir=tmp_dir)
    builder2 = dill.loads(dill.dumps(builder))
    self.assertEqual(builder.name, builder2.name)
    self.assertEqual(builder.version, builder2.version)


class BuilderRestoreGcsTest(testing.TestCase):

  def setUp(self):
    super(BuilderRestoreGcsTest, self).setUp()

    def load_mnist_dataset_info(self):
      mnist_info_path = os.path.join(
          utils.tfds_path(),
          "testing/test_data/dataset_info/mnist/3.0.1",
      )
      mnist_info_path = os.path.normpath(mnist_info_path)
      self.read_from_directory(mnist_info_path)

    patcher = mock.patch.object(
        dataset_info.DatasetInfo,
        "initialize_from_bucket",
        new=load_mnist_dataset_info,
    )
    patcher.start()
    self.patch_gcs = patcher
    self.addCleanup(patcher.stop)

  def test_stats_restored_from_gcs(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = testing.DummyMnist(data_dir=tmp_dir)
      self.assertEqual(builder.info.splits["train"].num_examples, 20)

  def test_stats_not_restored_gcs_overwritten(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # If split are different that the one restored, stats should be recomputed
      builder = testing.DummyMnist(data_dir=tmp_dir)
      self.assertEqual(builder.info.splits["train"].num_examples, 20)

  def test_gcs_not_exists(self):
    # By disabling the patch, and because DummyMnist is not on GCS, we can
    # simulate a new dataset starting from scratch
    self.patch_gcs.stop()
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = testing.DummyMnist(data_dir=tmp_dir)
      # No dataset_info restored, so stats are empty
      self.assertEqual(builder.info.splits.total_num_examples, 0)

      dl_config = download.DownloadConfig()
      builder.download_and_prepare(download_config=dl_config)

      # Statistics should have been recomputed
      self.assertEqual(builder.info.splits["train"].num_examples, 20)
    self.patch_gcs.start()


class DatasetBuilderGenerateModeTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DatasetBuilderGenerateModeTest, cls).setUpClass()

  def test_reuse_cache_if_exists(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = testing.DummyMnist(data_dir=tmp_dir)
      dl_config = download.DownloadConfig(max_examples_per_split=3)
      builder.download_and_prepare(download_config=dl_config)

      dl_config = download.DownloadConfig(
          download_mode=download.GenerateMode.REUSE_CACHE_IF_EXISTS,
          max_examples_per_split=5,
      )
      builder.download_and_prepare(download_config=dl_config)
      self.assertEqual(builder.info.splits["train"].num_examples, 5)

  def test_update_dataset_info_keeps_data_source(
      self,
  ):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = testing.DummyMnist(data_dir=tmp_dir)
      with mock.patch.object(tf.data, "TFRecordDataset") as mock_read:
        builder.read_tfrecord_as_dataset("/x/y")
        mock_read.assert_called_once_with(
            filenames=["/x/y"],
            compression_type=None,
            num_parallel_reads=None,
        )
      info_proto = builder.info.as_proto
      assert len(info_proto.data_source_accesses) == 1
      assert info_proto.data_source_accesses[0].file_system.path == "/x/y"
      builder.download_and_prepare()
      # Manually check information was indeed written in dataset_info.json and
      # can be reloaded:
      builder = testing.DummyMnist(data_dir=tmp_dir)
      info_proto = builder.info.as_proto
      assert len(info_proto.data_source_accesses) == 1
      assert info_proto.data_source_accesses[0].file_system.path == "/x/y"
      assert info_proto.description == "Mnist description."
      # Re-generate the info file with a different description:
      dl_config = download.DownloadConfig(
          download_mode=download.GenerateMode.UPDATE_DATASET_INFO,
      )
      info_proto.description = "new description"
      builder.download_and_prepare(download_config=dl_config)
      # New description is available after calling download_and_prepare:
      assert info_proto.description == "new description"
      # Then check that data_source is still there, and description was builder
      builder = read_only_builder.builder_from_files(
          builder.name,
          data_dir=tmp_dir,
      )
      info_proto = builder.info.as_proto
      assert len(info_proto.data_source_accesses) == 1
      assert info_proto.data_source_accesses[0].file_system.path == "/x/y"
      assert info_proto.description == "new description"


class DatasetBuilderReadTest(testing.TestCase):
  NUM_SHARDS = None  # Automatically infers the number based on size.

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    builder = DummyDatasetSharedGenerator(data_dir=cls._tfds_tmp_dir)
    builder.download_and_prepare(
        download_config=download.DownloadConfig(num_shards=cls.NUM_SHARDS)
    )

  @classmethod
  def tearDownClass(cls):
    super().tearDownClass()
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  def setUp(self):
    super(DatasetBuilderReadTest, self).setUp()
    self.builder = DummyDatasetSharedGenerator(data_dir=self._tfds_tmp_dir)

  @testing.run_in_graph_and_eager_modes()
  def test_all_splits(self):
    splits = dataset_utils.as_numpy(self.builder.as_dataset(batch_size=-1))
    self.assertSetEqual(
        set(splits.keys()), set([splits_lib.Split.TRAIN, splits_lib.Split.TEST])
    )

    # Test that enum and string both access same object
    self.assertIs(splits["train"], splits[splits_lib.Split.TRAIN])
    self.assertIs(splits["test"], splits[splits_lib.Split.TEST])

    train_data = splits[splits_lib.Split.TRAIN]["x"]
    test_data = splits[splits_lib.Split.TEST]["x"]
    self.assertLen(train_data, 20)
    self.assertLen(test_data, 10)
    self.assertEqual(sum(range(30)), int(train_data.sum() + test_data.sum()))

  @testing.run_in_graph_and_eager_modes()
  def test_with_batch_size(self):
    items = list(
        dataset_utils.as_numpy(
            self.builder.as_dataset(split="train+test", batch_size=10)
        )
    )
    # 3 batches of 10
    self.assertLen(items, 3)
    x1, x2, x3 = items[0]["x"], items[1]["x"], items[2]["x"]
    self.assertEqual(10, x1.shape[0])
    self.assertEqual(10, x2.shape[0])
    self.assertEqual(10, x3.shape[0])
    self.assertEqual(sum(range(30)), int(x1.sum() + x2.sum() + x3.sum()))

    # By default batch_size is None and won't add a batch dimension
    ds = self.builder.as_dataset(split=splits_lib.Split.TRAIN)
    self.assertEmpty(ds.element_spec["x"].shape)
    # Setting batch_size=1 will add an extra batch dimension
    ds = self.builder.as_dataset(split=splits_lib.Split.TRAIN, batch_size=1)
    self.assertLen(ds.element_spec["x"].shape, 1)
    # Setting batch_size=2 will add an extra batch dimension
    ds = self.builder.as_dataset(split=splits_lib.Split.TRAIN, batch_size=2)
    self.assertLen(ds.element_spec["x"].shape, 1)

  def test_autocache(self):
    # All the following should cache

    # Default should cache as dataset is small and has a single shard
    self.assertTrue(
        self.builder._should_cache_ds(
            split="train",
            shuffle_files=True,
            read_config=read_config_lib.ReadConfig(),
        )
    )

    # Multiple shards should cache when shuffling is disabled
    self.assertTrue(
        self.builder._should_cache_ds(
            split="train+test",
            shuffle_files=False,
            read_config=read_config_lib.ReadConfig(),
        )
    )

    # Multiple shards should cache when re-shuffling is disabled
    self.assertTrue(
        self.builder._should_cache_ds(
            split="train+test",
            shuffle_files=True,
            read_config=read_config_lib.ReadConfig(
                shuffle_reshuffle_each_iteration=False
            ),
        )
    )

    # Sub-split API can cache if only a single shard is selected.
    self.assertTrue(
        self.builder._should_cache_ds(
            split="train+test[:0]",
            shuffle_files=True,
            read_config=read_config_lib.ReadConfig(),
        )
    )

    # All the following should NOT cache

    # Default should not cache if try_autocache is disabled
    self.assertFalse(
        self.builder._should_cache_ds(
            split="train",
            shuffle_files=True,
            read_config=read_config_lib.ReadConfig(try_autocache=False),
        )
    )

    # Multiple shards should not cache when shuffling is enabled
    self.assertFalse(
        self.builder._should_cache_ds(
            split="train+test",
            shuffle_files=True,
            read_config=read_config_lib.ReadConfig(),
        )
    )

  def test_with_tfds_info(self):
    ds = self.builder.as_dataset(split=splits_lib.Split.TRAIN)
    self.assertEmpty(ds.element_spec["x"].shape)


class DatasetBuilderReadWithMutipleShardsTest(DatasetBuilderReadTest):
  NUM_SHARDS = 3

  def test_autocache(self):
    """Default should not cache as dataset with multiple shards."""
    self.assertFalse(
        self.builder._should_cache_ds(
            split="train",
            shuffle_files=True,
            read_config=read_config_lib.ReadConfig(),
        )
    )

  def test_function_tracing(self):
    """Tests `DatasetBuilder.as_dataset` can be traced with `tf.function`."""

    @tf.function(
        input_signature=(
            tf.TensorSpec((), tf.int64, "num_input_pipelines"),
            tf.TensorSpec((), tf.int64, "input_pipeline_id"),
        ),
        autograph=False,
    )
    def dataset_fn(
        num_input_pipelines: tf.Tensor, input_pipeline_id: tf.Tensor
    ) -> tf.data.Dataset:
      input_context = tf.distribute.InputContext(
          num_input_pipelines, input_pipeline_id
      )
      return self.builder.as_dataset(
          split=splits_lib.Split.TRAIN,
          batch_size=-1,
          read_config=read_config_lib.ReadConfig(input_context=input_context),
      )

    xs = []
    num_input_pipelines = np.array(self.NUM_SHARDS, np.int64)
    for i in range(num_input_pipelines):
      dataset = dataset_fn(num_input_pipelines, np.array(i, np.int64))
      x = dataset_utils.as_numpy(dataset)["x"]
      self.assertBetween(len(x), 6, 7)
      xs.extend(x)
    self.assertCountEqual(xs, range(20))


class DummyDatasetWithSupervisedKeys(DummyDatasetSharedGenerator):

  def __init__(self, *args, supervised_keys=None, **kwargs):
    self.supervised_keys = supervised_keys
    super().__init__(*args, **kwargs)

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"x": np.int64}),
        supervised_keys=self.supervised_keys,
    )


class DatasetBuilderAsSupervisedTest(parameterized.TestCase, testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    builder = DummyDatasetWithSupervisedKeys(data_dir=cls._tfds_tmp_dir)
    builder.download_and_prepare()

  @classmethod
  def tearDownClass(cls):
    super().tearDownClass()
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  @testing.run_in_graph_and_eager_modes()
  def test_supervised_keys_basic(self):
    self.builder = DummyDatasetWithSupervisedKeys(
        data_dir=self._tfds_tmp_dir, supervised_keys=("x", "x")
    )
    x, _ = dataset_utils.as_numpy(
        self.builder.as_dataset(
            split=splits_lib.Split.TRAIN, as_supervised=True, batch_size=-1
        )
    )
    self.assertEqual(x.shape[0], 20)

  def test_supervised_keys_triple(self):
    self.builder = DummyDatasetWithSupervisedKeys(
        data_dir=self._tfds_tmp_dir, supervised_keys=("x", "x", "x")
    )
    result = dataset_utils.as_numpy(
        self.builder.as_dataset(
            split=splits_lib.Split.TRAIN, as_supervised=True, batch_size=-1
        )
    )
    self.assertLen(result, 3)
    self.assertEqual(result[0].shape[0], 20)

  def test_supervised_keys_nested(self):
    self.builder = DummyDatasetWithSupervisedKeys(
        data_dir=self._tfds_tmp_dir,
        supervised_keys=("x", ("x", ("x", "x")), {"a": "x", "b": ("x",)}),
    )
    single, pair, a_dict = dataset_utils.as_numpy(
        self.builder.as_dataset(
            split=splits_lib.Split.TRAIN, as_supervised=True, batch_size=-1
        )
    )
    self.assertEqual(single.shape[0], 20)
    self.assertLen(pair, 2)
    self.assertEqual(pair[1][1].shape[0], 20)
    self.assertLen(a_dict, 2)
    self.assertEqual(a_dict["b"][0].shape[0], 20)

  @parameterized.named_parameters(
      ("not_a_tuple", "x", "tuple of 2 or 3"),
      ("wrong_length_tuple", ("x", "x", "x", "x", "x"), "tuple of 2 or 3"),
      ("wrong_nested_type", ("x", ["x", "x"]), "tuple, dict, str"),
  )
  def test_bad_supervised_keys(self, supervised_keys, error_message):
    with self.assertRaisesRegex(ValueError, error_message):
      self.builder = DummyDatasetWithSupervisedKeys(
          data_dir=self._tfds_tmp_dir,
          # Not a tuple
          supervised_keys=supervised_keys,
      )




class NestedSequenceBuilder(dataset_builder.GeneratorBasedBuilder):
  """Dataset containing nested sequences."""

  VERSION = utils.Version("0.0.1")

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({
            "frames": features.Sequence({
                "coordinates": features.Sequence(
                    features.Tensor(shape=(2,), dtype=tf.int32)
                ),
            }),
        }),
    )

  def _split_generators(self, dl_manager):
    del dl_manager
    return {"train": self._generate_examples()}

  def _generate_examples(self):
    ex0 = [[[0, 1], [2, 3], [4, 5]], [], [[6, 7]]]
    ex1 = []
    ex2 = [
        [[10, 11]],
        [[12, 13], [14, 15]],
    ]
    for i, ex in enumerate([ex0, ex1, ex2]):
      yield i, {"frames": {"coordinates": ex}}


class NestedSequenceBuilderTest(testing.TestCase):
  """Test of the NestedSequenceBuilder."""

  @classmethod
  def setUpClass(cls):
    super(NestedSequenceBuilderTest, cls).setUpClass()
    dataset_builder._is_py2_download_and_prepare_disabled = False

  @classmethod
  def tearDownClass(cls):
    dataset_builder._is_py2_download_and_prepare_disabled = True
    super(NestedSequenceBuilderTest, cls).tearDownClass()

  @testing.run_in_graph_and_eager_modes()
  def test_nested_sequence(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      ds_train, ds_info = load.load(
          name="nested_sequence_builder",
          data_dir=tmp_dir,
          split="train",
          with_info=True,
          shuffle_files=False,
      )
      ex0, ex1, ex2 = [
          ex["frames"]["coordinates"] for ex in dataset_utils.as_numpy(ds_train)
      ]
      self.assertAllEqual(
          ex0,
          tf.ragged.constant(
              [
                  [[0, 1], [2, 3], [4, 5]],
                  [],
                  [[6, 7]],
              ],
              inner_shape=(2,),
          ),
      )
      self.assertAllEqual(ex1, tf.ragged.constant([], ragged_rank=1))
      self.assertAllEqual(
          ex2,
          tf.ragged.constant(
              [
                  [[10, 11]],
                  [[12, 13], [14, 15]],
              ],
              inner_shape=(2,),
          ),
      )

      self.assertEqual(
          ds_info.features.dtype,
          {"frames": {"coordinates": tf.int32}},
      )
      self.assertEqual(
          ds_info.features.shape,
          {"frames": {"coordinates": (None, None, 2)}},
      )
      nested_tensor_info = ds_info.features.get_tensor_info()
      self.assertEqual(
          nested_tensor_info["frames"]["coordinates"].sequence_rank,
          2,
      )


def test_read_tfrecord_as_dataset():
  builder = DummyDatasetWithConfigs()
  with mock.patch.object(tf.data, "TFRecordDataset") as mock_read:
    builder.read_tfrecord_as_dataset("/x/y")
    mock_read.assert_called_once_with(
        filenames=["/x/y"],
        compression_type=None,
        num_parallel_reads=None,
    )
    info_proto = builder.info.as_proto
    assert len(info_proto.data_source_accesses) == 1
    assert info_proto.data_source_accesses[0].file_system.path == "/x/y"




if __name__ == "__main__":
  testing.test_main()
