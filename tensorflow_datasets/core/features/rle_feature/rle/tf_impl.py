"""Tensorflow encode/decode/utility implementations."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


def brle_length(brle):
  return tf.reduce_sum(brle)


def rle_length(rle):
  return tf.reduce_sum(rle[1::2])


def brle_logical_not(brle):
  """Get the BRLE encoding of the `logical_not`ed decoding of brle.

  Equivalent to `encode(tf.logical_not(decode(brle)))` but highly optimized.
  Actual implementation just pads brle with a 0 on each end.

  Args:
    brle: rank 1 int tensor of
  """
  return tf.pad(brle, [[1, 1]])


def brle_to_dense(brle, vals=None):
  """Decode binary run length encoded data.

  Args:
    brle: binary run length encoded data, 1D tensor of int dtype
    vals (optional): length-2 tensor/array/tuple made up of
        (false_val, true_val).

  Returns:
    Dense representation, rank-1 tensor with dtype the same as vals or `tf.bool`
      if `vals is None`.
  """
  brle = tf.convert_to_tensor(brle)
  if not brle.dtype.is_integer:
    raise TypeError("`brle` must be of integer type.")
  if not brle.shape.ndims == 1:
    raise TypeError("`brle` must be a rank 1 tensor.")
  enc_false, enc_true = tf.unstack(tf.reshape(brle, (-1, 2)), axis=1)

  n_false = tf.reduce_sum(enc_false)
  n_true = tf.reduce_sum(enc_true)
  if vals is None:
    false_vals = tf.zeros((n_false,), dtype=tf.bool)
    true_vals = tf.ones((n_true,), dtype=tf.bool)
  else:
    vals = tf.convert_to_tensor(vals)
    if vals.shape.ndims != 1:
      raise ValueError("`vals` must be rank 1 tensor.")
    if vals.shape[0] != 2:
      raise ValueError("`vals` must have exactly 2 entries.")

    false_val, true_val = tf.unstack(vals, axis=0)
    false_vals = tf.fill([n_false], false_val)
    true_vals = tf.fill([n_true], true_val)

  ragged_false = tf.RaggedTensor.from_row_lengths(false_vals, enc_false)
  ragged_true = tf.RaggedTensor.from_row_lengths(true_vals, enc_true)

  ragged_all = tf.concat([ragged_false, ragged_true], axis=1)
  return ragged_all.values


def tf_repeat(values, counts):
  """Tensorflow implementation of np.repeat.

  Currently uses `tf.py_function`.
  """
  import numpy as np
  def f(values, counts):
    return np.repeat(values.numpy(), counts.numpy())

  return tf.py_function(f, [values, counts], values.dtype, name='repeat')


def rle_to_dense(rle, dtype=tf.int64):
  """Convert run length encoded data to dense.

  Note current implementation uses `tf.py_function` in `tf_repeat`.
  """
  rle = tf.convert_to_tensor(rle)
  values, counts = tf.unstack(tf.reshape(rle, (-1, 2)), axis=-1)
  return tf_repeat(values, counts)
