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

"""To deserialize bytes (Example) to tf.Example."""

import numpy as np

import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import utils


class ExampleParser(object):
  """To parse Examples."""

  def __init__(self, example_specs):
    self._example_specs = example_specs
    self._flat_example_specs = utils.flatten_nest_dict(self._example_specs)

  def _build_feature_specs(self):
    """Returns the `tf.train.Example` feature specification.

    Returns:
      The `dict` of `tf.io.FixedLenFeature`, `tf.io.VarLenFeature`, ...
    """

    # Convert individual fields into tf.train.Example compatible format
    def build_single_spec(k, v):
      with utils.try_reraise(f"Specification error for feature {k!r} ({v}): "):
        return _to_tf_example_spec(v)

    return {
        k: build_single_spec(k, v) for k, v in self._flat_example_specs.items()
    }

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
    nested_feature_specs = self._build_feature_specs()

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
    flat_feature_specs = utils.flatten_nest_dict(nested_feature_specs)

    unsupported_dtype_features = {}
    # since TF proto does not support dtypes other than `tf.int64` for integers
    # fetch the features that are not `tf.int64` and temporarily replace them
    # with dtype=tf.int64, after parsing the serialized example, restore changes
    # and cast the feature value and spec back to the original dtype.

    # QnA: Should we also try doing this for bool and floats?
    for feature, spec in flat_feature_specs.items():
      if (np.issubdtype(spec.dtype.as_numpy_dtype, np.integer) and
          spec.dtype != tf.int64):
        unsupported_dtype_features[feature] = spec
        spec_type = type(spec)
        if isinstance(spec, tf.io.FixedLenFeature):
          supported_spec = spec_type(spec.shape, dtype=tf.int64,
                                     default_value=spec.default_value)
        else:
          supported_spec = spec_type(spec.shape, dtype=tf.int64,
                                     default_value=spec.default_value,
                                     allow_missing=spec.allow_missing)
        flat_feature_specs.pop(feature)
        flat_feature_specs[feature] = supported_spec

    example = tf.io.parse_single_example(
        serialized=serialized_example,
        features=flat_feature_specs,
    )

    # cast back the feature to original dtype and also restore the feature_spec.
    if len(unsupported_dtype_features) > 0:
      for feature, spec in unsupported_dtype_features.items():
        flat_feature_specs.pop(feature)
        flat_feature_specs[feature] = spec
        tf.cast(example[feature], spec.dtype)
    example = utils.pack_as_nest_dict(example, nested_feature_specs)

    example = {  # pylint:disable=g-complex-comprehension
        k: _deserialize_single_field(example_data, tensor_info)
        for k, (
            example_data,
            tensor_info) in utils.zip_dict(example, self._flat_example_specs)
    }
    # Reconstruct all nesting
    example = utils.pack_as_nest_dict(example, self._example_specs)
    return example


def _deserialize_single_field(example_data, tensor_info):
  """Reconstruct the serialized field."""
  # Ragged tensor case:
  if tensor_info.sequence_rank > 1:
    example_data = _dict_to_ragged(example_data, tensor_info)

  # Restore shape if possible. TF Example flattened it.
  elif tensor_info.shape.count(None) < 2:
    shape = [-1 if i is None else i for i in tensor_info.shape]
    example_data = tf.reshape(example_data, shape)

  # Restore dtype
  if example_data.dtype != tensor_info.dtype:
    example_data = tf.dtypes.cast(example_data, tensor_info.dtype)
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


def _to_tf_example_spec(tensor_info):
  """Convert a `TensorInfo` into a feature proto object."""
  # Convert the dtype

  # TODO(b/119937875): TF Examples proto only support int64, float32 and string
  # This create limitation like float64 downsampled to float32, bool converted
  # to int64 which is space ineficient, no support for complexes or quantized
  # It seems quite space inefficient to convert bool to int64
  if tensor_info.dtype.is_integer or tensor_info.dtype.is_bool:
    if tensor_info.dtype.is_bool:
      dtype = tf.int64
    else:
      dtype = tensor_info.dtype
  elif tensor_info.dtype.is_floating:
    dtype = tf.float32
  elif tensor_info.dtype == tf.string:
    dtype = tf.string
  else:
    # TFRecord only support 3 types
    raise NotImplementedError(
        "Serialization not implemented for dtype {}".format(tensor_info))

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
            dtype=dtype,
            allow_missing=True,
        ) for k in range(tensor_info.sequence_rank - 1)
    }
    tf_specs["ragged_flat_values"] = tf.io.FixedLenSequenceFeature(
        shape=tensor_info.shape[tensor_info.sequence_rank:],
        dtype=dtype,
        allow_missing=True,
        default_value=tensor_info.default_value,
    )
    return tf_specs
  else:
    raise NotImplementedError(
        "Multiple unknown dimension not supported.\n"
        "If using `tfds.features.Tensor`, please set "
        "`Tensor(..., encoding='zlib')` (or 'bytes', or 'gzip')")
