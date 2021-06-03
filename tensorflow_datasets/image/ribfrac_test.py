"""ribfrac dataset."""

import tensorflow_datasets as tfds
from tensorflow_datasets import testing

import ribfrac


class RibfracTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ribfrac dataset."""
  # TODO(ribfrac):
  DATASET_CLASS = ribfrac.Ribfrac
  SPLITS = {
      'train': 1,  # Number of fake train example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = {
    'image': 'ribfrac-val-images/RibFrac421-image.nii.gz',
    'mask': 'ribfrac-val-labels/RibFrac421-label.nii.gz',
    'csv': 'ribfrac-val-info.csv'
  }


if __name__ == '__main__':
  tfds.testing.test_main()
