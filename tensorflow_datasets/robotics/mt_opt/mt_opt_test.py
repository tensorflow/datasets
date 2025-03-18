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

"""mt_opt dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.robotics.mt_opt import mt_opt


class MtOptTestRlds(tfds.testing.DatasetBuilderTestCase):
  """Tests for mt_opt dataset."""

  DATASET_CLASS = mt_opt.MtOpt
  SPLITS = {'train': 2}

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['rlds']

  @classmethod
  def setUpClass(cls):
    mt_opt.MtOpt._INPUT_FILE_PREFIX = cls.dummy_data
    mt_opt._NAME_TO_SPLITS['rlds']['train'] = 1
    super().setUpClass()


class MtOptTestSd(tfds.testing.DatasetBuilderTestCase):
  """Tests for mt_opt dataset."""

  DATASET_CLASS = mt_opt.MtOpt
  SPLITS = {'train': 2, 'test': 2}

  SKIP_TF1_GRAPH_MODE = True

  BUILDER_CONFIG_NAMES_TO_TEST = ['sd']

  @classmethod
  def setUpClass(cls):
    mt_opt.MtOpt._INPUT_FILE_PREFIX = cls.dummy_data
    mt_opt._NAME_TO_SPLITS['sd']['train'] = 1
    mt_opt._NAME_TO_SPLITS['sd']['test'] = 1
    super().setUpClass()


if __name__ == '__main__':
  tfds.testing.test_main()
