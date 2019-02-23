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


def _check_size(data_size, expected_shape):
  if expected_shape is not None:
    expected_size = np.prod([s for s in expected_shape if s is not None])
    exact_size = not (None in expected_shape)
    if (exact_size and data_size != expected_size or
        data_size % expected_size != 0):
      raise ValueError(
        "encoding size %d is incompatible with expected shape %s"
        % (data_size, expected_shape))

def _check_dtype(dtype, expected_dtype):
  if dtype != expected_dtype:
    raise ValueError(
      "dtype %s does not match expected %s" % (dtype, expected_dtype))


class ShapedTensor(feature.FeatureConnector):
  """Base `FeatureConnector` class for shaped tensors.

  tfrecords do not store shapes with tensors. If a feature's shape is known
  statically (or is missing at most one dimension), the shape is stored on
  the FeatureConnector and the tfrecords store just the flat data. If two or
  more dimensions are unknown (or the number of dimensions is unknown) we store
  both the shape and flat values of each example.

  This class has overridable methods for different ways of storing the flat
  values. These are:
    * _decode_flat_values
    * _encode_flat_values
    * _get_flat_serialized_info

  You will almost certainly have to override all 3 or none.

  See RunLengthEncodedFeature / BinaryRunLengthEncodedFeature from
  tensorflow_datasets.core.features for example implementations.
  """
  def __init__(self, shape, dtype):
    """Create an instance, optionally providing shape.

    Args:
      shape: tuple of ints, common shape of all examples, or None if number of
        dimensions is unknown. This can be partially unkown. e.g. for a general
        2D image it might be (None, None). Storage is simpler if at most 1
        dimension is unknown.
      dtype: data type of decoded data.
    """
    self._dtype = dtype
    if shape is None:
      self._size_multiple = 1
      self._is_static_shape = False
    else:
      if not isinstance(shape, tuple):
        raise ValueError('shape must be None or a tuple')
      self._is_static_shape = shape.count(None) < 2
      if self._is_static_shape:
        self._reshape_shape = tuple(-1 if s is None else s for s in shape)
      shape = tf.TensorShape(shape)
    self._shape = shape

  def get_serialized_info(self):
    flat_info = self._get_flat_serialized_info()
    if self._is_static_shape:
      return flat_info
    else:
      shape_shape = (None if self._shape is None else len(self._shape),)
      shape_info = feature.to_serialized_field(
        tfds.features.TensorInfo(shape=shape_shape, dtype=tf.int64))
      return dict(
        flat_values=flat_info,
        shape=shape_info,
      )

  def get_tensor_info(self):
    return tfds.features.TensorInfo(shape=self._shape, dtype=self._dtype)

  def _decode_flat_values(self, flat_values):
    """Convert flat values stored on disk to flat values that will be reshaped.

    Defaults to a cast of the saved value.
    """
    if flat_values.dtype != self._dtype:
      flat_values = tf.cast(flat_values, self._dtype)
    return flat_values

  def _encode_flat_values(self, flat_values):
    """Convert flat values for saving to flat values to be stored on disk.

    Defaults to the identity after checking shape and dtype.
    """
    np_dtype = np.dtype(self._dtype.as_numpy_dtype)
    # Convert to numpy if possible
    if not isinstance(flat_values, np.ndarray):
      flat_values = np.array(flat_values, dtype=np_dtype)
    # Ensure the shape and dtype match
    if flat_values.dtype != np_dtype:
      raise ValueError('Dtype {} do not match {}'.format(
          flat_values.dtype, np_dtype))
    _check_size(flat_values.size, self._shape)
    # For booleans, convert to integer (tf.train.Example does not support bool)
    if flat_values.dtype == np.bool_:
      flat_values = flat_values.astype(int)
    return flat_values

  def _get_flat_serialized_info(self):
    """Get serialized_info associated with flat data."""
    return feature.to_serialized_field(
      tfds.features.TensorInfo(
        shape=(self._shape.num_elements(),), dtype=self._dtype))

  def decode_example(self, tfexample_data):
    if self._is_static_shape:
      flat_values = tfexample_data
      shape = self._reshape_shape
    else:
      shape = tfexample_data['shape']
      flat_values = tfexample_data['flat_values']
    return tf.reshape(self._decode_flat_values(flat_values), shape)

  def encode_example(self, example_data):
    """Encode the given example.

    Args:
      example_data: a tuple of (shape, flat_values) or a shaped array with shape
        consistent with that provided in the constructor.

    Returns:
      encoding, int64 array

    Raises:
      `ValueError` if the input shape is inconsistent with `shape` provided in
      the constructor.
    """
    if isinstance(example_data, tuple):
      if len(example_data) != 2:
        raise ValueError(
          'encoded_example can take a tuple of length 2 or a list/shaped array')
      shape, flat_values = example_data
    else:
      if not isinstance(example_data, np.ndarray):
        example_data = np.array(example_data, dtype=self._dtype.as_numpy_dtype)
      shape = example_data.shape
      flat_values = example_data.flatten()
    if self._shape is not None:
      if not tf.TensorShape(self._shape).is_compatible_with(shape):
        raise ValueError(
          'shape %s is incompatible with feature shape %s'
          % (shape, self._shape))
    flat_values = self._encode_flat_values(flat_values)
    if self._is_static_shape:
      return flat_values
    else:
      return dict(shape=shape, flat_values=flat_values)


class RunLengthEncodedFeatureBase(ShapedTensor):
  _encoded_dtype = tf.int64

  def _get_flat_serialized_info(self):
    return feature.to_serialized_field(
        tfds.features.TensorInfo(shape=(None,), dtype=self._encoded_dtype))


class RunLengthEncodedFeature(RunLengthEncodedFeatureBase):
  """`FeatureConnector` for run length encoded 1D tensors."""
  def __init__(self, shape):
    super(RunLengthEncodedFeature, self).__init__(shape, self._encoded_dtype)

  def _decode_flat_values(self, flat_values):
    return tf_impl.rle_to_dense(flat_values)

  def _encode_flat_values(self, example_data):
    """Encode the given example.

    Args:
      example_data: dense int64 flattened dense values to encode

    Returns:
      run length encoding int64 array

    Raises:
      `ValueError` if the input size is inconsistent with `size` provided in
      the constructor or the `example_data.dtype` is not int64.
    """
    # only supports dense -> rle encoding
    dtype = self._encoded_dtype.as_numpy_dtype
    _check_dtype(example_data.dtype, dtype)
    _check_size(example_data.size, self._shape)
    return np_impl.dense_to_rle(example_data, dtype=dtype)


class BinaryRunLengthEncodedFeature(RunLengthEncodedFeatureBase):
  """`FeatureConnector` for binary run length encoded 1D tensors."""
  def __init__(self, shape):
    super(BinaryRunLengthEncodedFeature, self).__init__(shape, tf.bool)

  def _decode_flat_values(self, flat_values):
    return tf_impl.brle_to_dense(flat_values)

  def _encode_flat_values(self, example_data):
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
    dtype = self._encoded_dtype.as_numpy_dtype
    if example_data.dtype == np.bool:
      # assume dense
      _check_size(example_data.size, self._shape)
      return np_impl.dense_to_brle(example_data, dtype=dtype)
    elif example_data.dtype == dtype:
      # assume encoded already
      _check_size(np_impl.brle_length(example_data), self._shape)
      return example_data
    else:
      raise ValueError(
        "`example_data.dtype` must be %s or %s, got %s"
        % (np.bool, dtype, example_data.dtype))
