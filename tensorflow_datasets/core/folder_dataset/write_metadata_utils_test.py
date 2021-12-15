# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Tests for write_metadata_lib."""

import pathlib

import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.folder_dataset import write_metadata_utils


@pytest.mark.parametrize(
    'file_format',
    [
        None,
    ],
)
def test_write_metadata(
    tmp_path: pathlib.Path,
    file_format,
):
  tmp_path = utils.as_path(tmp_path)

  src_builder = testing.DummyDataset(
      data_dir=tmp_path / 'origin',
      file_format=file_format,
  )
  src_builder.download_and_prepare()

  dst_dir = tmp_path / 'copy'
  dst_dir.mkdir()

  # Copy all the tfrecord files, but not the dataset info
  for f in src_builder.data_path.iterdir():
    if naming.FilenameInfo.is_valid(f.name):
      f.copy(dst_dir / f.name)

  metadata_path = dst_dir / 'dataset_info.json'

  if file_format is None:
    split_infos = list(src_builder.info.splits.values())
  else:
    split_infos = None  # Auto-compute split infos

  assert not metadata_path.exists()
  write_metadata_utils.write_metadata(
      data_dir=dst_dir,
      features=src_builder.info.features,
      split_infos=split_infos,
      description='my test description.')
  assert metadata_path.exists()

  # After metadata are written, builder can be restored from the directory
  builder = read_only_builder.builder_from_directory(dst_dir)
  assert builder.name == 'dummy_dataset'
  assert builder.version == '1.0.0'
  assert set(builder.info.splits) == {'train'}
  assert builder.info.splits['train'].num_examples == 3
  assert builder.info.description == 'my test description.'

  # Values are the same
  src_ds = src_builder.as_dataset(split='train')
  ds = builder.as_dataset(split='train')
  assert list(src_ds.as_numpy_iterator()) == list(ds.as_numpy_iterator())
