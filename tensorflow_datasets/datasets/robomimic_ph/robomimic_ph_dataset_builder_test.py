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

"""robomimic_ph dataset."""

from tensorflow_datasets.datasets.robomimic_ph import robomimic_ph_dataset_builder
import tensorflow_datasets.public_api as tfds


class RobomimicPhTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for robomimic_ph dataset."""

  DATASET_CLASS = robomimic_ph_dataset_builder.Builder
  SPLITS = {'train': 2}
  SKIP_TF1_GRAPH_MODE = True

  DL_EXTRACT_RESULT = {'file_path': 'lift_low_dim.hdf5'}
  DL_DOWNLOAD_RESULT = {'file_path': 'lift_low_dim.hdf5'}

  BUILDER_CONFIG_NAMES_TO_TEST = ['lift_ph_low_dim']
