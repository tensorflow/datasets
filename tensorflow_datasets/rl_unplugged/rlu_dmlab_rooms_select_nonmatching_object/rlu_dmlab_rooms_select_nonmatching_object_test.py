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

"""rlu_dmlab_rooms_select_nonmatching_object dataset."""
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged import dmlab_dataset
from tensorflow_datasets.rl_unplugged.rlu_dmlab_rooms_select_nonmatching_object import rlu_dmlab_rooms_select_nonmatching_object


class RluDmlabRoomsSelectNonmatchingObjectTest(
    tfds.testing.DatasetBuilderTestCase
):
  """Tests for rlu_dmlab_explore_object_rewards_many dataset."""

  DATASET_CLASS = (
      rlu_dmlab_rooms_select_nonmatching_object.RluDmlabRoomsSelectNonmatchingObject
  )
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  # The different configs are only different in the name of the files.
  BUILDER_CONFIG_NAMES_TO_TEST = ['training_0']

  @classmethod
  def setUpClass(cls):
    dmlab_dataset.DMLabDatasetBuilder._INPUT_FILE_PREFIX = cls.dummy_data
    dmlab_dataset.DMLabDatasetBuilder._SHARDS = 1
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()
