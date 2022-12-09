# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for mnist dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.kmnist import kmnist_dataset_builder

# testing/mnist.py generates fake input data

mnist._TRAIN_EXAMPLES = 10  # pylint: disable=protected-access
mnist._TEST_EXAMPLES = 2  # pylint: disable=protected-access


class MNISTTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = kmnist_dataset_builder.Builder
  SPLITS = {
      "train": 10,
      "test": 2,
  }
  DL_EXTRACT_RESULT = {
      "train_data": "train-image",
      "train_labels": "train-label",
      "test_data": "test-image",
      "test_labels": "test-label",
  }


class FashionMNISTTest(MNISTTest):
  DATASET_CLASS = kmnist_dataset_builder.Builder


class KMNISTTest(MNISTTest):
  DATASET_CLASS = kmnist_dataset_builder.Builder


mnist.EMNIST.BUILDER_CONFIGS.extend([
    mnist.EMNISTConfig(
        name="test",
        class_number=200,
        train_examples=10,
        test_examples=2,
        description="EMNIST test data config.",
    ),
])


class EMNISTTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = kmnist_dataset_builder.Builder
  SPLITS = {
      "train": 10,
      "test": 2,
  }
  BUILDER_CONFIG_NAMES_TO_TEST = ["test"]


if __name__ == "__main__":
  testing.test_main()
