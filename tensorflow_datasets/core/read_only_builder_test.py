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

"""Tests for read_only_builder."""

import functools
import os
import pathlib
from typing import Sequence
from unittest import mock

import dill
import pytest
import tensorflow as tf

from tensorflow_datasets import testing
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import load
from tensorflow_datasets.core import proto
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.features import features_dict
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.core.utils import file_utils

from google.protobuf import json_format


class DummyNoConfMnist(testing.DummyDataset):
  """Same as DummyMnist (but declared here to avoid skip_registering issues)."""


class DummyConfigMnist(testing.DummyDataset):
  """Same as DummyMnist, but with config."""

  BUILDER_CONFIGS = [
      dataset_builder.BuilderConfig(
          name='dummy_config',
          version='0.1.0',
          release_notes={'0.1.0': 'Release notes 0.1.0'},
          description='testing config',
      ),
      dataset_builder.BuilderConfig(
          name='dummy_config2',
          version='0.1.0',
          release_notes={'0.1.0': 'Release notes 0.1.0'},
          description='testing config',
      ),
  ]


# All tests using `code_builder` will be executed twice (with/without config)
@pytest.fixture(scope='module', params=[DummyNoConfMnist, DummyConfigMnist])
def code_builder(request, tmp_path_factory) -> dataset_builder.DatasetBuilder:
  """Parametrized fixture to test both config and non-config dataset."""
  tmp_path = tmp_path_factory.mktemp('tfds_datasets')  # Temporary data_dir
  builder_cls = request.param
  # Generate the dataset (only once for all tests as scope == 'module').
  builder = builder_cls(data_dir=tmp_path)
  builder.download_and_prepare()

  # Update the default DATA_DIR during the test.
  with mock.patch.object(constants, 'DATA_DIR', str(tmp_path)):
    yield builder


# pylint: disable=redefined-outer-name


def test_builder_files_exists(code_builder: dataset_builder.DatasetBuilder):
  """Tests that `tfds.builder` is correctly loaded from the code/files."""
  # When code is available, and no version specified, load from code
  builder = load.builder(code_builder.name)
  assert isinstance(builder, type(code_builder))  # Check builder is DummyMnist
  assert not isinstance(builder, read_only_builder.ReadOnlyBuilder)

  # If the version is specified, load from the files (backward support)
  builder = load.builder(f'{code_builder.name}:*.*.*')  # Most recent version
  assert not isinstance(builder, type(code_builder))
  assert isinstance(builder, read_only_builder.ReadOnlyBuilder)

  # If the version is specified but files not found, load from the code
  builder = load.builder(
      f'{code_builder.name}:*.*.*', data_dir='/tmp/path/tfds/not-exists')
  assert isinstance(builder, type(code_builder))
  assert not isinstance(builder, read_only_builder.ReadOnlyBuilder)


def test_builder_config(code_builder: dataset_builder.DatasetBuilder):
  """Tests that code found but config not loads from files."""
  if not code_builder.BUILDER_CONFIGS:
    return

  # Remove the registered configs
  with mock.patch.object(type(code_builder), 'BUILDER_CONFIGS', []), \
       mock.patch.object(type(code_builder), 'builder_configs', {}):
    # Config isn't present in the code anymore
    with pytest.raises(ValueError, match='BuilderConfig .* not found'):
      load.builder(
          f'{code_builder.name}/dummy_config', data_dir='/tmp/path/not-exists')

    # But previously generated configs still be loaded from disk
    builder = load.builder(f'{code_builder.name}/dummy_config')
    assert not isinstance(builder, type(code_builder))
    assert isinstance(builder, read_only_builder.ReadOnlyBuilder)


