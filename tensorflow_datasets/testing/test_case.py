# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Base TestCase to use test_data."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import tempfile

import tensorflow as tf


class TestCase(tf.test.TestCase):
  """Base TestCase for tests using test_data or tmp_dir.

  `test_data` class attribute: path to the directory with test data.
  `tmp_dir` attribute: path to temp directory reset before every test.
  """

  @classmethod
  def setUpClass(cls):
    cls.test_data = os.path.join(os.path.dirname(__file__), "test_data")

  def setUp(self):
    # get_temp_dir is actually the same for all tests, so create a temp sub-dir.
    self.tmp_dir = tempfile.mkdtemp(dir=tf.test.get_temp_dir())


main = tf.test.main
