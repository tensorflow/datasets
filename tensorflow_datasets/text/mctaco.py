# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""The MC Taco dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@inproceedings{ZKNR19,
    author = {Ben Zhou, Daniel Khashabi, Qiang Ning and Dan Roth},
    title = {"Going on a vacation" takes longer than "Going for a walk": A Study of Temporal Commonsense Understanding },
    booktitle = {EMNLP},
    year = {2019},
}
"""

_DESCRIPTION = """\
MC-TACO is a dataset of 13k question-answer pairs that require temporal
commonsense comprehension. The dataset contains five temporal properties:

1. duration (how long an event takes)
2. temporal ordering (typical order of events)
3. typical time (when an event occurs)
4. frequency (how often an event occurs)
5. stationarity (whether a state is maintained for a very long time or indefinitely)

We hope that this dataset can promote the future exploration of this
 particular class of reasoning problems.
"""

_SPLIT_DOWNLOAD_URL = {
    'validation':
        'https://raw.githubusercontent.com/CogComp/MCTACO/master/dataset/dev_3783.tsv',
    'test':
        'https://raw.githubusercontent.com/CogComp/MCTACO/master/dataset/test_9442.tsv',
}


class Mctaco(tfds.core.GeneratorBasedBuilder):
  """The Mctaco dataset."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'sentence':
                tfds.features.Text(),
            'question':
                tfds.features.Text(),
            'answer':
                tfds.features.Text(),
            'label':
                tfds.features.ClassLabel(names=['no', 'yes']),
            'category':
                tfds.features.ClassLabel(names=[
                    'Event Ordering', 'Event Duration', 'Frequency',
                    'Stationarity', 'Typical Time'
                ])
        }),
        # No default supervised_keys (as we have to pass both the sentence,
        # question and possible answer as input.
        supervised_keys=None,
        homepage='https://github.com/CogComp/MCTACO',
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
    """This function returns the examples in the raw (text) form."""
    with tf.io.gfile.GFile(file_path) as f:
      reader = csv.DictReader(
          f,
          delimiter='\t',
          fieldnames=['sentence', 'question', 'answer', 'label', 'category'])
      for i, row in enumerate(reader):
        yield i, {
            'sentence': row['sentence'],
            'question': row['question'],
            'answer': row['answer'],
            'label': row['label'],
            'category': row['category'],
        }
