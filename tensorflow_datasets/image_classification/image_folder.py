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
"""FileFolder datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import os

from absl import logging
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds


SUPPORTED_IMAGE_FORMAT = (".jpg", ".jpeg", ".png")

class ImageLabelFolder(tfds.core.DatasetBuilder):

  MANUAL_DOWNLOAD_INSTRUCTIONS = "This is a 'template' dataset."

  VERSION = tfds.core.Version(
      "2.0.0", "New split API (https://tensorflow.org/datasets/splits)")

  def __init__(self, dataset_name="image_label_folder", **kwargs):
    self.name = dataset_name
    super(ImageLabelFolder, self).__init__(**kwargs)

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description="Generic image classification dataset.",
        features=tfds.features.FeaturesDict({
            "image": tfds.features.Image(),
            "label": tfds.features.ClassLabel(num_classes=None),
        }),
        supervised_keys=("image", "label"),
    )

  def _download_and_prepare(self, dl_manager, **kwargs):
    split_names = list_folders(dl_manager.manual_dir)
    split_dict = tfds.core.SplitDict(dataset_name=self.name)
    # TODO: Update splits according to directory structure

  def _as_dataset(self, split, **kwargs):
    # TODO: Make dataset
    # ds = tf.data.Dataset.list_files() or tf.data.Dataset.from_generator()
    return ds

def list_folders(root_dir):
  return [
      f for f in tf.io.gfile.listdir(root_dir)
      if tf.io.gfile.isdir(os.path.join(root_dir, f))
  ]

def list_imgs(root_dir):
  return [
      os.path.join(root_dir, f)
      for f in tf.io.gfile.listdir(root_dir)
      if any(f.lower().endswith(ext) for ext in SUPPORTED_IMAGE_FORMAT)
  ]
