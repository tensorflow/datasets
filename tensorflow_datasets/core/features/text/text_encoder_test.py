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

from absl.testing import parameterized
import tensorflow as tf
from tensorflow_datasets.core import test_utils
from tensorflow_datasets.core.features.text import text_encoder

ZH_HELLO = u'你好 '
EN_HELLO = u'hello '


class ByteTextEncoderTest(tf.test.TestCase):
  # Incremented for pad
  ZH_HELLO_IDS = [i + 1 for i in [228, 189, 160, 229, 165, 189, 32]]
  EN_HELLO_IDS = [i + 1 for i in [104, 101, 108, 108, 111, 32]]

  def test_encode_decode(self):
    encoder = text_encoder.ByteTextEncoder()
    self.assertEqual(self.ZH_HELLO_IDS, encoder.encode(ZH_HELLO))
    self.assertEqual(self.EN_HELLO_IDS, encoder.encode(EN_HELLO))
    self.assertEqual(self.EN_HELLO_IDS, encoder.encode('hello '))
    self.assertEqual(EN_HELLO, encoder.decode(self.EN_HELLO_IDS))
    self.assertEqual(ZH_HELLO, encoder.decode(self.ZH_HELLO_IDS))
    self.assertEqual(2**8 + 1, encoder.vocab_size)


class TokenTextEncoderTest(tf.test.TestCase):

  def test_encode_decode(self):
    encoder = text_encoder.TokenTextEncoder(
        vocab_list=[u'hi', 'bye', ZH_HELLO])
    ids = [i + 1 for i in [0, 1, 2, 0]]
    self.assertEqual(ids, encoder.encode('hi  bye %s hi' % ZH_HELLO))
    self.assertEqual(u'hi bye %shi' % ZH_HELLO, encoder.decode(ids))

  def test_oov(self):
    encoder = text_encoder.TokenTextEncoder(
        vocab_list=[u'hi', 'bye', ZH_HELLO],
        oov_buckets=1,
        oov_token='UNK')
    ids = [i + 1 for i in [0, 3, 3, 1]]
    self.assertEqual(ids, encoder.encode('hi boo foo bye'))
    self.assertEqual('hi UNK UNK bye', encoder.decode(ids))
    self.assertEqual(5, encoder.vocab_size)

  def test_multiple_oov(self):
    encoder = text_encoder.TokenTextEncoder(
        vocab_list=[u'hi', 'bye', ZH_HELLO],
        oov_buckets=2,
        oov_token='UNK')
    encoded = encoder.encode('hi boo zoo too foo bye')
    self.assertEqual(1, encoded[0])
    self.assertEqual(2, encoded[-1])
    self.assertIn(4, encoded)
    self.assertIn(5, encoded)
    self.assertEqual(6, encoder.vocab_size)
    self.assertEqual('hi UNK UNK bye', encoder.decode([1, 4, 5, 2]))

  def test_tokenization(self):
    encoder = text_encoder.TokenTextEncoder(vocab_list=[u'hi', 'bye', ZH_HELLO])
    text = 'hi<<>><<>foo!^* bar && bye (%s hi)' % ZH_HELLO
    self.assertEqual(['hi', 'foo', 'bar', 'bye', ZH_HELLO.strip(), 'hi'],
                     text_encoder.Tokenizer().tokenize(text))
    self.assertEqual([i + 1 for i in [0, 3, 3, 1, 2, 0]], encoder.encode(text))

  def test_file_backed(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      vocab_fname = os.path.join(tmp_dir, 'vocab.tokens')
      encoder = text_encoder.TokenTextEncoder(
          vocab_list=[u'hi', 'bye', ZH_HELLO])
      encoder.store_to_file(vocab_fname)
      file_backed_encoder = text_encoder.TokenTextEncoder(
          vocab_file=vocab_fname)
      self.assertEqual(encoder.tokens, file_backed_encoder.tokens)


class TokenizeTest(parameterized.TestCase, tf.test.TestCase):

  def test_default(self):
    text = 'hi<<>><<>foo!^* bar &&  bye (%s hi)' % ZH_HELLO
    self.assertEqual(['hi', 'foo', 'bar', 'bye', ZH_HELLO.strip(), 'hi'],
                     text_encoder.Tokenizer().tokenize(text))

  def test_with_nonalphanum(self):
    text = 'hi world<<>><<>foo!^* bar &&  bye (%s hi)' % ZH_HELLO
    tokens = [
        'hi', ' ', 'world', '<<>><<>', 'foo', '!^* ', 'bar', ' &&  ', 'bye',
        ' (', ZH_HELLO.strip(), '  ', 'hi', ')'
    ]
    tokenizer = text_encoder.Tokenizer(alphanum_only=False)
    self.assertEqual(
        tokens, tokenizer.tokenize(text))
    self.assertEqual(
        text, tokenizer.join(tokenizer.tokenize(text)))

  @parameterized.parameters(
      # Single Space at at beginning
      (' hello world', [' ', 'hello', ' ', 'world']),
      (' !hello world', [' !', 'hello', ' ', 'world']),
      # Single space at end
      ('hello world ', ['hello', ' ', 'world', ' ']),
      ('hello world! ', ['hello', ' ', 'world', '! ']),
      # Double space at beginning
      ('  hello world', ['  ', 'hello', ' ', 'world']),
      ('  !hello world', ['  !', 'hello', ' ', 'world']),
      # Double space in middle
      ('hello  world', ['hello', '  ', 'world']),
      ('hello!  world', ['hello', '!  ', 'world']),
      ('hello  !world', ['hello', '  !', 'world']),
  )
  def test_whitespace(self, s, exp):
    tokenizer = text_encoder.Tokenizer(alphanum_only=False)
    self.assertEqual(exp, tokenizer.tokenize(s))
    self.assertEqual(s, tokenizer.join(tokenizer.tokenize(s)))

  def test_reserved_tokens(self):
    text = u'hello worldbar bar foozoo zoo FOO<EOS>'
    tokens = ['hello', ' ', 'world', 'bar', ' ', 'bar', ' ', 'foozoo',
              ' ', 'zoo', ' ', 'FOO', '<EOS>']
    tokenizer = text_encoder.Tokenizer(alphanum_only=False,
                                       reserved_tokens=['<EOS>', 'FOO', 'bar'])
    self.assertEqual(tokens, tokenizer.tokenize(text))
    self.assertEqual(text, tokenizer.join(tokenizer.tokenize(text)))


if __name__ == '__main__':
  tf.test.main()
