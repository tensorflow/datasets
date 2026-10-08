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

# Lint as: python3
"""Points of Correspondence Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{lebanoff-etal-2020-understanding,
    title = "Understanding Points of Correspondence between Sentences for Abstractive Summarization",
    author = "Lebanoff, Logan and Muchovej, John and Dernoncourt, Franck and Kim, Doo Soon and Wang, \
    Lidan and Chang, Walter and Liu, Fei",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: \
    Student Research Workshop",
    month = jul,
    year = "2020",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-srw.26",
    pages = "191--198",
}
"""

_DESCRIPTION = """
The dataset contains 1,599 sentence fusion examples with fine-grained Points of Correspondence annotations.
A Point of Correspondence is an entity or event that connects two sentences together, 
which is represented as a span of text from each sentence.
Please take a look at our Github for a description of each feature in our dataset: 
https://github.com/ucfnlp/points-of-correspondence
"""

_URL = "https://github.com/ucfnlp/points-of-correspondence/raw/master/PoC_dataset.json"

_FULL_ARTICLE = "Full_Article"
_FULL_SUMMARY = "Full_Summary"
_SENTENCE_1 = "Sentence_1"
_SENTENCE_2 = "Sentence_2"
_SENTENCE_FUSED = "Sentence_Fused"
_SENTENCE_1_INDEX = "Sentence_1_Index"
_SENTENCE_2_INDEX = "Sentence_2_Index"
_SENTENCE_FUSED_INDEX = "Sentence_Fused_Index"
_POCS = "PoCs"
_EXAMPLE_ID = "Example_Id"

_SENTENCE_1_SELECTION = "Sentence_1_Selection"
_SENTENCE_2_SELECTION = "Sentence_2_Selection"
_SENTENCE_FUSED_SELECTION = "Sentence_Fused_Selection"
_POC_TYPE = "PoC_Type"

_POC_TYPE_CLASSES = [
    "Nominal", "Pronominal", "Common-Noun", "Repetition", "Event"
]


class PointsOfCorrespondence(tfds.core.GeneratorBasedBuilder):
  """Points of Correspondence Dataset."""

  VERSION = tfds.core.Version("3.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _FULL_ARTICLE: tfds.features.Text(),
            _FULL_SUMMARY: tfds.features.Text(),
            _SENTENCE_1: tfds.features.Text(),
            _SENTENCE_2: tfds.features.Text(),
            _SENTENCE_FUSED: tfds.features.Text(),
            _SENTENCE_1_INDEX: tf.int32,
            _SENTENCE_2_INDEX: tf.int32,
            _SENTENCE_FUSED_INDEX: tf.int32,
            _POCS: tfds.features.Sequence({
                _SENTENCE_1_SELECTION:
                    tfds.features.Tensor(shape=(2,), dtype=tf.int32),
                _SENTENCE_2_SELECTION:
                    tfds.features.Tensor(shape=(2,), dtype=tf.int32),
                _SENTENCE_FUSED_SELECTION:
                    tfds.features.Tensor(shape=(2,), dtype=tf.int32),
                _POC_TYPE: tfds.features.Text(),
            }),
        }),
        supervised_keys=(_FULL_ARTICLE, _FULL_SUMMARY),
        homepage="https://github.com/ucfnlp/points-of-correspondence",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_path = dl_manager.download(_URL)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "path":
                    os.path.join(dl_path),
                "key":
                    _EXAMPLE_ID
            },
        ),
    ]

  def _generate_examples(self, path=None, key=None):
    """Yields examples."""
    with tf.io.gfile.GFile(path + 'PoC_dataset.json') as f:
      data = json.load(f)
      for ex in data:
        yield ex[key], {k: v for k, v in ex.items() if k != _EXAMPLE_ID}