def test_builder_code_not_found(code_builder: dataset_builder.DatasetBuilder):
  """If the code isn't found, use files instead."""

  # Patch `tfds.builder_cls` to emulate that the dataset isn't registered
  with mock.patch.object(
      load,
      'builder_cls',
      side_effect=registered.DatasetNotFoundError(code_builder.name),
  ):
    # Files exists, but not code, loading from files
    builder = load.builder(code_builder.name)
    assert isinstance(builder, read_only_builder.ReadOnlyBuilder)
    load.load(code_builder.name, split=[])  # Dataset found -> no error

    if code_builder.builder_config:
      # When the code isn't found, default config is infered from `.config/`
      assert builder.builder_config.name == code_builder.BUILDER_CONFIGS[0].name

      # Explicitly passing a config should works too.
      config_name = f'{code_builder.name}/{code_builder.builder_config.name}'
      builder = load.builder(config_name)
      assert isinstance(builder, read_only_builder.ReadOnlyBuilder)

    # Neither code not files found, raise DatasetNotFoundError
    with pytest.raises(registered.DatasetNotFoundError):
      load.builder(code_builder.name, data_dir='/tmp/non-existing/tfds/dir')

    with pytest.raises(registered.DatasetNotFoundError):
      load.load(
          code_builder.name, split=[], data_dir='/tmp/non-existing/tfds/dir')


# Test both with and without config
def test_builder_from_directory(code_builder: dataset_builder.DatasetBuilder):
  """Builder can be created from the files only."""

  # Reconstruct the dataset
  builder = read_only_builder.builder_from_directory(code_builder.data_dir)
  assert builder.name == code_builder.name
  assert builder.data_dir == code_builder.data_dir
  assert builder.info.version == code_builder.info.version
  assert builder.info.full_name == code_builder.info.full_name
  assert repr(builder.info) == repr(code_builder.info)
  assert builder.VERSION == code_builder.info.version
  assert builder.RELEASE_NOTES == code_builder.info.release_notes
  assert builder.__module__ == type(code_builder).__module__
  assert read_only_builder.ReadOnlyBuilder.VERSION is None

  if code_builder.builder_config:
    assert builder.builder_config
    code_config = code_builder.builder_config
    file_config = builder.builder_config
    # Config attributes should be restored too
    assert code_config.name == file_config.name
    assert code_config.description == file_config.description
    assert code_config.version == file_config.version

  # Test that the dataset can be read
  ds = dataset_utils.as_numpy(builder.as_dataset(split='train').take(5))
  origin_ds = dataset_utils.as_numpy(builder.as_dataset(split='train').take(5))
  assert [ex['id'] for ex in ds] == [ex['id'] for ex in origin_ds]

  builder.download_and_prepare()  # Should be a no-op

  # Test pickling and un-pickling
  builder2 = dill.loads(dill.dumps(builder))
  assert builder.name == builder2.name
  assert builder.version == builder2.version


def test_builder_from_metadata(code_builder: dataset_builder.DatasetBuilder):
  features = features_dict.FeaturesDict({
      'a': tf.float32,
      'b': tf.string,
  })
  info_proto = dataset_info_pb2.DatasetInfo(
      name='abcd',
      description='efgh',
      config_name='en',
      config_description='something',
      version='9.9.9',
      release_notes={'9.9.9': 'release description'},
      citation='some citation',
      features=features.to_proto())
  builder = read_only_builder.builder_from_metadata(
      code_builder.data_dir, info_proto=info_proto)
  assert builder.name == info_proto.name
  assert builder.info.description == info_proto.description
  assert builder.info.citation == info_proto.citation
  assert builder.info.version == info_proto.version
  assert builder.builder_config
  assert builder.builder_config.name == info_proto.config_name
  assert builder.builder_config.version == info_proto.version
  assert builder.builder_config.description == info_proto.config_description
  assert builder.builder_config.release_notes == info_proto.release_notes
  assert str(builder.info.features) == str(features)


def test_builder_from_directory_dir_not_exists(tmp_path: pathlib.Path):
  with pytest.raises(FileNotFoundError, match='Could not load dataset info'):
    read_only_builder.builder_from_directory(tmp_path)


