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
"""PG-19 language modeling dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@article{raecompressive2019,
author = {Rae, Jack W and Potapenko, Anna and Jayakumar, Siddhant M and
          Hillier, Chloe and Lillicrap, Timothy P},
title = {Compressive Transformers for Long-Range Sequence Modelling},
journal = {arXiv preprint},
url = {https://arxiv.org/abs/1911.05507},
year = {2019},
}
"""

_DESCRIPTION = """
This dataset contains the PG-19 language modeling benchmark. It includes a set
of books extracted from the Project Gutenberg books project
(https://www.gutenberg.org), that were published before 1919. It also contains
metadata of book titles and publication dates.
PG-19 is over double the size of the Billion Word benchmark and contains
documents that are 20X longer, on average, than the WikiText long-range
language modelling benchmark.

Books are partitioned into a train, validation, and test set. Books metadata is
stored in metadata.csv which contains
(book_id, short_book_title, publication_date, book_link).
"""

_DATA_DIR = 'gs://deepmind-gutenberg'


class Pg19(tfds.core.GeneratorBasedBuilder):
  """This dataset contains the PG-19 language modeling benchmark."""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'book_text': tfds.features.Text(),
            'book_id': tf.int32,
            'book_title': tf.string,
            'publication_date': tf.string,
            'book_link': tf.string
        }),
        supervised_keys=None,
        homepage='https://github.com/deepmind/pg19',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    del dl_manager  # Unused

    metadata_dict = dict()
    metadata_path = os.path.join(_DATA_DIR, 'metadata.csv')
    metadata = tf.io.gfile.GFile(metadata_path).read().splitlines()

    for row in metadata:
      row_split = row.split(',')
      # book_id: [book_title, publication_date, book_link]
      metadata_dict[int(row_split[0])] = row_split[1:]

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'metadata': metadata_dict,
                'filepath': os.path.join(_DATA_DIR, 'train')},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'metadata': metadata_dict,
                'filepath': os.path.join(_DATA_DIR, 'validation')},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'metadata': metadata_dict,
                'filepath': os.path.join(_DATA_DIR, 'test')},
        ),
    ]

  def _generate_examples(self, filepath, metadata):
    """Yields examples."""
    for file in tf.io.gfile.listdir(filepath):
      book_id = int(file.rstrip('.txt'))
      book_data = metadata[book_id]
      path = os.path.join(filepath, file)
      with tf.io.gfile.GFile(path, 'r') as f:
        text = f.read().strip()
        yield book_id, {
            'book_text': text,
            'book_id': book_id,
            'book_title': book_data[0],
            'publication_date': book_data[1],
            'book_link': book_data[2],
        }
