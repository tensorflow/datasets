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

"""Setup/teardown fixtures common to unittest/pytest.

* Unittest: Those functions are wrapped in `@contextlib.contextmanager` and
  called in `setUpClass`/`tearDownClass`.
* Pytest: Those functions are wrapped in `@fixture`.

This file is not part of `tensorflow_datasets.testing` because this module still
heavily depends on TensorFlow.
"""

from unittest import mock

from tensorflow_datasets.core import load
from tensorflow_datasets.core.github_api import github_path


def assert_no_api_call():
  """Globally disable github API calls."""
  with mock.patch.object(
      github_path.GithubApi,  # pylint: disable=protected-access
      'query',
      side_effect=AssertionError('Forbidden API call'),
  ):
    yield


# Fixtures automatically applied for all tests (unittest and pytest)
GLOBAL_FIXTURES = [
    assert_no_api_call,
]
