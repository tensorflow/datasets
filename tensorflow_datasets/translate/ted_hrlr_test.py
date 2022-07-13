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

"""Tests for the bilingual translate TED Talk module."""

from tensorflow_datasets import testing
from tensorflow_datasets.translate import ted_hrlr


class TedHrlrTranslateTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = ted_hrlr.TedHrlrTranslate
  BUILDER_CONFIG_NAMES_TO_TEST = ["az_to_en", "aztr_to_en"]
  SPLITS = {
      "train": 4,
      "validation": 4,
      "test": 4,
  }


if __name__ == "__main__":
  testing.test_main()
