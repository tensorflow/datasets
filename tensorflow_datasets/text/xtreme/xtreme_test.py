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

"""xtreme dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text.xtreme import xtreme


class XtremeXnliTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for xtreme dataset."""
  DATASET_CLASS = xtreme.Xtreme
  BUILDER_CONFIG_NAMES_TO_TEST = ['xnli_ar']
  SPLITS = {
      'test': 1,  # Number of fake train example
      'validation': 2,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = 'xnli'


# class XtremeXnliTest(tfds.testing.DatasetBuilderTestCase):
#   """Tests for xtreme dataset."""
#   DATASET_CLASS = xtreme.Xtreme
#   BUILDER_CONFIG_NAMES_TO_TEST = ["xnli_ar"]
#   SPLITS = {
#       'test': 2,  # Number of fake train example
#       'validation': 2,  # Number of fake test example
#   }
#   DL_EXTRACT_RESULT = {'test': 'xnli/dev.tsv', 'validation': 'xnli/test.tsv'}

if __name__ == '__main__':
  tfds.testing.test_main()
