# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""To deserialize bytes (Example) to tf.Example."""

from __future__ import annotations

import abc
import dataclasses
from typing import Mapping, Union

import numpy as np
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

example_pb2 = tf.train
feature_pb2 = tf.train


class Parser(abc.ABC):

  @abc.abstractmethod
  def parse_example(self, serialized_example: bytes):
    raise NotImplementedError


class ExampleParser(Parser):
  """To parse Examples."""

  def __init__(self, example_specs):
    self._example_specs = example_specs
    self._flat_example_specs = utils.flatten_nest_dict(self._example_specs)
    self._nested_feature_specs = _build_feature_specs(self._flat_example_specs)
    self.flat_feature_specs = utils.flatten_nest_dict(
        self._nested_feature_specs
    )

  def parse_example(self, serialized_example):
    """Deserialize a single `tf.train.Example` proto.

    Usage:
    ```
    ds = tf.data.TFRecordDataset(filepath)
    ds = ds.map(file_adapter.parse_example)
    ```

    Args:
      serialized_example: `tf.Tensor`, the `tf.string` tensor containing the
        serialized proto to decode.

    Returns:
      example: A nested `dict` of `tf.Tensor` values. The structure and tensors
        shape/dtype match the  `example_specs` provided at construction.
    """
    # Because of RaggedTensor specs, feature_specs can be a 2-level nested dict,
    # so have to wrap `tf.io.parse_single_example` between
    # `flatten_nest_dict`/`pack_as_nest_dict`.
    # {
    #     'video/image': tf.io.FixedLenSequenceFeature(...),
    #     'video/object/bbox': {
    #         'ragged_flat_values': tf.io.FixedLenSequenceFeature(...),
    #         'ragged_row_lengths_0', tf.io.FixedLenSequenceFeature(...),
    #     },
    # }
    example = tf.io.parse_single_example(
        serialized=serialized_example,
        features=self.flat_feature_specs,
    )
    example = utils.pack_as_nest_dict(example, self._nested_feature_specs)

    example = {  # pylint:disable=g-complex-comprehension
        k: _deserialize_single_field(example_data, tensor_info)
        for k, (example_data, tensor_info) in utils.zip_dict(
            example, self._flat_example_specs
        )
    }
    # Reconstruct all nesting
    example = utils.pack_as_nest_dict(example, self._example_specs)
    return example


@dataclasses.dataclass
class ExampleParserNp(Parser):
  """Parse Examples with NumPy (without any usage of TensorFlow)."""

  example_specs: Union[
      feature_lib.TensorInfo, Mapping[str, feature_lib.TensorInfo]
  ]

  def __post_init__(self):
    self._flat_example_specs = utils.flatten_nest_dict(self.example_specs)

  def parse_example(
      self, serialized_example: bytes
  ) -> type_utils.NpArrayOrScalarDict:
    example = example_pb2.Example.FromString(serialized_example)
    np_example = _features_to_numpy(example.features, self._flat_example_specs)
    return utils.pack_as_nest_dict(np_example, self.example_specs)


def _features_to_numpy(
    features: feature_pb2.Features,
    flat_example_specs: Mapping[str, feature_lib.TensorInfo],
) -> type_utils.NpArrayOrScalarDict:
  """Parses features to NumPy type.

  Args:
    features: TensorFlow Features.
    flat_example_specs: All tensor infos in a flat dictionary.

  Returns:
    The parsed NumPy object of type: np.ndarray or np.dtype.

  Raises:
    KeyError: if `flat_example_specs` is malformed.
  """
  parsed_example = {}
  feature_map = features.feature
  for key in feature_map:
    if key not in flat_example_specs:
      raise KeyError(
          f"Malformed input: {key} is found in the feature, but not in"
          f" {flat_example_specs}"
      )
    with utils.try_reraise(f"Error wile parsing feature {key}: "):
      parsed_example[key] = _feature_to_numpy(
          feature_map[key], flat_example_specs[key], key
      )
  return parsed_example


def _feature_to_numpy(
    feature: feature_pb2.Feature,
    tensor_info: feature_lib.TensorInfo,
    feature_name: str,
) -> type_utils.NpArrayOrScalar:
  """Parses a single feature to NumPy type.

  Args:
    feature: TensorFlow Feature.
    tensor_info: Tensor info for the current feature.
    feature_name: name of the feature to convert to NumPy.

  Returns:
    The parsed NumPy object of type: np.ndarray or np.dtype.

  Raises:
    AttributeError: if the parsed feature is malformed.
    ValueError: if a scalar feature is represented by an array.
  """
  dtype = tensor_info.np_dtype
  shape = tensor_info.shape
  if None in shape:
    raise ValueError(
        f"tensors with shape ({shape}) including None are not supported when"
        " decoding with NumPy."
    )
  if feature.HasField("int64_list"):
    value_array = feature.int64_list.value
  elif feature.HasField("float_list"):
    value_array = feature.float_list.value
  elif feature.HasField("bytes_list"):
    value_array = feature.bytes_list.value
  else:
    raise AttributeError(f"cannot convert '{feature_name}' from proto to NumPy")
  array = np.array(value_array, dtype=dtype).reshape(shape)
  if not shape:
    if array.size != 1:
      raise ValueError(f"scalar feature '{feature_name}' should have length 1")
    return array.item()
  return array


