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

"""Tests for tedlium dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.audio import tedlium
import tensorflow_datasets.public_api as tfds


class TedliumTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = tedlium.Tedlium
  BUILDER_CONFIG_NAMES_TO_TEST = ["release1"]
  SPLITS = {
      tfds.Split.TRAIN: 4,
      tfds.Split.TEST: 1,
      tfds.Split.VALIDATION: 1,
  }


if __name__ == "__main__":
  testing.test_main()
