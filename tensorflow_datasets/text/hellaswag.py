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

"""HellaSwag dataset."""

from __future__ import annotations

import json
import os

from etils import epath
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{zellers2019hellaswag,
    title={HellaSwag: Can a Machine Really Finish Your Sentence?},
    author={Zellers, Rowan and Holtzman, Ari and Bisk, Yonatan and Farhadi, Ali and Choi, Yejin},
    booktitle ={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
    year={2019}
}
"""

_DESCRIPTION = """
The HellaSwag dataset is a benchmark for Commonsense NLI. It includes a context
and some endings which complete the context.
"""

_HELLASWAG_URL = 'https://raw.githubusercontent.com/rowanz/hellaswag/master/data/'


class Hellaswag(tfds.core.GeneratorBasedBuilder):
  """HellaSwag Dataset."""

  VERSION = tfds.core.Version('1.1.0')
  RELEASE_NOTES = {
      '1.1.0': 'Another split dimension for source (wikihow vs activitynet)',
      '1.0.0': 'Adding separate splits for in-domain and out-of-domain '
               'validation/test sets.'
  }
  SUPPORTED_VERSIONS = [
      tfds.core.Version('1.1.0'),
      tfds.core.Version('1.0.0'),
      tfds.core.Version('0.0.1')
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'context': tfds.features.Text(),
            'endings': tfds.features.Sequence(tfds.features.Text()),
            'activity_label': tfds.features.Text(),
            'label': tf.int32,
            'split_type': tfds.features.Text(),
            'source_id': tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage='https://rowanzellers.com/hellaswag/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""

    files = dl_manager.download_and_extract({
        'train': os.path.join(_HELLASWAG_URL, 'hellaswag_train.jsonl'),
        'validation': os.path.join(_HELLASWAG_URL, 'hellaswag_val.jsonl'),
        'test': os.path.join(_HELLASWAG_URL, 'hellaswag_test.jsonl'),
    })

    return {
        'train':
            self._generate_examples(files['train']),
        'train_activitynet':
            self._generate_examples(files['train'], source='activitynet'),
        'train_wikihow':
            self._generate_examples(files['train'], source='wikihow'),
        'validation':
            self._generate_examples(files['validation']),
        'test':
            self._generate_examples(files['test']),
        'validation_ind_activitynet':
            self._generate_examples(files['validation'], 'IND', 'activitynet'),
        'validation_ood_activitynet':
            self._generate_examples(files['validation'], 'OOD', 'activitynet'),
        'test_ind_activitynet':
            self._generate_examples(files['test'], 'IND', 'activitynet'),
        'test_ood_activitynet':
            self._generate_examples(files['test'], 'OOD', 'activitynet'),
        'validation_ind_wikihow':
            self._generate_examples(files['validation'], 'IND', 'wikihow'),
        'validation_ood_wikihow':
            self._generate_examples(files['validation'], 'OOD', 'wikihow'),
        'test_ind_wikihow':
            self._generate_examples(files['test'], 'IND', 'wikihow'),
        'test_ood_wikihow':
            self._generate_examples(files['test'], 'OOD', 'wikihow')
    }

  def _generate_examples(self, filepath, domain=None, source=None):
    """Yields examples."""
    with epath.Path(filepath).open() as f:
      for idx, line in enumerate(f):
        elem = json.loads(line)
        elem_id = '%s_%d' % (os.path.basename(filepath), idx)

        if domain == 'IND' and elem['split_type'] != 'indomain':
          continue
        if domain == 'OOD' and elem['split_type'] != 'zeroshot':
          continue
        if source and not elem['source_id'].startswith(source):
          continue

        yield elem_id, {
            'context': elem['ctx'],
            'endings': elem['endings'],
            'activity_label': elem['activity_label'],
            'label': elem.get('label', -1),
            'split_type': elem['split_type'],
            'source_id': elem['source_id']
        }
