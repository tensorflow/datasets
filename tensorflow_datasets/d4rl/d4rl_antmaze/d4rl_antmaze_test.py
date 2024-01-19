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

"""d4rl_antmaze dataset."""

from tensorflow_datasets.d4rl.d4rl_antmaze import d4rl_antmaze
import tensorflow_datasets.public_api as tfds


class D4rlUMazeTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_antmaze dataset."""

  DATASET_CLASS = d4rl_antmaze.D4rlAntmaze
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'antmaze-umaze-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'antmaze-umaze-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['umaze-v0']


class D4rlUMazeDiverseTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_antmaze dataset."""

  DATASET_CLASS = d4rl_antmaze.D4rlAntmaze
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'antmaze-umaze-diverse-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'antmaze-umaze-diverse-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['umaze-diverse-v0']


class D4rlMediumPlayTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_antmaze dataset."""

  DATASET_CLASS = d4rl_antmaze.D4rlAntmaze
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'antmaze-medium-play-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'antmaze-medium-play-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['medium-play-v0']


class D4rlMediumDiverseTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_antmaze dataset."""

  DATASET_CLASS = d4rl_antmaze.D4rlAntmaze
  SPLITS = {
      'train': 3,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'antmaze-medium-diverse-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'antmaze-medium-diverse-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['medium-diverse-v0']


class D4rlLargeDiverseTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_antmaze dataset."""

  DATASET_CLASS = d4rl_antmaze.D4rlAntmaze
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'antmaze-large-diverse-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'antmaze-large-diverse-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['large-diverse-v0']


class D4rlLargePlayTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for d4rl_antmaze dataset."""

  DATASET_CLASS = d4rl_antmaze.D4rlAntmaze
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'antmaze-large-play-v0.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'antmaze-large-play-v0.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['large-play-v0']


if __name__ == '__main__':
  tfds.testing.test_main()
