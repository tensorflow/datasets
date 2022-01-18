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

"""Tests for CREMA-D dataset builder."""

from tensorflow_datasets import testing
from tensorflow_datasets.audio import crema_d


class CremaDTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = crema_d.CremaD
  SPLITS = {
      'train': 2,
      'validation': 1,
      'test': 1,
  }

  DL_EXTRACT_RESULT = {
      'summary_table':
          'summary_table.csv',
      'all_files': [
          '1000_AA_HAP_XX.wav',
          '1001_AA_HAP_XX.wav',
          '1002_AA_ANG_XX.wav',
          '1003_AA_FEA_XX.wav',
      ]
  }


if __name__ == '__main__':
  testing.test_main()
