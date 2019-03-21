from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from tensorflow_datasets.image import places365_small
import tensorflow_datasets.testing as tfds_test


class Places365SmallTest(tfds_test.DatasetBuilderTestCase):
    DATASET_CLASS = places365_small.Places365Small
    SPLITS = {  
        "train": 2,
        "test":2,
        "validation":2
      }

    DL_EXTRACT_RESULT = {
        'train':'data_256',
        'test':'test_256',
        'extra':'val_256'
      }
 

if __name__ == "__main__":
    tfds_test.test_main()
