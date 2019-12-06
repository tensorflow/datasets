"""Test for div2k dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import div2k


class Div2kTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = div2k.Div2k
  SPLITS = {
      "train": 4,
      "validation": 4,
  }
  DL_EXTRACT_RESULT = {
    "HR": "",
    "bicubic": "",
  }

if __name__ == "__main__":
  testing.test_main()
