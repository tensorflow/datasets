"""Test file for spine_web"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
import spine_web


class SpineWebTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = spine_web.SpineWeb
  SPLITS = {
    "train": 5,  # Number of fake train example
    "test": 2,  # Number of fake test example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = {
    'train': "training_images",
    'train_csv': "training_angles.csv",
    'test': "test_images",
    'test_csv': "test_angles.csv"
  }


if __name__ == "__main__":
  testing.test_main()
