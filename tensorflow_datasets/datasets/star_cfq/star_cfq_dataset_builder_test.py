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

"""Tests for CFQ dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.star_cfq import star_cfq_dataset_builder


class StarCFQRandomSplitTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = star_cfq_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = [
      "single_pool_10x_b_cfq",
      "equal_weighting_1x_b_cfq_1x_x_cfq",
  ]
  SPLITS = {
      "train": 2,
      "test": 1,
  }


class StarCFQCompoundDivergenceSplitTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = star_cfq_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ["u_cfq_compound_divergence_0.333333_0.3_r4"]
  SPLITS = {
      "train": 2,
      "validation": 1,
      "test": 1,
  }


if __name__ == "__main__":
  testing.test_main()
