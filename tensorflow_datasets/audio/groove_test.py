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

"""Tests for Groove dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.audio import groove


class GrooveFullTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = groove.Groove
  BUILDER_CONFIG_NAMES_TO_TEST = ["full-16000hz"]
  SPLITS = {
      "train": 2,
      "test": 1,
  }
  DL_EXTRACT_RESULT = ".."


class GrooveFullMidiOnlyTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = groove.Groove
  BUILDER_CONFIG_NAMES_TO_TEST = ["full-midionly"]
  SPLITS = {
      "train": 3,
      "test": 1,
  }
  DL_EXTRACT_RESULT = ".."


class Groove2BarTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = groove.Groove
  BUILDER_CONFIG_NAMES_TO_TEST = ["2bar-16000hz"]
  SPLITS = {
      "train": 5,  # 3, 2
      "test": 1,
  }
  DL_EXTRACT_RESULT = ".."


class Groove2BarMidiOnlyTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = groove.Groove
  BUILDER_CONFIG_NAMES_TO_TEST = ["2bar-midionly"]
  SPLITS = {
      "train": 6,  # 3, 2, 1
      "test": 1,
  }
  DL_EXTRACT_RESULT = ".."


if __name__ == "__main__":
  testing.test_main()
