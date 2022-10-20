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

"""robomimic_ph dataset."""

from __future__ import annotations

import dataclasses

import h5py
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.robomimic import dataset_utils


_DESCRIPTION = """
The Proficient Human datasets were collected by 1 proficient operator using the
[RoboTurk](https://roboturk.stanford.edu/) platform (with the exception of
Transport, which had 2 proficient operators working together). Each dataset
consists of 200 successful trajectories.

Each task has two versions: one with low dimensional observations (`low_dim`),
and one with images (`image`).

The datasets follow the [RLDS format](https://github.com/google-research/rlds)
to represent steps and episodes.
"""

_CITATION = """
@inproceedings{robomimic2021,
  title={What Matters in Learning from Offline Human Demonstrations for Robot Manipulation},
  author={Ajay Mandlekar and Danfei Xu and Josiah Wong and Soroush Nasiriany
          and Chen Wang and Rohun Kulkarni and Li Fei-Fei and Silvio Savarese
          and Yuke Zhu and Roberto Mart\'{i}n-Mart\'{i}n},
  booktitle={Conference on Robot Learning},
  year={2021}
}
"""


@dataclasses.dataclass
class BuilderConfig(tfds.core.BuilderConfig):
  """Configuration of the dataset versions."""
  task: str = 'lift'
  filename: str = 'demo'
  horizon: int = 100


_TASKS = {
    'lift': {
        'object': 10,
        'states': 32,
        'horizon': 400,
        'action_size': 7,
    },
    'can': {
        'object': 14,
        'states': 71,
        'horizon': 400,
        'action_size': 7,
    },
    'square': {
        'object': 14,
        'states': 45,
        'horizon': 400,
        'action_size': 7,
    },
    'transport': {
        'object': 41,
        'states': 115,
        'horizon': 700,
        'action_size': 14,
    },
    'tool_hang': {
        'object': 44,
        'states': 58,
        'horizon': 700,
        'action_size': 7,
    }
}


def _builder_configs():
  """Creates the PH build configs."""
  configs = []
  for task, details in _TASKS.items():
    types = ['low_dim', 'image']
    for obs_type in types:
      # pytype: disable=wrong-keyword-args
      configs.append(
          BuilderConfig(
              name=f'{task}_{obs_type}',
              task=task,
              filename=obs_type,
              horizon=details['horizon']))
      # pytype: enable=wrong-keyword-args
  return configs


def _float_tensor_feature(size: int) -> tfds.features.Tensor:
  return tfds.features.Tensor(
      shape=(size,), dtype=tf.float64, encoding=tfds.features.Encoding.ZLIB)


def _image_feature(size: int) -> tfds.features.Image:
  return tfds.features.Image(
      shape=(size, size, 3), dtype=tf.uint8, encoding_format='png')


class RobomimicPh(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for robomimic_ph dataset."""

  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.0.1': 'Citation updated.',
  }
  BUILDER_CONFIGS = _builder_configs()


  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=self._get_features(),
        supervised_keys=None,
        homepage='https://arise-initiative.github.io/robomimic-web/',
        citation=_CITATION,
    )

  def _get_features(self):
    obs_dim = _TASKS[self.builder_config.task]['object']
    states_dim = _TASKS[self.builder_config.task]['states']
    action_size = _TASKS[self.builder_config.task]['action_size']

    observation = {
        'object': _float_tensor_feature(obs_dim,),
        'robot0_eef_pos': _float_tensor_feature(3),
        'robot0_eef_quat': _float_tensor_feature(4),
        'robot0_eef_vel_ang': _float_tensor_feature(3),
        'robot0_eef_vel_lin': _float_tensor_feature(3),
        'robot0_gripper_qpos': _float_tensor_feature(2),
        'robot0_gripper_qvel': _float_tensor_feature(2),
        'robot0_joint_pos': _float_tensor_feature(7),
        'robot0_joint_pos_cos': _float_tensor_feature(7),
        'robot0_joint_pos_sin': _float_tensor_feature(7),
        'robot0_joint_vel': _float_tensor_feature(7),
    }
    if self.builder_config.task == 'transport':
      observation['robot1_eef_pos'] = _float_tensor_feature(3)
      observation['robot1_eef_quat'] = _float_tensor_feature(4)
      observation['robot1_eef_vel_ang'] = _float_tensor_feature(3)
      observation['robot1_eef_vel_lin'] = _float_tensor_feature(3)
      observation['robot1_gripper_qpos'] = _float_tensor_feature(2)
      observation['robot1_gripper_qvel'] = _float_tensor_feature(2)
      observation['robot1_joint_pos'] = _float_tensor_feature(7)
      observation['robot1_joint_pos_cos'] = _float_tensor_feature(7)
      observation['robot1_joint_pos_sin'] = _float_tensor_feature(7)
      observation['robot1_joint_vel'] = _float_tensor_feature(7)

    if 'image' in self.builder_config.filename:
      if self.builder_config.task == 'tool_hang':
        observation['robot0_eye_in_hand_image'] = _image_feature(240)
        observation['sideview_image'] = _image_feature(240)
      elif self.builder_config.task == 'transport':
        observation['robot0_eye_in_hand_image'] = _image_feature(84)
        observation['robot1_eye_in_hand_image'] = _image_feature(84)
        observation['shouldercamera0_image'] = _image_feature(84)
        observation['shouldercamera1_image'] = _image_feature(84)
      else:
        observation['agentview_image'] = _image_feature(84)
        observation['robot0_eye_in_hand_image'] = _image_feature(84)

    episode_metadata = {
        'train': tf.bool,
        'valid': tf.bool,
    }
    if self.builder_config.task != 'tool_hang':
      episode_metadata = {
          '20_percent': tf.bool,
          '20_percent_train': tf.bool,
          '20_percent_valid': tf.bool,
          '50_percent': tf.bool,
          '50_percent_train': tf.bool,
          '50_percent_valid': tf.bool,
          'train': tf.bool,
          'valid': tf.bool,
      }

    features = tfds.features.FeaturesDict({
        'horizon':
            tf.int32,
        'episode_id':
            tf.string,
        'steps':
            tfds.features.Dataset({
                'action': _float_tensor_feature(action_size),
                'observation': observation,
                'reward': tf.float64,
                'is_first': tf.bool,
                'is_last': tf.bool,
                'is_terminal': tf.bool,
                'discount': tf.int32,
                'states': _float_tensor_feature(states_dim),
            }),
        **episode_metadata,
    })
    return features

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract({
        'file_path':
            f'http://downloads.cs.stanford.edu/downloads/rt_benchmark/{self.builder_config.task}/ph/{self.builder_config.filename}.hdf5'
    })

    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    file_path = path['file_path']

    with tf.io.gfile.GFile(file_path, 'rb') as f:
      with h5py.File(f, 'r') as dataset_file:
        data = dataset_file['data']
        mask = dataset_file['mask']
        string_mask = {}
        for k in mask:
          string_mask[k] = []
          for element in mask[k]:
            string_mask[k].append(element.decode('UTF-8'))
        mask = string_mask
        for key in data:
          yield key, {
              'steps': dataset_utils.build_episode(data[key]),
              'horizon': self.builder_config.horizon,
              'episode_id': key,
              **dataset_utils.episode_metadata(mask, key)
          }
