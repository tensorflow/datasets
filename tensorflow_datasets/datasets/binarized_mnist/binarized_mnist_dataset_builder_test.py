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

"""Tests for binarized_mnist dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.binarized_mnist import binarized_mnist_dataset_builder

# testing/binarized_mnist.py generates fake input data


class MNISTTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = binarized_mnist_dataset_builder.Builder
  SPLITS = {
      "train": 10,
      "validation": 2,
      "test": 2,
  }
  DL_EXTRACT_RESULT = {
      "train_data": binarized_mnist_dataset_builder._TRAIN_DATA_FILENAME,
      "validation_data": binarized_mnist_dataset_builder._VALID_DATA_FILENAME,
      "test_data": binarized_mnist_dataset_builder._TEST_DATA_FILENAME,
  }


if __name__ == "__main__":
  testing.test_main()
