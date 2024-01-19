# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Tests for Quickdraw data."""
from tensorflow_datasets import testing
from tensorflow_datasets.datasets.quickdraw_bitmap import quickdraw_bitmap_dataset_builder


class QuickdrawTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = quickdraw_bitmap_dataset_builder.Builder
  SPLITS = {
      "train": 9,
  }
  DL_EXTRACT_RESULT = {
      "airplane": "airplane.npy",
      "ambulance": "ambulance.npy",
      "angel": "angel.npy",
  }


if __name__ == "__main__":
  testing.test_main()
