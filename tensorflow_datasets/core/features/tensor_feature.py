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

import numpy as np
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib

Json = utils.Json
Shape = utils.Shape


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
  ):
    """Construct a Tensor feature.

    Args:
      shape: Tensor shape
      dtype: Tensor dtype
    """
    self._shape = tuple(shape)
    self._dtype = dtype

  def get_tensor_info(self):
    """See base class for details."""
    return feature_lib.TensorInfo(shape=self._shape, dtype=self._dtype)

  def decode_batch_example(self, example_data):
    """See base class for details."""
    # Overwrite the `tf.map_fn`, decoding is a no-op
    return self.decode_example(example_data)

  def decode_ragged_example(self, example_data):
    """See base class for details."""
    # Overwrite the `tf.map_fn`, decoding is a no-op
    return self.decode_example(example_data)

  def encode_example(self, example_data):
    """See base class for details."""
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
    utils.assert_shape_match(example_data.shape, self._shape)
    return example_data

  @classmethod
  def from_json_content(cls, value: Json) -> 'Tensor':
    return cls(
        shape=tuple(value['shape']),
        dtype=tf.dtypes.as_dtype(value['dtype']),
    )

  def to_json_content(self) -> Json:
    return {
        'shape': list(self._shape),
        'dtype': self._dtype.name,
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
