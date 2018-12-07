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
from tensorflow_datasets.core.features.text import text_encoder


class TextFeatureTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):
    nonunicode_text = 'hello world'
    unicode_text = u'你好'
    return [
        test_utils.FeatureExpectation(
            name='text',
            feature=features.Text(),
            shape=(),
            dtype=tf.string,
            tests=[
                # Non-unicode
                test_utils.FeatureExpectationItem(
                    value=nonunicode_text,
                    expected=tf.compat.as_bytes(nonunicode_text),
                ),
                # Unicode
                test_utils.FeatureExpectationItem(
                    value=unicode_text,
                    expected=tf.compat.as_bytes(unicode_text),
                ),
            ],
        ),
        # Unicode integer-encoded by byte
        test_utils.FeatureExpectation(
            name='text_unicode_encoded',
            feature=features.Text(encoder=text_encoder.ByteTextEncoder()),
            shape=(None,),
            dtype=tf.int64,
            tests=[
                test_utils.FeatureExpectationItem(
                    value=unicode_text,
                    expected=[i + 1 for i in [228, 189, 160, 229, 165, 189]],
                ),
            ],
        ),
    ]

  def test_text_conversion(self):
    text_f = features.Text(encoder=text_encoder.ByteTextEncoder())
    text = u'你好'
    self.assertEqual(text, text_f.ints2str(text_f.str2ints(text)))

  def test_save_load_metadata(self):
    text_f = features.Text(
        encoder=text_encoder.ByteTextEncoder(additional_tokens=['HI']))
    text = u'HI 你好'
    ids = text_f.str2ints(text)
    self.assertEqual(1, ids[0])

    with test_utils.tmp_dir(self.get_temp_dir()) as data_dir:
      feature_name = 'dummy'
      text_f.save_metadata(data_dir, feature_name)

      new_f = features.Text()
      new_f.load_metadata(data_dir, feature_name)
      self.assertEqual(ids, text_f.str2ints(text))


if __name__ == '__main__':
  tf.test.main()
