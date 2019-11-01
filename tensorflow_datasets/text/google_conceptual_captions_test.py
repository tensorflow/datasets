"""
A new dataset of image captionannotations, Conceptual Captions, whichcontains an order of magnitude more im-ages than the MS-COCO dataset and  represents  a  wider  variety  of both images and image caption styles.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.text import google_conceptual_captions


class GoogleConceptualCaptionsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = google_conceptual_captions.GoogleConceptualCaptions
  VERSION="1.1.0"
  SPLITS = {
      "train": 3,  # Number of fake train example
      "validation": 1,  # Number of fake validation example
  }


if __name__ == "__main__":
  testing.test_main()
