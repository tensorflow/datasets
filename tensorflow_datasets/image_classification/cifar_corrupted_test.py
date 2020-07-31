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

# Lint as: python3
"""Tests for corrupted Cifar10 and Cifar 100."""

from __future__ import absolute_import, division, print_function

from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import cifar_corrupted

class Cifar10CorruptedTest(testing.DatasetBuilderTestCase):

  BUILDER_CONFIG_NAMES_TO_TEST = [
      "elastic_1",
      "elastic_4",
      "elastic_5",
  ]

  DATASET_CLASS = cifar_corrupted.Cifar10Corrupted
  SPLITS = {
      "test": 10,
  }


class Cifar100CorruptedTest(testing.DatasetBuilderTestCase):

  BUILDER_CONFIG_NAMES_TO_TEST = [
      "elastic_1",
      "elastic_4",
      "elastic_5",
  ]

  DATASET_CLASS = cifar_corrupted.Cifar100Corrupted
  SPLITS = {
      "test": 10,
  }


if __name__ == "__main__":
  testing.test_main()
