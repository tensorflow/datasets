"""Coil-100 Test"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.image import coil100
import tensorflow_datasets.testing as tfds_test


class Coil100Test(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = coil100.Coil100
  SPLITS = {
      "train": 5,
  }


if __name__ == "__main__":
  tfds_test.test_main()
