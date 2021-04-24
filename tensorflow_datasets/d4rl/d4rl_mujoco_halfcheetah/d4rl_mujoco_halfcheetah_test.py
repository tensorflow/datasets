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

"""D4Rl Halfcheetah dataset from Mujoco."""

from tensorflow_datasets.d4rl.d4rl_mujoco_halfcheetah import d4rl_mujoco_halfcheetah
import tensorflow_datasets.public_api as tfds


class D4rlMujocoHalfcheetahTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for halfcheetah dataset."""
  DATASET_CLASS = d4rl_mujoco_halfcheetah.D4rlMujocoHalfcheetah
  SPLITS = {
      'train': 2,  # Number of fake train example
  }
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'halfcheetah_medium.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'halfcheetah_medium.hdf5'}

  # builder configs only affect the dataset path
  BUILDER_CONFIG_NAMES_TO_TEST = ['v0-medium']

if __name__ == '__main__':
  tfds.testing.test_main()
