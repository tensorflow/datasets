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

"""Tests for qa_utils."""

import os

from tensorflow_datasets import testing
from tensorflow_datasets.question_answering import qa_utils


class QAUtilsTest(testing.TestCase):

  def test_generate_squadlike_examples(self):
    filepath = os.path.join(testing.test_utils.fake_examples_dir(), 'xquad',
                            'translate-test.json')
    examples = qa_utils.generate_squadlike_examples(filepath)

    self.assertEqual(
        list(examples),
        [('1', {
            'id': '1',
            'title': 'Zurich_Switzerland',
            'context':
                'Zurich is the largest city in Switzerland with over 400000 '
                'inhabitants. In spite of this, it is not the capital of '
                'Switzerland, which is located in Bern aka Bernie.',
            'question': 'What is the capital of Switzerland?',
            'answers': {
                'answer_start': [1, 20, 29],
                'text': ['Zurich', 'Bern', 'Bernie']
            }
        }),
         ('2', {
             'id': '2',
             'title': 'Zurich_Switzerland',
             'context':
                 'Switzerland is the country in Euriope with 26 cantons. Zurich '
                 'canton has the largest population of 1.5 million.',
             'question': 'How many cantons does Switzerland have?',
             'answers': {
                 'answer_start': [8],
                 'text': ['26']
             }
         }),
         ('3', {
             'id': '3',
             'title': 'Paris_France',
             'context':
                 '  Paris is the largest city in France with over 2 million '
                 'inhabitants. It is the capital of France.',
             'question': 'What is the capital of France?',
             'answers': {
                 'answer_start': [3, 9],
                 'text': ['Paris', 'France']
             }
         })])


if __name__ == '__main__':
  testing.test_main()
