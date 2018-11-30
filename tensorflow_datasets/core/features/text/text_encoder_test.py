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
from tensorflow_datasets.core.features.text import subword_text_encoder
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
    self.assertEqual(text_encoder.NUM_BYTES + 1, encoder.vocab_size)

  def test_additional_tokens(self):
    # One with non-alphanumeric chars, one uppercase, one lowercase
    additional_tokens = ['<EOS>', 'FOO', 'bar']
    encoder = text_encoder.ByteTextEncoder(additional_tokens=additional_tokens)
    # Without additional tokens
    hello_ids = [i + len(additional_tokens) for i in self.ZH_HELLO_IDS]
    self.assertEqual(hello_ids, encoder.encode(ZH_HELLO))
    # With additional tokens
    text_additional = '%s %s%s%s' % (additional_tokens[0], ZH_HELLO,
                                     additional_tokens[1], additional_tokens[2])
    self.assertEqual([1, 32 + 1 + len(additional_tokens)] + hello_ids + [2, 3],
                     encoder.encode(text_additional))
    self.assertEqual(text_encoder.NUM_BYTES + 1 + len(additional_tokens),
                     encoder.vocab_size)


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
    text = u'hi<<>><<>foo!^* bar && bye (%s hi)' % ZH_HELLO
    self.assertEqual([u'hi', u'foo', u'bar', u'bye',
                      ZH_HELLO.strip(), u'hi'],
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

  def test_mixedalphanum_tokens(self):
    mixed_tokens = ['<EOS>', 'zoo!', '!foo']
    vocab_list = mixed_tokens + [u'hi', 'bye', ZH_HELLO]

    encoder = text_encoder.TokenTextEncoder(vocab_list=vocab_list)

    # No mixed tokens
    text = 'hi<<>><<>foo!^* bar && bye (%s hi)' % ZH_HELLO
    # hi=3, foo=OOV, bar=OOV, bye=4, ZH_HELLO=5, hi=3
    text_ids = [i + 1 for i in [3, 6, 6, 4, 5, 3]]
    self.assertEqual(text_ids, encoder.encode(text))

    # With mixed tokens
    text = 'hi<<>><<>foo!<EOS>^* barzoo! FOO && bye (%s hi)' % ZH_HELLO
    # hi=3, foo=OOV, <EOS>=0, bar=OOV, zoo!=1, FOO=OOV, bye=4, ZH_HELLO=5, hi=3
    text_ids = [i + 1 for i in [3, 6, 0, 6, 1, 6, 4, 5, 3]]
    self.assertEqual(text_ids, encoder.encode(text))

  def test_lowercase(self):
    mixed_tokens = ['<EOS>', 'zoo!']
    vocab_list = mixed_tokens + [u'hi', 'bye', ZH_HELLO]
    encoder = text_encoder.TokenTextEncoder(
        vocab_list=vocab_list, lowercase=True)
    # No mixed tokens
    self.assertEqual([3, 4, 3], encoder.encode('hi byE HI!'))
    # With mixed tokens
    self.assertEqual([3, 1, 4, 2, 3], encoder.encode('hi<EOS>byE Zoo! HI!'))

  def test_with_tokenizer(self):

    class DummyTokenizer(object):

      def tokenize(self, s):
        del s
        return ['hi', 'bye']

    tokenizer = DummyTokenizer()
    vocab_list = [u'hi', 'bye', ZH_HELLO]
    encoder = text_encoder.TokenTextEncoder(
        vocab_list=vocab_list, tokenizer=tokenizer)
    # Ensure it uses the passed tokenizer and not the default
    self.assertEqual([1, 2], encoder.encode('zoo foo'))


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


class SubwordTextEncoderTest(parameterized.TestCase, tf.test.TestCase):

  def setUp(self):
    super(SubwordTextEncoderTest, self).setUp()
    # Vocab ids will be (offset for pad=0):
    #                  1       2       3      4      5
    self.vocab_list = ['foo_', 'bar_', 'foo', 'bar', '<EOS>']
    self.encoder = subword_text_encoder.SubwordTextEncoder(
        vocab_list=self.vocab_list)

  def test_vocab_size(self):
    # Bytes + pad + subwords
    self.assertEqual((256 + 1 + len(self.vocab_list)), self.encoder.vocab_size)

  @parameterized.parameters(
      (u'foo bar', [1, 4]),
      (u'foobar foo bar<EOS>bar', [3, 2, 1, 4, 5, 4]),
      # Respects whitespace
      (u'bar <EOS>bar', [2, 5, 4]),
      (u'bar <EOS> bar', [2, 5, 38, 4]),
      (u'bar<EOS> bar', [4, 5, 38, 4]),
      # Invertible even with oov, respecting underscores and backslashes
      (u'a_b!', [103, 101, 104, 39]),
      (u'foo \\bar_!', [3, 38, 98, 4, 101, 39]),
      (u'foo \\\\bar_!', [3, 38, 98, 98, 4, 101, 39]),
      (u'hello world!', None),
      (u'foo_ bar', None),
      (u'foo _ bar', None),
      (u'foo _bar', None),
      (u'hello_world', None),
      (u'hello_ world', None),
      (u'hello _ world', None),
      (u'hello _world', None),
      (u'_', None),
      # Test that the underscore replacement string is unharmed
      (u'\\&undsc', None),
      # Unicode encoded as bytes but decoded back to unicode character
      (u'你', [234, 195, 166]),
  )
  def test_encode_decode(self, text, expected_ids):
    ids = self.encoder.encode(text)
    # Test ids match if ids provided
    if expected_ids:
      self.assertEqual(expected_ids, ids)
    # Test invertibility
    self.assertEqual(tf.compat.as_text(text), self.encoder.decode(ids))

  def test_bad_bytes(self):
    valid_unicode = u'你'
    bad_bytes = [220 + len(self.vocab_list) + 1]
    bad_ids = self.encoder.encode(u'你') + bad_bytes
    text = self.encoder.decode(bad_ids)
    # Valid unicode character preserved
    self.assertEqual(valid_unicode, text[0])
    # Invalid byte converted to unknown character
    self.assertEqual(u'\uFFFD', text[1])

  def test_vocab_file(self):
    vocab_file = os.path.join(self.get_temp_dir(), 'vocab.subwords')
    self.encoder.store_to_file(vocab_file)
    encoder = subword_text_encoder.SubwordTextEncoder(vocab_file=vocab_file)
    self.assertEqual(encoder.subwords, self.vocab_list)


if __name__ == '__main__':
  tf.test.main()
