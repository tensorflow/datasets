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

"""*-CFQ (Star-CFQ) dataset suite."""

import json
import os

from absl import logging
from etils import epath
import tensorflow_datasets.public_api as tfds

_DATA_URL = 'https://storage.googleapis.com/star_cfq_dataset'

_RANDOM_SEEDS = [
    '4_0',
    '4_42',
    '4_81',
    '4_86',
    '4.25_0',
    '4.25_121',
    '4.25_125',
    '4.25_142',
    '4.5_0',
    '4.5_45',
    '4.5_82',
    '4.5_87',
    '4.75_0',
    '4.75_122',
    '4.75_126',
    '4.75_145',
    '5_0',
    '5_50',
    '5_83',
    '5_88',
    '5.25_0',
    '5.25_123',
    '5.25_127',
    '5.25_150',
    '5.5_0',
    '5.5_55',
    '5.5_84',
    '5.5_89',
    '5.75_0',
    '5.75_124',
    '5.75_128',
    '5.75_155',
    '6_0',
    '6_71',
    '6_85',
    '6_90',
]

_SHARD_SIZE = 95742

# '' is used for CFQ, 'o' is used for o-CFQ, and so on.
_POOLS = ['', 'o', 'u', 'b', 'l', 'half_l', 'n', 'half_n', 'x', 'half_x']
_SUPPLEMENTARY_POOLS = ['l', 'half_l', 'n', 'half_n', 'x', 'half_x']

_UCFQ_POOL = 'u-CFQ'

_NONBLENDED_TRAIN_SET_SIZES = {
    'default': [0.25, 0.5, 0.75, 1, 3, 10, 30, 80, 100],
    '': [0.1, 0.2, 0.3, 0.5, 1, 2],
    'b': [
        0.1,
        0.2,
        0.25,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7,
        0.75,
        0.8,
        1,
        1.5,
        2,
        3,
        4,
        5,
        6,
        8,
        10,
        11,
        12,
        13,
        15,
        30,
        35,
        80,
        85,
        100,
    ],
    'o': [0.1, 0.2, 0.3, 0.5, 1, 2],
    'u': [0.1, 0.2, 0.3, 0.5, 1, 2, 3, 6, 10, 30, 100],
}
_BLENDING_INITIAL_SIZES = [0, 0.1, 0.2, 0.3, 0.5, 1, 2, 3, 5]
_BLENDING_SUPPLEMENTARY_SIZES = [0.1, 0.3, 1, 2, 3, 10, 30, 80, 100]
_UNIQUE_INITIAL_SIZES = [0.1, 1]
_OVERWEIGHTING_SIZES = [0.1, 0.3, 1, 3, 10, 30, 80]
# Smaller sizes are skipped to limit the number of generated builder configs.
_DIVERGENCE_SPLIT_SIZES = [0.333333]

_QUESTION = 'question'
_QUERY = 'query'
_QUESTION_FIELD = 'questionPatternModEntities'
_QUERY_FIELD = 'sparqlPatternModEntities'


class StarCFQConfig(tfds.core.BuilderConfig):
  """BuilderConfig for *-CFQ splits."""

  def __init__(
      self,
      *,
      name,
      split_archive_path,
      split_path,
      compound_divergence=False,
      **kwargs,
  ):
    """BuilderConfig for a *-CFQ dataset.

    Args:
      name: Unique name of the split.
      split_archive_path: Path to the archive containing the split file.
      split_path: Relative path to the split file in the archive.
      compound_divergence: If true, the config corresponds to a compound
        divergence split. Otherwise, it corresponds to a random split.
      **kwargs: keyword arguments forwarded to super.
    """
    super(StarCFQConfig, self).__init__(
        name=name, version=tfds.core.Version('1.1.0'), **kwargs
    )
    self.split_archive_path = split_archive_path
    self.split_path = split_path
    self.compound_divergence = compound_divergence


def _generate_compound_divergence_builder_configs():
  """Generate configs for different compound divergences and random seeds."""
  configs = []
  for size in _DIVERGENCE_SPLIT_SIZES:
    for compound_divergence in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]:
      for seed_idx, seed in enumerate(_RANDOM_SEEDS):
        configs.append(
            StarCFQConfig(
                name=f'u_cfq_compound_divergence_{size}_{compound_divergence}_r{seed_idx}',
                compound_divergence=True,
                split_archive_path='splits/u-cfq-divergence-splits-1.0.tar.gz',
                split_path=f'divergence_splits/divergence_split_s{size}_d{compound_divergence}_r{seed}.json',
            )
        )

  return configs


