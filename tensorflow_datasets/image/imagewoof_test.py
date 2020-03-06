from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import imagewoof


class ImagewangFullSizeTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagewoof.Imagewoof
  SPLITS = {
      "train": 4,
      "validation": 4,
  }


if __name__ == "__main__":
  testing.test_main()