def test_builder_from_files_multi_dir(
    code_builder: dataset_builder.DatasetBuilder,
    tmp_path: pathlib.Path,
):
  some_dir = tmp_path / 'other'
  some_dir.mkdir()

  builder = read_only_builder.builder_from_files(
      code_builder.name,
      data_dir=[
          code_builder._data_dir_root, some_dir, '/tmp/non-existing-dir/'
      ],
  )
  assert builder.name == code_builder.name
  assert builder.data_dir == code_builder.data_dir


def test_not_registered():
  """Ensure the ReadOnlyBuilder is not registered."""
  assert read_only_builder.ReadOnlyBuilder.name not in load.list_builders()


# We assume that all datasets are added into `data_dir='path/to'`
_find_builder_dir = functools.partial(
    read_only_builder._find_builder_dir, data_dir='path/to')


def test_find_builder_dir_with_multiple_data_dir(mock_fs: testing.MockFs):
  mock_fs.add_file('path/to/ds0/1.0.0/features.json')

  # Dataset not found.
  assert read_only_builder._find_builder_dir('ds0') is None

  with mock.patch.object(
      file_utils,
      'list_data_dirs',
      return_value=[constants.DATA_DIR, 'path/to'],
  ):
    assert read_only_builder._find_builder_dir('ds0') == 'path/to/ds0/1.0.0'

    # Dataset present in 2 different data_dir
    duplicate_path = os.path.join(constants.DATA_DIR, 'ds0/1.0.0/features.json')
    mock_fs.add_file(duplicate_path)
    with pytest.raises(ValueError, match='detected in multiple locations'):
      read_only_builder._find_builder_dir('ds0')


def test_find_builder_dir_legacy_ds(mock_fs: testing.MockFs):
  """Legacy dataset should be ignored (no feature config file)."""
  mock_fs.add_file('path/to/ds0/1.0.0/temp.txt')
  assert _find_builder_dir('ds0') is None

  mock_fs.add_file('path/to/ds0/1.0.0/features.json')
  assert _find_builder_dir('ds0') == 'path/to/ds0/1.0.0'


def test_find_builder_dir_multi_versions(mock_fs: testing.MockFs):
  """Versions should be sorted numerically (10 > 9)."""
  mock_fs.add_file('path/to/ds0/1.0.0/features.json')
  mock_fs.add_file('path/to/ds0/9.9.9/features.json')
  mock_fs.add_file('path/to/ds0/10.0.0/features.json')
  assert _find_builder_dir('ds0') == 'path/to/ds0/10.0.0'
  # Explicitly given version
  assert _find_builder_dir('ds0:9.9.9') == 'path/to/ds0/9.9.9'
  # Non-existing version
  assert _find_builder_dir('ds0:9.9.0') is None


def test_find_builder_dir_bad_version_dir_name(mock_fs: testing.MockFs):
  """Ill-formatted folders should be ignored."""
  mock_fs.add_file('path/to/ds0/9.9./features.json')
  mock_fs.add_file('path/to/ds0/1.0.o/features.json')
  mock_fs.add_file('path/to/ds0/other/features.json')
  assert _find_builder_dir('ds0') is None

  mock_fs.add_file('path/to/ds0/1.1.0/features.json')
  assert _find_builder_dir('ds0') == 'path/to/ds0/1.1.0'


def test_find_builder_config_no_code(mock_fs: testing.MockFs):
  """When the code can't be reached, config should be explicit."""
  mock_fs.add_file('path/to/ds0/config/1.0.0/features.json')
  mock_fs.add_file('path/to/ds0/1.1.0/features.json')

  # If the original code can't be reached, assume no config
  assert _find_builder_dir('ds0') == 'path/to/ds0/1.1.0'
  # Config is explicitly given
  assert _find_builder_dir('ds0/config') == 'path/to/ds0/config/1.0.0'

  mock_fs.add_file('path/to/ds1/config/1.0.0/features.json')
  # Config not available, return None
  assert _find_builder_dir('ds1') is None
  assert _find_builder_dir('ds1/config') == 'path/to/ds1/config/1.0.0'