def _generate_single_pool_random_split_builder_configs():
  """Generate configs for random splits using the same pool for train & test."""
  configs = []
  for pool in _POOLS:
    for size in _NONBLENDED_TRAIN_SET_SIZES.get(
        pool, _NONBLENDED_TRAIN_SET_SIZES['default']
    ):
      full_pool_name = '_'.join([pool, 'cfq']).lstrip('_')
      configs.append(
          StarCFQConfig(
              name=f'single_pool_{size}x_{full_pool_name}',
              split_archive_path='splits/star-cfq-random-splits-1.0.tar.gz',
              split_path=f'random_splits/train_{size}x_{full_pool_name}__test_1x_{full_pool_name}.json',
          )
      )
  return configs


def _generate_ungrounded_on_grounded_builder_configs():
  """Generate configs for random splits training on ungrounded and testing on grounded data."""
  configs = []
  for size in _NONBLENDED_TRAIN_SET_SIZES['u']:
    # Out of the usual train set sizes for u-CFQ, there was no split created
    # with 6x u-CFQ train set and an o-CFQ test set.
    if size == 6:
      continue
    configs.append(
        StarCFQConfig(
            name=f'ungrounded_on_grounded_{size}x',
            split_archive_path='splits/star-cfq-random-splits-1.0.tar.gz',
            split_path=f'random_splits/train_{size}x_u_cfq__test_1x_o_cfq.json',
        )
    )
  return configs


def _generate_blended_split_builder_configs():
  """Generate configs for blended random splits."""
  configs = []
  split_archive_path = 'splits/star-cfq-random-splits-1.0.tar.gz'
  for supplementary_pool in _SUPPLEMENTARY_POOLS:
    for initial_size in _BLENDING_INITIAL_SIZES:
      for supplementary_size in _BLENDING_SUPPLEMENTARY_SIZES:
        # Some splits with 80x n-CFQ/half-n-CFQ sizes are missing, skip them.
        if supplementary_size == 80 and (
            supplementary_pool in ['n', 'half_n']
            or initial_size not in [0, 0.1, 1]
        ):
          continue
        if initial_size != 0:
          configs.append(
              StarCFQConfig(
                  name=f'equal_weighting_{initial_size}x_b_cfq_{supplementary_size}x_{supplementary_pool}_cfq',
                  split_archive_path=split_archive_path,
                  split_path=f'random_splits/train_{initial_size}x_b_cfq_{supplementary_size}x_{supplementary_pool}_cfq__test_1x_b_cfq.json',
              )
          )
        else:
          configs.append(
              StarCFQConfig(
                  name=f'equal_weighting_0x_b_cfq_{supplementary_size}x_{supplementary_pool}_cfq',
                  split_archive_path=split_archive_path,
                  split_path=f'random_splits/train_{supplementary_size}x_{supplementary_pool}_cfq__test_1x_b_cfq.json',
              )
          )
  for unique_initial_size in _UNIQUE_INITIAL_SIZES:
    for supplementary_pool in _SUPPLEMENTARY_POOLS:
      for size in _OVERWEIGHTING_SIZES:
        # Splits with 80x n-CFQ/half-n-CFQ sizes are missing, skip them for now.
        if size == 80 and supplementary_pool in ['n', 'half_n']:
          continue
        # This split file is missing, skip it in this version.
        if (
            unique_initial_size == 1
            and size == 1
            and supplementary_pool == 'half_n'
        ):
          continue
        configs.append(
            StarCFQConfig(
                name=f'overweighting_{unique_initial_size}x_unique_{size}x_b_cfq_{size}x_{supplementary_pool}_cfq',
                split_archive_path=split_archive_path,
                split_path=f'random_splits/train_{unique_initial_size}x_unique_{size}x_b_cfq_{size}x_{supplementary_pool}_cfq__test_1x_b_cfq.json',
            )
        )

  return configs


def _read_pool_shard(pool_path, index):
  path = os.path.join(pool_path, 'dataset_%03d.json' % index)
  logging.info('Reading %s...', path)
  with epath.Path(path).open() as f:
    questions = json.load(f)
  return questions


class Slice:

  def __init__(self, shard_index, range_begin, range_end):
    self.shard_index = shard_index
    self.range_begin = range_begin
    self.range_end = range_end


