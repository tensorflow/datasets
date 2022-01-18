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

"""goemotions dataset."""

import csv

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{demszky-2020-goemotions,
    title = "{G}o{E}motions: A Dataset of Fine-Grained Emotions",
    author = "Demszky, Dorottya  and
      Movshovitz-Attias, Dana  and
      Ko, Jeongwoo  and
      Cowen, Alan  and
      Nemade, Gaurav  and
      Ravi, Sujith",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.372",
    pages = "4040--4054",
}
"""

_DESCRIPTION = """
The GoEmotions dataset contains 58k carefully curated Reddit comments labeled
for 27 emotion categories or Neutral. The emotion categories are admiration,
amusement, anger, annoyance, approval, caring, confusion, curiosity, desire,
disappointment, disapproval, disgust, embarrassment, excitement, fear,
gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief,
remorse, sadness, surprise.
"""

_URL_TRAIN = 'https://github.com/google-research/google-research/raw/master/goemotions/data/train.tsv'
_URL_DEV = 'https://github.com/google-research/google-research/raw/master/goemotions/data/dev.tsv'
_URL_TEST = 'https://github.com/google-research/google-research/raw/master/goemotions/data/test.tsv'

_TEXT_LABEL = 'comment_text'
_EMOTION_LABELS = [
    'admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring',
    'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval',
    'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief',
    'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief',
    'remorse', 'sadness', 'surprise', 'neutral'
]


class Goemotions(tfds.core.GeneratorBasedBuilder):
  """Dataset of Reddit comments with one or more emotion labels."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    """Returns information on the GoEmotions dataset."""
    features = {_TEXT_LABEL: tfds.features.Text()}

    for label in _EMOTION_LABELS:
      features[label] = tf.bool

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features),
        # Each emotion can be used for single-label classification.
        supervised_keys=None,
        homepage='https://github.com/google-research/google-research/tree/master/goemotions',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    # Download the data.
    dl_paths = dl_manager.download({
        'train': _URL_TRAIN,
        'test': _URL_TEST,
        'dev': _URL_DEV,
    })

    # Specify the splits.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'filename': dl_paths['train'],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'filename': dl_paths['dev'],
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'filename': dl_paths['test'],
            },
        ),
    ]

  def _parse_row_as_example(self, row):
    example = {}

    if len(row) != 3:
      return example

    example[_TEXT_LABEL] = row['comment_text']

    emotion_ids = row['emotion_ids'].split(',')
    for emotion_id in emotion_ids:
      emotion_id = int(emotion_id)
      example[_EMOTION_LABELS[emotion_id]] = True

    for i in range(len(_EMOTION_LABELS)):
      if _EMOTION_LABELS[i] not in example.keys():
        example[_EMOTION_LABELS[i]] = False

    return example

  def _generate_examples(self, filename):
    """Yields examples.

    Each example contains a text input with the relevant emotion labels.

    Args:
      filename: the path of the file to be read for this split.

    Yields:
      A dictionary of features, containing the comment text and, for each
      emotions label, 0/1 depending on whether is it a label for the input.
    """
    fieldnames = ['comment_text', 'emotion_ids', 'comment_id']
    with tf.io.gfile.GFile(filename) as f:
      reader = csv.DictReader(f, fieldnames=fieldnames, delimiter='\t')
      for row in reader:
        example = self._parse_row_as_example(row)
        if example:
          yield row['comment_id'], example
