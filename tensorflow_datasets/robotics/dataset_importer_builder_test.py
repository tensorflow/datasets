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

"""Tests for rds_importer_builder dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.robotics import dataset_importer_builder


class MockRDSDataset(dataset_importer_builder.DatasetImporterBuilder):
  """DatasetBuilder for mock `bridge` dataset."""

  def get_description(self):
    return 'tbd'

  def get_citation(self):
    return 'tbd'

  def get_homepage(self):
    return 'tbd'

  def get_relative_dataset_location(self):
    return 'bridge/1.0.0'


class MockRDSDatasetTestRlds(tfds.testing.DatasetBuilderTestCase):
  """Tests for an rds dataset."""

  DATASET_CLASS = MockRDSDataset
  SPLITS = {'train': 1}

  SKIP_TF1_GRAPH_MODE = True

  @classmethod
  def setUpClass(cls):
    MockRDSDataset._GCS_BUCKET = cls.dummy_data
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()
