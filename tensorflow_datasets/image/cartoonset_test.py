"""Test for the cartoon dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import cartoonset


class CartoonSet10kTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cartoonset.Cartoonset10k
  SPLITS = {
    "train": 3,  # Number of fake train example
  }


class CartoonSet100kTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cartoonset.Cartoonset100k
  SPLITS = {
    "train": 30,  # Number of fake train example
  }


if __name__ == "__main__":
  testing.test_main()
