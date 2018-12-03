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

"""Tests for tensorflow_datasets.core.download.download_manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import os

import tensorflow as tf

from tensorflow_datasets.core.download import util
from tensorflow_datasets.testing import test_case


class ReadChecksumDigestTest(test_case.TestCase):

  def test_digest(self):
    digest = util.read_checksum_digest(
        os.path.join(self.test_data, '6pixels.png'), hashlib.sha256)
    self.assertEqual(
        digest,
        '04f38ebed34d3b027d2683193766155912fba647158c583c3bdb4597ad8af34c')


if __name__ == '__main__':
  tf.test.main()
