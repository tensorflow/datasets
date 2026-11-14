from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from tensorflow_datasets import testing
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image_classification import affnist

class AffnistTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = affnist.Affnist
  SPLITS = {
      "train": 20,
      "validation": 10,
      "test": 10,
  }
  DL_EXTRACT_RESULT = {
      "train_data": "train_data",
      "validation_data": "validation_data",
      "test_data": "test_data",
  }

if __name__ == "__main__":
  testing.test_main()
