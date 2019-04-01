from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from tensorflow_datasets.image import mura
import tensorflow_datasets.testing as tfds_test


class MuraTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = mura.Mura
  SPLITS = {  
      "train":2,
      "valid":2
  }
 

if __name__ == "__main__":
  tfds_test.test_main()
    