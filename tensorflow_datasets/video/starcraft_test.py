# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.testing import dataset_builder_testing
from tensorflow_datasets.video import starcraft


class StarcraftVideoDatasetTest(dataset_builder_testing.TestCase):
  DATASET_CLASS = starcraft.StarcraftVideoBrawl64

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


if __name__ == "__main__":
  dataset_builder_testing.main()
