from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from tensorflow_datasets.image import binary_alpha_digits
import tensorflow_datasets.testing as tfds_test


class BinaryAlphaDigitsTest(tfds_test.DatasetBuilderTestCase):
    DATASET_CLASS = binary_alpha_digits.BinaryAlphaDigits
    SPLITS = {  
        "train": 2,
      }

    DL_EXTRACT_RESULT = {
        tf.compat.as_str("'train':'train_20x16.mat'",encoding='utf-8'),
      }
 

if __name__ == "__main__":
    tfds_test.test_main()
