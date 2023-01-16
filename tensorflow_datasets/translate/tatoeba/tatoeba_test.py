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

"""tatoeba dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate.tatoeba import tatoeba


class TatoebaTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for tatoeba dataset."""

  DATASET_CLASS = tatoeba.Tatoeba
  BUILDER_CONFIG_NAMES_TO_TEST = ['tatoeba_af']
  SPLITS = {
      'train': 5,  # Number of fake train example
  }

  DL_EXTRACT_RESULT = {
      'tatoeba_source_data': 'tatoeba.afr-eng.afr',
      'tatoeba_eng_data': 'tatoeba.afr-eng.eng',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
