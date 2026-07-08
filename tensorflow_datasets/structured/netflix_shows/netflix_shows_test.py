# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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
"""netflix_shows dataset."""

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.structured.netflix_shows import netflix_shows


class NetflixShowsTest(tfds.testing.DatasetBuilderTestCase):
  """Tests for netflix_shows dataset."""
  DATASET_CLASS = netflix_shows.NetflixShows
  SPLITS = {
      'train': 7787,
  }
  DL_EXTRACT_RESULT = 'netflix_titles.csv'


if __name__ == '__main__':
  tfds.testing.test_main()
