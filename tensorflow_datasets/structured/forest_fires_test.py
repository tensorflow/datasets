"""Test for Forest Fires dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import forest_fires


class ForestFiresTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = forest_fires.ForestFires
  SPLITS = {
      "train": 1,
  }

  DL_EXTRACT_RESULT = 'forestfires.csv'

if __name__ == "__main__":
  testing.test_main()
