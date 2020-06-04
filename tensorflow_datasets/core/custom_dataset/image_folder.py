# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the 'License");
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
"""Image FileFolder datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import os

from absl import logging
import tensorflow.compat.v2 as tf
from tensorflow_datasets import core

_SUPPORTED_IMAGE_FORMAT = ('.jpg', '.jpeg', '.png')
_AUTOTUNE = tf.data.experimental.AUTOTUNE


class ImageLabelFolder(core.DatasetBuilder):

  VERSION = core.Version('2.0.0')

  def __init__(self, root_dir):    
    self._version = str(self.VERSION)
    self._root_dir = os.path.expanduser(root_dir)

    # dict[split_name][label_name] = list(img_paths)
    self._split_label_images, labels = _get_split_label_images(self._root_dir)

    self._ds_info = core.DatasetInfo(
        builder=self,
        description='Generic image classification dataset.',
        features=core.features.FeaturesDict({
            'image': core.features.Image(),
            'label': core.features.ClassLabel(names=list(labels)),
        }),
        supervised_keys=('image', 'label'),
    )

    super(ImageLabelFolder, self).__init__(
        data_dir=self._root_dir, version=self._version, config=None)
    
    # Calculate splits for DatasetInfo
    splits = {
        split_name: sum(len(l)
                        for l in self._split_label_images[split_name].values())
        for split_name in self._split_label_images
    }

    split_dict = core.SplitDict(self.name)
    for split_name, size in splits.items():
      split_dict.add(
          core.SplitInfo(name=split_name, shard_lengths=[size]))

    self._ds_info.update_splits_if_different(split_dict)

    # Reset `_data_dir` as it should not change to DATA_DIR/Version
    self._data_dir = self._root_dir

  def _info(self):
    return self._ds_info

  def _download_and_prepare(self, **kwargs):
    pass

  def download_and_prepare(self, **kwargs):
    pass

  def _process_ds(self, image_paths):
    for path in image_paths:
      path = path.decode()
      label = path.split(os.path.sep)[-2]
      img = tf.io.read_file(path)
      img = _decode_img(img)
      yield {'image': img, 'label': self.info.features['label'].str2int(label)}

  def _as_dataset(self, split, shuffle_files=False, **kwargs):
    if split not in self.info.splits.keys():
      raise ValueError('Split name {} not present in {}'.format(split, self._split_label_images.keys()))

    imgs = [img for l in self._split_label_images[split].values() for img in l]
    ds = tf.data.Dataset.from_generator(
      self._process_ds,
      output_shapes=self.info.features.shape,
      output_types=self.info.features.dtype,
      args=[imgs])
    
    if shuffle_files:
      ds = ds.shuffle(len(imgs))
    return ds


def _get_split_label_images(root_dir):
  split_names = _list_folders(root_dir)
  split_label_images = dict()
  labels = set()
  for split_name in split_names:
    split_dir = os.path.join(root_dir, split_name)
    split_label_images[split_name] = {
        label_name: _list_imgs(os.path.join(split_dir, label_name))
        for label_name in _list_folders(split_dir)
    }
    labels.update(split_label_images[split_name].keys())
  return split_label_images, labels


def _decode_img(img):
  img = tf.image.decode_jpeg(img, channels=3)
  return tf.image.convert_image_dtype(img, tf.uint8)


def _list_folders(root_dir):
  return sorted(
      f for f in tf.io.gfile.listdir(root_dir)
      if tf.io.gfile.isdir(os.path.join(root_dir, f))
  )


def _list_imgs(root_dir):
  return sorted(
      os.path.join(root_dir, f)
      for f in tf.io.gfile.listdir(root_dir)
      if any(f.lower().endswith(ext) for ext in _SUPPORTED_IMAGE_FORMAT)
  )
