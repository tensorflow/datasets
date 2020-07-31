# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""Tests for starcraft video dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.video import starcraft


class StarcraftVideoDatasetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = starcraft.StarcraftVideo
  BUILDER_CONFIG_NAMES_TO_TEST = ["brawl_64"]

  DL_EXTRACT_RESULT = {
      "valid": "valid.tfrecords",
      "test": "test.tfrecords",
      "train_0": "train_0.tfrecords",
      "train_1": "train_1.tfrecords"
  }

  SPLITS = {
      "train": 2,
      "test": 1,
      "validation": 1,
  }


class StarcraftVideoDataset128Test(testing.DatasetBuilderTestCase):
  """Separate test to cover the 128x128 resolution videos."""
  DATASET_CLASS = starcraft.StarcraftVideo
  BUILDER_CONFIG_NAMES_TO_TEST = ["brawl_128"]

  DL_EXTRACT_RESULT = {
      "valid": "128_valid.tfrecords",
      "test": "128_test.tfrecords",
      "train_0": "128_train_0.tfrecords",
      "train_1": "128_train_1.tfrecords"
  }

  SPLITS = {
      "train": 2,
      "test": 1,
      "validation": 1,
  }


if __name__ == "__main__":
  testing.test_main()
