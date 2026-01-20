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

"""longt5 dataset.

Note that most of the code is based on the original datasets:
  * third_party/py/tensorflow_datasets/summarization/media_sum/media_sum.py
  * third_party/py/tensorflow_datasets/question_answering/natural_questions.py
"""
import functools
import json
import os
import re
from typing import Optional

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_BEAM_NAMESPACE = 'TFDS_LONGT5'

# TODO(long): Markdown description  that will appear on the catalog page.
_LONGT5_DESCRIPTION = """
Description is **formatted** as markdown.

It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""

_LONGT5_CITATION = """
@misc{longt5,
    title={LongT5: Efficient Text-To-Text Transformer for Long Sequences},
    year={2021},
}
"""

_DESCRIPTIONS = {
    'media_sum':
        """This large-scale media interview dataset contains 463.6K transcripts
        with abstractive summaries, collected from interview transcripts and
        overview / topic descriptions from NPR and CNN.""",
    'natural_questions':
        """The NQ corpus contains questions from real users, and it requires QA
        systems to read and comprehend an entire Wikipedia article that may or
        may not contain the answer to the question. The inclusion of real user
        questions, and the requirement that solutions should read an entire page
        to find the answer, cause NQ to be a more realistic and challenging task
        than prior QA datasets.""",
}

_CITATIONS = {
    'media_sum':
        """@article{zhu2021mediasum,
              title={MediaSum: A Large-scale Media Interview Dataset for Dialogue Summarization},
              author={Zhu, Chenguang and Liu, Yang and Mei, Jie and Zeng, Michael},
              journal={arXiv preprint arXiv:2103.06410},
              year={2021}
        }
    """,
    'natural_questions':
        """@article{47761,
          title = {Natural Questions: a Benchmark for Question Answering Research},
          author = {Tom Kwiatkowski and Jennimaria Palomaki and Olivia Redfield and Michael Collins and Ankur Parikh and Chris Alberti and Danielle Epstein and Illia Polosukhin and Matthew Kelcey and Jacob Devlin and Kenton Lee and Kristina N. Toutanova and Llion Jones and Ming-Wei Chang and Andrew Dai and Jakob Uszkoreit and Quoc Le and Slav Petrov},
          year = {2019},
          journal = {Transactions of the Association of Computational Linguistics}
        }
    """
}

_HOMEPAGES = {
    'media_sum':
        'https://github.com/zcgzcgzcg1/MediaSum',
    'natural_questions':
        'https://ai.google.com/research/NaturalQuestions/dataset',
}

_FEATURES = {
    'media_sum':
        tfds.features.FeaturesDict({
            'interview': tfds.features.Text(),
            'summary': tfds.features.Text(),
        }),
    'natural_questions':
        tfds.features.FeaturesDict({
            'id': tfds.features.Text(),
            'title': tfds.features.Text(),
            'context': tfds.features.Text(),
            'question': tfds.features.Text(),
            'answer': tfds.features.Text(),
            'all_answers': tfds.features.Sequence(tfds.features.Text()),
        }),
}


class Longt5Config(tfds.core.BuilderConfig):
  """BuilderConfig for Longt5."""

  def __init__(self,
               *,
               citation: Optional[str] = None,
               description: Optional[str] = None,
               homepage: Optional[str] = None,
               features: Optional[tfds.features.FeaturesDict] = None,
               **kwargs):
    """BuilderConfig for Longt5.

    Args:
      citation: `string`, citation for the data set.
      description: `string`, description for the data set.
      homepage: `string`, homepage for the data set.
      features: `dict[string, string]`, map from the name of the feature dict
        for each text field to the name of the column in the tsv file.
      **kwargs: keyword arguments forwarded to super.
    """
    super(Longt5Config, self).__init__(**kwargs)
    self.citation = citation
    self.description = description
    self.homepage = homepage
    self.features = features


class Longt5(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for longt5 dataset."""
  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  MANUAL_DOWNLOAD_INSTRUCTIONS = """
  One of the two configs in this dataset requires manual download instructions.

  For the media_sum dataset config, manual_dir should contain the files:

    * news_dialogue.json
    * train_val_test_split.json

  The files can be downloaded and extracted from the dataset's GitHub page:
  https://github.com/zcgzcgzcg1/MediaSum/tree/main/data
  """

  BUILDER_CONFIGS = [
      Longt5Config(
          name='media_sum',
          description=_DESCRIPTIONS['media_sum'],
          citation=_CITATIONS['media_sum'],
          homepage=_HOMEPAGES['media_sum'],
          features=_FEATURES['media_sum']),
      Longt5Config(
          name='natural_questions',
          description=_DESCRIPTIONS['natural_questions'],
          citation=_CITATIONS['natural_questions'],
          homepage=_HOMEPAGES['natural_questions'],
          features=_FEATURES['natural_questions'],
      )
  ]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_LONGT5_DESCRIPTION,
        features=self.builder_config.features,
        homepage='https://github.com/google/longt5',
        citation=_LONGT5_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    if self.builder_config.name == 'media_sum':
      archive = {
          'samples': dl_manager.manual_dir / 'news_dialogue.json',
          'splits_ids': dl_manager.manual_dir / 'train_val_test_split.json',
      }

      splits_ids = self._load_json_file(archive['splits_ids'])
      raw_samples = self._load_json_file(archive['samples'])

      return {
          'train':
              self._generate_examples(
                  split_ids=splits_ids['train'],
                  raw_samples=raw_samples,
                  filepaths=[]),
          'val':
              self._generate_examples(
                  split_ids=splits_ids['val'],
                  raw_samples=raw_samples,
                  filepaths=[]),
          'test':
              self._generate_examples(
                  split_ids=splits_ids['test'],
                  raw_samples=raw_samples,
                  filepaths=[]),
      }

    if self.builder_config.name == 'natural_questions':
      nq_url = 'https://storage.googleapis.com/natural_questions/v1.0'
      nq_download_urls = {
          'train': [
              '%s/train/nq-train-%02d.jsonl.gz' % (nq_url, i) for i in range(50)
          ],
          'validation': [
              '%s/dev/nq-dev-%02d.jsonl.gz' % (nq_url, i) for i in range(5)
          ]
      }
      files = dl_manager.download(nq_download_urls)
      return {
          'train':
              self._generate_examples(
                  filepaths=files['train'], split_ids=[], raw_samples=[]),
          'validation':
              self._generate_examples(
                  filepaths=files['validation'], split_ids=[], raw_samples=[]),
      }

  def _load_json_file(self, json_path):
    with tf.io.gfile.GFile(json_path) as f:
      file_content = json.load(f)
    return file_content

  def _generate_examples(self, split_ids, raw_samples, filepaths):
    """Yields examples for the media_sum data set."""
    beam = tfds.core.lazy_imports.apache_beam
    if self.builder_config.name == 'media_sum':

      def _process_example(sample):
        speakers = sample['speaker']
        utterances = sample['utt']
        interview = []
        for s, u in zip(speakers, utterances):
          interview.append(s + ': ' + u)
        example = {
            'interview': ' '.join(interview),
            'summary': sample['summary']
        }
        return sample['id'], example

      return (beam.Create(raw_samples)
              | 'Select raw samples with the correct split id' >>
              beam.Filter(lambda x: x['id'] in split_ids)
              | 'Process and yield examples' >> beam.Map(_process_example))

    if self.builder_config.name == 'natural_questions':
      counter = functools.partial(beam.metrics.Metrics.counter, _BEAM_NAMESPACE)

      def _parse_example(line):
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
                      _pad_punctuation(
                          json_dict['document_tokens'][pos]['token']))
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

        counter('nq_examples').inc()

        # Convert to str since some IDs cannot be represented by tf.int64.
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

      return (beam.Create([os.fspath(f) for f in filepaths])
              | beam.io.ReadAllFromText()
              | beam.Map(_parse_example))
