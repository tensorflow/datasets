# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Cartoon Datasets"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import tensorflow as tf

import tensorflow_datasets as tfds
from tensorflow_datasets.core import api_utils


_CARTOON_IMAGE_SIZE = 500
_CARTOON_IMAGE_SHAPE = (_CARTOON_IMAGE_SIZE, _CARTOON_IMAGE_SIZE, 3)

_DESCRIPTION = """
Cartoon Set is a collection of random, 2D cartoon avatar images. Each image is a
500 x 500 PNG. The cartoons vary in 10 artwork categories, 4 color categories, 
and  4 proportion categories, with a total of ~10^13 possible combinations. Set 
of 10k and 100k randomly chosen cartoons and labeled attributes are provided. 
"""
_CITATION = """
@ONLINE {CartoonSet,
  author = "Forrester Cole, Inbar Mosseri, Dilip Krishnan, Aaron Sarna, Aaron Maschinot, Bill Freeman, Shiraz Fuman",
  title = "Cartoon Set : An Image Dataset of Random Cartoons",
  url  = "https://google.github.io/cartoonset/"
}
"""

_DATA_OPTIONS = ['cartoonset10k', 'cartoonset100k']


class CartoonsetConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CartoonSet."""

  @api_utils.disallow_positional_args
  def __init__(self, data, **kwargs):
    """Constructs a CartoonsetConfig.
    Args:
      data: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if data not in _DATA_OPTIONS:
      raise ValueError("data must be one of %s" % _DATA_OPTIONS)

    super(CartoonsetConfig, self).__init__(**kwargs)
    self.data = data


class Cartoonset(tfds.core.GeneratorBasedBuilder):
  """CartoonSet is a collection of random, 2D cartoon avatar images."""

  VERSION = tfds.core.Version('0.1.0')

  BUILDER_CONFIGS = [
      CartoonsetConfig(
          name='cartoonset10k',
          description="A collection of random, 10000 2D cartoon avatar images",
          version="0.1.0",
          data='cartoonset10k',
      ),
      CartoonsetConfig(
          name='cartoonset100k',
          description="A collection of random, 100000 2D cartoon avatar images",
          version="0.1.0",
          data='cartoonset100k',
      )
  ]
  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(
            {"image": tfds.features.Image(shape=_CARTOON_IMAGE_SHAPE),
             "eye_angle": tfds.features.ClassLabel(num_classes=3),
             "eye_lashes": tfds.features.ClassLabel(num_classes=2),
             "eye_lid": tfds.features.ClassLabel(num_classes=2),
             "chin_length": tfds.features.ClassLabel(num_classes=3),
             "eyebrow_weight": tfds.features.ClassLabel(num_classes=2),
             "eyebrow_shape": tfds.features.ClassLabel(num_classes=14),
             "eyebrow_thickness": tfds.features.ClassLabel(num_classes=4),
             "face_shape": tfds.features.ClassLabel(num_classes=7),
             "facial_hair": tfds.features.ClassLabel(num_classes=15),
             "hair": tfds.features.ClassLabel(num_classes=111),
             "eye_color": tfds.features.ClassLabel(num_classes=5),
             "face_color": tfds.features.ClassLabel(num_classes=11),
             "hair_color": tfds.features.ClassLabel(num_classes=10),
             "glasses": tfds.features.ClassLabel(num_classes=12),
             "glasses_color": tfds.features.ClassLabel(num_classes=7),
             "eye_slant": tfds.features.ClassLabel(num_classes=3),
             "eyebrow_width": tfds.features.ClassLabel(num_classes=3),
             "eye_eyebrow_distance": tfds.features.ClassLabel(num_classes=3)}),
        supervised_keys=None,
        # Homepage of the dataset for documentation
        urls=["https://google.github.io/cartoonset/"],
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    # There is no predefined train/val/test split for this dataset.
    path = dl_manager.manual_dir
    if not tf.io.gfile.exists(path):
      msg = 'You must download the dataset files manually and place them in: '
      msg += ', '.join([path])
      raise AssertionError(msg)
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=2,
            gen_kwargs={
                "filepath": path
            })
    ]

  def _generate_examples(self, filepath):
    """Yields examples."""
    for path, _, files in tf.io.gfile.walk(
        os.path.join(filepath, self.builder_config.name)):
      for file in files:
        features_dict = dict()
        name, dtype = file.split('.')
        if dtype == 'png':
          image = tfds.core.lazy_imports.skimage.io.imread(
              path + '/' + name + '.png')

          with tf.io.gfile.GFile(path + '/' + name + '.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
              features_dict[row[0]] = row[1]
          features_dict['image'] = image[:, :, :3]  # Currently TensoFlow does not support alpha channels
          yield features_dict
