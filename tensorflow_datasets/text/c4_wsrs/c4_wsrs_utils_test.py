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

"""Tests for c4_wsrs_utils."""
import re
from unittest import mock
from absl.testing import absltest
import numpy as np
from tensorflow_datasets.text.c4_wsrs import c4_wsrs_utils


class C4WsrsUtilsTest(absltest.TestCase):

  def test_create_word_finder_regex(self):
    words = ['pt', 'ct', 's']
    word_finder_re = c4_wsrs_utils.create_word_finder_regex(words)
    string = "the (pt's) #ct to feel drowsy."
    self.assertEqual(word_finder_re.findall(string), ['pt', 'ct'])

  def test_get_abbreviation_expansion_pairs(self):
    snippet = 'the patient is in the emergency room.'
    abbreviations_by_expansion = {'patient': ['pt'], 'emergency room': ['er']}
    expansion_re = re.compile('(patient|emergency room)')
    result = c4_wsrs_utils._get_abbreviation_expansion_pairs(
        snippet, abbreviations_by_expansion, expansion_re
    )
    self.assertEqual(
        result, {4: ('pt', 'patient'), 22: ('er', 'emergency room')}
    )

  def test_extract_snippets(self):
    doc = {
        'url': b'test/url.com',
        'text': b'the patient is in the emergency room. the doctor just left.',
    }
    abbreviations_by_expansion = {
        'patient': ['pt'],
        'emergency room': ['er'],
        'doctor': ['dr'],
    }
    expansion_re = re.compile('(patient|emergency room|doctor)')
    with mock.patch.object(
        np.random, 'uniform', autospec=True
    ) as random_uniform_mock:
      random_uniform_mock.return_value = 0.1
      results = list(
          c4_wsrs_utils.extract_snippets(
              doc,
              max_sentences_per_snippet=1,
              abbreviations_by_expansion=abbreviations_by_expansion,
              expansion_regex=expansion_re,
              max_snippet_char_len=1024,
              alpha_keep_no_rs=0.0,
              alpha_keep_rs=0.0,
          )
      )
    self.assertEqual(
        results,
        [
            (
                'url=test/url.com,snippet_id=0',
                (
                    'the patient is in the emergency room.',
                    ('pt', 'patient'),
                    {4: ('pt', 'patient'), 22: ('er', 'emergency room')},
                ),
            ),
            (
                'url=test/url.com,snippet_id=1',
                (
                    'the doctor just left.',
                    ('dr', 'doctor'),
                    {4: ('dr', 'doctor')},
                ),
            ),
        ],
    )

  def test_reverse_substitute_snippet(self):
    snippet = 'the patient is in the emergency room.'
    index_to_pair = {4: ('pt', 'patient'), 22: ('er', 'emergency room')}
    result = c4_wsrs_utils._reverse_substitute_snippet(
        snippet, index_to_pair, substitution_rate=1.0
    )
    self.assertEqual(result, 'the pt is in the er.')

  def test_reverse_substitution(self):
    element = (
        'url=test/url.com,snippet_id=0',
        (
            'the patient is in the emergency room.',
            ('pt', 'patient'),
            {4: ('pt', 'patient'), 22: ('er', 'emergency room')},
        ),
    )
    rs_results = list(
        c4_wsrs_utils.reverse_substitution(
            element, substitution_rate=1.0, min_snippet_token_len=3
        )
    )
    expected_features = c4_wsrs_utils.WSRSFeatures(
        original_snippet='the patient is in the emergency room.',
        abbreviated_snippet='the pt is in the er.',
    )
    self.assertSameElements(
        rs_results,
        [(
            ('pt', 'patient'),
            ('url=test/url.com,snippet_id=0', expected_features),
        )],
    )


if __name__ == '__main__':
  absltest.main()
