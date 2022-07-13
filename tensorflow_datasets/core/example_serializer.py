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

"""To serialize Dict or sequence to Example."""

import abc
import collections
import dataclasses
from typing import Any, Mapping
import numpy as np
import six

import tensorflow as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib

TensorInfo = feature_lib.TensorInfo
TreeDict = utils.TreeDict
Shape = utils.Shape


@dataclasses.dataclass(frozen=True)
class Serializer(abc.ABC):
  """Interface of an example serializer."""
  example_specs: TreeDict[TensorInfo]

  @abc.abstractmethod
  def serialize_example(self, example: TreeDict[Any]) -> Any:
    """Serialize the given example.

    Args:
      example: Nested `dict` containing the input to serialize. The input
        structure and values dtype/shape must match the `example_specs` provided
        at construction.

    Returns:
      the serialized example.
    """
    raise NotImplementedError


class ExampleSerializer(Serializer):
  """To serialize examples."""

  def __init__(self, example_specs: TreeDict[TensorInfo]):
    """Constructor.

    Args:
      example_specs: Nested `dict` of `tfds.features.TensorInfo`, corresponding
        to the structure of data to write/read.
    """
    super().__init__(example_specs)
    self._flat_example_specs = utils.flatten_nest_dict(self.example_specs)

  def get_tf_example(self, example: TreeDict[Any]) -> tf.train.Example:
    """Creates a TF Example for the given example.

    Args:
      example: Nested `dict` containing the input to serialize. The input
        structure and values dtype/shape must match the `example_specs` provided
        at construction.

    Returns:
      The `tf.train.Example` proto
    """
    return _dict_to_tf_example(
        utils.flatten_nest_dict(example), self._flat_example_specs)

  def serialize_example(self, example: TreeDict[Any]) -> Any:
    """Serialize the given example.

    Args:
      example: Nested `dict` containing the input to serialize. The input
        structure and values dtype/shape must match the `example_specs` provided
        at construction.

    Returns:
      serialize_proto: `str`, the serialized `tf.train.Example` proto
    """
    return self.get_tf_example(example).SerializeToString()


def _dict_to_tf_example(
    example_dict: Mapping[str, Any],
    tensor_info_dict: Mapping[str, feature_lib.TensorInfo]) -> tf.train.Example:
  """Builds tf.train.Example from (string -> int/float/str list) dictionary.

  Args:
    example_dict: `dict`, dict of values, tensor,...
    tensor_info_dict: `dict` of `tfds.features.TensorInfo`

  Returns:
    example_proto: `tf.train.Example`, the encoded example proto.
  """

  def run_with_reraise(fn, k, example_data, tensor_info):
    try:
      return fn(example_data, tensor_info)
    except Exception as e:  # pylint: disable=broad-except
      utils.reraise(
          e,
          f"Error while serializing feature `{k}`: `{tensor_info}`: ",
      )

  # Add the RaggedTensor fields for the nested sequences
  # Nested sequences are encoded as {'flat_values':, 'row_lengths':}, so need
  # to flatten the example nested dict again.
  # Ex:
  # Input: {'objects/tokens': [[0, 1, 2], [], [3, 4]]}
  # Output: {
  #     'objects/tokens/flat_values': [0, 1, 2, 3, 4],
  #     'objects/tokens/row_lengths_0': [3, 0, 2],
  # }
  features = utils.flatten_nest_dict({
      k: run_with_reraise(_add_ragged_fields, k, example_dict[k], tensor_info)
      for k, tensor_info in tensor_info_dict.items()
  })
  features = {
      k: run_with_reraise(_item_to_tf_feature, k, item, tensor_info)
      for k, (item, tensor_info) in features.items()
  }
  return tf.train.Example(features=tf.train.Features(feature=features))


