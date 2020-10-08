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

"""Tests for `tensorflow_datasets.core.as_dataframe`."""

import pandas

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import as_dataframe
from tensorflow_datasets.core import load

# Import for registration
# pylint: disable=unused-import,g-bad-import-order
from tensorflow_datasets.image_classification import mnist
from tensorflow_datasets.text import anli
# pylint: enable=unused-import,g-bad-import-order


def _as_df(ds_name: str, **kwargs) -> pandas.DataFrame:
  """Loads the dataset as `pandas.DataFrame`."""
  with testing.mock_data(num_examples=3):
    ds, ds_info = load.load(ds_name, split='train', with_info=True, **kwargs)
  df = as_dataframe.as_dataframe(ds, ds_info)
  return df


def test_flatten_with_path():
  """Test that the flatten function works as expected"""
  from from tensorflow_datasets.core.as_dataframe import _flatten_with_path
  assert list(_flatten_with_path('value')) == [([], 'value')]
  assert list(_flatten_with_path({'key': 'value'})) == [('key', 'value')]
  assert list(_flatten_with_path({'key1': 'value', 'key2': 'value2'})) == [
    ('key1', 'value'),
    ('key2', 'value2'),
  ]
  complex_dict = {
    'key': 'value',
    'nested': {
      'sub_key': 'subvalue',
      'sub_nested': {
        'subsubkey1': 'subsubvalue1',
        'subsubkey2': 'subsubvalue2',
      },
      'key2': 'value2',
    }
  }
  assert list(_flatten_with_path(complex_dict)) == [
    (['key'], 'value'),
    (['key2'], 'value2'),
    (['nested', 'subkey'], 'subvalue'),
    (['nested', 'sub_nested', 'subsubkey1'], 'subsubvalue1'),
    (['nested', 'sub_nested', 'subsubkey2'], 'subsubvalue2'),
  ]

def test_flatten():
  """Test that the flatten function works as expected"""
  from from tensorflow_datasets.core.as_dataframe import _flatten
  assert list(_flatten('value')) == ['value']
  assert list(_flatten({'key': 'value'})) == ['value']
  assert list(_flatten({'key1': 'value', 'key2': 'value2'})) == ['value', 'value2']
  complex_dict = {
    'key': 'value',
    'nested': {
      'sub_key': 'subvalue',
      'sub_nested': {
        'subsubkey1': 'subsubvalue1',
        'subsubkey2': 'subsubvalue2',
      },
      'key2': 'value2',
    }
  }
  assert list(_flatten(complex_dict)) == ['value', 'value2', 'subvalue', 'subsubvalue1', 'subsubvalue2']

def test_as_dataframe():
  """Tests that as_dataframe works without the `tfds.core.DatasetInfo`."""
  ds = tf.data.Dataset.from_tensor_slices(
      {
          'some_key': [1, 2, 3],
          'nested': {
              'sub1': [1.0, 2.0, 3.0],
          },
      }
  )
  df = as_dataframe.as_dataframe(ds)
  assert isinstance(df, pandas.DataFrame)
  assert df._repr_html_().startswith('<style')
  assert list(df.columns) == ['nested/sub1', 'some_key']


def test_text_dataset():
  df = _as_df('anli')
  assert isinstance(df, pandas.DataFrame)
  assert isinstance(df._repr_html_(), str)
  assert list(df.columns) == ['context', 'hypothesis', 'label', 'uid']


def test_as_supervised():
  df = _as_df('mnist', as_supervised=True)
  assert isinstance(df, pandas.DataFrame)
  assert isinstance(df._repr_html_(), str)
  assert list(df.columns) == ['image', 'label']
