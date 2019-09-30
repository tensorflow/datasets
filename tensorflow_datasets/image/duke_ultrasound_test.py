"""DAS beamformed phantom images and paired clinical post-processed images test."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image import duke_ultrasound


class DukeUltrasoundTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = duke_ultrasound.DukeUltrasound
  OVERLAPPING_SPLITS = ['A', 'B', 'TRAIN']

  SPLITS = {
    "train": 1,
    "test": 1,
    "validation": 1,
    "MARK": 1,
    "A": 1,
    "B": 1
  }

  DL_EXTRACT_RESULT = {
    "mark_data": "data",
    "phantom_data": "data",
    "train": "train.csv",
    "test": "test.csv",
    "validation": "validation.csv",
    "A": "train.csv",
    "B": "train.csv",
    "MARK": "mark.csv"
  }

if __name__ == "__main__":
  testing.test_main()
