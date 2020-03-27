"""Tests for REDS dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import reds


class REDSTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = reds.REDS
  BUILDER_CONFIG_NAMES_TO_TEST = ["blur"]
  SPLITS = {"train": 4, "validation": 4, "test": 4}
  DL_EXTRACT_RESULT = ["train_blur.zip", "val_blur.zip", "test_blur.zip"]


if __name__ == "__main__":
  testing.test_main()
