"""(Binary) run length encoded ((B)RLE) feature connectors.

Provides `RunLengthEncodedFeature` and `BinaryRunLengthEncodedFeature` for encoding each variant.

See `tensorflow_datasets/core/features/run_length_encoded_feature/README.md` for for details.
"""
import abc
import numpy as np
import six
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core.features.run_length_encoded_feature.rle import np_impl
from tensorflow_datasets.core.features.run_length_encoded_feature.rle import tf_impl


def _assert_dense(data, expected_dtype, expected_size):
  if (expected_size is not None and data.shape != (expected_size,)):
    raise ValueError(
      "Inconsistent number of elements in example_data, %s vs %s"
      % (data.shape, expected_size))
  if data.dtype != expected_dtype:
    raise ValueError(
      "Inconsistent dtypes, expected %s, got %s" % (expected_dtype, data.dtype))


def _assert_encoded(data, expected_dtype, expected_size, size_fn):
  shape = data.shape
  dtype = data.dtype
  if dtype != expected_dtype:
    raise ValueError(
      "encodings must have dtype %s, got %s" % (expected_dtype, dtype))
  if len(shape) != 1:
    raise ValueError("encodings must be 1D, got %s" % str(shape))
  if expected_size is not None:
    size = size_fn(data)
    if size != expected_size:
      raise ValueError(
        "encoding size is inconsistent, %d vs %d" % (size, expected_size))


class RunLengthEncodedFeatureBase(feature.FeatureConnector):
  """Abstract Base Class `FeatureConnector` class for (B)RLE 1D tensors.

  See `RunLengthEncodedFeature` and `BinaryRunLengthEncodedFeature` for
  implementations.
  """
  def __init__(self, size=None):
    """Create an instance, optionally providing size.

    Args:
      size: number of elements in the dense representation of each example. If
        not None, size checking is performed during encoding.
    """
    tf_impl._assert_required_version('`%s`' % self.__class__.__name__)
    self._size = size

  _encoded_dtype = tf.int64

  def get_serialized_info(self):
    return feature.to_serialized_field(
        tfds.features.TensorInfo(shape=(None,), dtype=self._encoded_dtype))

  def _set_dense_shape(self, dense_example):
    """Set the shape if `size` was provided in the constructor.

    If `size` was not provided, this method does nothing. `dense_example` is
    returned for convenience.
    """
    if self._size is not None:
      dense_example.set_shape((self._size,))
    return dense_example


class RunLengthEncodedFeature(RunLengthEncodedFeatureBase):
  """`FeatureConnector` for run length encoded 1D tensors."""
  def get_tensor_info(self):
    return tfds.features.TensorInfo(shape=(None,), dtype=self._encoded_dtype)

  def decode_example(self, tfexample_data):
    return self._set_dense_shape(tf_impl.rle_to_dense(tfexample_data))

  def encode_example(self, example_data):
    """Encode the given example.

    Args:
      example_data: dense int64 dense values to encode

    Returns:
      run length encoding int64 array

    Raises:
      `ValueError` if the input size is inconsistent with `size` provided in
      the constructor or the `example_data.dtype` is not int64.
    """
    # only supports dense -> rle encoding
    _assert_dense(
      example_data, self._encoded_dtype.as_numpy_dtype, self._size)
    return np_impl.dense_to_rle(
        example_data, dtype=self._encoded_dtype.as_numpy_dtype)


class BinaryRunLengthEncodedFeature(RunLengthEncodedFeatureBase):
  """`FeatureConnector` for binary run length encoded 1D tensors."""
  def get_tensor_info(self):
    return tfds.features.TensorInfo(shape=(self._size,), dtype=tf.bool)

  def decode_example(self, tfexample_data):
    return self._set_dense_shape(tf_impl.brle_to_dense(tfexample_data))

  def encode_example(self, example_data):
    """Encode the given example.

    Args:
      example_data: a numpy bool array, or the already encoded representation.

    Returns:
      binary run length encoded bool array.

    Raises:
      `ValueError` if the input is an unsupported dtype (bool or int64) and
      the corresponding size is not consistent with the value provided in the
      constructor.
    """
    if not hasattr(example_data, "dtype"):
      raise ValueError("`example_data` must have `dtype` attribute.")
    if example_data.dtype == np.bool:
      # assume dense
      _assert_dense(example_data, np.bool, self._size)
      return np_impl.dense_to_brle(
        example_data, dtype=self._encoded_dtype.as_numpy_dtype)
    else:
      # assume encoded already
      _assert_encoded(
        example_data, self._encoded_dtype.as_numpy_dtype, self._size,
        np_impl.brle_length)
      return example_data
