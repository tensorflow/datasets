# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""BeeDataset dataset."""
from __future__ import annotations

import json
import random

import numpy as np
import tensorflow_datasets.public_api as tfds


class BeeDatasetConfig(tfds.core.BuilderConfig):
  """BuilderConfig for the BeeDataset.

  Args:
  image_width (int): Desired image width.
  image_height (int): Desired image heigth.
  """

  def __init__(self, image_height=300, image_width=150, **kwargs):
    super().__init__(**kwargs)
    self.width = image_width
    self.height = image_height
    self.depth = 3


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for BeeDataset dataset."""

  VERSION = tfds.core.Version('1.0.0')

  URL = 'https://raspbee.de/BeeDataset_20201121.zip'

  BEE_CFG_300 = BeeDatasetConfig(
      name='bee_dataset_300',
      description='BeeDataset images with 300 pixel height and 150 pixel width',
      version='1.0.0',
      image_height=300,
      image_width=150,
  )

  BEE_CFG_200 = BeeDatasetConfig(
      name='bee_dataset_200',
      description='BeeDataset images with 200 pixel height and 100 pixel width',
      version='1.0.0',
      image_height=200,
      image_width=100,
  )

  BEE_CFG_150 = BeeDatasetConfig(
      name='bee_dataset_150',
      description='BeeDataset images with 200 pixel height and 100 pixel width',
      version='1.0.0',
      image_height=150,
      image_width=75,
  )

  BUILDER_CONFIGS = [BEE_CFG_300, BEE_CFG_200, BEE_CFG_150]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    t_shape = (
        self.builder_config.height,
        self.builder_config.width,
        self.builder_config.depth,
    )
    features = tfds.features.FeaturesDict({
        'input': tfds.features.Image(shape=t_shape),
        'output': {
            'varroa_output': np.float64,
            'pollen_output': np.float64,
            'wasps_output': np.float64,
            'cooling_output': np.float64,
        },
    })

    return self.dataset_info_from_configs(
        features=features,
        supervised_keys=('input', 'output'),
        homepage='https://raspbee.de',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract(self.URL)
    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    # Load labels and image path.
    data = json.loads((path / 'data.json').read_text())
    indexes = list(data.keys())
    random.shuffle(indexes)
    for name in indexes:
      labels = []
      entry = data[name]

      for lbl in ['varroa', 'pollen', 'wasps', 'cooling']:
        labels.append(1.0 if entry[lbl] else 0.0)

      img = path / f'images_{self.builder_config.height}' / name

      yield name + str(self.builder_config.height), {
          'input': img,
          'output': {
              'varroa_output': labels[0],
              'pollen_output': labels[1],
              'wasps_output': labels[2],
              'cooling_output': labels[3],
          },
      }
