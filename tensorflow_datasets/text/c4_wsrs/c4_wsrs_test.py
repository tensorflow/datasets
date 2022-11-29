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

"""Configures tests for C4-WSRS dataset."""
import contextlib
from unittest import mock

import tensorflow as tf
from tensorflow_datasets import testing
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.c4_wsrs import c4_wsrs


class C4WSRSTest(testing.DatasetBuilderTestCase):
  """Tests for c4_wsrs dataset."""

  DATASET_CLASS = c4_wsrs.C4WSRS
  SPLITS = {
      'train': 2,  # Number of fake train example
      'validation': 2,  # Number of fake test example
  }

  OVERLAPPING_SPLITS = ['train', 'validation']
  SKIP_CHECKSUMS = True
  DL_DOWNLOAD_RESULT = 'abbreviation_expansion_dictionary.csv'
  SKIP_TF1_GRAPH_MODE = True

  @classmethod
  def setUpClass(cls):
    super().setUpClass()
    beam = tfds.core.lazy_imports.apache_beam
    inputs = [
        tf.nest.map_structure(
            tf.convert_to_tensor, {
                'content-length': 'abc',
                'content-type': 'text/plain',
                'text': ('patient in the emergency room with complications. '
                         'will check in morning.'),
                'timestamp': 'this is a timestamp',
                'url': 'http://google.com/1'
            }),
        tf.nest.map_structure(
            tf.convert_to_tensor, {
                'content-length': 'abc',
                'content-type': 'text/plain',
                'text': ('magnetic resonance imaging test in patient with '
                         'lower back pain. send for treatment.'),
                'timestamp': 'this is a timestamp',
                'url': 'http://google.com/2'
            })
    ]

    cls._exit_stack = contextlib.ExitStack().__enter__()
    cls._exit_stack.enter_context(
        mock.patch.object(tfds, 'builder', autospec=True))
    cls._exit_stack.enter_context(
        mock.patch.object(
            tfds.beam,
            'ReadFromTFDS',
            return_value=beam.Create(inputs),
        ))

  @classmethod
  def tearDownClass(cls):
    cls._exit_stack.__exit__(None, None, None)
    super().tearDownClass()


if __name__ == '__main__':
  tfds.testing.test_main()
