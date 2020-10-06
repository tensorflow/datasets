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

"""Tests for tensorflow_datasets.core.load.

Note: `load.py` code was previously in `registered.py`, so some of the tests
are still on `registered_test.py`.
"""

import functools
import os
from unittest import mock

import pytest

from tensorflow_datasets import testing
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import load


# We assume that all datasets are added into `data_dir='path/to'`
_find_builder_dir = functools.partial(
    load.find_builder_dir, data_dir='path/to'
)


def test_find_builder_dir_with_multiple_data_dir(mock_fs: testing.MockFs):
  mock_fs.add_file('path/to/ds0/1.0.0/features.json')

  # Dataset not found.
  assert load.find_builder_dir('ds0') is None

  with mock.patch.object(
      constants,
      'list_data_dirs',
      return_value=[constants.DATA_DIR, 'path/to'],
  ):
    assert load.find_builder_dir('ds0') == 'path/to/ds0/1.0.0'

    # Dataset present in 2 different data_dir
    duplicate_path = os.path.join(constants.DATA_DIR, 'ds0/1.0.0/features.json')
    mock_fs.add_file(duplicate_path)
    with pytest.raises(ValueError, match='detected in multiple locations'):
      load.find_builder_dir('ds0')


def test_find_builder_dir_legacy_ds(mock_fs: testing.MockFs):
  """Legacy dataset should be ignored (no feature config file)."""
  mock_fs.add_file('path/to/ds0/1.0.0/temp.txt')
  assert _find_builder_dir('ds0') is None

  mock_fs.add_file('path/to/ds0/1.0.0/features.json')
  assert _find_builder_dir('ds0') == 'path/to/ds0/1.0.0'


def test_find_builder_dir_multi_versions(mock_fs: testing.MockFs):
  """Versions should be sorted numerically (10 > 9)."""
  mock_fs.add_file('path/to/ds0/1.0.0/features.json')
  mock_fs.add_file('path/to/ds0/9.9.9/features.json')
  mock_fs.add_file('path/to/ds0/10.0.0/features.json')
  assert _find_builder_dir('ds0') == 'path/to/ds0/10.0.0'
  # Explicitly given version
  assert _find_builder_dir('ds0:9.9.9') == 'path/to/ds0/9.9.9'
  # Non-existing version
  assert _find_builder_dir('ds0:9.9.0') is None


def test_find_builder_dir_bad_version_dir_name(mock_fs: testing.MockFs):
  """Ill-formatted folders should be ignored."""
  mock_fs.add_file('path/to/ds0/9.9./features.json')
  mock_fs.add_file('path/to/ds0/1.0.o/features.json')
  mock_fs.add_file('path/to/ds0/other/features.json')
  assert _find_builder_dir('ds0') is None

  mock_fs.add_file('path/to/ds0/1.1.0/features.json')
  assert _find_builder_dir('ds0') == 'path/to/ds0/1.1.0'


def test_find_builder_config_no_code(mock_fs: testing.MockFs):
  """When the code can't be reached, config should be explicit."""
  mock_fs.add_file('path/to/ds0/config/1.0.0/features.json')
  mock_fs.add_file('path/to/ds0/1.1.0/features.json')

  # If the original code can't be reached, assume no config
  assert _find_builder_dir('ds0') == 'path/to/ds0/1.1.0'
  # Config is explicitly given
  assert _find_builder_dir('ds0/config') == 'path/to/ds0/config/1.0.0'

  mock_fs.add_file('path/to/ds1/config/1.0.0/features.json')
  # Config not available, return None
  assert _find_builder_dir('ds1') is None
  assert _find_builder_dir('ds1/config') == 'path/to/ds1/config/1.0.0'


def test_find_builder_wrong_dir(mock_fs: testing.MockFs):
  mock_fs.add_file('path/to/ds0/1.1.0/features.json')
  assert _find_builder_dir('ds0') == 'path/to/ds0/1.1.0'
  assert _find_builder_dir('ds0', data_dir='path/to/other/dir') is None


def test_find_builder_config_code(mock_fs: testing.MockFs):
  """When code exists, extract the default config name."""

  class MyDataset(testing.DummyMnist):  # pylint: disable=unused-variable
    """Dummy dataset."""
    BUILDER_CONFIGS = [
        dataset_builder.BuilderConfig(  # pylint: disable=g-complex-comprehension
            name=name,
            version='2.0.0',
            description=f'{name} description'
        )
        for name in ('default_config', 'other_config')
    ]

  mock_fs.add_file('path/to/my_dataset/default_config/0.0.1/features.json')
  mock_fs.add_file('path/to/my_dataset/default_config/1.0.0/features.json')
  mock_fs.add_file('path/to/my_dataset/other_config/1.0.0/features.json')
  mock_fs.add_file('path/to/my_dataset/old_config/0.8.0/features.json')
  mock_fs.add_file('path/to/my_dataset/old_config/1.0.0/features.json')
  mock_fs.add_file('path/to/my_dataset/broken_config/features.json')
  mock_fs.add_file('path/to/my_dataset/0.0.1/features.json')

  # If code can be reached, use it to load the default config name
  # Note that the existing version is loaded, even if the code is at a
  # more recent version.
  assert (
      _find_builder_dir('my_dataset')
      == 'path/to/my_dataset/default_config/1.0.0'
  )
  # Explicitly given version with implicit config.
  assert (
      _find_builder_dir('my_dataset:0.0.1')
      == 'path/to/my_dataset/default_config/0.0.1'
  )
  # When config is explicitly given, load the last detected version
  assert (
      _find_builder_dir('my_dataset/other_config')
      == 'path/to/my_dataset/other_config/1.0.0'
  )
  assert (
      _find_builder_dir('my_dataset/old_config')
      == 'path/to/my_dataset/old_config/1.0.0'
  )
  assert (
      _find_builder_dir('my_dataset/old_config:0.8.0')
      == 'path/to/my_dataset/old_config/0.8.0'
  )
  assert _find_builder_dir('my_dataset/broken_config') is None
  assert _find_builder_dir('my_dataset/unknown_config') is None


def test_get_version_str(mock_fs: testing.MockFs):

  mock_fs.add_file('path/to/ds/1.0.0/features.json')
  mock_fs.add_file('path/to/ds/1.0.1/features.json')
  mock_fs.add_file('path/to/ds/1.1.0/features.json')
  mock_fs.add_file('path/to/ds/2.0.1/features.json')

  get_version_str = functools.partial(load._get_version_str, 'path/to/ds/')  # pylint: disable=protected-access

  # requested_version is None -> Returns last version
  assert get_version_str(requested_version=None) == '2.0.1'
  # Returns highest matching version
  assert get_version_str(requested_version='1.*.*') == '1.1.0'
  assert get_version_str(requested_version='*.*.*') == '2.0.1'
  assert get_version_str(requested_version='1.0.0') == '1.0.0'
  # No matching version found
  assert get_version_str(requested_version='1.3.*') is None
  assert get_version_str(requested_version='2.3.5') is None

  assert _find_builder_dir('ds') == 'path/to/ds/2.0.1'
  assert _find_builder_dir('ds:*.*.*') == 'path/to/ds/2.0.1'
  assert _find_builder_dir('ds:1.*.*') == 'path/to/ds/1.1.0'
  assert _find_builder_dir('ds:1.0.0') == 'path/to/ds/1.0.0'
  assert _find_builder_dir('ds:1.3.*') is None
  assert _find_builder_dir('ds:2.3.5') is None
