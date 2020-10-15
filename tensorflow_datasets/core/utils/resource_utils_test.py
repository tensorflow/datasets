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

"""Tests for tensorflow_datasets.core.resource_utils."""

import io
import os
import pathlib
import zipfile

import pytest

from tensorflow_datasets.core.utils import resource_utils


def make_zip_file() -> zipfile.ZipFile:
  """Returns an in-memory zip file."""
  data = io.BytesIO()
  zf = zipfile.ZipFile(data, 'w')
  zf.writestr('a.txt', b'content of a')
  zf.writestr('b/c.txt', b'content of c')
  zf.writestr('b/d/e.txt', b'content of e')
  zf.writestr('b/f.txt', b'content of f')
  zf.writestr('g/h/i.txt', b'content of i')
  zf.filename = 'alpharep.zip'
  return zf


def test_resource_path():
  path = resource_utils.ResourcePath(make_zip_file())
  assert path.joinpath('b/c.txt').read_text() == 'content of c'
  sub_dirs = list(path.joinpath('b').iterdir())
  assert len(sub_dirs) == 3
  for p in sub_dirs:  # Childs should be `ResourcePath` instances
    assert isinstance(p, resource_utils.ResourcePath)


def test_resource_path_bad_usage():
  path = resource_utils.resource_path('tensorflow_datasets')
  path = path / 'core'

  # os.fspath can't be used on directories
  with pytest.raises(ValueError, match='`os.fspath` should only be called on '):
    os.path.join(path, '__init__.py')

  # But can be used on files.
  init_path = path / '__init__.py'
  path_str = os.fspath(init_path)
  assert pathlib.Path(path_str) == init_path

  # And can be used on write paths
  assert isinstance(path, resource_utils._Path)
  path = resource_utils.to_write_path(path)
  assert not isinstance(path, resource_utils._Path)
  assert os.fspath(path) == str(path)
