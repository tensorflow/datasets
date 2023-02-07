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

"""Pytest plugins globally available.

`conftest.py` file is automatically detected by Pytest and register
plugins (hooks and fixtures) common to all tests.

See: https://docs.pytest.org/en/latest/writing_plugins.html
"""
from __future__ import annotations

import typing
from typing import Iterator, Type

import pytest
from tensorflow_datasets import setup_teardown

if typing.TYPE_CHECKING:
  from tensorflow_datasets import testing
  from tensorflow_datasets.core import dataset_builder

# Global setup/teardown

# Ignore tests and non-test files
# https://docs.pytest.org/en/latest/reference/reference.html#globalvar-collect_ignore
collect_ignore = ['testing/test_utils.py', 'core/features/features_test.py']

# Register fixtures which are automatically applied once when tests start.


@pytest.fixture(scope='session', autouse=True)
def disable_community_datasets():
  """During tests, `tfds.list_builders` disable community datasets."""
  # For tests, only public datasets are available (no-community datasets)
  # Kokoro pytest tests are executed without absl.app, so the default
  # visibility isn't automatically set.
  from tensorflow_datasets.core import visibility  # pylint: disable=g-import-not-at-top

  visibility.set_availables(
      [
          visibility.DatasetType.TFDS_PUBLIC,
      ]
  )


# Register all fixtures defined in `setup_teardown` to be automatically
# applied in all tests.
global_dict = globals()
for fixture_fn in setup_teardown.GLOBAL_FIXTURES:
  fixture_name = fixture_fn.__name__
  if fixture_name in global_dict:
    raise ValueError(f'{fixture_name} already in module.')
  fixture_fn = pytest.fixture(scope='session', autouse=True)(fixture_fn)
  # In orders for fixtures to be registered, there need to be an explicit
  # attribute
  # https://stackoverflow.com/questions/27064004/splitting-a-conftest-py-file-into-several-smaller-conftest-like-parts/65035367#65035367
  global_dict[fixture_name] = fixture_fn
del global_dict  # Do not modifying global beyond this point

# Fixtures globally available


@pytest.fixture
def mock_fs() -> Iterator[testing.MockFs]:
  """Patch `tf.io.gfile` API into a virtual file system."""
  from tensorflow_datasets import testing  # pylint: disable=g-import-not-at-top

  with testing.MockFs() as fs:
    yield fs


def _make_dataset(
    tmp_path_factory: pytest.TempPathFactory,
    builder_cls: Type[dataset_builder.DatasetBuilder],
) -> dataset_builder.DatasetBuilder:
  tmp_path = tmp_path_factory.mktemp(f'global_{builder_cls.__name__}')
  builder = builder_cls(data_dir=tmp_path)
  builder.download_and_prepare()
  return builder


@pytest.fixture(scope='session')
def dummy_mnist(
    tmp_path_factory: pytest.TempPathFactory,
) -> dataset_builder.DatasetBuilder:
  """Dummy mnist dataset builder pre-generated."""
  from tensorflow_datasets import testing  # pylint: disable=g-import-not-at-top

  return _make_dataset(tmp_path_factory, testing.DummyMnist)


@pytest.fixture(scope='session')
def dummy_dataset(
    tmp_path_factory: pytest.TempPathFactory,
) -> dataset_builder.DatasetBuilder:
  """Dummy dataset builder pre-generated."""
  from tensorflow_datasets import testing  # pylint: disable=g-import-not-at-top

  return _make_dataset(tmp_path_factory, testing.DummyDataset)
