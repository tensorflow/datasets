# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Labeled faces in wild."""

import os

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# URL where the data is hosted. This is the same also used e.g. by scikit-learn:
# https://github.com/scikit-learn/scikit-learn/blob/98ed9dc73a86f5f11781a0e21f24c8f47979ec67/sklearn/datasets/_lfw.py#L36
_URL = "https://ndownloader.figshare.com/files/5976018"

LFW_IMAGE_SHAPE = (250, 250, 3)


class Builder(tfds.core.GeneratorBasedBuilder):
  """LFW Builder class."""

  VERSION = tfds.core.Version("0.1.1")

  def _info(self):
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            "label": tfds.features.Text(),
            "image": tfds.features.Image(shape=LFW_IMAGE_SHAPE),
        }),
        supervised_keys=("label", "image"),
        homepage="http://vis-www.cs.umass.edu/lfw",
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download_and_extract(_URL)
    path = os.path.join(path, "lfw")

    # There is no train/test split predefined
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                "data_path": path,
            },
        ),
    ]

  def _generate_examples(self, data_path):
    image_list = self.path_maker(data_path)
    for label, path in image_list:
      key = "%s/%s" % (label, os.path.basename(path))
      yield key, {
          "label": label,
          "image": path,
      }

  def path_maker(self, path):
    """Returns all images within path as tuples (label, path)."""
    path_list = []
    dir_list = tf.io.gfile.listdir(path)
    for directory in dir_list:
      img_dir_path = os.path.join(path, directory)
      if tf.io.gfile.isdir(img_dir_path):
        img_list = tf.io.gfile.listdir(img_dir_path)
        for img in img_list:
          img_path = os.path.join(img_dir_path, img)
          path_list.append([directory, img_path])
    return path_list
