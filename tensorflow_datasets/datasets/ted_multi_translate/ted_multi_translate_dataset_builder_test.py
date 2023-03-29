# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Tests for the translate TED Talk module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.ted_multi_translate import ted_multi_translate_dataset_builder


class TedMultiTranslateTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = ted_multi_translate_dataset_builder.Builder
  SPLITS = {  # Expected number of examples on each split from fake example.
      "train": 4,
      "validation": 4,
      "test": 4,
  }
  DL_EXTRACT_RESULT = ""


if __name__ == "__main__":
  testing.test_main()
