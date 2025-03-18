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

"""Pneumonia Mnist dataset."""

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for Pneumonia Mnist dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(28, 28, 1)),
            'label': tfds.features.ClassLabel(names=['Normal', 'Pneumonia']),
        }),
        supervised_keys=('image', 'label'),
        homepage='https://medmnist.com//',
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    npz_path = dl_manager.download(
        'https://zenodo.org/records/10519652/files/pneumoniamnist.npz'
    )

    with tf.io.gfile.GFile(npz_path, 'rb') as f:
      raw_data = np.load(f)

    train_images = np.expand_dims(raw_data.f.train_images, axis=-1)
    val_images = np.expand_dims(raw_data.f.val_images, axis=-1)
    test_images = np.expand_dims(raw_data.f.test_images, axis=-1)
    train_labels = raw_data.f.train_labels.flatten()
    val_labels = raw_data.f.val_labels.flatten()
    test_labels = raw_data.f.test_labels.flatten()

    return {
        'train': self._generate_examples(train_images, train_labels),
        'val': self._generate_examples(val_images, val_labels),
        'test': self._generate_examples(test_images, test_labels),
    }

  def _generate_examples(self, images, labels):
    """Yields examples."""
    for idx, (image, label) in enumerate(zip(images, labels)):
      yield idx, {
          'image': image,
          'label': int(np.squeeze(label)),
      }
