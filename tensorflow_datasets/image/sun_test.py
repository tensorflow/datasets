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

# Lint as: python3
"""Tests for SUN (Scene UNderstanding) datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from tensorflow_datasets import testing
from tensorflow_datasets.image import sun

_EXAMPLE_DIR = os.path.join(
    os.path.normpath(os.path.dirname(__file__) + '/../'), 'testing',
    'test_data', 'fake_examples', 'sun397')


class TestableSun397(sun.Sun397):

  def __init__(self, **kwargs):
    tfds_split_files = {
        'tr': os.path.join(_EXAMPLE_DIR, 'sun397_tfds_tr.txt'),
        'te': os.path.join(_EXAMPLE_DIR, 'sun397_tfds_te.txt'),
        'va': os.path.join(_EXAMPLE_DIR, 'sun397_tfds_va.txt'),
    }
    super(TestableSun397, self).__init__(
        tfds_split_files=tfds_split_files, **kwargs)


class Sun397StandardPartitionTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = TestableSun397
  EXAMPLE_DIR = _EXAMPLE_DIR
  BUILDER_CONFIG_NAMES_TO_TEST = ['standard-part1-120k']
  SPLITS = {
      'train': 4,
      'test': 3,
  }


class Sun397TfdsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = TestableSun397
  EXAMPLE_DIR = _EXAMPLE_DIR
  BUILDER_CONFIG_NAMES_TO_TEST = ['tfds']
  SPLITS = {
      'train': 4,
      'test': 2,
      'validation': 2,
  }


if __name__ == '__main__':
  testing.test_main()
