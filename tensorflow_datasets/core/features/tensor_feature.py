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

"""Feature connector."""

import enum
from typing import Union
import zlib

import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib

Json = utils.Json
Shape = utils.Shape


class Encoding(enum.Enum):
  """Encoding type of `tfds.features.Tensor`.

  For higher dimension tensors, it is recommended to define the encoding as
  zlib or bytes to save space on disk.

  Attributes:
    NONE: No compression (default). bools/integers will be upcasted to int64 as
      this is the only integer format supported by the
      [`tf.train.Example`](https://www.tensorflow.org/tutorials/load_data/tfrecord#tftrainexample)
        protobufs in which examples are saved.
    BYTES: Stored as raw bytes (avoid the upcasting from above).
    ZLIB: The raw bytes are compressed using zlib.
  """
  NONE = 'none'
  BYTES = 'bytes'
  ZLIB = 'zlib'
  # Could eventually add GZIP too (as supported by `tf.io.decode_compressed`
  # but feel redundant with ZLIB.


class Tensor(feature_lib.FeatureConnector):
  """`FeatureConnector` for generic data of arbitrary shape and type."""

  # For backward compatibility with the `features.json` saved by
  # `FeatureConnector.save_config`
  ALIASES = ['tensorflow_datasets.core.features.feature.Tensor']

  def __init__(
      self,
      *,
      shape: utils.Shape,
      dtype: tf.dtypes.DType,
      # TODO(tfds): Could add an Encoding.AUTO to automatically compress
      # tensors using some heuristic. However, careful about backward
      # compatibility.
      # Would require some `DatasetInfo.api_version = 1` which would be
      # increased when triggering backward-incompatible changes.
      encoding: Union[str, Encoding] = Encoding.NONE,
  ):
    """Construct a Tensor feature.

    Args:
      shape: Tensor shape
      dtype: Tensor dtype
      encoding: Internal encoding. See `tfds.features.Encoding` for available
        values.
    """
    self._shape = tuple(shape)
    self._dtype = dtype
    if isinstance(encoding, str):
      encoding = encoding.lower()
    self._encoding = Encoding(encoding)

    self._encoded_to_bytes = self._encoding != Encoding.NONE
    self._dynamic_shape = self._shape.count(None) > 1

    if self._dtype == tf.string and self._encoded_to_bytes:
      raise NotImplementedError(
          'tfds.features.Tensor() does not support `encoding=` when '
          'dtype=tf.string. Please open a PR if you need this feature.')

  def get_tensor_info(self) -> feature_lib.TensorInfo:
    """See base class for details."""
    return feature_lib.TensorInfo(shape=self._shape, dtype=self._dtype)

  def get_serialized_info(self):
    """See base class for details."""
    if self._encoded_to_bytes:  # Values encoded (stored as bytes)
      serialized_spec = feature_lib.TensorInfo(shape=(), dtype=tf.string)
    else:
      serialized_spec = feature_lib.TensorInfo(
          shape=self._shape,
          dtype=self._dtype,
      )

    # Dynamic shape, need an additional field to restore the shape after
    # de-serialization.
    if self._dynamic_shape:
      return {
          'shape':
              feature_lib.TensorInfo(
                  shape=(len(self._shape),),
                  dtype=tf.int32,
              ),
          'value':
              serialized_spec,
      }
    return serialized_spec

  def encode_example(self, example_data):
    """See base class for details."""
    # TODO(epot): Is there a better workaround ?
    # It seems some user have non-conventional use of tfds.features.Tensor where
    # they defined shape=(None, None) even if it wasn't supported.
    # For backward compatibility, the check is moved inside encode example.
    if self._dynamic_shape and not self._encoded_to_bytes:
      raise ValueError('Multiple unknown dimensions Tensor require to set '
                       "`Tensor(..., encoding='zlib')` (or 'bytes'). "
                       f'For {self}')

    np_dtype = np.dtype(self.dtype.as_numpy_dtype)
    if isinstance(example_data, tf.Tensor):
      raise TypeError(
          f'Error encoding: {example_data!r}. `_generate_examples` should '
          'yield `np.array` compatible values, not `tf.Tensor`')
    if not isinstance(example_data, np.ndarray):
      example_data = np.array(example_data, dtype=np_dtype)
    # Ensure the shape and dtype match
    if example_data.dtype != np_dtype:
      raise ValueError('Dtype {} do not match {}'.format(
          example_data.dtype, np_dtype))

    shape = example_data.shape
    utils.assert_shape_match(shape, self._shape)

    # Eventually encode the data
    if self._encoded_to_bytes:
      example_data = example_data.tobytes()
      if self._encoding == Encoding.ZLIB:
        example_data = zlib.compress(example_data)

    # For dynamically shaped tensors, also save the shape (the proto
    # flatten all values so we need a way to recover the shape).
    if self._dynamic_shape:
      return {
          'value': example_data,
          'shape': shape,
      }
    else:
      return example_data

  def decode_example(self, tfexample_data):
    """See base class for details."""
    if self._dynamic_shape:
      value = tfexample_data['value']
      # Extract the shape (while using static values when available)
      shape = utils.merge_shape(tfexample_data['shape'], self._shape)
    else:
      value = tfexample_data
      shape = tuple(-1 if dim is None else dim for dim in self._shape)

    if self._encoded_to_bytes:
      if self._encoding == Encoding.ZLIB:
        value = tf.io.decode_compressed(value, compression_type='ZLIB')
      value = tf.io.decode_raw(value, self._dtype)
      value = tf.reshape(value, shape)

    return value

  def decode_batch_example(self, example_data):
    """See base class for details."""
    if self._dynamic_shape or self._encoded_to_bytes:
      # For Sequence(Tensor()), use `tf.map_fn` to decode/reshape individual
      # tensors.
      return super().decode_batch_example(example_data)
    else:
      # For regular tensors, `decode_example` is a no-op so can be applied
      # directly (avoid `tf.map_fn`)
      return self.decode_example(example_data)

  def decode_ragged_example(self, example_data):
    """See base class for details."""
    if self._dynamic_shape or self._encoded_to_bytes:
      # For dynamic/bytes, we need to decode individual values, so call
      # `tf.ragged.map_flat_values`
      return super().decode_ragged_example(example_data)
    else:
      # For regular tensors, `decode_example` is a no-op so can be applied
      # directly (avoid `tf.ragged.map_flat_values overhead`)
      return self.decode_example(example_data)

  @classmethod
  def from_json_content(cls, value: Json) -> 'Tensor':
    return cls(
        shape=tuple(value['shape']),
        dtype=tf.dtypes.as_dtype(value['dtype']),
        # Use .get for backward-compatibility
        encoding=value.get('encoding', Encoding.NONE),
    )

  def to_json_content(self) -> Json:
    return {
        'shape': list(self._shape),
        'dtype': self._dtype.name,
        'encoding': self._encoding.value,
    }


def get_inner_feature_repr(feature):
  """Utils which returns the object which should get printed in __repr__.

  This is used in container features (Sequence, FeatureDict) to print scalar
  Tensor in a less verbose way `Sequence(tf.int32)` rather than
  `Sequence(Tensor(shape=(), dtype=tf.in32))`.

  Args:
    feature: The feature to dispaly

  Returns:
    Either the feature or it's inner value.
  """
  # We only print `tf.int32` rather than `Tensor(shape=(), dtype=tf.int32)`
  # * For the base `Tensor` class (and not subclass).
  # * When shape is scalar (explicit check to avoid trigger when `shape=None`).
  if type(feature) == Tensor and feature.shape == ():  # pylint: disable=unidiomatic-typecheck,g-explicit-bool-comparison
    return repr(feature.dtype)
  else:
    return repr(feature)
