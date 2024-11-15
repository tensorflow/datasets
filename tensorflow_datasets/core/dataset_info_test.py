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

import json
import os
import pathlib
import re
import tempfile
import time
from typing import Union
from unittest import mock

from etils import epath
import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.image_classification import mnist
from tensorflow_datasets.testing.dummy_config_based_datasets.dummy_ds_1 import dummy_ds_1_dataset_builder

from google.protobuf import text_format


_TFDS_DIR = utils.tfds_path()
_DATA_DIR = os.path.join(_TFDS_DIR, "testing", "test_data", "dataset_info")
_INFO_DIR = os.path.join(_DATA_DIR, "mnist", "3.0.1")
_INFO_DIR_UNLABELED = os.path.join(_DATA_DIR, "mnist_unlabeled", "3.0.1")
_NON_EXISTENT_DIR = os.path.join(_TFDS_DIR, "non_existent_dir")

DummyDatasetSharedGenerator = testing.DummyDatasetSharedGenerator


class RandomShapedImageGenerator(DummyDatasetSharedGenerator):

  BUILDER_CONFIGS = [
      dataset_builder.BuilderConfig(
          name="random_shaped_image_config",
      )
  ]

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({"im": features.Image()}),
        supervised_keys=("im", "im"),
        metadata=dataset_info.MetadataDict(),
    )

  def _generate_examples(self, range_):
    self.info.metadata["some_key"] = 123

    for i in range_:
      height = np.random.randint(5, high=10)
      width = np.random.randint(5, high=10)
      yield i, {
          "im": np.random.randint(
              0, 255, size=(height, width, 3), dtype=np.uint8
          )
      }


class DatasetInfoTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DatasetInfoTest, cls).setUpClass()
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    cls._builder = mnist.MNIST(data_dir=cls._tfds_tmp_dir)

  @classmethod
  def tearDownClass(cls):
    super(DatasetInfoTest, cls).tearDownClass()
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  def test_non_existent_dir(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    with self.assertRaisesWithPredicateMatch(
        FileNotFoundError, "from a directory which does not exist"
    ):
      info.read_from_directory(_NON_EXISTENT_DIR)

  def test_reading_different_version(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info._identity.version = utils.Version("2.0.0")
    with pytest.raises(
        AssertionError,
        match=(
            "The constructed DatasetInfo instance and the restored proto"
            " version do not match"
        ),
    ):
      # The dataset in _INFO_DIR has version 3.0.1 whereas the builder is 2.0.0
      info.read_from_directory(_INFO_DIR)

  def test_reading(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.read_from_directory(_INFO_DIR)

    # Assert that we read the file and initialized DatasetInfo.
    self.assertTrue(info.initialized)
    self.assertEqual("mnist", info.name)
    self.assertEqual("mnist/3.0.1", info.full_name)

    # Test splits are initialized properly.
    split_dict = info.splits

    # Assert they are the correct number.
    self.assertLen(split_dict, 2)

    # Assert on what they are
    self.assertIn("train", split_dict)
    self.assertIn("test", split_dict)

    # Assert that this is computed correctly.
    self.assertEqual(40, info.splits.total_num_examples)
    self.assertEqual(11594722, info.dataset_size)

    self.assertEqual("image", info.supervised_keys[0])
    self.assertEqual("label", info.supervised_keys[1])
    self.assertEqual(
        info.module_name, "tensorflow_datasets.image_classification.mnist"
    )
    self.assertEqual(False, info.disable_shuffling)

    self.assertEqual(info.version, utils.Version("3.0.1"))
    self.assertEqual(info.release_notes, {})

  def test_disable_shuffling(self):
    info = dataset_info.DatasetInfo(
        builder=self._builder, disable_shuffling=True
    )
    info.read_from_directory(_INFO_DIR)

    self.assertEqual(True, info.disable_shuffling)

  def test_reading_empty_properties(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.read_from_directory(_INFO_DIR_UNLABELED)

    # Assert supervised_keys has not been set
    self.assertIsNone(None, info.supervised_keys)

  def test_writing(self):
    # First read in stuff.
    mnist_builder = mnist.MNIST(data_dir=_DATA_DIR)

    info = dataset_info.DatasetInfo(
        builder=mnist_builder, features=mnist_builder.info.features
    )
    info.read_from_directory(_INFO_DIR)

    # Read the json file into a string.
    with tf.io.gfile.GFile(dataset_info.dataset_info_path(_INFO_DIR)) as f:
      existing_json = json.load(f)

    # Now write to a temp directory.
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      info.write_to_directory(tmp_dir)

      # Read the newly written json file into a string.
      with tf.io.gfile.GFile(dataset_info.dataset_info_path(tmp_dir)) as f:
        new_json = json.load(f)

      # Read the newly written LICENSE file into a string.
      with tf.io.gfile.GFile(dataset_info.license_path(tmp_dir)) as f:
        license_ = f.read()

    # Assert what was read and then written and read again is the same.
    self.assertEqual(existing_json, new_json)

    # Assert correct license was written.
    self.assertEqual(existing_json["redistributionInfo"]["license"], license_)

    # Do not check the full string as it display the generated path.
    self.assertEqual(_INFO_STR % mnist_builder.data_dir, repr(info))
    self.assertIn("'test': <SplitInfo num_examples=", repr(info))

  def test_restore_after_modification(self):
    # Create a DatasetInfo
    info = dataset_info.DatasetInfo(
        builder=self._builder,
        description="A description",
        supervised_keys=("input", "output"),
        homepage="http://some-location",
        citation="some citation",
        license="some license",
    )
    info.as_proto.config_tags.extend(["foo", "bar"])
    info.download_size = 456
    filepath_template = "{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}"
    info.as_proto.splits.add(
        name="train", num_bytes=512, filepath_template=filepath_template
    )
    info.as_proto.splits.add(
        name="validation", num_bytes=64, filepath_template=filepath_template
    )
    info.as_proto.schema.feature.add()
    info.as_proto.schema.feature.add()  # Add dynamic statistics
    info.download_checksums = {
        "url1": "some checksum",
        "url2": "some other checksum",
    }

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # Save it
      info.write_to_directory(tmp_dir)

      # If fields are not defined, then everything is restored from disk.
      restored_info = dataset_info.DatasetInfo(builder=self._builder)
      restored_info.read_from_directory(tmp_dir)
      self.assertProtoEquals(info.as_proto, restored_info.as_proto)

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # Save it
      info.write_to_directory(tmp_dir)

      # If fields are defined, then the code version is kept
      restored_info = dataset_info.DatasetInfo(
          builder=self._builder,
          supervised_keys=("input (new)", "output (new)"),
          homepage="http://some-location-new",
          citation="some citation (new)",
          redistribution_info={"license": "some license (new)"},
      )
      restored_info.download_size = 789
      restored_info.as_proto.splits.add(name="validation", num_bytes=288)
      restored_info.as_proto.schema.feature.add()
      restored_info.as_proto.schema.feature.add()
      restored_info.as_proto.schema.feature.add()
      restored_info.as_proto.schema.feature.add()  # Add dynamic statistics
      restored_info.download_checksums = {
          "url2": "some other checksum (new)",
          "url3": "some checksum (new)",
      }

      restored_info.read_from_directory(tmp_dir)

      # Even though restored_info has been restored, informations defined in
      # the code overwrite informations from the json file.
      self.assertEqual(restored_info.description, "A description")
      self.assertEqual(restored_info.version, utils.Version("3.0.1"))
      self.assertEqual(restored_info.release_notes, {})
      self.assertEqual(
          restored_info.supervised_keys, ("input (new)", "output (new)")
      )
      self.assertEqual(restored_info.homepage, "http://some-location-new")
      self.assertEqual(restored_info.citation, "some citation (new)")
      self.assertEqual(
          restored_info.redistribution_info.license, "some license (new)"
      )
      self.assertEqual(restored_info.download_size, 789)
      self.assertEqual(restored_info.dataset_size, 576)
      self.assertLen(restored_info.as_proto.schema.feature, 4)
      self.assertEqual(
          restored_info.download_checksums,
          {
              "url2": "some other checksum (new)",
              "url3": "some checksum (new)",
          },
      )

  def test_reading_from_gcs_bucket(self):
    # The base TestCase prevents GCS access, so we explicitly ask it to restore
    # access here.
    with testing.enable_gcs_access():
      mnist_builder = mnist.MNIST(
          data_dir=tempfile.mkdtemp(dir=self.get_temp_dir())
      )
      info = dataset_info.DatasetInfo(builder=mnist_builder)
      info = mnist_builder.info

      # A nominal check to see if we read it.
      self.assertTrue(info.initialized)
      self.assertEqual(10000, info.splits["test"].num_examples)

  def test_str_smoke(self):
    info = mnist.MNIST(data_dir="/tmp/some_dummy_dir").info
    _ = str(info)

  def test_metadata(self):
    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      builder = RandomShapedImageGenerator(data_dir=tmp_dir)
      builder.download_and_prepare()
      # Metadata should have been created
      self.assertEqual(builder.info.metadata, {"some_key": 123})

      # Metadata should have been restored
      builder2 = RandomShapedImageGenerator(data_dir=tmp_dir)
      self.assertEqual(builder2.info.metadata, {"some_key": 123})

      # Metadata should have been restored even if the builder code was not
      # available and we restored from files.
      builder3 = read_only_builder.builder_from_files(
          builder.name,
          data_dir=tmp_dir,
      )
      self.assertEqual(builder3.info.metadata, {"some_key": 123})

      # Test whether the metadata is copyable.
      builder = RandomShapedImageGenerator(data_dir=tmp_dir)
      self.assertIsInstance(
          builder.info.metadata, dataset_info.LazyMetadataDict
      )
      metadata_copy = {**builder.info.metadata}
      self.assertEqual(metadata_copy, {"some_key": 123})

  def test_redistribution_info(self):
    info = dataset_info.DatasetInfo(
        builder=self._builder, license="some license"
    )
    info_proto = info.as_proto
    self.assertEqual(info_proto.redistribution_info.license, "some license")

  def test_updates_on_bucket_info(self):
    info = dataset_info.DatasetInfo(
        builder=self._builder, description="won't be updated"
    )
    # No statistics in the above.
    self.assertEqual(0, info.splits.total_num_examples)
    self.assertEmpty(info.as_proto.schema.feature)

    # Partial update will happen here.
    info.read_from_directory(_INFO_DIR)

    # Assert that description (things specified in the code) didn't change
    # but statistics are updated.
    self.assertEqual("won't be updated", info.description)

    # These are dynamically computed, so will be updated.
    self.assertEqual(40, info.splits.total_num_examples)
    self.assertLen(info.as_proto.schema.feature, 2)

  def test_set_splits_normal(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    split_info1 = splits_lib.SplitInfo(
        name="train", shard_lengths=[1, 2], num_bytes=0
    )
    split_info2 = splits_lib.SplitInfo(
        name="test", shard_lengths=[1], num_bytes=0
    )
    split_dict = splits_lib.SplitDict(split_infos=[split_info1, split_info2])
    info.set_splits(split_dict)
    self.assertEqual(str(info.splits), str(split_dict))
    self.assertEqual(
        str(info.as_proto.splits),
        str([split_info1.to_proto(), split_info2.to_proto()]),
    )

  def test_set_splits_incorrect_dataset_name(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    split_info1 = splits_lib.SplitInfo(
        name="train",
        shard_lengths=[1, 2],
        num_bytes=0,
        filename_template=naming.ShardedFileTemplate(
            dataset_name="some_other_dataset",
            split="train",
            data_dir=info.data_dir,
            filetype_suffix="tfrecord",
        ),
    )
    split_dict = splits_lib.SplitDict(split_infos=[split_info1])
    with pytest.raises(
        AssertionError, match="SplitDict contains SplitInfo for split"
    ):
      info.set_splits(split_dict)

  def test_set_splits_multi_split_info(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    split_info1 = splits_lib.SplitInfo(
        name="train", shard_lengths=[1, 2], num_bytes=0
    )
    split_info2 = splits_lib.SplitInfo(
        name="test", shard_lengths=[1], num_bytes=0
    )
    multi_split_info1 = splits_lib.MultiSplitInfo(
        name="train", split_infos=[split_info1]
    )
    multi_split_info2 = splits_lib.MultiSplitInfo(
        name="test", split_infos=[split_info2]
    )
    split_dict = splits_lib.SplitDict(
        split_infos=[multi_split_info1, multi_split_info2]
    )
    info.set_splits(split_dict)
    self.assertEqual(str(info.splits), str(split_dict))
    self.assertEqual(
        str(info.as_proto.splits),
        str([split_info1.to_proto(), split_info2.to_proto()]),
    )

  def test_set_file_format_override_fails(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.set_file_format(file_adapters.FileFormat.TFRECORD)
    self.assertEqual(info.file_format, file_adapters.FileFormat.TFRECORD)
    with pytest.raises(
        ValueError,
        match=(
            "File format is already set to FileFormat.TFRECORD. Got"
            " FileFormat.RIEGELI"
        ),
    ):
      info.set_file_format(file_adapters.FileFormat.RIEGELI)

  def test_set_file_format_override(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.set_file_format(file_adapters.FileFormat.TFRECORD)
    self.assertEqual(info.file_format, file_adapters.FileFormat.TFRECORD)
    info.set_file_format(file_adapters.FileFormat.RIEGELI, override=True)
    self.assertEqual(info.file_format, file_adapters.FileFormat.RIEGELI)

  def test_set_file_format_override_failes_when_fully_initialized(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.set_file_format(file_adapters.FileFormat.TFRECORD)
    info._fully_initialized = True
    self.assertEqual(info.file_format, file_adapters.FileFormat.TFRECORD)
    with pytest.raises(
        ValueError,
        match=(
            "File format is already set to FileFormat.TFRECORD. Got"
            " FileFormat.RIEGELI"
        ),
    ):
      info.set_file_format(file_adapters.FileFormat.RIEGELI)

  def test_set_file_format_override_fully_initialized(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.set_file_format(file_adapters.FileFormat.TFRECORD)
    info._fully_initialized = True
    self.assertEqual(info.file_format, file_adapters.FileFormat.TFRECORD)
    info.set_file_format(
        file_adapters.FileFormat.RIEGELI,
        override=True,
        override_if_initialized=True,
    )
    self.assertEqual(info.file_format, file_adapters.FileFormat.RIEGELI)

  def test_update_info_proto_with_features(self):
    info_proto = dataset_info.DatasetInfo(builder=self._builder).as_proto
    new_features = features.FeaturesDict({"text": features.Text()})
    new_info = dataset_info.update_info_proto_with_features(
        info_proto, new_features
    )
    self.assertEqual(new_info.features, new_features.to_proto())


@pytest.mark.parametrize(
    "file_format",
    [
        file_adapters.FileFormat.TFRECORD,
    ],
)
def test_file_format_save_restore(
    tmp_path: pathlib.Path,
    file_format: file_adapters.FileFormat,
):
  builder = testing.DummyDataset(data_dir=tmp_path, file_format=file_format)

  assert isinstance(builder.info.file_format, file_adapters.FileFormat)
  assert builder.info.file_format is file_format

  builder.download_and_prepare()

  # When restoring the builder, we do not provide the `file_format=`
  # yet it is correctly restored
  builder2 = testing.DummyDataset(data_dir=tmp_path)
  assert builder2.info.file_format is file_format

  # Explicitly passing the correct format is accepted.
  builder3 = testing.DummyDataset(data_dir=tmp_path, file_format=file_format)
  assert builder3.info.file_format is file_format

  # Providing an inconsistent format is rejected.
  with pytest.raises(ValueError, match="File format is already set to"):
    different_file_format = {
        file_adapters.FileFormat.TFRECORD: file_adapters.FileFormat.RIEGELI,
        file_adapters.FileFormat.RIEGELI: file_adapters.FileFormat.TFRECORD,
    }[file_format]
    testing.DummyDataset(data_dir=tmp_path, file_format=different_file_format)


def test_file_format_values(tmp_path: pathlib.Path):
  # Default file format
  builder = testing.DummyDataset(data_dir=tmp_path, file_format=None)
  assert builder.info.file_format == file_adapters.FileFormat.TFRECORD

  # str accepted
  builder = testing.DummyDataset(data_dir=tmp_path, file_format="riegeli")
  assert builder.info.file_format == file_adapters.FileFormat.RIEGELI

  # file_adapters.FileFormat accepted
  builder = testing.DummyDataset(
      data_dir=tmp_path, file_format=file_adapters.FileFormat.RIEGELI
  )
  assert builder.info.file_format == file_adapters.FileFormat.RIEGELI

  # Unknown value
  with pytest.raises(ValueError, match="is not a valid FileFormat"):
    testing.DummyDataset(data_dir=tmp_path, file_format="arrow")


@pytest.fixture(scope="session")
def generator_builder():
  return RandomShapedImageGenerator(data_dir=testing.make_tmp_dir())


def test_dataset_info_from_proto(generator_builder):  # pylint: disable=redefined-outer-name
  train = dataset_info_pb2.SplitInfo(
      name="train", num_shards=2, shard_lengths=[4, 5]
  )
  test = dataset_info_pb2.SplitInfo(
      name="test", num_shards=3, shard_lengths=[1, 2, 3]
  )
  text_feature = feature_pb2.Feature(
      python_class_name="tensorflow_datasets.core.features.text_feature.Text",
      text=feature_pb2.TextFeature(),
  )
  proto = dataset_info_pb2.DatasetInfo(
      name="random_shaped_image_generator",
      config_name=generator_builder.builder_config.name,
      version=str(generator_builder.version),
      features=feature_pb2.Feature(
          python_class_name=(
              "tensorflow_datasets.core.features.features_dict.FeaturesDict"
          ),
          features_dict=feature_pb2.FeaturesDict(
              features={"text": text_feature}
          ),
      ),
      splits=[train, test],
  )
  result = dataset_info.DatasetInfo.from_proto(
      builder=generator_builder,
      proto=proto,
  )
  assert result.splits["test"].shard_lengths == test.shard_lengths
  assert result.splits["train"].shard_lengths == train.shard_lengths
  assert set(result.features.keys()) == {"text"}
  assert result.version == generator_builder.version


def test_supervised_keys_from_proto():
  proto = text_format.Parse(
      text="""
  tuple: {
      items: [
        {
          dict: {
            dict: {
              key: "f2"
              value: { feature_key: "f2" }
            },
            dict: {
              key: "f1"
              value: { feature_key: "f1" }
            },
          }
        },
        {
          feature_key: "target"
        }
      ]
    }
  """,
      message=dataset_info_pb2.SupervisedKeys(),
  )
  supervised_keys = dataset_info._supervised_keys_from_proto(proto=proto)
  assert str(supervised_keys) == "({'f1': 'f1', 'f2': 'f2'}, 'target')"


def test_supervised_keys_from_proto_different_ordering():
  proto1 = text_format.Parse(
      text="""
  tuple: {
      items: [
        {
          dict: {
            dict: {
              key: "f1"
              value: { feature_key: "f1" }
            },
            dict: {
              key: "f2"
              value: { feature_key: "f2" }
            },
            dict: {
              key: "f3"
              value: { feature_key: "f3" }
            },
          }
        },
        {
          feature_key: "target"
        }
      ]
    }
  """,
      message=dataset_info_pb2.SupervisedKeys(),
  )
  proto2 = text_format.Parse(
      text="""
  tuple: {
      items: [
        {
          dict: {
            dict: {
              key: "f3"
              value: { feature_key: "f3" }
            },
            dict: {
              key: "f2"
              value: { feature_key: "f2" }
            },
            dict: {
              key: "f1"
              value: { feature_key: "f1" }
            },
          }
        },
        {
          feature_key: "target"
        }
      ]
    }
  """,
      message=dataset_info_pb2.SupervisedKeys(),
  )
  supervised_keys1 = dataset_info._supervised_keys_from_proto(proto=proto1)
  supervised_keys2 = dataset_info._supervised_keys_from_proto(proto=proto2)
  assert str(supervised_keys1) == str(supervised_keys2)


@pytest.mark.parametrize(
    ("license_", "redistribution_info", "expected_license"),
    (
        ("a", None, "a"),
        (None, {"license": "a"}, "a"),
        ("a", {"license": "a"}, "a"),
        (None, None, None),
    ),
)
def test_create_redistribution_info_proto(
    license_, redistribution_info, expected_license
):
  result = dataset_info._create_redistribution_info_proto(
      license=license_, redistribution_info=redistribution_info
  )
  if expected_license is None:
    assert result is None
  else:
    assert result.license == expected_license


def test_create_redistribution_info_proto_inconsistent():
  with pytest.raises(
      ValueError, match="License specified twice and inconsistently"
  ):
    dataset_info._create_redistribution_info_proto(
        license="a", redistribution_info={"license": "b"}
    )


def test_create_redistribution_info_proto_unsupported_fields():
  with pytest.raises(
      ValueError, match="`redistribution_info` contains unsupported keys"
  ):
    dataset_info._create_redistribution_info_proto(
        license="a", redistribution_info={"unsupported": "b"}
    )


def test_supports_file_format():
  dataset_info_proto = dataset_info_pb2.DatasetInfo(
      file_format=file_adapters.FileFormat.TFRECORD.value,
      alternative_file_formats=[file_adapters.FileFormat.RIEGELI.value],
  )
  assert dataset_info.supports_file_format(
      dataset_info_proto, file_format=file_adapters.FileFormat.TFRECORD
  )
  assert dataset_info.supports_file_format(
      dataset_info_proto, file_format=file_adapters.FileFormat.RIEGELI
  )
  assert not dataset_info.supports_file_format(
      dataset_info_proto, file_format=file_adapters.FileFormat.PARQUET
  )


class GetSplitInfoFromProtoTest(testing.TestCase):

  def _dataset_info_proto_with_splits(self):
    return dataset_info_pb2.DatasetInfo(
        name="dataset",
        file_format="tfrecord",
        alternative_file_formats=["riegeli"],
        splits=[
            dataset_info_pb2.SplitInfo(
                name="train",
                shard_lengths=[1, 2, 3],
                num_bytes=42,
            ),
            dataset_info_pb2.SplitInfo(
                name="test",
                shard_lengths=[1, 2, 3],
                num_bytes=42,
                filepath_template="{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}",
            ),
        ],
    )

  def test_get_split_dict_from_proto(self):
    actual = dataset_info.get_split_dict_from_proto(
        dataset_info_proto=self._dataset_info_proto_with_splits(),
        data_dir="/data",
        file_format=file_adapters.FileFormat.PARQUET,
    )
    assert set(["train", "test"]) == set(actual.keys())

    train = actual["train"]
    assert train.name == "train"
    assert train.shard_lengths == [1, 2, 3]
    assert train.num_bytes == 42
    assert train.filename_template.dataset_name == "dataset"
    assert train.filename_template.template == naming.DEFAULT_FILENAME_TEMPLATE
    assert train.filename_template.filetype_suffix == "parquet"

    test = actual["test"]
    assert test.name == "test"
    assert test.shard_lengths == [1, 2, 3]
    assert test.num_bytes == 42
    assert test.filename_template.dataset_name == "dataset"
    assert (
        test.filename_template.template == "{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}"
    )
    assert test.filename_template.filetype_suffix == "parquet"

  def test_get_split_info_from_proto_undefined_filename_template(self):
    actual = dataset_info.get_split_info_from_proto(
        dataset_info_proto=self._dataset_info_proto_with_splits(),
        split_name="train",
        data_dir="/path/to/data",
        file_format=file_adapters.FileFormat.TFRECORD,
    )
    assert actual.name == "train"
    assert actual.shard_lengths == [1, 2, 3]
    assert actual.num_bytes == 42
    assert actual.filename_template.dataset_name == "dataset"
    assert actual.filename_template.template == naming.DEFAULT_FILENAME_TEMPLATE

  def test_get_split_info_from_proto_defined_filename_template(self):
    actual = dataset_info.get_split_info_from_proto(
        dataset_info_proto=self._dataset_info_proto_with_splits(),
        split_name="test",
        data_dir="/path/to/data",
        file_format=file_adapters.FileFormat.TFRECORD,
    )
    assert actual.name == "test"
    assert actual.shard_lengths == [1, 2, 3]
    assert actual.filename_template.dataset_name == "dataset"
    assert (
        actual.filename_template.template
        == "{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}"
    )

  def test_get_split_info_from_proto_non_existing_split(self):
    actual = dataset_info.get_split_info_from_proto(
        dataset_info_proto=self._dataset_info_proto_with_splits(),
        split_name="undefined",
        data_dir="/path/to/data",
        file_format=file_adapters.FileFormat.TFRECORD,
    )
    assert actual is None

  def test_get_split_info_from_proto_unavailable_format(self):
    with pytest.raises(
        ValueError,
        match=re.escape(
            "File format parquet does not match available dataset file formats:"
            " ['riegeli', 'tfrecord']."
        ),
    ):
      dataset_info.get_split_info_from_proto(
          dataset_info_proto=self._dataset_info_proto_with_splits(),
          split_name="undefined",
          data_dir="/path/to/data",
          file_format=file_adapters.FileFormat.PARQUET,
      )


# pylint: disable=g-inconsistent-quotes
_INFO_STR = '''tfds.core.DatasetInfo(
    name='mnist',
    full_name='mnist/3.0.1',
    description="""
    The MNIST database of handwritten digits.
    """,
    homepage='https://storage.googleapis.com/cvdf-datasets/mnist/',
    data_dir='%s',
    file_format=tfrecord,
    download_size=1.95 KiB,
    dataset_size=11.06 MiB,
    features=FeaturesDict({
        'image': Image(shape=(28, 28, 1), dtype=uint8),
        'label': ClassLabel(shape=(), dtype=int64, num_classes=10),
    }),
    supervised_keys=('image', 'label'),
    disable_shuffling=False,
    nondeterministic_order=False,
    splits={
        'test': <SplitInfo num_examples=20, num_shards=1>,
        'train': <SplitInfo num_examples=20, num_shards=1>,
    },
    citation="""@article{lecun2010mnist,
      title={MNIST handwritten digit database},
      author={LeCun, Yann and Cortes, Corinna and Burges, CJ},
      journal={ATT Labs [Online]. Available: http://yann. lecun. com/exdb/mnist},
      volume={2},
      year={2010}
    }
    """,
    redistribution_info=license: "test license",
)'''
# pylint: enable=g-inconsistent-quotes


class LazyMetadataDictTest(testing.TestCase):

  def setUp(self):
    super().setUp()
    self.data_dir = epath.Path(self.tmp_dir)
    metadata_file = self.data_dir / "metadata.json"
    metadata_file.write_text(json.dumps({"test": "test123"}))

  def test_load_metadata(self):
    metadata_dict = dataset_info.LazyMetadataDict(self.data_dir)
    self.assertEqual(metadata_dict["test"], "test123")

  @mock.patch.object(dataset_info, "_load_metadata_from_file")
  def test_get_item(self, mock_load_metadata_from_file):
    mock_load_metadata_from_file.return_value = {"test": "test123"}

    metadata_dict = dataset_info.LazyMetadataDict(self.data_dir)
    mock_load_metadata_from_file.assert_not_called()

    self.assertEqual(metadata_dict["test"], "test123")
    mock_load_metadata_from_file.assert_called_with(self.data_dir)

    self.assertEqual(sorted(metadata_dict.keys()), ["test"])

    # Update the metadata.
    metadata_dict["abc"] = "def"
    self.assertEqual(metadata_dict["abc"], "def")

  @mock.patch.object(dataset_info, "_load_metadata_from_file")
  def test_keys(self, mock_load_metadata_from_file):
    mock_load_metadata_from_file.return_value = {"test": "test123"}
    metadata_dict = dataset_info.LazyMetadataDict(self.data_dir)
    mock_load_metadata_from_file.assert_not_called()
    actual_keys = sorted(metadata_dict.keys())
    mock_load_metadata_from_file.assert_called_with(self.data_dir)
    self.assertEqual(actual_keys, ["test"])

  @mock.patch.object(dataset_info, "_load_metadata_from_file")
  def test_items(self, mock_load_metadata_from_file):
    mock_load_metadata_from_file.return_value = {"test": "test123"}
    metadata_dict = dataset_info.LazyMetadataDict(self.data_dir)
    mock_load_metadata_from_file.assert_not_called()
    self.assertNotEmpty(metadata_dict.items())
    mock_load_metadata_from_file.assert_called_with(self.data_dir)

  @mock.patch.object(dataset_info, "_load_metadata_from_file")
  def test_updating_before_loading(self, mock_load_metadata_from_file):
    metadata_dict = dataset_info.LazyMetadataDict(self.data_dir)
    mock_load_metadata_from_file.assert_not_called()

    metadata_dict.update({"abc": "def", "ghi": "jkl"})
    mock_load_metadata_from_file.assert_not_called()

  def test_copy(self):
    metadata_dict = dataset_info.LazyMetadataDict(self.data_dir)
    metadata_dict_copy = metadata_dict.copy()
    self.assertEqual(metadata_dict_copy["test"], "test123")


if __name__ == "__main__":
  testing.test_main()
