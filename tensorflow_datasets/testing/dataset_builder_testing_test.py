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

"""Tests for tensorflow_datasets.testing.dataset_builder_testing."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v2 as tf
from tensorflow_datasets import testing
from tensorflow_datasets.testing.dataset_builder_testing import checksum


class DatasetBuilderTesting(tf.test.TestCase):

  def test_dataset_builder_testing(self):

    # pylint: disable=unreachable
    self.all_checksums = {checksum(tf.constant([b"foo", b"bar"]).numpy()) for _ in range(5)}
    self.assertEqual(len(self.all_checksums), 1)  


if __name__ == '__main__':
  testing.test_main()
