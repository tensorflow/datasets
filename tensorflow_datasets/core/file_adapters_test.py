# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

from etils import epath
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming


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


@pytest.mark.parametrize(
    'adapter_cls',
    (
        (file_adapters.TfRecordFileAdapter),
        (file_adapters.ArrayRecordFileAdapter),
    ),
)
def test_shard_lengths(
    tmp_path: pathlib.Path, adapter_cls: file_adapters.FileAdapter
):
  file_template = naming.ShardedFileTemplate(
      data_dir=tmp_path,
      dataset_name='data',
      filetype_suffix=adapter_cls.FILE_SUFFIX,
      split='train',
  )
  tmp_path_1 = file_template.sharded_filepath(shard_index=0, num_shards=2)
  tmp_path_2 = file_template.sharded_filepath(shard_index=1, num_shards=2)
  adapter_cls.write_examples(
      tmp_path_1, [(0, b'0'), (1, b'1'), (2, b'2222'), (3, b'33333')]
  )
  adapter_cls.write_examples(tmp_path_2, [(3, b'3'), (4, b'4'), (5, b'555')])
  size_1 = epath.Path(tmp_path_1).stat().length
  size_2 = epath.Path(tmp_path_2).stat().length
  expected_shard_lengths = [(4, size_1), (3, size_2)]

  # First test without passing the number of shards explicitly.
  actual_no_num_shards = adapter_cls.shard_lengths_and_sizes(file_template)
  assert actual_no_num_shards == expected_shard_lengths, 'no num_shards passed'

  # Now test with passing the number of shards explicitly.
  actual_with_num_shards = adapter_cls.shard_lengths_and_sizes(
      file_template,
      num_shards=2,
  )
  assert actual_with_num_shards == expected_shard_lengths, 'num_shards passed'
