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

"""Github API util tests."""

import contextlib
import os
import textwrap
from unittest import mock

import pytest

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.github_api import github_path

_SKIP_NON_HERMETIC = False

# Non hermetic tests are explicitly marked and skipped if `_SKIP_NON_HERMETIC`
# is True.
non_hermetic_test = pytest.mark.skipif(
    _SKIP_NON_HERMETIC,
    reason='Non-hermetic test skipped.',
)

_original_query_github = github_path._PathMetadata._query_github

_AUTHOR_EXPECTED_CONTENT = textwrap.dedent("""\
    # This is the list of TensorFlow Datasets authors for copyright purposes.
    #
    # This does not necessarily list everyone who has contributed code, since in
    # some cases, their employer may be the copyright holder.  To see the full list
    # of contributors, see the revision history in source control.

    Google Inc.
    """)

# Note: assert_no_api_call is globally applied on all tests (in conftest.py)


@contextlib.contextmanager
def enable_api_call():
  """Contextmanager which locally re-enable API calls."""
  with mock.patch.object(github_path._PathMetadata, '_query_github',
                         _original_query_github):
    yield


def test_parse_github_path():
  url = 'github://tensorflow/datasets/tree/master/docs/README.md'
  repo, branch, path = github_path._parse_github_path(url)
  assert repo == 'tensorflow/datasets'
  assert branch == 'master'
  assert path == 'docs/README.md'

  url = 'github://tensorflow/datasets/tree/master'
  repo, branch, path = github_path._parse_github_path(url)
  assert repo == 'tensorflow/datasets'
  assert branch == 'master'
  assert path == ''  # pylint: disable=g-explicit-bool-comparison


def test_github_path_registered_as_path():
  uri = 'github://tensorflow/datasets/tree/master/docs/README.md'
  path = utils.as_path(uri)
  assert isinstance(path, github_path.GithubPath)
  assert os.fspath(path) == uri


def test_invalid_github_path():
  # Path are lazily validated, so require explicit `_metadata` call.

  with pytest.raises(ValueError, match='Invalid github path'):
    _ = github_path.GithubPath()._metadata

  with pytest.raises(ValueError, match='Invalid github path'):
    _ = github_path.GithubPath('')._metadata

  with pytest.raises(ValueError, match='Invalid github path'):
    _ = github_path.GithubPath('github://not/a/path')

  with pytest.raises(ValueError, match='Invalid github path'):
    _ = github_path.GithubPath('github://tensorflow/tree/master/docs/README.md')

  # `blob` isn't accepted for consistency between paths.
  with pytest.raises(ValueError, match='/blob/` isn\'t accepted.'):
    _ = github_path.GithubPath(
        'github://tensorflow/datasets/blob/master/docs/README.md')

  p = github_path.GithubPath(
      'github://tensorflow/datasets/tree/master/docs/README.md')
  p = p.parent  # /docs
  _ = p._metadata
  p = p.parent  # /
  _ = p._metadata
  p = p.parent
  with pytest.raises(ValueError, match='Invalid github path'):
    _ = p._metadata


def test_github_path_purepath():
  """Tests that pathlib methods works as expected."""
  p = github_path.GithubPath('github://tensorflow/datasets/tree/master')
  sub_p = p / 'some_folder'
  assert isinstance(sub_p, github_path.GithubPath)
  assert str(p) == 'github://tensorflow/datasets/tree/master'
  assert str(sub_p) == 'github://tensorflow/datasets/tree/master/some_folder'
  assert os.fspath(p) == 'github://tensorflow/datasets/tree/master'
  assert p == github_path.GithubPath.from_repo('tensorflow/datasets')


def test_github_path_as_url():
  p = github_path.GithubPath.from_repo('tensorflow/datasets', 'v3.1.0')
  p /= 'README.md'
  expected = 'https://raw.githubusercontent.com/tensorflow/datasets/v3.1.0/README.md'
  assert p.as_raw_url() == expected


