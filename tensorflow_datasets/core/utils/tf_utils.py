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

"""TensorFlow utils."""

from __future__ import annotations

import collections
import contextlib
from typing import Any, Union

import numpy as np
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import tree_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

# Struct containing a graph for the TFGraphRunner
GraphRun = collections.namedtuple(
    'GraphRun', 'graph, session, placeholder, output'
)

# Struct containing the run args, kwargs
RunArgs = collections.namedtuple('RunArgs', 'fct, input')


class TFGraphRunner(object):
  """Run in session mode or Eager mode.

  This is a compatibility util between graph and eager TensorFlow.

  The graph runner allow to run function defining small TensorFlow graphs:
   * In eager mode: The function is simply run eagerly and the result is
     returned
   * In graph mode: The first time, the function is compiled in a new graph,
     then, every time the same function will be called, the cached graph and
     session will be run.

  Ideally, one graph runner should only be used with a single function to avoid
  having too many opened session in session mode.
  Limitations:
   * Currently the graph runner only support function with single input
     and output. Support for more complex function could be added and should be
     relatively straightforward.
   * A different graph is created for each input shape, so it isn't really
     adapted for dynamic batch size.

  Usage:
    graph_runner = TFGraphRunner()
    output = graph_runner.run(tf.sigmoid, np.ones(shape=(5,)))
  """

  __slots__ = ['_graph_run_cache']

  def __init__(self):
    """Constructor."""
    # Cache containing all compiled graph and opened session. Only used in
    # non-eager mode.
    self._graph_run_cache = {}

  def __getstate__(self):
    return {}

  def __setstate__(self, state):
    self.__init__(**state)

  def run(self, fct, input_):
    """Execute the given TensorFlow function."""
    # TF 2.0
    if tf.executing_eagerly():
      return fct(input_).numpy()
    # TF 1.0
    else:
      # Should compile the function if this is the first time encountered
      if not isinstance(input_, np.ndarray):
        input_ = np.array(input_)
      run_args = RunArgs(fct=fct, input=input_)
      signature = self._build_signature(run_args)
      if signature not in self._graph_run_cache:
        graph_run = self._build_graph_run(run_args)
        self._graph_run_cache[signature] = graph_run
      else:
        graph_run = self._graph_run_cache[signature]

      # Then execute the cached graph
      return graph_run.session.run(
          graph_run.output,
          feed_dict={graph_run.placeholder: input_},
      )

  def _build_graph_run(self, run_args):
    """Create a new graph for the given args."""
    # Could try to use tfe.py_func(fct) but this would require knowing
    # information about the signature of the function.

    # Create a new graph:
    with tf.Graph().as_default() as g:
      # Create placeholder
      input_ = run_args.input
      placeholder = tf.compat.v1.placeholder(
          dtype=input_.dtype, shape=input_.shape
      )
      output = run_args.fct(placeholder)
    return GraphRun(
        session=raw_nogpu_session(g),
        graph=g,
        placeholder=placeholder,
        output=output,
    )

  def _build_signature(self, run_args):
    """Create a unique signature for each fct/inputs."""
    return (id(run_args.fct), run_args.input.dtype, run_args.input.shape)

  def __del__(self):
    # Close all sessions
    for graph_run in self._graph_run_cache.values():
      graph_run.session.close()


def convert_to_shape(shape: Any) -> type_utils.Shape:
  """Converts a shape to a TFDS shape."""
  if isinstance(shape, tuple):
    return shape
  if isinstance(shape, tf.TensorShape):
    return tuple(shape.as_list())
  if isinstance(shape, list):
    return tuple(shape)
  raise ValueError(
      f'Shape of type {type(shape)} with content {shape} is not supported!'
  )


