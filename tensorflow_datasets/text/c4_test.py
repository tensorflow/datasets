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

"""Tests for c4 dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.text import c4


class C4Test(testing.DatasetBuilderTestCase):
  DATASET_CLASS = c4.C4
  BUILDER_CONFIG_NAMES_TO_TEST = ["en"]

  DL_EXTRACT_RESULT = {
      "wet_path_urls": ["wet_urls.txt"],
      "wet_files": ["cc_0.warc.wet.gz", "cc_1.warc.wet.gz"],
      "badwords": {"en": "badwords.txt"},
  }
  SPLITS = {
      "train": 2,
      "validation": 2,
  }


class C4NoCleanTest(C4Test):
  BUILDER_CONFIG_NAMES_TO_TEST = ["en.noclean"]
  SPLITS = {
      "train": 4,
      "validation": 2,
  }


class C4MultilingualTest(C4Test):
  BUILDER_CONFIG_NAMES_TO_TEST = ["multilingual"]
  for config in c4.C4.BUILDER_CONFIGS:
    if config.name == "multilingual":
      config.languages = ["en", "de"]

  SPLITS = {
      "en": 1,
      "en-validation": 1,
      "de": 1,
      "de-validation": 1,
      "und": 1,
      "und-validation": 1,
  }

if __name__ == "__main__":
  testing.test_main()
