from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import tiny_imagenet


class TinyImagenetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = tiny_imagenet.TinyImagenet
  SPLITS = {
      "train": 3, 
      "test": 1,
  }

DL_EXTRACT_RESULT = [
  
  'tiny-imagenet-200.zip'
]


if __name__ == "__main__":
  testing.test_main()

