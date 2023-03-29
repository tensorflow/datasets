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

"""The Stanford Natural Language Inference (SNLI) Corpus."""

import csv
import os

from etils import epath
import tensorflow_datasets.public_api as tfds

_DATA_URL = 'https://nlp.stanford.edu/projects/snli/snli_1.0.zip'


class Builder(tfds.core.GeneratorBasedBuilder):
  """The Stanford Natural Language Inference (SNLI) Corpus."""

  VERSION = tfds.core.Version('1.1.0')

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'premise': tfds.features.Text(),
            'hypothesis': tfds.features.Text(),
            'label': tfds.features.ClassLabel(
                names=['entailment', 'neutral', 'contradiction']
            ),
        }),
        # No default supervised_keys (as we have to pass both premise
        # and hypothesis as input).
        supervised_keys=None,
        homepage='https://nlp.stanford.edu/projects/snli/',
    )

  def _split_generators(self, dl_manager):
    dl_dir = dl_manager.download_and_extract(_DATA_URL)
    data_dir = os.path.join(dl_dir, 'snli_1.0')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'filepath': os.path.join(data_dir, 'snli_1.0_test.txt')
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'filepath': os.path.join(data_dir, 'snli_1.0_dev.txt')},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'filepath': os.path.join(data_dir, 'snli_1.0_train.txt')
            },
        ),
    ]

  def _generate_examples(self, filepath):
    """This function returns the examples in the raw (text) form."""
    with epath.Path(filepath).open() as f:
      reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
      for idx, row in enumerate(reader):
        label = -1 if row['gold_label'] == '-' else row['gold_label']
        yield idx, {
            'premise': row['sentence1'],
            'hypothesis': row['sentence2'],
            'label': label,
        }
