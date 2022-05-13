# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

import json
import os
import pathlib
import tempfile
import numpy as np
import pytest

import tensorflow as tf
from tensorflow_datasets import testing
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

from google.protobuf import text_format

_TFDS_DIR = utils.tfds_path()
_INFO_DIR = os.path.join(_TFDS_DIR, "testing", "test_data", "dataset_info",
                         "mnist", "3.0.1")
_INFO_DIR_UNLABELED = os.path.join(_TFDS_DIR, "testing", "test_data",
                                   "dataset_info", "mnist_unlabeled", "3.0.1")
_NON_EXISTENT_DIR = os.path.join(_TFDS_DIR, "non_existent_dir")

DummyDatasetSharedGenerator = testing.DummyDatasetSharedGenerator


class RandomShapedImageGenerator(DummyDatasetSharedGenerator):

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
          "im":
              np.random.randint(
                  0, 255, size=(height, width, 3), dtype=np.uint8)
      }


class DatasetInfoTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DatasetInfoTest, cls).setUpClass()
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    cls._builder = DummyDatasetSharedGenerator(data_dir=cls._tfds_tmp_dir)

  @classmethod
  def tearDownClass(cls):
    super(DatasetInfoTest, cls).tearDownClass()
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  def test_non_existent_dir(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    with self.assertRaisesWithPredicateMatch(
        FileNotFoundError, "from a directory which does not exist"):
      info.read_from_directory(_NON_EXISTENT_DIR)

  def test_reading(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.read_from_directory(_INFO_DIR)

    # Assert that we read the file and initialized DatasetInfo.
    self.assertTrue(info.initialized)
    self.assertEqual("dummy_dataset_shared_generator", info.name)
    self.assertEqual("dummy_dataset_shared_generator/1.0.0", info.full_name)

    # Test splits are initialized properly.
    split_dict = info.splits

    # Assert they are the correct number.
    self.assertTrue(len(split_dict), 2)

    # Assert on what they are
    self.assertIn("train", split_dict)
    self.assertIn("test", split_dict)

    # Assert that this is computed correctly.
    self.assertEqual(40, info.splits.total_num_examples)
    self.assertEqual(11594722, info.dataset_size)

    self.assertEqual("image", info.supervised_keys[0])
    self.assertEqual("label", info.supervised_keys[1])
    self.assertEqual(info.module_name, "tensorflow_datasets.testing.test_utils")
    self.assertEqual(False, info.disable_shuffling)

    self.assertEqual(info.version, utils.Version("1.0.0"))
    self.assertEqual(info.release_notes, {
        "1.0.0": "Release notes 1.0.0",
        "2.0.0": "Release notes 2.0.0"
    })

  def test_disable_shuffling(self):
    info = dataset_info.DatasetInfo(
        builder=self._builder, disable_shuffling=True)
    info.read_from_directory(_INFO_DIR)

    self.assertEqual(True, info.disable_shuffling)

  def test_reading_empty_properties(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    info.read_from_directory(_INFO_DIR_UNLABELED)

    # Assert supervised_keys has not been set
    self.assertIsNone(None, info.supervised_keys)

  def test_writing(self):
    # First read in stuff.
    mnist_builder = mnist.MNIST(
        data_dir=tempfile.mkdtemp(dir=self.get_temp_dir()))

    info = dataset_info.DatasetInfo(
        builder=mnist_builder, features=mnist_builder.info.features)
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
    info.download_size = 456
    filepath_template = "{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}"
    info.as_proto.splits.add(
        name="train", num_bytes=512, filepath_template=filepath_template)
    info.as_proto.splits.add(
        name="validation", num_bytes=64, filepath_template=filepath_template)
    info.as_proto.schema.feature.add()
    info.as_proto.schema.feature.add()  # Add dynamic statistics
    info.download_checksums = {
        "url1": "some checksum",
        "url2": "some other checksum",
    }

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # Save it
      info.write_to_directory(tmp_dir)

      # If fields are not defined, then everything is restored from disk
      restored_info = dataset_info.DatasetInfo(builder=self._builder)
      restored_info.read_from_directory(tmp_dir)
      self.assertEqual(info.as_proto, restored_info.as_proto)

    with testing.tmp_dir(self.get_temp_dir()) as tmp_dir:
      # Save it
      info.write_to_directory(tmp_dir)

      # If fields are defined, then the code version is kept
      restored_info = dataset_info.DatasetInfo(
          builder=self._builder,
          supervised_keys=("input (new)", "output (new)"),
          homepage="http://some-location-new",
          citation="some citation (new)",
          redistribution_info={"license": "some license (new)"})
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
      self.assertEqual(restored_info.version, utils.Version("1.0.0"))
      self.assertEqual(restored_info.release_notes, {
          "1.0.0": "Release notes 1.0.0",
          "2.0.0": "Release notes 2.0.0"
      })
      self.assertEqual(restored_info.supervised_keys,
                       ("input (new)", "output (new)"))
      self.assertEqual(restored_info.homepage, "http://some-location-new")
      self.assertEqual(restored_info.citation, "some citation (new)")
      self.assertEqual(restored_info.redistribution_info.license,
                       "some license (new)")
      self.assertEqual(restored_info.download_size, 789)
      self.assertEqual(restored_info.dataset_size, 576)
      self.assertEqual(len(restored_info.as_proto.schema.feature), 4)
      self.assertEqual(restored_info.download_checksums, {
          "url2": "some other checksum (new)",
          "url3": "some checksum (new)",
      })

  def test_reading_from_gcs_bucket(self):
    # The base TestCase prevents GCS access, so we explicitly ask it to restore
    # access here.
    with self.gcs_access():
      mnist_builder = mnist.MNIST(
          data_dir=tempfile.mkdtemp(dir=self.get_temp_dir()))
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

  def test_updates_on_bucket_info(self):

    info = dataset_info.DatasetInfo(
        builder=self._builder, description="won't be updated")
    # No statistics in the above.
    self.assertEqual(0, info.splits.total_num_examples)
    self.assertEqual(0, len(info.as_proto.schema.feature))

    # Partial update will happen here.
    info.read_from_directory(_INFO_DIR)

    # Assert that description (things specified in the code) didn't change
    # but statistics are updated.
    self.assertEqual("won't be updated", info.description)

    # These are dynamically computed, so will be updated.
    self.assertEqual(40, info.splits.total_num_examples)
    self.assertEqual(2, len(info.as_proto.schema.feature))

  def test_set_splits_normal(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    split_info1 = splits_lib.SplitInfo(
        name="train", shard_lengths=[1, 2], num_bytes=0)
    split_info2 = splits_lib.SplitInfo(
        name="test", shard_lengths=[1], num_bytes=0)
    split_dict = splits_lib.SplitDict(split_infos=[split_info1, split_info2])
    info.set_splits(split_dict)
    self.assertEqual(str(info.splits), str(split_dict))
    self.assertEqual(
        str(info.as_proto.splits),
        str([split_info1.to_proto(),
             split_info2.to_proto()]))

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
            filetype_suffix="tfrecord"))
    split_dict = splits_lib.SplitDict(split_infos=[split_info1])
    with pytest.raises(
        AssertionError, match="SplitDict contains SplitInfo for split"):
      info.set_splits(split_dict)

  def test_set_splits_multi_split_info(self):
    info = dataset_info.DatasetInfo(builder=self._builder)
    split_info1 = splits_lib.SplitInfo(
        name="train", shard_lengths=[1, 2], num_bytes=0)
    split_info2 = splits_lib.SplitInfo(
        name="test", shard_lengths=[1], num_bytes=0)
    multi_split_info1 = splits_lib.MultiSplitInfo(
        name="train", split_infos=[split_info1])
    multi_split_info2 = splits_lib.MultiSplitInfo(
        name="test", split_infos=[split_info2])
    split_dict = splits_lib.SplitDict(
        split_infos=[multi_split_info1, multi_split_info2])
    info.set_splits(split_dict)
    self.assertEqual(str(info.splits), str(split_dict))
    self.assertEqual(
        str(info.as_proto.splits),
        str([split_info1.to_proto(),
             split_info2.to_proto()]))


@pytest.mark.parametrize(
    "file_format",
    [
        file_adapters.FileFormat.TFRECORD,
    ])
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
      data_dir=tmp_path, file_format=file_adapters.FileFormat.RIEGELI)
  assert builder.info.file_format == file_adapters.FileFormat.RIEGELI

  # Unknown value
  with pytest.raises(ValueError, match="is not a valid FileFormat"):
    testing.DummyDataset(data_dir=tmp_path, file_format="arrow")


def test_dataset_info_from_proto():
  builder = RandomShapedImageGenerator(data_dir=testing.make_tmp_dir())
  train = dataset_info_pb2.SplitInfo(
      name="train", num_shards=2, shard_lengths=[4, 5])
  test = dataset_info_pb2.SplitInfo(
      name="test", num_shards=3, shard_lengths=[1, 2, 3])
  text_feature = feature_pb2.Feature(
      python_class_name="tensorflow_datasets.core.features.text_feature.Text",
      text=feature_pb2.TextFeature())
  proto = dataset_info_pb2.DatasetInfo(
      name="random_shaped_image_generator",
      version=str(builder.version),
      features=feature_pb2.Feature(
          python_class_name="tensorflow_datasets.core.features.features_dict.FeaturesDict",
          features_dict=feature_pb2.FeaturesDict(
              features={"text": text_feature})),
      splits=[train, test])
  result = dataset_info.DatasetInfo.from_proto(builder=builder, proto=proto)
  assert result.splits["test"].shard_lengths == test.shard_lengths
  assert result.splits["train"].shard_lengths == train.shard_lengths
  assert set(result.features.keys()) == {"text"}
  assert result.version == builder.version


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
      message=dataset_info_pb2.SupervisedKeys())
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
      message=dataset_info_pb2.SupervisedKeys())
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
      message=dataset_info_pb2.SupervisedKeys())
  supervised_keys1 = dataset_info._supervised_keys_from_proto(proto=proto1)
  supervised_keys2 = dataset_info._supervised_keys_from_proto(proto=proto2)
  assert str(supervised_keys1) == str(supervised_keys2)


# pylint: disable=g-inconsistent-quotes
_INFO_STR = '''tfds.core.DatasetInfo(
    name='mnist',
    full_name='mnist/3.0.1',
    description="""
    The MNIST database of handwritten digits.
    """,
    homepage='https://storage.googleapis.com/cvdf-datasets/mnist/',
    data_path='%s',
    file_format=tfrecord,
    download_size=1.95 KiB,
    dataset_size=11.06 MiB,
    features=FeaturesDict({
        'image': Image(shape=(28, 28, 1), dtype=tf.uint8),
        'label': ClassLabel(shape=(), dtype=tf.int64, num_classes=10),
    }),
    supervised_keys=('image', 'label'),
    disable_shuffling=False,
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

if __name__ == "__main__":
  testing.test_main()
