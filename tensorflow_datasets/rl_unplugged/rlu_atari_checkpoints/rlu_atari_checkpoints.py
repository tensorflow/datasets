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

"""RLU Atari datasets."""

from typing import Any, Dict

import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import atari_utils
from tensorflow_datasets.rl_unplugged import rlu_common

_EXTRA_DESCRIPTION = """
  Each of the configurations is broken into splits. Splits correspond to
  checkpoints of 1M steps (note that the number of episodes may difer).
  Checkpoints are ordered in time (so checkpoint 0 ran before checkpoint 1).
"""


class RluAtariCheckpoints(rlu_common.RLUBuilder):
  """DatasetBuilder for RLU Atari with one split per checkpoint."""

  _SHARDS = 50
  _SPLITS = 50
  _INPUT_FILE_PREFIX = 'gs://rl_unplugged/atari_episodes_ordered'

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  BUILDER_CONFIGS = atari_utils.builder_configs()

  def get_features_dict(self):
    return atari_utils.features_dict()

  def get_description(self):
    return atari_utils.description() + _EXTRA_DESCRIPTION

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

  def tf_example_to_step_ds(self,
                            tf_example: tf.train.Example) -> Dict[str, Any]:
    return atari_utils.atari_example_to_rlds(tf_example)

  def get_splits(self):
    checkpoints = {}
    for i in range(self.num_shards()):
      paths = {
          'file_paths': [
              rlu_common.filename(self.get_file_prefix(), self.num_shards(), i)
          ]
      }
      checkpoints[f'checkpoint_{i:02d}'] = self._generate_examples(paths)
    return checkpoints
