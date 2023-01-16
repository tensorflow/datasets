# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""asset dataset for tuning and evaluating text simplification models."""

import csv

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_HOMEPAGE = 'https://github.com/facebookresearch/asset'

_LICENSE = 'Creative Common Attribution-NonCommercial 4.0 International'

_URL_LIST = [
    (
        'human_ratings.csv',
        'https://raw.githubusercontent.com/facebookresearch/asset/main/human_ratings/human_ratings.csv',
    ),
    (
        'asset.valid.orig',
        'https://raw.githubusercontent.com/facebookresearch/asset/main/dataset/asset.valid.orig',
    ),
    (
        'asset.test.orig',
        'https://raw.githubusercontent.com/facebookresearch/asset/main/dataset/asset.test.orig',
    ),
]

# https://github.com/facebookresearch/asset/raw/master/dataset/

_URL_LIST += [
    (  # pylint:disable=g-complex-comprehension
        f'asset.{spl}.simp.{i}',
        f'https://raw.githubusercontent.com/facebookresearch/asset/main/dataset/asset.{spl}.simp.{i}',
    )
    for spl in ['valid', 'test']
    for i in range(10)
]

_URLs = dict(_URL_LIST)


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for asset dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name='simplification',
          description=(
              'A set of original sentences aligned with 10 possible'
              ' simplifications for each.'
          ),
      ),
      tfds.core.BuilderConfig(
          name='ratings',
          description=(
              'Human ratings of automatically produced text simplification.'
          ),
      ),
  ]

  DEFAULT_CONFIG_NAME = 'simplification'

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""

    if self.builder_config.name == 'simplification':
      features = tfds.features.FeaturesDict({
          'original': tfds.features.Text(),
          'simplifications': tfds.features.Sequence(tfds.features.Text()),
      })
    else:
      features = tfds.features.FeaturesDict({
          'original': tfds.features.Text(),
          'simplification': tfds.features.Text(),
          'original_sentence_id': np.int32,
          'aspect': tfds.features.ClassLabel(
              names=['meaning', 'fluency', 'simplicity']
          ),
          'worker_id': np.int32,
          'rating': np.int32,
      })

    return self.dataset_info_from_configs(
        features=features,
        supervised_keys=None,
        homepage=_HOMEPAGE,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    data_dir = dl_manager.download_and_extract(_URLs)
    if self.builder_config.name == 'simplification':
      return {
          'validation': self._generate_examples(
              filepaths=data_dir, split='valid'
          ),
          'test': self._generate_examples(filepaths=data_dir, split='test'),
      }
    else:
      return {
          'full': self._generate_examples(filepaths=data_dir, split='full'),
      }

  def _generate_examples(self, filepaths, split):
    """Yields examples."""

    if self.builder_config.name == 'simplification':
      files = [tf.io.gfile.GFile(filepaths[f'asset.{split}.orig'])] + [
          tf.io.gfile.GFile(filepaths[f'asset.{split}.simp.{i}'])
          for i in range(10)
      ]
      for id_, lines in enumerate(zip(*files)):
        yield id_, {
            'original': lines[0].strip(),
            'simplifications': [line.strip() for line in lines[1:]],
        }
    else:
      with tf.io.gfile.GFile(filepaths['human_ratings.csv']) as f:
        reader = csv.reader(f, delimiter=',')
        for id_, row in enumerate(reader):
          if id_ == 0:
            keys = row[:]
          else:
            res = {}
            for k, v in zip(keys, row):
              res[k] = v
            for k in ['original_sentence_id', 'worker_id', 'rating']:
              res[k] = int(res[k])
            yield (id_ - 1), res
