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


if __name__ == "__main__":
  tfds.testing.test_main()

