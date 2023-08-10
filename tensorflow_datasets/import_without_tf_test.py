# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

import unittest


class ImportWithoutTfTest(unittest.TestCase):

  @mock.patch.object(logging, 'log_first_n')
  @mock.patch('builtins.print')
  def test_import_tfds_without_loading_tf(self, print_mock, log_first_n):
    # Check that conftest.py didn't already import TFDS:
    self.assertNotIn('tensorflow_datasets', sys.modules)

    import tensorflow_datasets as tfds  # pylint: disable=g-import-not-at-top

    class DummyDataset(tfds.core.dataset_builder.GeneratorBasedBuilder):
      """Test DatasetBuilder."""

      VERSION = tfds.core.Version('1.0.0')

      def _info(self):
        return tfds.core.dataset_info.DatasetInfo(
            builder=self,
            features=tfds.core.features.FeaturesDict({
                'integer': np.int32,
                'nested': tfds.core.features.FeaturesDict(
                    {'text': tfds.core.features.Text()}
                ),
                'text': tfds.core.features.Text(),
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

    self.assertNotIn('tensorflow', sys.modules)
    self.assertNotIn('array_record', sys.modules)
    self.assertNotIn('pandas', sys.modules)

    data_dir = '/tmp/import_without_tf'
    builder = DummyDataset(data_dir=data_dir)
    builder.download_and_prepare(
        file_format=tfds.core.file_adapters.FileFormat.ARRAY_RECORD,
    )
    data_source = builder.as_data_source()
    self.assertLen(data_source['train'], 20)
    self.assertEqual(
        data_source['train'][0],
        {
            'integer': 6,
            'nested': {'text': b'nested_text'},
            'text': b'test_6',
        },
    )

    # No warning concerning TensorFlow DTypes was dispatched while loading
    self.assertFalse(log_first_n.called)
    self.assertNotIn('tensorflow', sys.modules)
    self.assertIn('array_record', sys.modules)

    # No error concerning TensorFlow was dispatched:
    self.assertLen(print_mock.call_args_list, 2)
    first_call_args = print_mock.call_args_list[0][0][0]
    self.assertRegex(first_call_args, '.*Downloading and preparing dataset.*')
    second_call_args = print_mock.call_args_list[1][0][0]
    self.assertRegex(second_call_args, '.*Dataset .* downloaded and prepared.*')

    # The function `tfds.testing.mock_data` can be used without TF:
    with tfds.testing.mock_data():
      assert 'tensorflow' not in sys.modules


if __name__ == '__main__':
  unittest.main()
