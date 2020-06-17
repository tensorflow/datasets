"""Tests for Custom Translate Dataset."""

import tensorflow_datasets as tfds

class TranslateDatasetTests(tfds.testing.DatasetBuilderTestCase):
  # DATASET_CLASS =  TranslateDatasetTests
  SPLITS = {
      'train': 2,
      'test': 2,
      'test': 2,
  }

  # TODO: Tests

if __name__ == '__main__':
#   tfds.testing.test_main()
    pass
