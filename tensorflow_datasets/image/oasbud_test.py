"""Raw rf ultrasound data of breast tumors, with segmentation masks and classifiers test."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image import oasbud


class OasbudTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = oasbud.Oasbud
  BUILDER_CONFIG_NAMES_TO_TEST = ["raw_rf", "b_mode"]

  SPLITS = {
      "train": 5  # Number of entries in fake .mat file
  }

  DL_EXTRACT_RESULT = 'oasbud_fake.mat'


if __name__ == "__main__":
  tfds.testing.test_main()
