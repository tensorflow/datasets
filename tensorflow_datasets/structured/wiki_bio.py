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

"""wiki_bio dataset."""
from __future__ import annotations

import os

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{lebret-etal-2016-neural,
    title = "Neural Text Generation from Structured Data with Application to the Biography Domain",
    author = "Lebret, R{\'e}mi  and
      Grangier, David  and
      Auli, Michael",
    booktitle = "Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2016",
    address = "Austin, Texas",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D16-1128",
    doi = "10.18653/v1/D16-1128",
    pages = "1203--1213",
}
"""

_DESCRIPTION = """
WikiBio is constructed using Wikipedia biography pages, it contains the first
paragraph and the infobox tokenized.
The dataset follows a standarized table format.
"""

_URL = 'https://huggingface.co/datasets/wiki_bio/resolve/main/data/wikipedia-biography-dataset.zip'


def _get_table(infobox_line):
  """Converts the infobox into a one row table."""
  cells = infobox_line.split('\t')
  # remove empty cells
  cells = list(filter(lambda x: x.find('<none>') == -1, cells))
  columns = set([cell[0 : cell.split(':')[0].rfind('_')] for cell in cells])
  table = {col: dict() for col in columns}
  for cell in cells:
    delimiter_position_value = cell.find(':')
    column_index = cell[0:delimiter_position_value]
    value = cell[delimiter_position_value + 1 :]
    delimiter_column_index = column_index.rfind('_')
    column = column_index[0:delimiter_column_index]
    index = column_index[delimiter_column_index + 1 :]
    table[column][index] = value
  infobox_line_as_table = []
  for column in table.keys():
    row_value = ' '.join(
        [table[column][index] for index in sorted(table[column].keys())]
    )
    infobox_line_as_table.append({
        'column_header': column,
        'row_number': 1,
        'content': row_value,
    })
  return infobox_line_as_table


class WikiBio(tfds.core.GeneratorBasedBuilder):
  """Infoboxes and first paragraph from Wikipedia biography pages."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'input_text': {
                'table': tfds.features.Sequence({
                    'column_header': np.str_,
                    'row_number': np.int16,
                    'content': np.str_,
                }),
                # context will be the article's title
                'context': np.str_,
            },
            'target_text': np.str_,
        }),
        supervised_keys=('input_text', 'target_text'),
        homepage='https://github.com/DavidGrangier/wikipedia-biography-dataset',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dataset_url = tfds.download.Resource(
        url=_URL, extract_method=tfds.download.ExtractMethod.ZIP
    )
    data_dir = dl_manager.download_and_extract(dataset_url)

    extracted_path = os.path.join(data_dir, 'wikipedia-biography-dataset')

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'id_file': os.path.join(extracted_path, 'train', 'train.id'),
                'infobox_file': os.path.join(
                    extracted_path, 'train', 'train.box'
                ),
                'nb_lines_file': os.path.join(
                    extracted_path, 'train', 'train.nb'
                ),
                'sentences_file': os.path.join(
                    extracted_path, 'train', 'train.sent'
                ),
                'article_title_file': os.path.join(
                    extracted_path, 'train', 'train.title'
                ),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'id_file': os.path.join(extracted_path, 'valid', 'valid.id'),
                'infobox_file': os.path.join(
                    extracted_path, 'valid', 'valid.box'
                ),
                'nb_lines_file': os.path.join(
                    extracted_path, 'valid', 'valid.nb'
                ),
                'sentences_file': os.path.join(
                    extracted_path, 'valid', 'valid.sent'
                ),
                'article_title_file': os.path.join(
                    extracted_path, 'valid', 'valid.title'
                ),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'id_file': os.path.join(extracted_path, 'test', 'test.id'),
                'infobox_file': os.path.join(
                    extracted_path, 'test', 'test.box'
                ),
                'nb_lines_file': os.path.join(
                    extracted_path, 'test', 'test.nb'
                ),
                'sentences_file': os.path.join(
                    extracted_path, 'test', 'test.sent'
                ),
                'article_title_file': os.path.join(
                    extracted_path, 'test', 'test.title'
                ),
            },
        ),
    ]

  def _generate_examples(
      self,
      id_file,
      infobox_file,
      nb_lines_file,
      sentences_file,
      article_title_file,
  ):
    """Yields examples."""
    with tf.io.gfile.GFile(id_file) as id_src, tf.io.gfile.GFile(
        infobox_file
    ) as infobox_src, tf.io.gfile.GFile(
        nb_lines_file
    ) as nb_lines_src, tf.io.gfile.GFile(
        sentences_file
    ) as sentences_src, tf.io.gfile.GFile(
        article_title_file
    ) as article_title_src:
      for id_, infobox, nb_lines, article_title in zip(
          id_src, infobox_src, nb_lines_src, article_title_src
      ):
        target_text = []
        for _ in range(int(nb_lines)):
          target_text.append(sentences_src.readline())
        yield id_, {
            'input_text': {
                'table': _get_table(infobox),
                'context': article_title,
            },
            'target_text': ''.join(target_text),
        }
