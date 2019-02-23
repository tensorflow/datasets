from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

from tensorflow_datasets.core.features.run_length_encoded_feature.rle import tf_impl
from tensorflow_datasets.core.features.run_length_encoded_feature.rle import np_impl
from tensorflow_datasets.testing import test_utils
from tensorflow_datasets.core import tf_compat
tf.compat.v1.enable_eager_execution()


def random_rle_encoding(n=20, max_value=255, dtype=np.uint8):
  return (np.random.uniform(size=(n,),)*(max_value-1) + 1).astype(np.uint8)


def random_brle_encoding(n=20, max_value=255, dtype=np.uint8):
  return (np.random.uniform(size=(n,)) * (max_value-1) + 1).astype(dtype)


class RlreTfTest(tf.test.TestCase):

  def assert_array_equal(self, x, y, *args, **kwargs):
    if isinstance(x, tf.Tensor):
      x = self.evaluate(x)
    if isinstance(y, tf.Tensor):
      y = self.evaluate(y)
    return self.assertAllEqual(x, y, *args, **kwargs)

  @test_utils.run_in_graph_and_eager_modes()
  def test_brle_logical_not(self):
    original = random_brle_encoding(dtype=np.int64)
    notted = tf_impl.brle_logical_not(original)
    dense_notted = tf_impl.brle_to_dense(notted)
    dense_original = tf_impl.brle_to_dense(original)
    self.assert_array_equal(
        dense_notted, tf.logical_not(dense_original))

  @test_utils.run_in_graph_and_eager_modes()
  def test_brle_to_dense(self):
    self.assert_array_equal(
      tf_impl.brle_to_dense(np.array([300, 200, 1000, 0], dtype=np.int64)),
      [False]*300 + [True]*200 + [False]*1000)
    self.assert_array_equal(
      tf_impl.brle_to_dense(
          np.array(
            [255, 0, 45, 200, 255, 0, 255, 0, 255, 0, 235, 0], dtype=np.int64)),
      [False]*300 + [True]*200 + [False]*1000)

  @test_utils.run_in_graph_and_eager_modes()
  def test_brle_length(self):
    enc = random_brle_encoding(dtype=np.int64)
    dec = tf_impl.brle_to_dense(enc)
    self.assert_array_equal(tf.shape(dec)[0], tf_impl.brle_length(enc))

  @test_utils.run_in_graph_and_eager_modes()
  def test_rle_length(self):
    self.assert_array_equal(
      tf_impl.rle_length(
        [0, 5, 1, 3, 0, 6]), tf_impl.brle_length([5, 3, 6, 0]))

  @test_utils.run_in_graph_and_eager_modes()
  def test_rle_to_dense(self):
    self.assert_array_equal(
      tf_impl.rle_to_dense([5, 3, 4, 10]), [5]*3 + [4]*10)
    self.assert_array_equal(
      tf_impl.rle_to_dense([5, 300, 4, 100]), [5]*300 + [4]*100)

  @test_utils.run_in_graph_and_eager_modes()
  def test_brle_encode_decode(self):
    small = np.array([False]*500 + [True]*1000 + [False], dtype=bool)
    rand = np.random.uniform(size=(10000,)) > 0.05
    for original in [small, rand]:
      for dtype in [np.uint8, np.int64]:
        enc = np_impl.dense_to_brle(original, dtype=dtype)
        dec = tf_impl.brle_to_dense(enc)
        self.assert_array_equal(original, dec)

  @test_utils.run_in_graph_and_eager_modes()
  def test_brle_decode_encode(self):
    small = np.array([3, 5, 5, 10, 2, 1], dtype=np.int64)
    rand = random_brle_encoding()
    for original in [small, rand]:
      for dtype in [np.uint8, np.int64]:
        dec = tf_impl.brle_to_dense(original)
        enc = np_impl.dense_to_brle(self.evaluate(dec), dtype=dtype)
        self.assert_array_equal(original, enc)

  @test_utils.run_in_graph_and_eager_modes()
  def test_rle_encode_decode(self):
    small = np.array([3]*500 + [5]*1000 + [2], dtype=np.uint8)
    rand = (np.random.uniform(size=(10000,)) > 0.05).astype(np.uint8)
    for original in [small, rand]:
      for dtype in [np.uint8, np.int64]:
        enc = np_impl.dense_to_rle(original, dtype=dtype)
        dec = tf_impl.rle_to_dense(enc)
        self.assert_array_equal(original, dec)

  @test_utils.run_in_graph_and_eager_modes()
  def test_rle_decode_encode(self):
    small = [3, 5, 5, 10, 2, 1]
    rand = random_rle_encoding()
    for original in [small, rand]:
      for dtype in [np.uint8, np.int64]:
        dec = tf_impl.brle_to_dense(original)
        enc = np_impl.dense_to_brle(self.evaluate(dec), dtype=dtype)
        self.assert_array_equal(original, enc)

  @test_utils.run_in_graph_and_eager_modes()
  def test_tf_repeat(self):
    values = [1, 2, 3]
    repeats = [3, 2, 1]
    expected = [1, 1, 1, 2, 2, 3]
    self.assert_array_equal(tf_impl.tf_repeat(values, repeats), expected)


if __name__ == '__main__':
  tf.test.main()
