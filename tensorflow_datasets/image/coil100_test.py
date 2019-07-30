"""Coil-100 Test"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.image import coil100
from tensorflow_datasets import testing


class Coil100Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = coil100.Coil100
  SPLITS = {
      "train": 5,
  }


if __name__ == "__main__":
  testing.test_main()
