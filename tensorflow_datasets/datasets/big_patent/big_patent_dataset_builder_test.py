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

"""Test for BigPatent dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.big_patent import big_patent_dataset_builder


class BigPatentTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = big_patent_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ["all"]
  SPLITS = {
      "train": 9,  # Number of fake train example
      "validation": 9,  # Number of fake val example
      "test": 9,  # Number of fake test example
  }


class BigPatentATest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = big_patent_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ["a", "y"]
  SPLITS = {
      "train": 1,  # Number of fake train example
      "validation": 1,  # Number of fake val example
      "test": 1,  # Number of fake test example
  }


if __name__ == "__main__":
  testing.test_main()
