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

"""d4rl_adroit_door dataset."""
from typing import Any

from tensorflow_datasets.d4rl import dataset_builder
import tensorflow_datasets.public_api as tfds


class D4rlAdroitDoor(dataset_builder.D4RLDatasetBuilder):
  """DatasetBuilder for d4rl_adroit_door dataset."""

  VERSION = tfds.core.Version('1.1.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.1.0': 'Added is_last.',
  }

  BUILDER_CONFIGS = dataset_builder.ADROIT_BUILDER_CONFIGS

  def __init__(self, **kwargs: Any):
    config = dataset_builder.DatasetConfig(
        name='door', obs_len=39, action_len=28, qpos_len=30, qvel_len=30)
    super().__init__(ds_config=config, **kwargs)
