"""assin2 dataset."""

import tensorflow_datasets as tfds
from . import assin2
# import assin2


class Assin2Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for assin2 dataset."""
  # TODO(assin2):
  DATASET_CLASS = assin2.Assin2
  SPLITS = {
      'train': 5,
      'validation': 5,
      'test': 5,
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = {
    'train': 'assin2-train-only.xml',
    'validation': 'assin2-dev.xml',
    'test': 'assin2-test.xml'
    }


if __name__ == '__main__':
  tfds.testing.test_main()
