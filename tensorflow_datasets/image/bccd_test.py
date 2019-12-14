"""TODO(bccd_dataset): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import bccd


class BCCDTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = bccd.BCCD
  SPLITS = {
    "train": 1,
  }


if __name__ == "__main__":
  testing.test_main()
