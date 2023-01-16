# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for error_utils."""
import pytest

from tensorflow_datasets.core.utils import error_utils


def test_default_empty_context_stack():
  with pytest.raises(ValueError, match=''):
    with error_utils.reraise_with_context(ValueError):
      raise ValueError


def test_raise_with_context():
  with pytest.raises(ValueError, match='Adding context'):
    with error_utils.reraise_with_context(ValueError):
      error_utils.add_context('Adding context')
      raise ValueError


def test_raise_with_multiple_contexts():
  with pytest.raises(
      ValueError, match='\n'.join(['Adding context', 'Adding context 2'])
  ):
    with error_utils.reraise_with_context(ValueError):
      error_utils.add_context('Adding context')
      error_utils.add_context('Adding context 2')
      raise ValueError


def test_do_not_raise_error_if_nested_reraise_with_context():
  with pytest.raises(
      ValueError, match='\n'.join(['Adding context', 'Adding context 2'])
  ):
    with error_utils.reraise_with_context(ValueError):
      error_utils.add_context('Adding context')
      with error_utils.reraise_with_context(ValueError):
        error_utils.add_context('Adding context 2')
        raise ValueError


def test_add_context_outside_contextmanager():
  with pytest.raises(
      AttributeError,
      match=(
          'add_context called outside of reraise_with_context contextmanager.'
      ),
  ):
    error_utils.add_context('Adding context')
