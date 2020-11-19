# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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
from tensorflow_datasets.testing import setup_teardown


# Global setup/teardown


@pytest.fixture(scope='session', autouse=True)
def activate_eager():
  """Globally and automatically enable eager."""
  tf.compat.v1.enable_v2_behavior()


# Fixtures globally available


@pytest.fixture
def mock_fs() -> Iterator[testing.MockFs]:
  """Patch `tf.io.gfile` API into a virtual file system."""
  with testing.MockFs() as fs:
    yield fs
