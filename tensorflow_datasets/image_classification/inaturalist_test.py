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

"""Tests for INaturalist dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import inaturalist


class INaturalist2017Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = inaturalist.INaturalist2017
  SPLITS = {  # Expected number of examples on each split.
      "train": 4,
      "validation": 3,
      "test": 2,
  }
  DL_EXTRACT_RESULT = {
      "test_images": "test2017.tar.gz",
      "trainval_annos": "train_val2017",
      "trainval_images": "train_val_images.tar.gz",
  }


if __name__ == "__main__":
  testing.test_main()
