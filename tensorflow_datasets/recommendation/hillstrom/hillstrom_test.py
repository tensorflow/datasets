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

"""Kevin Hillstrom Dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.recommendation.hillstrom import hillstrom


class HillstromTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for Kevin Hillstrom Dataset."""

  DATASET_CLASS = hillstrom.Hillstrom
  SPLITS = {'train': 4}  # Number of fake train example

  # If you are calling `download/download_and_extract` with a dict, like:
  #   dl_manager.download({'some_key': 'http://a.org/out.txt', ...})
  # then the tests needs to provide the fake output paths relative to the
  # fake data directory
  DL_EXTRACT_RESULT = 'fake_data.txt'


if __name__ == '__main__':
  tfds.testing.test_main()
