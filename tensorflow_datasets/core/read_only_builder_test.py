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

import pytest

from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import load
from tensorflow_datasets.core import read_only_builder


class DummyConfigMnist(testing.DummyMnist):

  BUILDER_CONFIGS = [
      dataset_builder.BuilderConfig(
          name='dummy_config', version='0.1.0', description='testing config',
      )
  ]


# Test both with and without config
@pytest.mark.parametrize('builder_cls', [testing.DummyMnist, DummyConfigMnist])
def test_read_only_builder(
    builder_cls: dataset_builder.DatasetBuilder,
    tmp_path: pathlib.Path,
):
  # Generate the dataset
  origin_builder = builder_cls(data_dir=tmp_path)
  origin_builder.download_and_prepare()

  # Reconstruct the dataset
  builder = read_only_builder.builder_from_directory(origin_builder.data_dir)
  assert builder.name == origin_builder.name
  assert builder.data_dir == origin_builder.data_dir
  assert builder.info.version == origin_builder.info.version
  assert builder.info.full_name == origin_builder.info.full_name
  assert repr(builder.info) == repr(origin_builder.info)
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


def test_registered():
  """Ensure the ReadOnlyBuilder is not registered."""
  assert read_only_builder.ReadOnlyBuilder.name not in load.list_builders()
