# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for file_adapters."""

import pathlib
from typing import Type

import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import file_adapters


def test_is_example_file():
  assert file_adapters.is_example_file('example1.tfrecord')
  assert file_adapters.is_example_file('example1.riegeli')
  assert file_adapters.is_example_file('example1.tfrecord-00000-of-00001')
  assert not file_adapters.is_example_file('example1.info')


def test_format_suffix():
  assert (
      file_adapters.ADAPTER_FOR_FORMAT[
          file_adapters.DEFAULT_FILE_FORMAT
      ].FILE_SUFFIX
      == 'tfrecord'
  )
  assert (
      file_adapters.ADAPTER_FOR_FORMAT[
          file_adapters.FileFormat.TFRECORD
      ].FILE_SUFFIX
      == 'tfrecord'
  )
  assert (
      file_adapters.ADAPTER_FOR_FORMAT[
          file_adapters.FileFormat.RIEGELI
      ].FILE_SUFFIX
      == 'riegeli'
  )


@pytest.mark.parametrize(
    'file_format',
    [
        file_adapters.FileFormat.TFRECORD,
    ],
)
@pytest.mark.parametrize(
    'builder_cls',
    [
        testing.DummyDataset,
        testing.DummyBeamDataset,
    ],
)
def test_read_write(
    tmp_path: pathlib.Path,
    builder_cls: Type[dataset_builder.DatasetBuilder],
    file_format: file_adapters.FileFormat,
):
  builder = builder_cls(data_dir=tmp_path, file_format=file_format)
  builder.download_and_prepare()
  ds = builder.as_dataset(split='train')
  assert list(ds.as_numpy_iterator()) == [{'id': i} for i in range(3)]


def test_as_dataset_fails_for_array_record(
    tmp_path: pathlib.Path,
):
  builder = testing.DummyDataset(
      data_dir=tmp_path, file_format=file_adapters.FileFormat.ARRAY_RECORD
  )
  builder.download_and_prepare()
  with pytest.raises(
      NotImplementedError, match='not implemented for ArrayRecord files'
  ):
    ds = builder.as_dataset(split='train')


def test_prase_file_format():
  assert (
      file_adapters.FileFormat.from_value('tfrecord')
      == file_adapters.FileFormat.TFRECORD
  )
  assert (
      file_adapters.FileFormat.from_value(file_adapters.FileFormat.TFRECORD)
      == file_adapters.FileFormat.TFRECORD
  )
  assert (
      file_adapters.FileFormat.from_value('riegeli')
      == file_adapters.FileFormat.RIEGELI
  )
  assert (
      file_adapters.FileFormat.from_value(file_adapters.FileFormat.RIEGELI)
      == file_adapters.FileFormat.RIEGELI
  )
  with pytest.raises(ValueError, match='is not a valid FileFormat'):
    file_adapters.FileFormat.from_value('i do not exist')
  assert (
      file_adapters.FileFormat.from_value('array_record')
      == file_adapters.FileFormat.ARRAY_RECORD
  )
  assert (
      file_adapters.FileFormat.from_value(file_adapters.FileFormat.ARRAY_RECORD)
      == file_adapters.FileFormat.ARRAY_RECORD
  )
