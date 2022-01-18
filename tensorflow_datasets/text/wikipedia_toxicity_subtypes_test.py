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

"""Tests for WikipediaToxicitySubtypes dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text import wikipedia_toxicity_subtypes


class WikipediaToxicitySubtypesTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = wikipedia_toxicity_subtypes.WikipediaToxicitySubtypes
  BUILDER_CONFIG_NAMES_TO_TEST = ["EnglishSubtypes"]
  SPLITS = {
      "train": 3,  # Number of fake train examples
      "test": 1,  # Number of fake test examples
  }


class WikipediaToxicityMultilingualTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = wikipedia_toxicity_subtypes.WikipediaToxicitySubtypes
  BUILDER_CONFIG_NAMES_TO_TEST = ["Multilingual"]
  SPLITS = {
      "validation": 2,  # Number of fake validation examples
      "test": 2,  # Number of fake test examples
  }


if __name__ == "__main__":
  tfds.testing.test_main()
