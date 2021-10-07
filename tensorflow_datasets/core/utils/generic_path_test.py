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

"""Tests for tensorflow_datasets.core.utils.generic_path."""

import os
import pathlib

from unittest import mock

from tensorflow_datasets.core.utils import generic_path
from tensorflow_datasets.core.utils import gpath
from tensorflow_datasets.core.utils import type_utils


def test_windows_encoding():
  with mock.patch('os.name', 'nt'):
    assert os.name == 'nt'

    # On windows, paths should be `WindowsGPath`
    path = generic_path.as_path('c:/Program Files/text.txt')
    assert isinstance(path, gpath.WindowsGPath)

    path = generic_path.as_path(pathlib.PosixPath('some_dir/abc'))
    assert isinstance(path, gpath.WindowsGPath)

    # Other `GPath` and `gs://` should be `PosixPurePath`
    path = generic_path.as_path('gs://some_dir/abc')
    assert not isinstance(path, gpath.WindowsGPath)
    assert isinstance(path, gpath.PosixGPath)

    # Other `GPath` and `s3://` should be `PosixPurePath`
    path = generic_path.as_path('s3://some_dir/abc')
    assert not isinstance(path, gpath.WindowsGPath)
    assert isinstance(path, gpath.PosixGPath)

    path = generic_path.as_path(gpath.PosixGPath('some_dir/abc'))
    assert not isinstance(path, gpath.WindowsGPath)
    assert isinstance(path, gpath.PosixGPath)


def test_as_path_registering():

  @generic_path.register_pathlike_cls('my_path://')
  class MyPath(gpath.PosixGPath):
    pass

  my_path = generic_path.as_path('my_path://abc')
  assert isinstance(my_path, MyPath)
  assert generic_path.as_path(my_path) is my_path


def test_as_path_new():

  p0 = type_utils.ReadWritePath('some/path/to/xyz')
  p1 = type_utils.ReadOnlyPath('some/path/to/xyz')
  p2 = generic_path.as_path('some/path/to/xyz')
  assert p0 == p1
  assert p0 == p2
  assert type(p0) is type(p1)
  assert type(p0) is type(p2)
