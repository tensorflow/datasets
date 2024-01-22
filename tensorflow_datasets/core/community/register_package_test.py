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

"""Tests for tensorflow_datasets.core.community.register_path."""

import contextlib
import datetime
import json
import os
import pathlib
import sys
import tempfile
import textwrap
from typing import Iterator
from unittest import mock

from etils import epath
import pytest
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import cache
from tensorflow_datasets.core.community import dataset_sources
from tensorflow_datasets.core.community import register_package


@contextlib.contextmanager
def mock_cache_path(new_cache_dir: epath.Path) -> Iterator[None]:
  """Mock which overwrite the cache path."""
  # Use `__wrapped__` to access the original function wrapped inside
  # `functools.lru_cache`
  new_cache_path = utils.memoize()(cache.cache_path.__wrapped__)
  new_module_path = utils.memoize()(cache.module_path.__wrapped__)
  with mock.patch.object(
      cache, '_default_cache_dir', return_value=new_cache_dir
  ), mock.patch.object(cache, 'cache_path', new_cache_path), mock.patch.object(
      cache, 'module_path', new_module_path
  ):
    yield


@pytest.fixture(scope='module')
def dummy_register():
  """Dummy register."""

  with tempfile.TemporaryDirectory() as tmp_path:
    tmp_path = epath.Path(tmp_path)

    source_path = utils.tfds_path() / 'testing/dummy_dataset/dummy_dataset.py'

    # Single-file dataset package (without checksums)
    src_single = dataset_sources.DatasetSource.from_json(os.fspath(source_path))

    # Multi-file dataset package (with checksums)
    src_multi = dataset_sources.DatasetSource.from_json({
        'root_path': os.fspath(source_path.parent),
        'filenames': ['checksums.tsv', 'dummy_dataset.py'],
    })
    src_multi_json = json.dumps(src_multi.to_json())  # `dict` -> `str`

    # Create the remote index content
    # Note the absence of `"` for the `src_multi_json` as it is parsed as `dict`
    content = textwrap.dedent(f"""\
        {{"name": "kaggle:dummy_dataset", "source": "{src_single.to_json()}"}}
        {{"name": "kaggle:ds1", "source": "{src_single.to_json()}"}}
        {{"name": "mlds:dummy_dataset", "source": {src_multi_json}}}
        """)
    dummy_path = tmp_path / 'dummy-community-datasets.toml'
    dummy_path.write_text(content)

    with mock_cache_path(tmp_path / 'cache'):
      yield register_package.PackageRegister(path=dummy_path)


def test_list_dataset_references(
    dummy_register: register_package.PackageRegister,
):  # pylint: disable=redefined-outer-name
  assert sorted(dummy_register.list_dataset_references()) == [
      naming.DatasetReference(dataset_name='ds1', namespace='kaggle'),
      naming.DatasetReference(dataset_name='dummy_dataset', namespace='kaggle'),
      naming.DatasetReference(dataset_name='dummy_dataset', namespace='mlds'),
  ]


def test_builder_cls(dummy_register: register_package.PackageRegister):  # pylint: disable=redefined-outer-name
  # The dataset will be installed in the cache
  installed_path = cache.cache_path()
  installed_path /= 'modules/tfds_community/kaggle/dummy_dataset'
  assert not installed_path.exists()

  ds_name = naming.DatasetName('kaggle:dummy_dataset')
  builder_cls = dummy_register.builder_cls(ds_name)
  assert builder_cls.name == 'dummy_dataset'

  clshash = 'd66db99e4dbd05066b84b97ff9528f404fc71e61d556add952a67416e70a1786'
  assert installed_path / f'{clshash}/dummy_dataset.py' == builder_cls.code_path
  assert 'kaggle' in builder_cls.code_path.parts
  assert issubclass(builder_cls, dataset_builder.DatasetBuilder)
  assert not builder_cls.url_infos  # No checksums installed with the package

  # Dataset installed in the cache
  # Filename should be deterministic
  assert list(sorted(installed_path.iterdir())) == [installed_path / clshash]

  # Reusing the dataset should re-use the cache
  with mock.patch.object(
      register_package,
      '_download_and_cache',
      side_effect=ValueError('Dataset should have been cached already'),
  ):
    ds_name = naming.DatasetName('kaggle:dummy_dataset')
    builder_cls2 = dummy_register.builder_cls(ds_name)
  assert builder_cls is builder_cls2

  # Datasets from different namespace can have the same name
  ds_name = naming.DatasetName('mlds:dummy_dataset')
  builder_cls = dummy_register.builder_cls(ds_name)
  assert 'mlds' in builder_cls.code_path.parts
  assert issubclass(builder_cls, dataset_builder.DatasetBuilder)
  # Checksums have been correctly installed
  assert 'http://dummy.org/data.txt' in builder_cls.url_infos

  with pytest.raises(registered.DatasetNotFoundError):
    dummy_register.builder(naming.DatasetName('other:ds0'))


def test_register_path_list_builders(dummy_register):  # pylint: disable=redefined-outer-name
  assert dummy_register.list_builders() == [
      'kaggle:ds1',
      'kaggle:dummy_dataset',
      'mlds:dummy_dataset',
  ]


def test_dataset_package():
  """Exports/imports operation should be identity."""
  pkg = register_package.DatasetPackage(
      name=naming.DatasetName('ns:ds'),
      source=dataset_sources.DatasetSource.from_json(
          'github://<owner>/<name>/tree/<branch>/my_ds/ds.py',
      ),
  )
  assert register_package.DatasetPackage.from_json(pkg.to_json()) == pkg

  pkg2 = register_package._InstalledPackage(
      package=pkg,
      instalation_date=datetime.datetime.now(),
      hash='asdajhdadsadsad',
  )
  assert register_package._InstalledPackage.from_json(pkg2.to_json()) == pkg2


def test_mock_cache_path(tmp_path: pathlib.Path):
  with mock_cache_path(epath.Path(tmp_path)):
    assert os.fspath(tmp_path) not in sys.path
    assert cache.cache_path() == tmp_path
    assert cache.module_path() == tmp_path / 'modules'
    assert os.fspath(tmp_path / 'modules') in sys.path
