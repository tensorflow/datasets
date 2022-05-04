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

"""Wrapper around FeatureDict to allow better control over decoding."""

from __future__ import annotations

from typing import Any, Union

import tensorflow as tf
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib


class TopLevelFeature(feature_lib.FeatureConnector):
  """Top-level `FeatureConnector` to manage decoding.

  Note that `FeatureConnector` which are declared as `TopLevelFeature` can be
  nested. However, only the top-level feature should be decoded.

  `TopLevelFeature` allows better control over the decoding, and
  eventually better support for augmentations.
  """

  def decode_example(self, serialized_example, *, decoders=None):
    # pylint: disable=line-too-long
    """Decode the serialize examples.

    Args:
      serialized_example: Nested `dict` of `tf.Tensor`
      decoders: Nested dict of `Decoder` objects which allow to customize the
        decoding. The structure should match the feature structure, but only
        customized feature keys need to be present. See [the
          guide](https://github.com/tensorflow/datasets/tree/master/docs/decode.md)
            for more info.

    Returns:
      example: Nested `dict` containing the decoded nested examples.
    """
    # Step 1: Flatten the nested dict => []
    flat_example = self._flatten(serialized_example)
    flat_features = self._flatten(self)
    flat_serialized_info = self._flatten(self.get_serialized_info())
    flat_decoders = self._flatten(decoders)

    # Step 2: Apply the decoding
    flatten_decoded = [
        _decode_feature(  # pylint: disable=g-complex-comprehension
            feature=feature,
            example=example,
            serialized_info=serialized_info,
            decoder=decoder,
        ) for (
            feature,
            example,
            serialized_info,
            decoder,
        ) in zip(flat_features, flat_example, flat_serialized_info,
                 flat_decoders)
    ]

    # Step 3: Restore nesting [] => {}
    nested_decoded = self._nest(flatten_decoded)
    return nested_decoded

  def serialize_example(self, example_data) -> bytes:
    """Encodes nested data values into `tf.train.Example` bytes.

    See `deserialize_example` to decode the proto into `tf.Tensor`.

    Args:
      example_data: Example data to encode (numpy-like nested dict)

    Returns:
      The serialized `tf.train.Example`.
    """
    example_data = self.encode_example(example_data)
    return self._example_serializer.serialize_example(example_data)

  def deserialize_example(
      self,
      serialized_example: Union[tf.Tensor, bytes],
      *,
      decoders=None,
  ) -> utils.TensorDict:
    """Decodes the `tf.train.Example` data into `tf.Tensor`.

    See `serialize_example` to encode the data into proto.

    Args:
      serialized_example: The tensor-like object containing the serialized
        `tf.train.Example` proto.
      decoders: Eventual decoders to apply (see
        [documentation](https://www.tensorflow.org/datasets/decode))

    Returns:
      The decoded features tensors.
    """
    example_data = self._example_parser.parse_example(serialized_example)
    return self.decode_example(example_data, decoders=decoders)

  @property
  def tf_example_spec(self) -> dict[str, Any]:
    """Returns the `tf.Example` proto structure.

    Returns:
      The flat `dict[str, tf.io.FixedLenFeature | tf.io.XyzFeature | ...]`
    """
    return self._example_parser.flat_feature_specs

  @utils.memoized_property
  def _example_parser(self):
    from tensorflow_datasets.core import example_parser  # pytype: disable=import-error  # pylint: disable=g-import-not-at-top
    example_specs = self.get_serialized_info()
    return example_parser.ExampleParser(example_specs)

  @utils.memoized_property
  def _example_serializer(self):
    from tensorflow_datasets.core import example_serializer  # pytype: disable=import-error  # pylint: disable=g-import-not-at-top
    example_specs = self.get_serialized_info()
    return example_serializer.ExampleSerializer(example_specs)


def _decode_feature(feature, example, serialized_info, decoder):
  """Decode a single feature."""
  if decoder is not None:
    # If the decoder is still a dict, it means that the feature is a Dataset
    # (it wasn't flattened).
    if isinstance(decoder, dict):
      decode_kwargs = dict(decoders=decoder)
      decoder = feature
    else:
      # Eventually overwrite the default decoding
      decode_kwargs = {}
      decoder.setup(feature=feature)
  else:
    decode_kwargs = {}
    decoder = feature

  sequence_rank = _get_sequence_rank(serialized_info)
  if sequence_rank == 0:
    return decoder.decode_example(example, **decode_kwargs)
  elif sequence_rank == 1:
    # Return a batch of examples from a sequence
    return decoder.decode_batch_example(example, **decode_kwargs)
  elif sequence_rank > 1:
    # Use ragged tensor if the sequance rank is greater than one
    return decoder.decode_ragged_example(example, **decode_kwargs)


def _get_sequence_rank(serialized_info):
  """Return the number of sequence dimensions of the feature."""

  if isinstance(serialized_info, dict):
    # If the element is a dictionary, it might correspond to a nested dataset
    # whose serialized_info is not flattened (so it might be a nested dict).
    all_sequence_rank = [
        _get_sequence_rank(s) for s in serialized_info.values()
    ]
  else:
    # If this is a nested dataset, we ignore the sequence_rank. We will decode
    # the full dataset example with the Dataset decoder.
    if serialized_info.dataset_lvl > 0:
      return 0
    all_sequence_rank = [serialized_info.sequence_rank]
  sequence_ranks = set(all_sequence_rank)
  if len(sequence_ranks) != 1:
    raise NotImplementedError(
        'Decoding do not support mixing sequence and context features within a '
        'single FeatureConnector. Received inputs of different sequence_rank: '
        '{}'.format(sequence_ranks))
  return next(iter(sequence_ranks))
