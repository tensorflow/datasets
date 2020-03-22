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
"""Tests for tensorflow_datasets.structured.breast_cancer."""

from tensorflow_datasets import testing
from tensorflow_datasets.structured import breast_cancer


class BreastCancerTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = breast_cancer.BreastCancer

  SPLITS = {
      "train": 13,
  }
  DL_EXTRACT_RESULT = "breast-cancer-wisconsin.data"


if __name__ == "__main__":
  testing.test_main()
