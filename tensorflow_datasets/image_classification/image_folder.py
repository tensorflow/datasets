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
DATA_DIR = os.path.join('~', 'tensorflow_datasets')
AUTOTUNE = tf.data.experimental.AUTOTUNE


class ImageLabelFolder():

  def __init__(self, dataset_name, data_dir=None):
    self._name = dataset_name
    self._data_dir = data_dir or os.path.expanduser(
      os.path.join(DATA_DIR, dataset_name))

    # dict[split_name][label_name] = list(img_paths)
    self._split_label_images = self._get_split_label_images()

  def _get_split_label_images(self):
    split_names = list_folders(self.data_dir)
    split_label_images = {}
    for split_name in split_names:
      split_dir = os.path.join(self.data_dir, split_name)
      split_label_images[split_name] = {
          label_name: list_imgs(os.path.join(split_dir, label_name))	
          for label_name in list_folders(split_dir)	
      }
    return split_label_images

  @property
  def data_dir(self):
    return self._data_dir

  @property
  def name(self):
    return self._name

  def as_dataset(self, split=None):
    if split:
      return self._as_dataset(split)
    return {
          split_name: self._as_dataset(split_name)
          for split_name in list_folders(self.data_dir)
      }

  def _as_dataset(self, split_name):
    if split_name not in self._split_label_images.keys():
      raise ValueError("Split name {} not present in {}".format(split_name, self._split_label_images.keys()))

    imgs = [img for l in self._split_label_images[split_name].values() for img in l]
    list_ds = tf.data.Dataset.list_files(imgs)
    labeled_ds = list_ds.map(process_path, num_parallel_calls=AUTOTUNE)
    return labeled_ds

def decode_img(img):
  img = tf.image.decode_jpeg(img, channels=3)
  return tf.image.convert_image_dtype(img, tf.float32)

def process_path(file_path):
  label = tf.strings.split(file_path, os.path.sep)[-2]
  img = tf.io.read_file(file_path)
  img = decode_img(img)
  return img, label

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
