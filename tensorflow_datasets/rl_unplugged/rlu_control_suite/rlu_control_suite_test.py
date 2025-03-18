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

"""rlu_control_suite dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.rl_unplugged.rlu_control_suite import rlu_control_suite


class RluControlSuiteTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for rlu_control_suite dataset."""

  DATASET_CLASS = rlu_control_suite.RluControlSuite
  SPLITS = {
      'train': 1,  # Number of fake train example
  }

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['cartpole_swingup']

  @classmethod
  def setUpClass(cls):
    rlu_control_suite.RluControlSuite._INPUT_FILE_PREFIX = cls.dummy_data
    rlu_control_suite.RluControlSuite._SHARDS = 1
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()
