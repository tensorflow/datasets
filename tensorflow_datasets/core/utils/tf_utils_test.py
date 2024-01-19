# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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
import pytest
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
      {'a': {'b': (28, 28, 3)}},
      {'a': {'b': (None, None, 3)}},
  )
  assert not tf_utils.shapes_are_compatible(
      {'a': {'b': (28, 28, 3)}},
      {'a': {'b': (None, 27, 3)}},
  )


@pytest.mark.parametrize(
    ['tensor', 'np_shape', 'result'],
    [
        (
            tf.constant([28, 28, 3]),
            (None, None, 3),
            (tf.constant(28), tf.constant(28), 3),
        ),
        (np.array([28, 28, 3]), (None, None, 3), (28, 28, 3)),
    ],
)
def test_merge_shape(tensor, np_shape, result):
  assert tf_utils.merge_shape(tensor, np_shape) == result


@pytest.mark.parametrize(
    ['shape1', 'shape2'],
    [
        (None, None),
        ((None,), (None,)),
        ((1,), (1,)),
        ((None,), (1,)),
        ((1,), (None,)),
        ((1, 2), (1, 2)),
        ((1, 2), (None, None)),
        ((1, None), (None, None)),
        ((None, 2), (None, None)),
        ((None, None), (1, 2)),
        ((None, None), (1, None)),
        ((None, None), (None, 2)),
    ],
)
def test_assert_shapes_match(shape1, shape2):
  try:
    tf_utils.assert_shape_match(shape1, shape2)
  except ValueError as exception:
    raise Exception(f'test should fail for {shape1}/{shape2}') from exception


@pytest.mark.parametrize(
    ['shape1', 'shape2'],
    [
        ((1, 2), (3, 2)),
        ((1, 2), (1, 3)),
    ],
)
def test_assert_must_have_the_same_dimension(shape1, shape2):
  with pytest.raises(ValueError, match='are incompatible'):
    tf_utils.assert_shape_match(shape1, shape2)


@pytest.mark.parametrize(
    ['shape1', 'shape2'],
    [
        (None, (1,)),
        (None, (1, 2)),
        ((1,), None),
        ((1, 2), None),
        ((1,), (1, 2)),
        ((1, 2), (1,)),
    ],
)
def test_assert_must_have_the_same_rank(shape1, shape2):
  with pytest.raises(ValueError, match='must have the same rank'):
    tf_utils.assert_shape_match(shape1, shape2)


if __name__ == '__main__':
  testing.test_main()
