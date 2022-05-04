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

"""locomotion dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rlds.locomotion import locomotion


class AntTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for Ant dataset."""
  DATASET_CLASS = locomotion.Locomotion
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['ant_sac_1M_single_policy_stochastic']

  DL_EXTRACT_RESULT = {'file_path': 'ant_sac_1M_single_policy_stochastic'}
  DL_DOWNLOAD_RESULT = {'file_path': 'ant_sac_1M_single_policy_stochastic'}


class Walker2dTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for Walker2d dataset."""
  DATASET_CLASS = locomotion.Locomotion
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['walker2d_sac_1M_single_policy_stochastic']

  DL_EXTRACT_RESULT = {'file_path': 'walker2d_sac_1M_single_policy_stochastic'}
  DL_DOWNLOAD_RESULT = {'file_path': 'walker2d_sac_1M_single_policy_stochastic'}


class HopperTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for Hopper dataset."""
  DATASET_CLASS = locomotion.Locomotion
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['hopper_sac_1M_single_policy_stochastic']

  DL_EXTRACT_RESULT = {'file_path': 'hopper_sac_1M_single_policy_stochastic'}
  DL_DOWNLOAD_RESULT = {'file_path': 'hopper_sac_1M_single_policy_stochastic'}


class HalfCheetahTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for HalfCheetah dataset."""
  DATASET_CLASS = locomotion.Locomotion
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['halfcheetah_sac_1M_single_policy_stochastic']

  DL_EXTRACT_RESULT = {
      'file_path': 'halfcheetah_sac_1M_single_policy_stochastic'
  }
  DL_DOWNLOAD_RESULT = {
      'file_path': 'halfcheetah_sac_1M_single_policy_stochastic'
  }


class HumanoidTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for Humanoid dataset."""
  DATASET_CLASS = locomotion.Locomotion
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['humanoid_sac_15M_single_policy_stochastic']

  DL_EXTRACT_RESULT = {'file_path': 'humanoid_sac_15M_single_policy_stochastic'}
  DL_DOWNLOAD_RESULT = {
      'file_path': 'humanoid_sac_15M_single_policy_stochastic'
  }


if __name__ == '__main__':
  tfds.testing.test_main()
