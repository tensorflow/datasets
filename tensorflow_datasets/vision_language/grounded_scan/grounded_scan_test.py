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

"""Grounded Scan dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.vision_language.grounded_scan import grounded_scan


class GroundedScanTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for grounded_scan dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = ["target_length_split"]
  DATASET_CLASS = grounded_scan.GroundedScan

  SPLITS = {
      "train": 1,
      "dev": 1,
      "test": 1,
      "target_lengths": 1,
  }


if __name__ == "__main__":
  tfds.testing.test_main()
