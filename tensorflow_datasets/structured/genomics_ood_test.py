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

"""Test for genomics_ood dataset."""

import os

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured import genomics_ood

_FAKE_DATA_FILE = os.path.join(
    os.path.normpath(os.path.dirname(__file__) + '/../../'),
    'tensorflow_datasets',
    'testing',
    'test_data',
    'fake_examples',
    'genomics_ood',
    'genomics_ood.zip',
)


class GenomicsOodTest(tfds.testing.DatasetBuilderTestCase):
  genomics_ood._DATA_URL = _FAKE_DATA_FILE
  DATASET_CLASS = genomics_ood.GenomicsOod
  SPLITS = {
      'train': 5,  # Number of fake train example
      'validation': 5,  # Number of fake validation example
      'test': 5,  # Number of fake test example
      'validation_ood': 5,  # Number of fake validation ood example
      'test_ood': 5,  # Number of fake test ood example
  }


if __name__ == '__main__':
  tfds.testing.test_main()
