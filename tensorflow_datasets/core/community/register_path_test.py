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

"""Tests for tensorflow_datasets.core.community.register_path."""

from etils import epath
from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.community import register_path


def test_data_dir_register():
  register = register_path.DataDirRegister(
      namespace_to_data_dirs={'ns1': [epath.Path('/path/ns1')]}
  )
  assert {'ns1'} == register.namespaces


def test_list_dataset_references(mock_fs: testing.MockFs):
  path = '/path/ns1'
  mock_fs.add_file(path=f'{path}/ds1/1.0.0/dataset_info.json')
  mock_fs.add_file(path=f'{path}/ds1/1.0.0/features.json')
  mock_fs.add_file(path=f'{path}/ds2/config1/1.0.0/dataset_info.json')
  mock_fs.add_file(path=f'{path}/ds2/config1/1.0.0/features.json')
  mock_fs.add_file(path=f'{path}/ds2/config1/2.0.0/dataset_info.json')
  mock_fs.add_file(path=f'{path}/ds2/config1/2.0.0/features.json')
  mock_fs.add_file(path=f'{path}/ds2/config2/1.0.0/dataset_info.json')
  mock_fs.add_file(path=f'{path}/ds2/config2/1.0.0/features.json')
  data_dir = epath.Path('/path/ns1')
  register = register_path.DataDirRegister(
      namespace_to_data_dirs={'ns1': [data_dir]}
  )
  assert sorted(register.list_dataset_references()) == [
      naming.DatasetReference(
          dataset_name='ds1', namespace='ns1', data_dir=data_dir
      ),
      naming.DatasetReference(
          dataset_name='ds2', namespace='ns1', data_dir=data_dir
      ),
  ]
