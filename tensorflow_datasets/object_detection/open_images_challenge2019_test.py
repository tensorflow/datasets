# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for open_images_challenge2019.py."""

import os

from tensorflow_datasets import testing
from tensorflow_datasets.object_detection import open_images_challenge2019

_BASE_EXAMPLE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "testing", "test_data", "fake_examples")

open_images_challenge2019._NUM_CLASSES = 6  # This is only done for testing!


class OpenImagesChallenge2019DetectionTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = open_images_challenge2019.OpenImagesChallenge2019Detection
  BUILDER_CONFIG_NAMES_TO_TEST = ["200k"]
  DL_DOWNLOAD_RESULT = {
      "train_images": ["train_%02d.zip" % i for i in range(9)],
      "test_images": ["test.zip"],
      "validation_images": ["validation.zip"],
      "train_image_label":
          "challenge-2019-train-detection-human-imagelabels.csv",
      "train_boxes":
          "challenge-2019-train-detection-bbox.csv",
      "validation_image_label":
          "validation-detection-human-imagelabels.csv",
      "validation_boxes":
          "validation-detection-bbox.csv",
      "classes":
          "challenge-2019-classes-description-500.csv",
      "hierarchy":
          "challenge-2019-label500-hierarchy.json",
  }
  EXAMPLE_DIR = os.path.join(
      _BASE_EXAMPLE_DIR, "open_images_challenge2019_detection")

  SPLITS = {  # Expected number of examples on each split.
      "train": 15,
      "test": 2,
      "validation": 3,
  }

if __name__ == "__main__":
  testing.test_main()
