"""DiscoFuse Test"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.text import disco_fuse


class DiscoFuseTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = disco_fuse.DiscoFuse
  BUILDER_CONFIG_NAMES_TO_TEST = ["wikipedia"]
  SPLITS = {
      "train": 9,  # Number of fake train example
      "test": 4,
      "dev": 3,
      "train_balanced": 9,  # Number of fake train example
      "test_balanced": 4,
      "dev_balanced": 3
  }
  OVERLAPPING_SPLITS = ["train_balanced", "test_balanced", "dev_balanced"]

if __name__ == "__main__":
  testing.test_main()

