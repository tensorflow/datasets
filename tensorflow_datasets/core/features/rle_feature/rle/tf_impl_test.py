from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

import tensorflow_datasets.core.features.rle_feature.rle.tf_impl as brle
import tensorflow_datasets.core.features.rle_feature.rle.shared_tests as st



class BlreTfTest(tf.test.TestCase):
  @property
  def impl(self):
    return brle

  def assert_array_equal(self, x, y, *args, **kwargs):
    return self.assertAllEqual(x, y, *args, **kwargs)

  def dense_logical_not(self, x):
    return tf.logical_not(x)

  def dense_length(self, x):
    assert(len(x.shape) == 1)
    return tf.shape(x)[0]

#   def test_encode_decode(self):
#     st.test_encode_decode(self)

#   def test_decode_encode(self):
#     st.test_decode_encode(self)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_brle_logical_not(self):
    st.test_brle_logical_not(self)

#   def test_maybe_pad_brle(self):
#     st.test_maybe_pad_brle(self)

#   def test_merge_brle_lengths(self):
#     st.test_merge_brle_lengths(self)

#   def test_split_long_brle_lengths(self):
#     st.test_split_long_brle_lengths(self)

#   def test_split_merge(self):
#     st.test_split_merge(self)

#   def test_encode(self):
#     st.test_encode(self)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_brle_to_dense(self):
    st.test_brle_to_dense(self)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_brle_length(self):
    st.test_brle_length(self)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_rle_length(self):
    st.test_rle_length(self)

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_rle_to_dense(self):
    st.test_rle_to_dense(self)


if __name__ == '__main__':
  tf.test.main()
