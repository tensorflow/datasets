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

"""Visualization tools and utils.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib


def show_examples(ds_info, ds, rows=3, cols=3, plot_scale=3., image_key=None):
  """Visualize images (and labels) from an image classification dataset.

  Only works with datasets that have 1 image feature and optionally 1 label
  feature (both inferred from `ds_info`). Note the dataset should be unbatched.
  Requires matplotlib to be installed.

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
    rows: `int`, number of rows of the display grid.
    cols: `int`, number of columns of the display grid.
    plot_scale: `float`, controls the plot size of the images. Keep this
      value around 3 to get a good plot. High and low values may cause
      the labels to get overlapped.
    image_key: `string`, name of the feature that contains the image. If not
       set, the system will try to auto-detect it.

  Returns:
    fig: The `matplotlib.Figure` object
  """
  plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

  if not image_key:
    # Infer the image and label keys
    image_keys = [
        k for k, feature in ds_info.features.items()
        if isinstance(feature, features_lib.Image)
    ]

    if not image_keys:
      raise ValueError(
          "Visualisation not supported for dataset `{}`. Was not able to "
          "auto-infer image.".format(ds_info.name))

    if len(image_keys) > 1:
      raise ValueError(
          "Multiple image features detected in the dataset. Using the first one. You can "
          "use `image_key` argument to override. Images detected: %s" %
          (",".join(image_keys)))

    image_key = image_keys[0]

  label_keys = [
      k for k, feature in ds_info.features.items()
      if isinstance(feature, features_lib.ClassLabel)
  ]

  label_key = label_keys[0] if len(label_keys) == 1 else None
  if not label_key:
    logging.info("Was not able to auto-infer label.")

  num_examples = rows * cols
  examples = list(dataset_utils.as_numpy(ds.take(num_examples)))

  fig = plt.figure(figsize=(plot_scale*cols, plot_scale*rows))
  fig.subplots_adjust(hspace=1/plot_scale, wspace=1/plot_scale)
  for i, ex in enumerate(examples):
    if not isinstance(ex, dict):
      raise ValueError(
          "tfds.show_examples requires examples as `dict`, with the same "
          "structure as `ds_info.features`. It is currently not compatible "
          "with `as_supervised=True`. Received: {}".format(type(ex)))
    ax = fig.add_subplot(rows, cols, i+1)

    # Plot the image
    image = ex[image_key]
    if len(image.shape) != 3:
      raise ValueError(
          "Image dimension should be 3. tfds.show_examples does not support "
          "batched examples or video.")
    _, _, c = image.shape
    if c == 1:
      image = image.reshape(image.shape[:2])
    ax.imshow(image, cmap="gray")
    ax.grid(False)
    plt.xticks([], [])
    plt.yticks([], [])

    # Plot the label
    if label_key:
      label = ex[label_key]
      label_str = ds_info.features[label_key].int2str(label)
      plt.xlabel("{} ({})".format(label_str, label))
  plt.show()
  return fig
