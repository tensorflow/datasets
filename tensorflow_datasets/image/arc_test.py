"""TODO(arc): Add a description here."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import arc


class ArcTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = arc.ARC
  SPLITS = {
      "train": 10,  # Number of fake train example
      "test": 5,  # Number of fake test example
  }


if __name__ == "__main__":
  testing.test_main()
