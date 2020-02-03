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

"""CFQ (Compositional Freebase Question) dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import json
import os
from absl import logging
import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_CITATION = """
@inproceedings{Lake2018GeneralizationWS,
  title={Measuring Compositional Generalization: A Comprehensive Method on
         Realistic Data},
  author={Daniel Keysers, et al.},
  booktitle={ICLR},
  year={2020},
  url={https://arxiv.org/abs/1912.09713.pdf},
}
"""

_DESCRIPTION = """
The CFQ dataset (and it's splits) for measuring compositional generalization.

See https://arxiv.org/abs/1912.09713.pdf for background.

Example usage:
data = tfds.load('cfq/mcd1')
"""

_DATA_URL = 'https://storage.googleapis.com/cfq_dataset/cfq.tar.gz'


class CFQConfig(tfds.core.BuilderConfig):
  """BuilderConfig for CFQ splits."""

  @tfds.core.disallow_positional_args
  def __init__(self, name, directory='splits', **kwargs):
    """BuilderConfig for CFQ.

    Args:
      name: Unique name of the split.
      directory: Which subdirectory to read the split from.
      **kwargs: keyword arguments forwarded to super.
    """
    # Version history:
    super(CFQConfig, self).__init__(
        name=name,
        version=tfds.core.Version('1.0.0'),
        description=_DESCRIPTION,
        **kwargs)
    self.split_file = os.path.join(directory, name + '.json')


_QUESTION = 'question'
_QUERY = 'query'


class CFQ(tfds.core.GeneratorBasedBuilder):
  """CFQ task / splits."""

  BUILDER_CONFIGS = [
      CFQConfig(name='mcd1'),
      CFQConfig(name='mcd2'),
      CFQConfig(name='mcd3'),
      CFQConfig(name='question_complexity_split'),
      CFQConfig(name='question_pattern_split'),
      CFQConfig(name='query_complexity_split'),
      CFQConfig(name='query_pattern_split'),
      CFQConfig(name='random_split'),
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            _QUESTION: tfds.features.Text(),
            _QUERY: tfds.features.Text(),
        }),
        supervised_keys=(_QUESTION, _QUERY),
        homepage='https://github.com/google-research/google-research/tree/master/cfq',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    data_dir = dl_manager.download_and_extract(_DATA_URL)
    data_dir = os.path.join(data_dir, 'cfq')
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'base_directory': data_dir,
                'splits_file': self.builder_config.split_file,
                'split_id': 'trainIdxs'
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'base_directory': data_dir,
                'splits_file': self.builder_config.split_file,
                'split_id': 'testIdxs'
            })
    ]

  def _generate_examples(self, base_directory, splits_file, split_id):
    """Yields examples."""
    samples_path = os.path.join(base_directory, 'dataset.json')
    splits_path = os.path.join(base_directory, splits_file)
    with tf.io.gfile.GFile(samples_path) as samples_file:
      with tf.io.gfile.GFile(splits_path) as splits_file:
        logging.info('Reading json from %s into memory...', samples_path)
        samples = json.load(samples_file)
        logging.info('Loaded json data from %s.', samples_path)
        splits = json.load(splits_file)
        for idx in splits[split_id]:
          sample = samples[idx]
          yield idx, {_QUESTION: sample['questionPatternModEntities'],
                      _QUERY: sample['sparqlPatternModEntities']}