def _is_string(item):
  """Check if the object contains string or bytes."""
  if isinstance(item, (six.binary_type, six.string_types)):
    return True
  elif (isinstance(item, (tuple, list)) and all(_is_string(x) for x in item)):
    return True
  elif (isinstance(item, np.ndarray) and  # binary or unicode
        (item.dtype.kind in ("U", "S") or item.dtype == object)):
    return True
  return False


def _item_to_np_array(item, dtype: tf.dtypes.DType, numpy_dtype: np.dtype,
                      shape: Shape) -> np.ndarray:
  """Single item to a np.array."""
  result = np.asanyarray(item, dtype=numpy_dtype)
  utils.assert_shape_match(result.shape, shape)
  if utils.is_same_tf_dtype(dtype, tf.string) and not _is_string(item):
    raise ValueError(
        f"Unsupported value: {result}\nCould not convert to bytes list.")
  return result


def _item_to_tf_feature(
    item, tensor_info: feature_lib.TensorInfo) -> tf.train.Feature:
  """Single item to a tf.train.Feature."""
  v = _item_to_np_array(
      item,
      shape=tensor_info.shape,
      dtype=tensor_info.dtype,
      numpy_dtype=tensor_info.numpy_dtype,
  )

  # Convert boolean to integer (tf.train.Example does not support bool)
  if utils.is_same_np_dtype(v.dtype, np.bool_):
    v = v.astype(int)

  vals = v.flat  # Convert v into a 1-d array (without extra copy)
  if utils.is_np_sub_dtype(v.dtype, np.integer):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=vals))
  elif utils.is_np_sub_dtype(v.dtype, np.floating):
    return tf.train.Feature(float_list=tf.train.FloatList(value=vals))
  elif utils.is_same_tf_dtype(tensor_info.dtype, tf.string):
    vals = [tf.compat.as_bytes(x) for x in vals]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=vals))
  else:
    raise ValueError(
        "Unsupported value: {}.\n"
        "tf.train.Feature does not support type {}. "
        "This may indicate that one of the FeatureConnectors received an "
        "unsupported value as input.".format(repr(v), repr(type(v))))


RaggedExtraction = collections.namedtuple("RaggedExtraction", [
    "nested_list",
    "flat_values",
    "nested_row_lengths",
    "curr_ragged_rank",
    "tensor_info",
])


def _add_ragged_fields(example_data, tensor_info: feature_lib.TensorInfo):
  """Optionally convert the ragged data into flat/row_lengths fields.

  Example:

  ```
  example_data = [
      [1, 2, 3],
      [],
      [4, 5]
  ]
  tensor_info = TensorInfo(shape=(None, None,), sequence_rank=2, ...)
  out = _add_ragged_fields(example_data, tensor_info)
  out == {
      'ragged_flat_values': ([1, 2, 3, 4, 5], TensorInfo(shape=(), ...)),
      'ragged_row_length_0': ([3, 0, 2], TensorInfo(shape=(None,), ...))
  }
  ```

  If `example_data` isn't ragged, `example_data` and `tensor_info` are
  forwarded as-is.

  Args:
    example_data: Data to optionally convert to ragged data.
    tensor_info: TensorInfo associated with the given data.

  Returns:
    A tuple(example_data, tensor_info) if the tensor isn't ragged, or a dict of
      tuple(example_data, tensor_info) if the tensor is ragged.
  """
  # Step 1: Extract the ragged tensor info
  if tensor_info.sequence_rank:
    # If the input is ragged, extract the nested values.
    # 1-level sequences are converted as numpy and stacked.
    # If the sequence is empty, a np.empty(shape=(0, ...)) array is returned.
    example_data, nested_row_lengths = _extract_ragged_attributes(
        example_data, tensor_info)

  # Step 2: Format the ragged tensor data as dict
  # No sequence or 1-level sequence, forward the data.
  # Could eventually handle multi-level sequences with static lengths
  # in a smarter way.
  if tensor_info.sequence_rank < 2:
    return (example_data, tensor_info)
  # Multiple level sequence:
  else:
    tensor_info_length = feature_lib.TensorInfo(shape=(None,), dtype=tf.int64)
    ragged_attr_dict = {
        "ragged_row_lengths_{}".format(i): (length, tensor_info_length)
        for i, length in enumerate(nested_row_lengths)
    }
    tensor_info_flat = feature_lib.TensorInfo(
        shape=(None,) + tensor_info.shape[tensor_info.sequence_rank:],
        dtype=tensor_info.dtype,
    )
    ragged_attr_dict["ragged_flat_values"] = (example_data, tensor_info_flat)
    return ragged_attr_dict


