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

"""Tests for all data sources."""

from unittest import mock

from etils import epath
import pytest
import tensorflow_datasets as tfds
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.data_sources import array_record
from tensorflow_datasets.core.data_sources import parquet
from tensorflow_datasets.core.utils import shard_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import array_record_data_source
from tensorflow_datasets.core.utils.lazy_imports_utils import parquet as pq


@pytest.fixture()
def mocked_array_record_dataset():
  mock_data_source = mock.create_autospec(
      array_record_data_source.ArrayRecordDataSource,
      spec_set=True,
  )
  with mock.patch.object(
      array_record_data_source,
      'ArrayRecordDataSource',
      return_value=mock_data_source,
  ):
    yield


@pytest.fixture()
def mocked_parquet_dataset():
  mock_data_source = mock.create_autospec(
      pq.ParquetDataset,
      spec_set=True,
  )
  with mock.patch.object(
      pq,
      'ParquetDataset',
      return_value=mock_data_source,
  ):
    yield


_FIXTURES = ['mocked_array_record_dataset', 'mocked_parquet_dataset']
_DATA_SOURCE_CLS = [
    array_record.ArrayRecordDataSource,
    parquet.ParquetDataSource,
]


@pytest.mark.parametrize(
    'file_format', file_adapters.FileFormat.with_random_access()
)
@pytest.mark.parametrize(
    'builder_cls',
    [testing.DummyDataset, testing.DummyBeamDataset],
)
def test_read_write(
    tmp_path: epath.Path,
    builder_cls: dataset_builder.DatasetBuilder,
    file_format: file_adapters.FileFormat,
):
  builder = builder_cls(data_dir=tmp_path, file_format=file_format)
  builder.download_and_prepare()
  data_source = builder.as_data_source(split='train')
  assert len(data_source) == 3
  for i in range(3):
    assert data_source[i] == {'id': i}
  assert data_source.__getitems__([0, 2]) == [{'id': 0}, {'id': 2}]
  assert data_source.__getitems__(range(0, 2)) == [{'id': 0}, {'id': 1}]
  assert data_source.__getitems__([]) == []  # pylint: disable=g-explicit-bool-comparison
  for i, element in enumerate(data_source):
    assert element == {'id': i}


_FILE_INSTRUCTIONS = [
    shard_utils.FileInstruction(
        'my_file-000-of-003', skip=0, take=12, examples_in_shard=12
    ),
    shard_utils.FileInstruction(
        'my_file-001-of-003', skip=2, take=9, examples_in_shard=11
    ),
    shard_utils.FileInstruction(
        'my_file-002-of-003', skip=0, take=4, examples_in_shard=4
    ),
]


def create_dataset_info(file_format: file_adapters.FileFormat):
  with mock.patch.object(splits_lib, 'SplitInfo') as split_mock:
    split_mock.return_value.name = 'train'
    split_mock.return_value.file_instructions = _FILE_INSTRUCTIONS
    dataset_info = mock.create_autospec(dataset_info_lib.DatasetInfo)
    dataset_info.file_format = file_format
    dataset_info.splits = {'train': split_mock()}
    dataset_info.name = 'dataset_name'
    return dataset_info


@pytest.mark.parametrize(
    'data_source_cls',
    _DATA_SOURCE_CLS,
)
def test_missing_split_raises_error(data_source_cls):
  dataset_info = create_dataset_info(file_adapters.FileFormat.ARRAY_RECORD)
  with pytest.raises(
      ValueError,
      match="Unknown split 'doesnotexist'.",
  ):
    data_source_cls(dataset_info, split='doesnotexist')


@pytest.mark.usefixtures(*_FIXTURES)
@pytest.mark.parametrize(
    'data_source_cls',
    _DATA_SOURCE_CLS,
)
def test_repr_returns_meaningful_string_without_decoders(data_source_cls):
  dataset_info = create_dataset_info(file_adapters.FileFormat.ARRAY_RECORD)
  source = data_source_cls(dataset_info, split='train')
  name = data_source_cls.__name__
  assert (
      repr(source) == f"{name}(name=dataset_name, split='train', decoders=None)"
  )


@pytest.mark.usefixtures(*_FIXTURES)
@pytest.mark.parametrize(
    'data_source_cls',
    _DATA_SOURCE_CLS,
)
def test_repr_returns_meaningful_string_with_decoders(data_source_cls):
  dataset_info = create_dataset_info(file_adapters.FileFormat.ARRAY_RECORD)
  source = data_source_cls(
      dataset_info,
      split='train',
      decoders={'my_feature': decode.SkipDecoding()},
  )
  name = data_source_cls.__name__
  assert (
      repr(source)
      == f'{name}(name=dataset_name,'
      " split='train', decoders={'my_feature': <class"
      " 'tensorflow_datasets.core.decode.base.SkipDecoding'>})"
  )


def test_data_source_is_sliceable():
  mock_array_record_data_source = tfds.testing.PickableDataSourceMock()
  with tfds.testing.mock_data(
      mock_array_record_data_source=mock_array_record_data_source
  ):
    tfds.data_source('mnist', split='train')
    assert len(mock_array_record_data_source.call_args_list) == 1
    file_instructions = mock_array_record_data_source.call_args_list[0].args[0]
    assert file_instructions[0].skip == 0
    assert file_instructions[0].take == 60000

    tfds.data_source('mnist', split='train[:50%]')
    assert len(mock_array_record_data_source.call_args_list) == 2
    file_instructions = mock_array_record_data_source.call_args_list[1].args[0]
    assert file_instructions[0].skip == 0
    assert file_instructions[0].take == 30000
