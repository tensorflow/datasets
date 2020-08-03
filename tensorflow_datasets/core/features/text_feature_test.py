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

# coding=utf-8
"""Tests for tensorflow_datasets.core.features.text_feature."""

import tensorflow.compat.v2 as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import features

tf.enable_v2_behavior()


class TextFeatureTest(testing.FeatureExpectationsTestCase):

  def test_text(self):
    nonunicode_text = 'hello world'
    unicode_text = u'你好'

    self.assertFeature(
        feature=features.Text(),
        shape=(),
        dtype=tf.string,
        tests=[
            # Non-unicode
            testing.FeatureExpectationItem(
                value=nonunicode_text,
                expected=tf.compat.as_bytes(nonunicode_text),
            ),
            # Unicode
            testing.FeatureExpectationItem(
                value=unicode_text,
                expected=tf.compat.as_bytes(unicode_text),
            ),
            # Empty string
            testing.FeatureExpectationItem(
                value='',
                expected=tf.compat.as_bytes(''),
            ),
        ],
    )


if __name__ == '__main__':
  testing.test_main()
