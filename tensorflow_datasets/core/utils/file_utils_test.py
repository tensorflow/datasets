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

"""Tests for file_utils."""

import os
from absl.testing import flagsaver
from etils import epath
from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils import read_config


def test_default_data_dir():
  data_dir = file_utils.get_default_data_dir(given_data_dir=None)
  assert data_dir
  assert isinstance(data_dir, str)


def test_is_version_folder(mock_fs: testing.MockFs):
  folder_with_version = '/a/b/1.2.3'
  mock_fs.add_file(
      path=os.path.join(folder_with_version, 'features.json'), content='1')
  assert file_utils.is_version_folder(folder_with_version)

  folder_without_version = '/c/d'
  mock_fs.add_file(
      path=os.path.join(folder_without_version, 'features.json'), content='1')
  assert not file_utils.is_version_folder(folder_without_version)


def test_list_dataset_variants_with_configs(mock_fs: testing.MockFs):
  data_dir = epath.Path('/a')
  dataset_dir = data_dir / 'ds'
  configs_and_versions = {
      'x': ['1.0.0', '1.0.1'],
      'y': ['2.0.0'],
  }
  for config, versions in configs_and_versions.items():
    for version in versions:
      mock_fs.add_file(
          dataset_dir / config / version / 'features.json', content='x')

  references = sorted(
      file_utils.list_dataset_variants(
          dataset_name='my_ds', dataset_dir=dataset_dir))
  assert references == [
      naming.DatasetReference(
          dataset_name='my_ds', config='x', version='1.0.0', data_dir=data_dir),
      naming.DatasetReference(
          dataset_name='my_ds', config='x', version='1.0.1', data_dir=data_dir),
      naming.DatasetReference(
          dataset_name='my_ds', config='y', version='2.0.0', data_dir=data_dir),
  ]


def test_list_dataset_variants_without_configs(mock_fs: testing.MockFs):
  dataset_dir = '/a/ds'
  versions = ['1.0.0', '1.0.1']
  for version in versions:
    mock_fs.add_file(
        os.path.join(dataset_dir, version, 'features.json'), content='x')

  references = sorted(
      file_utils.list_dataset_variants(
          dataset_name='my_ds', dataset_dir=epath.Path(dataset_dir)))
  data_dir = epath.Path('/a')
  assert references == [
      naming.DatasetReference(
          dataset_name='my_ds', version='1.0.0', data_dir=data_dir),
      naming.DatasetReference(
          dataset_name='my_ds', version='1.0.1', data_dir=data_dir),
  ]


def test_list_datasets_in_data_dir(mock_fs: testing.MockFs):
  data_dir = '/a'
  mock_fs.add_file(
      os.path.join(data_dir, 'ds1/config1/1.0.0/features.json'), content='x')
  mock_fs.add_file(
      os.path.join(data_dir, 'ds1/config1/2.0.0/features.json'), content='x')
  mock_fs.add_file(
      os.path.join(data_dir, 'ds1/config2/1.0.0/features.json'), content='x')
  mock_fs.add_file(
      os.path.join(data_dir, 'ds2/1.0.0/features.json'), content='x')

  # The following are problematic and should thus be ignored.
  mock_fs.add_file(
      os.path.join(data_dir, 'invalid-name/1.0.0/features.json'), content='x')
  mock_fs.add_file(
      os.path.join(data_dir, 'invalid_version1/1.a.b/features.json'),
      content='x')
  mock_fs.add_file(
      os.path.join(data_dir, 'invalid_version2/1.2.3.4/features.json'),
      content='x')

  references = sorted(
      file_utils.list_datasets_in_data_dir(data_dir=epath.Path(data_dir)))
  data_dir = epath.Path('/a')
  assert references == [
      naming.DatasetReference(
          dataset_name='ds1',
          config='config1',
          version='1.0.0',
          data_dir=data_dir),
      naming.DatasetReference(
          dataset_name='ds1',
          config='config1',
          version='2.0.0',
          data_dir=data_dir),
      naming.DatasetReference(
          dataset_name='ds1',
          config='config2',
          version='1.0.0',
          data_dir=data_dir),
      naming.DatasetReference(
          dataset_name='ds2', version='1.0.0', data_dir=data_dir),
  ]


def test_list_datasets_in_data_dir_with_namespace(mock_fs: testing.MockFs):
  data_dir = '/a'
  namespace = 'ns'
  mock_fs.add_file(
      os.path.join(data_dir, 'ds1/config1/1.0.0/features.json'), content='x')

  references = sorted(
      file_utils.list_datasets_in_data_dir(
          data_dir=epath.Path(data_dir),
          namespace=namespace,
          include_configs=True,
          include_versions=True))
  data_dir = epath.Path('/a')
  assert references == [
      naming.DatasetReference(
          dataset_name='ds1',
          namespace=namespace,
          config='config1',
          version='1.0.0',
          data_dir=data_dir),
  ]

if __name__ == '__main__':
  testing.test_main()
