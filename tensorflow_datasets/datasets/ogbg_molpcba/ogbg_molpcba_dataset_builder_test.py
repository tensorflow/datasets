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

"""ogbg_molpcba dataset tests."""

from tensorflow_datasets.datasets.ogbg_molpcba import ogbg_molpcba_dataset_builder
import tensorflow_datasets.public_api as tfds


class OgbgMolpcbaTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for ogbg_molpcba dataset."""

  # TODO(ameyasd): Add reasonable tests.
  DATASET_CLASS = ogbg_molpcba_dataset_builder.Builder
  SPLITS = {
      'train': 4,  # Number of fake train examples.
      'validation': 4,  # Number of fake validation examples.
      'test': 4,  # Number of fake test examples.
  }


if __name__ == '__main__':
  tfds.testing.test_main()
