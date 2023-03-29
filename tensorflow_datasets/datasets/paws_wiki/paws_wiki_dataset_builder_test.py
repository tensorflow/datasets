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

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.paws_wiki import paws_wiki_dataset_builder


class PawsWikiLabeldFinalTokenizedTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["labeled_final_tokenized"]
  DATASET_CLASS = paws_wiki_dataset_builder.Builder
  SPLITS = {
      "train": 2,  # Number of fake train examples
      "validation": 2,  # Number of fake validation examples
      "test": 3,  # Number of fake test examples
  }
  DL_EXTRACT_RESULT = {"labeled_final": ""}


class PawsWikiLabeledSwapRawTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["labeled_swap_raw"]
  DATASET_CLASS = paws_wiki_dataset_builder.Builder
  SPLITS = {
      "train": 2,  # Number of fake train examples
  }
  DL_EXTRACT_RESULT = {"labeled_swap": "", "raw_and_mapping": ""}


if __name__ == "__main__":
  testing.test_main()
