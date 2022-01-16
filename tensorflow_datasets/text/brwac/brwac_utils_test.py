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

"""Utilities for the brwac dataset."""

from tensorflow_datasets.text.brwac.brwac_utils import (extract_ids,
                                                        parse_single_doc)

mock_header = \
  '<doc docid="example_docid" title="Example title" uri="example_uri.com">'

mock_doc_str = """\
<doc docid="example_docid" title="Example title" uri="example_uri.com">
<p>
<s>
This
paragraph
contains
one
single
sentence
</s>
</p>
<p>
<s>
This
paragraph
also
"
<g/>
contains
<g/>
"
a
single
sentence
</s>
</p>
<p>
<s>
Another
paragraph
with
one
sentence
,
but
also
with
a
dot
mark
<g/>
.
</s>
</p>
<p>
<s>
Another
single
sentence
paragraph
</s>
</p>
<p>
<s>
This
is
the
last
paragraph
containing
one
sentence
</s>
</p>
<p>
<s>
Sentence
1
from
last
paragraph
<g/>
.
</s>
<s>
Sentence
2
<g/>
.
</s>
<s>
Sentence
3
start
<g/>
,
middle
<g/>
,
end
<g/>
.
</s>
<s>
Sentence
4
<g/>
,
after
comma
before
dot
<g/>
.
</s>
<s>
Sentence
5
before
comma
<g/>
,
sentence
5
after
comma
<g/>
.
</s>
<s>
Sentence
6
<g/>
,
sentence
6
<g/>
,
sentence
6
finish
and
doc
end
<g/>
.
</s>
</p>
</doc>
"""


def test_extract_ids():
  expected_result = {
      'doc_id': 'example_docid',
      'title': 'Example title',
      'uri': 'example_uri.com'
  }
  assert extract_ids(mock_doc_str) == expected_result


def test_parse_single_doc():
  expected_result = {
      'doc_id': 'example_docid',
      'title': 'Example title',
      'uri': 'example_uri.com',
      'text':{
        'paragraphs': [
          ['This paragraph contains one single sentence'],
          ['This paragraph also "contains" a single sentence'],
          ['Another paragraph with one sentence , but also with a dot mark.'],
          ['Another single sentence paragraph'],
          ['This is the last paragraph containing one sentence'],
          [
            'Sentence 1 from last paragraph.', 'Sentence 2.',
            'Sentence 3 start, middle, end.',
            'Sentence 4, after comma before dot.',
            'Sentence 5 before comma, sentence 5 after comma.',
            'Sentence 6, sentence 6, sentence 6 finish and doc end.'
          ]
        ]
      }
  }
  candidate_result = parse_single_doc(mock_doc_str)
  # id data match
  for k in ['doc_id', 'title', 'uri']:
    assert candidate_result[k] == expected_result[k]

  true_paragraphs = expected_result['text']['paragraphs']
  pred_paragraphs = candidate_result['text']['paragraphs']

  # number of paragraphs match
  assert len(true_paragraphs) == len(pred_paragraphs)

  # number of sentences in each paragraph match
  for t, p in zip(true_paragraphs, pred_paragraphs):
    assert len(t) == len(p)

    # content of paragraphs match
  for t, p in zip(true_paragraphs, pred_paragraphs):
    assert t == p
