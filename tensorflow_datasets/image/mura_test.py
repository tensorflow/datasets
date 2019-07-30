"""Tests for Mura Dataset"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.image import mura
from tensorflow_datasets import testing


class MuraTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = mura.Mura
  SPLITS = {
      "train": 2,
      "valid": 2
  }


if __name__ == "__main__":
  testing.test_main()
