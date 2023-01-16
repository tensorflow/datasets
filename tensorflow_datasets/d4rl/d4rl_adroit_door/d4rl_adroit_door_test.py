# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

from tensorflow_datasets.d4rl.d4rl_adroit_door import d4rl_adroit_door
import tensorflow_datasets.public_api as tfds


class D4rlAdroitDoorClonedV1Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_adroit_door dataset."""

  DATASET_CLASS = d4rl_adroit_door.D4rlAdroitDoor

  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'door-cloned-v1.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'door-cloned-v1.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v1-cloned']


class D4rlAdroitDoorExpertV1Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_adroit_door dataset."""

  DATASET_CLASS = d4rl_adroit_door.D4rlAdroitDoor

  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'door-expert-v1.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'door-expert-v1.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v1-expert']


class D4rlAdroitDoorHumanV1Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_adroit_door dataset."""

  DATASET_CLASS = d4rl_adroit_door.D4rlAdroitDoor

  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'door-human-v1.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'door-human-v1.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v1-human']


class D4rlAdroitDoorClonedV0Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_adroit_door dataset."""

  DATASET_CLASS = d4rl_adroit_door.D4rlAdroitDoor

  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'door-cloned-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'door-cloned-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v0-cloned']


class D4rlAdroitDoorExpertV0Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_adroit_door dataset."""

  DATASET_CLASS = d4rl_adroit_door.D4rlAdroitDoor

  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'door-expert-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'door-expert-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v0-expert']


class D4rlAdroitDoorHumanV0Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_adroit_door dataset."""

  DATASET_CLASS = d4rl_adroit_door.D4rlAdroitDoor

  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'door-human-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'door-human-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['v0-human']


if __name__ == '__main__':
  tfds.testing.test_main()
