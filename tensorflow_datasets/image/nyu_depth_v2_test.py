"""Tests for NYU Depth V2 Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import nyu_depth_v2


class NyuDepthV2Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = nyu_depth_v2.NyuDepthV2
  SPLITS = {"train": 2, "test": 1}


if __name__ == "__main__":
  testing.test_main()
