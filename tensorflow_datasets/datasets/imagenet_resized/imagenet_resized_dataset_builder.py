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

"""Resized imagenet to 8x8, 16x16, 32x32.

This is not to be confused with `downsampled_imagenet` which is a unsupervised
dataset used for generative modeling.
"""

import io
import itertools
import numpy as np
import tensorflow_datasets.public_api as tfds

_LABELS_FNAME = 'image_classification/imagenet_resized_labels.txt'
_URL_PREFIX = 'http://www.image-net.org/data/downsample/'


class ImagenetResizedConfig(tfds.core.BuilderConfig):
  """BuilderConfig for Imagenet Resized."""

  def __init__(self, size, **kwargs):
    super(ImagenetResizedConfig, self).__init__(
        version=tfds.core.Version('0.1.0'), **kwargs
    )
    self.size = size


def _make_builder_configs():
  """Returns BuilderConfigs."""
  configs = []
  for size in [8, 16, 32, 64]:
    configs.append(
        ImagenetResizedConfig(
            name='%dx%d' % (size, size),
            size=size,
            description=f'Images resized to {size}x{size}',
        ),
    )
  return configs


class Builder(tfds.core.GeneratorBasedBuilder):
  """Imagenet Resized dataset."""

  VERSION = tfds.core.Version('0.1.1')
  RELEASE_NOTES = {
      '0.1.0': 'Imagenet Resized Datset',
      '0.1.1': 'Webisite URL update',
  }
  BUILDER_CONFIGS = _make_builder_configs()

  def _info(self):
    names_file = tfds.core.tfds_path(_LABELS_FNAME)
    size = self.builder_config.size
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            'image': tfds.features.Image(shape=(size, size, 3)),
            'label': tfds.features.ClassLabel(names_file=names_file),
        }),
        supervised_keys=('image', 'label'),
        homepage='https://patrykchrabaszcz.github.io/Imagenet32/',
    )

  def _split_generators(self, dl_manager):
    size = self.builder_config.size

    if size in [8, 16, 32]:
      train_path, val_path = dl_manager.download([
          '%s/Imagenet%d_train_npz.zip' % (_URL_PREFIX, size),
          '%s/Imagenet%d_val_npz.zip' % (_URL_PREFIX, size),
      ])
      train_paths = [train_path]
    elif size == 64:
      # 64x64 uses more than one file due to its size.
      train1_path, train2_path, val_path = dl_manager.download([
          f'{_URL_PREFIX}/Imagenet64_train_part1_npz.zip',
          f'{_URL_PREFIX}/Imagenet64_train_part2_npz.zip',
          f'{_URL_PREFIX}/Imagenet64_val_npz.zip',
      ])
      train_paths = [train1_path, train2_path]
    else:
      raise ValueError('Size not implemented!')

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'archive': itertools.chain(
                    *[
                        dl_manager.iter_archive(train_path)
                        for train_path in train_paths
                    ]
                ),
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'archive': dl_manager.iter_archive(val_path),
            },
        ),
    ]

  def _generate_examples(self, archive):
    """Yields examples."""
    for fname, fobj in archive:
      content = fobj.read()
      if content:
        fobj_mem = io.BytesIO(content)
        data = np.load(fobj_mem, allow_pickle=False)
        size = self.builder_config.size
        for i, (image, label) in enumerate(zip(data['data'], data['labels'])):
          record = {
              # The data is packed flat as CHW where as most image datasets
              # in tensorflow are HWC. We reshape to recover CHW, then transpose
              # to put back into HWC.
              'image': np.reshape(image, (3, size, size)).transpose(1, 2, 0),
              # Labels in the original dataset are 1 indexed so we subtract 1
              # here.
              'label': label - 1,
          }
          yield fname + str(i), record
