"""Provides `StaticShapedTensor` and `DynamicShapedTensor`.

These are designed for composition with other `FeatureConnector`s whose internal
representation is unable to represent shape, e.g. run length encoded features.
"""

import abc
import collections
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core.features import feature


def _size(shape):
  """Number of elements in fully defined part, or 1 if None."""
  if shape is None:
    return 1
  else:
    return np.prod([1 if s is None else s for s in shape], dtype=np.int64)


def _fully_defined(shape):
  return shape is not None and not any(s is None or s == -1 for s in shape)


def _reshape_shape(shape):
  """Replace None dimensions with -1s."""
  if shape is None:
    raise ValueError("No reshape shape corresponding to None")
  return tuple(-1 if s is None else s for s in shape)


def _validate_size(source_size, target_size, target_fully_defined):
  if target_fully_defined:
    if source_size != target_size:
      raise ValueError(
        "source_size (%d) not equal to target_size (%d)" %
        (source_size, target_size))
  elif source_size % target_size != 0:
    raise ValueError(
      "source_size (%d) not divisible by target_size (%d)" %
      (source_size, target_size))


class ShapedTensorBase(feature.FeatureConnector):
  def __init__(self, base_feature, shape):
    if not isinstance(base_feature, feature.FeatureConnector):
      raise ValueError(
          "`base_feature` must be a `FeatureConnector` but got %s"
          % base_feature)
    self._base_feature = base_feature
    self._shape = shape
    base_shape = base_feature.get_tensor_info().shape
    self._base_shape = base_shape
    self._base_size = _size(base_shape)
    self._base_fully_defined = _fully_defined(base_shape)
    size = _size(shape)

    if _fully_defined(shape) != self._base_fully_defined:
      raise ValueError(
        "shape must be fully defined if `base_feature`"
        " has fully defined shape.")
    elif self._base_fully_defined:
    # both fully defined
      if size != self._base_size:
        raise ValueError(
          "Inconsistent number of elements between base (%d) and shape (%d)"
          % (self._base_size, size))
    else:
      # neither fully defined
      if not (size % self._base_size == 0 or self._base_size % size == 0):
        raise ValueError(
          "Inconsistent shapes for base (%s) and shape (%s)" %
          (str(self._base_shape), str(shape)))

  def __repr__(self):
    return (
        "ShapedTensor(base=%s, shape=%s)" % (self._base_feature, self._shape))

  @abc.abstractmethod
  def _encode_shape_and_data(self, shape, base_encoding):
    """Encode `shape` and `base_encoding` for a given example.

    Args:
      shape: validated shape of the given example
      base_encoding: output of `base_feature.encoded_example(base_data)`

    Returns:
      encoded example, i.e. expected output of `self.encode_example`.
    """
    raise NotImplementedError

  def get_tensor_info(self):
    return feature.TensorInfo(
        shape=self._shape,
        dtype=self._base_feature.get_tensor_info().dtype)

  def encode_example(self, example_data):
    """Convert `example_data` to serialized form.

    Example usage:
    ```python
    import numpy as np
    from tensorflow_datasets.core.features.rle.np_impl import rle_to_brle
    from tensorflow_datasets.core.features.rle.np_impl import rle_to_dense

    h, w = 100, 100
    base_feature = BinaryRunLengthEncodedFeature(size=h*w)
    feature = ShapedTensor(base_feature, shape=(h, w))
    run_length_encoding = [0, 9000, 1, 1000]  # not binary

    encoding = feature.encode_example(
      rle_to_dense(run_length_encoding).astype(np.bool))
    efficient_encoding = feature.encode_example(dict(
      shape=(h, w), encoding=rle_to_brle(run_length_encoding)
    ))
    np.all(encoding == efficient_encoding)  # True
    ```

    Args:
      example_data: be one of the following:
        a. numpy-like `base_data` with `shape` property and `reshape` method;
        b. a `dict` with 'shape' and 'encoding' keys; or
        c. a tuple of (shape, encoding)

        If (a), the `base_data` should be a valid input to
        `base_feature.encode_example` after reshaping. If (b) or (c), then
        `encoding` should be a valid input to `base_feature.encode_example`.

    Returns:
      output of `self._encode_shape_and_data`.

    Raises:
      `ValueError` if example_data is a dict with additional/insufficient keys,
      a tuple with not exactly 2 elements, or if `shape` is inconsistent with
      value provided in the constructor, or anything
      `base_feature.encode_example` could raise.
    """
    if isinstance(example_data, dict):
      keys = 'shape', 'encoding'
      if not all(k in example_data for k in keys) and len(example_data) == 2:
        raise ValueError(
          "`example_data` must have keys (%s) if a dict" % str(keys))
      shape, data = (example_data[k] for k in keys)
    elif isinstance(example_data, tuple):
      shape, data = example_data
    else:
      # assume is numpy-like, i.e. has `shape` property and `reshape` method
      shape = example_data.shape
      data = example_data
      if self._base_shape is not None:
        data = data.reshape(_reshape_shape(self._base_shape))
    _validate_size(_size(shape), self._base_size, self._base_fully_defined)
    base_encoding = self._base_feature.encode_example(data)
    return self._encode_shape_and_data(shape, base_encoding)


