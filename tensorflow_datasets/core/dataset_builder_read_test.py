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

"""Tests for tensorflow_datasets.core.dataset_builder_read."""

from unittest import mock

import pytest

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import logging as tfds_logging
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import read_config as read_config_lib


def test_add_tfds_id(dummy_dataset: dataset_builder.DatasetBuilder):
  """Tests `add_tfds_id=True`."""
  read_config = read_config_lib.ReadConfig(add_tfds_id=True)
  ds = dummy_dataset.as_dataset(split='train', read_config=read_config)
  assert ds.element_spec == {
      'id': tf.TensorSpec(shape=(), dtype=tf.int64),
      'tfds_id': tf.TensorSpec(shape=(), dtype=tf.string),
  }
  assert list(dataset_utils.as_numpy(ds)) == [
      {
          'id': 0,
          'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__0'
      },
      {
          'id': 1,
          'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__1'
      },
      {
          'id': 2,
          'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__2'
      },
  ]

  # Subsplit API works too
  ds = dummy_dataset.as_dataset(split='train[1:]', read_config=read_config)
  assert ds.element_spec == {
      'id': tf.TensorSpec(shape=(), dtype=tf.int64),
      'tfds_id': tf.TensorSpec(shape=(), dtype=tf.string),
  }
  assert list(dataset_utils.as_numpy(ds)) == [
      {
          'id': 1,
          'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__1'
      },
      {
          'id': 2,
          'tfds_id': b'dummy_dataset-train.tfrecord-00000-of-00001__2'
      },
  ]


def test_add_tfds_id_as_supervised(
    dummy_dataset: dataset_builder.DatasetBuilder):
  """Tests `add_tfds_id=True` with `as_supervised=True`."""
  read_config = read_config_lib.ReadConfig(add_tfds_id=True)
  ds = dummy_dataset.as_dataset(
      split='train',
      read_config=read_config,
      as_supervised=True,
  )
  # `add_tfds_id=True` is ignored when `as_supervised=True`
  assert ds.element_spec == (
      tf.TensorSpec(shape=(), dtype=tf.int64),
      tf.TensorSpec(shape=(), dtype=tf.int64),
  )


def test_registered_logger_is_called(
    dummy_dataset: dataset_builder.DatasetBuilder):
  logger = mock.MagicMock()
  tfds_logging.register(logger)

  read_config = read_config_lib.ReadConfig(add_tfds_id=True)
  read_config.try_autocache = False
  read_config.num_parallel_calls_for_decode = 42
  ds = dummy_dataset.as_dataset(
      split='train',
      read_config=read_config,
      as_supervised=True,
  )
  # Logging doesn't change the result:
  assert ds.element_spec == (
      tf.TensorSpec(shape=(), dtype=tf.int64),
      tf.TensorSpec(shape=(), dtype=tf.int64),
  )
  # Logger was indeed called:
  assert logger.as_dataset.call_args_list == [
      mock.call(
          dataset_name='dummy_dataset',
          config_name='',
          version='1.0.0',
          data_path=mock.ANY,
          split='train',
          shuffle_files=False,
          as_supervised=True,
          batch_size=None,
          decoders=None,
          read_config=read_config,
      )
  ]


def test_cannonical_version_for_config():
  get_version = dataset_builder.cannonical_version_for_config

  # No config
  version = get_version(testing.DummyDataset)
  assert version == utils.Version('1.0.0')

  class DummyDatasetWithConfig(testing.DummyDataset, skip_registration=True):
    BUILDER_CONFIGS = [
        dataset_builder.BuilderConfig(name='x', version='2.0.0'),
        dataset_builder.BuilderConfig(name='y'),
    ]

  with pytest.raises(ValueError, match='Cannot infer version'):
    version = get_version(DummyDatasetWithConfig)

  version = get_version(
      DummyDatasetWithConfig,
      DummyDatasetWithConfig.builder_configs['x'],
  )
  assert version == utils.Version('2.0.0')

  version = get_version(
      DummyDatasetWithConfig,
      DummyDatasetWithConfig.builder_configs['y'],
  )
  assert version == utils.Version('1.0.0')
