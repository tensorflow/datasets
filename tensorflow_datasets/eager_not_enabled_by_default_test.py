# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Tests for checking that eager isn't enabled by default on importing tfds."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

import tensorflow_datasets as tfds  # pylint: disable=unused-import


class EagerNotEnabledByDefaultTest(tf.test.TestCase):

  def test_eager_is_not_enabled_by_default(self):
    self.assertFalse(tf.executing_eagerly())


if __name__ == '__main__':
  tf.test.main()
