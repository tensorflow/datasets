"""medical dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate import medical


class MedicalTest(tfds.testing.DatasetBuilderTestCase):
  # TODO(medical):
  DATASET_CLASS = medical.Medical
  BUILDER_CONFIG_NAMES_TO_TEST = ["en_to_de"]
  SPLITS = {
      "train": 15,  # Number of fake train example
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}


if __name__ == "__main__":
  tfds.testing.test_main()

