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

"""Czech Restaurants dataset."""

from __future__ import annotations

import json

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_CITATION = r"""

@inproceedings{dusek_neural_2019,
        author = {Dušek, Ondřej and Jurčíček, Filip},
        title = {Neural {Generation} for {Czech}: {Data} and {Baselines}},
        shorttitle = {Neural {Generation} for {Czech}},
        url = {https://www.aclweb.org/anthology/W19-8670/},
        urldate = {2019-10-18},
        booktitle = {Proceedings of the 12th {International} {Conference} on {Natural} {Language} {Generation} ({INLG} 2019)},
        month = oct,
        address = {Tokyo, Japan},
        year = {2019},
        pages = {563--574},
        abstract = {We present the first dataset targeted at end-to-end NLG in Czech in the restaurant domain, along with several strong baseline models using the sequence-to-sequence approach. While non-English NLG is under-explored in general, Czech, as a morphologically rich language, makes the task even harder: Since Czech requires inflecting named entities, delexicalization or copy mechanisms do not work out-of-the-box and lexicalizing the generated outputs is non-trivial. In our experiments, we present two different approaches to this this problem: (1) using a neural language model to select the correct inflected form while lexicalizing, (2) a two-step generation setup: our sequence-to-sequence model generates an interleaved sequence of lemmas and morphological tags, which are then inflected by a morphological generator.},
}
"""

_DESCRIPTION = """
Czech data-to-text dataset in the restaurant domain. The input meaning representations
contain a dialogue act type (inform, confirm etc.), slots (food, area, etc.) and their values.
It originated as a translation of the English San Francisco Restaurants dataset by Wen et al. (2015).
"""

_HOMEPAGE_URL = 'https://github.com/UFAL-DSG/cs_restaurant_dataset'

_TRAIN_URL = (
    'https://github.com/UFAL-DSG/cs_restaurant_dataset/raw/master/train.json'
)
_DEV_URL = (
    'https://github.com/UFAL-DSG/cs_restaurant_dataset/raw/master/devel.json'
)
_TEST_URL = (
    'https://github.com/UFAL-DSG/cs_restaurant_dataset/raw/master/test.json'
)


def _get_table_from_da(da):
  """Converts a dialogue act from the cs_restaurant dataset into a table row."""
  # DA format example: intent(slot1='first value',slot2=val2)
  intent, slots = da.split('(', 1)  # split intent and slots
  slots = slots[:-1]  # remove closing ')'
  # Start with intent (always present)
  da_as_table = [{
      'column_header': 'intent',
      'row_number': 1,
      'content': intent,
  }]
  # Add slots (requested values have the value “?”)
  for slot_val in slots.split(','):
    if '=' in slot_val:
      slot, value = slot_val.split('=', 1)
    else:
      slot = slot_val
      value = '?'
    if value.startswith("'"):
      value = value[1:-1]
    da_as_table.append({
        'column_header': slot,
        'row_number': 1,
        'content': value,
    })
  return da_as_table


class CSRestaurants(tfds.core.GeneratorBasedBuilder):
  """MR in the restaurant domain and target utterances describing it."""

  VERSION = tfds.core.Version('1.0.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            'input_text': {
                'table': tfds.features.Sequence({
                    'column_header': np.str_,
                    'row_number': np.int16,
                    'content': np.str_,
                })
            },
            'delex_input_text': {
                'table': tfds.features.Sequence({
                    'column_header': np.str_,
                    'row_number': np.int16,
                    'content': np.str_,
                })
            },
            'target_text': np.str_,
            'delex_target_text': np.str_,
        }),
        # If there's a common (input, target) tuple from the features,
        # specify them here. They'll be used if as_supervised=True in
        # builder.as_dataset.
        supervised_keys=('input_text', 'target_text'),
        # Homepage of the dataset for documentation
        homepage=_HOMEPAGE_URL,
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    extracted_path = dl_manager.download_and_extract(
        {'train_path': _TRAIN_URL, 'dev_path': _DEV_URL, 'test_path': _TEST_URL}
    )

    return {
        'train': self._generate_examples(
            json_path=extracted_path['train_path']
        ),
        'validation': self._generate_examples(
            json_path=extracted_path['dev_path']
        ),
        'test': self._generate_examples(json_path=extracted_path['test_path']),
    }

  def _generate_examples(self, json_path):
    """Yields examples."""
    with epath.Path(json_path).open() as f:
      data = json.load(f)
      for i, row in enumerate(data):
        yield i, {
            'input_text': {
                'table': _get_table_from_da(row['da']),
            },
            'delex_input_text': {
                'table': _get_table_from_da(row['delex_da']),
            },
            'target_text': row['text'],
            'delex_target_text': row['delex_text'],
        }
