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

"""Tests for libritts dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.libritts import libritts_dataset_builder


class LibriTTSTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = libritts_dataset_builder.Builder
  SPLITS = {
      "train_clean100": 2,
      "train_clean360": 2,
      "train_other500": 2,
      "test_clean": 2,
      "test_other": 2,
      "dev_clean": 2,
      "dev_other": 2,
  }
  DL_DOWNLOAD_RESULT = {
      "train_clean100": "train-clean-100.tar.gz",
      "train_clean360": "train-clean-360.tar.gz",
      "train_other500": "train-other-500.tar.gz",
      "test_clean": "test-clean.tar.gz",
      "test_other": "test-other.tar.gz",
      "dev_clean": "dev-clean.tar.gz",
      "dev_other": "dev-other.tar.gz",
  }


if __name__ == "__main__":
  testing.test_main()
