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

"""Test for Reddit TIFU Dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.reddit_tifu import reddit_tifu_dataset_builder


class RedditTifuTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = reddit_tifu_dataset_builder.Builder
  SPLITS = {
      "train": 3,  # Number of fake train example
  }
  DL_EXTRACT_RESULT = "data.jsonl"
  BUILDER_CONFIG_NAMES_TO_TEST = ["short", "long"]


class RedditTifuSplitTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = reddit_tifu_dataset_builder.Builder
  SPLITS = {
      "train": 1,  # Number of fake train example
      "test": 1,  # Number of fake test example
      "validation": 1,  # Number of fake validation example
  }
  DL_EXTRACT_RESULT = {"data": "data.jsonl", "split": "split.json"}
  BUILDER_CONFIG_NAMES_TO_TEST = ["long_split"]


if __name__ == "__main__":
  testing.test_main()
