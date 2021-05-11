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

"""Builder Configs for Mujoco Datasets."""

from typing import Any, Dict

import dataclasses
import tensorflow.compat.v2 as tf
from tensorflow_datasets.d4rl import dataset_utils
import tensorflow_datasets.public_api as tfds


@dataclasses.dataclass
class BuilderConfig(tfds.core.BuilderConfig):
  dataset_dir: str = 'gym_mujoco'
  file_suffix: str = 'medium'
  # All use float32 except for the replay datasets.
  float_type: tf.DType = tf.float32
  # All datasets have step metadata except for mujoco v0.
  has_step_metadata: bool = False
  has_episode_metadata: bool = False
  has_policy_metadata: bool = False


@dataclasses.dataclass
class DatasetConfig():
  """Configuration of the shape of the dataset.

  Attributes:
    name: name of the Mujoco task
    obs_len: first dimension of the obsercations.
    action_len: first dimension of the actions.
    qpos_len: first dimension of the infos/qpos field (ignored if the dataset
      does not include step metadata).
    qvel_len: first dimension of the infos/qvel field (ignored if the dataset
      does not include step metadata).
  """
  name: str
  obs_len: int
  action_len: int
  qpos_len: int
  qvel_len: int


# pytype: disable=wrong-keyword-args
BUILDER_CONFIGS = [
    BuilderConfig(
        name='v0-expert',
        dataset_dir='gym_mujoco',
        file_suffix='expert',
        float_type=tf.float32,
        has_step_metadata=False,
        has_episode_metadata=False,
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-medium',
        dataset_dir='gym_mujoco',
        file_suffix='medium',
        float_type=tf.float32,
        has_step_metadata=False,
        has_episode_metadata=False,
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-medium-expert',
        dataset_dir='gym_mujoco',
        file_suffix='medium_expert',
        float_type=tf.float32,
        has_step_metadata=False,
        has_episode_metadata=False,
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-mixed',
        dataset_dir='gym_mujoco',
        file_suffix='mixed',
        float_type=tf.float32,
        has_step_metadata=False,
        has_episode_metadata=False,
        has_policy_metadata=False),
    BuilderConfig(
        name='v0-random',
        dataset_dir='gym_mujoco',
        file_suffix='random',
        float_type=tf.float32,
        has_step_metadata=False,
        has_episode_metadata=False,
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-expert',
        dataset_dir='gym_mujoco_v1',
        file_suffix='expert-v1',
        float_type=tf.float32,
        has_step_metadata=True,
        has_episode_metadata=True,
        has_policy_metadata=True),
    BuilderConfig(
        name='v1-medium',
        dataset_dir='gym_mujoco_v1',
        file_suffix='medium-v1',
        float_type=tf.float32,
        has_step_metadata=True,
        has_episode_metadata=True,
        has_policy_metadata=True),
    BuilderConfig(
        name='v1-medium-expert',
        dataset_dir='gym_mujoco_v1',
        file_suffix='medium_expert-v1',
        float_type=tf.float32,
        has_step_metadata=True,
        has_episode_metadata=False,
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-medium-replay',
        dataset_dir='gym_mujoco_v1',
        file_suffix='medium_replay-v1',
        float_type=tf.float64,
        has_step_metadata=True,
        has_episode_metadata=True,
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-full-replay',
        dataset_dir='gym_mujoco_v1',
        file_suffix='full_replay-v1',
        float_type=tf.float64,
        has_step_metadata=True,
        has_episode_metadata=True,
        has_policy_metadata=False),
    BuilderConfig(
        name='v1-random',
        dataset_dir='gym_mujoco_v1',
        file_suffix='random-v1',
        float_type=tf.float32,
        has_step_metadata=True,
        has_episode_metadata=False,
        has_policy_metadata=False),
    BuilderConfig(
        name='v2-expert',
        dataset_dir='gym_mujoco_v2',
        file_suffix='expert-v2',
        float_type=tf.float32,
        has_step_metadata=True,
        has_episode_metadata=True,
        has_policy_metadata=True),
    BuilderConfig(
        name='v2-full-replay',
        dataset_dir='gym_mujoco_v2',
        file_suffix='full_replay-v2',
        float_type=tf.float64,
        has_step_metadata=True,
        has_episode_metadata=True,
        has_policy_metadata=False),
    BuilderConfig(
        name='v2-medium',
        dataset_dir='gym_mujoco_v2',
        file_suffix='medium-v2',
        float_type=tf.float32,
        has_step_metadata=True,
        has_episode_metadata=True,
        has_policy_metadata=True),
    BuilderConfig(
        name='v2-medium-expert',
        dataset_dir='gym_mujoco_v2',
        file_suffix='medium_expert-v2',
        float_type=tf.float32,
        has_step_metadata=True,
        has_episode_metadata=False,
        has_policy_metadata=False),
    BuilderConfig(
        name='v2-medium-replay',
        dataset_dir='gym_mujoco_v2',
        file_suffix='medium_replay-v2',
        float_type=tf.float64,
        has_step_metadata=True,
        has_episode_metadata=True,
        has_policy_metadata=False),
    BuilderConfig(
        name='v2-random',
        dataset_dir='gym_mujoco_v2',
        file_suffix='random-v2',
        float_type=tf.float32,
        has_step_metadata=True,
        has_episode_metadata=False,
        has_policy_metadata=False),
]


