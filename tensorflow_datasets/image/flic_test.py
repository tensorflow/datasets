"""Test for FLIC dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import flic

class FlicTest_small(testing.DatasetBuilderTestCase):
  DATASET_CLASS = flic.Flic
  BUILDER_CONFIG_NAMES_TO_TEST = ["small"]
  SPLITS = {
      "train": 1,
      "test": 1,
  }

class FlicTest_full(testing.DatasetBuilderTestCase):
  DATASET_CLASS = flic.Flic
  BUILDER_CONFIG_NAMES_TO_TEST = ["full"]
  SPLITS = {
      "train": 1,
      "test": 1,
  }

if __name__ == "__main__":
  testing.test_main()
