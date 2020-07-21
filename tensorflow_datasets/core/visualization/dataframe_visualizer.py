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
"""Dataframe visualizer."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.visualization import visualizer


class DataframeVisualizer(visualizer.Visualizer):
  """Visualizer for text and structured datasets."""

  def match(self, ds_info: dataset_info.DatasetInfo) -> bool:
    """See base class."""
    ds_type = visualizer.extract_dataset_type(ds_info.full_name)
    return ds_type in ['text', 'structured']

  def show(
      self,
      ds: tf.data.Dataset,
      ds_info: dataset_info.DatasetInfo,
      num_examples: int = 20,
  ):
    """Display the dataset.

    Args:
      ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
        should not be batched. Examples will be consumed in order until
        rows are read or the dataset is consumed.
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
      num_examples: `int`, number of rows in the pandas dataframe.

    Returns:
      df: The pandas dataframe.
    """
    # Extract the keys
    features = visualizer.extract_all_keys(ds_info.features)

    # Create the dataframe
    dataframe = lazy_imports_lib.lazy_imports.pandas.DataFrame(columns=features)

    # Populate the dataframe
    examples = list(dataset_utils.as_numpy(ds.take(num_examples)))
    for i, ex in enumerate(examples):
      if not isinstance(ex, dict):
        raise ValueError(
            '{} requires examples as `dict`, with the same '
            'structure as `ds_info.features`. It is currently not compatible '
            'with `as_supervised=True`. Received: {}'.format(
                type(self).__name__, type(ex)))
      dataframe.loc[i] = [ex[feature] for feature in features]

    return dataframe
