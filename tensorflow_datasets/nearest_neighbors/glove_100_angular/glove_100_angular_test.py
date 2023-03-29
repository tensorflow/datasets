# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""glove_100_angular dataset."""

from tensorflow_datasets.nearest_neighbors.glove_100_angular import glove_100_angular
import tensorflow_datasets.public_api as tfds


class Glove100AngularTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for glove_100_angular dataset."""

  DATASET_CLASS = glove_100_angular.Glove100Angular
  SPLITS = {
      'database': 3,
      'test': 2,
  }

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = {'file': 'dummy.hdf5'}


if __name__ == '__main__':
  tfds.testing.test_main()
