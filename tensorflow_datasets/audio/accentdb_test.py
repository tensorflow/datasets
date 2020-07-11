"""AccentDB dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.audio import accentdb


class AccentDTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = accentdb.AccentDB
  SPLITS = {
      "train": 33,  
      "test": 8, 
      "validation": 7,
  }


if __name__ == "__main__":
  tfds.testing.test_main()