def _get_dataset_slices(start, end):
  """Splits an absolute range to slices split by shard."""
  slices = []
  for shard_idx in range(int((end - 1) / _SHARD_SIZE) + 1):
    start_offset = shard_idx * _SHARD_SIZE
    end_offset = (shard_idx + 1) * _SHARD_SIZE
    if end_offset <= start:
      continue
    s = Slice(
        shard_idx,
        max(start, start_offset) % _SHARD_SIZE,
        (min(end, end_offset) - 1) % _SHARD_SIZE + 1,
    )
    slices.append(s)
  return slices


class Builder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for a *-CFQ split."""

  BUILDER_CONFIGS = (
      _generate_single_pool_random_split_builder_configs()
      + _generate_blended_split_builder_configs()
      + _generate_ungrounded_on_grounded_builder_configs()
      + _generate_compound_divergence_builder_configs()
  )

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=tfds.features.FeaturesDict({
            _QUESTION: tfds.features.Text(),
            _QUERY: tfds.features.Text(),
        }),
        supervised_keys=(_QUESTION, _QUERY),
        homepage='https://github.com/google-research/google-research/tree/master/star-cfq',
    )

  def _split_generators(self, dl_manager):
    """Returns SplitGenerators."""
    split_dir = dl_manager.download_and_extract(
        '%s/%s' % (_DATA_URL, self.builder_config.split_archive_path)
    )
    split_path = os.path.join(split_dir, self.builder_config.split_path)

    dataset_paths = {}
    if self.builder_config.compound_divergence:
      extracted_dataset_path = dl_manager.download_and_extract(
          _DATA_URL
          + '/datasets/u-cfq-for-divergence-splits-1.0-compact-combined.tar.gz'
      )
      dataset_paths[_UCFQ_POOL] = os.path.join(
          extracted_dataset_path,
          'u-cfq-for-divergence-splits-1.0-compact-combined',
      )

    else:
      with epath.Path(split_path).open() as file:
        splits = json.load(file)
        for split in splits.values():
          for s in split:
            name = s['dataset']
            if name in dataset_paths:
              continue
            logging.info('Downloading dataset %s...', name)
            extracted_dataset_path = dl_manager.download_and_extract(
                _DATA_URL + f'/datasets/{name.lower()}-1.0-compact.tar.gz'
            )
            dataset_paths[name] = os.path.join(
                extracted_dataset_path, f'{name.lower()}-1.0-compact'
            )

    if self.builder_config.compound_divergence:
      return {
          'train': self._generate_examples(
              dataset_paths, split_path, 'trainIdxs'
          ),
          'validation': self._generate_examples(
              dataset_paths, split_path, 'devIdxs'
          ),
          'test': self._generate_examples(
              dataset_paths, split_path, 'testIdxs'
          ),
      }
    return {
        'train': self._generate_examples(dataset_paths, split_path, 'train'),
        'test': self._generate_examples(dataset_paths, split_path, 'test'),
    }

  def _generate_examples(self, dataset_paths, split_path, split_id):
    """Yields examples."""
    if self.builder_config.compound_divergence:
      samples_path = os.path.join(dataset_paths[_UCFQ_POOL], 'dataset.json')
      with epath.Path(samples_path).open() as samples_file:
        logging.info('Reading json from %s into memory...', samples_path)
        samples = json.loads(samples_file.read())
        logging.info('%d samples loaded', len(samples))
        with epath.Path(split_path).open() as split_file:
          splits = json.loads(split_file.read())
          for idx in splits[split_id]:
            sample = samples[idx]
            yield idx, {
                _QUESTION: sample[_QUESTION_FIELD],
                _QUERY: sample[_QUERY_FIELD],
            }
    else:
      with epath.Path(split_path).open() as sf:
        split_config = json.load(sf)
      slice_index = 0
      for dss in split_config[split_id]:
        previous_shard = -1
        pool = None
        dataset = dss['dataset']
        if dataset not in dataset_paths:
          logging.error('Unexpected dataset %s', dataset)
          continue
        pool_path = dataset_paths[dataset]
        for rng in dss['indices']:
          start = int(rng['startIndex'])
          end = int(rng['endIndex'])
          for s in _get_dataset_slices(start, end):
            if previous_shard != s.shard_index:
              pool = _read_pool_shard(pool_path, s.shard_index)
              previous_shard = s.shard_index
            for idx in range(s.range_begin, s.range_end):
              absolute_index = s.shard_index * _SHARD_SIZE + idx
              # The slice_index is also part of the key because overweighting
              # splits use the same example multiple times and the key must
              # be unique for each instance.
              key = f'{dataset}-{absolute_index}-{slice_index}'
              yield key, {
                  _QUESTION: pool[idx][_QUESTION_FIELD],
                  _QUERY: pool[idx][_QUERY_FIELD],
              }
            slice_index += 1
