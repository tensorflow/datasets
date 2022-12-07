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

"""Tests for imagenet dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.imagenet2012 import imagenet2012_dataset_builder

imagenet2012_dataset_builder.PNG_IMAGES = ["n01440764_1.JPEG"]
imagenet2012_dataset_builder.CMYK_IMAGES = [
    "n01440764_2.JPEG",
    "n01440764_3.JPEG",
]


class Imagenet2012Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagenet2012_dataset_builder.Builder
  SPLITS = {  # Expected number of examples on each split.
      "train": 100,
      "validation": 10,
      "test": 5,
  }
  DL_EXTRACT_RESULT = [
      "ILSVRC2012_img_train.tar",
      "ILSVRC2012_img_val.tar",
      "ILSVRC2012_img_test.tar",
  ]


if __name__ == "__main__":
  testing.test_main()
