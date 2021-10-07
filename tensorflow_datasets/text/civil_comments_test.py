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

"""Tests for CivilComments from Jigsaw Unintended Bias Kaggle Competition."""

from tensorflow_datasets import testing
from tensorflow_datasets.text import civil_comments


class CivilCommentsNoCovertTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = civil_comments.CivilComments
  BUILDER_CONFIG_NAMES_TO_TEST = ["CivilComments", "CivilCommentsIdentities"]
  SPLITS = {
      "train": 2,  # Number of fake train examples
      "test": 1,  # Number of fake test examples
      "validation": 1,  # Number of fake validation examples
  }


# Separate test for CivilCommentsCovert without validation split.
class CivilCommentsCovertTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = civil_comments.CivilComments
  BUILDER_CONFIG_NAMES_TO_TEST = ["CivilCommentsCovert"]
  SPLITS = {
      "train": 2,  # Number of fake train examples
      "test": 1,  # Number of fake test examples
  }


if __name__ == "__main__":
  testing.test_main()
