from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from tensorflow_datasets.image import cars196
import tensorflow_datasets.testing as tfds_test


class BinaryAlphaDigitsTest(tfds_test.DatasetBuilderTestCase):
    DATASET_CLASS = cars196.Cars196
    SPLITS = {  
        "train": 2,
        "test":2
      }

    DL_EXTRACT_RESULT = {
        'train':'train/cars_train',
        'test':'test/cars_test',
        'extra':'extra/devkit'
      }
 

if __name__ == "__main__":
    tfds_test.test_main()
