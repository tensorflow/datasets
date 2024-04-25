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

"""Tests for tensorflow_datasets.core.load.

Note: `load.py` code was previously in `registered.py`, so some of the tests
are still on `registered_test.py`.
"""

import logging
from unittest import mock

import pytest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import load
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import visibility
def test_load_hf_dataset():
  builder = object()
  with mock.patch(
      'tensorflow_datasets.core.dataset_builders.huggingface_dataset_builder.builder',
      return_value=builder,
  ):
    assert load.builder('huggingface:x/y') is builder


@visibility.set_availables_tmp([
    visibility.DatasetType.COMMUNITY_PUBLIC,
])
def test_community_public_load():
  with mock.patch(
      'tensorflow_datasets.core.community.registry.DatasetRegistry.list_builders',
      return_value=['ns:ds'],
  ), mock.patch(
      'tensorflow_datasets.core.community.registry.DatasetRegistry.builder_cls',
      return_value=testing.DummyDataset,
  ), mock.patch(
      'tensorflow_datasets.core.registered.list_imported_builders',
      return_value=[],
  ):
    assert load.list_builders() == ['ns:ds']

    # Builder is correctly returned
    assert load.builder_cls('ns:ds') is testing.DummyDataset
    assert isinstance(load.builder('ns:ds'), testing.DummyDataset)


@pytest.fixture(scope='session')
def dummy_dc_loader() -> load.DatasetCollectionLoader:
  return load.DatasetCollectionLoader(
      collection=testing.DummyDatasetCollection()
  )


def test_dc_loader_name(dummy_dc_loader: load.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  assert dummy_dc_loader.collection_name == 'dummy_dataset_collection'


def test_load_dataset(dummy_dc_loader: load.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  with mock.patch.object(load, 'load', autospec=True) as mock_load:
    examples = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    expected = {'train': examples, 'test': examples}
    mock_load.return_value = expected
    loaded_dataset = dummy_dc_loader.load_dataset('c')
    mock_load.assert_called_once_with(name='c/e:3.5.7', with_info=False)
    assert loaded_dataset == expected


def test_load_dataset_split(dummy_dc_loader: load.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  with mock.patch.object(load, 'load', autospec=True) as mock_load:
    examples = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    expected = {'train': examples}
    mock_load.return_value = [examples, examples]
    loaded_dataset = dummy_dc_loader.load_dataset('c', split='train')
    mock_load.assert_called_once_with(
        name='c/e:3.5.7', with_info=False, split=['train']
    )
    assert loaded_dataset == expected


def test_load_dataset_splits(dummy_dc_loader: load.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  with mock.patch.object(load, 'load', autospec=True) as mock_load:
    examples = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    expected = {'train': examples, 'test': examples}
    mock_load.return_value = [examples, examples]
    loaded_dataset = dummy_dc_loader.load_dataset('c', split=['train', 'test'])
    mock_load.assert_called_once_with(
        name='c/e:3.5.7', with_info=False, split=['train', 'test']
    )
    assert loaded_dataset == expected


def test_load_dataset_runtime_error(
    dummy_dc_loader: load.DatasetCollectionLoader,
):  # pylint: disable=redefined-outer-name
  with pytest.raises(RuntimeError, match='Unsupported return type.+'):
    with mock.patch.object(load, 'load', autospec=True) as mock_load:
      examples = tf.data.Dataset.from_tensor_slices([1, 2, 3])
      mock_load.return_value = examples
      dummy_dc_loader.load_dataset('c')


def test_load_dataset_key_error(dummy_dc_loader: load.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  with pytest.raises(
      KeyError, match='Dataset d is not included in this collection.+'
  ):
    dummy_dc_loader.load_dataset('d')


def test_load_dataset_with_kwargs(
    dummy_dc_loader: load.DatasetCollectionLoader,
):  # pylint: disable=redefined-outer-name
  with mock.patch.object(load, 'load', autospec=True) as mock_load:
    examples = tf.data.Dataset.from_tensor_slices([1, 2, 3])
    expected = {'train': examples, 'test': examples}
    mock_load.return_value = expected
    loaded_dataset = dummy_dc_loader.load_dataset(
        'c', loader_kwargs={'with_info': True, 'batch_size': 3}
    )

    mock_load.assert_called_once_with(
        name='c/e:3.5.7', with_info=False, batch_size=3
    )
    assert loaded_dataset == expected


@pytest.mark.parametrize(
    'builder_kwargs',
    [
        None,
        {'file_format': 'array_record'},
        {'file_format': file_adapters.FileFormat.ARRAY_RECORD},
    ],
)
def test_data_source_defaults_to_array_record_format(
    builder_kwargs,
):
  with mock.patch.object(load, 'builder', autospec=True) as mock_builder:
    load.data_source(
        'mydataset', builder_kwargs=builder_kwargs,
    )
    mock_builder.assert_called_with(
        'mydataset',
        data_dir=None,
        try_gcs=False,
        file_format=file_adapters.FileFormat.ARRAY_RECORD,
    )
@pytest.mark.parametrize(
    'file_format',
    ['tfrecord', file_adapters.FileFormat.TFRECORD],
)
def test_data_source_raises_error_for_other_file_formats(file_format):
  with pytest.raises(
      NotImplementedError, match='No random access data source'
  ):
    with mock.patch.object(load, 'builder', autospec=True):
      load.data_source(
          'mydataset', builder_kwargs={'file_format': file_format}
      )
