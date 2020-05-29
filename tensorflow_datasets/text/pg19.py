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

"""PG-19 language modeling dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import pg19_utils


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

_METADATA_URL = 'https://storage.googleapis.com/deepmind-gutenberg/metadata.csv'
_TRAIN_DATA = pg19_utils.get_all_files_name('train')
_TEST_DATA = pg19_utils.get_all_files_name('test')
_VALIDATION_DATA = pg19_utils.get_all_files_name('validation')
_DOWNLOAD_URLS = {
    'metadata': _METADATA_URL,
    'train': pg19_utils.get_urls(_TRAIN_DATA)[:100],
    'test': pg19_utils.get_urls(_TEST_DATA),
    'val': pg19_utils.get_urls(_VALIDATION_DATA)
}

class Pg19(tfds.core.GeneratorBasedBuilder):
  """This dataset contains the PG-19 language modeling benchmark"""

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

    dl_dir = dl_manager.download(_DOWNLOAD_URLS)
    metadata = tf.io.gfile.GFile(dl_dir['metadata']).read().splitlines()
    metadata_dict = dict()
    for row in metadata:
      row_split = row.split(',')
      # book_id: [book_title, publication_date, book_link]
      metadata_dict[int(row_split[0])] = row_split[1:]

    def _get_filename(url):
      return int(url.split('/')[-1].rstrip(".txt"))

    train_filenames = list(map(_get_filename, _DOWNLOAD_URLS['train']))
    test_filenames = list(map(_get_filename, _DOWNLOAD_URLS['test']))
    val_filenames = list(map(_get_filename, _DOWNLOAD_URLS['val']))
    print(train_filenames)
    train_metadata = [(file, metadata_dict[file]) for file in train_filenames]
    test_metadata = [(file, metadata_dict[file]) for file in test_filenames]
    val_metadata = [(file, metadata_dict[file]) for file in val_filenames]

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "metadata": train_metadata,
                "filepaths": dl_dir['train']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "metadata": val_metadata,
                "filepaths": dl_dir['val']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "metadata": test_metadata,
                "filepaths": dl_dir['test']},
        ),
    ]

  def _generate_examples(self, filepaths, metadata):
    """Yields examples."""

    def _get_file_name(filename):
     # Return book_id from filename
      for name in filename.split('/'):
        if name.startswith('deepmind'):
          file = name.split('_')[2]
          book_id = ''
          for i in file:
            if not i.isdigit():
              return book_id[:5]
            book_id += i
          return book_id[:5]
      return '10005'


    for index, file in enumerate(filepaths):
      # book_id = _get_file_name(file)
      book_id = metadata[index][0]
      print("<-----CHARLES----->", file)
      book_data = metadata[index][1]
      print(book_data)
      # book_data = metadata[int(book_id)]

      with tf.io.gfile.GFile(file, 'r') as f:
        text = f.read().strip()
        yield index, {
            "book_text": text,
            "book_id": book_id,
            "book_title": book_data[0],
            "publication_date": book_data[1],
            "book_link": book_data[2]
            }
