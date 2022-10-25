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

"""Tests for CLEVR dataset module."""
from tensorflow_datasets import testing
from tensorflow_datasets.datasets.clevr import clevr_dataset_builder


class CLEVRTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = clevr_dataset_builder.Builder
  SPLITS = {  # Expected number of examples on each split.
      "train": 5,
      "validation": 5,
      "test": 5,
  }


if __name__ == "__main__":
  testing.test_main()
