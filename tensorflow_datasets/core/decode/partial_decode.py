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

"""Partial feature connector decoding util."""

import typing
from typing import Dict, Optional

from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.decode import base
from tensorflow_datasets.core.features import features_dict

# Expected feature specs provided by the user
_FeatureSpecs = utils.TreeDict[features_lib.FeatureConnector]
_FeaturesDict = Dict[str, features_lib.FeatureConnector]


class PartialDecoding:
  """Allow to decode a subset of features.

  See guide:
  https://www.tensorflow.org/datasets/decode#only_decode_a_sub-set_of_the_features

  """

  def __init__(
      self,
      features: _FeatureSpecs,
      decoders: Optional[utils.TreeDict[base.Decoder]] = None,
  ):
    """Constructor.

    Args:
      features: A nested dict of `tfds.features.FeatureConnector`
      decoders: Optional additional decoders to apply (e.g.
        `tfds.decode.SkipDecoding()`)
    """
    self.decoders = decoders
    self._feature_specs = features  # Expected feature specs

  def extract_features(
      self,
      features: features_lib.FeatureConnector,
  ) -> features_lib.FeatureConnector:
    """Returns the `tfds.features.FeaturesDict`.

    Extract the subset of features

    Args:
      features: Features on which extract the sub-set

    Returns:
      features_subset: A subset of the features
    """
    with utils.try_reraise(
        'Provided PartialDecoding specs does not match actual features: '):
      return _extract_features(
          feature=features,
          expected_feature=features_dict.to_feature(self._feature_specs),
      )


def _extract_features(
    feature: features_lib.FeatureConnector,
    expected_feature: features_lib.FeatureConnector,
) -> features_lib.FeatureConnector:
  """Recursive implementation of `PartialDecoding.extract_features`."""
  # Feature types should match
  if not isinstance(feature, type(expected_feature)):
    raise TypeError(f'Expected: {expected_feature}. Got: {feature}')

  # Recurse into FeaturesDict, Sequence
  # Use `type` rather than `isinstance` to not recurse into inherited classes.
  if type(feature) == features_lib.FeaturesDict:  # pylint: disable=unidiomatic-typecheck
    expected_feature = typing.cast(features_lib.FeaturesDict, expected_feature)
    return features_lib.FeaturesDict({  # Extract the feature subset
        k: _extract_feature_item(
            feature=feature, expected_key=k, expected_value=v)
        for k, v in expected_feature.items()
    })
  elif type(feature) == features_lib.Sequence:  # pylint: disable=unidiomatic-typecheck
    feature = typing.cast(features_lib.Sequence, feature)
    expected_feature = typing.cast(features_lib.Sequence, expected_feature)
    feature_subset = _extract_features(
        feature=feature.feature,
        expected_feature=expected_feature.feature,
    )
    return features_lib.Sequence(feature_subset, length=feature._length)  # pylint: disable=protected-access
  else:
    # Assert that the specs matches
    if (feature.dtype != expected_feature.dtype or
        not utils.shapes_are_compatible(feature.shape, expected_feature.shape)):
      raise ValueError(f'Expected: {expected_feature}. Got: {feature}')
    return feature


def _extract_feature_item(
    feature: features_lib.FeaturesDict,
    expected_key: str,
    expected_value: features_lib.FeatureConnector,
) -> features_lib.FeatureConnector:
  """Calls `_extract_features(feature[key], expected_feature=value)`."""
  assert isinstance(feature, features_lib.FeaturesDict)
  if expected_key not in feature:
    raise ValueError(f'Missing expected feature {expected_key!r}.')

  with utils.try_reraise(f'In {expected_key!r}: '):
    return _extract_features(
        feature=feature[expected_key], expected_feature=expected_value)
