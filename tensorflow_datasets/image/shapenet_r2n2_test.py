"""Tests for shapenet_r2n2 dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.image import shapenet_r2n2 as sn
import tensorflow_datasets.testing.shapenet_r2n2 as snt

# testing/shapenet_r2n2.py generates fake input data
train_count = int(snt.N_EXAMPLES * sn._TRAIN_FRAC)
test_count = snt.N_EXAMPLES - train_count


class ShapeNetR2n2MultiTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = sn.ShapenetR2n2
  BUILDER_CONFIG_NAMES_TO_TEST = ['%s-multi' % c for c in snt.CAT_IDS]
  SPLITS = {
      "train": train_count,
      "test": test_count,
  }
  DL_EXTRACT_RESULT = {
      "voxels_path": "./",
      "renderings_path": "./",
  }


class ShapeNetR2n2SingleTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = sn.ShapenetR2n2
  BUILDER_CONFIG_NAMES_TO_TEST = ['%s-single' % c for c in sn.cat_ids()[:2]]
  SPLITS = {
      "train": train_count * sn.RENDERINGS_PER_EXAMPLE,
      "test":  test_count * sn.RENDERINGS_PER_EXAMPLE,
  }
  DL_EXTRACT_RESULT = {
      "voxels_path": "./",
      "renderings_path": "./",
  }


if __name__ == "__main__":
  testing.test_main()
