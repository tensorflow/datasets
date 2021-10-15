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

"""robosuite_panda_pick_place_can dataset."""

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rlds import rlds_base

_DESCRIPTION = """
These datasets have been created with the PickPlaceCan environment of the
[robosuite robotic arm simulator](https://robosuite.ai/). The human datasets
were recorded by a single operator using
the [RLDS Creator](https://github.com/google-research/rlds-creator) and a
gamepad controller.

The synthetic datasets have been recorded using the
[EnvLogger library](https://github.com/deepmind/envlogger).

Episodes consist of 400 steps. In each episode, a tag is
added when the task is completed, this tag is stored as part of the custom step
metadata.
"""

_CITATION = """
 @misc{google-research, title={RLDS},
 url={https://github.com/google-research/rlds}, journal={GitHub},
 author={S. Ramos, S. Girgin et al.}}
"""

_HOMEPAGE = 'https://github.com/google-research/rlds'


class RobosuitePandaPickPlaceCan(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for robosuite_panda_pick_place_can dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  _DATA_PATHS = {
      'human_dc29b40a':
          'https://storage.googleapis.com/rlds_external_data_release/rlds_robosuite_panda_pick_place_can_human_state_only_dc29b40a.tar.gz',
      'human_images_dc29b40a':
          'https://storage.googleapis.com/rlds_external_data_release/rlds_robosuite_panda_pick_place_can_human_dc29b40a.tar.gz',
      'synthetic_stochastic_sac_afe13968':
          'https://storage.googleapis.com/rlds_external_data_release/rlds_robosuite_panda_pick_place_can_synthetic_stochastic_sac_afe13968.tar.gz'
  }

  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [
      rlds_base.DatasetConfig(
          name='human_dc29b40a',
          observation_info={
              'object-state':
                  tfds.features.Tensor(shape=(14,), dtype=tf.float64),
              'Can_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float64),
              'Can_to_robot0_eef_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float32),
              'robot0_joint_pos_cos':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float64),
              'robot0_gripper_qpos':
                  tfds.features.Tensor(shape=(2,), dtype=tf.float64),
              'robot0_proprio-state':
                  tfds.features.Tensor(shape=(32,), dtype=tf.float64),
              'robot0_joint_vel':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float64),
              'robot0_joint_pos_sin':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float64),
              'Can_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float64),
              'Can_to_robot0_eef_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float64),
              'robot0_gripper_qvel':
                  tfds.features.Tensor(shape=(2,), dtype=tf.float64),
              'robot0_eef_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float64),
              'robot0_eef_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float64),
          },
          action_info=tfds.features.Tensor(shape=(7,), dtype=tf.float64),
          reward_info=tf.float64,
          discount_info=tf.float64,
          episode_metadata_info={
              'agent_id': tf.string,
              'episode_index': tf.int32,
              'episode_id': tf.string,
          },
          step_metadata_info={
              'tag:placed': tf.bool,
              'image': tfds.features.Image(),
          },
          citation=_CITATION,
          homepage=_HOMEPAGE,
          overall_description=_DESCRIPTION,
          description='Human generated dataset (50 episodes).',
          supervised_keys=None,
      ),
      rlds_base.DatasetConfig(
          name='human_images_dc29b40a',
          observation_info={
              'birdview_image':
                  tfds.features.Image(
                      shape=(256, 256, 3),
                      dtype=tf.uint8,
                      encoding_format='png'),
              'object-state':
                  tfds.features.Tensor(shape=(14,), dtype=tf.float64),
              'Can_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float64),
              'Can_to_robot0_eef_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float32),
              'robot0_joint_pos_cos':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float64),
              'robot0_eye_in_hand_image':
                  tfds.features.Image(
                      shape=(256, 256, 3),
                      dtype=tf.uint8,
                      encoding_format='png'),
              'robot0_gripper_qpos':
                  tfds.features.Tensor(shape=(2,), dtype=tf.float64),
              'robot0_proprio-state':
                  tfds.features.Tensor(shape=(32,), dtype=tf.float64),
              'robot0_robotview_image':
                  tfds.features.Image(
                      shape=(256, 256, 3),
                      dtype=tf.uint8,
                      encoding_format='png'),
              'robot0_joint_vel':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float64),
              'robot0_joint_pos_sin':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float64),
              'agentview_image':
                  tfds.features.Image(
                      shape=(256, 256, 3),
                      dtype=tf.uint8,
                      encoding_format='png'),
              'Can_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float64),
              'Can_to_robot0_eef_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float64),
              'robot0_gripper_qvel':
                  tfds.features.Tensor(shape=(2,), dtype=tf.float64),
              'robot0_eef_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float64),
              'robot0_eef_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float64),
          },
          action_info=tfds.features.Tensor(shape=(7,), dtype=tf.float64),
          reward_info=tf.float64,
          discount_info=tf.float64,
          episode_metadata_info={
              'agent_id': tf.string,
              'episode_index': tf.int32,
              'episode_id': tf.string,
          },
          step_metadata_info={
              'tag:placed': tf.bool,
              'image': tfds.features.Image(),
          },
          citation=_CITATION,
          overall_description=_DESCRIPTION,
          description=(
              'Human generated dataset, including images with different camera'
              ' angles in the observation.'
              ' Note that it may take some time to generate.'),
          supervised_keys=None,
      ),
      rlds_base.DatasetConfig(
          name='synthetic_stochastic_sac_afe13968',
          observation_info={
              'object-state':
                  tfds.features.Tensor(shape=(14,), dtype=tf.float32),
              'Can_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float32),
              'Can_to_robot0_eef_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float32),
              'robot0_joint_pos_cos':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float32),
              'robot0_gripper_qpos':
                  tfds.features.Tensor(shape=(2,), dtype=tf.float32),
              'robot0_proprio-state':
                  tfds.features.Tensor(shape=(32,), dtype=tf.float32),
              'robot0_joint_vel':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float32),
              'robot0_joint_pos_sin':
                  tfds.features.Tensor(shape=(7,), dtype=tf.float32),
              'Can_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float32),
              'Can_to_robot0_eef_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float32),
              'robot0_gripper_qvel':
                  tfds.features.Tensor(shape=(2,), dtype=tf.float32),
              'robot0_eef_pos':
                  tfds.features.Tensor(shape=(3,), dtype=tf.float32),
              'robot0_eef_quat':
                  tfds.features.Tensor(shape=(4,), dtype=tf.float32),
          },
          action_info=tfds.features.Tensor(shape=(7,), dtype=tf.float32),
          reward_info=tf.float64,
          discount_info=tf.float64,
          episode_metadata_info={
              'agent_id': tf.string,
              'episode_index': tf.int32,
              'episode_id': tf.string,
          },
          step_metadata_info={
              'tag:placed': tf.bool,
              'image': tfds.features.Image(),
          },
          citation=_CITATION,
          homepage=_HOMEPAGE,
          overall_description=_DESCRIPTION,
          description='Synthetic dataset generated by a stochastic agent trained with SAC (200 episodes).',
          supervised_keys=None,
      ),
  ]

  # pytype: enable=wrong-keyword-args

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return rlds_base.build_info(self.builder_config, self)

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    path = dl_manager.download_and_extract({
        'file_path': self._DATA_PATHS[self.builder_config.name],
    })
    return {
        'train': self._generate_examples(path),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    file_path = path['file_path']
    return rlds_base.generate_examples(file_path)