def get_mujoco_features_dict(
    builder_config: BuilderConfig,
    ds_config: DatasetConfig) -> Dict[str, tfds.features.FeatureConnector]:
  """Builds the features dict of a Mujoco dataset.

  Args:
    builder_config: builder config of the Mujoco dataset.
    ds_config: config of the Mujoco dataset containing the specs.

  Returns:
    Dictionary with the features of this dataset.
  """

  float_type = builder_config.float_type

  steps_dict = {
      'observation':
          tfds.features.Tensor(shape=(ds_config.obs_len,), dtype=float_type),
      'action':
          tfds.features.Tensor(shape=(ds_config.action_len,), dtype=float_type),
      'reward':
          float_type,
      'is_terminal':
          tf.bool,
      'is_first':
          tf.bool,
      'discount':
          float_type,
  }
  if builder_config.has_step_metadata:
    steps_dict['infos'] = {
        # Infos correspond to state information.
        # See https://github.com/rail-berkeley/d4rl/wiki/Tasks#gym.
        'action_log_probs':
            float_type,
        'qpos':
            tfds.features.Tensor(shape=(ds_config.qpos_len,), dtype=float_type),
        'qvel':
            tfds.features.Tensor(shape=(ds_config.qvel_len,), dtype=float_type),
    }

  episode_metadata = {}
  if builder_config.has_episode_metadata:
    episode_metadata.update({
        'algorithm': tf.string,
        'iteration': tf.int32,
    })
  if builder_config.has_policy_metadata:
    episode_metadata.update({
        # The policy dictionary contains the weights of the policy used to
        # generate the dataset.
        # See https://github.com/rail-berkeley/d4rl/wiki/Tasks#gym.
        'policy': {
            'fc0': {
                'bias':
                    tfds.features.Tensor(shape=(256,), dtype=float_type),
                'weight':
                    tfds.features.Tensor(
                        shape=(256, ds_config.obs_len), dtype=float_type),
            },
            'fc1': {
                'bias':
                    tfds.features.Tensor(shape=(256,), dtype=float_type),
                'weight':
                    tfds.features.Tensor(shape=(256, 256), dtype=float_type),
            },
            'last_fc': {
                'bias':
                    tfds.features.Tensor(
                        shape=(ds_config.action_len,), dtype=float_type),
                'weight':
                    tfds.features.Tensor(
                        shape=(ds_config.action_len, 256), dtype=float_type),
            },
            'last_fc_log_std': {
                'bias':
                    tfds.features.Tensor(
                        shape=(ds_config.action_len,), dtype=float_type),
                'weight':
                    tfds.features.Tensor(
                        shape=(ds_config.action_len, 256), dtype=float_type),
            },
            'nonlinearity': tf.string,
            'output_distribution': tf.string,
        },
    })

  features_dict = {
      'steps': tfds.features.Dataset(steps_dict),
  }
  if episode_metadata:
    features_dict.update(episode_metadata)

  return features_dict


class D4RLMujocoDatasetBuilder(
    tfds.core.GeneratorBasedBuilder, skip_registration=True):
  """DatasetBuilder for D4RL Mujoco."""

  def __init__(self, *, ds_config: DatasetConfig, **kwargs: Any):
    self._ds_config = ds_config
    super().__init__(**kwargs)

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    features_dict = get_mujoco_features_dict(
        builder_config=self.builder_config, ds_config=self._ds_config)
    return tfds.core.DatasetInfo(
        builder=self,
        description=dataset_utils.description(),
        features=tfds.features.FeaturesDict(features_dict),
        supervised_keys=None,  # disabled
        homepage=dataset_utils.url(),
        citation=dataset_utils.citation(),
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    ds_dir = self.builder_config.dataset_dir
    name = self._ds_config.name
    if name == 'walker2d' and self.builder_config.name == 'v0-mixed':
      # There is a mismatch in the name of the original files, where one of them
      # uses walker instead of walker2d.
      name = 'walker'
    ds_name = (name + '_' + self.builder_config.file_suffix + '.hdf5')
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
