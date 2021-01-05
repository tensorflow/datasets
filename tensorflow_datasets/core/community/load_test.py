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

"""Tests for tensorflow_datasets.core.community.load."""

import pytest
from tensorflow_datasets.core import load as core_load
from tensorflow_datasets.core.community import load


def test_import():
  builder_cls = load.builder_cls_from_module(
      'tensorflow_datasets.testing.dummy_dataset.dummy_dataset'
  )
  assert builder_cls.__name__ == 'DummyDataset'

  # Module should have been cached
  builder_cls_2 = load.builder_cls_from_module(
      'tensorflow_datasets.testing.dummy_dataset.dummy_dataset'
  )
  assert builder_cls is builder_cls_2

  from tensorflow_datasets.testing.dummy_dataset import dummy_dataset  # pylint: disable=g-import-not-at-top

  assert builder_cls is dummy_dataset.DummyDataset
  assert builder_cls.__name__ not in core_load.list_builders()


def test_bad_import():
  # Invalid module
  with pytest.raises(ImportError):
    load.builder_cls_from_module('tensorflow_datasets_invalid')

  # Valid module, but bad dataset
  with pytest.raises(ValueError, match='Could not load DatasetBuilder'):
    load.builder_cls_from_module('tensorflow_datasets')
