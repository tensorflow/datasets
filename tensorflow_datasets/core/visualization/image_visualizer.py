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

"""Image visualizer."""

from typing import Optional

from absl import logging
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.visualization import visualizer


def _make_grid(plot_single_ex_fn, ds, rows, cols, plot_scale):
  """Plot each individual example in a grid.

  Args:
    plot_single_ex_fn: Function with fill a single cell of the grid, with
      signature `fn(ax: matplotlib.axes.Axes, ex: Nested[np.array]) -> None`
    ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
      should not be batched. Examples will be consumed in order until (rows *
      cols) are read or the dataset is consumed.
    rows: `int`, number of rows of the display grid.
    cols: `int`, number of columns of the display grid.
    plot_scale: `float`, controls the plot size of the images. Keep this value
      around 3 to get a good plot. High and low values may cause the labels to
      get overlapped.

  Returns:
    fig: The `matplotlib.Figure` object.
  """
  plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

  num_examples = rows * cols
  examples = list(dataset_utils.as_numpy(ds.take(num_examples)))

  fig = plt.figure(figsize=(plot_scale * cols, plot_scale * rows))
  fig.subplots_adjust(hspace=1 / plot_scale, wspace=1 / plot_scale)

  for i, ex in enumerate(examples):
    ax = fig.add_subplot(rows, cols, i + 1)
    plot_single_ex_fn(ax, ex)

  plt.show()
  return fig


def _add_image(ax, image):
  """Add the image to the given `matplotlib.axes.Axes`."""
  plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

  if len(image.shape) != 3:
    raise ValueError(
        'Image dimension should be 3. tfds.show_examples does not support '
        'batched examples or video.')
  _, _, c = image.shape
  if c == 1:
    image = image.reshape(image.shape[:2])
  ax.imshow(image, cmap='gray')
  ax.grid(False)
  plt.xticks([], [])
  plt.yticks([], [])


class ImageGridVisualizer(visualizer.Visualizer):
  """Visualizer for supervised image datasets."""

  def match(self, ds_info: dataset_info.DatasetInfo) -> bool:
    """See base class."""
    # Supervised required a single image key
    image_keys = visualizer.extract_keys(ds_info.features, features_lib.Image)
    return len(image_keys) >= 1

  def show(
      self,
      ds: tf.data.Dataset,
      ds_info: dataset_info.DatasetInfo,
      rows: int = 3,
      cols: int = 3,
      plot_scale: float = 3.,
      image_key: Optional[str] = None,
  ):
    """Display the dataset.

    Args:
      ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
        should not be batched. Examples will be consumed in order until (rows *
        cols) are read or the dataset is consumed.
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
      rows: `int`, number of rows of the display grid.
      cols: `int`, number of columns of the display grid.
      plot_scale: `float`, controls the plot size of the images. Keep this value
        around 3 to get a good plot. High and low values may cause the labels to
        get overlapped.
      image_key: `string`, name of the feature that contains the image. If not
        set, the system will try to auto-detect it.

    Returns:
      fig: The pyplot figure.
    """
    # Extract the image key
    if not image_key:
      image_keys = visualizer.extract_keys(ds_info.features, features_lib.Image)
      if len(image_keys) > 1:
        raise ValueError(
            'Multiple image features detected in the dataset. '
            'Use `image_key` argument to override. Images detected: {}'.format(
                image_keys))
      image_key = image_keys[0]

    # Optionally extract the label key
    label_keys = visualizer.extract_keys(ds_info.features,
                                         features_lib.ClassLabel)
    label_key = label_keys[0] if len(label_keys) == 1 else None
    if not label_key:
      logging.info('Was not able to auto-infer label.')

    # Single image display
    def make_cell_fn(ax, ex):
      plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

      if not isinstance(ex, dict):
        raise ValueError(
            '{} requires examples as `dict`, with the same '
            'structure as `ds_info.features`. It is currently not compatible '
            'with `as_supervised=True`. Received: {}'.format(
                type(self).__name__, type(ex)))

      _add_image(ax, ex[image_key])
      if label_key:
        label = ex[label_key]
        label_str = ds_info.features[label_key].int2str(label)
        plt.xlabel('{} ({})'.format(label_str, label))

    # Returns the grid.
    fig = _make_grid(make_cell_fn, ds, rows, cols, plot_scale)
    return fig
