"""Tests for STL10 dataset module"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import stl10


class Stl10Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = stl10.Stl10
  SPLITS = {
      "train": 3,  # Number of fake train example
      "test": 1,  # Number of fake test example
  }


if __name__ == "__main__":
  testing.test_main()
