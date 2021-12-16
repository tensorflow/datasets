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

"""Tests for tensorflow_datasets.core.load.

Note: `load.py` code was previously in `registered.py`, so some of the tests
are still on `registered_test.py`.
"""

from unittest import mock

import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import load
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import utils
from tensorflow_datasets.core import visibility


@visibility.set_availables_tmp([
    visibility.DatasetType.COMMUNITY_PUBLIC,
])
def test_community_public_load():
  with mock.patch(
      'tensorflow_datasets.core.community.community_register.list_builders',
      return_value=['ns:ds'],
  ), mock.patch(
      'tensorflow_datasets.core.community.community_register.builder_cls',
      return_value=testing.DummyDataset,
  ):
    assert load.list_builders() == ['ns:ds']

    # Builder is correctly returned
    assert load.builder_cls('ns:ds') is testing.DummyDataset
    assert isinstance(load.builder('ns:ds'), testing.DummyDataset)
