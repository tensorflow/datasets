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

"""wiki_table_questions dataset."""

import textwrap
from unittest import mock

import tensorflow as tf
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

  OVERLAPPING_SPLITS = ['split-{}-train'.format(i) for i in range(1, 4)
                       ] + ['split-{}-dev'.format(i) for i in range(1, 4)]

  def test_generate_examples(self):
    examples_file = textwrap.dedent("""
      id	utterance	context	targetValue
      nu-0	which country had the most cyclists finish within the top 5?	csv/203-csv/733.csv	Italy
      nu-165	who was the first cyclist to finish?	csv/203-csv/733.csv	Alejandro Valverde
    """)
    csv_203_csv_733 = textwrap.dedent("""
      "Rank","Cyclist","Team","Time","UCI ProTour\nPoints"
      "1","Alejandro Valverde (ESP)","Caisse d'Epargne","5h 29' 10\"","40"
      "2","Davide Rebellin (ITA)","Gerolsteiner","s.t.","25"
      "3","Paolo Bettini (ITA)","Quick Step","s.t.","20"
    """)
    table_formated = [{
        'column_header': 'Rank',
        'row_number': 1,
        'content': '1',
    }, {
        'column_header': 'Cyclist',
        'row_number': 1,
        'content': 'Alejandro Valverde (ESP)',
    }, {
        'column_header': 'Team',
        'row_number': 1,
        'content': """Caisse d'Epargne""",
    }, {
        'column_header': 'Time',
        'row_number': 1,
        'content': '''5h 29' 10"''',
    }, {
        'column_header': 'UCI ProTour\nPoints',
        'row_number': 1,
        'content': '40',
    }, {
        'column_header': 'Rank',
        'row_number': 2,
        'content': '2',
    }, {
        'column_header': 'Cyclist',
        'row_number': 2,
        'content': 'Davide Rebellin (ITA)',
    }, {
        'column_header': 'Team',
        'row_number': 2,
        'content': 'Gerolsteiner',
    }, {
        'column_header': 'Time',
        'row_number': 2,
        'content': 's.t.',
    }, {
        'column_header': 'UCI ProTour\nPoints',
        'row_number': 2,
        'content': '25',
    }, {
        'column_header': 'Rank',
        'row_number': 3,
        'content': '3',
    }, {
        'column_header': 'Cyclist',
        'row_number': 3,
        'content': 'Paolo Bettini (ITA)',
    }, {
        'column_header': 'Team',
        'row_number': 3,
        'content': 'Quick Step',
    }, {
        'column_header': 'Time',
        'row_number': 3,
        'content': 's.t.',
    }, {
        'column_header': 'UCI ProTour\nPoints',
        'row_number': 3,
        'content': '20',
    }]
    expected_examples = [{
        'input_text': {
            'table':
                table_formated,
            'context':
                'which country had the most cyclists finish within the top 5?'
        },
        'target_text': 'Italy'
    }, {
        'input_text': {
            'table': table_formated,
            'context': 'who was the first cyclist to finish?'
        },
        'target_text': 'Alejandro Valverde'
    }]
    tf_mock = mock.Mock()
    tf_mock.gfile.GFile.side_effect = lambda f: csv_203_csv_733 if f else examples_file
    dataset = wiki_table_questions.WikiTableQuestions()
    with mock.patch.object(tf, 'io', return_value=tf_mock):
      for i, (_, example) in enumerate(dataset._generate_examples('', '')):
        self.assertCountEqual(example, expected_examples[i])


if __name__ == '__main__':
  tfds.testing.test_main()
