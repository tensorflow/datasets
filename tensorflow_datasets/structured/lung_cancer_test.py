"""Test for Lung Cancer Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.structured import lung_cancer


class LungCancerTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = lung_cancer.LungCancer
  SPLITS = {
      "train": 1,
  }
  DL_EXTRACT_RESULT = "lung-cancer.data"

if __name__ == "__main__":
  testing.test_main()
