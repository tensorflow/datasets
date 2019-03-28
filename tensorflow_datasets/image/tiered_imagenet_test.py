"""Tests for PASCAL VOC image data loading."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import tiered_imagenet

class TieredImagenetTest(testing.DatasetBuilderTestCase):
    DATASET_CLASS = tiered_imagenet.TieredImagenet
    SPLITS = {
        "train": 6,
        "validation": 4,
        "test": 4
    }


if __name__ == "__main__":
    testing.test_main()
