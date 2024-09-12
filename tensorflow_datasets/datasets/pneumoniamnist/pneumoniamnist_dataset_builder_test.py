"""pneumoniamnist dataset."""

from tensorflow_datasets.datasets.pneumoniamnist import pneumoniamnist_dataset_builder
import tensorflow_datasets.public_api as tfds

class PneumoniamnistTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for pneumoniamnist dataset."""

  DATASET_CLASS = pneumoniamnist_dataset_builder.Builder
  SPLITS = {
    'train': 3,
    'val': 1,
    'test': 1,
  }

  DL_EXTRACT_RESULT = {
        'https://zenodo.org/record/10519652/files/pneumoniamnist.npz?download=1': 'pneumoniamnist.npz',
  }



if __name__ == '__main__':
  tfds.testing.test_main()
