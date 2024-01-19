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

"""d4rl_adroit_pen dataset."""
from typing import Any

from tensorflow_datasets.d4rl import dataset_builder
import tensorflow_datasets.public_api as tfds


class D4rlAdroitPen(dataset_builder.D4RLDatasetBuilder):
  """DatasetBuilder for d4rl_adroit_pen dataset."""

  VERSION = tfds.core.Version('1.1.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.1.0': 'Added is_last.',
  }

  # pytype: disable=wrong-keyword-args
  # pylint: disable=protected-access
  # Pen uses a different policy size in expert-v1
  BUILDER_CONFIGS = dataset_builder.ADROIT_BUILDER_CONFIGS[:-1] + [
      dataset_builder.BuilderConfig(
          name='v1-expert',
          dataset_dir='hand_dapg_v1',
          env='adroit',
          file_suffix='-expert-v1',
          step_metadata_keys=frozenset([
              dataset_builder._QPOS,
              dataset_builder._QVEL,
              dataset_builder._ADROIT_BODY_POS,
              dataset_builder._ACTION_MEAN,
              dataset_builder._ACTION_LOG_STD,
          ]),
          episode_metadata_keys=frozenset([dataset_builder._ALGORITHM]),
          has_policy_metadata=True,
          has_policy_last_fc_log_std=True,
          policy_size=64,  # pytype: disable=wrong-arg-types  # gen-stub-imports
      ),
  ]

  # pylint: enable=protected-access
  # pytype: enable=wrong-keyword-args

  def __init__(self, **kwargs: Any):
    config = dataset_builder.DatasetConfig(
        name='pen', obs_len=45, action_len=24, qpos_len=30, qvel_len=30
    )
    super().__init__(ds_config=config, **kwargs)
