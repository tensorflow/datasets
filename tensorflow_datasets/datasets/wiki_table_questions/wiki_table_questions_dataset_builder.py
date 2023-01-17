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

"""wiki_table_questions dataset."""

from __future__ import annotations

import csv
import os

from etils import epath
import numpy as np
import tensorflow_datasets.public_api as tfds

_DOWNLOAD_URL = (
    'https://github.com/ppasupat/WikiTableQuestions/archive/master.zip'
)


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wiki_table_questions dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'input_text': {
                'table': tfds.features.Sequence({
                    'column_header': np.str_,
                    'row_number': np.int16,
                    'content': np.str_,
                }),
                # Here the context corresponds to the question.
                'context': np.str_,
            },
            'target_text': np.str_,
        }),
        supervised_keys=('input_text', 'target_text'),
        homepage='https://ppasupat.github.io/WikiTableQuestions/#usage-notes',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = os.path.join(
        dl_manager.download_and_extract(_DOWNLOAD_URL),
        'WikiTableQuestions-master',
    )
    examples_sub_dir = os.path.join(path, 'data')
    data_splits = {}
    for split_name in ['train', 'dev']:
      for split_num in range(1, 4):
        examples_file = os.path.join(
            examples_sub_dir, f'random-split-{split_num}-{split_name}.tsv'
        )
        data_split_key = 'split-{}-{}'.format(split_num, split_name)
        data_splits[data_split_key] = self._generate_examples(
            examples_path=examples_file, tables_path=path
        )
    data_splits['train'] = self._generate_examples(
        examples_path=os.path.join(examples_sub_dir, 'training.tsv'),
        tables_path=path,
    )
    data_splits['test'] = self._generate_examples(
        examples_path=os.path.join(
            examples_sub_dir, 'pristine-unseen-tables.tsv'
        ),
        tables_path=path,
    )
    return data_splits

  def _generate_examples(self, examples_path, tables_path):
    """Yields examples."""
    with epath.Path(examples_path).open() as examples:
      for example in csv.DictReader(examples, delimiter='\t'):
        table = []
        with epath.Path(
            os.path.join(tables_path, example['context'])
        ).open() as table_csv:
          for row_number, row in enumerate(
              csv.DictReader(
                  table_csv, delimiter=',', quotechar='"', escapechar='\\'
              )
          ):
            for header, value in row.items():
              table.append({
                  'column_header': header,
                  'row_number': row_number,
                  'content': value,
              })
        yield example['id'], {
            'input_text': {'table': table, 'context': example['utterance']},
            'target_text': example['targetValue'],
        }
