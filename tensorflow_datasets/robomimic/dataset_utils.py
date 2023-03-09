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

"""Library functions for robomimic datasets."""

from typing import Any, Dict, List, Mapping

from etils import epath
import h5py
import numpy as np
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.robomimic import config
import tree



def _concat_obs(base_obs, extra_obs):
  return np.append(base_obs, np.expand_dims(extra_obs, 0), axis=0)


def episode_metadata(
    mask: Mapping[str, List[str]], episode_key: str
) -> Dict[str, bool]:
  """Builds the metadata of an episode.

  Args:
    mask: A dict that maps flags to the list of episodes for which this flag is
      true.
    episode_key: The key of an episode.

  Returns:
    Dictionary that maps the flags to the value corresponding to the given
    episode.
  """
  metadata = {}
  for k in mask:
    metadata[k] = episode_key in mask[k]
  return metadata


def build_episode(steps: Mapping[str, Any]) -> Dict[str, Any]:
  """Builds a full episode dict.

  Args:
    steps: A dict with each key corresponding to an episode of that variable.

  Returns:
   A dict with data specific to one episode.
  """

  # This is the base episode length without the end step, that step will get
  # added manually.  `[:]` notation is necessary to extract data from the hdf5
  # object.
  ep_length = steps['actions'][:].shape[0]
  episode = {}
  episode['is_first'] = np.append(True, np.zeros(ep_length, dtype=bool))

  # The standard 'obs' needs to be extended with the last element from
  # 'next_obs' to reconstruct the full sequence.
  obs = tree.map_structure(np.array, dict(steps['obs']))
  last_obs = tree.map_structure(
      lambda el: el[-1], dict(steps['next_obs'])
  )
  concat_obs = tree.map_structure(_concat_obs, obs, last_obs)

  actions = steps['actions'][:]
  dones = steps['dones'][:]
  episode['observation'] = concat_obs
  episode['action'] = np.append(
      actions, np.expand_dims(np.zeros(actions[0].shape), 0), axis=0
  )
  episode['reward'] = np.append(steps['rewards'][:], 0)
  episode['discount'] = np.append(np.ones(ep_length), 0)
  # Offset `dones` by one as it corresponds to the `next_obs`:
  # "done signal, equal to 1 if playing the corresponding action in the state
  # should terminate the episode".  Since playing another action may not end the
  # episode, it is actually representing whether the following state is
  # the terminal state.
  episode['is_terminal'] = np.append(False, dones).astype(bool)
  episode['is_last'] = np.append(np.zeros(ep_length, dtype=bool), True)
  states = steps['states'][:]
  episode['states'] = np.append(
      states, np.expand_dims(np.zeros(states[0].shape), 0), axis=0
  )

  return episode


def tensor_feature(size: int) -> tfds.features.Tensor:
  return tfds.features.Tensor(
      shape=(size,), dtype=np.float64, encoding=tfds.features.Encoding.ZLIB
  )


def image_feature(size: int) -> tfds.features.Image:
  return tfds.features.Image(
      shape=(size, size, 3), dtype=np.uint8, encoding_format='png'
  )


