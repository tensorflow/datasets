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

"""Pytest plugins globally available.

`conftest.py` file is automatically detected by Pytest and register
plugins (hooks and fixtures) common to all tests.

See: https://docs.pytest.org/en/latest/writing_plugins.html

"""
from typing import Iterator

import pytest

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import visibility
from tensorflow_datasets.testing import setup_teardown


# Global setup/teardown


@pytest.fixture(scope='session', autouse=True)
def activate_eager():
  """Globally and automatically enable eager."""
  tf.compat.v1.enable_v2_behavior()


# Register fixtures which are automatically applied once when tests start.


@pytest.fixture(scope='session', autouse=True)
def disable_community_datasets():
  """During tests, `tfds.list_builders` disable community datasets."""
  # For tests, only public datasets are available (no-community datasets)
  # Kokoro pytest tests are executed without absl.app, so the default
  # visibility isn't automatically set.
  visibility.set_availables([
      visibility.DatasetType.TFDS_PUBLIC,
  ])


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
  with testing.MockFs() as fs:
    yield fs
