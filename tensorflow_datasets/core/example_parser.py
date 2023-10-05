# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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
from collections.abc import Iterable, Mapping, Sequence
import dataclasses
import re
from typing import Any, Union

import numpy as np
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.proto import tf_example_pb2
from tensorflow_datasets.proto import tf_feature_pb2

_RAGGED_ROW_COLUMN = re.compile(
    r"(?P<feature_name>.+)/(ragged_row_lengths_\d+|ragged_flat_values)$"
)
_RAGGED_ROW_LENGTH_REGEX = re.compile(
    r"(?P<feature_name>.+)/ragged_row_lengths_(?P<length>\d+)$"
)
_RAGGED_FLAT_VALUES_REGEX = re.compile(
    r"(?P<feature_name>.+)/ragged_flat_values$"
)


def _key_to_feature_name(key: str) -> str:
  """Extracts the feature name from the key in the Example dictionary."""
  if (match := _RAGGED_ROW_COLUMN.match(key)) is not None:
    return match.group("feature_name")
  else:
    return key


def _is_ragged_tensor(key: str) -> bool:
  return _RAGGED_ROW_COLUMN.match(key) is not None


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
  ) -> Mapping[str, Union[np.ndarray, list[Any]]]:
    example = tf_example_pb2.Example.FromString(serialized_example)
    np_example = _features_to_numpy(example.features, self._flat_example_specs)
    return utils.pack_as_nest_dict(np_example, self.example_specs)


def _features_to_numpy(
    features: tf_feature_pb2.Features,
    flat_example_specs: Mapping[str, feature_lib.TensorInfo],
) -> Mapping[str, Union[np.ndarray, list[Any]]]:
  """Parses features to NumPy type.

  Args:
    features: The features of an example, encoded by TFDS.
    flat_example_specs: All tensor infos in a flat dictionary.

  Returns:
    The parsed NumPy object of type: np.ndarray or np.dtype.

  Raises:
    KeyError: if `features` and `flat_example_specs` do not correspond.
  """
  parsed_example = {}
  feature_map = features.feature
  for key in feature_map:
    ragged_row_length = _RAGGED_ROW_LENGTH_REGEX.match(key)
    ragged_flat_values = _RAGGED_FLAT_VALUES_REGEX.match(key)
    # For ragged arrays we need to reshape the np.arrays using
    # ragged_flat_values/ragged_row_lengths_*. `features` can look like:
    # {
    #     'video/image': np.array(...),
    #     'video/object/bbox': {
    #         'ragged_flat_values': np.array(...),
    #         'ragged_row_lengths_0', np.array(...),
    #     },
    # }
    if key in flat_example_specs or ragged_flat_values:
      feature_name = _key_to_feature_name(key)
      with utils.try_reraise(f"Error wile parsing feature {key}: "):
        parsed_example[feature_name] = _feature_to_numpy(
            feature_map,
            flat_example_specs[feature_name],
            key,
        )
    elif ragged_row_length:
      # Lengths are extracted later for each feature in _feature_to_numpy.
      continue
    else:
      raise KeyError(
          f"Malformed input: {key} is found in the feature, but not in"
          f" {flat_example_specs}"
      )
  return parsed_example


def _feature_to_numpy(
    features: Mapping[str, tf_feature_pb2.Feature],
    tensor_info: feature_lib.TensorInfo,
    key: str,
) -> Union[np.ndarray, list[Any]]:
  """Parses a single feature to NumPy type.

  Args:
    features: TFDS features.
    tensor_info: Tensor info for the current feature.
    key: full name of the feature to convert to NumPy.

  Returns:
    The parsed NumPy object of type: np.ndarray or np.dtype.

  Raises:
    AttributeError: if the parsed feature is malformed.
    KeyError: if feature_name is not found in example_specs.
    ValueError: if a scalar feature is represented by an array.
  """
  if key not in features:
    raise KeyError(f"Malformed input: {key} is not in {features}")
  feature = features[key]
  dtype = tensor_info.np_dtype
  shape = tensor_info.shape
  if feature.HasField("int64_list"):
    value_array = feature.int64_list.value
  elif feature.HasField("float_list"):
    value_array = feature.float_list.value
  elif feature.HasField("bytes_list"):
    value_array = feature.bytes_list.value
  else:
    raise AttributeError(f"cannot convert '{key}' from proto to NumPy")
  value_array = np.array(value_array, dtype=dtype)
  if not shape:
    return value_array.item()
  feature_name = _key_to_feature_name(key)
  row_lengths = _extract_row_lengths(features, feature_name)
  return reshape_ragged_tensor(value_array, row_lengths, shape)


def _extract_row_lengths(
    features: Mapping[str, tf_feature_pb2.Feature],
    feature_name: str,
) -> list[Sequence[int]]:
  """Extracts all existing row lengths from the `features`."""
  i = 0
  row_lengths: list[Sequence[int]] = []
  while True:
    row_length_key = f"{feature_name}/ragged_row_lengths_{i}"
    if row_length_key not in features:
      break
    row_lengths.append(features[row_length_key].int64_list.value)
    i += 1
  return row_lengths


def reshape_ragged_tensor(
    values: np.ndarray,
    row_lengths: list[Sequence[int]],
    shape: tuple[Union[int, None], ...],
) -> Union[np.ndarray, list[Any]]:
  """Reshapes a list to a heterogeneous NumPy array.

  Warning: this function makes copies of arrays. It could be optimized by not
  recreating the array at each iteration but by reshaping an existing array.

  Args:
    values: 1-dimension array with all the values to reshape.
    row_lengths: array of length of the unknown dimension.
    shape: target shape of the array containing None for unknown dimensions.

  Returns:
    An array of ragged NumPy arrays.
  """
  if not row_lengths:
    # Reshape with (None, 3, 4) -> (-1, 3, 4).
    return values.reshape([d if d is not None else -1 for d in shape])
  full_row_lengths = _full_row_lengths(values, row_lengths, shape)
  # We start by the most upright dimension, which is the innerest dimension.
  for row_length in full_row_lengths:
    array = []
    i = 0
    for length in row_length:
      value = values[i : i + length]
      array.append(value)
      i += length
    values = array
  return values


def _full_row_lengths(
    values: np.ndarray,
    row_lengths: list[Sequence[int]],
    shape: tuple[Union[int, None], ...],
) -> Iterable[Sequence[int]]:
  """Corrects `row_lengths` by adding the length of non-ambiguous rows.

  `row_lengths` only contain the lengths of the ambiguous (None) rows. If the
  last dimensions are non-ambiguous (int), we can complete them.

  Args:
    values: 1-dimension array with all the values to reshape.
    row_lengths: array of length of the unknown dimension.
    shape: target shape of the array containing None for unknown dimensions.

  Returns:
    The corrected row lengths in reversed order (left is the most outer
      dimension).
  """
  if shape and shape[-1] is None:
    return reversed(row_lengths)
  full_row_lengths: list[Sequence[int]] = []
  current_row_length = len(row_lengths) - 1
  for dim_length in reversed(shape):
    if dim_length is None:
      if current_row_length < 0:
        return full_row_lengths
      full_row_lengths.append(row_lengths[current_row_length])
      current_row_length -= 1
    else:
      full_row_lengths.append([dim_length] * (len(values) // dim_length))
  return full_row_lengths


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
