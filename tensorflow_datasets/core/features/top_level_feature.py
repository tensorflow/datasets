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

"""Wrapper around FeatureDict to allow better control over decoding.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core.features import feature as feature_lib


class TopLevelFeature(feature_lib.FeatureConnector):
  """Top-level `FeatureConnector` to manage decoding.

  Note that `FeatureConnector` which are declared as `TopLevelFeature` can be
  nested. However, only the top-level feature can be decoded.

  `TopLevelFeature` allows better control over the decoding, and
  eventually better support for augmentations.
  """

  def __init__(self, *args, **kwargs):
    """Constructor."""
    self.__is_top_level = False
    super(TopLevelFeature, self).__init__(*args, **kwargs)

  def _set_top_level(self):
    """Indicates that the feature is top level.

    Internal function called by `DatasetInfo`.
    """
    self.__is_top_level = True

  def decode_example(self, serialized_example):
    """Decode the serialize examples.

    Args:
      serialized_example: Nested `dict` of `tf.Tensor`

    Returns:
      example: Nested `dict` containing the decoded nested examples.
    """
    if not self.__is_top_level:
      raise AssertionError(
          'Feature {} can only be decoded when defined as top-level '
          'feature, through info.features.decode_example()'.format(
              type(self).__name__))

    # Step 1: Flatten the nested dict => []
    flat_example = self._flatten(serialized_example)
    flat_features = self._flatten(self)
    flat_serialized_info = self._flatten(self.get_serialized_info())
    flat_tensor_info = self._flatten(self.get_tensor_info())

    # Step 2: Apply the decoding
    flatten_decoded = []
    for feature, example, tensor_info, serialized_info in zip(
        flat_features, flat_example, flat_tensor_info, flat_serialized_info):
      flatten_decoded.append(_decode_feature(
          feature=feature,
          example=example,
          tensor_info=tensor_info,
          serialized_info=serialized_info,
      ))

    # Step 3: Restore nesting [] => {}
    nested_decoded = self._nest(flatten_decoded)
    return nested_decoded


def _decode_feature(feature, example, tensor_info, serialized_info):
  """Decode a single feature."""
  sequence_rank = _get_sequence_rank(serialized_info)
  if sequence_rank == 0:
    return feature.decode_example(example)
  elif sequence_rank == 1:
    # Note: This all works fine in Eager mode (without tf.function) because
    # tf.data pipelines are always executed in Graph mode.

    # Apply the decoding to each of the individual distributed features.
    return tf.map_fn(
        feature.decode_example,
        example,
        dtype=tensor_info.dtype,
        parallel_iterations=10,
        back_prop=False,
        name='sequence_decode',
    )
  else:
    raise NotImplementedError(
        'Nested sequences not supported yet. Got: {}'.format(serialized_info)
    )


def _get_sequence_rank(serialized_info):
  """Return the number of sequence dimensions of the feature."""
  if isinstance(serialized_info, dict):
    all_sequence_rank = [s.sequence_rank for s in serialized_info.values()]
  else:
    all_sequence_rank = [serialized_info.sequence_rank]

  sequence_ranks = set(all_sequence_rank)
  if len(sequence_ranks) != 1:
    raise NotImplementedError(
        'Decoding do not support mixing sequence and context features within a '
        'single FeatureConnector. Received inputs of different sequence_rank: '
        '{}'.format(sequence_ranks)
    )
  return next(iter(sequence_ranks))
