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

"""dart dataset."""

from __future__ import annotations

import json
import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{radev2020dart,
  title={DART: Open-Domain Structured Data Record to Text Generation},
  author={Dragomir Radev and Rui Zhang and Amrit Rau and Abhinand Sivaprasad and Chiachun Hsieh and Nazneen Fatema Rajani and Xiangru Tang and Aadit Vyas and Neha Verma and Pranav Krishna and Yangxiaokang Liu and Nadia Irwanto and Jessica Pan and Faiaz Rahman and Ahmad Zaidi and Murori Mutuma and Yasin Tarabar and Ankit Gupta and Tao Yu and Yi Chern Tan and Xi Victoria Lin and Caiming Xiong and Richard Socher},
  journal={arXiv preprint arXiv:2007.02871},
  year={2020}
"""

_DESCRIPTION = """
DART (DAta Record to Text generation) contains RDF entity-relation annotated
with sentence descriptions that cover all facts in the triple set. DART was
constructed using existing datasets such as: WikiTableQuestions, WikiSQL, WebNLG
and Cleaned E2E. The tables from WikiTableQuestions and WikiSQL were transformed
to subject-predicate-object triples, and its text annotations were mainly
collected from MTurk. The meaningful representations in E2E were also
transformed to triples and its descriptions were used, some that couldn't be
transformed were dropped.

The dataset splits of E2E and WebNLG are kept, and for the WikiTableQuestions
and WikiSQL the Jaccard similarity is used to keep similar tables in the same
set (train/dev/tes).

This dataset is constructed following a standarized table format.
"""

_URL = 'https://github.com/Yale-LILY/dart/archive/master.zip'


class Dart(tfds.core.GeneratorBasedBuilder):
  """DAta Record to Text Generation."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'input_text': {
                'table': tfds.features.Sequence({  # Each row will be one triple fact.
                    # we'll only have subject/predicate/object headers
                    'column_header': np.str_,
                    'row_number': np.int16,
                    'content': np.str_,
                }),
            },
            'target_text': np.str_,
        }),
        supervised_keys=('input_text', 'target_text'),
        # Homepage of the dataset for documentation
        homepage='https://github.com/Yale-LILY/dart',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extracted_path = os.path.join(
        dl_manager.download_and_extract(_URL), 'dart-master', 'data', 'v1.1.1'
    )
    return {
        tfds.Split.TRAIN: self._generate_examples(
            json_file=os.path.join(
                extracted_path, 'dart-v1.1.1-full-train.json'
            )
        ),
        tfds.Split.VALIDATION: self._generate_examples(
            json_file=os.path.join(extracted_path, 'dart-v1.1.1-full-dev.json')
        ),
        tfds.Split.TEST: self._generate_examples(
            json_file=os.path.join(extracted_path, 'dart-v1.1.1-full-test.json')
        ),
    }

  def _generate_examples(self, json_file):
    """Yields examples."""
    with epath.Path(json_file).open() as f:
      data = json.load(f)
      for entry_count, entry in enumerate(data):
        table = []
        for i, triple_set in enumerate(entry['tripleset']):
          for header, content in zip(
              ['subject', 'predicate', 'object'], triple_set
          ):
            table.append({
                'column_header': header,
                'row_number': i,
                'content': content,
            })
        for annotation_count, annotation in enumerate(entry['annotations']):
          yield '{}_{}'.format(entry_count, annotation_count), {
              'input_text': {
                  'table': table,
              },
              'target_text': annotation['text'],
          }
