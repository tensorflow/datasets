"""Tests for chexpert dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.image import chexpert


class ChexpertTest(testing.DatasetBuilderTestCase):
    DATASET_CLASS = chexpert.Chexpert
    SPLITS = {
        "train": 1,
        "validation": 1,
    }


if __name__ == "__main__":
    testing.test_main()
