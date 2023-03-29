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

"""Tests for squad dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.squad import squad_dataset_builder


class SquadV1Test(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["v1.1"]
  DATASET_CLASS = squad_dataset_builder.Builder

  DL_EXTRACT_RESULT = {
      "train": "train-v1.1.json",
      "dev": "dev-v1.1.json",
  }

  SPLITS = {
      "train": 3,
      "validation": 2,
  }


class SquadV2Test(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["v2.0"]
  DATASET_CLASS = squad_dataset_builder.Builder

  DL_EXTRACT_RESULT = {
      "train": "train-v2.0.json",
      "dev": "dev-v2.0.json",
  }

  SPLITS = {
      "train": 3,
      "validation": 2,
  }


if __name__ == "__main__":
  testing.test_main()
