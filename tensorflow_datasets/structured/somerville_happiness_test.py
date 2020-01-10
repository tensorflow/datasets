
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import somerville_happiness


class SomervilleHappinessTest(testing.DatasetBuilderTestCase):
 
  DATASET_CLASS = somerville_happiness.SomervilleHappiness
  SPLITS = {
      "train": 1, 
  }


if __name__ == "__main__":
  testing.test_main()

