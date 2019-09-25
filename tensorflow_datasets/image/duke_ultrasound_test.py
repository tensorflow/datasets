"""DAS beamformed phantom images and paired clinical post-processed images test."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import duke_ultrasound


class DukeUltrasoundTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = duke_ultrasound.DukeUltrasound
  SPLITS = {
    "train": 1,
    "test": 1,
    "validation": 1,
    "invivo": 1
  }

  DL_EXTRACT_RESULT = {
    "data": "data",
    "train": "train.csv",
    "test": "test.csv",
    "validation": "validation.csv",
    "invivo": "invivo.csv"
  }

if __name__ == "__main__":
  testing.test_main()
