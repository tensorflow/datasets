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
"""Tests for tensorflow_datasets.core.registered."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow_datasets as tfds

_TEST_DATASETS = set(["dummy_mnist", "dummy_dataset_shared_generator"])

class ListBuilderTest(tfds.testing.TestCase):

  def test_list_builder(self):
    registered_datasets = set(tfds.list_builders())
    self.assertEmpty(_TEST_DATASETS.intersection(registered_datasets),
                     "List of Registered datasets should not contain {}"
                     .format(_TEST_DATASETS)
                    )

if __name__ == "__main__":
  tfds.testing.test_main()
