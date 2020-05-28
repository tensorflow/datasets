"""pg19 dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections

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
    'train': pg19_utils.get_urls(_TRAIN_DATA),
    'test': pg19_utils.get_urls(_TEST_DATA),
    'val': pg19_utils.get_urls(_VALIDATION_DATA)
}

class Pg19(tfds.core.GeneratorBasedBuilder):
  """This dataset contains the PG-19 language modeling benchmark"""

  VERSION = tfds.core.Version('0.1.0')

  def _info(self):

    return tfds.core.DatasetInfo(
        builder=self,
        # This is the description that will appear on the datasets page.
        description=_DESCRIPTION,
        # tfds.features.FeatureConnectors
        features=tfds.features.FeaturesDict({
            "book_text": tfds.features.Text(),
            'metadata': {
                'book_id': tf.int32,
                'book_title': tf.string,
                'publication_date': tf.string,
                'book_link': tf.string
            },
        }),
        supervised_keys=None,
        homepage='https://github.com/deepmind/pg19',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    dl_dir = dl_manager.download(_DOWNLOAD_URLS)
    metadata = tf.io.gfile.GFile(dl_dir['metadata']).read().splitlines()

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "metadata": metadata,
                "filepaths": dl_dir['train']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                "metadata": metadata,
                "filepaths": dl_dir['val']},
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                "metadata": metadata,
                "filepaths": dl_dir['test']},
        ),
    ]

  def _generate_examples(self, filepaths, metadata):
    """Yields examples."""

    metadata_dict = collections.defaultdict(list)
    for row in metadata:
      features = row.split(',')
      metadata_dict['book_id'].append(int(features[0]))
      metadata_dict['book_title'].append(str(features[1]))
      metadata_dict['publication_date'].append(str(features[2]))
      metadata_dict['book_link'].append(str(features[3]))

    with tf.io.gfile.GFile(filepaths, 'r') as f:
      text = f.read().strip()

      yield metadata_dict, {"book_data": text}
