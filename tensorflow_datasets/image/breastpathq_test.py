"""Breast cancer whole slide image dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import breastpathq


class BreastpathqTest(testing.DatasetBuilderTestCase):

  DATASET_CLASS = breastpathq.Breastpathq
  SPLITS = {
      "train": 3,  # Number of fake train example
      "validation": 1,  # Number of fake test example
  }


if __name__ == "__main__":
  testing.test_main()