"""heart_disease dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured import heart_disease

class HeartDiseaseTest(tfds.testing.DatasetBuilderTestCase):
  """test for heart disease dataset"""
  DATASET_CLASS = heart_disease.HeartDisease
  SPLITS = {
      "train": 1,  # Number of fake train example
  }
  DL_EXTRACT_RESULT = 'processed.cleveland.data'

if __name__ == "__main__":
  tfds.testing.test_main()
