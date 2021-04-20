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

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
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
    float_type = tf.float32
    scalar_info = float_type
    replay_datasets = {
        'v1-medium-replay', 'v1-full-replay', 'v2-medium-replay',
        'v2-full-replay'
    }
    if self.builder_config.name in replay_datasets:
      float_type = tf.float64
      scalar_info = tfds.features.Tensor(shape=(1,), dtype=float_type)

    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            'steps':
                tfds.features.Dataset({
                    'observation':
                        tfds.features.Tensor(shape=(17,), dtype=float_type),
                    'action':
                        tfds.features.Tensor(shape=(6,), dtype=float_type),
                    'reward':
                        scalar_info,
                    'is_terminal':
                        tf.bool,
                    'is_first':
                        tf.bool,
                    'discount':
                        scalar_info,
                }),
        }),
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
