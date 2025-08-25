"""isic2019 dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image_classification import isic2019


class Isic2019Test(tfds.testing.DatasetBuilderTestCase):
  # TODO(isic2019):
  DATASET_CLASS = isic2019.Isic2019
  SPLITS = {
      "train": 3,  # Number of fake train example
      # Number of fake test example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
    DL_EXTRACT_RESULT = {
        "images_zip": "ISIC_2019_Training_Input.zip",
        "label_csv": "ISIC_2019_Training_GroundTruth.csv",
        "meta_csv": 'ISIC_2019_Training_Metadata.csv',
    }


if __name__ == "__main__":
  tfds.testing.test_main()

