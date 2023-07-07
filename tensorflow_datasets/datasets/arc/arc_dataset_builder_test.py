# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for the ARC dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.arc import arc_dataset_builder


class ArcTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = arc_dataset_builder.Builder
  SPLITS = {
      "train": 10,  # Number of fake train example
      "test": 5,  # Number of fake test example
  }


if __name__ == "__main__":
  testing.test_main()
