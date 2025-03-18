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

"""Tests for file_adapters."""

import os
import pathlib
from typing import Type, TypeAlias

import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import file_adapters


FileFormat: TypeAlias = file_adapters.FileFormat


def test_batched():
  assert list(file_adapters._batched(range(10), 5)) == [
      [0, 1, 2, 3, 4],
      [5, 6, 7, 8, 9],
  ]
  assert list(file_adapters._batched(range(10), 100)) == [
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  ]
  assert not list(file_adapters._batched(range(10), 0))


def test_is_example_file():
  assert file_adapters.is_example_file('example1.tfrecord')
  assert file_adapters.is_example_file('example1.riegeli')
  assert file_adapters.is_example_file('example1.tfrecord-00000-of-00001')
  assert not file_adapters.is_example_file('example1.info')


@pytest.mark.parametrize(
    'format_suffix,file_format',
    (
        ('array_record', FileFormat.ARRAY_RECORD),
        ('parquet', FileFormat.PARQUET),
        ('riegeli', FileFormat.RIEGELI),
        ('tfrecord', FileFormat.TFRECORD),
    ),
)
def test_format_suffix(format_suffix, file_format):
  assert (
      file_adapters.ADAPTER_FOR_FORMAT[file_format].FILE_SUFFIX == format_suffix
  )


@pytest.mark.parametrize(
    'file_format',
    [
        file_format
        for file_format in FileFormat
        if file_format in FileFormat.with_tf_data()
        and file_format != FileFormat.RIEGELI
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
    file_format: FileFormat,
):
  builder = builder_cls(data_dir=tmp_path, file_format=file_format)
  builder.download_and_prepare()
  ds = builder.as_dataset(split='train')
  assert list(ds.as_numpy_iterator()) == [{'id': i} for i in range(3)]


def test_as_dataset_fails_for_array_record(
    tmp_path: pathlib.Path,
):
  builder = testing.DummyDataset(
      data_dir=tmp_path, file_format=FileFormat.ARRAY_RECORD
  )
  builder.download_and_prepare()
  with pytest.raises(
      NotImplementedError, match='not implemented for ArrayRecord files'
  ):
    ds = builder.as_dataset(split='train')


@pytest.mark.parametrize(
    'format_enum_value,file_format',
    (
        ('array_record', FileFormat.ARRAY_RECORD),
        ('parquet', FileFormat.PARQUET),
        ('riegeli', FileFormat.RIEGELI),
        ('tfrecord', FileFormat.TFRECORD),
    ),
)
def test_prase_file_format(format_enum_value, file_format):
  assert FileFormat.from_value(format_enum_value) == file_format
  assert FileFormat.from_value(file_format) == file_format


@pytest.mark.parametrize(
    'path,file_format,expected_path',
    (
        (
            '/tmp/dataset-train.tfrecord-00000-of-00001',
            file_adapters.FileFormat.TFRECORD,
            '/tmp/dataset-train.tfrecord-00000-of-00001',
        ),
        (
            '/tmp/dataset-train.riegeli-00000-of-00001',
            file_adapters.FileFormat.TFRECORD,
            '/tmp/dataset-train.tfrecord-00000-of-00001',
        ),
        (
            '/tmp/dataset-train.tfrecord-00000-of-00001',
            file_adapters.FileFormat.RIEGELI,
            '/tmp/dataset-train.riegeli-00000-of-00001',
        ),
    ),
)
def test_convert_path_to_file_format(path, file_format, expected_path):
  converted_path = file_adapters.convert_path_to_file_format(path, file_format)
  assert os.fspath(converted_path) == expected_path
