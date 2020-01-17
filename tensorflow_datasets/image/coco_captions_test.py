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

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  # DL_EXTRACT_RESULT = {'some_key': 'output_file1.txt', ...}
  DL_EXTRACT_RESULT = {
    'images': '.',
    'annotations': '.' 
  }

if __name__ == "__main__":
  testing.test_main()

