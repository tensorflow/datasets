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

"""Natural Questions: A Benchmark for Question Answering Research."""
import html
import json
import os
import re
from typing import Optional

import numpy as np
import tensorflow_datasets.public_api as tfds

_BEAM_NAMESPACE = 'TFDS_LONGT5'

_URL = 'https://ai.google.com/research/NaturalQuestions/dataset'

_BASE_DOWNLOAD_URL = 'https://storage.googleapis.com/natural_questions/v1.0'
_DOWNLOAD_URLS = {
    'train': [
        '%s/train/nq-train-%02d.jsonl.gz' % (_BASE_DOWNLOAD_URL, i)
        for i in range(50)
    ],
    'validation': [
        '%s/dev/nq-dev-%02d.jsonl.gz' % (_BASE_DOWNLOAD_URL, i)
        for i in range(5)
    ],
}

_CITATIONS = {
    'longt5': """@misc{guo2021longt5,
        title={LongT5: Efficient Text-To-Text Transformer for Long Sequences},
        author={Mandy Guo and Joshua Ainslie and David Uthus and Santiago Ontanon and Jianmo Ni and Yun-Hsuan Sung and Yinfei Yang},
        year={2021},
        eprint={2112.07916},
        archivePrefix={arXiv},
        primaryClass={cs.CL}
        }
    """,
}


def _features():
  return {
      'default': tfds.features.FeaturesDict({
          'id': np.str_,
          'document': {
              'title': tfds.features.Text(),
              'url': tfds.features.Text(),
              'html': tfds.features.Text(),
              'tokens': tfds.features.Sequence({
                  'token': tfds.features.Text(),
                  'is_html': np.bool_,
              }),
          },
          'question': {
              'text': tfds.features.Text(),
              'tokens': tfds.features.Sequence(np.str_),
          },
          'annotations': tfds.features.Sequence({
              'id': np.str_,
              'long_answer': {
                  'start_token': np.int64,
                  'end_token': np.int64,
                  'start_byte': np.int64,
                  'end_byte': np.int64,
              },
              'short_answers': tfds.features.Sequence({
                  'start_token': np.int64,
                  'end_token': np.int64,
                  'start_byte': np.int64,
                  'end_byte': np.int64,
                  'text': tfds.features.Text(),
              }),
              'yes_no_answer': tfds.features.ClassLabel(
                  names=['NO', 'YES']
              ),  # Can also be -1 for NONE.
          }),
      }),
      'longt5': tfds.features.FeaturesDict({
          'id': tfds.features.Text(),
          'title': tfds.features.Text(),
          'context': tfds.features.Text(),
          'question': tfds.features.Text(),
          'answer': tfds.features.Text(),
          'all_answers': tfds.features.Sequence(tfds.features.Text()),
      }),
  }


class NaturalQuestionsConfig(tfds.core.BuilderConfig):
  """NaturalQuestions for Longt5."""

  def __init__(
      self,
      *,
      citation: Optional[str] = None,
      features: Optional[tfds.features.FeaturesDict] = None,
      **kwargs,
  ):
    """BuilderConfig for Longt5.

    Args:
      citation: `string`, citation for the config.
      features: `dict[string, string]`, map from the name of the feature dict
        for each text field to the name of the column in the tsv file.
      **kwargs: keyword arguments forwarded to super.
    """
    super(NaturalQuestionsConfig, self).__init__(**kwargs)
    self.citation = citation
    self.features = features


