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

"""Tests for registry."""

import os
import tempfile
import textwrap
from unittest import mock

from etils import epath
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.community import config as config_lib
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
    tmp_path = epath.Path(tmp_path)

    # Prepare the datasets
    # Namespace 0
    Ds0(data_dir=tmp_path / 'kaggle').download_and_prepare()
    Ds1(data_dir=tmp_path / 'kaggle2').download_and_prepare()
    # Namespace 1
    Ds0(data_dir=tmp_path / 'mlds').download_and_prepare()
    # Namespace 2: (non-existing)
    for d in tmp_path.iterdir():
      print(d)
    for d in (tmp_path / 'kaggle').iterdir():
      print(d)
    for d in (tmp_path / 'kaggle2').iterdir():
      print(d)
    for d in (tmp_path / 'mlds').iterdir():
      print(d)

    content = textwrap.dedent(f"""
        [kaggle]
        paths=[
            '{os.fspath(tmp_path / 'kaggle')}',
            '{os.fspath(tmp_path / 'kaggle2')}',
        ]
        info = "Kaggle datasets."
        [mlds]
        paths='{os.fspath(tmp_path / 'mlds')}'
        [other]
        paths='/tmp/path/to/non-existing-path'
        """)

    dummy_path = tmp_path / 'dummy-community-datasets.toml'
    dummy_path.write_text(content)
    config = config_lib.NamespaceRegistry(dummy_path)
    yield registry_lib.DatasetRegistry(config)


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
  register = registry_lib._load_registry(
      namespace='huggingface',
      config=config_lib.NamespaceConfig(
          paths=['github://huggingface/datasets/tree/master/datasets']
      ),
  )
  assert isinstance(register, register_package.PackageRegister)
  assert register._path == gcs_utils.GCS_COMMUNITY_INDEX_PATH


def test_load_register_for_path_gcs():
  registers = registry_lib._load_registry(
      namespace='my_namespace',
      config=config_lib.NamespaceConfig(
          paths=['gs://my-bucket/datasets', 'gs://my-bucket2/datasets']
      ),
  )
  assert isinstance(registers, register_path.DataDirRegister)


def test_load_register_for_path_mixed():
  with pytest.raises(RuntimeError, match='Both a path containing .*'):
    registry_lib._load_registry(
        namespace='my_namespace',
        config=config_lib.NamespaceConfig(
            paths=[
                'github://huggingface/datasets/tree/master/datasets',
                'gs://my-bucket/datasets',
            ]
        ),
    )


def test_community_register():
  assert 'huggingface' in registry_lib.community_register().list_namespaces()


def _write_dummy_config(content: str, tmp_path: str) -> epath.Path:
  tmp_path = epath.Path(tmp_path)
  dummy_path = tmp_path / 'dummy-community-datasets.toml'
  dummy_path.write_text(content)
  return dummy_path


@mock.patch.object(registry_lib, '_registers_per_namespace')
def test_dataset_registry_list_builders(mock_registers_per_namespace, tmp_path):
  register1 = mock.create_autospec(register_path.DataDirRegister)
  register1.list_builders.return_value = ['a', 'b']
  register2 = mock.create_autospec(register_package.PackageRegister)
  register2.list_builders.return_value = ['c']
  mock_registers_per_namespace.return_value = {
      'ns1': [register1],
      'ns2': [register2],
  }
  dummy_path = _write_dummy_config(
      textwrap.dedent("""
    [ns1]
    paths = '/data/ds1'
    [ns2]
    paths = '/data/ds2'
  """),
      tmp_path,
  )
  config = config_lib.NamespaceRegistry(dummy_path)
  registry = registry_lib.DatasetRegistry(config)
  assert set(registry.list_namespaces()) == {'ns1', 'ns2'}
  assert set(registry.list_builders()) == {'a', 'b', 'c'}


@pytest.fixture()
def dummy_refs_and_registers():
  ref1 = naming.DatasetReference(dataset_name='ds1', namespace='ns1')
  ref2 = naming.DatasetReference(dataset_name='ds2', namespace='ns1')
  ref3 = naming.DatasetReference(dataset_name='ds3', namespace='ns2')
  register1 = mock.create_autospec(register_path.DataDirRegister)
  register1.list_dataset_references.return_value = [ref1, ref2]
  register2 = mock.create_autospec(register_package.PackageRegister)
  register2.list_dataset_references.return_value = [ref3]
  return {
      'dummy_references': [ref1, ref2, ref3],
      'dummy_registers': [register1, register2],
  }


@pytest.fixture()
def dummy_config(tmp_path):
  dummy_path = _write_dummy_config(
      textwrap.dedent("""
    [ns1]
    paths = '/data/ds1'
    [ns2]
    paths = '/data/ds2'
  """),
      tmp_path,
  )
  return config_lib.NamespaceRegistry(dummy_path)


@mock.patch.object(registry_lib, '_registers_per_namespace')
def test_list_dataset_references(
    mock_registers_per_namespace, dummy_refs_and_registers, dummy_config
):  # pylint: disable=redefined-outer-name
  register1, register2 = dummy_refs_and_registers['dummy_registers']
  mock_registers_per_namespace.return_value = {
      'ns1': [register1],
      'ns2': [register2],
  }
  registry = registry_lib.DatasetRegistry(dummy_config)
  assert (
      sorted(registry.list_dataset_references())
      == dummy_refs_and_registers['dummy_references']
  )


@mock.patch.object(registry_lib, '_registers_per_namespace')
def test_list_dataset_references_per_namespace(
    mock_registers_per_namespace, dummy_refs_and_registers, dummy_config
):  # pylint: disable=redefined-outer-name
  ref1, ref2, ref3 = dummy_refs_and_registers['dummy_references']
  register1, register2 = dummy_refs_and_registers['dummy_registers']
  mock_registers_per_namespace.return_value = {
      'ns1': [register1],
      'ns2': [register2],
  }
  registry = registry_lib.DatasetRegistry(dummy_config)
  assert sorted(
      registry.list_dataset_references_for_namespace(namespace='ns1')
  ) == [ref1, ref2]
  assert sorted(
      registry.list_dataset_references_for_namespace(namespace='ns2')
  ) == [ref3]

  with pytest.raises(ValueError, match='Namespace ns3 not found.'):
    list(registry.list_dataset_references_for_namespace(namespace='ns3'))


def test_add_namespace(dummy_register: registry_lib.DatasetRegistry):  # pylint: disable=redefined-outer-name
  mock_register = mock.create_autospec(register_path.DataDirRegister)
  dummy_register.add_namespace(
      'my_namespace',
      config=config_lib.NamespaceConfig(paths=[epath.Path('/data')]),
      registers=[mock_register],
  )
  assert 'my_namespace' in dummy_register.list_namespaces()
  assert 'my_namespace' in dummy_register.config_per_namespace
  assert 'my_namespace' in dummy_register.registers_per_namespace
  assert dummy_register.registers_per_namespace['my_namespace'] == [
      mock_register
  ]
  assert 'kaggle' in dummy_register.list_namespaces()


def test_add_namespace_duplicate(dummy_register: registry_lib.DatasetRegistry):  # pylint: disable=redefined-outer-name
  mock_register = mock.create_autospec(register_path.DataDirRegister)
  with pytest.raises(ValueError, match='Namespace kaggle already exists!.*'):
    dummy_register.add_namespace(
        'kaggle',
        config=config_lib.NamespaceConfig(paths=[epath.Path('/data')]),
        registers=[mock_register],
    )
