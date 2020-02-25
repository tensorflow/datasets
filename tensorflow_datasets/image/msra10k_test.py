"""TODO(msra10k): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import msra10k


class Msra10kTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = msra10k.Msra10k
  SPLITS = {
      "train": 3,  # Number of fake train example
  }


if __name__ == "__main__":
  testing.test_main()