class RobomimicBuilder(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for robomimic datasets."""

  VERSION: tfds.core.Version
  RELEASE_NOTES: Dict[str, str]
  BUILDER_CONFIGS: List[tfds.core.BuilderConfig]
  DATASET_NAME: str
  DATASET_FILE_EXTENSION: str = ''


  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return self.dataset_info_from_configs(
        features=self._get_features(),
        supervised_keys=None,
        homepage='https://arise-initiative.github.io/robomimic-web/',
    )

  def _get_features(self) -> tfds.features.FeaturesDict:
    obs_dim = config.TASKS[self.builder_config.task]['object']
    states_dim = config.TASKS[self.builder_config.task]['states']
    action_size = config.TASKS[self.builder_config.task]['action_size']

    observation = {
        'object': tensor_feature(
            obs_dim,
        ),
        'robot0_eef_pos': tensor_feature(3),
        'robot0_eef_quat': tensor_feature(4),
        'robot0_eef_vel_ang': tensor_feature(3),
        'robot0_eef_vel_lin': tensor_feature(3),
        'robot0_gripper_qpos': tensor_feature(2),
        'robot0_gripper_qvel': tensor_feature(2),
        'robot0_joint_pos': tensor_feature(7),
        'robot0_joint_pos_cos': tensor_feature(7),
        'robot0_joint_pos_sin': tensor_feature(7),
        'robot0_joint_vel': tensor_feature(7),
    }
    if self.builder_config.task == config.Task.TRANSPORT:
      observation['robot1_eef_pos'] = tensor_feature(3)
      observation['robot1_eef_quat'] = tensor_feature(4)
      observation['robot1_eef_vel_ang'] = tensor_feature(3)
      observation['robot1_eef_vel_lin'] = tensor_feature(3)
      observation['robot1_gripper_qpos'] = tensor_feature(2)
      observation['robot1_gripper_qvel'] = tensor_feature(2)
      observation['robot1_joint_pos'] = tensor_feature(7)
      observation['robot1_joint_pos_cos'] = tensor_feature(7)
      observation['robot1_joint_pos_sin'] = tensor_feature(7)
      observation['robot1_joint_vel'] = tensor_feature(7)

    if self.builder_config.filename == config.DataType.IMAGE:
      if self.builder_config.task == config.Task.TOOL_HANG:
        observation['robot0_eye_in_hand_image'] = image_feature(240)
        observation['sideview_image'] = image_feature(240)
      elif self.builder_config.task == config.Task.TRANSPORT:
        observation['robot0_eye_in_hand_image'] = image_feature(84)
        observation['robot1_eye_in_hand_image'] = image_feature(84)
        observation['shouldercamera0_image'] = image_feature(84)
        observation['shouldercamera1_image'] = image_feature(84)
      else:
        observation['agentview_image'] = image_feature(84)
        observation['robot0_eye_in_hand_image'] = image_feature(84)

    # metadata depends on the quality type
    metadata = self._get_metadata()

    features = tfds.features.FeaturesDict({
        'horizon': np.int32,
        'episode_id': np.str_,
        'steps': tfds.features.Dataset({
            'action': tensor_feature(action_size),
            'observation': observation,
            'reward': np.float64,
            'is_first': np.bool_,
            'is_last': np.bool_,
            'is_terminal': np.bool_,
            'discount': np.int32,
            'states': tensor_feature(states_dim),
        }),
        **metadata,
    })
    return features

  def _get_metadata(self) -> Dict[Any, Any]:
    return {}

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # Machine generated datasets have an additional variant as they are trained
    # using dense rather than sparse rewards. We currently are only interested
    # in the sparse rewards, for consistency with the other datasets.
    ext = self.DATASET_FILE_EXTENSION
    filepath = (
        'http://downloads.cs.stanford.edu/downloads/rt_benchmark/'
        f'{self.builder_config.task}/{self.builder_config.dataset}/'
        f'{self.builder_config.filename}{ext}.hdf5'
    )
    path = dl_manager.download_and_extract({'file_path': filepath})
    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    path = epath.Path(path['file_path'])
    with path.open('rb') as f:
      with h5py.File(f, 'r') as dataset_file:
        data = dataset_file['data']
        if 'mask' in dataset_file.keys():
          mask = dataset_file['mask']
          string_mask = {}
          for k in mask:
            string_mask[k] = []
            for element in mask[k]:
              string_mask[k].append(element.decode('UTF-8'))
          mask = string_mask
          for key in data:
            yield key, {
                'steps': build_episode(data[key]),
                'horizon': self.builder_config.horizon,
                'episode_id': key,
                **episode_metadata(mask, key),
            }
        else:
          for key in data:
            yield key, {
                'steps': build_episode(data[key]),
                'horizon': self.builder_config.horizon,
                'episode_id': key,
            }
