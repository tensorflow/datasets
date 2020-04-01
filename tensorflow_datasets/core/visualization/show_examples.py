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
"""Show example util.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.core.visualization import image_visualizer

_ALL_VISUALIZERS = [
    image_visualizer.ImageGridVisualizer(),
]


def show_examples(ds_info, ds, **options_kwargs):
  """Visualize images (and labels) from an image classification dataset.

  This function is for interactive use (Colab, Jupyter). It displays and return
  a plot of (rows*columns) images from a tf.data.Dataset.

  Usage:
  ```python
  ds, ds_info = tfds.load('cifar10', split='train', with_info=True)
  fig = tfds.show_examples(ds_info, ds)
  ```

  Args:
    ds_info: The dataset info object to which extract the label and features
      info. Available either through `tfds.load('mnist', with_info=True)` or
      `tfds.builder('mnist').info`
    ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
      should not be batched. Examples will be consumed in order until
      (rows * cols) are read or the dataset is consumed.
    **options_kwargs: Additional display options, specific to the dataset type
      to visualize. Are forwarded to `tfds.visualization.Visualizer.show`.
      See the `tfds.visualization` for a list of available visualizers.

  Returns:
    fig: The `matplotlib.Figure` object
  """
  for visualizer in _ALL_VISUALIZERS:
    if visualizer.match(ds_info):
      visualizer.show(ds_info, ds, **options_kwargs)
      break
  else:
    raise ValueError(
        "Visualisation not supported for dataset `{}`".format(ds_info.name)
    )
