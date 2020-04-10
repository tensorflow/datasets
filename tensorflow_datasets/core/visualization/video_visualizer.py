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
from IPython.display import display,Image

import tensorflow as tf
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.visualization import visualizer


def _display_gif(gif_fn, ds, num_examples, width, height):
  """Display Video as GIF.

  Args:
    plot_single_ex_fn: Function with fill a single cell of the grid, with
      signature `fn(ax: matplotlib.axes.Axes, ex: Nested[np.array]) -> None`
    ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
      should not be batched. Examples will be consumed in order until
      (rows * cols) are read or the dataset is consumed.
    num_examples: Number of examples to display from video dataset.
  """
  examples = list(dataset_utils.as_numpy(ds.take(num_examples)))
  for i, ex in enumerate(examples):
    gif_fn(ex)
    with open('sample.gif','rb') as f:
      display(Image(data=f.read(),format="png",width=width,height=height))

  tf.io.gfile.remove("sample.gif")


def _write_video_gif(video, fps):
  """Process the Video and write it as GIF."""
  ImageSequenceClip = lazy_imports_lib.lazy_imports.moviepy.editor.ImageSequenceClip

  if len(video.shape) != 4:
    raise ValueError(
        'Video dimension should be 4.')
  _,_, _, c = video.shape
  # Write GIF using imageio & moviepy
  clip = ImageSequenceClip(list(video), fps=fps)
  clip.write_gif("sample.gif", fps=fps, verbose=False, progress_bar=False)


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
      num_examples=5,
      video_key=None,
      width=150,
      height=150,
      fps=10,
  ):
    """Display the dataset.

    Args:
      ds_info: `tfds.core.DatasetInfo` object of the dataset to visualize.
      ds: `tf.data.Dataset`. The tf.data.Dataset object to visualize. Examples
        should not be batched. Examples will be consumed in order until
        (rows * cols) are read or the dataset is consumed.
      num_examples: Number of examples to display from video dataset. Default is 5
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

    def make_cell_fn(ex):
      if not isinstance(ex, dict):
        raise ValueError(
            '{} requires examples as `dict`, with the same '
            'structure as `ds_info.features`. It is currently not compatible '
            'with `as_supervised=True`. Received: {}'.format(
                type(self).__name__, type(ex)))

      _write_video_gif(ex[video_key], fps)
      if label_key:
        label = ex[label_key]
        label_str = ds_info.features[label_key].int2str(label)
        #plt.xlabel('{} ({})'.format(label_str, label))

    # Display GIF
    _display_gif(make_cell_fn, ds, num_examples, width, height)  
