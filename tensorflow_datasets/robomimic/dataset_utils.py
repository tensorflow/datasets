# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Library functions and types for the robomimic datasets."""

import dataclasses
import enum
from typing import Any, Dict, List, Mapping

from etils import epath
import h5py
import numpy as np
import tensorflow_datasets.public_api as tfds
import tree



class Task(enum.Enum):
  LIFT = 'lift'
  CAN = 'can'
  SQUARE = 'square'
  TRANSPORT = 'transport'
  TOOL_HANG = 'tool_hang'

  def __str__(self) -> str:
    return self.value


class DataSource(enum.Enum):
  PH = 'ph'  # proficient human, i.e. expert demonstrations
  MH = 'mh'  # mixed-human, i.e. more suboptimal than proficient human
  MG = 'mg'  # machine generated, i.e. soft actor critic with dense reward

  def __str__(self) -> str:
    return self.value


class ObservationType(enum.Enum):
  IMAGE = 'image'  # image-based observations (i.e. exteroception)
  LOW_DIM = 'low_dim'  # internal state-based observations (i.e. proprioception)

  def __str__(self) -> str:
    return self.value


@dataclasses.dataclass
class BuilderConfig(tfds.core.BuilderConfig):
  """Configuration of the dataset versions."""

  task: Task = Task.LIFT
  dataset: DataSource = DataSource.PH
  filename: ObservationType = ObservationType.LOW_DIM
  horizon: int = 100


TASKS = {
    Task.LIFT: {
        'datasets': [DataSource.PH, DataSource.MH, DataSource.MG],
        'object': 10,
        'states': 32,
        'horizon': 400,
        'action_size': 7,
    },
    Task.CAN: {
        'datasets': [DataSource.PH, DataSource.MH, DataSource.MG],
        'object': 14,
        'states': 71,
        'horizon': 400,
        'action_size': 7,
    },
    Task.SQUARE: {
        'datasets': [DataSource.PH, DataSource.MH],
        'object': 14,
        'states': 45,
        'horizon': 400,
        'action_size': 7,
    },
    Task.TRANSPORT: {
        'datasets': [DataSource.PH, DataSource.MH],
        'object': 41,
        'states': 115,
        'horizon': 700,
        'action_size': 14,
    },
    Task.TOOL_HANG: {
        'datasets': [
            DataSource.PH,
        ],
        'object': 44,
        'states': 58,
        'horizon': 700,
        'action_size': 7,
    },
}


def make_builder_configs(dataset: DataSource):
  """Creates the PH build configs."""
  configs = []
  for task, details in TASKS.items():
    if dataset in details['datasets']:
      for observation_type in [ObservationType.IMAGE, ObservationType.LOW_DIM]:
        # pytype: disable=wrong-keyword-args
        configs.append(
            # name is inherited from base dataclass unbeknownst to the linter
            BuilderConfig(  # pylint: disable=unexpected-keyword-arg
                name=f'{task}_{dataset}_{observation_type}',
                task=task,
                dataset=dataset,
                filename=observation_type,
                horizon=details['horizon'],
            )
        )
        # pytype: enable=wrong-keyword-args
  return configs


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
  last_obs = tree.map_structure(lambda el: el[-1], dict(steps['next_obs']))
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


def tensor_feature(size: int, doc=None) -> tfds.features.Tensor:
  return tfds.features.Tensor(
      shape=(size,),
      dtype=np.float64,
      encoding=tfds.features.Encoding.ZLIB,
      doc=doc,
  )


def image_feature(size: int, doc=None) -> tfds.features.Image:
  return tfds.features.Image(
      shape=(size, size, 3), dtype=np.uint8, encoding_format='png', doc=doc
  )


class RobomimicBuilder(tfds.core.GeneratorBasedBuilder, skip_registration=True):
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
    obs_dim = TASKS[self.builder_config.task]['object']
    states_dim = TASKS[self.builder_config.task]['states']
    action_size = TASKS[self.builder_config.task]['action_size']

    observation = {
        'object': tensor_feature(
            obs_dim,
        ),
        'robot0_eef_pos': tensor_feature(3, doc='End-effector position'),
        'robot0_eef_quat': tensor_feature(4, doc='End-effector orientation'),
        'robot0_eef_vel_ang': tensor_feature(
            3, doc='End-effector angular velocity'
        ),
        'robot0_eef_vel_lin': tensor_feature(
            3, doc='End-effector cartesian velocity'
        ),
        'robot0_gripper_qpos': tensor_feature(2, doc='Gripper position'),
        'robot0_gripper_qvel': tensor_feature(2, doc='Gripper velocity'),
        'robot0_joint_pos': tensor_feature(7, doc='7DOF joint positions'),
        'robot0_joint_pos_cos': tensor_feature(7),
        'robot0_joint_pos_sin': tensor_feature(7),
        'robot0_joint_vel': tensor_feature(7, doc='7DOF joint velocities'),
    }
    if self.builder_config.task == Task.TRANSPORT:
      observation['robot1_eef_pos'] = tensor_feature(
          3, doc='End-effector position'
      )
      observation['robot1_eef_quat'] = tensor_feature(
          4, doc='End-effector orientation'
      )
      observation['robot1_eef_vel_ang'] = tensor_feature(
          3, doc='End-effector angular velocity'
      )
      observation['robot1_eef_vel_lin'] = tensor_feature(
          3, doc='End-effector cartesian velocity'
      )
      observation['robot1_gripper_qpos'] = tensor_feature(
          2, doc='Gripper position'
      )
      observation['robot1_gripper_qvel'] = tensor_feature(
          2, doc='Gripper velocity'
      )
      observation['robot1_joint_pos'] = tensor_feature(
          7, doc='7DOF joint positions'
      )
      observation['robot1_joint_pos_cos'] = tensor_feature(7)
      observation['robot1_joint_pos_sin'] = tensor_feature(7)
      observation['robot1_joint_vel'] = tensor_feature(
          7, doc='7DOF joint velocities'
      )

    if self.builder_config.filename == ObservationType.IMAGE:
      if self.builder_config.task == Task.TOOL_HANG:
        observation['robot0_eye_in_hand_image'] = image_feature(240)
        observation['sideview_image'] = image_feature(240)
      elif self.builder_config.task == Task.TRANSPORT:
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
