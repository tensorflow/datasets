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

"""covid19 dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.covid19 import covid19


class Covid19Test(tfds.testing.DatasetBuilderTestCase):
  """Tests for covid-19 dataset."""
  DATASET_CLASS = covid19.Covid19
  SPLITS = {
      'train': 3,
  }
  DL_EXTRACT_RESULT = 'covid19.csv.gz'

  def setUp(self):
    super().setUp()
    covid19._N_RECORDS = 3
    covid19._BATCH_SIZE = 2


if __name__ == '__main__':
  tfds.testing.test_main()
