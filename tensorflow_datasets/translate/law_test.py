"""law dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate import law


class LawTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = law.Law
  BUILDER_CONFIG_NAMES_TO_TEST = ["de_en"]
  SPLITS = {
      "train": 15,
  }


if __name__ == "__main__":
  tfds.testing.test_main()

