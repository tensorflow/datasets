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

"""To serialize Dict or sequence to Example."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import six
import tensorflow as tf

from tensorflow_datasets.core import utils


class ExampleSerializer(object):
  """To serialize examples."""

  def __init__(self, example_specs):
    """Constructor.

    Args:
      example_specs: Nested `dict` of `tfds.features.TensorInfo`, corresponding
        to the structure of data to write/read.
    """
    self._example_specs = example_specs
    self._flat_example_specs = utils.flatten_nest_dict(self._example_specs)

  def serialize_example(self, example):
    """Serialize the given example.

    Args:
      example: Nested `dict` containing the input to serialize. The input
        structure and values dtype/shape must match the `example_specs`
        provided at construction.

    Returns:
      serialize_proto: `str`, the serialized `tf.train.Example` proto
    """
    example = utils.flatten_nest_dict(example)
    example = _dict_to_tf_example(example, self._flat_example_specs)
    return example.SerializeToString()


def _dict_to_tf_example(example_dict, tensor_info_dict=None):
  """Builds tf.train.Example from (string -> int/float/str list) dictionary.

  Args:
    example_dict: `dict`, dict of values, tensor,...
    tensor_info_dict: `dict` of `tfds.feature.TensorInfo` If given, perform
      additional checks on the example dict (check dtype, shape, number of
      fields...)
  """
  def serialize_single_field(k, example_data, tensor_info):
    with utils.try_reraise(
        "Error while serializing feature {} ({}): ".format(k, tensor_info)):
      return _item_to_tf_feature(example_data, tensor_info)

  if tensor_info_dict:
    example_dict = {
        k: serialize_single_field(k, example_data, tensor_info)
        for k, (example_data, tensor_info)
        in utils.zip_dict(example_dict, tensor_info_dict)
    }
  else:
    example_dict = {
        k: serialize_single_field(k, example_data, None)
        for k, example_data in example_dict.items()
    }

  return tf.train.Example(features=tf.train.Features(feature=example_dict))


def _is_string(item):
  """Check if the object contains string or bytes."""
  if isinstance(item, (six.binary_type, six.string_types)):
    return True
  elif (isinstance(item, (tuple, list)) and
        all(isinstance(x, (six.binary_type, six.string_types)) for x in item)):
    return True
  elif (isinstance(item, np.ndarray) and  # binary or unicode
        (item.dtype.kind in ("U", "S") or item.dtype == object)):
    return True
  return False


def _item_to_tf_feature(item, tensor_info=None):
  """Single item to a tf.train.Feature."""
  v = item
  if not tensor_info and isinstance(v, (list, tuple)) and not v:
    raise ValueError(
        "Received an empty list value, so is unable to infer the "
        "feature type to record. To support empty value, the corresponding "
        "FeatureConnector should return a numpy array with the correct dtype "
        "instead of a Python list."
    )

  # Handle strings/bytes first
  is_string = _is_string(v)

  if tensor_info:
    np_dtype = np.dtype(tensor_info.dtype.as_numpy_dtype)
  elif is_string:
    np_dtype = object  # Avoid truncating trailing '\x00' when converting to np
  else:
    np_dtype = None

  v = np.array(v, dtype=np_dtype)

  # Check that the shape is expected
  if tensor_info:
    utils.assert_shape_match(v.shape, tensor_info.shape)
    if tensor_info.dtype == tf.string and not is_string:
      raise ValueError(
          "Unsuported value: {}\nCould not convert to bytes list.".format(item))

  # Convert boolean to integer (tf.train.Example does not support bool)
  if v.dtype == np.bool_:
    v = v.astype(int)

  v = v.flatten()  # Convert v into a 1-d array
  if np.issubdtype(v.dtype, np.integer):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=v))
  elif np.issubdtype(v.dtype, np.floating):
    return tf.train.Feature(float_list=tf.train.FloatList(value=v))
  elif is_string:
    v = [tf.compat.as_bytes(x) for x in v]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=v))
  else:
    raise ValueError(
        "Unsuported value: {}.\n"
        "tf.train.Feature does not support type {}. "
        "This may indicate that one of the FeatureConnectors received an "
        "unsupported value as input.".format(repr(v), repr(type(v)))
    )
