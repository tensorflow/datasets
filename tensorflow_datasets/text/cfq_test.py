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

"""Tests for CFQ dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.text import cfq


class CFQTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = cfq.CFQ
  BUILDER_CONFIG_NAMES_TO_TEST = ["mcd1"]
  SPLITS = {
      "train": 2,  # Number of fake train example
      "test": 1,  # Number of fake test example
      "validation": 1,  # Number of fake validation example
  }


if __name__ == "__main__":
  testing.test_main()
