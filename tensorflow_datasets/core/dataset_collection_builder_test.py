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

"""Tests for dataset_collection_builder."""
from unittest import mock

from etils import epath
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_collection_builder as dcb
from tensorflow_datasets.core.utils import version as version_lib


@mock.patch.object(dcb, 'get_filepath_in_dataset_folder', autospec=True)
def test_get_file_content_from_dataset_folder(mock_get_path):
  expected = 'Mocked file content'
  mock_path = mock.create_autospec(epath.Path)
  mock_path.read_text.return_value = expected
  mock_get_path.return_value = mock_path
  actual = dcb.get_file_content_from_dataset_folder(
      dataset_class=None, file_name='anything')
  mock_get_path.assert_called_once_with(None, 'anything')
  assert actual == expected


@mock.patch.object(dcb, 'get_filepath_in_dataset_folder', autospec=True)
def test_get_file_content_from_dataset_folder_raise_exception(mock_get_path):
  with pytest.raises(AttributeError):
    mock_get_path.return_value = FileNotFoundError
    dcb.get_file_content_from_dataset_folder(
        dataset_class=None, file_name=None, raise_error_if_fails=True)


@mock.patch.object(dcb, 'get_filepath_in_dataset_folder', autospec=True)
def test_get_file_content_from_dataset_folder_return_none(mock_get_path):
  mock_get_path.return_value = FileNotFoundError
  actual = dcb.get_file_content_from_dataset_folder(
      dataset_class=None, file_name=None)
  assert actual is None


def test_dataset_collection_info_from_cls():

  expected_description = 'description'
  dummy_dc_info = dcb.DatasetCollectionInfo.from_cls(
      dataset_collection_class=testing.DummyDatasetCollection,
      description=expected_description,
      release_notes={
          '1.0.0': 'Initial release',
      },
  )

  assert dummy_dc_info.name == 'dummy_dataset_collection'
  assert dummy_dc_info.description == expected_description
  assert dummy_dc_info.citation is None


def test_dataset_reference_from_tfds_name():
  actual = dcb.DatasetReference.from_tfds_name(
      'ds/config:1.2.3', split_mapping={'x': 'y'})
  expected = dcb.DatasetReference(
      dataset_name='ds',
      version='1.2.3',
      config='config',
      split_mapping={'x': 'y'})
  assert actual == expected


def test_dataset_reference_tfds_name():
  reference = dcb.DatasetReference(
      dataset_name='ds', version='1.2.3', config='config')
  assert reference.tfds_name() == 'ds/config:1.2.3'


def test_dataset_reference_get_split():
  reference = dcb.DatasetReference.from_tfds_name(
      'ds/config:1.2.3', split_mapping={'x': 'y'})
  assert reference.get_split('x') == 'y'
  assert reference.get_split('y') == 'y'
  assert reference.get_split('z') == 'z'


def test_references_for():
  expected = {
      'one':
          dcb.DatasetReference(
              dataset_name='ds1', version='1.2.3', config='config'),
      'two':
          dcb.DatasetReference(dataset_name='ds2', version='1.0.0')
  }
  assert dcb.references_for({
      'one': 'ds1/config:1.2.3',
      'two': 'ds2:1.0.0'
  }) == expected


def test_reference_for():
  expected = dcb.DatasetReference(
      dataset_name='ds', version='1.2.3', config='config')
  assert dcb.reference_for('ds/config:1.2.3') == expected


@pytest.fixture(name='dummy_dc', scope='session')
def fixture_dummy_dc():
  return testing.DummyDatasetCollection()


def test_all_versions(dummy_dc):
  assert set(dummy_dc.all_versions) == {
      version_lib.Version('1.0.0'),
      version_lib.Version('1.1.0'),
      version_lib.Version('2.0.0')
  }


def test_get_latest_version(dummy_dc):
  assert dummy_dc.get_latest_version() == '2.0.0'


def test_get_collection(dummy_dc):
  assert sorted(dummy_dc.get_collection().keys()) == ['a', 'b', 'c']
  assert sorted(
      dummy_dc.get_collection(version='2.0.0').keys()) == ['a', 'b', 'c']
  assert sorted(dummy_dc.get_collection(version='1.0.0').keys()) == ['a', 'b']


def test_get_collection_with_wildcards(dummy_dc):
  assert sorted(dummy_dc.get_collection(version='1.0.*').keys()) == ['a', 'b']
  assert sorted(dummy_dc.get_collection(version='1.*.*').keys()) == ['a', 'c']


def test_get_nonexistent_collection(dummy_dc):
  with pytest.raises(ValueError):
    dummy_dc.get_collection(version='1.2.0')
    dummy_dc.get_collection(version='1.*.2')
