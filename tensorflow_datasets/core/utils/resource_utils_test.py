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

"""Tests for tensorflow_datasets.core.resource_utils."""

from tensorflow_datasets.core.utils import resource_utils


def test_tfds_path():
  """Test the proper suffix only, since the prefix can vary."""
  assert resource_utils.tfds_path().name == 'tensorflow_datasets'
  # assert resource_utils.tfds_write_path().name == 'tensorflow_datasets'
