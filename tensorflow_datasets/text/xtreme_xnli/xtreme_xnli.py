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

"""Machine Translations of XNLI: The Cross-Lingual NLI Corpus."""

import collections
import csv

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@article{hu2020xtreme,
      author    = {Junjie Hu and Sebastian Ruder and Aditya Siddhant and Graham Neubig and Orhan Firat and Melvin Johnson},
      title     = {XTREME: A Massively Multilingual Multi-task Benchmark for Evaluating Cross-lingual Generalization},
      journal   = {CoRR},
      volume    = {abs/2003.11080},
      year      = {2020},
      archivePrefix = {arXiv},
      eprint    = {2003.11080}
}"""

_DESCRIPTION = """\
This dataset contains machine translations of MNLI into each of the XNLI
languages. The translation data is provided by XTREME. Note that this is
different from the machine translated data provided by the original XNLI paper.
"""

_XTREME_TRANSLATIONS_FORMAT = 'https://storage.googleapis.com/xtreme_translations/XNLI/translate-train/en-{0}-translated.tsv'

_LANGUAGES = (
    'ar',
    'bg',
    'de',
    'el',
    'en',
    'es',
    'fr',
    'hi',
    'ru',
    'sw',
    'th',
    'tr',
    'ur',
    'vi',
    'zh',
)


class XtremeXnli(tfds.core.GeneratorBasedBuilder):
  """Machine translations of the MNLI dataset."""

  VERSION = tfds.core.Version('1.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'premise': tfds.features.Translation(
                languages=_LANGUAGES,
            ),
            'hypothesis': tfds.features.TranslationVariableLanguages(
                languages=_LANGUAGES,
            ),
            'label': tfds.features.ClassLabel(
                names=['entailment', 'neutral', 'contradiction']
            ),
        }),
        # No default supervised_keys (as we have to pass both premise
        # and hypothesis as input).
        supervised_keys=None,
        homepage='https://www.nyu.edu/projects/bowman/xnli/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    # Add urls pointing to machine translations of MNLI, provided by XTREME
    download_urls = {
        lang: _XTREME_TRANSLATIONS_FORMAT.format(lang)
        for lang in _LANGUAGES
        if lang != 'en'
    }
    dl_dirs = dl_manager.download_and_extract(download_urls)
    return {'train': self._generate_examples(dl_dirs)}

  def _generate_examples(self, dl_dirs):
    rows_per_pair_id = collections.defaultdict(list)
    en_pair_to_id = {}
    for lang in _LANGUAGES:
      # Translations are only for non-English languages.
      if lang == 'en':
        continue
      with tf.io.gfile.GFile(dl_dirs[lang]) as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        for row in reader:
          en_sent1, en_sent2, translated_sent1, translated_sent2, label = row
          # Change XTREME's label to conform with eval data.
          if label == 'contradictory':
            label = 'contradiction'
          key = (en_sent1, en_sent2)
          if key not in en_pair_to_id:
            en_pair_to_id[key] = len(en_pair_to_id)
            rows_per_pair_id[key].append({
                'language': 'en',
                'sentence1': en_sent1,
                'sentence2': en_sent2,
                'gold_label': label,
                'pairID': en_pair_to_id[key],
            })
          pair_id = en_pair_to_id[key]
          row = {
              'language': lang,
              'sentence1': translated_sent1,
              'sentence2': translated_sent2,
              'gold_label': label,
              'pairID': pair_id,
          }
          rows_per_pair_id[key].append(row)

    for rows in rows_per_pair_id.values():
      premise = {row['language']: row['sentence1'] for row in rows}
      hypothesis = {row['language']: row['sentence2'] for row in rows}
      yield rows[0]['pairID'], {
          'premise': premise,
          'hypothesis': hypothesis,
          'label': rows[0]['gold_label'],
      }
