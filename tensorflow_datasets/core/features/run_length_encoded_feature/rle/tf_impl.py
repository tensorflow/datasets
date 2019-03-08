"""Tensorflow encode/decode/utility implementations for run length encodings."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core import tf_compat


def tf_repeat(values, repeats):
  values = tf.convert_to_tensor(values)
  repeats = tf.convert_to_tensor(repeats)

  if values.shape.ndims != 1:
    raise ValueError('values must be rank 1, got shape %s' % values.shape)
  if repeats.shape.ndims != 1:
    raise ValueError('repeats must be rank 1, got shape %s' % repeats.shape)
  if not repeats.dtype.is_integer:
    raise ValueError('repeats must be an integer, got %s' % repeats.dtype)

  try:
    from tensorflow.python.ops.ragged.ragged_util import repeat
    return repeat(values, repeats, axis=0)
  except ImportError:
    return _foldl_repeat(values, repeats)


def _foldl_repeat(values, repeats):
  """Repeat using `tf.foldl` with `TensorArray` concatenation.

  Mostly just a fallback in case of issues importing `ragged_util.repeat`.
  The ragged implementation is significantly faster for small-to-medium size
  arrays, though benchmarking indicates this may be faster for generating arrays
  of ~200k blocks of ~1k elements each or more.
  """
  size = values.shape[0]
  element_shape = (None,) + tuple(values.shape[1:])
  acc0 = tf.TensorArray(
      dtype=values.dtype, size=size, dynamic_size=False,
      element_shape=element_shape, infer_shape=False)

  def fold_fn(out, args):
    index, acc = out
    repeat, value = args
    value = tf.fill((repeat,), value)
    acc = acc.write(index, value)
    return index + 1, acc

  acc = tf.foldl(
    fold_fn, (repeats, values), initializer=(0, acc0),
    parallel_iterations=8, back_prop=False)[1]
  return acc.concat()


def _assert_is_rle(rle):
  if not rle.dtype.is_integer:
    raise ValueError("rle must be integer type, got %s" % rle.dtyp)
  if rle.shape.ndims != 1:
    raise ValueError("rle must be flat, got shape %s" % (rle.shape))


def brle_length(brle):
  """Length of dense form of binary run-length-encoded input.

  Efficient implementation of `len(brle_to_dense(brle))`."""
  return tf.reduce_sum(brle)


def rle_length(rle):
  """Length of dense form of run-length-encoded input.

  Efficient implementation of `len(rle_to_dense(rle))`."""
  return tf.reduce_sum(rle[1::2])


def brle_logical_not(brle):
  """Get the BRLE encoding of the `logical_not`ed decoding of brle.

  Equivalent to `dense_to_brle(tf.logical_not(brle_to_dense(brle)))` but highly
  optimized. Actual implementation just pads brle with a 0 on each end.

  Args:
    brle: rank 1 int tensor of ints.
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
  _assert_is_rle(brle)
  # alternating True/False
  values = tf.cast(tf.range(tf.size(brle)) % 2, tf.bool)
  return tf_repeat(values, brle)


def rle_to_dense(rle, dtype=tf.int64):
  """Convert run length encoded data to dense.

  Note current implementation uses `tf.py_function` in `tf_repeat`.
  """
  rle = tf.convert_to_tensor(rle)
  _assert_is_rle(rle)
  values, repeats = tf.unstack(tf.reshape(rle, (-1, 2)), axis=-1)
  return tf_repeat(values, repeats)
