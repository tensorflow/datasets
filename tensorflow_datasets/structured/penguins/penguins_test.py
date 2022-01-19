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

"""Unit tests for penguins dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.penguins import penguins


class PenguinsSimpleTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for penguins dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['simple']
  DATASET_CLASS = penguins.Penguins
  SPLITS = {'train': 4}
  DL_EXTRACT_RESULT = 'simple.csv'


class PenguinsRawTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for penguins/raw dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['raw']
  DATASET_CLASS = penguins.Penguins
  SPLITS = {'train': 6}
  DL_EXTRACT_RESULT = 'raw.csv'


class PenguinsProcessedTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for penguins/raw dataset."""
  BUILDER_CONFIG_NAMES_TO_TEST = ['processed']
  DATASET_CLASS = penguins.Penguins
  SPLITS = {'train': 3}
  DL_EXTRACT_RESULT = 'processed.csv'


if __name__ == '__main__':
  tfds.testing.test_main()
