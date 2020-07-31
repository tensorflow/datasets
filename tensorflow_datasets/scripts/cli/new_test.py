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

"""Tests for tensorflow_datasets.scripts.cli.main."""

import pathlib

import pytest

from tensorflow_datasets.scripts.cli import main


def _run_cli(cmd: str) -> None:
  main.main(main._parse_flags([''] + cmd.split()))


def test_new_wrong_args(capsys):
  # Dataset name is required argument
  with pytest.raises(SystemExit):
    _run_cli('new')

  captured = capsys.readouterr()
  assert 'the following arguments are required: dataset_name' in captured.err


def test_new_outside_tfds(tmp_path: pathlib.Path):
  """Test adding a new dataset in an external repository."""
  _run_cli(f'new my_dataset --dir {str(tmp_path)}')

  filenames = [f.name for f in (tmp_path / 'my_dataset').iterdir()]
  assert sorted(filenames) == [
      '__init__.py',
      'checksums.tsv',
      'dummy_data',
      'my_dataset.py',
      'my_dataset_test.py',
  ]

  # If the dataset already exists, raise an error
  with pytest.raises(FileExistsError):
    _run_cli(f'new my_dataset --dir {str(tmp_path)}')


def test_new_in_tfds(tmp_path: pathlib.Path):
  """Test adding a new dataset in the TFDS repository."""
  tmp_path = tmp_path / 'tensorflow_datasets' / 'image'
  print('BEFORE', tmp_path)
  _run_cli(f'new my_dataset --dir {str(tmp_path)}')
  print('AFTER', tmp_path)

  filenames = [f.name for f in (tmp_path / 'my_dataset').iterdir()]
  assert sorted(filenames) == [
      '__init__.py',
      'checksums.tsv',
      'dummy_data',
      'my_dataset.py',
      'my_dataset_test.py',
  ]
