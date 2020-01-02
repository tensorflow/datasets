""" Tests for Imagewang contains Imagenette and Imagewoof combined. """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import imagewang


class ImagewangFullSizeTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagewang.Imagewang
  BUILDER_CONFIG_NAMES_TO_TEST = ['full-size']
  SPLITS = {
      "train": 4,
      "test": 4,
  }


class Imagewang320Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagewang.Imagewang
  BUILDER_CONFIG_NAMES_TO_TEST = ['320px']
  SPLITS = {
      "train": 4,
      "test": 4,
  }


class Imagewang160Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagewang.Imagewang
  BUILDER_CONFIG_NAMES_TO_TEST = ['160px']
  SPLITS = {
      "train": 4,
      "test": 4,
  }


if __name__ == "__main__":
  testing.test_main()
