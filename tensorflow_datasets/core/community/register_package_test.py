# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
import os
import pathlib
import sys
import tempfile
import textwrap
from typing import Iterator
from unittest import mock

import pytest

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import cache
from tensorflow_datasets.core.community import register_package


@contextlib.contextmanager
def mock_cache_path(new_cache_dir: utils.PathLike) -> Iterator[None]:
  """Mock which overwrite the cache path."""
  new_dir = utils.as_path(new_cache_dir)

  # Use `__wrapped__` to access the original function wrapped inside
  # `functools.lru_cache`
  new_cache_path = utils.memoize()(cache.cache_path.__wrapped__)
  new_module_path = utils.memoize()(cache.module_path.__wrapped__)
  with mock.patch.object(cache, '_default_cache_dir', return_value=new_dir), \
       mock.patch.object(cache, 'cache_path', new_cache_path), \
       mock.patch.object(cache, 'module_path', new_module_path):
    yield


@pytest.fixture(scope='module')
def dummy_register():
  """Dummy register."""

  with tempfile.TemporaryDirectory() as tmp_path:
    tmp_path = pathlib.Path(tmp_path)

    # Create the remote index content
    source_path = utils.tfds_path() / 'testing/dummy_dataset'
    source_str = os.fspath(source_path)
    content = textwrap.dedent(
        f"""\
        {{"name": "kaggle:ds0", "source": "{source_str}"}}
        {{"name": "kaggle:ds1", "source": "{source_str}"}}
        {{"name": "mlds:ds0", "source": "{source_str}"}}
        """
    )
    dummy_path = tmp_path / 'dummy-community-datasets.toml'
    dummy_path.write_text(content)

    with mock_cache_path(tmp_path / 'cache'):
      yield register_package.PackageRegister(path=dummy_path)


def test_builder_cls(dummy_register):  # pylint: disable=redefined-outer-name

  # The dataset will be installed in the cache
  installed_path = cache.cache_path() / 'modules/tfds_community/kaggle/ds0'

  assert not installed_path.exists()

  builder_cls = dummy_register.builder_cls(utils.DatasetName('kaggle:ds0'))
  assert builder_cls.name == 'dummy_dataset'
  assert 'kaggle' in builder_cls.code_path.parts
  assert issubclass(builder_cls, dataset_builder.DatasetBuilder)

  # Dataset installed in the cache
  # Filename should be deterministic
  assert list(sorted(installed_path.iterdir())) == [
      installed_path /
      '1de59094bbe913e9a95aa0cff6f46bc06d813bd5c288eac34950b473e4ef199c',
  ]

  # Reusing the dataset should re-use the cache
  with mock.patch.object(
      register_package,
      '_download_and_cache',
      side_effect=ValueError('Dataset should have been cached already')
  ):
    builder_cls2 = dummy_register.builder_cls(utils.DatasetName('kaggle:ds0'))
  assert builder_cls is builder_cls2

  # Datasets from different namespace can have the same name
  builder_cls = dummy_register.builder_cls(utils.DatasetName('mlds:ds0'))
  assert 'mlds' in builder_cls.code_path.parts
  assert issubclass(builder_cls, dataset_builder.DatasetBuilder)

  with pytest.raises(registered.DatasetNotFoundError):
    dummy_register.builder(utils.DatasetName('other:ds0'))


def test_register_path_list_builders(dummy_register):  # pylint: disable=redefined-outer-name
  assert dummy_register.list_builders() == [
      'kaggle:ds0',
      'kaggle:ds1',
      'mlds:ds0',
  ]


def test_dataset_package():
  """Exports/imports operation should be identity."""
  pkg = register_package._DatasetPackage(
      name=utils.DatasetName('ns:ds'),
      source='github://...',
  )
  assert register_package._DatasetPackage.from_json(pkg.to_json()) == pkg

  pkg2 = register_package._InstalledPackage(
      package=pkg,
      filestem='dummy_dataset',
      instalation_date=datetime.datetime.now(),
      hash='asdajhdadsadsad',
  )
  assert register_package._InstalledPackage.from_json(pkg2.to_json()) == pkg2


def test_mock_cache_path(tmp_path: pathlib.Path):
  with mock_cache_path(tmp_path):
    assert os.fspath(tmp_path) not in sys.path
    assert cache.cache_path() == tmp_path
    assert cache.module_path() == tmp_path / 'modules'
    assert os.fspath(tmp_path / 'modules') in sys.path
