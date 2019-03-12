
'''Tests for Cityscapes dataset module.'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import cityscapes

class CityscapesTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes.Cityscapes
  SPLITS = {  # Expected number of examples on each split.
      'train': 3,
      'validation': 1,
      'test': 2,
  }

class CityscapesCoarseTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cityscapes.CityscapesCoarse
  SPLITS = {  # Expected number of examples on each split.
      'train': 3,
      'train_extra': 4,
      'validation': 1,
  }

if __name__ == '__main__':
  testing.test_main()
