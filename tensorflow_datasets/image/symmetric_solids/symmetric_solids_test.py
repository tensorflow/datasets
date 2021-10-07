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

"""symmetric_solids dataset."""

from tensorflow_datasets.image.symmetric_solids import symmetric_solids
import tensorflow_datasets.public_api as tfds


class SymmetricSolidsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for symmetric_solids dataset."""
  DATASET_CLASS = symmetric_solids.SymmetricSolids
  SPLITS = {
      'train': 6,  # Number of fake train examples
      'test': 3,  # Number of fake test examples
  }
  DL_EXTRACT_RESULT = ''


if __name__ == '__main__':
  tfds.testing.test_main()