@py_utils.memoize(maxsize=1000)
def assert_shape_match(
    shape1: type_utils.Shape, shape2: type_utils.Shape
) -> None:
  """Ensure shape1 matches the pattern given by shape2.

  Ex:
    assert_shape_match((64, 64, 3), (None, None, 3))

  Args:
    shape1 (tuple): Static shape
    shape2 (tuple): Dynamic shape (can contain None)
  """
  if shape1 is None or shape2 is None:
    if shape1 != shape2:
      raise ValueError(f'Shapes {shape1} and {shape2} must have the same rank')
    return
  rank1 = len(shape1)
  rank2 = len(shape2)
  if rank1 != rank2:
    raise ValueError(f'Shapes {shape1} and {shape2} must have the same rank')
  for dimension1, dimension2 in zip(shape1, shape2):
    if dimension1 is None or dimension2 is None:
      continue
    if dimension1 != dimension2:
      raise ValueError(f'Shapes {shape1} and {shape2} are incompatible')


def assert_tf_shape_match(
    shape1: tf.TensorShape, shape2: tf.TensorShape
) -> None:
  if shape1.rank is None or shape2.rank is None:
    raise ValueError(
        'Shapes must have known rank. Got %s and %s.'
        % (shape1.rank, shape2.rank)
    )
  shape1.assert_same_rank(shape2)
  shape1.assert_is_compatible_with(shape2)


def shapes_are_compatible(
    shapes0: type_utils.TreeDict[type_utils.Shape],
    shapes1: type_utils.TreeDict[type_utils.Shape],
) -> bool:
  """Returns True if all shapes are compatible."""
  # Use `py_utils.map_nested` instead of `tree_utils.map_structure` as shapes
  # are tuple/list.
  shapes0 = py_utils.map_nested(tf.TensorShape, shapes0, dict_only=True)
  shapes1 = py_utils.map_nested(tf.TensorShape, shapes1, dict_only=True)
  all_values = tree_utils.map_structure(
      lambda s0, s1: s0.is_compatible_with(s1),
      shapes0,
      shapes1,
  )
  return all(tf.nest.flatten(all_values))


def normalize_shape(
    shape: Union[type_utils.Shape, tf.TensorShape]
) -> type_utils.Shape:
  """Normalize `tf.TensorShape` to tuple of int/None."""
  if isinstance(shape, tf.TensorShape):
    return tuple(shape.as_list())  # pytype: disable=attribute-error
  else:
    assert isinstance(shape, tuple)
    return shape


def merge_shape(
    tf_shape: Union[tf.Tensor, np.ndarray], np_shape: type_utils.Shape
):
  """Returns the most static version of the shape.

  Static `None` values are replaced by dynamic `tf.Tensor` values.

  Example:

  ```
  merge_shape(
      tf_shape=tf.constant([28, 28, 3]),
      np_shape=(None, None, 3),
  ) == (tf.Tensor(numpy=28), tf.Tensor(numpy=28), 3)
  ```

  Args:
    tf_shape: The tf.Tensor containing the shape (e.g. `tf.shape(x)`)
    np_shape: The static shape tuple (e.g. `(None, None, 3)`)

  Returns:
    A tuple like np_shape, but with `None` values replaced by `tf.Tensor` values
  """
  assert_shape_match(tf_shape.shape, (len(np_shape),))
  return tuple(
      tf_shape[i] if dim is None else dim for i, dim in enumerate(np_shape)
  )


@contextlib.contextmanager
def nogpu_session(graph=None):
  """tf.Session context manager, hiding GPUs."""
  # We don't use the with construction because we don't want the Session to be
  # installed as the "default" session.
  sess = raw_nogpu_session(graph)
  yield sess
  sess.close()


def raw_nogpu_session(graph=None):
  """tf.Session, hiding GPUs."""
  config = tf.compat.v1.ConfigProto(device_count={'GPU': 0})
  return tf.compat.v1.Session(config=config, graph=graph)


@contextlib.contextmanager
def maybe_with_graph(graph=None, create_if_none=True):
  """Eager-compatible Graph().as_default() yielding the graph."""
  if tf.executing_eagerly():
    yield None
  else:
    if graph is None and create_if_none:
      graph = tf.Graph()

    if graph is None:
      yield None
    else:
      with graph.as_default():
        yield graph
