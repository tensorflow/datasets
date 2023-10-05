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

import numpy as np
from tensorflow_datasets.core.utils import np_utils


def test_is_notebook():
  assert np_utils.to_np_shape(()) == ()  # pylint: disable=g-explicit-bool-comparison
  assert np_utils.to_np_shape((1, 2, 3)) == (1, 2, 3)
  assert np_utils.to_np_shape((None, 2, 3)) == (-1, 2, 3)
  assert np_utils.to_np_shape((None, None, None)) == (-1, -1, -1)


def test_np_map_fn():
  # Scalar to scalar.
  add_ten = lambda i: i + 10
  np.testing.assert_array_equal(
      np_utils.np_map_fn(add_ten, np.array([0, 1, 2])), np.array([10, 11, 12])
  )

  # Dicts to scalar.
  operation_on_dict = lambda d: d['a'] + d['b'] if d['a'] % 2 == 0 else 0
  result = np_utils.np_map_fn(
      operation_on_dict,
      {
          'a': np.array([0, 1, 2]),
          'b': np.array([5, 6, 7]),
      },
  )
  expected = np.array([5, 0, 9])
  np.testing.assert_array_equal(result, expected)

  # Dicts to dicts.
  operation_on_dict = lambda _: {'c': 1, 'd': 2}
  result = np_utils.np_map_fn(
      operation_on_dict,
      {
          'a': np.array([0, 1, 2]),
          'b': np.array([5, 6, 7]),
      },
  )
  expected = {
      'c': np.array([1, 1, 1]),
      'd': np.array([2, 2, 2]),
  }
  assert len(result) == 2
  np.testing.assert_array_equal(result['c'], expected['c'])
  np.testing.assert_array_equal(result['d'], expected['d'])
