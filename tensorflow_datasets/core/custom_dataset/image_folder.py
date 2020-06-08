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
"""Image Classification Folder datasets."""

import os
from typing import Dict, List, Tuple, Set

import tensorflow.compat.v2 as tf
from tensorflow_datasets import core

# Dict of `split_label_images['split']['Label']` = `List['images']`
SplitLabelImageDict = Dict[str, Dict[str, List[str]]]

_SUPPORTED_IMAGE_FORMAT = ('.jpg', '.jpeg', '.png')


class ImageFolder(core.DatasetBuilder):
  """Generic image classification dataset created from manual directory.

  The data directory should have the following structure:

  ```
  path/to/manual_dir/<dataset_name>/
    split_name/  # Ex: 'train'
      label1/  # Ex: 'airplane' or '0015'
        xxx.png
        xxy.png
        xxz.png
      label2/
        xxx.png
        xxy.png
        xxz.png
    split_name/  # Ex: 'test'
      ...
  ```

  To use it:

  ```
  builder = tfds.ImageFolder(root_dir='path/to/manual_dir/')
  print(builder.info)  # Splits, num examples,... are automatically calculated
  ds = builder.as_dataset(split='split_name', shuffle_files=True)
  tfds.show_examples(ds, builder.info)
  ```

  """

  VERSION = core.Version('2.0.0')

  def __init__(self, root_dir, **kwargs):
    del kwargs
    root_dir = os.path.expanduser(root_dir)
    super(ImageFolder, self).__init__(
        data_dir=root_dir, version=str(self.VERSION), config=None)

    # Reset `_data_dir` as it should not change to DATA_DIR/Version
    self._data_dir = root_dir

    # dict[split_name][label_name] = list(img_paths)
    self._split_label_images, labels = _get_split_label_images(root_dir)

    # Calculate and update DatasetInfo labels
    self.info.features['label'].names = sorted(list(labels))

    # Calculate and update DatasetInfo splits
    splits = {
        split_name: sum(len(l)
                        for l in self._split_label_images[split_name].values())
        for split_name in self._split_label_images
    }
    split_dict = core.SplitDict(self.name)
    for split_name, size in splits.items():
      split_dict.add(
          core.SplitInfo(name=split_name, shard_lengths=[size]))
    self.info.update_splits_if_different(split_dict)

  def _info(self):
    return core.DatasetInfo(
        builder=self,
        description='Generic image classification dataset.',
        features=core.features.FeaturesDict({
            'image': core.features.Image(),
            'label': core.features.ClassLabel(),
            'image/filename': core.features.Text(),
        }),
        supervised_keys=('image', 'label'),
    )

  def _download_and_prepare(self, **kwargs):
    raise NotImplementedError('No need to call download_and_prepare function.')

  def download_and_prepare(self, **kwargs):
    raise NotImplementedError('No need to call download_and_prepare function.')

  def _process_ds(self, path, label):
    image_path = tf.strings.split(path, os.path.sep)[-3:]
    img = tf.io.read_file(path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.uint8)
    return {
        'image': img,
        'label': tf.cast(label, tf.int64),
        'image/filename': tf.strings.reduce_join(image_path)
    }

  def _as_dataset(
      self,
      split,
      shuffle_files=False,
      decoders=None,
      read_config=None):
    """Generate dataset for given split"""
    del decoders
    del read_config
    if split not in self.info.splits.keys():
      raise ValueError('Split name {} not present in {}'
                       .format(split, self._split_label_images.keys()))

    img_paths = sorted(
        img for l in self._split_label_images[split].values() for img in l)

    labels = list(map(
        lambda path: self.info.features['label'].str2int(path.split(os.path.sep)[-2]),
                                                         img_paths))

    ds = tf.data.Dataset.from_tensor_slices((img_paths, labels))
    if shuffle_files:
      ds = ds.shuffle(len(img_paths))
    ds = ds.map(self._process_ds,
                num_parallel_calls=tf.data.experimental.AUTOTUNE)
    return ds


def _get_split_label_images(
    root_dir: str,
) -> Tuple[SplitLabelImageDict, Set[str]]:
  """Extract all label names and associated images"""
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


def _list_folders(root_dir: str) -> List[str]:
  return [
      f for f in tf.io.gfile.listdir(root_dir)
      if tf.io.gfile.isdir(os.path.join(root_dir, f))
  ]


def _list_imgs(root_dir: str) -> List[str]:
  return [
      os.path.join(root_dir, f)
      for f in tf.io.gfile.listdir(root_dir)
      if any(f.lower().endswith(ext) for ext in _SUPPORTED_IMAGE_FORMAT)
  ]
