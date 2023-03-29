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

"""Tests for np_utils."""

from tensorflow_datasets.core.utils import np_utils


def test_is_notebook():
  assert np_utils.to_np_shape(()) == ()  # pylint: disable=g-explicit-bool-comparison
  assert np_utils.to_np_shape((1, 2, 3)) == (1, 2, 3)
  assert np_utils.to_np_shape((None, 2, 3)) == (-1, 2, 3)
  assert np_utils.to_np_shape((None, None, None)) == (-1, -1, -1)
