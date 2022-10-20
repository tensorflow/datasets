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

"""Base visualizer class."""

from __future__ import annotations

import abc
from typing import Any

import six
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


def extract_keys(feature_dict, feature_cls):
  """Extracts keys from features dict based on feature type.

  Args:
    feature_dict: `tfds.features.FeaturesDict` from which extract keys
    feature_cls: `tfds.features.FeatureConnector` class to search.

  Returns:
    List of extracted keys matching the class.
  """
  return [k for k, f in feature_dict.items() if isinstance(f, feature_cls)]


@six.add_metaclass(abc.ABCMeta)
class Visualizer(object):
  """Visualizer."""

  @abc.abstractmethod
  def match(self, ds_info: dataset_info.DatasetInfo) -> bool:
    """Returns whether the visualizer is compatible with the dataset.

    Args:
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.

    Returns:
      bool: True if the visualizer can be applied to the dataset.
    """

  @abc.abstractmethod
  def show(self, ds: tf.data.Dataset, ds_info: dataset_info.DatasetInfo,
           **options_kwargs: Any):
    """Display the dataset.

    Args:
      ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
        should not be batched. Examples will be consumed in order until (rows *
        cols) are read or the dataset is consumed.
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
      **options_kwargs: Additional display options, specific to the dataset type
        to visualize. See the `tfds.visualization` for a list of available
        visualizers.
    """
