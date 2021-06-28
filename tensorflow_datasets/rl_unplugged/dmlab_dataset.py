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

"""Builder for DMLab Datasets."""

from typing import Any, Dict

import dataclasses
import tensorflow.compat.v2 as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import rlu_common


@dataclasses.dataclass
class BuilderConfig(tfds.core.BuilderConfig):
  """Configuration of the task.

  Attributes:
    task: name of the DMLab task
    episode_length: length of the episodes in this task
  """
  task: str = 'seekavoid_arena01'
  episode_length: int = 301


class DMLabDatasetBuilder(rlu_common.RLUBuilder, skip_registration=True):
  """DatasetBuilder for RLU DMLab."""

  _SHARDS = 500
  _INPUT_FILE_PREFIX = 'gs://rl_unplugged/dmlab/'

  def get_features_dict(self):
    return tfds.features.FeaturesDict({
        'steps':
            tfds.features.Dataset({
                'observation': {
                    'pixels':
                        tfds.features.Image(
                            shape=(
                                72,
                                96,
                                3,
                            ),
                            dtype=tf.uint8,
                            encoding_format='png'),
                    'last_action':
                        tf.int64,
                    'last_reward':
                        tf.float32,
                },
                'action': tf.int64,
                'reward': tf.float32,
                'is_terminal': tf.bool,
                'is_first': tf.bool,
                'discount': tf.float32,
            }),
        'episode_id':
            tf.int64,
        'episode_return':
            tf.float32,
    })

  def get_file_prefix(self):
    run = self.builder_config.name
    task = self.builder_config.task
    return f'{self._INPUT_FILE_PREFIX}/{task}/{run}/tfrecord'

  def num_shards(self):
    return self._SHARDS

  def tf_example_to_step_ds(self,
                            tf_example: tf.train.Example) -> Dict[str, Any]:
    """Create an episode from a TF example."""
    episode_length = self.builder_config.episode_length

    # Parse tf.Example.
    def sequence_feature(shape, dtype=tf.float32):
      return tf.io.FixedLenFeature(shape=[episode_length] + shape, dtype=dtype)

    feature_description = {
        'episode_id': tf.io.FixedLenFeature([], tf.int64),
        'start_idx': tf.io.FixedLenFeature([], tf.int64),
        'episode_return': tf.io.FixedLenFeature([], tf.float32),
        'observations_pixels': sequence_feature([], tf.string),
        'observations_reward': sequence_feature([]),
        # actions are one-hot arrays.
        'observations_action': sequence_feature([15]),
        'actions': sequence_feature([], tf.int64),
        'rewards': sequence_feature([]),
        'discounted_rewards': sequence_feature([]),
        'discounts': sequence_feature([]),
    }

    data = tf.io.parse_single_example(tf_example, feature_description)

    episode = {
        # Episode Metadata
        'episode_id': data['episode_id'],
        'episode_return': data['episode_return'],
        'steps': {
            'observation': {
                'pixels':
                    data['observations_pixels'],
                'last_action':
                    tf.argmax(
                        data['observations_action'],
                        axis=1,
                        output_type=tf.int64),
                'last_reward':
                    data['observations_reward'],
            },
            'action': data['actions'],
            'reward': data['rewards'],
            'discount': data['discounts'],
            'is_first': [True] + [False] * (episode_length - 1),
            'is_terminal': [False] * (episode_length)
        }
    }
    return episode
