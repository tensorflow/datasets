from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from tensorflow_datasets.image import malaria
import tensorflow_datasets.testing as tfds_test


class MalariaTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = malaria.Malaria
  SPLITS = {  
      "train":4,
  }
 

if __name__ == "__main__":
  tfds_test.test_main()
    