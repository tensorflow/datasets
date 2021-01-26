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

"""Setup/teardown fixtures common to unittest/pytest.

* Unittest: Those functions are wrapped in `@contextlib.contextmanager` and
  called in `setUpClass`/`tearDownClass`.
* Pytest: Those functions are wrapped in `@fixture`.

"""

from unittest import mock

import tensorflow as tf
from tensorflow_datasets.core import constants
from tensorflow_datasets.core.github_api import github_path
from tensorflow_datasets.testing import test_utils


def assert_no_api_call():
  """Globally disable github API calls."""
  with mock.patch.object(
      github_path._PathMetadata,  # pylint: disable=protected-access
      '_query_github',
      side_effect=AssertionError('Forbidden API call'),
  ):
    yield


# Fixtures automatically applied for all tests (unittest and pytest)
GLOBAL_FIXTURES = [
    assert_no_api_call,
]
