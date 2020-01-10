"""
Test for BBBP Dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import bbbp


class BbbpTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = bbbp.Bbbp
  SPLITS = {
      "train": 1
  }

  DL_EXTRACT_RESULT = "BBBP.csv"


if __name__ == "__main__":
  testing.test_main()
