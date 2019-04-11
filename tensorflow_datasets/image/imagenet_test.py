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

"""Tests for imagenet dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tensorflow_datasets import testing
from tensorflow_datasets.image import imagenet


class Imagenet2012Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagenet.Imagenet2012
  SPLITS = {  # Expected number of examples on each split.
      "train": 100,
      "validation": 10,
  }
  DL_EXTRACT_RESULT = [
      "ILSVRC2012_img_train.tar",
      "ILSVRC2012_img_val.tar",
  ]


if __name__ == "__main__":
  testing.test_main()
