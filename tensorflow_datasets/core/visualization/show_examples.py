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
<<<<<<< HEAD:tensorflow_datasets/core/visualization/show_examples.py
"""Show example util.
=======
"""Visualization tools and utils.
>>>>>>> added documentations, incorporated changes and added test for object detection datasets:tensorflow_datasets/core/visualization.py
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

<<<<<<< HEAD:tensorflow_datasets/core/visualization/show_examples.py
<<<<<<< HEAD:tensorflow_datasets/core/visualization/show_examples.py
from tensorflow_datasets.core.visualization import image_visualizer

<<<<<<< HEAD:tensorflow_datasets/core/visualization/show_examples.py
_ALL_VISUALIZERS = [
    image_visualizer.ImageGridVisualizer(),
]
=======
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.image_visualizer import ObjectVisulaizer, SupervisedVisualizer
from tensorflow_datasets.core import object_visualizer

_ALL_VISUALIZERS = [ObjectVisulaizer(), SupervisedVisualizer()]
>>>>>>> removed functions; added classes:tensorflow_datasets/core/visualization.py
=======
#from absl import logging

#from tensorflow_datasets.core import dataset_utils
#from tensorflow_datasets.core import features as features_lib
#from tensorflow_datasets.core import lazy_imports_lib
=======
>>>>>>> removed useless comments:tensorflow_datasets/core/visualization.py
from tensorflow_datasets.core import image_visualizer

_ALL_VISUALIZERS = [
    image_visualizer.ObjectVisulaizer(),
    image_visualizer.SupervisedVisualizer()
]
>>>>>>> added documentations, incorporated changes and added test for object detection datasets:tensorflow_datasets/core/visualization.py


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
<<<<<<< HEAD:tensorflow_datasets/core/visualization/show_examples.py
    **options_kwargs: Additional display options, specific to the dataset type
      to visualize. Are forwarded to `tfds.visualization.Visualizer.show`.
      See the `tfds.visualization` for a list of available visualizers.

=======
    rows: `int`, number of rows of the display grid.
    cols: `int`, number of columns of the display grid.
    plot_scale: `float`, controls the plot size of the images. Keep this
      value around 3 to get a good plot. High and low values may cause
      the labels to get overlapped.
    image_key: `string`, name of the feature that contains the image. If not
       set, the system will try to auto-detect it.
<<<<<<< HEAD:tensorflow_datasets/core/visualization/show_examples.py
<<<<<<< HEAD:tensorflow_datasets/core/visualization/show_examples.py
    bbox_label: `bool`, flag for bounding box labels. Default is True.
>>>>>>> removed functions; added classes:tensorflow_datasets/core/visualization.py
=======
>>>>>>> minor changes:tensorflow_datasets/core/visualization.py
=======
    bbox_label: `bool`, flag for bounding box labels. Only for object detection
      datasets.
>>>>>>> added documentations, incorporated changes and added test for object detection datasets:tensorflow_datasets/core/visualization.py
  Returns:
    fig: The `matplotlib.Figure` object
  """
  for visualizer in _ALL_VISUALIZERS:
    if visualizer.match(ds_info):
<<<<<<< HEAD:tensorflow_datasets/core/visualization/show_examples.py
      visualizer.show(ds_info, ds, **options_kwargs)
      break
  else:
    raise ValueError(
        "Visualisation not supported for dataset `{}`".format(ds_info.name)
    )
=======
      return visualizer.build(ds_info, ds, **options_kwargs)
  raise ValueError(
      f"Visualisation not supported for dataset `{ds_info.name}`"
  )
>>>>>>> added documentations, incorporated changes and added test for object detection datasets:tensorflow_datasets/core/visualization.py
