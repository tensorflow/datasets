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

"""wiki_table_text dataset."""

from etils import epath
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.wiki_table_text import wiki_table_text


class WikiTableTextTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for wiki_table_text dataset."""

  DATASET_CLASS = wiki_table_text.WikiTableText
  SPLITS = {
      'train': 4,
      'validation': 2,
      'test': 3,
  }

  DL_EXTRACT_RESULT = {
      'train_path': 'MSRA_NLC.Table2Text.train',
      'dev_path': 'MSRA_NLC.Table2Text.dev',
      'test_path': 'MSRA_NLC.Table2Text.test',
  }

  def test_generate_examples(self):
    expected_examples = [
        {
            'input_text': {
                'table': [
                    {
                        'column_header': 'subj_title_',
                        'row_number': 1,
                        'content': 'central bank of russia',
                    },
                    {
                        'column_header': 'subj_subtitle',
                        'row_number': 1,
                        'content': 'chairmen',
                    },
                    {
                        'column_header': 'name',
                        'row_number': 1,
                        'content': 'viktor gerashchenko',
                    },
                    {
                        'column_header': 'year',
                        'row_number': 1,
                        'content': '1992—1994',
                    },
                ]
            },
            'target_text': (
                'viktor gerashchenko is the chairman of central bank of russia '
                'during 1992 to 1994'
            ),
        },
        {
            'input_text': {
                'table': [
                    {
                        'column_header': 'subj_title_',
                        'row_number': 1,
                        'content': 'ace frehley',
                    },
                    {
                        'column_header': 'subj_subtitle',
                        'row_number': 1,
                        'content': 'discography',
                    },
                    {
                        'column_header': 'year',
                        'row_number': 1,
                        'content': '2006',
                    },
                    {
                        'column_header': 'title',
                        'row_number': 1,
                        'content': 'greatest hits live',
                    },
                ]
            },
            'target_text': (
                'greatest hits live is a discography of ace frehlely in 2006'
            ),
        },
    ]
    dataset = wiki_table_text.WikiTableText()

    def mock_open(*_):
      current_path = epath.Path(__file__).parent
      return open(current_path / 'test_data/examples.csv')

    with epath.testing.mock_epath(open=mock_open):
      examples = list(dataset._generate_examples(''))
      for i, (_, example) in enumerate(examples):
        self.assertCountEqual(example, expected_examples[i])
      assert len(examples) == len(expected_examples)


if __name__ == '__main__':
  tfds.testing.test_main()
