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

"""asset dataset."""

import sys

import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.text_simplification.asset import asset

sys.path.insert(0, '.')


class AssetTestRatings(tfds.testing.DatasetBuilderTestCase):
  """Tests for asset dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['ratings']
  DATASET_CLASS = asset.Asset

  DL_EXTRACT_RESULT = {
      'human_ratings.csv': 'ratings/1.0.0/human_ratings.csv',
  }

  SPLITS = {
      'full': 4,
  }


class AssetTestSimplification(tfds.testing.DatasetBuilderTestCase):
  """Tests for asset dataset."""

  BUILDER_CONFIG_NAMES_TO_TEST = ['simplification']
  DATASET_CLASS = asset.Asset

  _URL_LIST = [
      ('asset.valid.orig', 'simplification/1.0.0/asset.valid.orig'),
      ('asset.test.orig', 'simplification/1.0.0/asset.test.orig'),
  ]

  _URL_LIST += [
      (  # pylint:disable=g-complex-comprehension
          f'asset.{spl}.simp.{i}',
          f'simplification/1.0.0/asset.{spl}.simp.{i}',
      ) for spl in ['valid', 'test'] for i in range(10)
  ]
  DL_EXTRACT_RESULT = dict(_URL_LIST)

  SPLITS = {'validation': 5, 'test': 5}


if __name__ == '__main__':
  tfds.testing.test_main()
