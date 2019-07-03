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

"""So2SAT remote sensing dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import h5py
import numpy as np
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """\
So2Sat LCZ42 is a dataset consisting of co-registered synthetic aperture radar
and multispectral optical image patches acquired by the Sentinel-1 and
Sentinel-2 remote sensing satellites, and the corresponding local climate zones
(LCZ) label. The dataset is distributed over 42 cities across different
continents and cultural regions of the world.

The full dataset (`all`) consists of 8 Sentinel-1 and 10 Sentinel-2 channels.
Alternatively, one can select the `rgb` subset, which contains only the optical
frequency bands of Sentinel-2, rescaled and encoded as JPEG.

Dataset URL: http://doi.org/10.14459/2018MP1454690
License: http://creativecommons.org/licenses/by/4.0
"""

_LABELS = [
    'Compact high-rise', 'Compact mid-rise', 'Compact low-rise',
    'Open high-rise', 'Open mid-rise', 'Open low-rise', 'Lightweight low-rise',
    'Large low-rise', 'Sparsely built', 'Heavy industry', 'Dense trees',
    'Scattered trees', 'Bush or scrub', 'Low plants', 'Bare rock or paved',
    'Bare soil or sand', 'Water'
]

_DATA_OPTIONS = ['rgb', 'all']

# Maximal value observed for the optical channels of Sentinel-2 in this dataset.
_OPTICAL_MAX_VALUE = 2.8


class So2satConfig(tfds.core.BuilderConfig):
  """BuilderConfig for so2sat."""

  def __init__(self, selection=None, **kwargs):
    """Constructs a So2satConfig.

    Args:
      selection: `str`, one of `_DATA_OPTIONS`.
      **kwargs: keyword arguments forwarded to super.
    """
    kwargs['supported_versions'] = [
        tfds.core.Version('1.0.0', experiments={tfds.core.Experiment.S3: True}),
    ]
    if selection not in _DATA_OPTIONS:
      raise ValueError('selection must be one of %s' % _DATA_OPTIONS)

    super(So2satConfig, self).__init__(**kwargs)
    self.selection = selection


class So2sat(tfds.core.GeneratorBasedBuilder):
  """So2SAT remote sensing dataset."""

  BUILDER_CONFIGS = [
      So2satConfig(
          selection='rgb',
          name='rgb',
          version=tfds.core.Version('0.0.1'),
          description='Sentinel-2 RGB channels'),
      So2satConfig(
          selection='all',
          name='all',
          version=tfds.core.Version('0.0.1'),
          description='8 Sentinel-1 and 10 Sentinel-2 channels'),
  ]

  def _info(self):
    if self.builder_config.selection == 'rgb':
      features = tfds.features.FeaturesDict({
          'image': tfds.features.Image(shape=[32, 32, 3]),
          'label': tfds.features.ClassLabel(names=_LABELS),
          'sample_id': tfds.features.Tensor(shape=(), dtype=tf.int64),
      })
      supervised_keys = ('image', 'label')
    elif self.builder_config.selection == 'all':
      features = tfds.features.FeaturesDict({
          'sentinel1':
              tfds.features.Tensor(shape=[32, 32, 8], dtype=tf.float32),
          'sentinel2':
              tfds.features.Tensor(shape=[32, 32, 10], dtype=tf.float32),
          'label':
              tfds.features.ClassLabel(names=_LABELS),
          'sample_id':
              tfds.features.Tensor(shape=(), dtype=tf.int64),
      })
      supervised_keys = None
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features,
        supervised_keys=supervised_keys,
        urls=['http://doi.org/10.14459/2018MP1454690'],
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    paths = dl_manager.download({
        'train': 'ftp://m1454690:m1454690@dataserv.ub.tum.de/training.h5',
        'val': 'ftp://m1454690:m1454690@dataserv.ub.tum.de/validation.h5'
    })
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            num_shards=20,
            gen_kwargs={
                'path': paths['train'],
                'selection': self.builder_config.selection,
            },
        ),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            num_shards=5,
            gen_kwargs={
                'path': paths['val'],
                'selection': self.builder_config.selection,
            },
        ),
    ]

  def _generate_examples(self, path, selection):
    """Yields examples."""
    with h5py.File(path, 'r') as fid:
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
        if self.version.implements(tfds.core.Experiment.S3):
          yield i, record
        else:
          yield record


def _create_rgb(sen2_bands):
  return np.clip(sen2_bands[..., [2, 1, 0]] / _OPTICAL_MAX_VALUE * 255.0, 0,
                 255).astype(np.uint8)
