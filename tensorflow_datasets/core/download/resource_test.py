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

"""Tests for resource module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core.download import resource

NO_EXTRACT = resource.ExtractMethod.NO_EXTRACT
TAR = resource.ExtractMethod.TAR
TAR_GZ = resource.ExtractMethod.TAR_GZ
GZIP = resource.ExtractMethod.GZIP
ZIP = resource.ExtractMethod.ZIP


class GuessExtractMethodTest(tf.test.TestCase):

  def test_(self):
    for fname, expected_result in [
        ('bar.tar.gz', TAR_GZ),
        ('bar.gz', GZIP),
        ('bar.tar.zip', ZIP),
        ('bar.gz.strange', NO_EXTRACT),
        ('bar.tar', TAR),
    ]:
      res = resource._guess_extract_method(fname)
      self.assertEqual(res, expected_result, '(%s)->%s instead of %s' % (
          fname, res, expected_result))


if __name__ == '__main__':
  tf.test.main()
