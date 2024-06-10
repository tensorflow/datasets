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

"""Test QM9 dataset conversion to tensorflow_datasets format."""

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.qm9 import qm9_dataset_builder


class Qm9Test(testing.DatasetBuilderTestCase):
  """Tests for QM9 dataset. See superclass for details."""

  # We patch properties of the testdata here.
  qm9_dataset_builder._SIZE = 5
  qm9_dataset_builder._CHARACTERIZED_SIZE = 4

  DATASET_CLASS = qm9_dataset_builder.Builder

  DL_EXTRACT_RESULT = {
      'atomref': 'atomref.txt',
      'uncharacterized': 'uncharacterized.txt',
      # This is empty so it returns the base directory (where the
      # extracted files for the testdata are).
      'dsgdb9nsd': '',
  }

  SPLITS = {
      'train': 4,
  }


if __name__ == '__main__':
  testing.test_main()
