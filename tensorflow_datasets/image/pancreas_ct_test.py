"""pancreas_ct dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image import pancreas_ct


class PancreasCtTest(tfds.testing.DatasetBuilderTestCase):
  # TODO(pancreas_ct):
  DATASET_CLASS = pancreas_ct.PancreasCt
  SPLITS = {
      "train": 10,  # Number of fake train example
  }

if __name__ == "__main__":
  tfds.testing.test_main()

