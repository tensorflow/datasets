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

"""race dataset."""

from tensorflow_datasets.datasets.race import race_dataset_builder
import tensorflow_datasets.public_api as tfds


class RaceTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for race dataset."""

  DATASET_CLASS = race_dataset_builder.Builder
  BUILDER_CONFIG_NAMES_TO_TEST = ["high"]
  SPLITS = {
      "train": 1,  # Number of fake train example
      "test": 1,  # Number of fake test example
      "dev": 1,  # Number of fake dev example
  }


if __name__ == "__main__":
  tfds.testing.test_main()
