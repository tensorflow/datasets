"""ribfrac dataset."""

import tensorflow_datasets as tfds
from tensorflow_datasets import testing

import ribfrac


class RibfracTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ribfrac dataset."""
  SKIP_CHECKSUMS = True
  DATASET_CLASS = ribfrac.Ribfrac
  SPLITS = {
      'valid': 1,  # Number of fake train example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = { 
    'valid': {
      'valid_images_1': '',
      'valid_masks_1': '',
      'csv_1': 'ribfrac-val-info.csv'
    }
  }


if __name__ == '__main__':
  tfds.testing.test_main()