def _build_feature_specs(flat_example_specs):
  """Returns the `tf.train.Example` feature specification.

  Args:
    flat_example_specs: flattened example specs.

  Returns:
    The `dict` of `tf.io.FixedLenFeature`, `tf.io.VarLenFeature`, ...
  """

  # Convert individual fields into tf.train.Example compatible format
  def build_single_spec(k, v):
    with utils.try_reraise(f"Specification error for feature {k!r} ({v}): "):
      return _to_tf_example_spec(v)

  return {k: build_single_spec(k, v) for k, v in flat_example_specs.items()}


def _deserialize_single_field(
    example_data, tensor_info: feature_lib.TensorInfo
):
  """Reconstruct the serialized field."""
  # Ragged tensor case:
  if tensor_info.sequence_rank > 1:
    example_data = _dict_to_ragged(example_data, tensor_info)

  # Restore shape if possible. TF Example flattened it.
  elif tensor_info.shape.count(None) < 2:
    shape = [-1 if i is None else i for i in tensor_info.shape]
    example_data = tf.reshape(example_data, shape)

  # Restore dtype
  if example_data.dtype != tensor_info.tf_dtype:
    example_data = tf.dtypes.cast(example_data, tensor_info.tf_dtype)
  return example_data


def _dict_to_ragged(example_data, tensor_info):
  """Reconstruct the ragged tensor from the row ids."""
  return tf.RaggedTensor.from_nested_row_lengths(
      flat_values=example_data["ragged_flat_values"],
      nested_row_lengths=[
          example_data["ragged_row_lengths_{}".format(k)]
          for k in range(tensor_info.sequence_rank - 1)
      ],
  )


def _to_tf_example_spec(tensor_info: feature_lib.TensorInfo):
  """Convert a `TensorInfo` into a feature proto object."""
  # Convert the dtype

  # TODO(b/119937875): TF Examples proto only support int64, float32 and string
  # This create limitation like float64 downsampled to float32, bool converted
  # to int64 which is space ineficient, no support for complexes or quantized
  # It seems quite space inefficient to convert bool to int64
  if dtype_utils.is_integer(tensor_info.tf_dtype) or dtype_utils.is_bool(
      tensor_info.tf_dtype
  ):
    dtype = tf.int64
  elif dtype_utils.is_floating(tensor_info.tf_dtype):
    dtype = tf.float32
  elif dtype_utils.is_string(tensor_info.tf_dtype):
    dtype = tf.string
  else:
    # TFRecord only support 3 types
    raise NotImplementedError(
        "Serialization not implemented for dtype {}".format(tensor_info)
    )

  # Convert the shape

  # Select the feature proto type in function of the unknown shape
  if all(s is not None for s in tensor_info.shape):
    return tf.io.FixedLenFeature(  # All shaped defined
        shape=tensor_info.shape,
        dtype=dtype,
        default_value=tensor_info.default_value,
    )
  elif tensor_info.shape.count(None) == 1:
    # Extract the defined shape (without the None dimension)
    # The original shape is restored in `_deserialize_single_field`
    shape = tuple(dim for dim in tensor_info.shape if dim is not None)
    return tf.io.FixedLenSequenceFeature(  # First shape undefined
        shape=shape,
        dtype=dtype,
        allow_missing=True,
        default_value=tensor_info.default_value,
    )
  elif tensor_info.sequence_rank > 1:  # RaggedTensor
    # Decoding here should match encoding from `_add_ragged_fields` in
    # `example_serializer.py`
    tf_specs = {  # pylint: disable=g-complex-comprehension
        "ragged_row_lengths_{}".format(k): tf.io.FixedLenSequenceFeature(  # pylint: disable=g-complex-comprehension
            shape=(),
            dtype=tf.int64,
            allow_missing=True,
        )
        for k in range(tensor_info.sequence_rank - 1)
    }
    tf_specs["ragged_flat_values"] = tf.io.FixedLenSequenceFeature(
        shape=tensor_info.shape[tensor_info.sequence_rank :],
        dtype=dtype,
        allow_missing=True,
        default_value=tensor_info.default_value,
    )
    return tf_specs
  else:
    raise NotImplementedError(
        "Multiple unknown dimension not supported.\n"
        "If using `tfds.features.Tensor`, please set "
        "`Tensor(..., encoding='zlib')` (or 'bytes', or 'gzip')"
    )
