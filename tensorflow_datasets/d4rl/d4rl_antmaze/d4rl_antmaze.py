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

"""D4RL Ant-maze dataset."""

from typing import Any

from tensorflow_datasets.d4rl import dataset_builder
import tensorflow_datasets.public_api as tfds


class D4rlAntmaze(dataset_builder.D4RLDatasetBuilder):
  """DatasetBuilder for ant dataset."""

  VERSION = tfds.core.Version('1.1.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  _TASK_REFERENCE = ('See more details about the task and its versions in '
                     'https://github.com/rail-berkeley/d4rl/wiki/Tasks#antmaze')

  # pylint: disable=protected-access
  # Step metadata fields.
  QPOS = dataset_builder._QPOS
  QVEL = dataset_builder._QVEL
  GOAL = dataset_builder._GOAL
  # pylint: enable=protected-access

  BUILDER_CONFIGS = [
      dataset_builder.BuilderConfig(
          name='umaze-v0',
          dataset_dir='ant_maze_new',
          env='mujoco',
          file_suffix='Ant_maze_u-maze_noisy_multistart_False_multigoal_False_sparse',
          step_metadata_keys=frozenset([QPOS, QVEL, GOAL]),
          description=_TASK_REFERENCE),
      dataset_builder.BuilderConfig(
          name='umaze-diverse-v0',
          dataset_dir='ant_maze_new',
          env='mujoco',
          file_suffix='Ant_maze_u-maze_noisy_multistart_True_multigoal_True_sparse',
          step_metadata_keys=frozenset([QPOS, QVEL, GOAL]),
          description=_TASK_REFERENCE),
      dataset_builder.BuilderConfig(
          name='medium-play-v0',
          dataset_dir='ant_maze_new',
          env='mujoco',
          file_suffix='Ant_maze_big-maze_noisy_multistart_True_multigoal_False_sparse',
          step_metadata_keys=frozenset([QPOS, QVEL, GOAL]),
          description=_TASK_REFERENCE),
      dataset_builder.BuilderConfig(
          name='medium-diverse-v0',
          dataset_dir='ant_maze_new',
          env='mujoco',
          file_suffix='Ant_maze_big-maze_noisy_multistart_True_multigoal_True_sparse',
          step_metadata_keys=frozenset([QPOS, QVEL, GOAL]),
          description=_TASK_REFERENCE),
      dataset_builder.BuilderConfig(
          name='large-diverse-v0',
          dataset_dir='ant_maze_new',
          env='mujoco',
          file_suffix='Ant_maze_hardest-maze_noisy_multistart_True_multigoal_True_sparse',
          step_metadata_keys=frozenset([QPOS, QVEL, GOAL]),
          description=_TASK_REFERENCE),
      dataset_builder.BuilderConfig(
          name='large-play-v0',
          dataset_dir='ant_maze_new',
          env='mujoco',
          file_suffix='Ant_maze_hardest-maze_noisy_multistart_True_multigoal_False_sparse',
          step_metadata_keys=frozenset([QPOS, QVEL, GOAL]),
          description=_TASK_REFERENCE),
  ]

  def __init__(self, **kwargs: Any):
    config = dataset_builder.DatasetConfig(
        name='antmaze',
        obs_len=29,
        action_len=8,
        qpos_len=15,
        qvel_len=14,
        goal_len=2)
    super().__init__(ds_config=config, **kwargs)

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    ds_dir = self.builder_config.dataset_dir
    ds_name = self.builder_config.file_suffix + '.hdf5'
    path = dl_manager.download_and_extract({
        'file_path':
            'http://rail.eecs.berkeley.edu/datasets/offline_rl/' + ds_dir +
            '/' + ds_name
    })
    return {
        'train': self._generate_examples(path),
    }
