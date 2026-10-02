"""Abalone dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import abalone


class AbaloneTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = abalone.Abalone
  SPLITS = {
      "train": 1
  }

  DL_EXTRACT_RESULT = "abalone.data"

if __name__ == "__main__":
  testing.test_main()
