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
"""Video visualizer."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.visualization import visualizer

def _make_grid(plot_single_ex_fn, ds, rows, cols, plot_scale):

  plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

  num_examples = rows * cols
  examples = list(dataset_utils.as_numpy(ds.take(num_examples)))

  fig = plt.figure(figsize=(plot_scale * cols, plot_scale * rows))
  fig.subplots_adjust(hspace=1 / plot_scale, wspace=1 / plot_scale)

  for i, ex in enumerate(examples):
    ax = fig.add_subplot(rows, cols, i+1)
    plot_single_ex_fn(ax, ex)

  plt.show()
  return fig

def _add_video(ax, video):
  """Add the Video to the given `matplotlib.axes.Axes`."""
  plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

  if len(video.shape) != 4:
    raise ValueError(
        'Video dimension should be 4.')
  f,_, _, c = video.shape
  print(video.shape)
  if c == 1:
    video = video.reshape(video.shape[:3])
  for i in range(f):
    ax.imshow(video[i], cmap='gray')
    ax.grid(False)
    plt.xticks([], [])
    plt.yticks([], [])

class VideoGridVisualizer(visualizer.Visualizer):
  """Visualizer for video datasets."""

  def match(self, ds_info):
    """See base class."""
    # Supervised required a single image key
    video_keys = visualizer.extract_keys(ds_info.features, features_lib.Video)
    return len(video_keys) > 0


  def show(
      self,
      ds_info,
      ds,
      rows=3,
      cols=3,
      plot_scale=3.,
      video_key=None,
  ):
    """Display the dataset.

    Args:
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
      ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
        should not be batched. Examples will be consumed in order until
        (rows * cols) are read or the dataset is consumed.
      rows: `int`, number of rows of the display grid.
      cols: `int`, number of columns of the display grid.
      plot_scale: `float`, controls the plot size of the images. Keep this
        value around 3 to get a good plot. High and low values may cause
        the labels to get overlapped.
      video_key: `string`, name of the feature that contains the video. If not
         set, the system will try to auto-detect it.
    """
    # Extract the video key automatically.
    if not video_key:
      video_keys = visualizer.extract_keys(ds_info.features, features_lib.Video)
      video_key = video_keys[0]

    # Optionally extract the label key
    label_keys = visualizer.extract_keys(
        ds_info.features, features_lib.ClassLabel)
    label_key = label_keys[0] if len(label_keys) == 1 else None
    if not label_key:
      logging.info('Was not able to auto-infer label.')

    def make_cell_fn(ax, ex):
      plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

      if not isinstance(ex, dict):
        raise ValueError(
            '{} requires examples as `dict`, with the same '
            'structure as `ds_info.features`. It is currently not compatible '
            'with `as_supervised=True`. Received: {}'.format(
                type(self).__name__, type(ex)))

      _add_video(ax, ex[video_key])
      if label_key:
        label = ex[label_key]
        label_str = ds_info.features[label_key].int2str(label)
        plt.xlabel('{} ({})'.format(label_str, label))

    # Print the grid
    fig = _make_grid(make_cell_fn, ds, rows, cols, plot_scale)  

