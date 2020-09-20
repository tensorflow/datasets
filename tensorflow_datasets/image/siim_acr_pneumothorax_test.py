"""siim_acr_pneumothorax dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image import siim_acr_pneumothorax


class SiimAcrPneumothoraxTest(tfds.testing.DatasetBuilderTestCase):
  # TODO(siim_acr_pneumothorax):
  DATASET_CLASS = siim_acr_pneumothorax.SiimAcrPneumothorax
  SPLITS = {
      "train": 10
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  tfds.testing.test_main()

