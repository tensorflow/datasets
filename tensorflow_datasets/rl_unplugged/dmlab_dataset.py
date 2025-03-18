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

"""Builder for DMLab Datasets."""

from __future__ import annotations

import dataclasses
from typing import Any, Dict

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import rlu_common

_DMLAB_DESCRIPTION = """
DeepMind Lab dataset has several levels from the challenging, partially
observable [Deepmind Lab suite](https://github.com/deepmind/lab). DeepMind Lab
dataset is collected by training distributed R2D2 by [Kapturowski et al., 2018]
(https://openreview.net/forum?id=r1lyTjAqYX) agents from scratch on individual
tasks. We recorded the experience across all actors during entire training runs
a few times for every task. The details of the dataset generation process is
described in [Gulcehre et al., 2021](https://arxiv.org/abs/2103.09575).

We release datasets for five different DeepMind Lab levels: `seekavoid_arena_01`,
`explore_rewards_few`, `explore_rewards_many`, `rooms_watermaze`,
`rooms_select_nonmatching_object`. We also release the snapshot datasets for
`seekavoid_arena_01` level that we generated the datasets from a trained R2D2
snapshot with different levels of epsilons for the epsilon-greedy algorithm
when evaluating the agent in the environment.

DeepMind Lab dataset is fairly large-scale. We recommend you to try it if you
are interested in large-scale offline RL models with memory.
"""

_CITATION = """
@article{gulcehre2021rbve,
    title={Regularized Behavior Value Estimation},
    author={{\\c{C}}aglar G{\\"{u}}l{\\c{c}}ehre and
               Sergio G{\\'{o}}mez Colmenarejo and
               Ziyu Wang and
               Jakub Sygnowski and
               Thomas Paine and
               Konrad Zolna and
               Yutian Chen and
               Matthew W. Hoffman and
               Razvan Pascanu and
               Nando de Freitas},
    year={2021},
    journal   = {CoRR},
    url       = {https://arxiv.org/abs/2103.09575},
    eprint={2103.09575},
    archivePrefix={arXiv},
}
"""

_PIXELS_HEIGHT = 72
_PIXELS_WIDTH = 96
_PIXELS_SHAPE = (_PIXELS_HEIGHT, _PIXELS_WIDTH, 3)


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
        'steps': tfds.features.Dataset({
            'observation': {
                'pixels': tfds.features.Image(
                    shape=_PIXELS_SHAPE, dtype=np.uint8, encoding_format='png'
                ),
                'last_action': np.int64,
                'last_reward': np.float32,
            },
            'action': np.int64,
            'reward': np.float32,
            'is_terminal': np.bool_,
            'is_first': np.bool_,
            'is_last': np.bool_,
            'discount': np.float32,
        }),
        'episode_id': np.int64,
        'episode_return': np.float32,
    })

  def get_description(self):
    return _DMLAB_DESCRIPTION

  def get_citation(self):
    return _CITATION

  def get_file_prefix(self):
    run = self.builder_config.name
    task = self.builder_config.task
    return f'{self._INPUT_FILE_PREFIX}/{task}/{run}/tfrecord'

  def num_shards(self):
    return self._SHARDS

  def tf_example_to_step_ds(
      self, tf_example: tf.train.Example
  ) -> Dict[str, Any]:
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

    # Dmlab observations are compressed with OpenCV imencode function. Encoding
    # with imencode and decoding with TF PNG decoder flips the order of the
    # color channels. Here we flip back the order color of channels from BGR to
    # RGB:
    pixels = tf.scan(
        fn=lambda _, png: tf.reshape(tf.io.decode_png(png), _PIXELS_SHAPE),
        elems=data['observations_pixels'],
        initializer=tf.zeros(_PIXELS_SHAPE, dtype=tf.uint8),
    )
    pixels = tf.reverse(pixels, axis=[-1])

    episode = {
        # Episode Metadata
        'episode_id': data['episode_id'],
        'episode_return': data['episode_return'],
        'steps': {
            'observation': {
                'pixels': pixels,
                'last_action': tf.argmax(
                    data['observations_action'], axis=1, output_type=tf.int64
                ),
                'last_reward': data['observations_reward'],
            },
            'action': data['actions'],
            'reward': data['rewards'],
            'discount': data['discounts'],
            'is_first': [True] + [False] * (episode_length - 1),
            'is_last': [False] * (episode_length - 1) + [True],
            'is_terminal': [False] * (episode_length),
        },
    }
    return episode
