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
"""Test for PG-19 dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import pg19


class Pg19Test(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = pg19.Pg19
  SPLITS = {
      "train": 3,       # Number of fake train example
      "test": 1,        # Number of fake test example
      "validation": 1   # Number of fake validation example
  }

  DL_EXTRACT_RESULT = {
      "metadata": "metadata.csv",
      "train": ["121122.txt", "121222.txt", "121322.txt"],
      "val": ["121422.txt"],
      "test": ["121522.txt"]
  }

if __name__ == "__main__":
  tfds.testing.test_main()
