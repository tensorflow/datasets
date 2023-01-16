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

"""Tests for registry."""
import os
import pathlib
import tempfile
import textwrap
from unittest import mock

import pytest

from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.community import register_package
from tensorflow_datasets.core.community import register_path
from tensorflow_datasets.core.community import registry as registry_lib
from tensorflow_datasets.core.utils import gcs_utils


class Ds0(testing.DummyDataset):
  pass


class Ds1(testing.DummyDataset):
  pass


@pytest.fixture(scope='module')
def dummy_register():
  """Dummy register."""
  with tempfile.TemporaryDirectory() as tmp_path:
    tmp_path = pathlib.Path(tmp_path)

    # Prepare the datasets
    # Namespace 0
    Ds0(data_dir=tmp_path / 'kaggle').download_and_prepare()
    Ds1(data_dir=tmp_path / 'kaggle2').download_and_prepare()
    # Namespace 1
    Ds0(data_dir=tmp_path / 'mlds').download_and_prepare()
    # Namespace 2: (non-existing)
    print('XXXXXXX: CONTENT!!!')
    for d in tmp_path.iterdir():
      print(d)
    for d in (tmp_path / 'kaggle').iterdir():
      print(d)
    for d in (tmp_path / 'kaggle2').iterdir():
      print(d)
    for d in (tmp_path / 'mlds').iterdir():
      print(d)

    content = textwrap.dedent(
        f"""
        [Namespaces]
        kaggle=[
            '{os.fspath(tmp_path / 'kaggle')}',
            '{os.fspath(tmp_path / 'kaggle2')}',
        ]
        mlds='{os.fspath(tmp_path / 'mlds')}'
        other='/tmp/path/to/non-existing-path'
        """
    )

    dummy_path = tmp_path / 'dummy-community-datasets.toml'
    dummy_path.write_text(content)
    yield registry_lib.DatasetRegistry(
        namespace_config=registry_lib.NamespaceConfig(config_path=dummy_path)
    )


def test_register_builder(dummy_register):  # pylint: disable=redefined-outer-name
  builder = dummy_register.builder(naming.DatasetName('kaggle:ds0'))
  assert 'kaggle' in builder.data_path.parts

  # Same dataset name can be loaded from different namespace
  builder = dummy_register.builder(naming.DatasetName('mlds:ds0'))
  assert 'mlds' in builder.data_path.parts

  builder = dummy_register.builder(
      naming.DatasetName('mlds:ds0'),
      data_dir=None,  # data_dir can be passed only if None
      version='1.0.0',
  )
  assert 'mlds' in builder.data_path.parts

  with pytest.raises(ValueError, match='`data_dir` cannot be set for'):
    dummy_register.builder(
        naming.DatasetName('mlds:ds0'), data_dir='/path/to/data_dir'
    )

  with pytest.raises(
      registered.DatasetNotFoundError, match='Namespace .* not found.'
  ):
    dummy_register.builder(naming.DatasetName('non-existing-namespace:ds0'))

  with pytest.raises(registered.DatasetNotFoundError):
    dummy_register.builder(naming.DatasetName('other:ds0'))


def test_register_path_list_builders(dummy_register):  # pylint: disable=redefined-outer-name
  assert dummy_register.list_builders() == [
      'kaggle:ds0',
      'kaggle:ds1',
      'mlds:ds0',
  ]


def test_load_register_for_path_github():
  registers = registry_lib._load_register_for_paths(
      namespace='huggingface',
      paths=['github://huggingface/datasets/tree/master/datasets'],
  )
  assert len(registers) == 1
  assert isinstance(registers[0], register_package.PackageRegister)
  assert registers[0]._path == gcs_utils.GCS_COMMUNITY_INDEX_PATH


def test_load_register_for_path_gcs():
  registers = registry_lib._load_register_for_paths(
      namespace='my_namespace',
      paths=['gs://my-bucket/datasets', 'gs://my-bucket2/datasets'],
  )
  assert len(registers) == 1
  assert isinstance(registers[0], register_path.DataDirRegister)


def test_load_register_for_path_mixed():
  with pytest.raises(RuntimeError, match='Both a path containing .*'):
    registry_lib._load_register_for_paths(
        namespace='my_namespace',
        paths=[
            'github://huggingface/datasets/tree/master/datasets',
            'gs://my-bucket/datasets',
        ],
    )


def test_community_register():
  assert 'huggingface' in registry_lib.community_register.list_namespaces()


def test_dataset_registry_list_builders():
  register1 = mock.create_autospec(register_path.DataDirRegister)
  register1.list_builders.return_value = ['a', 'b']
  register2 = mock.create_autospec(register_package.PackageRegister)
  register2.list_builders.return_value = ['c']
  namespace_config = mock.create_autospec(registry_lib.NamespaceConfig)
  namespace_config.registers_per_namespace.return_value = {
      'ns1': [register1],
      'ns2': [register2],
  }
  registry = registry_lib.DatasetRegistry(namespace_config=namespace_config)
  assert set(registry.list_namespaces()) == {'ns1', 'ns2'}
  assert set(registry.list_builders()) == {'a', 'b', 'c'}


def test_list_dataset_references():
  ref1 = naming.DatasetReference(dataset_name='ds1', namespace='kaggle')
  ref2 = naming.DatasetReference(dataset_name='ds2', namespace='kaggle')
  ref3 = naming.DatasetReference(dataset_name='ds3', namespace='kaggle')
  register1 = mock.create_autospec(register_path.DataDirRegister)
  register1.list_dataset_references.return_value = [ref1, ref2]
  register2 = mock.create_autospec(register_package.PackageRegister)
  register2.list_dataset_references.return_value = [ref3]
  namespace_config = mock.create_autospec(registry_lib.NamespaceConfig)
  namespace_config.registers_per_namespace.return_value = {
      'ns1': [register1],
      'ns2': [register2],
  }
  registry = registry_lib.DatasetRegistry(namespace_config=namespace_config)
  assert sorted(registry.list_dataset_references()) == [ref1, ref2, ref3]
