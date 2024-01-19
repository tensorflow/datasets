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

"""Wine Quality dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.structured.wine_quality import wine_quality


class WineQualityWhiteTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["white"]
  DATASET_CLASS = wine_quality.WineQuality

  SPLITS = {
      "train": 2,
  }
  DL_EXTRACT_RESULT = {"train": "winequality-white.csv"}


class WineQualityRedTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["red"]
  DATASET_CLASS = wine_quality.WineQuality

  SPLITS = {
      "train": 2,
  }
  DL_EXTRACT_RESULT = {"train": "winequality-red.csv"}


if __name__ == "__main__":
  testing.test_main()
