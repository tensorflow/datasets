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

"""rlu_rwrl dataset."""

import collections
import dataclasses
import functools
import os
from typing import Any, Dict, Generator, Optional, Sequence, Text, Tuple, Union

import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import rlu_common

_DESCRIPTION = """
Examples in the dataset represent SAR transitions stored when running a
partially online trained agent as described in https://arxiv.org/abs/1904.12901.
We follow the RLDS dataset format, as specified in
https://github.com/google-research/rlds#dataset-format.


We release 40 datasets on 8 tasks in total -- with no combined challenge and
easy combined challenge on the cartpole, walker, quadruped, and humanoid tasks.
Each task contains 5 different sizes of datasets, 1%, 5%, 20%, 40%, and 100%.
Note that the smaller dataset is not guaranteed to be a subset of the larger
ones. For details on how the dataset was generated, please refer to the paper.
"""

_CITATION = """
@misc{gulcehre2020rl,
    title={RL Unplugged: Benchmarks for Offline Reinforcement Learning},
    author={Caglar Gulcehre and Ziyu Wang and Alexander Novikov and Tom Le Paine
        and  Sergio Gómez Colmenarejo and Konrad Zolna and Rishabh Agarwal and
        Josh Merel and Daniel Mankowitz and Cosmin Paduraru and Gabriel
        Dulac-Arnold and Jerry Li and Mohammad Norouzi and Matt Hoffman and
        Ofir Nachum and George Tucker and Nicolas Heess and Nando deFreitas},
    year={2020},
    eprint={2006.13888},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
"""

_HOMEPAGE = 'https://github.com/deepmind/deepmind-research/tree/master/rl_unplugged'

# Env constants
DOMAIN_NAMES = (
    'cartpole',
    'quadruped',
    'walker',
    'humanoid',
)
DOMAIN_TO_TASK = {
    'cartpole': 'swingup',
    'quadruped': 'walk',
    'walker': 'walk',
    'humanoid': 'walk',
}
# https://github.com/google-research/realworldrl_suite#rwrl-combined-challenge-benchmarks
COMBINED_CHALLENGES = (None, 'easy')
DATASET_SIZES = (
    '1_percent',
    '5_percent',
    '20_percent',
    '40_percent',
    '100_percent',
)
SHARDS_MAPPING = {
    # ('combined_challenge','domain','dataset_size'): number of shards.
    (None, 'cartpole', '1_percent'):
        3,
    (None, 'cartpole', '5_percent'):
        3,
    (None, 'cartpole', '20_percent'):
        6,
    (None, 'cartpole', '40_percent'):
        6,
    (None, 'cartpole', '100_percent'):
        7,
    (None, 'quadruped', '1_percent'):
        3,
    (None, 'quadruped', '5_percent'):
        3,
    (None, 'quadruped', '20_percent'):
        4,
    (None, 'quadruped', '40_percent'):
        7,
    (None, 'quadruped', '100_percent'):
        10,
    (None, 'walker', '1_percent'):
        3,
    (None, 'walker', '5_percent'):
        6,
    (None, 'walker', '20_percent'):
        14,
    (None, 'walker', '40_percent'):
        48,
    (None, 'walker', '100_percent'):
        94,
    (None, 'humanoid', '1_percent'):
        9,
    (None, 'humanoid', '5_percent'):
        123,
    (None, 'humanoid', '20_percent'):
        125,
    (None, 'humanoid', '40_percent'):
        344,
    (None, 'humanoid', '100_percent'):
        391,
    ('easy', 'cartpole', '1_percent'):
        2,
    ('easy', 'cartpole', '5_percent'):
        3,
    ('easy', 'cartpole', '20_percent'):
        8,
    ('easy', 'cartpole', '40_percent'):
        8,
    ('easy', 'cartpole', '100_percent'):
        14,
    ('easy', 'quadruped', '1_percent'):
        3,
    ('easy', 'quadruped', '5_percent'):
        3,
    ('easy', 'quadruped', '20_percent'):
        9,
    ('easy', 'quadruped', '40_percent'):
        10,
    ('easy', 'quadruped', '100_percent'):
        15,
    ('easy', 'walker', '1_percent'):
        11,
    ('easy', 'walker', '5_percent'):
        17,
    ('easy', 'walker', '20_percent'):
        78,
    ('easy', 'walker', '40_percent'):
        137,
    ('easy', 'walker', '100_percent'):
        371,
    ('easy', 'humanoid', '1_percent'):
        18,
    ('easy', 'humanoid', '5_percent'):
        98,
    ('easy', 'humanoid', '20_percent'):
        244,
    ('easy', 'humanoid', '40_percent'):
        410,
    ('easy', 'humanoid', '100_percent'):
        769,
}
# Control suite tasks have 1000 timesteps per episode. One additional timestep
# accounts for the very first observation where no action has been taken yet.
DEFAULT_NUM_TIMESTEPS = 1001
_DELIMITER = ':'


