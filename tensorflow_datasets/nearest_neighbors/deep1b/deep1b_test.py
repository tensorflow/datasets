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

"""deep1b dataset."""

from tensorflow_datasets.nearest_neighbors.deep1b import deep1b
import tensorflow_datasets.public_api as tfds


class Deep1bTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for deep1b dataset."""
  DATASET_CLASS = deep1b.Deep1b
  SPLITS = {
      'database': 3,  # Number of fake train example
      'test': 2,  # Number of fake test example
  }
  DL_EXTRACT_RESULT = {'file': 'dummy.hdf5'}


if __name__ == '__main__':
  tfds.testing.test_main()
