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

"""Visualizer for object detection datasets.
"""

from absl import logging

from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import lazy_imports_lib

def _draw_text(ax, xy, txt, size=14):
  """Draws text on the top-left corner of the bounding box"""
  ax.text(*xy, txt, verticalalignment='top', \
          color='white', fontsize=size, weight="normal", \
          bbox=dict(facecolor='black', alpha=0.7, pad=0.3))

def _draw_rectangle(ax, bbox):
  """Draws the bounding box"""
  patches = lazy_imports_lib.lazy_imports.matplotlib.patches
  ax.add_patch(patches.Rectangle(bbox[:2], \
              *bbox[-2:], fill=False, \
              edgecolor='red', lw=0.7))

def _bb_hw(bbox, height, width):
  """converts bounding box to height and width"""
  return [bbox[1]*width, bbox[0]*height, \
          (bbox[3]*width)-(bbox[1]*width)+1, \
          (bbox[2]*height)-(bbox[0]*height)+1]


def match(ds_info):
  """Checks if dataset belongs to object detection category"""
  image_keys = [
      k for k, feature in ds_info.features.items()
      if isinstance(feature, features_lib.Image)
  ]

  if not image_keys:
    return False

  sequence_keys = [
      k for k, feature in ds_info.features.items()
      if isinstance(feature, features_lib.Sequence)
  ]

  bbox_keys = []
  for key in sequence_keys:
    if isinstance(ds_info.features[key].feature, features_lib.FeaturesDict):
      bbox_keys = [
          k for k, feature in ds_info.features[key].items()
          if isinstance(feature, features_lib.BBoxFeature)
      ]

  if bbox_keys:
    return True

  return False

def build(ds_info, ds, **kwargs):
  """Builds the plot for visualization"""
  rows = kwargs.setdefault('rows', 3)
  cols = kwargs.setdefault('cols', 3)
  plot_scale = kwargs.setdefault('plot_scale', 3)
  image_key = kwargs.setdefault('image_key', None)
  args = ['rows', 'cols', 'plot_scale', 'image_key']

  for key in kwargs:
    if key not in args:
      raise TypeError(
          "show_example() got an unexpected keyword argument '{}'".format(key)
          )

  plt = lazy_imports_lib.lazy_imports.matplotlib.pyplot

  if not image_key:
    # Infer the image and label keys
    image_keys = [
        k for k, feature in ds_info.features.items()
        if isinstance(feature, features_lib.Image)
    ]

    if len(image_keys) > 1:
      raise ValueError(
          "Multiple image features detected in the dataset. Using the first one. You can "
          "use `image_key` argument to override. Images detected: %s" %
          (",".join(image_keys)))

    image_key = image_keys[0]

  # Infer the sequence keys since BBox are wrapped inside them
  sequence_keys = [
      k for k, feature in ds_info.features.items()
      if isinstance(feature, features_lib.Sequence)
  ]

  # Infer the BBox keys in the sequence feature connectors
  bbox_keys = []
  for key in sequence_keys:
    if isinstance(ds_info.features[key].feature, features_lib.FeaturesDict):
      bbox_keys = [
          k for k, feature in ds_info.features[key].items()
          if isinstance(feature, features_lib.BBoxFeature)
      ]
      if len(bbox_keys) > 0:
        sequence_key = key
        break

  # Infer the label keys in the sequence feature connector (BBox Labels)
  label_keys = [
      k for k, feature in ds_info.features[sequence_key].items()
      if isinstance(feature, features_lib.ClassLabel)
  ]

  # Taking first label key since some datasets have multiple label keys
  # for BBoxes as in voc dataset
  label_key = label_keys[0] if len(label_keys) > 0 else None
  if not label_key:
    logging.info("Was not able to auto-infer label.")
  bbox_key = bbox_keys[0] if len(bbox_keys) > 0 else None

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

    bboxes = ex[sequence_key][bbox_key]
    height = image.shape[0]
    width = image.shape[1]
    font_size = int((11./3.) * plot_scale)

    # Plot the label and bounding boxes
    for idx, box in enumerate(bboxes):
      bbox = _bb_hw(box, height, width)
      _draw_rectangle(ax, bbox)
      if label_key:
        text = ds_info.features[sequence_key][label_key].int2str(ex[sequence_key][label_key][idx])
        _draw_text(ax, bbox[:2], text, size=font_size)

  plt.show()
  return fig
