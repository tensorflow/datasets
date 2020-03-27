"""MSCOCO Captioning Dataset from 2014."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import coco_captions


class CocoCaptionsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = coco_captions.CocoCaptions
  SPLITS = {
      "validation": 1
  }

  DL_EXTRACT_RESULT = {
      'images': '.',
      'annotations': '.'
  }

if __name__ == "__main__":
  testing.test_main()
