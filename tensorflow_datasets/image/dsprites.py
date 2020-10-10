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

"""dSprites dataset."""

import numpy as np
from six import moves
import tensorflow.compat.v2 as tf

import tensorflow_datasets.public_api as tfds

_CITATION = """\
@misc{dsprites17,
author = {Loic Matthey and Irina Higgins and Demis Hassabis and Alexander Lerchner},
title = {dSprites: Disentanglement testing Sprites dataset},
howpublished= {https://github.com/deepmind/dsprites-dataset/},
year = "2017",
}
"""

_URL = ("https://github.com/deepmind/dsprites-dataset/blob/master/"
        "dsprites_ndarray_co1sh3sc6or40x32y32_64x64.hdf5?raw=true")

_DESCRIPTION = """\
dSprites is a dataset of 2D shapes procedurally generated from 6 ground truth
independent latent factors. These factors are *color*, *shape*, *scale*,
*rotation*, *x* and *y* positions of a sprite.

All possible combinations of these latents are present exactly once,
generating N = 737280 total images.

### Latent factor values

*   Color: white
*   Shape: square, ellipse, heart
*   Scale: 6 values linearly spaced in [0.5, 1]
*   Orientation: 40 values in [0, 2 pi]
*   Position X: 32 values in [0, 1]
*   Position Y: 32 values in [0, 1]

We varied one latent at a time (starting from Position Y, then Position X, etc),
and sequentially stored the images in fixed order.
Hence the order along the first dimension is fixed and allows you to map back to
the value of the latents corresponding to that image.

We chose the latents values deliberately to have the smallest step changes
while ensuring that all pixel outputs were different. No noise was added.
"""


class Dsprites(tfds.core.GeneratorBasedBuilder):
  """dSprites data set."""

  VERSION = tfds.core.Version("2.0.0")
  SUPPORTED_VERSIONS = [
      tfds.core.Version("2.1.0"),
  ]
  RELEASE_NOTES = {
      "2.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    features_dict = {
        "image": tfds.features.Image(shape=(64, 64, 1)),
        "label_shape": tfds.features.ClassLabel(num_classes=3),
        "label_scale": tfds.features.ClassLabel(num_classes=6),
        "label_orientation": tfds.features.ClassLabel(num_classes=40),
        "label_x_position": tfds.features.ClassLabel(num_classes=32),
        "label_y_position": tfds.features.ClassLabel(num_classes=32),
        "value_shape": tfds.features.Tensor(shape=[], dtype=tf.float32),
        "value_scale": tfds.features.Tensor(shape=[], dtype=tf.float32),
        "value_orientation": tfds.features.Tensor(shape=[], dtype=tf.float32),
        "value_x_position": tfds.features.Tensor(shape=[], dtype=tf.float32),
        "value_y_position": tfds.features.Tensor(shape=[], dtype=tf.float32),
    }
    if self.version > "2.0.0":
      features_dict["id"] = tfds.features.Text()
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features_dict),
        homepage="https://github.com/deepmind/dsprites-dataset",
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
    """Generates examples for the dSprites data set.

    Args:
      filepath: path to the dSprites hdf5 file.

    Yields:
      Dictionaries with images, latent classes, and latent values.
    """
    # Simultaneously iterating through the different data sets in the hdf5
    # file is >100x slower and the data set is small (26.7MB). Hence, we first
    # load everything into memory before yielding the samples.
    with tfds.core.lazy_imports.h5py.File(filepath, "r") as h5dataset:
      image_array = np.array(h5dataset["imgs"])
      class_array = np.array(h5dataset["latents"]["classes"])
      values_array = np.array(h5dataset["latents"]["values"])

    for i, (image, classes, values) in enumerate(moves.zip(
        image_array, class_array, values_array)):
      record = dict(
          image=np.expand_dims(image, -1),
          label_shape=classes[1],
          label_scale=classes[2],
          label_orientation=classes[3],
          label_x_position=classes[4],
          label_y_position=classes[5],
          value_shape=values[1],
          value_scale=values[2],
          value_orientation=values[3],
          value_x_position=values[4],
          value_y_position=values[5])
      if self.version > "2.0.0":
        record["id"] = "{:06d}".format(i)
      yield i, record
