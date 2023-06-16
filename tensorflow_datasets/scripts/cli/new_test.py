# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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
from tensorflow_datasets.scripts.cli import new


def _run_cli(cmd: str) -> None:
  main.main(main._parse_flags([''] + cmd.split()))


def test_new_without_args(capsys):
  # Dataset name is required argument
  with pytest.raises(SystemExit):
    _run_cli('new')

  captured = capsys.readouterr()
  assert 'the following arguments are required: dataset_name' in captured.err


def test_new_invalid_name():
  # Dataset name is required argument
  error_message = (
      'Invalid dataset name. It should be a valid Python class name.'
  )
  invalid_names = ['foo-15', '15foo']
  for invalid_name in invalid_names:
    with pytest.raises(ValueError) as execution_info:
      _run_cli('new ' + invalid_name)
    assert execution_info.value.args[0] == error_message


def test_new_outside_tfds(tmp_path: pathlib.Path):
  """Test adding a new dataset in an external repository."""
  _run_cli(f'new my_dataset --dir {str(tmp_path)}')

  filenames = [f.name for f in (tmp_path / 'my_dataset').iterdir()]
  assert sorted(filenames) == [
      'CITATIONS.bib',
      'README.md',
      'TAGS.txt',
      '__init__.py',
      'checksums.tsv',
      'dummy_data',
      'my_dataset_dataset_builder.py',
      'my_dataset_dataset_builder_test.py',
  ]

  # If the dataset already exists, raise an error
  with pytest.raises(FileExistsError):
    _run_cli(f'new my_dataset --dir {str(tmp_path)}')


def test_new_in_tfds(tmp_path: pathlib.Path):
  """Test adding a new dataset in the TFDS repository."""
  tmp_path = tmp_path / 'tensorflow_datasets' / 'image'
  _run_cli(f'new my_dataset --dir {str(tmp_path)}')

  filenames = [f.name for f in (tmp_path / 'my_dataset').iterdir()]
  assert sorted(filenames) == [
      'CITATIONS.bib',
      'README.md',
      'TAGS.txt',
      '__init__.py',
      'checksums.tsv',
      'dummy_data',
      'my_dataset_dataset_builder.py',
      'my_dataset_dataset_builder_test.py',
  ]
