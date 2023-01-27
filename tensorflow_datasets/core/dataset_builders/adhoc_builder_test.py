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

import os
from typing import Iterable

import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
import numpy as np
import tensorflow as tf

from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core.dataset_builders import adhoc_builder
import tensorflow_datasets.public_api as tfds


class TfDataBuilderTest(testing.TestCase):

  def test_tf_data_builder_no_config(self):
    ds_name = 'configless_dataset'
    data_dir = self.tmp_dir

    builder = adhoc_builder.store_as_tfds_dataset(
        name=ds_name,
        version='1.0.0',
        split_datasets={
            'train': tf.data.Dataset.from_tensor_slices({
                'a': [1, 2],
                'b': ['a', 'b'],
            }),
            'test': tf.data.Dataset.from_tensor_slices({
                'a': [3],
                'b': ['c'],
            }),
        },
        features=tfds.features.FeaturesDict({
            'a': tf.int64,
            'b': tfds.features.Text(),
        }),
        data_dir=data_dir,
        disable_shuffling=True,
    )

    assert builder.data_dir == os.path.join(self.tmp_dir, ds_name, '1.0.0')
    assert set(builder.info.splits.keys()) == {'train', 'test'}
    assert builder.info.disable_shuffling

    actual_train = tfds.load(
        f'{ds_name}:1.0.0', split='train', data_dir=data_dir
    )
    actual_train_np = list(dataset_utils.as_numpy(actual_train))
    assert actual_train_np == [{'a': 1, 'b': b'a'}, {'a': 2, 'b': b'b'}]

    actual_test = tfds.load(f'{ds_name}:1.0.0', split='test', data_dir=data_dir)
    actual_test_np = list(dataset_utils.as_numpy(actual_test))
    assert actual_test_np == [{'a': 3, 'b': b'c'}]

    builder_from_dir = tfds.builder_from_directory(
        builder_dir=os.path.join(data_dir, ds_name, '1.0.0')
    )
    actual_train_from_dir = builder_from_dir.as_dataset(split='train')
    actual_train_from_dir_np = list(
        dataset_utils.as_numpy(actual_train_from_dir)
    )
    assert actual_train_from_dir_np == [
        {'a': 1, 'b': b'a'},
        {'a': 2, 'b': b'b'},
    ]

  def test_tf_data_builder_with_config(self):
    ds_name = 'my_dataset'
    data_dir = self.tmp_dir

    builder = adhoc_builder.store_as_tfds_dataset(
        name=ds_name,
        version='1.0.0',
        split_datasets={
            'train': tf.data.Dataset.from_tensor_slices({
                'a': [1, 2],
                'b': ['a', 'b'],
            }),
            'test': tf.data.Dataset.from_tensor_slices({
                'a': [3],
                'b': ['c'],
            }),
        },
        features=tfds.features.FeaturesDict({
            'a': tf.int64,
            'b': tfds.features.Text(),
        }),
        config=dataset_builder.BuilderConfig(name='some_config'),
        data_dir=data_dir,
    )

    assert builder.data_dir == os.path.join(
        self.tmp_dir, ds_name, 'some_config', '1.0.0'
    )
    assert set(builder.info.splits.keys()) == {'train', 'test'}

    actual_train = tfds.load(
        f'{ds_name}/some_config:1.0.0', split='train', data_dir=data_dir
    )
    actual_train_np = list(dataset_utils.as_numpy(actual_train))
    assert actual_train_np == [{'a': 1, 'b': b'a'}, {'a': 2, 'b': b'b'}]

    actual_test = tfds.load(
        f'{ds_name}/some_config:1.0.0', split='test', data_dir=data_dir
    )
    actual_test_np = list(dataset_utils.as_numpy(actual_test))
    assert actual_test_np == [{'a': 3, 'b': b'c'}]

    builder_from_dir = tfds.builder_from_directory(
        builder_dir=os.path.join(data_dir, ds_name, 'some_config', '1.0.0')
    )
    actual_train_from_dir = builder_from_dir.as_dataset(split='train')
    actual_train_from_dir_np = list(
        dataset_utils.as_numpy(actual_train_from_dir)
    )
    assert actual_train_from_dir_np == [
        {'a': 1, 'b': b'a'},
        {'a': 2, 'b': b'b'},
    ]

  def test_tf_data_builder_multiple_versions(self):
    ds_name = 'my_dataset'
    data_dir = self.tmp_dir
    builder_a = adhoc_builder.store_as_tfds_dataset(
        name=ds_name,
        version='1.0.0',
        split_datasets={
            'train': tf.data.Dataset.from_tensor_slices({'a': [1]})
        },
        features=tfds.features.FeaturesDict({'a': tf.int64}),
        data_dir=data_dir,
    )

    builder_b = adhoc_builder.store_as_tfds_dataset(
        name=ds_name,
        version='2.0.0',
        split_datasets={
            'train': tf.data.Dataset.from_tensor_slices({'a': [2]})
        },
        features=tfds.features.FeaturesDict({'a': tf.int64}),
        data_dir=data_dir,
    )

    assert builder_a.data_dir == os.path.join(self.tmp_dir, ds_name, '1.0.0')
    assert builder_b.data_dir == os.path.join(self.tmp_dir, ds_name, '2.0.0')

    train1 = tfds.load(f'{ds_name}:1.0.0', split='train', data_dir=data_dir)
    assert list(dataset_utils.as_numpy(train1)) == [{'a': 1}]

    train2 = tfds.load(f'{ds_name}:2.0.0', split='train', data_dir=data_dir)
    assert list(dataset_utils.as_numpy(train2)) == [{'a': 2}]

  def test_tf_data_builder_multiple_configs(self):
    ds_name = 'my_dataset'
    data_dir = self.tmp_dir
    builder_a = adhoc_builder.store_as_tfds_dataset(
        name=ds_name,
        version='1.0.0',
        config=dataset_builder.BuilderConfig(name='a'),
        split_datasets={
            'train': tf.data.Dataset.from_tensor_slices({'a': [1]})
        },
        features=tfds.features.FeaturesDict({'a': tf.int64}),
        data_dir=data_dir,
    )

    builder_b = adhoc_builder.store_as_tfds_dataset(
        name=ds_name,
        version='1.0.0',
        config=dataset_builder.BuilderConfig(name='b'),
        split_datasets={
            'train': tf.data.Dataset.from_tensor_slices({'a': [2]})
        },
        features=tfds.features.FeaturesDict({'a': tf.int64}),
        data_dir=data_dir,
    )

    assert builder_a.data_dir == os.path.join(
        self.tmp_dir, ds_name, 'a', '1.0.0'
    )
    assert builder_b.data_dir == os.path.join(
        self.tmp_dir, ds_name, 'b', '1.0.0'
    )

    train1 = tfds.load(f'{ds_name}/a:1.0.0', split='train', data_dir=data_dir)
    assert list(dataset_utils.as_numpy(train1)) == [{'a': 1}]

    train2 = tfds.load(f'{ds_name}/b:1.0.0', split='train', data_dir=data_dir)
    assert list(dataset_utils.as_numpy(train2)) == [{'a': 2}]

  def test_tf_data_builder_class(self):
    ds_name = 'configless_dataset'
    data_dir = self.tmp_dir

    builder = adhoc_builder.TfDataBuilder(
        name=ds_name,
        version='1.0.0',
        split_datasets={
            'train': tf.data.Dataset.from_tensor_slices({
                'a': [1, 2],
                'b': ['a', 'b'],
            }),
            'test': tf.data.Dataset.from_tensor_slices({
                'a': [3],
                'b': ['c'],
            }),
        },
        features=tfds.features.FeaturesDict({
            'a': tf.int64,
            'b': tfds.features.Text(),
        }),
        data_dir=data_dir,
    )
    builder.download_and_prepare()

    actual_train = tfds.load(
        f'{ds_name}:1.0.0', split='train', data_dir=data_dir
    )
    actual_train_np = list(dataset_utils.as_numpy(actual_train))
    assert actual_train_np == [{'a': 1, 'b': b'a'}, {'a': 2, 'b': b'b'}]

    actual_test = tfds.load(f'{ds_name}:1.0.0', split='test', data_dir=data_dir)
    actual_test_np = list(dataset_utils.as_numpy(actual_test))
    assert actual_test_np == [{'a': 3, 'b': b'c'}]


