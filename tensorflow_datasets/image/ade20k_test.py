"""Tests for Ade20k dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import ade20k


class Ade20kTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = ade20k.Ade20k
  SPLITS = {
      "train": 1,
      "validation": 1,
  }


if __name__ == "__main__":
  testing.test_main()
