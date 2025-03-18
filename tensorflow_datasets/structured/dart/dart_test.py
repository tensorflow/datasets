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

"""Dart dataset tests."""

import json
from unittest import mock

from etils import epath
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.dart import dart


class DartTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = dart.Dart
  SPLITS = {
      'train': 2,
      'validation': 1,
      'test': 2,
  }

  def test_split_generators(self):
    json_str = """
      [
        {
          "tripleset": [
            [
              "Mars Hill College",
              "JOINED",
              "1973"
            ],
            [
              "Mars Hill College",
              "LOCATION",
              "Mars Hill, North Carolina"
            ]
          ],
          "subtree_was_extended": true,
          "annotations": [
            {
              "source": "WikiSQL_decl_sents",
              "text": "A school from Mars Hill, North Carolina, joined in 1973."
            }
          ]
        }
      ]
    """
    expected_examples = [{
        'input_text': {
            'table': [
                {
                    'column_header': 'subject',
                    'row_number': 0,
                    'content': 'Mars Hill College',
                },
                {
                    'column_header': 'predicate',
                    'row_number': 0,
                    'content': 'JOINED',
                },
                {
                    'column_header': 'object',
                    'row_number': 0,
                    'content': '1973',
                },
                {
                    'column_header': 'subject',
                    'row_number': 1,
                    'content': 'Mars Hill College',
                },
                {
                    'column_header': 'predicate',
                    'row_number': 1,
                    'content': 'LOCATION',
                },
                {
                    'column_header': 'object',
                    'row_number': 1,
                    'content': 'Mars Hill, North Carolina',
                },
            ]
        },
        'target_text': (
            'A school from Mars Hill, North Carolina, joined in 1973.'
        ),
    }]
    dart_dataset = dart.Dart()
    with mock.patch.object(
        json, 'load', return_value=json.loads(json_str)
    ), mock.patch.object(epath, 'Path'):
      examples = list(dart_dataset._generate_examples(''))
      for i, (_, example) in enumerate(examples):
        self.assertCountEqual(example, expected_examples[i])
      assert len(examples) == len(expected_examples)


if __name__ == '__main__':
  tfds.testing.test_main()
