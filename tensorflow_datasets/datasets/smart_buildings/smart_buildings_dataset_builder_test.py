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

"""smart_buildings_dataset dataset."""

from tensorflow_datasets.datasets.smart_buildings import smart_buildings_dataset_builder
import tensorflow_datasets.public_api as tfds


class SmartBuildingsDatasetTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for smart_buildings_dataset dataset."""

  DATASET_CLASS = smart_buildings_dataset_builder.Builder
  SPLITS = {
      'sb1_19': 12,  # Number of fake train examples
      'sb1_20': 12,  # Number of fake train examples
      'sb1_21': 12,  # Number of fake train examples
      'sb1_22': 12,  # Number of fake train examples
      'sb1_23': 12,  # Number of fake train examples
      'sb1_24': 12,  # Number of fake train examples
  }

  DL_EXTRACT_RESULT = {
      19: '',
      20: '',
      21: '',
      22: '',
      23: '',
      24: '',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
