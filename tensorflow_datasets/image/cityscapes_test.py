
'''Tests for Cityscapes dataset module.'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import cityscapes

# TODO add tests for features and files per configuration
class CityscapesSegmentationTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes.Cityscapes
  BUILDER_CONFIG_NAMES_TO_TEST = ['semantic_segmentation']
  SPLITS = {
      'train': 3,
      'validation': 1,
      'test': 2,
  }


class CityscapesSegmentationExtraTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes.Cityscapes
  BUILDER_CONFIG_NAMES_TO_TEST = ['semantic_segmentation_extra']
  SPLITS = {
      'train': 3,
      'train_extra': 4,
      'validation': 1,
  }


class CityscapesStereoDisparityTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes.Cityscapes
  BUILDER_CONFIG_NAMES_TO_TEST = ['stereo_disparity']
  SPLITS = {
      'train': 3,
      'validation': 1,
      'test': 2,
  }


class CityscapesStereoDisparityExtraTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes.Cityscapes
  BUILDER_CONFIG_NAMES_TO_TEST = ['stereo_disparity_extra']
  SPLITS = {
      'train': 3,
      'train_extra': 4,
      'validation': 1,
  }


if __name__ == '__main__':
  testing.test_main()
