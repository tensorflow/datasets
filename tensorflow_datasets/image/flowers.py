# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Flowers dataset.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """\
@ONLINE {tfflowers,
author = "The TensorFlow Team",
title = "Flowers",
month = "jan",
year = "2019",
url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }
"""

_URL = "http://download.tensorflow.org/example_images/flower_photos.tgz"


class TFFlowers(tfds.core.GeneratorBasedBuilder):
  """Flowers dataset."""

  VERSION = tfds.core.Version("1.0.0")

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="A large set of images of flowers",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(
                names=["dandelion", "daisy", "tulips", "sunflowers", "roses"]),
        }),
        supervised_keys=("image", "label"),
        urls=[_URL],
        citation=_CITATION
        )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(_URL)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=20,
            gen_kwargs={
                "images_dir_path": path
            }),
    ]

  def _generate_examples(self, images_dir_path):
    """Generate flower images and labels given the image directory path.

    Args:
      images_dir_path: path to the directory where the images are stored.

    Yields:
      The image path and its corresponding label.
    """
    parent_dir = tf.io.gfile.listdir(images_dir_path)[0]
    walk_dir = os.path.join(images_dir_path, parent_dir)
    dirs = tf.io.gfile.listdir(walk_dir)

    for d in dirs:
      if tf.io.gfile.isdir(os.path.join(walk_dir, d)):
        for full_path, _, fname in tf.io.gfile.walk(os.path.join(walk_dir, d)):
          for image_file in fname:
            if image_file.endswith(".jpg"):
              image_path = os.path.join(full_path, image_file)
              yield {
                  "image": image_path,
                  "label": d.lower(),
              }