@dataclasses.dataclass
class BuilderConfig(tfds.core.BuilderConfig):
  """Configuration of the task.

  Attributes:
    domain: The RealWorldRL environment domain.
    task: The RealWorldRL environment task.
    combined_challenge: Combines multiple challenges into the same environment.
      https://github.com/google-research/realworldrl_suite#rwrl-combined-challenge-benchmarks
    dataset_size: the size of the dataset.
  """
  domain: str = 'cartpole'
  task: str = 'swingup'
  combined_challenge: Optional[str] = None
  dataset_size: str = '1_percent'


def _builder_configs():
  """Creates a list of default builder configs."""
  configs = []
  for (combined_challenge, domain, dataset_size) in SHARDS_MAPPING:
    task = DOMAIN_TO_TASK[domain]
    # pytype: disable=wrong-keyword-args
    configs.append(
        BuilderConfig(
            name=(f'{domain}_{task}_'
                  f'combined_challenge_{str(combined_challenge).lower()}_'
                  f'{dataset_size}'),
            domain=domain,
            task=task,
            combined_challenge=combined_challenge,
            dataset_size=dataset_size))
    # pytype: enable=wrong-keyword-args
  return configs


def _decombine_key(k: str, delimiter: str = _DELIMITER) -> Sequence[str]:
  return k.split(delimiter)


def tf_example_to_feature_description(example: Union[tf.Tensor, bytes],
                                      num_timesteps=DEFAULT_NUM_TIMESTEPS):
  """Takes a string tensor encoding an tf example and returns its features."""
  if isinstance(example, tf.Tensor):
    if not tf.executing_eagerly():
      raise AssertionError(
          'tf_example_to_feature_description() only works under eager mode.')
    example = example.numpy()  # pytype: disable=attribute-error
  example = tf.train.Example.FromString(example)

  ret = {}
  for k, v in example.features.feature.items():
    l = len(v.float_list.value)
    if l % num_timesteps:
      raise ValueError('Unexpected feature length %d. It should be divisible '
                       'by num_timesteps: %d' % (l, num_timesteps))
    size = l // num_timesteps
    ret[k] = tf.io.FixedLenFeature([num_timesteps, size], tf.float32)
  return ret


def tree_deflatten_with_delimiter(
    flat_dict: Dict[str, Any], delimiter: str = _DELIMITER) -> Dict[str, Any]:
  """De-flattens a dict to its originally nested structure.

  Does the opposite of {combine_nested_keys(k) :v
                        for k, v in tree.flatten_with_path(nested_dicts)}
  Example: {'a:b': 1} -> {'a': {'b': 1}}
  Args:
    flat_dict: the keys of which equals the `path` separated by `delimiter`.
    delimiter: the delimiter that separates the keys of the nested dict.

  Returns:
    An un-flattened dict.
  """
  root = collections.defaultdict(dict)
  for delimited_key, v in flat_dict.items():
    keys = _decombine_key(delimited_key, delimiter=delimiter)
    node = root
    for k in keys[:-1]:
      node = node[k]
    node[keys[-1]] = v
  return dict(root)


def tf_feature_to_tfds_feature(nested: Union[tf.io.FixedLenFeature, Dict[Text,
                                                                         Any]]):
  """Converts potentially nested tf features into tfds features."""
  if isinstance(nested, tf.io.FixedLenFeature):
    # For some reason the dicts are transposed within the tfds features.
    # See transpose_dict_list() under
    # tensorflow_datasets/core/features/sequence_feature.py
    return tfds.features.Tensor(shape=nested.shape[1:], dtype=nested.dtype)  # pytype: disable=attribute-error
  elif isinstance(nested, dict):
    ret = type(nested)()
    for k, v in nested.items():
      ret[k] = tf_feature_to_tfds_feature(v)
    return ret
  else:
    raise ValueError(f'Unsupported type {type(nested)}')


