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
"""Tests for tensorflow_datasets.core.features.text.text_encoder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf
from tensorflow_datasets.core import test_utils
from tensorflow_datasets.core.features.text import text_encoder

CN_HELLO = u'你好 '
EN_HELLO = u'hello '


class ByteTextEncoderTest(tf.test.TestCase):
  CN_HELLO_IDS = [228, 189, 160, 229, 165, 189, 32]
  EN_HELLO_IDS = [104, 101, 108, 108, 111, 32]

  def test_encode_decode(self):
    encoder = text_encoder.ByteTextEncoder()
    self.assertEqual(self.CN_HELLO_IDS, encoder.encode(CN_HELLO))
    self.assertEqual(self.EN_HELLO_IDS, encoder.encode(EN_HELLO))
    self.assertEqual(self.EN_HELLO_IDS, encoder.encode('hello '))
    self.assertEqual(EN_HELLO, encoder.decode(self.EN_HELLO_IDS))
    self.assertEqual(CN_HELLO, encoder.decode(self.CN_HELLO_IDS))
    self.assertEqual(2**8, encoder.vocab_size)


class TokenTextEncoderTest(tf.test.TestCase):

  def test_encode_decode(self):
    encoder = text_encoder.TokenTextEncoder(
        vocab_list=[u'hi', 'bye', CN_HELLO])
    ids = [0, 1, 2, 0]
    self.assertEqual(ids, encoder.encode('hi  bye %s hi' % CN_HELLO))
    self.assertEqual(u'hi bye %shi' % CN_HELLO, encoder.decode(ids))

  def test_oov(self):
    encoder = text_encoder.TokenTextEncoder(
        vocab_list=[u'hi', 'bye', CN_HELLO],
        oov_buckets=1,
        oov_token='UNK')
    self.assertEqual([0, 3, 3, 1], encoder.encode('hi boo foo bye'))
    self.assertEqual('hi UNK UNK bye', encoder.decode([0, 3, 3, 1]))
    self.assertEqual(4, encoder.vocab_size)

  def test_multiple_oov(self):
    encoder = text_encoder.TokenTextEncoder(
        vocab_list=[u'hi', 'bye', CN_HELLO],
        oov_buckets=2,
        oov_token='UNK')
    encoded = encoder.encode('hi boo zoo too foo bye')
    self.assertEqual(0, encoded[0])
    self.assertEqual(1, encoded[-1])
    self.assertIn(3, encoded)
    self.assertIn(4, encoded)
    self.assertEqual(5, encoder.vocab_size)
    self.assertEqual('hi UNK UNK bye', encoder.decode([0, 3, 4, 1]))

  def test_tokenization(self):
    encoder = text_encoder.TokenTextEncoder(vocab_list=[u'hi', 'bye', CN_HELLO])
    text = 'hi<<>><<>foo!^* bar && bye (%s hi)' % CN_HELLO
    self.assertEqual(['hi', 'foo', 'bar', 'bye', CN_HELLO.strip(), 'hi'],
                     text_encoder.tokenize(text))
    self.assertEqual([0, 3, 3, 1, 2, 0], encoder.encode(text))

  def test_file_backed(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      vocab_fname = os.path.join(tmp_dir, 'vocab.tokens')
      encoder = text_encoder.TokenTextEncoder(
          vocab_list=[u'hi', 'bye', CN_HELLO])
      encoder.store_to_file(vocab_fname)
      file_backed_encoder = text_encoder.TokenTextEncoder(
          vocab_file=vocab_fname)
      self.assertEqual(encoder.tokens, file_backed_encoder.tokens)


if __name__ == '__main__':
  tf.test.main()
