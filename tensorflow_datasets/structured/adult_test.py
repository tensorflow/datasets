"""Test for UCI Adult Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import adult


class AdultTest(testing.DatasetBuilderTestCase):
  
  DATASET_CLASS = adult.Adult
  SPLITS = {
      "test": 5
  }

  DL_EXTRACT_RESULT = 'adult.test'


if __name__ == "__main__":
  testing.test_main()

