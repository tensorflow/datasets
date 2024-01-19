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

"""Nsynth Dataset Builder test."""

from tensorflow_datasets.datasets.nsynth import nsynth_dataset_builder
import tensorflow_datasets.testing as tfds_test


class NsynthFullTest(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = nsynth_dataset_builder.Builder
  # Make test run faster by using fewer output shards.
  nsynth_dataset_builder._SPLIT_SHARDS = {
      "train": 1,
      "valid": 1,
      "test": 1,
  }
  BUILDER_CONFIG_NAMES_TO_TEST = ["full"]
  SPLITS = {"train": 3, "test": 3, "valid": 3}
  DL_EXTRACT_RESULT = {
      "examples": {
          "train": "train",
          "test": "test",
          "valid": "valid",
      },
      "instrument_labels": "nsynth-instrument_labels.txt",
  }


class GANsynthTest(NsynthFullTest):
  BUILDER_CONFIG_NAMES_TO_TEST = ["gansynth_subset"]
  SPLITS = {"train": 2, "test": 1, "valid": 1}
  DL_EXTRACT_RESULT = dict(NsynthFullTest.DL_EXTRACT_RESULT)
  DL_EXTRACT_RESULT["gansynth_splits"] = "gansynth_splits.csv"


class GANsynthWithF0AndLoudnessTest(GANsynthTest):
  MOCK_OUT_FORBIDDEN_OS_FUNCTIONS = False
  BUILDER_CONFIG_NAMES_TO_TEST = ["gansynth_subset.f0_and_loudness"]


if __name__ == "__main__":
  tfds_test.test_main()
