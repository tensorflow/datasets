"""Tests for colorectal_histology dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.image import colorectal_histology

# testing/colorectal_histology.py generates fake input data

num_classes = len(colorectal_histology._CLASS_NAMES)


class ColorectalHistologyTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = colorectal_histology.ColorectalHistology
  SPLITS = {
      "train": 8*num_classes,
      "test": num_classes,
      "validation": num_classes,
  }


class ColorectalHistologyLargeTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = colorectal_histology.ColorectalHistologyLarge
  SPLITS = {
      "test": 1,
  }


if __name__ == "__main__":
  testing.test_main()
