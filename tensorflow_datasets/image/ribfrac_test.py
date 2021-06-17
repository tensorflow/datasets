"""ribfrac dataset."""

import tensorflow_datasets as tfds
import ribfrac

class RibfracTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ribfrac dataset."""
  SKIP_CHECKSUMS = True
  DATASET_CLASS = ribfrac.Ribfrac
  BUILDER_CONFIG_TO_TEST = ['stack']
  SPLITS = {
    'train': 4,
    'valid': 1,
  }

  DL_EXTRACT_RESULT = {
    'train_1': {
      'train_images_1': 'ribfrac/',
      'train_masks_1': 'ribfrac/',
      'csv_1': 'ribfrac/ribfrac-train-info-1.csv',
    },
    'train_2': {
      'train_images_2': 'ribfrac/',
      'train_masks_2': 'ribfrac/',
      'csv_2': 'ribfrac/ribfrac-train-info-2.csv'
    },
    'valid': {
      'valid_images_1': 'ribfrac/',
      'valid_masks_1': 'ribfrac/',
      'csv_1': 'ribfrac/ribfrac-val-info.csv',
    },
  }

if __name__ == '__main__':
  tfds.testing.test_main()
