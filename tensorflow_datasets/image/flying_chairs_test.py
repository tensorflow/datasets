"""Tests for the Flying Chairs dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import flying_chairs


class FlyingChairsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = flying_chairs.FlyingChairs
  SPLITS = {
      "train": 3,
      "validation": 2,
  }

  DL_EXTRACT_RESULT = ['zip', 'FlyingChairs_train_val.txt']

if __name__ == "__main__":
  testing.test_main()
