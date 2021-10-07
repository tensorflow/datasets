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

"""Tests for tensorflow_datasets.core.dataset_utils."""

import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_utils


def _create_dataset(rng):
  return tf.data.Dataset.from_tensor_slices(list(rng))


class DatasetAsNumPyTest(testing.TestCase):

  @testing.run_in_graph_and_eager_modes()
  def test_singleton_tensor(self):
    t = tf.random.normal((10, 10))
    np_t = dataset_utils.as_numpy(t)
    self.assertEqual((10, 10), np_t.shape)
    self.assertEqual(np.float32, np_t.dtype)

  @testing.run_in_graph_and_eager_modes()
  def test_nested_tensors(self):
    t1 = tf.random.normal((10, 10))
    t2 = tf.random.normal((10, 20))
    nest_tup = (t1, t2)
    np_t1, np_t2 = dataset_utils.as_numpy(nest_tup)
    self.assertEqual((10, 10), np_t1.shape)
    self.assertEqual(np.float32, np_t1.dtype)
    self.assertEqual((10, 20), np_t2.shape)
    self.assertEqual(np.float32, np_t2.dtype)

    nest_dict = {"foo": t1, "bar": {"zoo": t2}}
    np_nest_dict = dataset_utils.as_numpy(nest_dict)
    np_t1 = np_nest_dict["foo"]
    np_t2 = np_nest_dict["bar"]["zoo"]
    self.assertEqual((10, 10), np_t1.shape)
    self.assertEqual(np.float32, np_t1.dtype)
    self.assertEqual((10, 20), np_t2.shape)
    self.assertEqual(np.float32, np_t2.dtype)

  @testing.run_in_graph_and_eager_modes()
  def test_singleton_dataset(self):
    ds = _create_dataset(range(10))
    np_ds = dataset_utils.as_numpy(ds)
    self.assertEqual(list(range(10)), [int(el) for el in list(np_ds)])
    # Iterating twice on the dataset recreate the iterator.
    self.assertEqual(list(range(10)), [int(el) for el in list(np_ds)])

    if tf.executing_eagerly():
      self.assertEqual(len(np_ds), 10)
    else:
      with self.assertRaisesWithPredicateMatch(
          TypeError, "__len__() is not supported for `tfds.as_numpy`"):
        _ = len(np_ds)

  def test_with_graph(self):
    with tf.Graph().as_default():
      ds = _create_dataset(range(10))
      np_ds = dataset_utils.as_numpy(ds)
    self.assertEqual(list(range(10)), [int(el) for el in list(np_ds)])

  @testing.run_in_graph_and_eager_modes()
  def test_singleton_dataset_with_nested_elements(self):
    ds = _create_dataset(range(10))
    ds = ds.map(lambda el: {"a": el, "b": el + 1, "c": (el + 2, el + 3)})
    np_ds = dataset_utils.as_numpy(ds)
    for i, el in enumerate(np_ds):
      self.assertEqual(i, el["a"])
      self.assertEqual(i + 1, el["b"])
      self.assertEqual(i + 2, el["c"][0])
      self.assertEqual(i + 3, el["c"][1])

  @testing.run_in_graph_and_eager_modes()
  def test_nested_dataset_sequential_access(self):
    ds1 = _create_dataset(range(10))
    ds2 = _create_dataset(range(10, 20))
    np_ds = dataset_utils.as_numpy((ds1, {"a": ds2}))
    np_ds1 = np_ds[0]
    np_ds2 = np_ds[1]["a"]

    self.assertEqual(list(range(10)), [int(el) for el in list(np_ds1)])
    self.assertEqual(list(range(10, 20)), [int(el) for el in list(np_ds2)])

  @testing.run_in_graph_and_eager_modes()
  def test_nested_dataset_simultaneous_access(self):
    ds1 = _create_dataset(range(10))
    ds2 = _create_dataset(range(10, 20))
    np_ds = dataset_utils.as_numpy((ds1, {"a": ds2}))
    np_ds1 = np_ds[0]
    np_ds2 = np_ds[1]["a"]

    for i1, i2 in zip(np_ds1, np_ds2):
      self.assertEqual(i2, int(i1) + 10)

  @testing.run_in_graph_and_eager_modes()
  def test_nested_dataset_nested_elements(self):
    ds1 = _create_dataset(range(10))
    ds1 = ds1.map(lambda el: {"a": el, "b": el + 1, "c": (el + 2, el + 3)})
    ds2 = _create_dataset(range(10, 20))
    np_ds = dataset_utils.as_numpy((ds1, {"a": ds2}))
    np_ds1 = np_ds[0]
    np_ds2 = np_ds[1]["a"]

    for i, (el1, el2) in enumerate(zip(np_ds1, np_ds2)):
      self.assertEqual(i + 10, el2)
      self.assertEqual(i, el1["a"])
      self.assertEqual(i + 1, el1["b"])
      self.assertEqual(i + 2, el1["c"][0])
      self.assertEqual(i + 3, el1["c"][1])

  @testing.run_in_graph_and_eager_modes()
  def test_tensors_match(self):
    t = tf.random.uniform(
        shape=(50, 3),
        maxval=1000,
        dtype=tf.int32,
    )

    ds = dataset_utils.as_numpy({"a": t, "b": t})
    # sess.run() should be called a single time for all input. Otherwise input
    # and target may not match
    self.assertAllEqual(ds["a"], ds["b"])

  @testing.run_in_graph_and_eager_modes()
  def test_ragged_tensors(self):
    rt = tf.ragged.constant([
        [1, 2, 3],
        [],
        [4, 5],
    ])
    rt = dataset_utils.as_numpy(rt)

    if not tf.executing_eagerly():
      # Output of `sess.run(rt)` is a `RaggedTensorValue` object
      self.assertIsInstance(rt, tf.compat.v1.ragged.RaggedTensorValue)
    else:
      self.assertIsInstance(rt, tf.RaggedTensor)

    self.assertAllEqual(rt, tf.ragged.constant([
        [1, 2, 3],
        [],
        [4, 5],
    ]))

  @testing.run_in_graph_and_eager_modes()
  def test_ragged_tensors_ds(self):

    def _gen_ragged_tensors():
      # Yield the (flat_values, rowids)
      yield ([0, 1, 2, 3], [0, 0, 0, 2])  # ex0
      yield ([], [])  # ex1
      yield ([4, 5, 6], [0, 1, 1])  # ex2

    ds = tf.data.Dataset.from_generator(
        _gen_ragged_tensors,
        output_types=(tf.int64, tf.int64),
        output_shapes=((None,), (None,)))
    ds = ds.map(tf.RaggedTensor.from_value_rowids)

    rt0, rt1, rt2 = list(dataset_utils.as_numpy(ds))
    self.assertAllEqual(rt0, [
        [0, 1, 2],
        [],
        [
            3,
        ],
    ])
    self.assertAllEqual(rt1, [])
    self.assertAllEqual(rt2, [[4], [5, 6]])

  def test_none_ds(self):
    ds = tf.data.Dataset.range(10)
    ds = ds.map(lambda x: (x, None))
    exs = list(dataset_utils.as_numpy(ds))
    self.assertAllEqual(exs, [(x, None) for x in range(10)])


if __name__ == "__main__":
  testing.test_main()
