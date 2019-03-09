from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.image import ham10000
import tensorflow_datasets.testing as tfds_test


class Ham10000Test(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = ham10000.ham10000
  SPLITS = {  
      "train": 2,
  }
 

if __name__ == "__main__":
  tfds_test.test_main()