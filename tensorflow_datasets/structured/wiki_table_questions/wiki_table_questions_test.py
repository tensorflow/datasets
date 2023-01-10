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

"""wiki_table_questions dataset."""

import csv
from unittest import mock

from etils import epath
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.wiki_table_questions import wiki_table_questions


class WikiTableQuestionsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for wiki_table_questions dataset."""

  DATASET_CLASS = wiki_table_questions.WikiTableQuestions
  SPLITS = {
      'train': 2,
      'split-1-train': 1,
      'split-1-dev': 1,
      'split-2-train': 1,
      'split-2-dev': 1,
      'split-3-train': 1,
      'split-3-dev': 1,
      'test': 2,
  }

  OVERLAPPING_SPLITS = ['split-{}-train'.format(i) for i in range(1, 4)] + [
      'split-{}-dev'.format(i) for i in range(1, 4)
  ]

  def test_generate_examples(self):
    examples_file = [
        {
            'id': 'nu-0',
            'utterance': (
                'which country had the most cyclists finish within the top 5?'
            ),
            'context': 'csv/203-csv/733.csv',
            'targetValue': 'Italy',
        },
        {
            'id': 'nu-165',
            'utterance': 'who was the first cyclist to finish?',
            'context': 'csv/203-csv/733.csv',
            'targetValue': 'Alejandro Valverde',
        },
    ]
    csv_203_csv_733 = [
        {
            'Rank': '1',
            'Cyclist': 'Alejandro Valverde (ESP)',
            'Team': "Caisse d'Epargne",
            'Time': '5h 29\' 10"',
            'UCI ProTour\nPoints': '40',
        },
        {
            'Rank': '2',
            'Cyclist': 'Davide Rebellin (ITA)',
            'Team': 'Gerolsteiner',
            'Time': 's.t.',
            'UCI ProTour\nPoints': '25',
        },
        {
            'Rank': '3',
            'Cyclist': 'Paolo Bettini (ITA)',
            'Team': 'Quick Step',
            'Time': 's.t.',
            'UCI ProTour\nPoints': '20',
        },
    ]
    table_formated = [
        {
            'column_header': 'Rank',
            'row_number': 1,
            'content': '1',
        },
        {
            'column_header': 'Cyclist',
            'row_number': 1,
            'content': 'Alejandro Valverde (ESP)',
        },
        {
            'column_header': 'Team',
            'row_number': 1,
            'content': """Caisse d'Epargne""",
        },
        {
            'column_header': 'Time',
            'row_number': 1,
            'content': '''5h 29' 10"''',
        },
        {
            'column_header': 'UCI ProTour\nPoints',
            'row_number': 1,
            'content': '40',
        },
        {
            'column_header': 'Rank',
            'row_number': 2,
            'content': '2',
        },
        {
            'column_header': 'Cyclist',
            'row_number': 2,
            'content': 'Davide Rebellin (ITA)',
        },
        {
            'column_header': 'Team',
            'row_number': 2,
            'content': 'Gerolsteiner',
        },
        {
            'column_header': 'Time',
            'row_number': 2,
            'content': 's.t.',
        },
        {
            'column_header': 'UCI ProTour\nPoints',
            'row_number': 2,
            'content': '25',
        },
        {
            'column_header': 'Rank',
            'row_number': 3,
            'content': '3',
        },
        {
            'column_header': 'Cyclist',
            'row_number': 3,
            'content': 'Paolo Bettini (ITA)',
        },
        {
            'column_header': 'Team',
            'row_number': 3,
            'content': 'Quick Step',
        },
        {
            'column_header': 'Time',
            'row_number': 3,
            'content': 's.t.',
        },
        {
            'column_header': 'UCI ProTour\nPoints',
            'row_number': 3,
            'content': '20',
        },
    ]
    expected_examples = [
        {
            'input_text': {
                'table': table_formated,
                'context': (
                    'which country had the most cyclists finish within the'
                    ' top 5?'
                ),
            },
            'target_text': 'Italy',
        },
        {
            'input_text': {
                'table': table_formated,
                'context': 'who was the first cyclist to finish?',
            },
            'target_text': 'Alejandro Valverde',
        },
    ]
    with mock.patch.object(
        csv,
        'DictReader',
        side_effect=iter([examples_file, csv_203_csv_733, csv_203_csv_733]),
    ):
      mock_open = mock.MagicMock()
      with epath.testing.mock_epath(open=mock_open):
        dataset = wiki_table_questions.WikiTableQuestions()
        examples = list(dataset._generate_examples('', ''))
        for i, (_, example) in enumerate(examples):
          self.assertCountEqual(example, expected_examples[i])
        assert len(examples) == len(expected_examples)


if __name__ == '__main__':
  tfds.testing.test_main()
