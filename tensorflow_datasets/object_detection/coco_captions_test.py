# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for coco captions dataset module."""

import os

from tensorflow_datasets import testing
from tensorflow_datasets.object_detection import coco_captions

_BASE_EXAMPLE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "testing", "test_data",
    "fake_examples")


class CocoCaptionsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = coco_captions.CocoCaptions
  BUILDER_CONFIG_NAMES_TO_TEST = ["2014"]
  EXAMPLE_DIR = os.path.join(_BASE_EXAMPLE_DIR, "coco")
  SPLITS = {
      "train": 5,
      "val": 1,
      "test": 1,
      "restval": 1,
  }
  DL_EXTRACT_RESULT = {
      "train_images": "train_images",
      "train_annotations": "trainval_annotations",
      "validation_images": "val_images",
      "validation_annotations": "trainval_annotations",
      "test_images": "test_images",
      "test_annotations": "test_annotations",
      "test2015_images": "test2015_images",
      "test2015_annotations": "test2015_annotations",
      "karpathy_and_li_splits": "karpathy_and_li_splits"
  }


if __name__ == "__main__":
  testing.test_main()
