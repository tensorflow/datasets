"""pg19_language_modeling dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import pg19


class Pg19Test(tfds.testing.DatasetBuilderTestCase):
  # TODO(pg19_language_modeling):
  DATASET_CLASS = pg19.Pg19
  SPLITS = {
      "train": 3,  # Number of fake train example
      "test": 1,  # Number of fake test example
      "validation": 1 # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      "train": ["1211.txt", "1212.txt"],
      "test": ["1213.txt"],
      "validation": ["1214.txt"],
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  tfds.testing.test_main()
