# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from __future__ import annotations

import enum
import functools
from typing import Any, Optional, Protocol, Tuple, TypeVar, Union
import zlib

from etils import enp
import numpy as np
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils import np_utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

Json = utils.Json
Shape = utils.Shape

T = TypeVar('T')


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
      dtype: type_utils.TfdsDType,
      # TODO(tfds): Could add an Encoding.AUTO to automatically compress
      # tensors using some heuristic. However, careful about backward
      # compatibility.
      # Would require some `DatasetInfo.api_version = 1` which would be
      # increased when triggering backward-incompatible changes.
      encoding: Union[str, Encoding] = Encoding.NONE,
      doc: feature_lib.DocArg = None,
      serialized_dtype: Optional[type_utils.TfdsDType] = None,
      serialized_shape: Optional[utils.Shape] = None,
      minimum: Optional[type_utils.NpArrayOrScalar] = None,
      maximum: Optional[type_utils.NpArrayOrScalar] = None,
      optional: bool = False,
  ):
    """Construct a Tensor feature.

    Args:
      shape: Tensor shape
      dtype: Tensor dtype
      encoding: Internal encoding. See `tfds.features.Encoding` for available
        values.
      doc: Documentation of this feature (e.g. description).
      serialized_dtype: Tensor dtype. Used to validate that serialized examples
        have this dtype. If `None` then defaults to `dtype`
      serialized_shape: Tensor shape. Used to validate that serialized examples
        have this shape. If `None` then defaults to `shape`
      minimum: Tensor minimum. This can be useful to specify
        `tf_agents.specs.BoundedArraySpec` for example.
      maximum: Tensor maximum. This can be useful to specify
        `tf_agents.specs.BoundedArraySpec` for example.
      optional: Whether the feature is optional and accepts None values.
    """
    super().__init__(doc=doc)
    self._shape = tuple(shape)
    self._dtype = dtype_utils.cast_to_numpy(dtype)
    self._serialized_dtype = dtype_utils.cast_to_numpy(
        serialized_dtype or self._dtype
    )
    self._serialized_shape = tuple(
        self._shape if serialized_shape is None else serialized_shape
    )
    if isinstance(encoding, str):
      encoding = encoding.lower()
    self._encoding = Encoding(encoding)

    self._encoded_to_bytes = self._encoding != Encoding.NONE
    self._dynamic_shape = self._shape.count(None) > 1

    self._minimum = minimum
    self._maximum = maximum
    self._optional = optional

    if dtype_utils.is_string(self._dtype) and self._encoded_to_bytes:
      raise NotImplementedError(
          'tfds.features.Tensor() does not support `encoding=` when '
          'dtype is string. Please open a PR if you need this feature.'
      )

  @py_utils.memoize()
  def get_tensor_info(self) -> feature_lib.TensorInfo:
    """See base class for details."""
    return feature_lib.TensorInfo(
        shape=self._shape,
        dtype=self._dtype,
        minimum=self._minimum,
        maximum=self._maximum,
        optional=self._optional,
        default_value=self._default_value(),
    )

  @py_utils.memoize()
  def get_serialized_info(self):
    """See base class for details."""
    if self._encoded_to_bytes:  # Values encoded (stored as bytes)
      serialized_spec = feature_lib.TensorInfo(
          shape=(),
          dtype=np.object_,
          minimum=self._minimum,
          maximum=self._maximum,
          optional=self._optional,
          default_value=self._default_value(),
      )
    else:
      serialized_spec = feature_lib.TensorInfo(
          shape=self._serialized_shape,
          dtype=self._serialized_dtype,
          minimum=self._minimum,
          maximum=self._maximum,
          optional=self._optional,
          default_value=self._default_value(),
      )

    # Dynamic shape, need an additional field to restore the shape after
    # de-serialization.
    if self._dynamic_shape:
      return {
          'shape': feature_lib.TensorInfo(
              shape=(len(self._shape),),
              dtype=np.int32,
              minimum=self._minimum,
              maximum=self._maximum,
              optional=self._optional,
              default_value=self._default_value(),
          ),
          'value': serialized_spec,
      }
    return serialized_spec

  def _default_value(self) -> Any:
    """Default value for None value when the tensor is optional."""
    if not self._optional:
      return None
    # np.object_ arrays are normalized to np.str_ with empty str.
    dtype = self._dtype if self._dtype != np.object_ else np.str_
    if dtype_utils.is_string(dtype):
      default_value = b''
    elif dtype_utils.is_integer(dtype):
      default_value = np.iinfo(dtype).min
    elif dtype_utils.is_floating(dtype):
      default_value = np.finfo(dtype).min
    elif dtype_utils.is_bool(dtype):
      default_value = False
    else:
      raise ValueError(f'Unsupported dtype: {dtype}')
    if not self._shape:
      return default_value
    return np.full(self._shape, default_value, dtype=dtype)

  def encode_example(self, example_data):
    """See base class for details."""
    if example_data is None and self._optional:
      return None
    # TODO(epot): Is there a better workaround ?
    # It seems some user have non-conventional use of tfds.features.Tensor where
    # they defined shape=(None, None) even if it wasn't supported.
    # For backward compatibility, the check is moved inside encode example.
    if self._dynamic_shape and not self._encoded_to_bytes:
      raise ValueError(
          'Multiple unknown dimensions Tensor require to set '
          "`Tensor(..., encoding='zlib')` (or 'bytes'). "
          f'For {self}'
      )

    np_dtype = self._serialized_dtype
    if np_dtype == np.bool_ and isinstance(example_data, str):
      raise TypeError(
          f'Error encoding: {example_data!r}. {example_data!r} is a string, so '
          'converting it to `bool` will always output `True`. Please, fix '
          '`_generate_examples` with a better parsing.'
      )
    if enp.lazy.has_tf and isinstance(example_data, tf.Tensor):
      raise TypeError(
          f'Error encoding: {example_data!r}. `_generate_examples` should '
          'yield `np.array` compatible values, not `tf.Tensor`'
      )
    if not isinstance(example_data, np.ndarray):
      example_data = np.array(example_data, dtype=np_dtype)
    # Ensure the shape and dtype match
    if example_data.dtype != np_dtype:
      raise ValueError(
          'Dtype {} do not match {}'.format(example_data.dtype, np_dtype)
      )

    shape = example_data.shape

    utils.assert_shape_match(shape, self._serialized_shape)

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

  def _get_value_and_shape(self, example_data):
    if self._dynamic_shape:
      value = example_data['value']
      # Extract the shape (while using static values when available)
      if enp.lazy.has_tf and isinstance(example_data['shape'], tf.Tensor):
        shape = utils.merge_shape(example_data['shape'], self._shape)
      else:
        shape = utils.merge_shape(
            example_data['shape'][: len(value)], self._shape
        )
    else:
      value = example_data
      shape = np_utils.to_np_shape(self._shape)
    if (
        self._dtype == np.uint64
        and not self._encoded_to_bytes
        and isinstance(value, np.ndarray)
    ):
      # We can only store int64 inside tf.Example, so if we had a uint64, we
      # bitcasted it to int64 at encoding time. Thus, when decoding, we need to
      # bitcast it asback to uint64.
      value = value.view(np.uint64)
    return value, shape

  def decode_example(self, tfexample_data):
    """See base class for details."""
    value, shape = self._get_value_and_shape(tfexample_data)
    decode_dtype = self.tf_dtype if self.tf_dtype != tf.uint64 else tf.int64
    if self._encoded_to_bytes:
      if self._encoding == Encoding.ZLIB:
        value = tf.io.decode_compressed(value, compression_type='ZLIB')
      value = tf.io.decode_raw(value, decode_dtype)
      if self.dtype == tf.uint64:
        value = tf.bitcast(value, tf.uint64)
      value = tf.reshape(value, shape)

    return value

  def decode_example_np(
      self, example_data: type_utils.NpArrayOrScalar
  ) -> type_utils.NpArrayOrScalar:
    example_data, shape = self._get_value_and_shape(example_data)
    if not self._encoded_to_bytes:
      if isinstance(example_data, np.ndarray) and shape:
        return example_data.reshape(shape)
      return example_data
    if self._encoding == Encoding.ZLIB:
      example_data = _execute_function_on_array_or_scalar(
          zlib.decompress, example_data
      )
    return _execute_function_on_array_or_scalar(
        _bytes_to_np_array, example_data, dtype=self._dtype, shape=shape
    )

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

  def decode_ragged_example_np(self, example_data):
    """See base class for details."""
    # See comments in `decode_ragged_example`.
    if self._dynamic_shape or self._encoded_to_bytes:
      raise NotImplementedError()
    else:
      return self.decode_example_np(example_data)

  @classmethod
  def from_json_content(
      cls, value: Union[Json, feature_pb2.TensorFeature]
  ) -> 'Tensor':
    if isinstance(value, dict):
      return cls(
          shape=tuple(value['shape']),
          dtype=feature_lib.dtype_from_str(value['dtype']),
          # Use .get for backward-compatibility
          encoding=value.get('encoding', Encoding.NONE),
          minimum=value.get('minimum', None),
          maximum=value.get('maximum', None),
          optional=value.get('optional', False),
      )
    return cls(
        shape=feature_lib.from_shape_proto(value.shape),
        dtype=feature_lib.dtype_from_str(value.dtype),
        encoding=value.encoding or Encoding.NONE,
        minimum=value.minimum if value.HasField('minimum') else None,
        maximum=value.maximum if value.HasField('maximum') else None,
        optional=value.optional,
    )

  def to_json_content(self) -> feature_pb2.TensorFeature:
    return feature_pb2.TensorFeature(
        shape=feature_lib.to_shape_proto(self._shape),
        dtype=feature_lib.dtype_to_str(self._dtype),
        encoding=self._encoding.value,
        minimum=self._minimum,
        maximum=self._maximum,
        optional=self._optional,
    )