def test_find_builder_wrong_dir(mock_fs: testing.MockFs):
  mock_fs.add_file('path/to/ds0/1.1.0/features.json')
  assert _find_builder_dir('ds0') == 'path/to/ds0/1.1.0'
  assert _find_builder_dir('ds0', data_dir='path/to/other/dir') is None


def test_find_builder_config_code(mock_fs: testing.MockFs):
  """When code exists, extract the default config name."""

  class MyDataset(testing.DummyMnist):  # pylint: disable=unused-variable
    """Dummy dataset."""
    BUILDER_CONFIGS = [
        dataset_builder.BuilderConfig(  # pylint: disable=g-complex-comprehension
            name=name,
            version='2.0.0',
            description=f'{name} description')
        for name in ('default_config', 'other_config')
    ]

  mock_fs.add_file('path/to/my_dataset/default_config/0.0.1/features.json')
  mock_fs.add_file('path/to/my_dataset/default_config/1.0.0/features.json')
  mock_fs.add_file('path/to/my_dataset/other_config/1.0.0/features.json')
  mock_fs.add_file('path/to/my_dataset/old_config/0.8.0/features.json')
  mock_fs.add_file('path/to/my_dataset/old_config/1.0.0/features.json')
  mock_fs.add_file('path/to/my_dataset/broken_config/features.json')
  mock_fs.add_file('path/to/my_dataset/0.0.1/features.json')

  # If code can be reached, use it to load the default config name
  # Note that the existing version is loaded, even if the code is at a
  # more recent version.
  assert (_find_builder_dir('my_dataset') ==
          'path/to/my_dataset/default_config/1.0.0')
  # Explicitly given version with implicit config.
  assert (_find_builder_dir('my_dataset:0.0.1') ==
          'path/to/my_dataset/default_config/0.0.1')
  # When config is explicitly given, load the last detected version
  assert (_find_builder_dir('my_dataset/other_config') ==
          'path/to/my_dataset/other_config/1.0.0')
  assert (_find_builder_dir('my_dataset/old_config') ==
          'path/to/my_dataset/old_config/1.0.0')
  assert (_find_builder_dir('my_dataset/old_config:0.8.0') ==
          'path/to/my_dataset/old_config/0.8.0')
  assert _find_builder_dir('my_dataset/broken_config') is None
  assert _find_builder_dir('my_dataset/unknown_config') is None


def test_get_version_str(mock_fs: testing.MockFs):

  mock_fs.add_file('path/to/ds/1.0.0/features.json')
  mock_fs.add_file('path/to/ds/1.0.1/features.json')
  mock_fs.add_file('path/to/ds/1.1.0/features.json')
  mock_fs.add_file('path/to/ds/2.0.1/features.json')

  get_version_str = functools.partial(
      read_only_builder._get_version_str,
      'path/to/ds/'  # pylint: disable=protected-access
  )

  # requested_version is None -> Returns last version
  assert get_version_str(requested_version=None) == '2.0.1'
  # Returns highest matching version
  assert get_version_str(requested_version='1.*.*') == '1.1.0'
  assert get_version_str(requested_version='*.*.*') == '2.0.1'
  assert get_version_str(requested_version='1.0.0') == '1.0.0'
  # No matching version found
  assert get_version_str(requested_version='1.3.*') is None
  assert get_version_str(requested_version='2.3.5') is None

  assert _find_builder_dir('ds') == 'path/to/ds/2.0.1'
  assert _find_builder_dir('ds:*.*.*') == 'path/to/ds/2.0.1'
  assert _find_builder_dir('ds:1.*.*') == 'path/to/ds/1.1.0'
  assert _find_builder_dir('ds:1.0.0') == 'path/to/ds/1.0.0'
  assert _find_builder_dir('ds:1.3.*') is None
  assert _find_builder_dir('ds:2.3.5') is None


