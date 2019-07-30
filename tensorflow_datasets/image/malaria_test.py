"""Malaria Dataset Test"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.image import malaria
from tensorflow_datasets import testing


class MalariaTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = malaria.Malaria
  SPLITS = {
      "train": 4,
  }


if __name__ == "__main__":
  testing.test_main()
