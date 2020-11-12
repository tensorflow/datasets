"""Test for tensorflow_datasets.structured.htru_2"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import htru2

class Htru2Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = htru2.Htru2
  SPLITS = {
      "train": 10
  }

  DL_EXTRACT_RESULT = ""


if __name__ == "__main__":
  testing.test_main()
