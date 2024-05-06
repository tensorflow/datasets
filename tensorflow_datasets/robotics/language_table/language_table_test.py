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

"""language_table dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.robotics.language_table import language_table


class LanguageTableTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for language_table dataset."""
  DATASET_CLASS = language_table.LanguageTable
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['real']

  @classmethod
  def setUpClass(cls):
    language_table.LanguageTable._INPUT_FILE_PREFIX = cls.dummy_data
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()
