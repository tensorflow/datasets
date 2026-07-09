"""caltech256 dataset."""

import tensorflow_datasets as tfds
from tensorflow_datasets.image_classification.caltech256 import caltech256


class Caltech256Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for caltech256 dataset."""
  DATASET_CLASS = caltech256.Caltech256

  SPLITS = {
    'train': 2,  # Number of fake train example
    'test': 2,  # Number of fake test example
  }

  def setUp(self):
    super(Caltech256Test, self).setUp()
    caltech256._TRAIN_POINTS_PER_CLASS = 1


if __name__ == '__main__':
  tfds.testing.test_main()
