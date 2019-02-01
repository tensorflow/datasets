"""Provides `StaticShapedTensor` and `DynamicShapedTensor`.

These are designed for composition with other `FeatureConnector`s whose internal
representation is unable to represent shape, e.g. run length encoded features.
"""

import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core.features import feature


def _assert_is_feature(connector, name):
  if not isinstance(connector, feature.FeatureConnector):
      raise ValueError(
          "%s must be a `FeatureConnector` but got %s"
          % (name, connector))


def _num_unknown_dims(shape):
  return shape.count(None)


class DynamicShapedTensor(feature.FeaturesDict):
  """Connector adapter for converting flat connectors to dynamically tensors.

  Example use case: (B)RLE connector of images/voxel grids of variable size.

  Encoding is achieved by saving the array's encoded flattened data and its
  shape.

  Decoding is achieved by reshaping the decoded flattened data.
  """
  def __init__(self, flat_feature, shape=None):
    """Adapt the shape of the given `flat_feature` dynamically.

    Saves the flat data produced by `flat_feature` and shape of each example
    to file. If shape is not None, this also performs checks at encoding time
    to ensure the number of elements of each example is consistent with the
    given shape.

    Args:
      flat_feature: `FeatureConnector` providing flattened encoding/decoding.
      shape: any known shape information, e.g. if `flat_feature` is for
        rgb images, this might be (None, None, 3).
    """
    _assert_is_feature(flat_feature, "`flat_feature")
    self._flat_feature = flat_feature
    if shape is not None:
      shape = tuple(None if s == -1 else s for s in shape)
      if _num_unknown_dims(shape) < 2:
        raise ValueError(
          "shapes with less than 2 unknown dimensions should be implemented "
          "with `StaticShapedTensor`, got %s" % str(shape))
    self._shape = shape
    self._num_elements = 1 if shape is None else np.prod(
      tuple(s for s in shape if s is not None))

    super(DynamicShapedTensor, self).__init__(dict(
        flat_values=flat_feature,
        shape=feature.Tensor(shape=(None,), dtype=tf.int64)))

  def encode_example(self, example_data):
    """Encode the shape and the encoding of the flattened array.

    If any shape information was provided in the constructor, this also checks
    the number of elements in `example_data` is appropriate. For example, if
    shape from the constructor was (None, None, 3), this checks the number of
    elements of `example_data` is a multiple of 3.

    Args:
      example_data: numpy array

    Returns:
      dict:
        "shape": example_data.shape
        "flat_values": flat_feature's encoding of the example_data.flattened()

    Raises
      `ValueError` is the number of elements of example_data is incompatible
      with shape information provided in the constructor.
    """
    shape = example_data.shape
    flat_values = example_data.flatten()
    if flat_values.shape[0] % self._num_elements != 0:
      raise ValueError(
        "example_data has %d elements, but shape is %s"
        % (flat_values.shape[0], str(self._shape)))

    return super(DynamicShapedTensor, self).encode_example(
        dict(shape=shape, flat_values=flat_values))

  def decode_example(self, tfexample_data):
    data = super(DynamicShapedTensor, self).decode_example(
        tfexample_data)
    return tf.reshape(data["flat_values"], data["shape"])

  def get_tensor_info(self):
    return feature.TensorInfo(
        shape=self._shape,
        dtype=self._flat_feature.get_tensor_info().dtype)


class StaticShapedTensor(feature.FeatureConnector):
  """FeatureConnector for converting flat connectors to static shaped tensors.

  Output shape may have at most 1 unknown dimension.

  Example use case: (B)RLE connector of images/voxel grids of constant size.

  No shape information is saved directly in the datasets.
  """
  def __init__(self, flat_feature, shape):
    """Adapt the shape of the given `flat_feature` statically.

    Args:
      flat_feature: `FeatureConnector` providing flattened encoding/decoding.
      shape: shape of each input/output. Any `-1` values will be converted to
        `None`s. May contain at most one unknown dimension.

    Raises:
      ValueError if `shape` has more than 1 unknown dimension.
    """
    _assert_is_feature(flat_feature, "`flat_feature")
    self._flat_feature = flat_feature
    self._shape = tuple(None if s == -1 else s for s in shape)
    n_unknowns = _num_unknown_dims(self._shape)
    if n_unknowns > 1:
      raise ValueError(
        "`shape` can have at most 1 unknown dimension, got %s. "
        "Consider using DynamicShapedTensor" % shape)
    n_total = np.prod(
      [s for s in self._shape if s is not None], dtype=np.int64)
    if n_unknowns == 0:
      self._element_count_validator = (lambda n: n == n_total)
    else:
      self._element_count_validator = (lambda n: (n % n_total) == 0)

  def get_serialized_info(self):
    return self._flat_feature.get_serialized_info()

  def get_tensor_info(self):
    return feature.TensorInfo(
        shape=self._shape,
        dtype=self._flat_feature.get_tensor_info().dtype)

  def encode_example(self, example_data):
    """Get the encoding of the flattened array.

    Flattens `example_data` and checks the number of elements is consistent with
    the shape provided in the constructor.

    Args:
      example_data: example to be encoded.

    Returns:
      `flat_feature`'s encoding of flattened example_data.

    Raises:
      ValueError if the number of elements in example_data is inconsistent with
      the shape provided in constructor.
    """
    example_data = example_data.flatten()
    n_elements = example_data.shape[0]
    if not self._element_count_validator(n_elements):
      raise ValueError(
        "example had %d elements but shape is %s" % (n_elements, self._shape))
    return self._flat_feature.encode_example(example_data)

  def decode_example(self, tfexample_data):
    flat_example = self._flat_feature.decode_example(tfexample_data)
    shape = tuple(-1 if s is None else s for s in self._shape)
    return tf.reshape(flat_example, shape)


def ShapedTensor(flat_feature, shape):
  """Get `(Static|Dynamic)ShapedTensor` depending on shape.

  Args:
    flat_feature: `FeatureConnector` providing flattened encoding/decoding.
    shape: `tf.TensorShape` (or anything convertible to it) or `None`.

  Returns:
    `StaticTensor` if `shape` has at most 1 unknown dimension, otherwise a
      `DynamicTensor` wrapping `flat_feature`
  """
  if shape is None or _num_unknown_dims(shape) > 1:
    return DynamicShapedTensor(flat_feature, shape)
  else:
    return StaticShapedTensor(flat_feature, shape)