def test_builder_from_directories_splits(mock_fs: testing.MockFs):

  def split_for(name: str, shard_lengths: Sequence[int]) -> proto.SplitInfo:
    return proto.SplitInfo(name=name, shard_lengths=shard_lengths)

  def dataset_info(splits):
    text_feature = proto.feature_pb2.Feature(
        python_class_name='tensorflow_datasets.core.features.text_feature.Text',
        text=proto.feature_pb2.TextFeature())
    features = proto.feature_pb2.Feature(
        python_class_name='tensorflow_datasets.core.features.features_dict.FeaturesDict',
        features_dict=proto.feature_pb2.FeaturesDict(
            features={'text': text_feature}))
    return proto.dataset_info_pb2.DatasetInfo(
        name='ds_name',
        version='1.0.0',
        file_format='tfrecord',
        splits=splits,
        features=features)

  split_train_1 = split_for('train', [4, 5])
  split_test_1 = split_for('test', [3])

  split_train_2 = split_for('train', [3, 7])
  builder_dirs = {
      '/path/dataset/a': dataset_info([split_train_1, split_test_1]),
      '/path/dataset/b': dataset_info([split_train_2]),
  }
  for builder_dir, di_proto in builder_dirs.items():
    content = json_format.MessageToJson(di_proto, sort_keys=True)
    mock_fs.add_file(path=f'{builder_dir}/dataset_info.json', content=content)

  result = read_only_builder.builder_from_directories(list(builder_dirs.keys()))

  assert isinstance(result, read_only_builder.ReadOnlyBuilder)
  assert isinstance(result.info.splits['train'], splits_lib.MultiSplitInfo)
  assert isinstance(result.info.splits['test'], splits_lib.MultiSplitInfo)

  assert str(result.info.splits['test']) == (
      'MultiSplitInfo(name=\'test\', '
      'split_infos=[<SplitInfo num_examples=3, num_shards=1>])')
  assert str(result.info.splits['train']) == (
      'MultiSplitInfo(name=\'train\', split_infos=['
      '<SplitInfo num_examples=9, num_shards=2>, '
      '<SplitInfo num_examples=10, num_shards=2>])')


def test_builder_from_directories_reading(
    code_builder: dataset_builder.DatasetBuilder):
  other_dir1 = f'{code_builder.data_dir}/other1'
  other_dir2 = f'{code_builder.data_dir}/other2'

  # Copy from code_builder dir to the new dirs.
  tf.io.gfile.makedirs(other_dir1)
  tf.io.gfile.makedirs(other_dir2)
  for filename in tf.io.gfile.listdir(code_builder.data_dir):
    filepath = f'{code_builder.data_dir}/{filename}'
    if not tf.io.gfile.isdir(filepath):
      tf.io.gfile.copy(
          src=filepath, dst=f'{other_dir1}/{filename}', overwrite=True)
      tf.io.gfile.copy(
          src=filepath, dst=f'{other_dir2}/{filename}', overwrite=True)

  builder = read_only_builder.builder_from_directories(
      [other_dir1, other_dir2, code_builder.data_dir])
  train_np = dataset_utils.as_numpy(builder.as_dataset(split='train'))
  assert len(train_np) == 9
  ds = dataset_utils.as_numpy(builder.as_dataset(split='train').take(5))
  assert len(ds) == 5

  # Test split 'all'
  train_np = dataset_utils.as_numpy(builder.as_dataset(split='all'))
  assert len(train_np) == 9
  ds = dataset_utils.as_numpy(builder.as_dataset(split='all').take(5))
  assert len(ds) == 5
