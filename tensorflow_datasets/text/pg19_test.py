# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Test for PG-19 dataset module."""

import os

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import pg19


class Pg19Test(tfds.testing.DatasetBuilderTestCase):

  @classmethod
  def setUpClass(cls):
    super(Pg19Test, cls).setUpClass()
    pg19._DATA_DIR = os.path.join(
        os.path.normpath(os.path.dirname(__file__) + "/../"),
        "testing",
        "test_data",
        "fake_examples",
        "pg19",
    )

  DATASET_CLASS = pg19.Pg19
  SPLITS = {
      "train": 3,  # Number of fake train example
      "test": 1,  # Number of fake test example
      "validation": 1  # Number of fake validation example
  }


if __name__ == "__main__":
  tfds.testing.test_main()
