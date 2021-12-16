# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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
import json
import random

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
This dataset contains images and a set of labels that expose certain characterisitics of that images, such as *varroa-mite* infections, bees carrying *pollen-packets* or bee that are *cooling the hive* by flappingn their wings. Additionally, this dataset contains images of *wasps* to be able to distinguish bees and wasps.

The images of the bees are taken from above and rotated. The bee is vertical and either its head or the trunk is on top. All images were taken with a green background and the distance to the bees was always the same, thus all bees have the same size.

Each image can have multiple labels assigned to it. E.g. a bee can be cooling the hive and have a varrio-mite infection at the same time.

This dataset is designed as mutli-label dataset, where each label, e.g. *varroa_output*, contains 1 if the characterisitic was present in the image and a 0 if it wasn't. All images are provided by 300 pixel height and 150 pixel witdh. As default the dataset provides the images as 150x75 (h,w) pixel. You can select 300 pixel height by loading the datset with the name "bee_dataset/bee_dataset_300" and with 200 pixel height by "bee_dataset/bee_dataset_200".

License: GNU GENERAL PUBLIC LICENSE

Author: Fabian Hickert <Fabian.Hickert@raspbee.de>
"""

_CITATION = """
@misc{BeeAlarmed - A camera based bee-hive monitoring,
  title =   "Dataset for a camera based bee-hive monitoring",
  url={https://github.com/BeeAlarmed}, journal={BeeAlarmed},
  author =  "Fabian Hickert",
  year   =  "2021",
  NOTE   = "\\url{https://raspbee.de/} and \\url{https://github.com/BeeAlarmed/BeeAlarmed}"
}
"""


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


class BeeDataset(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for BeeDataset dataset."""

  VERSION = tfds.core.Version('1.0.0')

  URL = 'https://raspbee.de/BeeDataset_20201121.zip'

  BEE_CFG_300 = BeeDatasetConfig(
      name='bee_dataset_300',
      description='BeeDataset images with 300 pixel height and 150 pixel width',
      version='1.0.0',
      image_height=300,
      image_width=150)

  BEE_CFG_200 = BeeDatasetConfig(
      name='bee_dataset_200',
      description='BeeDataset images with 200 pixel height and 100 pixel width',
      version='1.0.0',
      image_height=200,
      image_width=100)

  BEE_CFG_150 = BeeDatasetConfig(
      name='bee_dataset_150',
      description='BeeDataset images with 200 pixel height and 100 pixel width',
      version='1.0.0',
      image_height=150,
      image_width=75)

  BUILDER_CONFIGS = [BEE_CFG_300, BEE_CFG_200, BEE_CFG_150]

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    t_shape = (self.builder_config.height, self.builder_config.width,
               self.builder_config.depth)
    features = tfds.features.FeaturesDict({
        'input': tfds.features.Image(shape=t_shape),
        'output': {
            'varroa_output': tf.float64,
            'pollen_output': tf.float64,
            'wasps_output': tf.float64,
            'cooling_output': tf.float64,
        }
    })

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=features,
        supervised_keys=('input', 'output'),
        homepage='https://raspbee.de',
        citation=_CITATION,
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
              'cooling_output': labels[3]
          }
      }
