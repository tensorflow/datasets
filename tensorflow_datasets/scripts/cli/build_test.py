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

"""Tests for tensorflow_datasets.scripts.cli.build."""

import os
import pathlib
from unittest import mock

import pytest

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.cli import main


@pytest.fixture(scope='function', autouse=True)
def mock_default_data_dir(tmp_path: pathlib.Path):
  """Changes the default `--data_dir` to tmp_path."""
  tmp_path = tmp_path / 'datasets'
  default_data_dir = os.environ.get('TFDS_DATA_DIR')
  try:
    os.environ['TFDS_DATA_DIR'] = os.fspath(tmp_path)
    yield tmp_path
  finally:
    if default_data_dir:
      os.environ['TFDS_DATA_DIR'] = default_data_dir
    else:
      del os.environ['TFDS_DATA_DIR']


def _build(cmd_flags: str) -> mock.Mock:
  """Executes `tfds build` command with the given flags."""
  # Execute the command
  args = main._parse_flags(f'tfds build {cmd_flags}'.split())
  with mock.patch(
      'tensorflow_datasets.core.DatasetBuilder.download_and_prepare'
  ) as mock_download_and_prepare:
    main.main(args)
  return mock_download_and_prepare


def test_build_single():
  dl_and_prepare = _build('mnist')
  assert dl_and_prepare.call_count == 1

  dl_and_prepare = _build('mnist:3.0.1')
  assert dl_and_prepare.call_count == 1

  with pytest.raises(tfds.core.load.DatasetNotFoundError):
    _build('unknown_dataset')

  with pytest.raises(AssertionError, match='cannot be loaded at version 1.0.0'):
    _build('mnist:1.0.0')  # Can only built the last version

  with pytest.raises(ValueError, match='not have config'):
    _build('mnist --config_idx 0')

  # Keyword arguments also possible
  dl_and_prepare = _build('--datasets mnist')
  assert dl_and_prepare.call_count == 1


def test_build_multiple():
  # Multiple datasets can be built in a single call
  dl_and_prepare = _build('mnist imagenet2012 cifar10')
  assert dl_and_prepare.call_count == 3

  # Keyword arguments also possible
  dl_and_prepare = _build('mnist --datasets imagenet2012 cifar10')
  assert dl_and_prepare.call_count == 3


def test_build_dataset_configs():
  # By default, all configs are build
  dl_and_prepare = _build('trivia_qa')
  assert dl_and_prepare.call_count == 4

  # If config is set, only the defined config is generated

  # --config_idx
  dl_and_prepare = _build('trivia_qa --config_idx=0')
  assert dl_and_prepare.call_count == 1

  # --config
  dl_and_prepare = _build('trivia_qa --config unfiltered.nocontext')
  assert dl_and_prepare.call_count == 1

  # name/config
  dl_and_prepare = _build('trivia_qa/unfiltered.nocontext')
  assert dl_and_prepare.call_count == 1

  with pytest.raises(ValueError, match='Config should only be defined once'):
    _build('trivia_qa/unfiltered.nocontext --config_idx=0')

  with pytest.raises(ValueError, match='greater than number of configs'):
    _build('trivia_qa --config_idx 100')


def test_exclude_datasets():
  # Exclude all datasets except 2
  all_ds = [b for b in tfds.list_builders() if b not in ('mnist', 'cifar10')]
  all_ds_str = ','.join(all_ds)

  dl_and_prepare = _build(f'--exclude_datasets {all_ds_str}')
  assert dl_and_prepare.call_count == 2

  with pytest.raises(ValueError, match='--exclude_datasets can\'t be used'):
    dl_and_prepare = _build('mnist --exclude_datasets cifar10')


def test_build_overwrite(mock_default_data_dir: pathlib.Path):  # pylint: disable=redefined-outer-name
  data_dir = mock_default_data_dir / 'mnist/3.0.1'
  data_dir.mkdir(parents=True)
  metadata_path = tfds.core.tfds_path(
      'testing/test_data/dataset_info/mnist/3.0.1'
  )

  for f in metadata_path.iterdir():  # Copy metadata files.
    data_dir.joinpath(f.name).write_text(f.read_text())

  # By default, will skip generation if the data already exists
  dl_and_prepare = _build('mnist')
  assert dl_and_prepare.call_count == 1  # Called, but no-op
  assert data_dir.exists()

  dl_and_prepare = _build('mnist --overwrite')
  assert dl_and_prepare.call_count == 1
  assert not data_dir.exists()  # Previous data-dir has been removed