class RluRwrl(rlu_common.RLUBuilder):
  """DatasetBuilder for rlu_rwrl dataset."""

  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.0.1': 'Fixes a bug in RLU RWRL dataset where there are duplicated '
               'episode ids in one of the humanoid datasets.',
  }
  _INPUT_FILE_PREFIX = 'gs://rl_unplugged/rwrl/'

  BUILDER_CONFIGS = _builder_configs()

  def get_features_dict(self):
    # Loads the features dynamically.
    file_paths = rlu_common.get_files(
        prefix=self.get_file_prefix(), num_shards=self.num_shards())

    # Take one item to get the output types and shapes.
    example_item = None
    iterator = tfds.as_numpy(tf.data.TFRecordDataset(file_paths[:1]))
    for example_item in iterator:
      break
    if example_item is None:
      raise ValueError('Empty dataset')

    feature_description = tf_example_to_feature_description(example_item)
    feature_description = tree_deflatten_with_delimiter(feature_description)
    return tfds.features.FeaturesDict({
        'steps':
            tfds.features.Dataset({
                'observation':
                    tf_feature_to_tfds_feature(
                        feature_description['observation']),
                'action':
                    tf_feature_to_tfds_feature(feature_description['action']),
                'reward':
                    tf_feature_to_tfds_feature(feature_description['reward']),
                'is_terminal':
                    tf.bool,
                'is_first':
                    tf.bool,
                'is_last':
                    tf.bool,
                'discount':
                    tf_feature_to_tfds_feature(feature_description['discount']),
            }),
        'episode_return':
            tf.float32,
    })

  def get_description(self):
    return _DESCRIPTION

  def get_citation(self):
    return _CITATION

  def get_file_prefix(self):
    domain = self.builder_config.domain
    task = self.builder_config.task
    combined_challenge = self.builder_config.combined_challenge
    dataset_size = self.builder_config.dataset_size
    return (f'{self._INPUT_FILE_PREFIX}/'
            f'combined_challenge_{str(combined_challenge).lower()}/'
            f'{domain}/{task}/{dataset_size}/episodes.tfrecord')

  def num_shards(self):
    try:
      return self._SHARDS  # For testing.  # type: ignore
    except AttributeError:
      pass
    domain = self.builder_config.domain
    combined_challenge = self.builder_config.combined_challenge
    dataset_size = self.builder_config.dataset_size
    return SHARDS_MAPPING[(combined_challenge, domain, dataset_size)]

  def tf_example_to_step_ds(self, tf_example: tf.Tensor,
                            feature_description) -> Dict[str, Any]:
    data = tf.io.parse_single_example(tf_example, feature_description)
    data = tree_deflatten_with_delimiter(data)

    # Shift the action and the rewards to conform to a common format.
    # The last action and reward will be a placeholder value.
    action = tf.concat((data['action'][1:], data['action'][:1]), axis=0)
    reward = tf.concat((data['reward'][1:], data['reward'][:1]), axis=0)
    discount = tf.concat((data['discount'][1:], data['discount'][:1]), axis=0)
    is_first = tf.concat([[True], [False] * tf.ones(DEFAULT_NUM_TIMESTEPS - 1)],
                         axis=0)
    is_last = tf.concat([[False] * tf.ones(DEFAULT_NUM_TIMESTEPS - 1), [True]],
                        axis=0)
    is_terminal = tf.squeeze(discount == 0., axis=-1)
    episode_return = tf.reduce_sum(reward)
    episode = {
        # Episode Metadata
        'episode_return': episode_return,
        'steps': {
            'observation': data['observation'],
            'action': action,
            'reward': reward,
            'discount': discount,
            'is_first': is_first,
            'is_last': is_last,
            'is_terminal': is_terminal,
        }
    }
    return episode

  def _generate_examples(self, paths):
    """Yields examples."""
    beam = tfds.core.lazy_imports.apache_beam
    file_paths = paths['file_paths']

    # Take one item to get the output types and shapes.
    example_item = None
    for example_item in tf.data.TFRecordDataset(file_paths[:1]).take(1):
      break
    if example_item is None:
      raise ValueError('Empty dataset')

    feature_description = tf_example_to_feature_description(example_item)

    def _generate_examples_one_file(
        path) -> Generator[Tuple[str, Dict[str, Any]], None, None]:
      """Yields examples from one file."""
      counter = 0
      key_prefix = os.path.basename(path)
      # Dataset of tf.Examples containing full episodes.
      example_ds = tf.data.TFRecordDataset(filenames=str(path))
      # Dataset of episodes, each represented as a dataset of steps.
      episode_ds = example_ds.map(
          functools.partial(
              self.tf_example_to_step_ds,
              feature_description=feature_description),
          num_parallel_calls=tf.data.experimental.AUTOTUNE)
      episode_ds = tfds.as_numpy(episode_ds)
      for e in episode_ds:
        episode_id = counter
        yield f'{key_prefix}/{episode_id}', e
        counter += 1

    return beam.Create(file_paths) | beam.FlatMap(_generate_examples_one_file)
