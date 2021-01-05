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

"""WebQuestions Benchmark for Question Answering."""

import json
import re

import tensorflow as tf
import tensorflow_datasets.public_api as tfds


_CITATION = """
@inproceedings{berant-etal-2013-semantic,
    title = "Semantic Parsing on {F}reebase from Question-Answer Pairs",
    author = "Berant, Jonathan  and
      Chou, Andrew  and
      Frostig, Roy  and
      Liang, Percy",
    booktitle = "Proceedings of the 2013 Conference on Empirical Methods in Natural Language Processing",
    month = oct,
    year = "2013",
    address = "Seattle, Washington, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D13-1160",
    pages = "1533--1544",
}
"""
_SPLIT_DOWNLOAD_URL = {
    'train':
        'https://worksheets.codalab.org/rest/bundles/0x4a763f8cde224c2da592b75f29e2f5c2/contents/blob/',
    'test':
        'https://worksheets.codalab.org/rest/bundles/0xe7bac352fce7448c9ef238fb0a297ec2/contents/blob/',
}

_DESCRIPTION = """\
This dataset consists of 6,642 question/answer pairs.
The questions are supposed to be answerable by Freebase, a large knowledge graph.
The questions are mostly centered around a single named entity.
The questions are popular ones asked on the web (at least in 2013).
"""


class WebQuestions(tfds.core.GeneratorBasedBuilder):
  """WebQuestions Benchmark for Question Answering."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'url':
                tfds.features.Text(),
            'question':
                tfds.features.Text(),
            'answers':
                tfds.features.Sequence(tfds.features.Text()),
        }),
        supervised_keys=None,
        homepage='https://worksheets.codalab.org/worksheets/0xba659fe363cb46e7a505c5b6a774dc8a',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    file_paths = dl_manager.download(_SPLIT_DOWNLOAD_URL)

    return [
        tfds.core.SplitGenerator(
            name=split, gen_kwargs={'file_path': file_path})
        for split, file_path in file_paths.items()
    ]

  def _generate_examples(self, file_path):
    """Parses split file and yields examples."""

    def _target_to_answers(target):
      target = re.sub(r'^\(list |\)$', '', target)
      return [
          ''.join(ans) for ans in
          re.findall(r'\(description (?:"([^"]+?)"|([^)]+?))\)\w*', target)
      ]

    with tf.io.gfile.GFile(file_path) as f:
      examples = json.load(f)
      for i, ex in enumerate(examples):
        yield i, {
            'url': ex['url'],
            'question': ex['utterance'],
            'answers': _target_to_answers(ex['targetValue']),
        }
