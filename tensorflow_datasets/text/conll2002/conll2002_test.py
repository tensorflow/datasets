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

"""conll2002 dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.conll2002 import conll2002


class Conll2002EspTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for conll2002 dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = [conll2002.ES_CONFIG.name]
  DATASET_CLASS = conll2002.Conll2002
  SPLITS = {
      'train': 2,
      'dev': 1,
      'test': 1,
  }

  DL_EXTRACT_RESULT = {
      'train': 'esp.train',
      'dev': 'esp.testa',
      'test': 'esp.testb',
  }


class Conll2002NedTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for conll2002 dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = [conll2002.NL_CONFIG.name]
  DATASET_CLASS = conll2002.Conll2002
  SPLITS = {
      'train': 2,
      'dev': 1,
      'test': 1,
  }

  DL_EXTRACT_RESULT = {
      'train': 'ned.train',
      'dev': 'ned.testa',
      'test': 'ned.testb',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
