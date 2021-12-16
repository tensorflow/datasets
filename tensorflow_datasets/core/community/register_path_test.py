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

"""Tests for tensorflow_datasets.core.community.register_path."""

import os
import pathlib
import tempfile
import textwrap

import pytest

from tensorflow_datasets import testing
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import register_path


class Ds0(testing.DummyDataset):
  pass


class Ds1(testing.DummyDataset):
  pass


@pytest.fixture(scope='module')
def dummy_register():
  """Dummy register."""
  with tempfile.TemporaryDirectory() as tmp_path:
    tmp_path = pathlib.Path(tmp_path)

    # Prepare the datasets
    # Namespace 0
    Ds0(data_dir=tmp_path / 'kaggle').download_and_prepare()
    Ds1(data_dir=tmp_path / 'kaggle2').download_and_prepare()
    # Namespace 1
    Ds0(data_dir=tmp_path / 'mlds').download_and_prepare()
    # Namespace 2: (non-existing)

    content = textwrap.dedent(f"""
        [Namespaces]
        kaggle=[
            '{os.fspath(tmp_path / 'kaggle')}',
            '{os.fspath(tmp_path / 'kaggle2')}',
        ]
        mlds='{os.fspath(tmp_path / 'mlds')}'
        other='/tmp/path/to/non-existing-path'
        """)

    dummy_path = tmp_path / 'dummy-community-datasets.toml'
    dummy_path.write_text(content)
    yield register_path.DataDirRegister(path=dummy_path)


def test_register_builder(dummy_register):  # pylint: disable=redefined-outer-name
  builder = dummy_register.builder(utils.DatasetName('kaggle:ds0'))
  assert 'kaggle' in builder.data_path.parts

  # Same dataset name can be loaded from different namespace
  builder = dummy_register.builder(utils.DatasetName('mlds:ds0'))
  assert 'mlds' in builder.data_path.parts

  builder = dummy_register.builder(
      utils.DatasetName('mlds:ds0'),
      data_dir=None,  # data_dir can be passed only if None
      version='1.0.0',
  )
  assert 'mlds' in builder.data_path.parts

  with pytest.raises(ValueError, match='`data_dir` cannot be set for'):
    dummy_register.builder(
        utils.DatasetName('mlds:ds0'), data_dir='/path/to/data_dir')

  with pytest.raises(KeyError, match='Namespace .* not found.'):
    dummy_register.builder(utils.DatasetName('non-existing-namespace:ds0'))

  with pytest.raises(registered.DatasetNotFoundError):
    dummy_register.builder(utils.DatasetName('other:ds0'))


def test_register_path_list_builders(dummy_register):  # pylint: disable=redefined-outer-name
  assert dummy_register.list_builders() == [
      'kaggle:ds0',
      'kaggle:ds1',
      'mlds:ds0',
  ]
