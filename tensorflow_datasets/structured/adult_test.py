"""UCI Adult Dataset, contains various information of adults"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import adult


class AdultTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = adult.Adult
  SPLITS = {
      "train": 5,  # Number of fake train example
      "test": 3,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = {"train_data": "adult.data", "test_data": "adult.test"}

if __name__ == "__main__":
  testing.test_main()
