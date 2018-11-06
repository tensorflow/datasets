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

# coding=utf-8
"""Tests for tensorflow_datasets.core.features.text_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core import features
from tensorflow_datasets.core import test_utils


class TextFeatureTest(tf.test.TestCase):

  @tf.contrib.eager.run_test_in_graph_and_eager_modes()
  def test_encode_decode(self):
    nonunicode_text = 'hello world'
    unicode_text = u'你好，世界'
    expectations = [
        # Non-unicode
        test_utils.FeatureExpectation(
            name='text',
            feature=features.Text(),
            value=nonunicode_text,
            expected=tf.compat.as_bytes(nonunicode_text)),
        # Unicode
        test_utils.FeatureExpectation(
            name='text_unicode',
            feature=features.Text(),
            value=unicode_text,
            expected=tf.compat.as_bytes(unicode_text)),
    ]

    specs = features.SpecDict({exp.name: exp.feature for exp in expectations})

    decoded_sample = test_utils.features_encode_decode(
        specs, dict([(exp.name, exp.value) for exp in expectations]))

    for exp in expectations:
      self.assertAllEqual(decoded_sample[exp.name], exp.expected)
      # TODO(rsepassi): test shape and dtype against exp.feature


if __name__ == '__main__':
  tf.test.main()
