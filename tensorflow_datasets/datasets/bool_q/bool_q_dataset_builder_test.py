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

"""bool_q dataset."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.bool_q import bool_q_dataset_builder


class PawsXWikiTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = bool_q_dataset_builder.Builder
  SPLITS = {
      "train": 2,  # Number of fake train examples
      "validation": 2,  # Number of fake validation examples
  }
  DL_EXTRACT_RESULT = {
      "train": "train.jsonl",
      "validation": "dev.jsonl",
  }


if __name__ == "__main__":
  testing.test_main()
