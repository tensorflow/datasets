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

import csv
import os

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
The dataset contains pairs table-question, and the respective answer. The
questions require multi-step reasoning and various data operations such as
comparison, aggregation, and arithmetic computation. The tables were randomly
selected among Wikipedia tables with at least 8 rows and 5 columns.

(As per the documentation usage notes)

- Dev: Mean accuracy over three (not five) splits of the training data. In other
words, train on 'split-{1,2,3}-train' and test on 'split-{1,2,3}-dev',
respectively, then average the accuracy.

- Test: Train on 'train' and test on 'test'.
"""

_CITATION = """
@inproceedings{pasupat-liang-2015-compositional,
    title = "Compositional Semantic Parsing on Semi-Structured Tables",
    author = "Pasupat, Panupong  and
      Liang, Percy",
    booktitle = "Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = jul,
    year = "2015",
    address = "Beijing, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P15-1142",
    doi = "10.3115/v1/P15-1142",
    pages = "1470--1480",
}
"""

_DOWNLOAD_URL = 'https://github.com/ppasupat/WikiTableQuestions/archive/master.zip'


class WikiTableQuestions(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for wiki_table_questions dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'input_text': {
                'table':
                    tfds.features.Sequence({
                        'column_header': tf.string,
                        'row_number': tf.int16,
                        'content': tf.string,
                    }),
                # Here the context corresponds to the question.
                'context':
                    tf.string,
            },
            'target_text': tf.string,
        }),
        supervised_keys=('input_text', 'target_text'),
        homepage='https://ppasupat.github.io/WikiTableQuestions/#usage-notes',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = os.path.join(
        dl_manager.download_and_extract(_DOWNLOAD_URL),
        'WikiTableQuestions-master')
    examples_sub_dir = os.path.join(path, 'data')
    data_splits = {}
    for split_name in ['train', 'dev']:
      for split_num in range(1, 4):
        examples_file = os.path.join(
            examples_sub_dir, f'random-split-{split_num}-{split_name}.tsv')
        data_split_key = 'split-{}-{}'.format(split_num, split_name)
        data_splits[data_split_key] = self._generate_examples(
            examples_path=examples_file, tables_path=path)
    data_splits['train'] = self._generate_examples(
        examples_path=os.path.join(examples_sub_dir, 'training.tsv'),
        tables_path=path)
    data_splits['test'] = self._generate_examples(
        examples_path=os.path.join(examples_sub_dir,
                                   'pristine-unseen-tables.tsv'),
        tables_path=path)
    return data_splits

  def _generate_examples(self, examples_path, tables_path):
    """Yields examples."""
    with tf.io.gfile.GFile(examples_path) as examples:
      for example in csv.DictReader(examples, delimiter='\t'):
        table = []
        with tf.io.gfile.GFile(os.path.join(tables_path,
                                            example['context'])) as table_csv:
          for row_number, row in enumerate(
              csv.DictReader(
                  table_csv, delimiter=',', quotechar='"', escapechar='\\')):
            for header, value in row.items():
              table.append({
                  'column_header': header,
                  'row_number': row_number,
                  'content': value
              })
        yield example['id'], {
            'input_text': {
                'table': table,
                'context': example['utterance']
            },
            'target_text': example['targetValue']
        }
