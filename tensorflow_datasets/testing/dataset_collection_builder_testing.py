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

"""Base DatasetCollectionTestCase to test a DatasetCollection."""
import typing
from typing import List, Optional, Type

import pytest

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_collection_builder
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered


class DatasetCollectionTestBase:
  """Inherit this class to test your DatasetCollection class.

  You must set the following class attribute:
    * DATASET_COLLECTION_CLASS: class object of DatasetCollection to test.

  You may set the following class attribute:
    * VERSION: The version of the DatasetCollection used to run the test.
      Defaults to None (latest version).
    * DATASETS_TO_TEST: List containing the datasets to test existence for. If
      no dataset is specified, the existence of all datasets in the collection
      will be tested.
    * CHECK_DATASETS_VERSION: Whether to check for the existence of the
      versioned datasets in the dataset collection, or for their default
      versions. Defaults to True.

  This test case will check for the following:
  - The dataset collection is correctly registered, i.e.
    `tfds.dataset_collection` works.
  - The datasets in the dataset collection exist, i.e. their builder is
    registered in tfds. If DATASETS_TO_TEST is not specified, all datasets in
    the collection will be checked.
  """

  DATASET_COLLECTION_CLASS = None
  VERSION: Optional[str] = None
  DATASETS_TO_TEST: List[str] = []
  CHECK_DATASETS_VERSION: bool = True

  @pytest.fixture(autouse=True)
  def dataset_collection(self):
    dataset_collection_cls = registered.imported_dataset_collection_cls(
        self.DATASET_COLLECTION_CLASS.name
    )
    dataset_collection_cls = typing.cast(
        Type[dataset_collection_builder.DatasetCollection],
        dataset_collection_cls,
    )
    yield dataset_collection_cls()

  @pytest.fixture(autouse=True)
  def datasets(self, dataset_collection):
    yield dataset_collection.get_collection(self.VERSION)

  def test_dataset_collection_is_registered(self, dataset_collection):
    """Checks that the dataset collection is registered."""
    assert registered.is_dataset_collection(dataset_collection.info.name)

  def test_dataset_collection_info(self, dataset_collection):
    """Checks that the collection's info is of type `DatasetCollectionInfo`."""
    assert isinstance(
        dataset_collection.info,
        dataset_collection_builder.DatasetCollectionInfo,
    )
    assert dataset_collection.info.name
    assert dataset_collection.info.description
    assert dataset_collection.info.release_notes

  def _get_dataset_builder(
      self, ds_reference: naming.DatasetReference, check_ds_version: bool = True
  ) -> dataset_builder.DatasetBuilder:
    """Returns the dataset builder for the requested dataset.

    Args:
      ds_reference: The `DatasetReference` containing the information about the
        dataset whose builder is to return.
      check_ds_version: Whether to return the dataset builder relative to a
        specific version of the dataset. If set to False, it will return the
        dataset builder for the latest version. Default is True.

    Returns:
      The dataset_builder.DatasetBuilder for the requested dataset.
    """
    cls = registered.imported_builder_cls(ds_reference.dataset_name)
    cls = typing.cast(Type[dataset_builder.DatasetBuilder], cls)
    version = ds_reference.version if check_ds_version else None
    return cls(config=ds_reference.config, version=version)

  def test_all_datasets_exist(self, datasets):
    """Checks that all the collection's datasets have a valid builder."""
    # If DATASETS_TO_TEST defined, restrict the scope of the datasets to test.
    if self.DATASETS_TO_TEST:
      datasets_to_test = {ds: datasets[ds] for ds in self.DATASETS_TO_TEST}
    else:
      datasets_to_test = datasets

    for ds, ds_reference in datasets_to_test.items():
      ds_builder = self._get_dataset_builder(
          ds_reference, check_ds_version=self.CHECK_DATASETS_VERSION
      )
      assert isinstance(ds_builder, dataset_builder.DatasetBuilder)
