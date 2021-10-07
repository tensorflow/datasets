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

"""rlu_dmlab_rooms_watermaze dataset."""
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import dmlab_dataset

_TASK = 'rooms_watermaze'
_EPISODE_LENGTH = 1801


class RluDmlabRoomsWatermaze(dmlab_dataset.DMLabDatasetBuilder):
  """DatasetBuilder for rlu_dmlab_rooms_select_nonmatching_object dataset."""

  VERSION = tfds.core.Version('1.1.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
      '1.1.0': 'Added is_last.',
  }

  # pytype: disable=wrong-keyword-args
  BUILDER_CONFIGS = [
      dmlab_dataset.BuilderConfig(
          name='training_0', task=_TASK, episode_length=_EPISODE_LENGTH),
      dmlab_dataset.BuilderConfig(
          name='training_1', task=_TASK, episode_length=_EPISODE_LENGTH),
      dmlab_dataset.BuilderConfig(
          name='training_2', task=_TASK, episode_length=_EPISODE_LENGTH)
  ]
  # pytype: enable=wrong-keyword-args
