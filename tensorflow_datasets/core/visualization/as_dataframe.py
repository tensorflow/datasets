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

from typing import Any

import tensorflow.compat.v2 as tf
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core.visualization import dataframe_visualizer


def as_dataframe(
    ds: tf.data.Dataset,
    ds_info: dataset_info.DatasetInfo,
    **options_kwargs: Any
):
  """Visualize the dataset as a pandas dataframe.

  This function is for interactive use (Colab, Jupyter). It displays and return
  a dataframe from a tf.data.Dataset.

  Usage:
  ```python
  ds, ds_info = tfds.load('cifar10', split='train', with_info=True)
  df = tfds.as_dataframe(ds, ds_info)
  ```

  Args:
    ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
      should not be batched. Examples will be consumed in order until
      num_examples are read or the dataset is consumed.
    ds_info: The dataset info object to which extract the label and features
      info. Available either through `tfds.load('mnist', with_info=True)` or
      `tfds.builder('mnist').info`
    **options_kwargs: Additional display options, specific to the dataset type
      to visualize. Are forwarded to `tfds.visualization.Visualizer.show`.
      See the `tfds.visualization` for a list of available visualizers.

  Returns:
    dataframe: The `pandas.DataFrame` object
  """
  visualizer = dataframe_visualizer.DataframeVisualizer()
  return visualizer.show(ds, ds_info, **options_kwargs)
