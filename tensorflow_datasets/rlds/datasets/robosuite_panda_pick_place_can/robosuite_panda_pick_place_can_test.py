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

"""robosuite_panda_pick_place_can dataset."""
import sys

import pytest
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rlds.datasets.robosuite_panda_pick_place_can import robosuite_panda_pick_place_can


pytest.importorskip(
    'envlogger',
    reason=(
        '`envlogger` library might not be available for Python'
        f' {sys.version} or platform {sys.platform}; see'
        ' https://pypi.org/project/envlogger/#files'
    ),
)


class RobosuitePandaPickPlaceCanHumanTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for robosuite_panda_pick_place_can dataset."""

  DATASET_CLASS = robosuite_panda_pick_place_can.RobosuitePandaPickPlaceCan
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['human_dc29b40a']

  DL_EXTRACT_RESULT = {'file_path': 'human_dc29b40a'}
  DL_DOWNLOAD_RESULT = {'file_path': 'human_dc29b40a'}


class RobosuitePandaPickPlaceCanHumanImagesTest(
    tfds.testing.DatasetBuilderTestCase
):
  """Tests for robosuite_panda_pick_place_can dataset."""

  DATASET_CLASS = robosuite_panda_pick_place_can.RobosuitePandaPickPlaceCan
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['human_images_dc29b40a']

  DL_EXTRACT_RESULT = {'file_path': 'human_images_dc29b40a'}
  DL_DOWNLOAD_RESULT = {'file_path': 'human_images_dc29b40a'}


class RobosuitePandaPickPlaceCanSyntheticTest(
    tfds.testing.DatasetBuilderTestCase
):
  """Tests for robosuite_panda_pick_place_can dataset."""

  DATASET_CLASS = robosuite_panda_pick_place_can.RobosuitePandaPickPlaceCan
  SPLITS = {
      'train': 2,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['synthetic_stochastic_sac_afe13968']

  DL_EXTRACT_RESULT = {'file_path': 'synthetic_stochastic_sac_afe13968'}
  DL_DOWNLOAD_RESULT = {'file_path': 'synthetic_stochastic_sac_afe13968'}


if __name__ == '__main__':
  tfds.testing.test_main()
