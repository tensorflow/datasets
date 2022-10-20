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

"""rlu_control_suite dataset."""

from __future__ import annotations

import dataclasses
from typing import Any, Dict, Optional

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import rlu_common

_CONTROL_SUITE_DESCRIPTION = """
DeepMind Control Suite [Tassa et al., 2018](https://arxiv.org/abs/1801.00690)
is a set of control tasks implemented in MuJoCo
[Todorov et al., 2012](https://homes.cs.washington.edu/~todorov/papers/TodorovIROS12.pdf).
We consider a subset of the tasks provided in the suite that cover a wide range
of difficulties.

Most of the datasets in this domain are generated using D4PG. For the
environments Manipulator insert ball and Manipulator insert peg we use V-MPO
[Song et al., 2020](https://arxiv.org/abs/1909.12238) to generate the data as
D4PG is unable to solve these tasks. We release datasets for 9 control suite
tasks. For details on how the dataset was generated, please refer to the paper.

DeepMind Control Suite is a traditional continuous action RL benchmark.
In particular, we recommend you test your approach in DeepMind Control Suite if
you are interested in comparing against other state of the art offline RL
methods.
"""

_CITATION = """
@inproceedings{gulcehre2020rl,
 title = {RL Unplugged: A Suite of Benchmarks for Offline Reinforcement Learning},
 author = {Gulcehre, Caglar and Wang, Ziyu and Novikov, Alexander and Paine, Thomas and G\'{o}mez, Sergio and Zolna, Konrad and Agarwal, Rishabh and Merel, Josh S and Mankowitz, Daniel J and Paduraru, Cosmin and Dulac-Arnold, Gabriel and Li, Jerry and Norouzi, Mohammad and Hoffman, Matthew and Heess, Nicolas and de Freitas, Nando},
 booktitle = {Advances in Neural Information Processing Systems},
 pages = {7248--7259},
 volume = {33},
 year = {2020}
}
"""


@dataclasses.dataclass
class ControlSuiteBuilderConfig(tfds.core.BuilderConfig):
  observation_size: Optional[Dict[str, int]] = None
  action_size: int = 0


# pytype: disable=wrong-keyword-args
_BUILDER_CONFIGS = [
    ControlSuiteBuilderConfig(
        name='cartpole_swingup',
        observation_size={
            'position': 3,
            'velocity': 2
        },
        action_size=1),
    ControlSuiteBuilderConfig(
        name='cheetah_run',
        observation_size={
            'position': 8,
            'velocity': 9
        },
        action_size=6),
    ControlSuiteBuilderConfig(
        name='finger_turn_hard',
        observation_size={
            'position': 4,
            'velocity': 3,
            'target_position': 2,
            'dist_to_target': 1
        },
        action_size=2),
    ControlSuiteBuilderConfig(
        name='fish_swim',
        observation_size={
            'target': 3,
            'velocity': 13,
            'upright': 1,
            'joint_angles': 7
        },
        action_size=5),
    ControlSuiteBuilderConfig(
        name='humanoid_run',
        observation_size={
            'velocity': 27,
            'com_velocity': 3,
            'torso_vertical': 3,
            'extremities': 12,
            'head_height': 1,
            'joint_angles': 21
        },
        action_size=21),
    ControlSuiteBuilderConfig(
        name='manipulator_insert_ball',
        observation_size={
            'arm_pos': 16,
            'arm_vel': 8,
            'touch': 5,
            'hand_pos': 4,
            'object_pos': 4,
            'object_vel': 3,
            'target_pos': 4,
        },
        action_size=5),
    ControlSuiteBuilderConfig(
        name='manipulator_insert_peg',
        observation_size={
            'arm_pos': 16,
            'arm_vel': 8,
            'touch': 5,
            'hand_pos': 4,
            'object_pos': 4,
            'object_vel': 3,
            'target_pos': 4,
        },
        action_size=5),
    ControlSuiteBuilderConfig(
        name='walker_stand',
        observation_size={
            'orientations': 14,
            'velocity': 9,
            'height': 1,
        },
        action_size=6),
    ControlSuiteBuilderConfig(
        name='walker_walk',
        observation_size={
            'orientations': 14,
            'velocity': 9,
            'height': 1,
        },
        action_size=6)
]
# pytype: enable=wrong-keyword-args


