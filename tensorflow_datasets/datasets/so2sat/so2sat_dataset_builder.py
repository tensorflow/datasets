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

"""So2SAT remote sensing dataset."""

import numpy as np
import tensorflow_datasets.public_api as tfds

_LABELS = [
    'Compact high-rise',
    'Compact mid-rise',
    'Compact low-rise',
    'Open high-rise',
    'Open mid-rise',
    'Open low-rise',
    'Lightweight low-rise',
    'Large low-rise',
    'Sparsely built',
    'Heavy industry',
    'Dense trees',
    'Scattered trees',
    'Bush or scrub',
    'Low plants',
    'Bare rock or paved',
    'Bare soil or sand',
    'Water',
]

_DATA_OPTIONS = ['rgb', 'all']

# Calibration for the optical RGB channels of Sentinel-2 in this dataset.
_OPTICAL_CALIBRATION_FACTOR = 3.5 * 255.0


class So2satConfig(tfds.core.BuilderConfig):
  """BuilderConfig for so2sat."""

  def __init__(self, selection=None, **kwargs):
    """Constructs a So2satConfig.

    Args:
      selection: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    if selection not in _DATA_OPTIONS:
      raise ValueError('selection must be one of %s' % _DATA_OPTIONS)

    v2 = tfds.core.Version('2.0.0')
    v2_1 = tfds.core.Version('2.1.0')

    super(So2satConfig, self).__init__(
        version=v2_1,
        supported_versions=[v2],
        release_notes={
            '2.0.0': 'New split API (https://tensorflow.org/datasets/splits)',
            '2.1.0': 'Using updated optical channels calibration factor.',
        },
        **kwargs,  # pytype: disable=wrong-arg-types  # gen-stub-imports
    )
    self.selection = selection


class Builder(tfds.core.GeneratorBasedBuilder):
  """So2SAT remote sensing dataset."""

  BUILDER_CONFIGS = [
      So2satConfig(
          selection='rgb', name='rgb', description='Sentinel-2 RGB channels'
      ),
      So2satConfig(
          selection='all',
          name='all',
          description='8 Sentinel-1 and 10 Sentinel-2 channels',
      ),
  ]

  def _info(self):
    if self.builder_config.selection == 'rgb':
      features = tfds.features.FeaturesDict({
          'image': tfds.features.Image(shape=[32, 32, 3]),
          'label': tfds.features.ClassLabel(names=_LABELS),
          'sample_id': tfds.features.Tensor(shape=(), dtype=np.int64),
      })
      supervised_keys = ('image', 'label')
    elif self.builder_config.selection == 'all':
      features = tfds.features.FeaturesDict({
          'sentinel1': tfds.features.Tensor(
              shape=[32, 32, 8], dtype=np.float32
          ),
          'sentinel2': tfds.features.Tensor(
              shape=[32, 32, 10], dtype=np.float32
          ),
          'label': tfds.features.ClassLabel(names=_LABELS),
          'sample_id': tfds.features.Tensor(shape=(), dtype=np.int64),
      })
      supervised_keys = None
    return self.dataset_info_from_configs(
        features=features,
        supervised_keys=supervised_keys,
        homepage='http://doi.org/10.14459/2018MP1454690',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    paths = dl_manager.download({
        'train': 'ftp://m1454690:m1454690@dataserv.ub.tum.de/training.h5',
        'val': 'ftp://m1454690:m1454690@dataserv.ub.tum.de/validation.h5',
    })
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'path': paths['train'],
                'selection': self.builder_config.selection,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={
                'path': paths['val'],
                'selection': self.builder_config.selection,
            },
        ),
    ]

  def _generate_examples(self, path, selection):
    """Yields examples."""
    with tfds.core.lazy_imports.h5py.File(path, 'r') as fid:
      sen1 = fid['sen1']
      sen2 = fid['sen2']
      label = fid['label']
      for i in range(len(sen1)):
        if selection == 'rgb':
          record = {
              'image': _create_rgb(sen2[i]),
              'label': np.argmax(label[i]).astype(int),
              'sample_id': i,
          }
        elif selection == 'all':
          record = {
              'sentinel1': sen1[i].astype(np.float32),
              'sentinel2': sen2[i].astype(np.float32),
              'label': np.argmax(label[i]).astype(int),
              'sample_id': i,
          }
        yield i, record


def _create_rgb(sen2_bands):
  return np.clip(
      sen2_bands[..., [2, 1, 0]] * _OPTICAL_CALIBRATION_FACTOR, 0, 255
  ).astype(np.uint8)
