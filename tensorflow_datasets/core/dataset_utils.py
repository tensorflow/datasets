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

"""Utilities for dealing with tf.data.Dataset."""

from __future__ import annotations

import collections.abc
import functools
import typing
from typing import Any, Callable, Iterable, Iterator, Union

from etils import enp
from etils.etree import nest as etree
import numpy as np
from tensorflow_datasets.core import logging as tfds_logging
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.core.utils.lazy_imports_utils import tree

Tree = type_utils.Tree
Tensor = type_utils.Tensor

if typing.TYPE_CHECKING:
  TensorflowElem = Union[None, Tensor, tf.data.Dataset]
  NumpyValue = Union[None, tf.RaggedTensor, np.ndarray, np.generic, bytes]
else:
  TensorflowElem = Any
  NumpyValue = Any
NumpyElem = Union[NumpyValue, Iterable[NumpyValue]]


class _IterableDataset(collections.abc.Iterable):
  """Iterable which can be called multiple times."""

  def __init__(
      self,
      make_iterator_fn: Callable[..., Iterator[NumpyElem]],
      ds: Union[tf.data.Dataset, Any],
      *args: Any,
      **kwargs: Any,
  ):
    self._ds = ds
    self._make_iterator_fn = functools.partial(
        make_iterator_fn, ds, *args, **kwargs
    )

  def __len__(self) -> int:
    """Dataset length."""
    if isinstance(self._ds, tf.data.Dataset):
      return len(self._ds)
    else:
      raise TypeError(
          '__len__() is not supported for `tfds.as_numpy` datasets '
          'created in graph mode.'
      )

  def __iter__(self) -> Iterator[NumpyElem]:
    """Calling `iter(ds)` multiple times recreates a new iterator."""
    return self._make_iterator_fn()

  @property
  def element_spec(self) -> Tree[enp.ArraySpec]:
    """Numpy version of element-spec."""
    return etree.spec_like(self._ds.element_spec)


def _eager_dataset_iterator(ds: tf.data.Dataset) -> Iterator[NumpyElem]:
  for elem in ds:
    yield tree.map_structure(_elem_to_numpy_eager, elem)


def _graph_dataset_iterator(ds_iter, graph: tf.Graph) -> Iterator[NumpyElem]:
  """Constructs a Python generator from a tf.data.Iterator."""
  with graph.as_default():
    init = ds_iter.initializer
    ds_item = ds_iter.get_next()
    with utils.nogpu_session() as sess:
      sess.run(tf.compat.v1.tables_initializer())
      sess.run(init)
      while True:
        try:
          yield sess.run(ds_item)
        except tf.errors.OutOfRangeError:
          break


def _assert_ds_types(nested_ds: Tree[TensorflowElem]) -> None:
  """Assert all inputs are from valid types."""
  for el in tf.nest.flatten(nested_ds):
    if not (
        isinstance(el, (tf.Tensor, tf.RaggedTensor))
        or isinstance(el, tf.data.Dataset)
    ):
      nested_types = tree.map_structure(type, nested_ds)
      raise TypeError(
          'Arguments to as_numpy must be tf.Tensors or tf.data.Datasets. '
          f'Got: {nested_types}.'
      )


def _elem_to_numpy_eager(
    tf_el: TensorflowElem,
) -> Union[NumpyElem, Iterable[NumpyElem]]:
  """Converts a single element from tf to numpy."""
  if isinstance(tf_el, tf.Tensor):
    return tf_el._numpy()  # pytype: disable=attribute-error  # pylint: disable=protected-access
  elif isinstance(tf_el, tf.RaggedTensor):
    return tf_el
  elif isinstance(tf_el, tf.data.Dataset):
    return _IterableDataset(_eager_dataset_iterator, tf_el)
  elif tf_el is None:
    return None
  else:
    raise AssertionError(f'Unexpected element: {type(tf_el)}: {tf_el}')


def _nested_to_numpy_graph(ds_nested: Tree[TensorflowElem]) -> Tree[NumpyElem]:
  """Convert the nested structure of TF element to numpy."""
  all_ds = []
  all_arrays = []
  flat_ds = tf.nest.flatten(ds_nested)
  for elem in flat_ds:
    # Create an iterator for all datasets
    if isinstance(elem, tf.data.Dataset):
      # Capture the current graph, so calling `iter(ds)` twice will reuse the
      # graph in which `as_numpy` was created.
      graph = tf.compat.v1.get_default_graph()
      ds_iter = tf.compat.v1.data.make_initializable_iterator(elem)
      all_ds.append(_IterableDataset(_graph_dataset_iterator, ds_iter, graph))
    else:
      all_arrays.append(elem)

  # Then create numpy arrays for all tensors
  if all_arrays:
    with utils.nogpu_session() as sess:  # Shared session for tf.Tensor
      all_arrays = sess.run(all_arrays)

  # Merge the dataset iterators and np arrays
  iter_ds = iter(all_ds)
  iter_array = iter(all_arrays)
  return tf.nest.pack_sequence_as(
      ds_nested,
      [
          next(iter_ds)
          if isinstance(ds_el, tf.data.Dataset)
          else next(iter_array)
          for ds_el in flat_ds
      ],
  )


@tfds_logging.as_numpy
def as_numpy(dataset: Tree[TensorflowElem]) -> Tree[NumpyElem]:
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

  Returns:
    A structure matching `dataset` where `tf.data.Dataset`s are converted to
    generators of NumPy arrays and `tf.Tensor`s are converted to NumPy arrays.
  """
  _assert_ds_types(dataset)
  if tf.executing_eagerly():
    return tree.map_structure(_elem_to_numpy_eager, dataset)
  else:
    return _nested_to_numpy_graph(dataset)


def dataset_shape_is_fully_defined(ds):
  output_shapes = tf.compat.v1.data.get_output_shapes(ds)
  return all([ts.is_fully_defined() for ts in tf.nest.flatten(output_shapes)])


def features_shape_is_fully_defined(features):
  return all([
      tf.TensorShape(info.shape).is_fully_defined()
      for info in tf.nest.flatten(features.get_tensor_info())
  ])