def _bytes_to_np_array(example_data: bytes, dtype: np.dtype, shape: Tuple[int]):
  return np.frombuffer(example_data, dtype=dtype).reshape(shape)


class InputFunc(Protocol[T]):
  """This protocol is used to type _execute_function_on_array_or_scalar."""

  def __call__(
      self, example_data: type_utils.NpArrayOrScalar, *args, **kwargs
  ) -> T:
    ...


def _execute_function_on_array_or_scalar(
    function: InputFunc[T],
    data: type_utils.NpArrayOrScalar,
    *args,
    **kwargs,
) -> T:
  """Runs `function` on `data`, or each element of `data` if it's an array."""
  if isinstance(data, bytes):
    return function(data, *args, **kwargs)
  if isinstance(data, np.ndarray):
    partial_function = functools.partial(function, *args, **kwargs)
    return np.array(list(map(partial_function, data)))
  raise ValueError(
      'example should have type `bytes` or `np.ndarray(dtype=bytes)`, but'
      f' has wrong type {type(data)}'
  )


def get_inner_feature_repr(feature):
  """Utils which returns the object which should get printed in __repr__.

  This is used in container features (Sequence, FeatureDict) to print scalar
  Tensor in a less verbose way `Sequence(int32)` rather than
  `Sequence(Tensor(shape=(), dtype=int32))`.

  Args:
    feature: The feature to display

  Returns:
    Either the feature or it's inner value.
  """
  # We only print `int32` rather than `Tensor(shape=(), dtype=int32)`
  # * For the base `Tensor` class (and not subclass).
  # * When shape is scalar (explicit check to avoid trigger when `shape=None`).
  if type(feature) == Tensor and feature.shape == ():  # pylint: disable=unidiomatic-typecheck,g-explicit-bool-comparison
    return feature_lib.dtype_to_str(feature.np_dtype)
  else:
    return repr(feature)
