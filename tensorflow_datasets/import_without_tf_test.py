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

"""Test import."""

import sys
from unittest import mock

from absl import logging
import numpy as np
import tensorflow_datasets as tfds
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features
from tensorflow_datasets.core import file_adapters


class DummyDataset(dataset_builder.GeneratorBasedBuilder):
  """Test DatasetBuilder."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return dataset_info.DatasetInfo(
        builder=self,
        features=features.FeaturesDict({
            'integer': np.int32,
            'nested': features.FeaturesDict({'text': features.Text()}),
            'text': features.Text(),
        }),
    )

  def _split_generators(self, dl_manager):
    return {
        'train': self._generate_examples(),
        'test': self._generate_examples(),
    }

  def _generate_examples(self):
    for i in range(20):
      yield i, {
          'integer': i,
          'nested': {'text': 'nested_text'},
          'text': f'test_{i}',
      }


def test_import_tfds_without_loading_tf():
  with mock.patch.object(logging, 'log_first_n') as log_first_n:
    assert 'tensorflow' not in sys.modules

    data_dir = '/tmp/import_without_tf'
    builder = DummyDataset(data_dir=data_dir)
    builder.download_and_prepare(
        file_format=file_adapters.FileFormat.ARRAY_RECORD,
    )

    # No warning concerning TensorFlow DTypes was dispatched while loading
    assert not log_first_n.called
    assert 'tensorflow' not in sys.modules