def generate_example(i: int, split: str):
  return i, {
      'id': i,
      'id_str': f'split={split} id={i}',
  }


def sort_ds_by_id(ds):
  return sorted(dataset_utils.as_numpy(ds), key=lambda x: x['id'])


class BeamBuilderTest(testing.TestCase):
  _DEFAULT_FEATURES = tfds.features.FeaturesDict({
      'id': tfds.features.Scalar(dtype=np.int64),
      'id_str': tfds.features.Text(),
  })

  def test_pcollection_is_not_iterable(self):
    with TestPipeline() as pipeline:
      d = pipeline | beam.Create(range(3))
      assert isinstance(d, beam.PCollection) or isinstance(
          d, beam.pvalue.PCollection
      )
      assert not isinstance(d, Iterable)

  def test_no_config(self):
    builder = adhoc_builder.store_as_tfds_dataset(
        name='adhoc',
        version='1.2.3',
        data_dir=self.tmp_dir,
        features=self._DEFAULT_FEATURES,
        split_datasets={
            'train': beam.Create(range(3)) | beam.Map(
                generate_example, split='train'
            ),
            'test': beam.Create(range(2)) | beam.Map(
                generate_example, split='test'
            ),
        },
    )

    assert builder.data_dir == os.path.join(self.tmp_dir, 'adhoc', '1.2.3')

    actual_train = tfds.load(
        'adhoc:1.2.3', split='train', data_dir=self.tmp_dir
    )
    assert sort_ds_by_id(actual_train) == [
        {'id': 0, 'id_str': b'split=train id=0'},
        {'id': 1, 'id_str': b'split=train id=1'},
        {'id': 2, 'id_str': b'split=train id=2'},
    ]

    actual_test = tfds.load('adhoc:1.2.3', split='test', data_dir=self.tmp_dir)
    assert sort_ds_by_id(actual_test) == [
        {'id': 0, 'id_str': b'split=test id=0'},
        {'id': 1, 'id_str': b'split=test id=1'},
    ]

  def test_config(self):
    builder_a = adhoc_builder.store_as_tfds_dataset(
        name='adhoc',
        version='1.2.3',
        config='a',
        data_dir=self.tmp_dir,
        features=self._DEFAULT_FEATURES,
        split_datasets={
            'train': beam.Create(range(3)) | beam.Map(
                generate_example, split='train'
            )
        },
    )

    builder_b = adhoc_builder.store_as_tfds_dataset(
        name='adhoc',
        version='1.2.3',
        config='b',
        data_dir=self.tmp_dir,
        features=self._DEFAULT_FEATURES,
        split_datasets={
            'train': beam.Create(range(2)) | beam.Map(
                generate_example, split='train'
            )
        },
    )

    assert builder_a.data_dir == os.path.join(
        self.tmp_dir, 'adhoc', 'a', '1.2.3'
    )
    assert builder_b.data_dir == os.path.join(
        self.tmp_dir, 'adhoc', 'b', '1.2.3'
    )

    actual_a = tfds.load('adhoc/a:1.2.3', split='train', data_dir=self.tmp_dir)
    assert sort_ds_by_id(actual_a) == [
        {'id': 0, 'id_str': b'split=train id=0'},
        {'id': 1, 'id_str': b'split=train id=1'},
        {'id': 2, 'id_str': b'split=train id=2'},
    ]

    actual_b = tfds.load('adhoc/b:1.2.3', split='train', data_dir=self.tmp_dir)
    assert sort_ds_by_id(actual_b) == [
        {'id': 0, 'id_str': b'split=train id=0'},
        {'id': 1, 'id_str': b'split=train id=1'},
    ]


