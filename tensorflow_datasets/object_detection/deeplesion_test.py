# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Tests for deeplesion dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets import testing
from tensorflow_datasets.object_detection import deeplesion


class DeeplesionTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = deeplesion.Deeplesion
  BUILDER_CONFIG_NAMES_TO_TEST = ["abnormal"]

  SPLITS = {
      "train": 2,
      "validation": 5,
      "test":2,
  }
  DL_EXTRACT_RESULT = {
      "zipfile01": "zipfile01.zip",  # Relative to fake_examples/my_dataset dir.
      "zipfile02": "zipfile02.zip",
      "zipfile03": "zipfile03.zip",
      'ann_file': "fake_DL_info.csv"
  }



if __name__ == "__main__":
  testing.test_main()