class Builder(tfds.core.BeamBasedBuilder):
  """Natural Questions: A Benchmark for Question Answering Research."""

  VERSION = tfds.core.Version('0.1.0')
  SUPPORTED_VERSIONS = [tfds.core.Version('0.0.2'), tfds.core.Version('0.1.0')]
  BUILDER_CONFIGS = [
      NaturalQuestionsConfig(
          name='default',
          description='Default natural_questions config',
          features=_features()['default'],
      ),
      NaturalQuestionsConfig(
          name='longt5',
          description=(
              'natural_questions preprocessed as in the longT5 benchmark'
          ),
          citation=_CITATIONS['longt5'],
          features=_features()['longt5'],
      ),
  ]
  DEFAULT_CONFIG_NAME = 'default'

  def _info(self):
    return self.dataset_info_from_configs(
        features=self.builder_config.features,
        supervised_keys=None,
        homepage=_URL,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    files = dl_manager.download(_DOWNLOAD_URLS)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={'filepaths': files['train']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'filepaths': files['validation']},
        ),
    ]

  @staticmethod
  def _parse_example_default(line):
    """Parse a single json line and emit an example dict."""

    def _parse_short_answer_default(html_bytes, short_ans):
      """Extract text of short answer."""
      ans_bytes = html_bytes[short_ans['start_byte'] : short_ans['end_byte']]
      # Remove non-breaking spaces.
      ans_bytes = ans_bytes.replace(b'\xc2\xa0', b' ')
      text = ans_bytes.decode('utf-8')
      # Remove HTML markup.
      text = re.sub('<([^>]*)>', '', html.unescape(text))
      # Replace \xa0 characters with spaces.
      return {
          'start_token': short_ans['start_token'],
          'end_token': short_ans['end_token'],
          'start_byte': short_ans['start_byte'],
          'end_byte': short_ans['end_byte'],
          'text': text,
      }

    def _parse_annotation_default(html_bytes, an_json):
      return {
          # Convert to str since some IDs cannot be represented by np.int64.
          'id': str(an_json['annotation_id']),
          'long_answer': {
              'start_token': an_json['long_answer']['start_token'],
              'end_token': an_json['long_answer']['end_token'],
              'start_byte': an_json['long_answer']['start_byte'],
              'end_byte': an_json['long_answer']['end_byte'],
          },
          'short_answers': [
              _parse_short_answer_default(html_bytes, ans)
              for ans in an_json['short_answers']
          ],
          'yes_no_answer': (
              -1
              if an_json['yes_no_answer'] == 'NONE'
              else an_json['yes_no_answer']
          ),
      }

    ex_json = json.loads(line)
    html_bytes = ex_json['document_html'].encode('utf-8')

    # Convert to str since some IDs cannot be represented by np.int64.
    id_ = str(ex_json['example_id'])
    return id_, {
        'id': id_,
        'document': {
            'title': ex_json['document_title'],
            'url': ex_json['document_url'],
            'html': html_bytes,
            'tokens': [
                {  # pylint: disable=g-complex-comprehension
                    'token': t['token'],
                    'is_html': t['html_token'],
                }
                for t in ex_json['document_tokens']
            ],
        },
        'question': {
            'text': ex_json['question_text'],
            'tokens': ex_json['question_tokens'],
        },
        'annotations': [
            _parse_annotation_default(html_bytes, an_json)
            for an_json in ex_json['annotations']
        ],
    }

  @staticmethod
  def _parse_example_longt5(line):
    """Parse a single json line and emit an example dict."""
    ex_json = json.loads(line)

    def _pad_punctuation(text):
      """Adds spaces around punctuation."""
      # Add space around punctuation.
      text = re.sub(r'(\W)', r' \1 ', text)
      # Collapse consecutive whitespace into one space.
      text = re.sub(r'\s+', ' ', text)
      return text

    def _get_context(json_dict):
      document_tokens = []
      for c in json_dict['long_answer_candidates']:
        if not bool(c['top_level']):
          continue
        for pos in range(c['start_token'], c['end_token']):
          t = json_dict['document_tokens'][pos]
          document_tokens.append(t['token'])
      context = ' '.join(document_tokens)
      # Substitute newlines and tabs with spaces.
      context = re.sub(r'\n\t', ' ', context)
      context = _pad_punctuation(context)
      return context

    def _has_short_answer(a):
      return bool(a['short_answers'])

    def _is_yes_no_answer(a):
      return a['yes_no_answer'] in ('YES', 'NO')

    def _get_all_answers(json_dict):
      all_answers = []
      for a in json_dict['annotations']:
        answer_tokens = []
        if _has_short_answer(a):
          for sa in a['short_answers']:
            for pos in range(sa['start_token'], sa['end_token']):
              answer_tokens.append(
                  _pad_punctuation(json_dict['document_tokens'][pos]['token'])
              )
            answer = ' '.join(answer_tokens)
            all_answers.append(answer)
        elif _is_yes_no_answer(a):
          all_answers.append(_pad_punctuation(a['yes_no_answer']))
        else:
          all_answers.append(_pad_punctuation('NULL'))
      return all_answers

    def _get_answer(all_answers):
      """Pick the first non NULL answer, if it exists."""
      for a in all_answers:
        if a != 'NULL':
          return a
      return 'NULL'

    # Convert to str since some IDs cannot be represented by np.int64.
    id_ = str(ex_json['example_id'])
    all_answers = _get_all_answers(ex_json)
    return id_, {
        'id': id_,
        'question': _pad_punctuation(ex_json['question_text'].strip()),
        'title': ex_json['document_title'].strip(),
        'context': _get_context(ex_json),
        'all_answers': all_answers,
        'answer': _get_answer(all_answers),
    }

  def _build_pcollection(self, pipeline, filepaths):
    """Build PCollection of examples."""
    beam = tfds.core.lazy_imports.apache_beam

    parse_example = {
        'default': self._parse_example_default,
        'longt5': self._parse_example_longt5,
    }[self.builder_config.name]

    return (
        pipeline
        | beam.Create([os.fspath(f) for f in filepaths])
        | beam.io.ReadAllFromText()
        | beam.Map(parse_example)
    )
