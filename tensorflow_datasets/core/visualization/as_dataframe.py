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
"""As dataframe util.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core.visualization import visualizer


def _filter_features(ds_info: tf.data.Dataset,
                     all_features: list,
                     filter_features: list
                     ) -> list:
  """Filter the feature types that are not supported.

  Args:
    ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
    all_features: List of all feature keys in the dataset.
    filter_features: List of feature types to remove from the dataframe.

  Returns:
    List of all feature keys that are supported by the dataframe.
  """
  for feature_type in filter_features:
    if feature_type == features_lib.Tensor:
      keys = [k for k, f in ds_info.features.items() if type(f) == feature_type
              and len(ds_info.features[k].shape) != 0]
    else:
      keys = [k for k, f in ds_info.features.items() if type(f) == feature_type]
    for key in keys:
      all_features.remove(key)
  return all_features


def as_dataframe(
    ds: tf.data.Dataset,
    ds_info: dataset_info.DatasetInfo,
    num_examples: int = 20
):
  """Visualize the dataset as a pandas dataframe.

  This function is for interactive use (Colab, Jupyter). It displays and return
  a dataframe from a tf.data.Dataset.

  Usage:
  ```python
  ds, ds_info = tfds.load('cifar10', split='train', with_info=True)
  dataframe = tfds.as_dataframe(ds, ds_info)
  ```

  Args:
    ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
      should not be batched. Examples will be consumed in order until
      num_examples are read or the dataset is consumed.
    ds_info: The dataset info object to which extract the label and features
      info. Available either through `tfds.load('mnist', with_info=True)` or
      `tfds.builder('mnist').info`
    num_examples: `int`, number of rows in the pandas dataframe.

  Returns:
    dataframe: The `pandas.DataFrame` object
  """
  # Extract the features
  features = visualizer.extract_all_keys(ds_info.features)

  # Filter feature types that are not supported
  unsupported_features = [
      features_lib.Audio, features_lib.Image,
      features_lib.Sequence, features_lib.Tensor,
      features_lib.Video
  ]
  features = _filter_features(ds_info, features, unsupported_features)

  # Create the dataframe
  dataframe = lazy_imports_lib.lazy_imports.pandas.DataFrame(columns=features)

  # Populate the dataframe
  examples = list(dataset_utils.as_numpy(ds.take(num_examples)))
  for i, ex in enumerate(examples):
    if not isinstance(ex, dict):
      raise ValueError(
          'as_dataframe() requires examples as `dict`, with the same '
          'structure as `ds_info.features`. It is currently not compatible '
          'with `as_supervised=True`. Received: {}'.format(type(ex)))
    dataframe.loc[i] = [ex[feature] for feature in features]

  return dataframe
