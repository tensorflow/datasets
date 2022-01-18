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

"""kdd_cup_99 dataset."""

import tensorflow_datasets.public_api as tfds

from tensorflow_datasets.structured.kddcup99 import kddcup99


class KddCup99Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for kdd_cup_99 dataset."""

  DATASET_CLASS = kddcup99.Kddcup99
  SPLITS = {
      'train': 100,
      'test': 10,
  }
  DL_EXTRACT_RESULT = {
      'train': 'dummy_train.csv.gz',
      'test': 'dummy_test.csv.gz',
  }


if __name__ == '__main__':
  tfds.testing.test_main()
