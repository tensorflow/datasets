"""nih_chest_xray dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.image_classification import nih_chest_xray


class NihChestXrayTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = nih_chest_xray.NihChestXray
  SPLITS = {
      "train": 3,  # Number of fake train example
      "test": 1,  # Number of fake test example
  }

  DL_EXTRACT_RESULT = {
    'zipfile01': 'data01', # fake data directory
    'data_entry_2017': 'fake_data_entry_2017.csv',
    'train_val_list': 'train_val_list.txt',
    'test_list': 'test_list.txt',
  }


if __name__ == "__main__":
  tfds.testing.test_main()