def _extract_ragged_attributes(nested_list,
                               tensor_info: feature_lib.TensorInfo):
  """Extract the values for the tf.RaggedTensor __init__.

  This extracts the ragged tensor attributes which allow to reconstruct the
  ragged tensor with `tf.RaggedTensor.from_nested_row_lengths`.

  Args:
    nested_list: A nested list containing the ragged tensor values
    tensor_info: The specs of the ragged tensor

  Returns:
    flat_values: The flatten values of the ragged tensor. All values from each
      list will be converted to np.array and stacked together.
    nested_row_lengths: The row lengths for each ragged dimensions.
  """
  assert tensor_info.sequence_rank, "{} is not ragged.".format(tensor_info)

  flat_values = []
  nested_row_lengths = [[] for _ in range(tensor_info.sequence_rank)]
  # Recursively append to `flat_values`, `nested_row_lengths`
  _fill_ragged_attribute(
      RaggedExtraction(
          nested_list=nested_list,
          flat_values=flat_values,
          nested_row_lengths=nested_row_lengths,
          curr_ragged_rank=0,
          tensor_info=tensor_info,
      ))
  if not flat_values:  # The full sequence is empty
    flat_values = np.empty(
        shape=(0,) + tensor_info.shape[tensor_info.sequence_rank:],
        dtype=tensor_info.numpy_dtype,
    )
  else:  # Otherwise, merge all flat values together, some might be empty
    flat_values = np.stack(flat_values)
  return flat_values, nested_row_lengths[1:]


def _fill_ragged_attribute(ext: RaggedExtraction) -> None:
  """Recurse the nested_list from the given RaggedExtraction.

  Args:
    ext: RaggedExtraction tuple containing the input/outputs

  Returns:
    None, the function mutates instead `ext.nested_row_lengths` and
      `ext.flat_values` lists.
  """
  # Register the current sequence length.
  # Could be 0 in case of empty list or an np.empty(shape=(0, ...)).
  curr_sequence_length = len(ext.nested_list)
  ext.nested_row_lengths[ext.curr_ragged_rank].append(curr_sequence_length)
  # Sanity check if sequence is static, but should have been catched before
  # by `Sequence.encode_example`
  expected_sequence_length = ext.tensor_info.shape[ext.curr_ragged_rank]
  if (expected_sequence_length is not None and
      expected_sequence_length != curr_sequence_length):
    raise ValueError(
        "Received length {} do not match the expected one {} from {}.".format(
            curr_sequence_length, expected_sequence_length, ext.tensor_info))

  if ext.curr_ragged_rank < ext.tensor_info.sequence_rank - 1:
    # If there are additional Sequence dimension, recurse 1 level deeper.
    for sub_list in ext.nested_list:
      _fill_ragged_attribute(
          ext._replace(
              nested_list=sub_list,
              curr_ragged_rank=ext.curr_ragged_rank + 1,
          ))
  else:
    # Otherwise, we reached the max level deep, so add the current items
    for item in ext.nested_list:
      item = _item_to_np_array(  # Normalize the item
          item,
          dtype=ext.tensor_info.dtype,
          numpy_dtype=ext.tensor_info.numpy_dtype,
          # We only check the non-ragged shape
          shape=ext.tensor_info.shape[ext.tensor_info.sequence_rank:],
      )
      ext.flat_values.append(item)
