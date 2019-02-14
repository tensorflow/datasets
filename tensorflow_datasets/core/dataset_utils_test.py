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

"""Tests for tensorflow_datasets.core.dataset_utils."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_utils

tf.compat.v1.enable_eager_execution()


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

  def test_with_graph(self):
    with tf.Graph().as_default():
      with tf.Graph().as_default() as g:
        ds = _create_dataset(range(10))
      np_ds = dataset_utils.as_numpy(ds, graph=g)
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


if __name__ == "__main__":
  testing.test_main()
