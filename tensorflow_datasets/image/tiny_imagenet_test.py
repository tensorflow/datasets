"""Tiny Imagenet: Smaller version of ImageNet"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import tiny_imagenet


class TinyImagenetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = tiny_imagenet.TinyImagenet
  SPLITS = {
      "train": 10,  # Number of fake train example
      "validation": 5,
      "test": 2,  # Number of fake test example
  }


class TinyImagenetS3Test(TinyImagenetTest):
  VERSION = 'experimental_latest'


if __name__ == "__main__":
  testing.test_main()
