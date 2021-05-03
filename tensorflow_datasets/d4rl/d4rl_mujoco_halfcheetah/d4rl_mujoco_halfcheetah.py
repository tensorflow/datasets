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

"""D4Rl Halfcheetah dataset from Mujoco."""

import dataclasses
import tensorflow.compat.v2 as tf
from tensorflow_datasets.d4rl import dataset_utils
import tensorflow_datasets.public_api as tfds

_DESCRIPTION = """
D4RL is an open-source benchmark for offline reinforcement learning. It provides
standardized environments and datasets for training and benchmarking algorithms.
"""

_CITATION = """\
@misc{fu2020d4rl,
    title={D4RL: Datasets for Deep Data-Driven Reinforcement Learning},
    author={Justin Fu and Aviral Kumar and Ofir Nachum and George Tucker and Sergey Levine},
    year={2020},
    eprint={2004.07219},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
"""


@dataclasses.dataclass
class DatasetConfig(tfds.core.BuilderConfig):
  dataset_dir: str = 'gym_mujoco'
  file_suffix: str = 'medium'


class D4rlMujocoHalfcheetah(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for halfcheetah dataset."""

  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.0':
          'Initial release.',
      '1.0.1':
          'Support for episode and step metadata, and unification of the' +
          ' reward shape accross all the configs.'
  }

  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [
      DatasetConfig(
          name='v0-expert',
          dataset_dir='gym_mujoco',
          file_suffix='expert'),
      DatasetConfig(
          name='v0-medium',
          dataset_dir='gym_mujoco',
          file_suffix='medium'),
      DatasetConfig(
          name='v0-medium-expert',
          dataset_dir='gym_mujoco',
          file_suffix='medium_expert'),
      DatasetConfig(
          name='v0-mixed',
          dataset_dir='gym_mujoco',
          file_suffix='mixed'),
      DatasetConfig(
          name='v0-random',
          dataset_dir='gym_mujoco',
          file_suffix='random'),
      DatasetConfig(
          name='v1-expert',
          dataset_dir='gym_mujoco_v1',
          file_suffix='expert-v1'),
      DatasetConfig(
          name='v1-medium',
          dataset_dir='gym_mujoco_v1',
          file_suffix='medium-v1'),
      DatasetConfig(
          name='v1-medium-expert',
          dataset_dir='gym_mujoco_v1',
          file_suffix='medium_expert-v1'),
      DatasetConfig(
          name='v1-medium-replay',
          dataset_dir='gym_mujoco_v1',
          file_suffix='medium_replay-v1'),
      DatasetConfig(
          name='v1-full-replay',
          dataset_dir='gym_mujoco_v1',
          file_suffix='full_replay-v1'),
      DatasetConfig(
          name='v1-random',
          dataset_dir='gym_mujoco_v1',
          file_suffix='random-v1'),
      DatasetConfig(
          name='v2-expert',
          dataset_dir='gym_mujoco_v2',
          file_suffix='expert-v2'),
      DatasetConfig(
          name='v2-full-replay',
          dataset_dir='gym_mujoco_v2',
          file_suffix='full_replay-v2'),
      DatasetConfig(
          name='v2-medium',
          dataset_dir='gym_mujoco_v2',
          file_suffix='medium-v2'),
      DatasetConfig(
          name='v2-medium-expert',
          dataset_dir='gym_mujoco_v2',
          file_suffix='medium_expert-v2'),
      DatasetConfig(
          name='v2-medium-replay',
          dataset_dir='gym_mujoco_v2',
          file_suffix='medium_replay-v2'),
      DatasetConfig(
          name='v2-random',
          dataset_dir='gym_mujoco_v2',
          file_suffix='random-v2'),
  ]
  # pytype: enable=wrong-keyword-args

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    replay_datasets = {
        'v1-medium-replay', 'v1-full-replay', 'v2-medium-replay',
        'v2-full-replay'
    }
    full_metadata_datasets = {
        'v1-expert', 'v2-expert', 'v1-medium', 'v2-medium'
    }
    float_type = tf.float32
    if self.builder_config.name in replay_datasets:
      float_type = tf.float64

    steps_dict = {
        'observation': tfds.features.Tensor(shape=(17,), dtype=float_type),
        'action': tfds.features.Tensor(shape=(6,), dtype=float_type),
        'reward': float_type,
        'is_terminal': tf.bool,
        'is_first': tf.bool,
        'discount': float_type,
    }
    # All except for v0 contain step metadata
    if self.builder_config.dataset_dir != 'gym_mujoco':
      steps_dict['infos'] = {
          # Infos correspond to state information.
          # See https://github.com/rail-berkeley/d4rl/wiki/Tasks#gym.
          'action_log_probs': float_type,
          'qpos': tfds.features.Tensor(shape=(9,), dtype=float_type),
          'qvel': tfds.features.Tensor(shape=(9,), dtype=float_type),
      }
    # Episode metadata
    episode_metadata = {}
    # Replay datasets contain only two fields of the metadata.
    if self.builder_config.name in replay_datasets:
      episode_metadata = {
          'algorithm': tf.string,
          'iteration': tf.int32,
      }
    if self.builder_config.name in full_metadata_datasets:
      episode_metadata = {
          'algorithm': tf.string,
          'iteration': tf.int32,
          # The policy dictionary contains the weights of the policy used to
          # generate the dataset.
          # See https://github.com/rail-berkeley/d4rl/wiki/Tasks#gym.
          'policy': {
              'fc0': {
                  'bias':
                      tfds.features.Tensor(shape=(256,), dtype=float_type),
                  'weight':
                      tfds.features.Tensor(shape=(256, 17), dtype=float_type),
              },
              'fc1': {
                  'bias':
                      tfds.features.Tensor(shape=(256,), dtype=float_type),
                  'weight':
                      tfds.features.Tensor(shape=(256, 256), dtype=float_type),
              },
              'last_fc': {
                  'bias':
                      tfds.features.Tensor(shape=(6,), dtype=float_type),
                  'weight':
                      tfds.features.Tensor(shape=(6, 256), dtype=float_type),
              },
              'last_fc_log_std': {
                  'bias':
                      tfds.features.Tensor(shape=(6,), dtype=float_type),
                  'weight':
                      tfds.features.Tensor(shape=(6, 256), dtype=float_type),
              },
              'nonlinearity': tf.string,
              'output_distribution': tf.string,
          },
      }

    features_dict = {
        'steps': tfds.features.Dataset(steps_dict),
    }
    if episode_metadata:
      features_dict.update(episode_metadata)

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,  # disabled
        homepage='https://sites.google.com/view/d4rl/home',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    ds_dir = self.builder_config.dataset_dir
    ds_name = 'halfcheetah_'+self.builder_config.file_suffix + '.hdf5'
    path = dl_manager.download_and_extract({
        'file_path':
            'http://rail.eecs.berkeley.edu/datasets/offline_rl/' + ds_dir +
            '/' + ds_name
    })
    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    file_path = path['file_path']
    return dataset_utils.generate_examples(file_path)
