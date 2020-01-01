""" Tests for Imagewang contains Imagenette and Imagewoof combined. """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import imagewang


class ImagewangTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagewang.Imagewang
  SPLITS = {
      "train": 4,  # Number of fake train example
      "test": 4,  # Number of fake test example
  }

if __name__ == "__main__":
  testing.test_main()
