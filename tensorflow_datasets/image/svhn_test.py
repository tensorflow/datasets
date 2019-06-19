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

"""Tests for tfds.image.svhn."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.image import svhn


class SvhnTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = svhn.SvhnCropped
  SPLITS = {  # Number of examples.
      "train": 3,
      "test": 2,
      "extra": 1,
  }
  DL_EXTRACT_RESULT = {
      "train": "train_32x32.mat",
      "test": "test_32x32.mat",
      "extra": "extra_32x32.mat",
  }


class SvhnS3Test(SvhnTest):
  VERSION = "2.0.0"


if __name__ == "__main__":
  testing.test_main()
