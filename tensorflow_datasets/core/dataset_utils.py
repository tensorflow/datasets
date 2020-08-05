# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""Utilities for dealing with tf.data.Dataset."""

import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import tf_compat
from tensorflow_datasets.core import utils


def _eager_dataset_iterator(dataset):
  for item in dataset:
    flat = tf.nest.flatten(item)
    flat = [t if isinstance(t, tf.RaggedTensor) else t.numpy() for t in flat]
    yield tf.nest.pack_sequence_as(item, flat)


def _graph_dataset_iterator(ds_iter, graph=None):
  """Constructs a Python generator from a tf.data.Iterator."""
  with utils.maybe_with_graph(graph, create_if_none=False):
    init = ds_iter.initializer
    ds_item = ds_iter.get_next()
  with utils.nogpu_session(graph) as sess:
    sess.run(init)
    while True:
      try:
        yield sess.run(ds_item)
      except tf.errors.OutOfRangeError:
        break


def as_numpy(dataset, *, graph=None):
  """Converts a `tf.data.Dataset` to an iterable of NumPy arrays.

  `as_numpy` converts a possibly nested structure of `tf.data.Dataset`s
  and `tf.Tensor`s to iterables of NumPy arrays and NumPy arrays, respectively.

  Note that because TensorFlow has support for ragged tensors and NumPy has
  no equivalent representation,
  [`tf.RaggedTensor`s](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)
  are left as-is for the user to deal with them (e.g. using `to_list()`).
  In TF 1 (i.e. graph mode), `tf.RaggedTensor`s are returned as
  `tf.ragged.RaggedTensorValue`s.

  Example:

  ```
  ds = tfds.load(name="mnist", split="train")
  ds_numpy = tfds.as_numpy(ds)  # Convert `tf.data.Dataset` to Python generator
  for ex in ds_numpy:
    # `{'image': np.array(shape=(28, 28, 1)), 'labels': np.array(shape=())}`
    print(ex)
  ```

  Args:
    dataset: a possibly nested structure of `tf.data.Dataset`s and/or
      `tf.Tensor`s.
    graph: `tf.Graph`, optional, explicitly set the graph to use.

  Returns:
    A structure matching `dataset` where `tf.data.Dataset`s are converted to
    generators of NumPy arrays and `tf.Tensor`s are converted to NumPy arrays.
  """
  nested_ds = dataset
  del dataset

  # Flatten
  flat_ds = tf.nest.flatten(nested_ds)
  flat_np = []

  # Type check for Tensors and Datasets
  for ds_el in flat_ds:
    types = [type(el) for el in flat_ds]
    types = tf.nest.pack_sequence_as(nested_ds, types)
    if not (
        isinstance(ds_el, (tf.Tensor, tf.RaggedTensor)) or
        tf_compat.is_dataset(ds_el)):
      raise ValueError("Arguments to as_numpy must be tf.Tensors or "
                       "tf.data.Datasets. Got: %s" % types)

  if tf.executing_eagerly():
    # Eager mode
    for ds_el in flat_ds:
      if isinstance(ds_el, tf.Tensor):
        np_el = ds_el.numpy()
      elif isinstance(ds_el, tf.RaggedTensor):
        np_el = ds_el
      elif tf_compat.is_dataset(ds_el):
        np_el = _eager_dataset_iterator(ds_el)
      else:
        assert False
      flat_np.append(np_el)
  else:
    # Graph mode

    # First create iterators for datasets
    with utils.maybe_with_graph(graph, create_if_none=False):
      ds_iters = [
          tf.compat.v1.data.make_initializable_iterator(ds_el)
          for ds_el in flat_ds if tf_compat.is_dataset(ds_el)
      ]
    ds_iters = [_graph_dataset_iterator(ds_iter, graph) for ds_iter in ds_iters]

    # Then create numpy arrays for tensors
    with utils.nogpu_session(graph) as sess:  # Shared session for tf.Tensor
      # Calling sess.run once so that randomness is shared.
      np_arrays = sess.run([tensor for tensor in flat_ds
                            if not tf_compat.is_dataset(tensor)])

    # Merge the dataset iterators and np arrays
    iter_ds = iter(ds_iters)
    iter_array = iter(np_arrays)
    flat_np = [
        next(iter_ds) if tf_compat.is_dataset(ds_el) else next(iter_array)
        for ds_el in flat_ds
    ]

  # Nest
  return tf.nest.pack_sequence_as(nested_ds, flat_np)


def dataset_shape_is_fully_defined(ds):
  output_shapes = tf.compat.v1.data.get_output_shapes(ds)
  return all([ts.is_fully_defined() for ts in tf.nest.flatten(output_shapes)])


def features_shape_is_fully_defined(features):
  return all([tf.TensorShape(info.shape).is_fully_defined() for info in
              tf.nest.flatten(features.get_tensor_info())])
