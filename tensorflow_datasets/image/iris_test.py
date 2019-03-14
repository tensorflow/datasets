"""Tests for tensorflow_datasets.image.lsun."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.image import iris


class IrisTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = iris.Iris

  SPLITS = {
      "train": 12,
      "test": 3,
  }
  DL_EXTRACT_RESULT = "iris.data"

if __name__ == "__main__":
  testing.test_main()
