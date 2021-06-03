"""ribfrac dataset."""

import tensorflow_datasets as tfds
from tensorflow_datasets import testing

import ribfrac

class RibfracTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ribfrac dataset."""
  SKIP_CHECKSUMS = True
  DATASET_CLASS = ribfrac.Ribfrac
  SPLITS = {
    'train_1': 2,
    'train_2': 2,
    'valid': 1,
  }

  DL_EXTRACT_RESULT = {
    'train_1': {
      'train_images_1': '',
      'train_masks_1': '',
      'csv_1': 'ribfrac-train-info-1.csv',
    },
    'train_2': {
      'train_images_2': '',
      'train_masks_2': '',
      'csv_2': 'ribfrac-train-info-2.csv'
    },
    'valid': {
      'valid_images_1': '',
      'valid_masks_1': '',
      'csv_1': 'ribfrac-val-info.csv',
    },
  }

if __name__ == '__main__':
  tfds.testing.test_main()
