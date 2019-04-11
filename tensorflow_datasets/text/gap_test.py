"""Test for GAP data set"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.text import gap


class GapTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = gap.Gap
  SPLITS = {
      "train": 5,  # Number of fake train examples
      "validation": 3,  # Number of fake validation examples
      "test": 3,  # Number of fake test examples
  }
  DL_EXTRACT_RESULT = {
      "train": "gap-development.tsv",
      "validation": "gap-validation.tsv",
      "test": "gap-test.tsv",
  }


if __name__ == "__main__":
  testing.test_main()