class DynamicShapedTensor(ShapedTensorBase):
  """Connector adapter for converting base connectors to dynamically tensors.

  Example use case: (B)RLE connector of images/voxel grids of variable size.

  Encoding is achieved by saving the array's encoded base data and its
  shape.

  Decoding is achieved by reshaping the decoded base data.
  """
  def __init__(self, base_feature, shape=None):
    """Adapt the shape of the given `base_feature` dynamically.

    Saves the base data produced by `base_feature` and shape of each example
    to file. If shape is not None, this also performs checks at encoding time
    to ensure the number of elements of each example is consistent with the
    given shape.

    Args:
      base_feature: `FeatureConnector` providing base encoding/decoding.
      shape: any known shape information, e.g. if `base_feature` is for
        rgb images, this might be (None, None, 3).
    """
    super(DynamicShapedTensor, self).__init__(base_feature, shape)
    shape = self._shape
    if shape is not None:
      if shape.count(None) < 2:
        raise ValueError(
          "shapes with less than 2 unknown dimensions should be implemented "
          "with `StaticShapedTensor`, got %s" % str(shape))

  def _encode_shape_and_data(self, shape, base_encoding):
    """Encode `shape` and `base_encoding` for a given example.

    Args:
      shape: validated shape of the given example
      base_encoding: output of `base_feature.encoded_example(base_data)`

    Returns:
      dict with args packed under 'shape' and 'base_feature' keys.
    """
    return dict(shape=shape, base_feature=base_encoding)

  def decode_example(self, tfexample_data):
    base_value = tfexample_data["base_feature"]
    base_value = self._base_feature.decode_example(base_value)
    return tf.reshape(base_value, tfexample_data["shape"])

  def get_serialized_info(self):
    shape = self._shape
    if shape is None:
      shape = (None,)
    return {
      "shape": feature.to_serialized_field(
          feature.Tensor(shape=shape, dtype=tf.int64)),
      "base_feature": self._base_feature.get_serialized_info(),
    }


class StaticShapedTensor(ShapedTensorBase):
  """FeatureConnector for converting base connectors to static shaped tensors.

  Output shape may have at most 1 unknown dimension.

  Example use case: (B)RLE features of images/voxel grids of constant size.

  No shape information is saved directly in the datasets.
  """
  def __init__(self, base_feature, shape):
    """Adapt the shape of the given `base_feature` statically.

    Args:
      base_feature: `FeatureConnector` providing base encoding/decoding.
      shape: shape of each input/output.

    Raises:
      ValueError if `shape` has more than 1 unknown dimension.
    """
    super(StaticShapedTensor, self).__init__(base_feature, shape)
    shape = self._shape
    if shape.count(None) > 1:
      raise ValueError(
        "`shape` can have at most 1 unknown dimension, got %s. "
        "Consider using DynamicShapedTensor" % str(shape))

  def get_serialized_info(self):
    return self._base_feature.get_serialized_info()

  def _encode_shape_and_data(self, shape, base_encoding):
    """Encode `shape` and `base_encoding` for a given example.

    `StaticShapeTensor`s do not save shape to file, so this simply returns
    the base_encoding unchanged.

    Args:
      shape: validated shape of the given example
      base_encoding: output of `base_feature.encoded_example(base_data)`

    Returns:
      base_encoding
    """
    return base_encoding

  def decode_example(self, tfexample_data):
    base_example = self._base_feature.decode_example(tfexample_data)
    return tf.reshape(base_example, _reshape_shape(self._shape))


def ShapedTensor(base_feature, shape):
  """Get `(Static|Dynamic)ShapedTensor` depending on shape.

  Args:
    base_feature: `FeatureConnector` providing base encoding/decoding.
    shape: `tf.TensorShape` (or anything convertible to it) or `None`.

  Returns:
    `StaticTensor` if `shape` has at most 1 unknown dimension, otherwise a
      `DynamicTensor` wrapping `base_feature`
  """
  if shape is None or shape.count(None) > 1:
    return DynamicShapedTensor(base_feature, shape)
  else:
    return StaticShapedTensor(base_feature, shape)
