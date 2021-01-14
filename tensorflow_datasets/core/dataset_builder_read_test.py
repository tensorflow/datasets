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

"""Tests for tensorflow_datasets.core.dataset_builder_read."""

import pytest

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core.utils import read_config as read_config_lib


@pytest.fixture(scope='module')
def dummy_builder(tmp_path_factory):
  """Dummy dataset shared accross tests."""
  data_dir = tmp_path_factory.mktemp('datasets')
  builder = testing.DummyDataset(data_dir=data_dir)
  builder.download_and_prepare()
  yield builder


def test_add_tfds_id(dummy_builder: dataset_builder.DatasetBuilder):  # pylint: disable=redefined-outer-name
  """Tests `add_tfds_id=True`."""
  read_config = read_config_lib.ReadConfig(add_tfds_id=True)
  ds = dummy_builder.as_dataset(split='train', read_config=read_config)
  assert ds.element_spec == {
      'id': tf.TensorSpec(shape=(), dtype=tf.int64),
      'tfds_id': tf.TensorSpec(shape=(), dtype=tf.string),
  }
  assert list(dataset_utils.as_numpy(ds)) == [
      {'id': 0, 'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__0'},
      {'id': 1, 'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__1'},
      {'id': 2, 'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__2'},
  ]

  # Subsplit API works too
  ds = dummy_builder.as_dataset(split='train[1:]', read_config=read_config)
  assert ds.element_spec == {
      'id': tf.TensorSpec(shape=(), dtype=tf.int64),
      'tfds_id': tf.TensorSpec(shape=(), dtype=tf.string),
  }
  assert list(dataset_utils.as_numpy(ds)) == [
      {'id': 1, 'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__1'},
      {'id': 2, 'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__2'},
  ]


def test_add_tfds_id_as_supervised(
    dummy_builder: dataset_builder.DatasetBuilder,  # pylint: disable=redefined-outer-name
):
  """Tests `add_tfds_id=True` with `as_supervised=True`."""
  read_config = read_config_lib.ReadConfig(add_tfds_id=True)
  ds = dummy_builder.as_dataset(
      split='train', read_config=read_config, as_supervised=True,
  )
  # `add_tfds_id=True` is ignored when `as_supervised=True`
  assert ds.element_spec == (
      tf.TensorSpec(shape=(), dtype=tf.int64),
      tf.TensorSpec(shape=(), dtype=tf.int64),
  )
