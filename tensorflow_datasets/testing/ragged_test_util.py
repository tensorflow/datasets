# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Test utils for tensorflow RaggedTensors.

Copied from the tensorflow/python/ops/ragged/ragged_test_util.py

TODO(epot): Delete this with the next TF public release.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

import tensorflow as tf


class RaggedTensorTestCase(tf.test.TestCase):
  """Base class for RaggedTensor test cases."""

  def _GetPyList(self, a):
    """Converts a to a nested python list."""
    if isinstance(a, tf.RaggedTensor):
      return self.evaluate(a).to_list()
    elif isinstance(a, tf.Tensor):
      a = self.evaluate(a)
      return a.tolist() if isinstance(a, np.ndarray) else a
    elif isinstance(a, np.ndarray):
      return a.tolist()
    elif isinstance(a, tf.ragged.RaggedTensorValue):
      return a.to_list()
    else:
      return np.array(a).tolist()

  def assertRaggedEqual(self, a, b):
    """Asserts that two potentially ragged tensors are equal."""
    a_list = self._GetPyList(a)
    b_list = self._GetPyList(b)
    self.assertEqual(a_list, b_list)

    if not (isinstance(a, (list, tuple)) or isinstance(b, (list, tuple))):
      a_ragged_rank = a.ragged_rank if is_ragged(a) else 0
      b_ragged_rank = b.ragged_rank if is_ragged(b) else 0
      self.assertEqual(a_ragged_rank, b_ragged_rank)

  def assertRaggedAlmostEqual(self, a, b, places=7):
    a_list = self._GetPyList(a)
    b_list = self._GetPyList(b)
    self.assertNestedListAlmostEqual(a_list, b_list, places, context='value')

    if not (isinstance(a, (list, tuple)) or isinstance(b, (list, tuple))):
      a_ragged_rank = a.ragged_rank if is_ragged(a) else 0
      b_ragged_rank = b.ragged_rank if is_ragged(b) else 0
      self.assertEqual(a_ragged_rank, b_ragged_rank)

  def assertNestedListAlmostEqual(self, a, b, places=7, context='value'):
    self.assertEqual(type(a), type(b))
    if isinstance(a, (list, tuple)):
      self.assertLen(a, len(b), 'Length differs for %s' % context)
      for i in range(len(a)):
        self.assertNestedListAlmostEqual(a[i], b[i], places,
                                         '%s[%s]' % (context, i))
    else:
      self.assertAlmostEqual(
          a, b, places,
          '%s != %s within %s places at %s' % (a, b, places, context))

  def eval_to_list(self, tensor):
    value = self.evaluate(tensor)
    if is_ragged(value):
      return value.to_list()
    elif isinstance(value, np.ndarray):
      return value.tolist()
    else:
      return value

  def _eval_tensor(self, tensor):
    if is_ragged(tensor):
      return tf.ragged.RaggedTensorValue(
          self._eval_tensor(tensor.values),
          self._eval_tensor(tensor.row_splits))
    else:
      return tf.test.TestCase._eval_tensor(self, tensor)

  @staticmethod
  def _normalize_pylist(item):
    """Convert all (possibly nested) np.arrays contained in item to list."""
    # convert np.arrays in current level to list
    if np.ndim(item) == 0:
      return item
    level = (x.tolist() if isinstance(x, np.ndarray) else x for x in item)
    _normalize = RaggedTensorTestCase._normalize_pylist  # pylint: disable=invalid-name
    return [_normalize(el) if np.ndim(el) != 0 else el for el in level]


def is_ragged(value):
  """Returns true if `value` is a ragged tensor or ragged tensor value."""
  return isinstance(value, (tf.RaggedTensor, tf.ragged.RaggedTensorValue))
