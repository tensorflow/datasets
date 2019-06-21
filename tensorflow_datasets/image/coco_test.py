# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Tests for coco dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets as tfds

from tensorflow_datasets import testing
from tensorflow_datasets.image import coco


class Coco2014Test(testing.DatasetBuilderTestCase):

  DATASET_CLASS = coco.Coco2014

  SPLITS = {
      tfds.Split.TRAIN: 5,
      tfds.Split.VALIDATION: 2,
      tfds.Split.TEST: 2,
      "test2015": 2,
  }

  DL_EXTRACT_RESULT = {
      "train_images": "train_images",
      "val_images": "val_images",
      "trainval_annotations": "trainval_annotations",
      "test_images": "test_images",
      "test_annotations": "test_annotations",
      "test2015_images": "test2015_images",
      "test2015_annotations": "test2015_annotations",
  }


class Coco2014S3Test(Coco2014Test):
  VERSION = "2.0.0"


if __name__ == "__main__":
  testing.test_main()
