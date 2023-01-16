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

"""rlu_locomotion dataset."""

from __future__ import annotations

from typing import Any, Dict, Optional

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import rlu_common

_LOCOMOTION_DESCRIPTION = """
These tasks are made up of the corridor locomotion tasks involving the CMU
Humanoid, for which prior efforts have either used motion capture data
[Merel et al., 2019a](https://arxiv.org/abs/1811.09656),
[Merel et al., 2019b](https://arxiv.org/abs/1811.11711) or training from scratch
[Song et al., 2020](https://arxiv.org/abs/1909.12238). In addition, the DM
Locomotion repository contains a set of tasks adapted to be suited to a virtual
rodent [Merel et al., 2020](https://arxiv.org/abs/1911.09451). We emphasize that
the DM Locomotion tasks feature the combination of challenging high-DoF
continuous control along with perception from rich egocentric observations.
For details on how the dataset was generated, please refer to the paper.

We recommend you to try offline RL methods on DeepMind Locomotion dataset, if
you are interested in very challenging offline RL dataset with continuous action
space.
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

_TASK_NAMES = [
    'humanoid_corridor',
    'humanoid_gaps',
    'humanoid_walls',
    'rodent_bowl_escape',
    'rodent_gaps',
    'rodent_mazes',
    'rodent_two_touch',
]


def _sequence(
    shape_size: Optional[int] = None, dtype: Optional[tf.DType] = None
) -> tf.io.FixedLenSequenceFeature:
  if dtype is None:
    dtype = tf.float32
  if shape_size:
    shape = [shape_size]
  else:
    shape = []
  return tf.io.FixedLenSequenceFeature(shape, dtype, allow_missing=True)


def _feature_description(task_name: str) -> Dict[str, Any]:
  """Returns the shape of a tf.Example for the given task."""
  if 'humanoid' in task_name:
    return {
        'observation/walker/joints_vel': _sequence(56),
        'observation/walker/sensors_velocimeter': _sequence(3),
        'observation/walker/sensors_gyro': _sequence(3),
        'observation/walker/joints_pos': _sequence(56),
        'observation/walker/world_zaxis': _sequence(3),
        'observation/walker/body_height': _sequence(1),
        'observation/walker/sensors_accelerometer': _sequence(3),
        'observation/walker/end_effectors_pos': _sequence(12),
        'observation/walker/egocentric_camera': _sequence(
            shape_size=None, dtype=tf.string
        ),
        'action': _sequence(56),
        'discount': _sequence(),
        'reward': _sequence(),
        'step_type': _sequence(),
        'episode_id': tf.io.FixedLenFeature([], tf.int64),
        'timestamp': tf.io.FixedLenFeature([], tf.int64),
    }
  else:
    return {
        'observation/walker/joints_pos': _sequence(30),
        'observation/walker/joints_vel': _sequence(30),
        'observation/walker/tendons_pos': _sequence(8),
        'observation/walker/tendons_vel': _sequence(8),
        'observation/walker/appendages_pos': _sequence(15),
        'observation/walker/world_zaxis': _sequence(3),
        'observation/walker/sensors_accelerometer': _sequence(3),
        'observation/walker/sensors_velocimeter': _sequence(3),
        'observation/walker/sensors_gyro': _sequence(3),
        'observation/walker/sensors_touch': _sequence(4),
        'observation/walker/egocentric_camera': _sequence(
            shape_size=None, dtype=tf.string
        ),
        'action': _sequence(38),
        'discount': _sequence(),
        'reward': _sequence(),
        'step_type': _sequence(),
        'episode_id': tf.io.FixedLenFeature([], tf.int64),
        'timestamp': tf.io.FixedLenFeature([], tf.int64),
    }


class RluLocomotion(rlu_common.RLUBuilder):
  """DatasetBuilder for rlu_locomotion dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [tfds.core.BuilderConfig(name=name) for name in _TASK_NAMES]
  # pytype: enable=wrong-keyword-args

  _SHARDS = 100
  _INPUT_FILE_PREFIX = 'gs://rl_unplugged/dm_locomotion_episodes/'

  def get_features_dict(self):
    if 'humanoid' in self.builder_config.name:
      walker_features = {
          'joints_vel': rlu_common.float_tensor_feature(56),
          'sensors_velocimeter': rlu_common.float_tensor_feature(3),
          'sensors_gyro': rlu_common.float_tensor_feature(3),
          'joints_pos': rlu_common.float_tensor_feature(56),
          'world_zaxis': rlu_common.float_tensor_feature(3),
          'body_height': rlu_common.float_tensor_feature(1),
          'sensors_accelerometer': rlu_common.float_tensor_feature(3),
          'end_effectors_pos': rlu_common.float_tensor_feature(12),
          'egocentric_camera': tfds.features.Image(
              shape=(64, 64, 3), dtype=np.uint8, encoding_format='png'
          ),
      }
      action_features = tfds.features.Tensor(shape=(56,), dtype=np.float32)
    else:  # 'rodent' datasets
      walker_features = {
          'joints_pos': rlu_common.float_tensor_feature(30),
          'joints_vel': rlu_common.float_tensor_feature(30),
          'tendons_pos': rlu_common.float_tensor_feature(8),
          'tendons_vel': rlu_common.float_tensor_feature(8),
          'appendages_pos': rlu_common.float_tensor_feature(15),
          'world_zaxis': rlu_common.float_tensor_feature(3),
          'sensors_accelerometer': rlu_common.float_tensor_feature(3),
          'sensors_velocimeter': rlu_common.float_tensor_feature(3),
          'sensors_gyro': rlu_common.float_tensor_feature(3),
          'sensors_touch': rlu_common.float_tensor_feature(4),
          'egocentric_camera': tfds.features.Image(
              shape=(64, 64, 3), dtype=np.uint8, encoding_format='png'
          ),
      }
      action_features = tfds.features.Tensor(shape=(38,), dtype=np.float32)

    return tfds.features.FeaturesDict({
        'steps': tfds.features.Dataset({
            'observation': {
                'walker': walker_features,
            },
            'action': action_features,
            'reward': np.float32,
            'is_terminal': np.bool_,
            'is_first': np.bool_,
            'is_last': np.bool_,
            'discount': np.float32,
        }),
        'episode_id': np.int64,
        'timestamp': np.int64,
    })

  def get_description(self):
    return _LOCOMOTION_DESCRIPTION

  def get_citation(self):
    return _CITATION

  def get_file_prefix(self):
    task = self.builder_config.name
    return f'{self._INPUT_FILE_PREFIX}/{task}/train'

  def num_shards(self):
    return self._SHARDS

  def tf_example_to_step_ds(
      self, tf_example: tf.train.Example
  ) -> Dict[str, Any]:
    """Create an episode from a TF example."""
    feature_description = _feature_description(self.builder_config.name)

    data = tf.io.parse_single_example(tf_example, feature_description)
    episode_length = tf.size(data['discount'])
    is_first = tf.concat(
        [[True], [False] * tf.ones(episode_length - 1)], axis=0
    )
    is_last = tf.concat([[False] * tf.ones(episode_length - 1), [True]], axis=0)
    is_terminal = [False] * tf.ones(episode_length, tf.int64)

    # The data is in RSA alignment, we realign it to SAR to comply with the
    # RLDS standard.
    discount = data['discount'][1:]
    if discount[-1] == 0.0:
      is_terminal = tf.concat(
          [[False] * tf.ones(episode_length - 1, tf.int64), [True]], axis=0
      )
      # If the episode ends in a terminal state, in the last step only the
      # observation has valid information (the terminal state).
      discount = tf.concat([discount, [0.0]], axis=0)
    else:
      discount = tf.concat([discount, [1.0]], axis=0)

    reward = tf.concat([data['reward'][1:], [0.0]], axis=0)

    obs_prefix = 'observation/walker/'
    obs = {}
    for k in feature_description:
      if k.startswith(obs_prefix):
        new_k = k[len(obs_prefix) :]
        if 'egocentric_camera' in k:
          obs[new_k] = tf.reshape(
              tf.io.decode_raw(data[k], out_type=tf.uint8),
              (-1,)
              + (
                  64,
                  64,
                  3,
              ),
          )
        else:
          obs[new_k] = data[k]
    episode = {
        'steps': {
            'observation': {'walker': obs},
            'action': data['action'],
            'reward': reward,
            'discount': discount,
            'is_first': is_first,
            'is_last': is_last,
            'is_terminal': is_terminal,
        },
        'episode_id': data['episode_id'],
        'timestamp': data['timestamp'],
    }
    return episode
