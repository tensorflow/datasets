# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""RLU Atari datasets."""

from __future__ import annotations

from typing import Any, Dict

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import atari_utils
from tensorflow_datasets.rl_unplugged import rlu_common


class RluAtari(rlu_common.RLUBuilder):
  """DatasetBuilder for RLU Atari."""

  _SHARDS = 50
  _INPUT_FILE_PREFIX = 'gs://rl_unplugged/atari_episodes_ordered'

  VERSION = tfds.core.Version('1.3.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.1.0': 'Added is_last.',
      '1.2.0': 'Added checkpoint id.',
      '1.3.0': 'Removed redundant clipped reward fields.',
  }

  BUILDER_CONFIGS = atari_utils.builder_configs()

  def get_features_dict(self):
    return atari_utils.features_dict()

  def get_description(self):
    return atari_utils.description()

  def get_citation(self):
    return atari_utils.citation()

  def get_file_prefix(self):
    run = self.builder_config.run
    game = self.builder_config.game
    return atari_utils.file_prefix(self._INPUT_FILE_PREFIX, run, game)

  def num_shards(self):
    return atari_utils.num_shards(self.builder_config.game, self._SHARDS)

  def get_episode_id(self, episode):
    return atari_utils.episode_id(episode)

  def tf_example_to_step_ds(
      self, tf_example: tf.train.Example
  ) -> Dict[str, Any]:
    return atari_utils.atari_example_to_rlds(tf_example)
