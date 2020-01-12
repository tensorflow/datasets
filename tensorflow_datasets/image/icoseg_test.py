"""Tests for tensorflow_datasets.image.icoseg"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import icoseg


class IcosegTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = icoseg.Icoseg

  SPLITS = {
      "train": 4,
  }

if __name__ == "__main__":
  testing.test_main()
