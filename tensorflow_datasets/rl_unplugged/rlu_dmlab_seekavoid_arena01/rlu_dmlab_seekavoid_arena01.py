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

"""rlu_dmlab_seekavoid_arena01 dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import dmlab_dataset


_TASK = 'seekavoid_arena_01'
_EPISODE_LENGTH = 301
_CONFIG_NAMES = ['training_0', 'training_1', 'training_2',
                 'snapshot_0_eps_0.0', 'snapshot_1_eps_0.0',
                 'snapshot_0_eps_0.01', 'snapshot_1_eps_0.01',
                 'snapshot_0_eps_0.25', 'snapshot_1_eps_0.25']


class RluDmlabSeekavoidArena01(dmlab_dataset.DMLabDatasetBuilder):
  """DatasetBuilder for rlu_dmlab_seekavoid_arena01 dataset."""

  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.0.1': 'Complete list of builder configs.',
  }

  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [
      dmlab_dataset.BuilderConfig(
          name=name, task=_TASK, episode_length=_EPISODE_LENGTH)
      for name in _CONFIG_NAMES
  ]
  # pytype: enable=wrong-keyword-args
