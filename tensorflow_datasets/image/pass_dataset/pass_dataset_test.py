"""pass dataset."""

import tensorflow_datasets as tfds
import pass_dataset


class PASSTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for pass dataset."""
  DATASET_CLASS = pass_dataset.PASS
  SPLITS = {
      'train': 5,  # Number of fake train examples
  }

  DL_EXTRACT_RESULT = {
      'train_images': ['pass_dataset/dummy.0.tar','pass_dataset/dummy.1.tar'],
      'meta_data': 'dummy_meta.csv'
  }


if __name__ == '__main__':
  tfds.testing.test_main()
