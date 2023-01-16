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

"""Tests for SUN (Scene UNderstanding) datasets."""

import os

from tensorflow_datasets import testing
from tensorflow_datasets.datasets.sun397 import sun397_dataset_builder

_EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), 'dummy_data')

# Could use functools.partialmethod in Python3
original_init = sun397_dataset_builder.Builder.__init__


def new_init(self, tfds_split_files=None, **kwargs):
  assert tfds_split_files is None
  original_init(
      self,
      tfds_split_files={
          'tr': os.path.join(_EXAMPLE_DIR, 'sun397_tfds_tr.txt'),
          'te': os.path.join(_EXAMPLE_DIR, 'sun397_tfds_te.txt'),
          'va': os.path.join(_EXAMPLE_DIR, 'sun397_tfds_va.txt'),
      },
      **kwargs,
  )


# Patch init to add init arguments without changing the class.__name__ and
# registration reguired to find the checksum file.
sun397_dataset_builder.Builder.__init__ = new_init


class Sun397StandardPartitionTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = sun397_dataset_builder.Builder
  EXAMPLE_DIR = _EXAMPLE_DIR
  BUILDER_CONFIG_NAMES_TO_TEST = ['standard-part1-120k']
  SPLITS = {
      'train': 4,
      'test': 3,
  }


class Sun397TfdsTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = sun397_dataset_builder.Builder
  EXAMPLE_DIR = _EXAMPLE_DIR
  BUILDER_CONFIG_NAMES_TO_TEST = ['tfds']
  SPLITS = {
      'train': 4,
      'test': 2,
      'validation': 2,
  }


if __name__ == '__main__':
  testing.test_main()
