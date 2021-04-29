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

"""web_nlg dataset."""

from unittest import mock
import xml.etree.ElementTree as etree

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.web_nlg import web_nlg


class WebNlgTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = web_nlg.WebNlg
  SPLITS = {
      'train': 12,
      'validation': 4,
      'test_all': 5,
      'test_unseen': 2,
  }

  @mock.patch.object(etree, 'parse', autospec=True)
  def test_generate_examples(self, parse_mock):
    xml_str = """
    <benchmark>
      <entries>
        <entry category="Building" eid="Id1" size="2">
          <originaltripleset>
            <otriple>103_Colmore_Row | architect | John_Madin</otriple>
            <otriple>103_Colmore_Row | location | "Colmore Row, Birmingham, England"@en</otriple>
          </originaltripleset>
          <modifiedtripleset>
            <mtriple>103_Colmore_Row | architect | John_Madin</mtriple>
            <mtriple>103_Colmore_Row | location | "Colmore Row, Birmingham, England"</mtriple>
          </modifiedtripleset>
          <lex comment="good" lid="Id1">Architect John Madin, designed 103 Colmore Row, located on Colmore Row, in Birmingham, England.</lex>
          <lex comment="good" lid="Id2">John Madin designed 103 Colmore Row, Birmingham, England.</lex>
        </entry>
        <entry category="Building" eid="Id2" size="2">
          <originaltripleset>
            <otriple>103_Colmore_Row | architect | John_Madin</otriple>
            <otriple>103_Colmore_Row | location | Colmore_Row</otriple>
          </originaltripleset>
          <modifiedtripleset>
            <mtriple>103_Colmore_Row | architect | John_Madin</mtriple>
            <mtriple>103_Colmore_Row | location | Colmore_Row</mtriple>
          </modifiedtripleset>
          <lex comment="good" lid="Id1">103 Colmore Row, located at Colmore Row, was designed by the architect, John Madin.</lex>
        </entry>
      </entries>
    </benchmark>
    """
    expected_examples = [{
        'input_text': {
            'table': [
                {
                    'column_header': 'subject',
                    'row_number': 0,
                    'content': '103_Colmore_Row',
                },
                {
                    'column_header': 'predicate',
                    'row_number': 0,
                    'content': 'architect',
                },
                {
                    'column_header': 'object',
                    'row_number': 0,
                    'content': 'John_Madin',
                },
                {
                    'column_header': 'subject',
                    'row_number': 1,
                    'content': '103_Colmore_Row',
                },
                {
                    'column_header': 'predicate',
                    'row_number': 1,
                    'content': 'location',
                },
                {
                    'column_header': 'object',
                    'row_number': 1,
                    'content': '"Colmore Row, Birmingham, England"',
                },
            ],
            'context': 'Building'
        },
        'target_text':
            'Architect John Madin, designed 103 Colmore Row, located on '
            'Colmore Row, in Birmingham, England.'
    }, {
        'input_text': {
            'table': [
                {
                    'column_header': 'subject',
                    'row_number': 0,
                    'content': '103_Colmore_Row',
                },
                {
                    'column_header': 'predicate',
                    'row_number': 0,
                    'content': 'architect',
                },
                {
                    'column_header': 'object',
                    'row_number': 0,
                    'content': 'John_Madin',
                },
                {
                    'column_header': 'subject',
                    'row_number': 1,
                    'content': '103_Colmore_Row',
                },
                {
                    'column_header': 'predicate',
                    'row_number': 1,
                    'content': 'location',
                },
                {
                    'column_header': 'object',
                    'row_number': 1,
                    'content': '"Colmore Row, Birmingham, England"',
                },
            ],
            'context': 'Building'
        },
        'target_text':
            'John Madin designed 103 Colmore Row, Birmingham, England.'
    }, {
        'input_text': {
            'table': [
                {
                    'column_header': 'subject',
                    'row_number': 0,
                    'content': '103_Colmore_Row',
                },
                {
                    'column_header': 'predicate',
                    'row_number': 0,
                    'content': 'architect',
                },
                {
                    'column_header': 'object',
                    'row_number': 0,
                    'content': 'John_Madin',
                },
                {
                    'column_header': 'subject',
                    'row_number': 1,
                    'content': '103_Colmore_Row',
                },
                {
                    'column_header': 'predicate',
                    'row_number': 1,
                    'content': 'location',
                },
                {
                    'column_header': 'object',
                    'row_number': 1,
                    'content': 'Colmore_Row',
                },
            ],
            'context': 'Building'
        },
        'target_text':
            '103 Colmore Row, located at Colmore Row, was designed by the '
            'architect, John Madin.'
    }]
    return_mock = mock.Mock()
    parse_mock.return_value = return_mock
    return_mock.getroot.return_value = etree.fromstring(xml_str)
    dataset = web_nlg.WebNlg()
    with mock.patch.object(tf, 'io'):
      for i, (_,
              example) in enumerate(dataset._generate_examples([''], 'train')):
        self.assertCountEqual(example, expected_examples[i])


if __name__ == '__main__':
  tfds.testing.test_main()
