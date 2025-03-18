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

"""Grounded Scan dataset."""
from __future__ import annotations

import json
import os
from typing import List

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
Grounded SCAN (gSCAN) is a synthetic dataset for evaluating compositional
generalization in situated language understanding. gSCAN pairs natural language
instructions with action sequences, and requires the agent to interpret
instructions within the context of a grid-based visual navigation environment.

More information can be found at:

* For the `compositional_splits` and the `target_length_split`:
https://github.com/LauraRuis/groundedSCAN

* For the `spatial_relation_splits`:
https://github.com/google-research/language/tree/master/language/gscan/data
"""

_CITATION = """
@inproceedings{NEURIPS2020_e5a90182,
 author = {Ruis, Laura and Andreas, Jacob and Baroni, Marco and Bouchacourt, Diane and Lake, Brenden M},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {H. Larochelle and M. Ranzato and R. Hadsell and M. F. Balcan and H. Lin},
 pages = {19861--19872},
 publisher = {Curran Associates, Inc.},
 title = {A Benchmark for Systematic Generalization in Grounded Language Understanding},
 url = {https://proceedings.neurips.cc/paper/2020/file/e5a90182cc81e12ab5e72d66e0b46fe3-Paper.pdf},
 volume = {33},
 year = {2020}
}

@inproceedings{qiu-etal-2021-systematic,
    title = "Systematic Generalization on g{SCAN}: {W}hat is Nearly Solved and What is Next?",
    author = "Qiu, Linlu  and
      Hu, Hexiang  and
      Zhang, Bowen  and
      Shaw, Peter  and
      Sha, Fei",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.166",
    doi = "10.18653/v1/2021.emnlp-main.166",
    pages = "2180--2188",
}
"""

_GSCAN_DATA_PATH = (
    'https://raw.githubusercontent.com/LauraRuis/groundedSCAN/master/data/'
)
_SPATIAL_DATA_PATH = 'https://storage.googleapis.com/gresearch/gscan/'


class GroundedScanConfig(tfds.core.BuilderConfig):
  """BuilderConfig for groundedSCAN."""

  def __init__(self, *, data_path: str, splits_names: List[str], **kwargs):
    """BuilderConfig for groundedSCAN.

    Args:
      data_path: path from which data will be downloaded.
      splits_names: list of splits for the given config.
      **kwargs: keyword arguments forwarded to super.
    """
    super(GroundedScanConfig, self).__init__(**kwargs)
    self.data_path = data_path
    self.splits_names = splits_names


class GroundedScan(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for grounded_scan dataset."""

  BUILDER_CONFIGS = [
      GroundedScanConfig(
          name='compositional_splits',
          description='Examples for compositional generalization.',
          data_path=os.path.join(_GSCAN_DATA_PATH, 'compositional_splits.zip'),
          splits_names=[
              'train',
              'dev',
              'test',
              'visual',
              'situational_1',
              'situational_2',
              'contextual',
              'adverb_1',
              'adverb_2',
              'visual_easier',
          ],
      ),
      GroundedScanConfig(
          name='target_length_split',
          description='Examples for generalizing to larger target lengths.',
          data_path=os.path.join(_GSCAN_DATA_PATH, 'target_length_split.zip'),
          splits_names=['train', 'dev', 'test', 'target_lengths'],
      ),
      GroundedScanConfig(
          name='spatial_relation_splits',
          description='Examples for spatial relation reasoning.',
          data_path=os.path.join(
              _SPATIAL_DATA_PATH, 'spatial_relation_splits.zip'
          ),
          splits_names=[
              'train',
              'dev',
              'test',
              'visual',
              'relation',
              'referent',
              'relative_position_1',
              'relative_position_2',
          ],
      ),
  ]

  VERSION = tfds.core.Version('2.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.1.0': 'Changed `vector` feature to Text().',
      '2.0.0': 'Adds the new spatial_relation_splits config.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    position_feature = tfds.features.FeaturesDict(
        {'row': np.int32, 'column': np.int32}
    )
    object_feature = tfds.features.FeaturesDict({
        'vector': tfds.features.Text(),
        'position': position_feature,
        'object': tfds.features.FeaturesDict({
            'shape': tfds.features.Text(),
            'color': tfds.features.Text(),
            'size': np.int32,
        }),
    })
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'situation': tfds.features.FeaturesDict({
                'grid_size': np.int32,
                'agent_position': position_feature,
                'agent_direction': np.int32,
                'target_object': object_feature,
                'distance_to_target': np.int32,
                'direction_to_target': tfds.features.Text(),
                'placed_objects': tfds.features.Sequence(object_feature),
            }),
            'target_commands': tfds.features.Sequence(tfds.features.Text()),
            'command': tfds.features.Sequence(tfds.features.Text()),
            'meaning': tfds.features.Sequence(tfds.features.Text()),
            'verb_in_command': tfds.features.Text(),
            'manner': tfds.features.Text(),
            'referred_target': tfds.features.Text(),
        }),
        supervised_keys=None,
        homepage='https://github.com/LauraRuis/groundedSCAN',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""

    path = dl_manager.download_and_extract(self.builder_config.data_path)
    return {
        split_name: self._generate_examples(
            path / self.builder_config.name, split_name=split_name
        )
        for split_name in self.builder_config.splits_names
    }

  def _generate_examples(self, path, split_name):
    """Yields examples."""

    beam = tfds.core.lazy_imports.apache_beam

    def _get_position_feature(raw_position):
      return {
          'row': int(raw_position['row']),
          'column': int(raw_position['column']),
      }

    def _get_object_feature(raw_object):
      return {
          'vector': raw_object['vector'].strip(),
          'position': _get_position_feature(raw_object['position']),
          'object': {
              'shape': raw_object['object']['shape'],
              'color': raw_object['object']['color'],
              'size': int(raw_object['object']['size']),
          },
      }

    def _parse_sparse_situation_to_feature(situation):
      return {
          'grid_size': int(situation['grid_size']),
          'agent_direction': int(situation['agent_direction']),
          'distance_to_target': int(situation['grid_size']),
          'direction_to_target': situation['direction_to_target'],
          'agent_position': _get_position_feature(situation['agent_position']),
          'target_object': _get_object_feature(situation['target_object']),
          'placed_objects': [
              _get_object_feature(obj)
              for obj in situation['placed_objects'].values()
          ],
      }

    def _preprocess(example):
      return {
          'command': example['command'].split(','),
          'target_commands': example['target_commands'].split(','),
          'meaning': example['meaning'].split(','),
          'manner': example['manner'],
          'verb_in_command': example['verb_in_command'],
          'referred_target': example['referred_target'],
          'situation': _parse_sparse_situation_to_feature(example['situation']),
      }

    def _yield_examples(path):
      dataset_path = os.path.join(path, 'dataset.txt')
      with tf.io.gfile.GFile(dataset_path, 'r') as f:
        dataset = json.load(f)
      for i, example in enumerate(dataset['examples'][split_name]):
        yield f'{split_name}_{i}', _preprocess(example)

    return 'Create pipeline' >> beam.Create(
        [path]
    ) | 'Process samples' >> beam.FlatMap(_yield_examples)
