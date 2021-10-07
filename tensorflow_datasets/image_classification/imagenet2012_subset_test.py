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

"""Tests for imagenet2012_subset dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import imagenet2012_subset

imagenet2012_subset.Imagenet2012Subset.PNG_IMAGES = ["n01440764_1.JPEG"]
imagenet2012_subset.Imagenet2012Subset.CMYK_IMAGES = [
    "n01440764_2.JPEG",
    "n01440764_3.JPEG",
]


class Imagenet2012SubsetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = imagenet2012_subset.Imagenet2012Subset
  BUILDER_CONFIG_NAMES_TO_TEST = ["1pct"]
  SPLITS = {  # Expected number of examples on each split.
      "train": 1,
      "validation": 10,
  }
  DL_EXTRACT_RESULT = [
      "1percent.txt",
      "ILSVRC2012_img_train.tar",
      "ILSVRC2012_img_val.tar",
  ]


if __name__ == "__main__":
  testing.test_main()