def my_iterator(max_i: int, split: str):
  for i in range(max_i):
    yield generate_example(i, split)


class IteratorBuilderTest(testing.TestCase):
  _DEFAULT_FEATURES = tfds.features.FeaturesDict({
      'id': tfds.features.Scalar(dtype=np.int64),
      'id_str': tfds.features.Text(),
  })

  def test_no_config(self):
    builder = adhoc_builder.store_as_tfds_dataset(
        name='adhoc',
        version='1.2.3',
        data_dir=self.tmp_dir,
        features=self._DEFAULT_FEATURES,
        split_datasets={
            'train': my_iterator(max_i=3, split='train'),
            'test': my_iterator(max_i=2, split='test'),
        },
    )

    assert builder.data_dir == os.path.join(self.tmp_dir, 'adhoc', '1.2.3')
    assert set(builder.info.splits.keys()) == {'train', 'test'}

    actual_train = tfds.load(
        'adhoc:1.2.3', split='train', data_dir=self.tmp_dir
    )
    assert sort_ds_by_id(actual_train) == [
        {'id': 0, 'id_str': b'split=train id=0'},
        {'id': 1, 'id_str': b'split=train id=1'},
        {'id': 2, 'id_str': b'split=train id=2'},
    ]

    actual_test = tfds.load('adhoc:1.2.3', split='test', data_dir=self.tmp_dir)
    assert sort_ds_by_id(actual_test) == [
        {'id': 0, 'id_str': b'split=test id=0'},
        {'id': 1, 'id_str': b'split=test id=1'},
    ]

  def test_list(self):
    adhoc_builder.store_as_tfds_dataset(
        name='adhoc',
        version='1.2.3',
        data_dir=self.tmp_dir,
        features=self._DEFAULT_FEATURES,
        split_datasets={
            'train': list(my_iterator(max_i=1, split='train')),
        },
    )

    actual_train = tfds.load(
        'adhoc:1.2.3', split='train', data_dir=self.tmp_dir
    )
    assert sort_ds_by_id(actual_train) == [
        {'id': 0, 'id_str': b'split=train id=0'},
    ]
