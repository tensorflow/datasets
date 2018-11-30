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
"""SubwordTextEncoder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import six
import tensorflow as tf

from tensorflow_datasets.core.features.text import text_encoder

# Internally, an underscore indicates a single space, so, to ensure
# user-supplied underscores are encoded properly, they are replaced with this
# string during encoding.
_UNDERSCORE_REPLACEMENT = u"\\&undsc"


class SubwordTextEncoder(text_encoder.TextEncoder):
  """Invertible `TextEncoder` using word pieces with a byte-level fallback.

  Encoding is fully invertible because all out-of-vocab wordpieces are
  byte-encoded.

  The vocabulary is "trained" on a corpus and all wordpieces are stored in a
  vocabulary file. To generate a vocabulary from a corpus, use
  `tfds.features.text.SubwordTextEncoder.build_from_corpus`.
  """

  def __init__(self, vocab_file=None, vocab_list=None):
    r"""Constructs a SubwordTextEncoder from a vocabulary file or list.

    Note: To generate a vocabulary from a corpus, use
    `tfds.features.text.SubwordTextEncoder.build_from_corpus`.

    Args:
      vocab_file: `str`, path to vocabulary file produced by
        `SubwordTextEncoder.store_to_file`.
      vocab_list: `list<str>`, list of subwords for the vocabulary. Note that an
        underscore at the end of a subword indicates the end of the word (i.e. a
        space will be inserted afterwards when decoding). Underscores in the
        interior are disallowed and should use the underscore escape sequence
        "\u".
    """
    if not (vocab_list or vocab_file) or (vocab_list and vocab_file):
      raise ValueError("Must provide either vocab_list or vocab_file.")
    if vocab_file:
      vocab_list = self._vocab_list_from_file(vocab_file)
    self._init_from_list(vocab_list)

  def encode(self, s):
    """Encodes text into a list of integers."""
    s = tf.compat.as_text(s)
    tokens = self._tokenizer.tokenize(s)

    def _encode_token(t, next_t):
      skip_next = False
      t = _escape(t)
      # If next token is a single space, add _ suffix to token and skip the
      # empty space.
      if next_t == u" ":
        t += u"_"
        skip_next = True
      t_ids = self._token_to_ids(t)
      return t_ids, skip_next

    ids = []
    next_tokens = tokens[1:] + [None]
    skip_single_token = False
    for token, next_token in zip(tokens, next_tokens):
      if skip_single_token:
        skip_single_token = False
        continue

      # If the user-supplied string contains the underscore replacement string,
      # break it into 2 tokens and encode those separately.
      if token == _UNDERSCORE_REPLACEMENT:
        t1, t2 = _UNDERSCORE_REPLACEMENT[:2], _UNDERSCORE_REPLACEMENT[2:]
        t1_ids, _ = _encode_token(t1, None)
        t2_ids, _ = _encode_token(t2, next_token)
        ids.extend(t1_ids)
        ids.extend(t2_ids)
        continue

      t_ids, skip_single_token = _encode_token(token, next_token)
      ids.extend(t_ids)
    return text_encoder.pad_incr(ids)

  def decode(self, ids):
    """Decodes a list of integers into text."""
    ids = text_encoder.pad_decr(ids)
    subword_ids = ids

    subwords = []

    # Some ids correspond to bytes. Because unicode characters are composed of
    # possibly multiple bytes, we attempt to decode contiguous lists of bytes
    # all together. Invalid byte sequences are replaced with the unicode
    # replacement (i.e. unknown) character U+FFFD.
    prev_bytes = []

    def consume_prev_bytes():
      if prev_bytes:
        bytestr = b"".join(prev_bytes)
        bytes_text = bytestr.decode("utf-8", "replace")
        subwords.append(bytes_text)
      return []

    for subword_id in subword_ids:
      subword = self._id_to_subword(subword_id)
      if isinstance(subword, six.binary_type):
        # Byte-encoded
        prev_bytes.append(subword)
      else:
        # If there were bytes previously, convert to unicode.
        prev_bytes = consume_prev_bytes()
        trimmed, add_space = _trim_underscore_and_tell(subword)
        subwords.append(trimmed)
        if add_space:
          subwords.append(" ")
    # If there were trailing bytes, convert to unicode.
    prev_bytes = consume_prev_bytes()

    return u"".join(subwords)

  @property
  def vocab_size(self):
    # Vocab is:
    # * pad=0
    # * subwords
    # * bytes
    return 1 + len(self._subwords) + text_encoder.NUM_BYTES

  @property
  def subwords(self):
    return list(self._subwords)

  def _token_to_ids(self, token):
    """Convert a single token to a list of integer ids."""
    # Check cache
    cache_location = hash(token) % self._cache_size
    cache_key, cache_value = self._token_to_ids_cache[cache_location]
    if cache_key == token:
      return cache_value

    subwords = self._token_to_subwords(token)
    ids = []
    for subword in subwords:
      if subword == _UNDERSCORE_REPLACEMENT:
        ids.append(len(self._subwords) + ord(u"_"))
        continue
      subword_id = self._subword_to_id.get(subword)
      if subword_id is None:
        # Byte-encode
        ids.extend(self._byte_encode(subword))
      else:
        ids.append(subword_id)

    # Update cache
    self._token_to_ids_cache[cache_location] = (token, ids)

    return ids

  def _byte_encode(self, token):
    """Encode a single token byte-wise into integer ids."""
    # Vocab ids for all bytes follow ids for the subwords
    offset = len(self._subwords)
    if token == u"_":
      return [len(self._subwords) + ord(u" ")]
    return [i + offset for i in list(bytearray(tf.compat.as_bytes(token)))]

  def _id_to_subword(self, subword_id):
    """Converts a subword integer ID to a subword string."""
    if subword_id < 0 or subword_id >= (self.vocab_size - 1):
      raise ValueError("Received id %d which is invalid. Ids must be within "
                       "[0, %d)." % (subword_id + 1, self.vocab_size))

    if 0 <= subword_id < len(self._subwords):
      # Subword
      return self._subwords[subword_id]
    else:
      # Byte
      offset = len(self._subwords)
      subword_id -= offset
      bytestr = bytes(bytearray([subword_id]))
      return bytestr

  def _token_to_subwords(self, token):
    """Greedily split token into subwords."""
    subwords = []

    start = 0
    while start < len(token):
      subword = None
      for end in range(
          min(len(token), start + self._max_subword_len), start, -1):
        candidate = token[start:end]
        if (candidate in self._subword_to_id or
            candidate == _UNDERSCORE_REPLACEMENT):
          subword = candidate
          subwords.append(subword)
          start = end
          break
      # No subword match found. Consume a single (unicode) character.
      if subword is None:
        subwords.append(token[start])
        start += 1

    return subwords

  def _init_from_list(self, subwords):
    """Initializes the encoder from a list of subwords."""
    subwords = [tf.compat.as_text(s) for s in subwords if s]
    self._subwords = subwords
    # Note that internally everything is 0-indexed. Padding is dealt with at the
    # end of encode and the beginning of decode.
    self._subword_to_id = {s: i for i, s in enumerate(subwords)}

    # We remember the maximum length of any subword to avoid having to
    # check arbitrarily long strings.
    self._max_subword_len = max(
        len(_UNDERSCORE_REPLACEMENT), max([len(s) for s in subwords]))

    # Initialize the cache
    self._cache_size = 2**20
    self._token_to_ids_cache = [(None, None)] * self._cache_size

    # Setup tokenizer
    # Reserved tokens are all tokens that are mixed alphanum and non-alphanum.
    reserved_tokens = [_UNDERSCORE_REPLACEMENT]
    for t in self._subwords:
      t = _trim_underscore(t)
      if text_encoder.is_mixed_alphanum(t):
        reserved_tokens.append(t)
    self._tokenizer = text_encoder.Tokenizer(
        alphanum_only=False, reserved_tokens=reserved_tokens)

  def _vocab_list_from_file(self, filename):
    """Extracts list of subwords from file."""
    if not tf.gfile.Exists(filename):
      raise ValueError("Vocab file not found: %s" % filename)
    with tf.gfile.Open(filename) as f:
      # Strip wrapping single quotes and newline
      vocab_list = [line[1:-2] for line in f]
      return vocab_list

  def store_to_file(self, filename):
    """Save the vocabulary to a file."""
    with tf.gfile.Open(filename, "wb") as f:
      for subword in self._subwords:
        # Wrap in single quotes to make it easier to see the full subword when
        # it has spaces and make it easier to search with ctrl+f.
        f.write(tf.compat.as_bytes(u"'"))
        f.write(tf.compat.as_bytes(subword))
        f.write(tf.compat.as_bytes(u"'"))
        f.write(tf.compat.as_bytes(u"\n"))

  @classmethod
  def build_from_corpus(cls,
                        corpus_generator,
                        target_vocab_size,
                        max_subword_length=None,
                        reserved_tokens=None):
    """Builds a `SubwordTextEncoder` based on the `corpus_generator`.

    Args:
      corpus_generator: generator yielding `str`.
      target_vocab_size: `int`, approximate size of the vocabulary to create.
      max_subword_length: `int`, maxmimum length of a subword. Note that memory
        and compute scale quadratically in the length of the longest token.
      reserved_tokens: `list<str>`, list of tokens that will always be treated
        as whole tokens and not split up. Note that these must contain a mix of
        alphanumeric and non-alphanumeric characters (e.g. "<EOS>").

    Returns:
      `SubwordTextEncoder`.
    """
    raise NotImplementedError


def _trim_underscore(token):
  if token.endswith(u"_"):
    return token[:-1]
  return token


def _trim_underscore_and_tell(token):
  if token.endswith(u"_"):
    return token[:-1], True
  return token, False


def _escape(s):
  return s.replace(u"_", _UNDERSCORE_REPLACEMENT)


def _unescape(s):
  return s.replace(_UNDERSCORE_REPLACEMENT, u"_")
