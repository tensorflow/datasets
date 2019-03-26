from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from tensorflow_datasets.image import food101
import tensorflow_datasets.testing as tfds_test


class Food101Test(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = food101.Food101
  SPLITS = {  
      "train":4,
  }
 

if __name__ == "__main__":
  tfds_test.test_main()
    