@non_hermetic_test
def test_github_api_listdir():
  """Test query github API."""
  # PurePath ops do not trigger API calls
  p = github_path.GithubPath.from_repo('tensorflow/datasets', 'v3.1.0')
  p = p / 'tensorflow_datasets' / 'testing'

  with enable_api_call():
    sub_dirs = sorted(p.iterdir())

  # `listdir` call cache the filetype of all childs
  all_dir_names = [d.name for d in sub_dirs if d.is_dir()]
  all_file_names = [d.name for d in sub_dirs if d.is_file()]
  all_names = [d.name for d in sub_dirs]

  with pytest.raises(NotADirectoryError):
    list((p / '__init__.py').iterdir())

  assert all_names == [
      '__init__.py',
      'dataset_builder_testing.py',
      'dataset_builder_testing_test.py',
      'fake_data_generation',
      'fake_data_utils.py',
      'generate_archives.sh',
      'metadata',
      'mocking.py',
      'mocking_test.py',
      'test_case.py',
      'test_data',
      'test_utils.py',
      'test_utils_test.py',
  ]
  assert all_dir_names == [
      'fake_data_generation',
      'metadata',
      'test_data',
  ]
  assert all_file_names == [
      '__init__.py',
      'dataset_builder_testing.py',
      'dataset_builder_testing_test.py',
      'fake_data_utils.py',
      'generate_archives.sh',
      'mocking.py',
      'mocking_test.py',
      'test_case.py',
      'test_utils.py',
      'test_utils_test.py',
  ]


@non_hermetic_test
def test_github_api_exists():
  """Test query github API."""
  p = github_path.GithubPath.from_repo('tensorflow/datasets', 'v3.1.0')
  with enable_api_call():
    assert p.exists()
    assert not (p / 'unknown_dir').exists()

  readme = p / 'README.md'
  core = p / 'tensorflow_datasets' / 'core'
  with enable_api_call():
    assert readme.is_file()
    assert core.is_dir()

  # Data should have been cached (no API calls required)
  assert not readme.is_dir()
  assert not core.is_file()
  assert readme.exists()
  assert core.exists()
  # Recreating a new Path reuse the cache
  assert (core.parent.parent / 'README.md').is_file()
  assert (core.parent.parent / 'README.md')._metadata is readme._metadata


@non_hermetic_test
def test_github_api_read_bytes_text():
  """Test query github API file content."""
  p = github_path.GithubPath.from_repo('tensorflow/datasets', 'v3.1.0')

  # Note: This is not wrapped inside `enable_api_call` contextmanager as
  # users need to download files without setting up an API token.

  content = (p / 'AUTHORS').read_bytes()
  assert isinstance(content, bytes)
  assert content == _AUTHOR_EXPECTED_CONTENT.encode()

  content = (p / 'AUTHORS').read_text()
  assert isinstance(content, str)
  assert content == _AUTHOR_EXPECTED_CONTENT

  # Cannot read the content of a directory.
  with pytest.raises(FileNotFoundError, match='Request failed'):
    (p / 'tensorflow_datasets' / 'core').read_bytes()


@non_hermetic_test
def test_github_api_copy(tmp_path):
  p = github_path.GithubPath.from_repo('tensorflow/datasets', 'v3.1.0')
  src = p / 'AUTHORS'
  dst = tmp_path / 'AUTHORS'

  target = src.copy(dst)
  assert target == dst
  assert dst.read_text() == _AUTHOR_EXPECTED_CONTENT

  with pytest.raises(FileExistsError, match='Destination .* exists'):
    src.copy(dst)

  src.copy(dst, overwrite=True)


def test_assert_no_api_call():
  with pytest.raises(AssertionError, match='Forbidden API call'):
    github_path.GithubPath.from_repo('tensorflow/datasets', 'v1.0.0').exists()
