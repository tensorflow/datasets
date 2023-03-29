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

"""rlu_atari_checkpoints_ordered dataset."""

from __future__ import annotations

from typing import Any, Dict

from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import atari_utils
from tensorflow_datasets.rl_unplugged import rlu_common

_EXTRA_DESCRIPTION = """
  Each of the configurations is broken into splits. Splits correspond to
  checkpoints of 1M steps (note that the number of episodes may difer).
  Checkpoints are ordered in time (so checkpoint 0 ran before checkpoint 1).

  Episodes within each split are ordered. Check
  https://www.tensorflow.org/datasets/determinism if you want to ensure
  that you read episodes in order.

  This dataset corresponds to the one used in the DQN replay paper.
  https://research.google/tools/datasets/dqn-replay/
"""


class RluAtariCheckpointsOrdered(rlu_common.RLUBuilder):
  """DatasetBuilder for RLU Atari with one split per checkpoint."""

  _SHARDS = 50
  _SPLITS = 50
  _INPUT_FILE_PREFIX = 'gs://rl_unplugged/atari_episodes_ordered'

  VERSION = tfds.core.Version('1.1.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.1.0': 'Removed redundant clipped reward fields.',
  }

  BUILDER_CONFIGS = atari_utils.builder_configs()

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata with shuffling disabled."""
    # pylint: disable=protected-access
    return tfds.core.DatasetInfo(
        builder=self,
        description=rlu_common._DESCRIPTION + self.get_description(),
        features=self.get_features_dict(),
        supervised_keys=None,
        homepage=rlu_common._HOMEPAGE,
        citation=self.get_citation(),
        disable_shuffling=True,
    )
    # pylint: enable=protected-access

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
    # TODO(b/209933106): Ordered datasets need an int id so we cannot use the
    # one from atari_utils. We estimate that there are at most 20k episodes
    # per checkpoint (numbers star at 0), 1e10 should be a more than safe
    # number.
    episode_id = episode['checkpoint_id'] * 1e10 + episode['episode_id']
    return int(episode_id)

  def tf_example_to_step_ds(
      self, tf_example: tf.train.Example
  ) -> Dict[str, Any]:
    return atari_utils.atari_example_to_rlds(tf_example)

  def get_splits(self):
    checkpoints = {}
    for i in range(self.num_shards()):
      paths = {
          'file_paths': rlu_common.filename(
              prefix=self.get_file_prefix(),
              num_shards=self.num_shards(),
              shard_id=i,
          )
      }
      checkpoints[f'checkpoint_{i:02d}'] = self._generate_examples(paths)
    return checkpoints

  def _generate_examples(self, paths):
    """Yields examples."""

    file_path = paths['file_paths']

    return self.generate_examples_one_file(file_path)
