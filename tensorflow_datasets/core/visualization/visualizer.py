# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Base visualizer class.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc

import six

from tensorflow_datasets.core import features as features_lib


def extract_keys(feature_dict, feature_cls):
  """Extracts keys from features dict based on feature type.

  Args:
    feature_dict: `tfds.features.FeaturesDict` from which extract keys
    feature_cls: `tfds.features.FeatureConnector` class to search.

  Returns:
    List of extracted keys matching the class.
  """
  return [k for k, f in feature_dict.items() if isinstance(f, feature_cls)]

def extract_nested_keys(features, feature_list):
  """Extracts nested feature keys in features dict.
  Args:
    features: `tfds.features.FeaturesDict` from which extract keys
    feature_list: List of `tfds.features.FeatureConnector` class to search.
  Returns:
    List of extracted keys containing a new key for each nested
    `tfds.features.FeatureDict`, including the top-level one.
  """
  out = []
  temp_fdt = features

  for i in range(len(feature_list)):
    if i > (len(feature_list) - 2):
      break
    f_slice = feature_list[i:(i+2)]
    top_level_keys = extract_keys(temp_fdt, f_slice[0])

    mid_level_keys = []
    for key in top_level_keys:
      if isinstance(temp_fdt[key].feature, features_lib.FeaturesDict):
        mid_level_keys = extract_keys(temp_fdt[key], f_slice[1])
        if len(mid_level_keys) > 0:
          if i == 0:
            out.append(key)
          out.append(mid_level_keys[0])
          new_key = key
          break
    if len(mid_level_keys) == 0:
      return False
    temp_fdt = temp_fdt[new_key]
  return out


@six.add_metaclass(abc.ABCMeta)
class Visualizer(object):
  """Visualizer."""

  @abc.abstractmethod
  def match(self, ds_info):
    """Returns whether the visualizer is compatible with the dataset.

    Args:
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.

    Returns:
      bool: True if the visualizer can be applied to the dataset.
    """

  @abc.abstractmethod
  def show(self, ds_info, ds, **options_kwargs):
    """Display the dataset.

    Args:
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
      ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
        should not be batched. Examples will be consumed in order until
        (rows * cols) are read or the dataset is consumed.
      **options_kwargs: Additional display options, specific to the dataset type
        to visualize. See the `tfds.visualization` for a list of available
        visualizers.
    """
