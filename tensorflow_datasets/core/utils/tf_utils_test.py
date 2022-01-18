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

"""Tests for tensorflow_datasets.core.utils.tf_utils."""

import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core.utils import tf_utils


class TfUtilsTest(testing.TestCase):

  @testing.run_in_graph_and_eager_modes()
  def test_graph_runner(self):
    graph_runner = tf_utils.TFGraphRunner()

    output = graph_runner.run(tf.nn.relu, [1, 1, -1, -1, 1])
    self.assertAllEqual(output, [1, 1, 0, 0, 1])

    output = graph_runner.run(tf.nn.relu, [-1, -1, -1, 1, 1])
    self.assertAllEqual(output, [0, 0, 0, 1, 1])

    # Cache should have been re-used, so should only contains one GraphRun
    # Ideally there should be two separate @tf.eager.run_test_in_graph() and
    # @tf.eager.run_test_in_eager() to avoid logic on the test. But haven't
    # found it.
    if not tf.executing_eagerly():
      self.assertEqual(len(graph_runner._graph_run_cache), 1)
    else:
      self.assertEqual(len(graph_runner._graph_run_cache), 0)

    # Different signature (different shape), so new GraphRun created
    output = graph_runner.run(tf.nn.relu, [-1, 1, 1])
    self.assertAllEqual(output, [0, 1, 1])
    if not tf.executing_eagerly():
      self.assertEqual(len(graph_runner._graph_run_cache), 2)
    else:
      self.assertEqual(len(graph_runner._graph_run_cache), 0)


def test_shapes_are_compatible():
  assert tf_utils.shapes_are_compatible(
      {'a': {
          'b': (28, 28, 3)
      }},
      {'a': {
          'b': (None, None, 3)
      }},
  )
  assert not tf_utils.shapes_are_compatible(
      {'a': {
          'b': (28, 28, 3)
      }},
      {'a': {
          'b': (None, 27, 3)
      }},
  )


def test_is_np_sub_dtype():
  assert tf_utils.is_np_sub_dtype(np.int32, np.integer)
  assert tf_utils.is_np_sub_dtype(np.int64, np.integer)
  assert tf_utils.is_np_sub_dtype(np.float, np.floating)
  assert not tf_utils.is_np_sub_dtype(np.int64, np.floating)
  assert not tf_utils.is_np_sub_dtype(np.float, np.integer)


def test_is_same_tf_dtype():
  assert tf_utils.is_same_tf_dtype(tf.int32, tf.int32)
  assert not tf_utils.is_same_tf_dtype(tf.int32, tf.int64)
  assert not tf_utils.is_same_tf_dtype(tf.int64, tf.int32)


def test_merge_shape():
  tensor = tf.constant([28, 28, 3])
  np_shape = (None, None, 3)
  actual = tf_utils.merge_shape(tensor, np_shape)
  assert actual == (tf.constant(28), tf.constant(28), 3)


if __name__ == '__main__':
  testing.test_main()
