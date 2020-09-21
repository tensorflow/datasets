"""siim_acr_pneumothorax dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image import siim_acr_pneumothorax


class SiimAcrPneumothoraxTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = siim_acr_pneumothorax.SiimAcrPneumothorax
  SKIP_CHECKSUMS = True
  SPLITS = {
      "train": 3  # Number of fake train example
  }


if __name__ == "__main__":
  tfds.testing.test_main()
