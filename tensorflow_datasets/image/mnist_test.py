# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.image import mnist
from tensorflow_datasets.testing import dataset_builder_testing


# testing/mnist.py generates fake input data

mnist._TRAIN_EXAMPLES = 10
mnist._TEST_EXAMPLES = 2


class MNISTTest(dataset_builder_testing.TestCase):
  DATASET_CLASS = mnist.MNIST
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
  DATASET_CLASS = mnist.FashionMNIST


if __name__ == "__main__":
  dataset_builder_testing.main()
