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

"""Tests for dataset_collection_builder_testing."""
from tensorflow_datasets import testing
from tensorflow_datasets.testing import dataset_collection_builder_testing as dc_testing


def test_dc_test_base():
  class TestDummyCollection(dc_testing.DatasetCollectionTestBase):
    DATASET_COLLECTION_CLASS = testing.DummyDatasetCollection

  # Check defaults class attributes are set up correctly.
  assert TestDummyCollection.VERSION is None
  assert not TestDummyCollection.DATASETS_TO_TEST
  assert TestDummyCollection.CHECK_DATASETS_VERSION
