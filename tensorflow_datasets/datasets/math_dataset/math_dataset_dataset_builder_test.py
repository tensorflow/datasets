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

"""Tests for Mathematical dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.math_dataset import math_dataset_dataset_builder


class MathDatasetTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = math_dataset_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ["algebra__linear_1d"]
  SPLITS = {
      "train": 6,  # Number of fake train example pairs
      "test": 6,  # Number of fake test example pairs
  }


if __name__ == "__main__":
  testing.test_main()
