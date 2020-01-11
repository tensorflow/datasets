"""Test for tensorflow_datasets.structured.HTRU2"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import HTRU2

class Htru2Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = HTRU2.Htru2
  SPLITS = {
      "train": 13
  }

  DL_EXTRACT_RESULT = ""


if __name__ == "__main__":
  testing.test_main()

