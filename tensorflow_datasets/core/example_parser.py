# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
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
      with utils.try_reraise(
          "Specification error for feature {} ({}): ".format(k, v)):
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
    example = tf.io.parse_single_example(
        serialized=serialized_example,
        features=self._build_feature_specs(),
    )
    example = {
        k: _deserialize_single_field(example_data, tensor_info)
        for k, (example_data, tensor_info)
        in utils.zip_dict(example, self._flat_example_specs)
    }
    # Reconstruct all nesting
    example = utils.pack_as_nest_dict(example, self._example_specs)
    return example


def _deserialize_single_field(example_data, tensor_info):
  """Reconstruct the serialized field."""

  # Restore shape if possible. TF Example flattened it.
  if tensor_info.shape.count(None) < 2:
    shape = [-1 if i is None else i for i in tensor_info.shape]
    example_data = tf.reshape(example_data, shape)

  # Restore dtype
  if example_data.dtype != tensor_info.dtype:
    example_data = tf.dtypes.cast(example_data, tensor_info.dtype)
  return example_data


def _to_tf_example_spec(tensor_info):
  """Convert a `TensorInfo` into a feature proto object."""
  # Convert the dtype

  # TODO(b/119937875): TF Examples proto only support int64, float32 and string
  # This create limitation like float64 downsampled to float32, bool converted
  # to int64 which is space ineficient, no support for complexes or quantized
  # It seems quite space inefficient to convert bool to int64
  if tensor_info.dtype.is_integer or tensor_info.dtype.is_bool:
    dtype = tf.int64
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
  elif (tensor_info.shape.count(None) == 1 and tensor_info.shape[0] is None):
    return tf.io.FixedLenSequenceFeature(  # First shape undefined
        shape=tensor_info.shape[1:],
        dtype=dtype,
        allow_missing=True,
        default_value=tensor_info.default_value,
    )
  else:
    raise NotImplementedError(
        "Tensor with a unknown dimension not at the first position not "
        "supported: {}".format(tensor_info))
