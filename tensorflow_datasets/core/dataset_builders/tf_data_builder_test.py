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

"""Tests for the tf.data.Dataset based Dataset Builder."""

import os
import tempfile
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core.dataset_builders import tf_data_builder
import tensorflow_datasets.public_api as tfds


def test_tf_data_builder_no_config():
  ds_name = 'configless_dataset'
  data_dir = tempfile.mkdtemp()
  train = tf.data.Dataset.from_tensor_slices({
      'a': [1, 2],
      'b': ['a', 'b'],
  })
  test = tf.data.Dataset.from_tensor_slices({
      'a': [3],
      'b': ['c'],
  })

  builder = tf_data_builder.TfDataBuilder(
      name=ds_name,
      version='1.0.0',
      split_datasets={
          'train': train,
          'test': test,
      },
      features=tfds.features.FeaturesDict({
          'a': tf.int64,
          'b': tfds.features.Text(),
      }),
      data_dir=data_dir,
  )

  builder.download_and_prepare()

  actual_train = tfds.load(f'{ds_name}:1.0.0', split='train', data_dir=data_dir)
  actual_train_np = list(dataset_utils.as_numpy(actual_train))
  assert actual_train_np == [{'a': 1, 'b': b'a'}, {'a': 2, 'b': b'b'}]

  actual_test = tfds.load(f'{ds_name}:1.0.0', split='test', data_dir=data_dir)
  actual_test_np = list(dataset_utils.as_numpy(actual_test))
  assert actual_test_np == [{'a': 3, 'b': b'c'}]

  builder_from_dir = tfds.builder_from_directory(
      builder_dir=os.path.join(data_dir, ds_name, '1.0.0'))
  actual_train_from_dir = builder_from_dir.as_dataset(split='train')
  actual_train_from_dir_np = list(dataset_utils.as_numpy(actual_train_from_dir))
  assert actual_train_from_dir_np == [{'a': 1, 'b': b'a'}, {'a': 2, 'b': b'b'}]


def test_tf_data_builder_with_config():
  ds_name = 'my_dataset'
  data_dir = tempfile.mkdtemp()
  train = tf.data.Dataset.from_tensor_slices({
      'a': [1, 2],
      'b': ['a', 'b'],
  })
  test = tf.data.Dataset.from_tensor_slices({
      'a': [3],
      'b': ['c'],
  })

  builder = tf_data_builder.TfDataBuilder(
      name=ds_name,
      version='1.0.0',
      split_datasets={
          'train': train,
          'test': test,
      },
      features=tfds.features.FeaturesDict({
          'a': tf.int64,
          'b': tfds.features.Text(),
      }),
      config=dataset_builder.BuilderConfig(name='some_config'),
      data_dir=data_dir,
  )

  builder.download_and_prepare()

  actual_train = tfds.load(
      f'{ds_name}/some_config:1.0.0', split='train', data_dir=data_dir)
  actual_train_np = list(dataset_utils.as_numpy(actual_train))
  assert actual_train_np == [{'a': 1, 'b': b'a'}, {'a': 2, 'b': b'b'}]

  actual_test = tfds.load(
      f'{ds_name}/some_config:1.0.0', split='test', data_dir=data_dir)
  actual_test_np = list(dataset_utils.as_numpy(actual_test))
  assert actual_test_np == [{'a': 3, 'b': b'c'}]

  builder_from_dir = tfds.builder_from_directory(
      builder_dir=os.path.join(data_dir, ds_name, 'some_config', '1.0.0'))
  actual_train_from_dir = builder_from_dir.as_dataset(split='train')
  actual_train_from_dir_np = list(dataset_utils.as_numpy(actual_train_from_dir))
  assert actual_train_from_dir_np == [{'a': 1, 'b': b'a'}, {'a': 2, 'b': b'b'}]


def test_tf_data_builder_multiple_versions():
  ds_name = 'my_dataset'
  data_dir = tempfile.mkdtemp()
  builder1 = tf_data_builder.TfDataBuilder(
      name=ds_name,
      version='1.0.0',
      split_datasets={'train': tf.data.Dataset.from_tensor_slices({'a': [1]})},
      features=tfds.features.FeaturesDict({'a': tf.int64}),
      data_dir=data_dir,
  )
  builder1.download_and_prepare()

  builder2 = tf_data_builder.TfDataBuilder(
      name=ds_name,
      version='2.0.0',
      split_datasets={'train': tf.data.Dataset.from_tensor_slices({'a': [2]})},
      features=tfds.features.FeaturesDict({'a': tf.int64}),
      data_dir=data_dir,
  )
  builder2.download_and_prepare()

  train1 = tfds.load(f'{ds_name}:1.0.0', split='train', data_dir=data_dir)
  assert list(dataset_utils.as_numpy(train1)) == [{'a': 1}]

  train2 = tfds.load(f'{ds_name}:2.0.0', split='train', data_dir=data_dir)
  assert list(dataset_utils.as_numpy(train2)) == [{'a': 2}]


def test_tf_data_builder_multiple_configs():
  ds_name = 'my_dataset'
  data_dir = tempfile.mkdtemp()
  builder1 = tf_data_builder.TfDataBuilder(
      name=ds_name,
      version='1.0.0',
      config=dataset_builder.BuilderConfig(name='config1'),
      split_datasets={'train': tf.data.Dataset.from_tensor_slices({'a': [1]})},
      features=tfds.features.FeaturesDict({'a': tf.int64}),
      data_dir=data_dir,
  )
  builder1.download_and_prepare()

  builder2 = tf_data_builder.TfDataBuilder(
      name=ds_name,
      version='1.0.0',
      config=dataset_builder.BuilderConfig(name='config2'),
      split_datasets={'train': tf.data.Dataset.from_tensor_slices({'a': [2]})},
      features=tfds.features.FeaturesDict({'a': tf.int64}),
      data_dir=data_dir,
  )
  builder2.download_and_prepare()

  train1 = tfds.load(
      f'{ds_name}/config1:1.0.0', split='train', data_dir=data_dir)
  assert list(dataset_utils.as_numpy(train1)) == [{'a': 1}]

  train2 = tfds.load(
      f'{ds_name}/config2:1.0.0', split='train', data_dir=data_dir)
  assert list(dataset_utils.as_numpy(train2)) == [{'a': 2}]