def _sequence_feature(
    size: Optional[int] = None) -> tf.io.FixedLenSequenceFeature:
  if size:
    shape = [size]
  else:
    shape = []
  return tf.io.FixedLenSequenceFeature(
      shape, dtype=tf.float32, allow_missing=True)


class RluControlSuite(rlu_common.RLUBuilder):
  """DatasetBuilder for rlu_control_suite dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  BUILDER_CONFIGS = _BUILDER_CONFIGS

  _SHARDS = 100
  _INPUT_FILE_PREFIX = 'gs://rl_unplugged/dm_control_suite_episodes/'

  def get_features_dict(self):
    return tfds.features.FeaturesDict({
        'steps':
            tfds.features.Dataset({
                'observation': {
                    k: rlu_common.float_tensor_feature(v)
                    for k, v in self.builder_config.observation_size.items()
                },
                'action':
                    tfds.features.Tensor(
                        shape=(self.builder_config.action_size,),
                        dtype=tf.float32),
                'reward':
                    tf.float32,
                'is_terminal':
                    tf.bool,
                'is_first':
                    tf.bool,
                'is_last':
                    tf.bool,
                'discount':
                    tf.float32,
            }),
        'episode_id':
            tf.int64,
        'timestamp':
            tf.int64
    })

  def get_description(self):
    return _CONTROL_SUITE_DESCRIPTION

  def get_citation(self):
    return _CITATION

  def get_file_prefix(self):
    task = self.builder_config.name
    return f'{self._INPUT_FILE_PREFIX}/{task}/train'

  def num_shards(self):
    return self._SHARDS

  def _get_example_specs(self):
    obs_features = {
        f'observation/{k}': _sequence_feature(v)
        for k, v in self.builder_config.observation_size.items()
    }
    return {
        **obs_features,
        'action':
            _sequence_feature(self.builder_config.action_size),
        'discount':
            _sequence_feature(),
        'reward':
            _sequence_feature(),
        'step_type':
            _sequence_feature(),
        'episode_id':
            tf.io.FixedLenFeature([], tf.int64),
        'timestamp':
            tf.io.FixedLenFeature([], tf.int64),
    }

  def tf_example_to_step_ds(self,
                            tf_example: tf.train.Example) -> Dict[str, Any]:
    feature_description = self._get_example_specs()

    data = tf.io.parse_single_example(tf_example, feature_description)
    episode_length = tf.size(data['discount'])
    is_first = tf.concat([[True], [False] * tf.ones(episode_length - 1)],
                         axis=0)
    is_last = tf.concat([[False] * tf.ones(episode_length - 1), [True]], axis=0)
    is_terminal = [False] * tf.ones(episode_length, tf.int64)

    # The data is in RSA alignment, we realign it to SAR to comply with the
    # RLDS standard.
    discount = data['discount'][1:]
    if discount[-1] == 0.:
      is_terminal = tf.concat(
          [[False] * tf.ones(episode_length - 1, tf.int64), [True]], axis=0)
      # If the episode ends in a terminal state, in the last step only the
      # observation has valid information (the terminal state).
      discount = tf.concat([discount, [0.]], axis=0)
    else:
      discount = tf.concat([discount, [1.]], axis=0)

    reward = tf.concat([data['reward'][1:], [0.]], axis=0)

    obs_prefix = 'observation/'
    obs = {}
    for k in feature_description:
      if k.startswith(obs_prefix):
        new_k = k[len(obs_prefix):]
        obs[new_k] = data[k]
    episode = {
        'steps': {
            'observation': obs,
            'action': data['action'],
            'reward': reward,
            'discount': discount,
            'is_first': is_first,
            'is_last': is_last,
            'is_terminal': is_terminal
        },
        'episode_id': data['episode_id'],
        'timestamp': data['timestamp']
    }
    return episode
