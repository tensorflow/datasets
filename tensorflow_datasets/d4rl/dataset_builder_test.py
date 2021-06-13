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

"""Tests for mujoco_build_configs."""

import tensorflow.compat.v2 as tf
from tensorflow_datasets.d4rl import dataset_builder


def _mujoco_replay_datasets():
  """Set of Mujoco datasets with replay."""
  return {
      'v1-medium-replay', 'v1-full-replay', 'v2-medium-replay', 'v2-full-replay'
  }


def _mujoco_full_metadata_datasets():
  """Set of Mujoco datasets that contain all of the metadata fields."""
  return {'v1-expert', 'v2-expert', 'v1-medium', 'v2-medium'}


class MujocoDatasetTest(tf.test.TestCase):

  def test_builder_config_step_metadata(self):
    for config in dataset_builder.MUJOCO_BUILDER_CONFIGS:
      if config.name in _mujoco_replay_datasets():
        self.assertEqual(config.float_type, tf.float64)
      else:
        self.assertEqual(config.float_type, tf.float32)

  def test_builder_config_float_type(self):
    for config in dataset_builder.MUJOCO_BUILDER_CONFIGS:
      if config.dataset_dir != 'gym_mujoco':
        self.assertTrue(config.step_metadata_keys,
                        f'Config {config.name} should contain step metadata.')
      else:
        self.assertFalse(
            config.step_metadata_keys,
            f'Config {config.name} should NOT contain step metadata.')

  def test_builder_config_episode_metadata(self):
    for config in dataset_builder.MUJOCO_BUILDER_CONFIGS:
      if config.name in _mujoco_replay_datasets():
        self.assertTrue(
            config.episode_metadata_keys,
            f'Config {config.name} should contain episode metadata.')
        self.assertFalse(
            config.has_policy_metadata,
            f'Config {config.name} should NOT contain policy metadata.')
        self.assertFalse(
            config.has_policy_last_fc_log_std,
            f'Config {config.name} should NOT contain policy values for last_fc_log_std.'
        )
      elif config.name in _mujoco_full_metadata_datasets():
        self.assertTrue(
            config.episode_metadata_keys,
            f'Config {config.name} should contain episode metadata.')
        self.assertTrue(
            config.has_policy_metadata,
            f'Config {config.name} should contain policy metadata.')
        self.assertTrue(
            config.has_policy_last_fc_log_std,
            f'Config {config.name} should contain policy values for last_fc_log_std.'
        )
      else:
        self.assertFalse(
            config.episode_metadata_keys,
            f'Config {config.name} should NOT contain episode metadata.')
        self.assertFalse(
            config.has_policy_metadata,
            f'Config {config.name} should NOT contain policy metadata.')
        self.assertFalse(
            config.has_policy_last_fc_log_std,
            f'Config {config.name} should NOT contain policy values for last_fc_log_std.'
        )


if __name__ == '__main__':
  tf.test.main()
