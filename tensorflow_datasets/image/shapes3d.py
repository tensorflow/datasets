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
"""Shapes3D dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from six import moves
import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{3dshapes18,
  title={3D Shapes Dataset},
  author={Burgess, Chris and Kim, Hyunjik},
  howpublished={https://github.com/deepmind/3dshapes-dataset/},
  year={2018}
}
"""

_URL = ("https://storage.googleapis.com/3d-shapes/3dshapes.h5")

_DESCRIPTION = """\
3dshapes is a dataset of 3D shapes procedurally generated from 6 ground truth
independent latent factors. These factors are *floor colour*, *wall colour*, *object colour*,
*scale*, *shape* and *orientation*.

All possible combinations of these latents are present exactly once, generating N = 480000 total images.

### Latent factor values

*   floor hue: 10 values linearly spaced in [0, 1]
*   wall hue: 10 values linearly spaced in [0, 1]
*   object hue: 10 values linearly spaced in [0, 1]
*   scale: 8 values linearly spaced in [0, 1]
*   shape: 4 values in [0, 1, 2, 3]
*   orientation: 15 values linearly spaced in [-30, 30]

We varied one latent at a time (starting from orientation, then shape, etc), and sequentially stored the images in fixed order in the `images` array. The corresponding values of the factors are stored in the same order in the `labels` array.
"""


class Shapes3d(tfds.core.GeneratorBasedBuilder):
  """Shapes3d data set."""

  VERSION = tfds.core.Version(
      "2.0.0", "New split API (https://tensorflow.org/datasets/splits)")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            "image":
                tfds.features.Image(shape=(64, 64, 3)),
            "label_floor_hue":
                tfds.features.ClassLabel(num_classes=10),
            "label_wall_hue":
                tfds.features.ClassLabel(num_classes=10),
            "label_object_hue":
                tfds.features.ClassLabel(num_classes=10),
            "label_scale":
                tfds.features.ClassLabel(num_classes=8),
            "label_shape":
                tfds.features.ClassLabel(num_classes=4),
            "label_orientation":
                tfds.features.ClassLabel(num_classes=15),
            "value_floor_hue":
                tfds.features.Tensor(shape=[], dtype=tf.float32),
            "value_wall_hue":
                tfds.features.Tensor(shape=[], dtype=tf.float32),
            "value_object_hue":
                tfds.features.Tensor(shape=[], dtype=tf.float32),
            "value_scale":
                tfds.features.Tensor(shape=[], dtype=tf.float32),
            "value_shape":
                tfds.features.Tensor(shape=[], dtype=tf.float32),
            "value_orientation":
                tfds.features.Tensor(shape=[], dtype=tf.float32),
        }),
        homepage="https://github.com/deepmind/3d-shapes",
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    filepath = dl_manager.download(_URL)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(filepath=filepath)),
    ]

  def _generate_examples(self, filepath):
    """Generate examples for the Shapes3d dataset.

    Args:
      filepath: path to the Shapes3d hdf5 file.

    Yields:
      Dictionaries with images and the different labels.
    """
    # Simultaneously iterating through the different data sets in the hdf5
    # file will be slow with a single file. Instead, we first load everything
    # into memory before yielding the samples.
    with tfds.core.lazy_imports.h5py.File(filepath, "r") as h5dataset:
      image_array = np.array(h5dataset["images"])
      # The 'label' data set in the hdf5 file actually contains the float values
      # and not the class labels.
      values_array = np.array(h5dataset["labels"])

    # We need to calculate the class labels from the float values in the file.
    labels_array = np.zeros_like(values_array, dtype=np.int64)
    for i in range(values_array.shape[1]):
      labels_array[:, i] = _discretize(values_array[:, i])  # pylint: disable=unsupported-assignment-operation

    for i, (image, labels, values) in enumerate(moves.zip(
        image_array, labels_array, values_array)):
      record = {
          "image": image,
          "label_floor_hue": labels[0],
          "label_wall_hue": labels[1],
          "label_object_hue": labels[2],
          "label_scale": labels[3],
          "label_shape": labels[4],
          "label_orientation": labels[5],
          "value_floor_hue": values[0],
          "value_wall_hue": values[1],
          "value_object_hue": values[2],
          "value_scale": values[3],
          "value_shape": values[4],
          "value_orientation": values[5],
      }
      yield i, record


def _discretize(a):
  """Discretizes array values to class labels."""
  arr = np.asarray(a)
  index = np.argsort(arr)
  inverse_index = np.zeros(arr.size, dtype=np.intp)
  inverse_index[index] = np.arange(arr.size, dtype=np.intp)
  arr = arr[index]
  obs = np.r_[True, arr[1:] != arr[:-1]]
  return obs.cumsum()[inverse_index] - 1
