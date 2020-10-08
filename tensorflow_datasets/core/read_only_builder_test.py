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

"""Tests for read_only_builder."""

import pathlib
from unittest import mock

import pytest

from tensorflow_datasets import testing
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import load
from tensorflow_datasets.core import read_only_builder


class DummyNoConfMnist(testing.DummyMnist):
  """Same as DummyMnist (but declared here to avoid skip_registering issues)."""


class DummyConfigMnist(testing.DummyMnist):
  """Same as DummyMnist, but with config."""

  BUILDER_CONFIGS = [
      dataset_builder.BuilderConfig(
          name='dummy_config', version='0.1.0', description='testing config',
      )
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
      f'{code_builder.name}:*.*.*', data_dir='/tmp/path/tfds/not-exists'
  )
  assert isinstance(builder, type(code_builder))
  assert not isinstance(builder, read_only_builder.ReadOnlyBuilder)


def test_builder_code_not_found(code_builder: dataset_builder.DatasetBuilder):
  """If the code isn't found, use files instead."""

  # Patch `tfds.builder_cls` to emulate that the dataset isn't registered
  with mock.patch.object(
      load,
      'builder_cls',
      side_effect=load.DatasetNotFoundError(code_builder.name),
  ):
    # When the code isn't found, loading dataset require explicit config name:
    # tfds.builder('ds/config')
    config_name = code_builder.name
    if code_builder.builder_config:
      config_name = f'{config_name}/{code_builder.builder_config.name}'

    # Files exists, but not code, loading from files
    builder = load.builder(config_name)
    assert isinstance(builder, read_only_builder.ReadOnlyBuilder)
    load.load(config_name, split=[])  # Dataset found -> no error

    # Neither code not files found, raise DatasetNotFoundError
    with pytest.raises(load.DatasetNotFoundError):
      load.builder(config_name, data_dir='/tmp/non-existing/tfds/dir')

    with pytest.raises(load.DatasetNotFoundError):
      load.load(config_name, split=[], data_dir='/tmp/non-existing/tfds/dir')


# Test both with and without config
def test_read_only_builder(code_builder: dataset_builder.DatasetBuilder):
  """Builder can be created from the files only."""

  # Reconstruct the dataset
  builder = read_only_builder.builder_from_directory(code_builder.data_dir)
  assert builder.name == code_builder.name
  assert builder.data_dir == code_builder.data_dir
  assert builder.info.version == code_builder.info.version
  assert builder.info.full_name == code_builder.info.full_name
  assert repr(builder.info) == repr(code_builder.info)
  assert builder.VERSION is None

  # Test that the dataset can be read
  ds = dataset_utils.as_numpy(builder.as_dataset(split='train').take(5))
  origin_ds = dataset_utils.as_numpy(builder.as_dataset(split='train').take(5))
  assert [ex['label'] for ex in ds] == [ex['label'] for ex in origin_ds]

  builder.download_and_prepare()  # Should be a no-op


def test_not_exists(tmp_path: pathlib.Path):
  with pytest.raises(
      FileNotFoundError, match='Could not load `ReadOnlyBuilder`'
  ):
    read_only_builder.builder_from_directory(tmp_path)


def test_not_registered():
  """Ensure the ReadOnlyBuilder is not registered."""
  assert read_only_builder.ReadOnlyBuilder.name not in load.list_builders()
