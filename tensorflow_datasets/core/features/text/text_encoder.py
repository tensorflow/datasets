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
"""TextEncoders convert between text and integers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import hashlib
import re

import six
import tensorflow as tf


ALPHANUM_REGEX = re.compile(r"\W+", flags=re.UNICODE)
ALL_REGEX = re.compile(r"(\W+)", flags=re.UNICODE)
NUM_BYTES = 2**8


@six.add_metaclass(abc.ABCMeta)
class TextEncoder(object):
  """Abstract base class for converting between text and integers.

  **A note on padding**:

    Because text data is typically variable length and nearly always requires
    padding during training, ID 0 is always reserved for padding. To accommodate
    this, all `TextEncoder`s behave in certain ways:

    * `encode`: never returns id 0 (all ids are 1+)
    * `decode`: drops 0 in the input ids
    * `vocab_size`: includes ID 0

    New subclasses should be careful to match this behavior.
  """

  @abc.abstractmethod
  def encode(self, s):
    """Encodes text into a list of integers."""
    raise NotImplementedError

  @abc.abstractmethod
  def decode(self, ids):
    """Decodes a list of integers into text."""
    raise NotImplementedError

  @abc.abstractproperty
  def vocab_size(self):
    raise NotImplementedError


class ByteTextEncoder(TextEncoder):
  """Byte-encodes text."""

  def __init__(self, additional_tokens=None):
    """Constructs ByteTextEncoder.

    Args:
      additional_tokens: `list<str>`, list of additional tokens. These will be
        assigned vocab ids `[1, 1+len(additional_tokens)]`. Useful for things
        like "end-of-string" tokens (e.g. "<EOS>").
    """
    self._additional_tokens, self._additional_tokens_re = (
        _prepare_reserved_tokens(additional_tokens))
    # Note that internally everything is 0-indexed. Padding is dealt with at the
    # end of encode and the beginning of decode.
    self._additional_token_to_id = dict(
        zip(self._additional_tokens, range(len(self._additional_tokens))))

  def encode(self, s):
    if not self.additional_tokens:
      return pad_incr(list(bytearray(tf.compat.as_bytes(s))))

    # Handle additional tokens
    s = tf.compat.as_text(s)
    ids = []
    for substr in self._additional_tokens_re.split(s):
      if not substr:
        continue
      tok_id = self._additional_token_to_id.get(substr)
      if tok_id is None:
        offset = len(self.additional_tokens)
        tok_ids = [i + offset for i in
                   list(bytearray(tf.compat.as_bytes(substr)))]
      else:
        tok_ids = [tok_id]
      ids.extend(tok_ids)

    return pad_incr(ids)

  def decode(self, ids):
    ids = pad_decr(ids)
    return tf.compat.as_text(bytes(bytearray(ids)))

  @property
  def vocab_size(self):
    # Plus 1 for pad
    return len(self.additional_tokens) + NUM_BYTES + 1

  @property
  def additional_tokens(self):
    return self._additional_tokens


class TokenTextEncoder(TextEncoder):
  r"""TextEncoder backed by a list of tokens.

  Tokenization splits on (and drops) non-alphanumeric characters with
  regex "\W+".
  """

  def __init__(self,
               vocab_list=None,
               vocab_file=None,
               oov_buckets=1,
               oov_token=u"UNK",
               lowercase=False,
               tokenizer=None):
    """Constructs a TokenTextEncoder.

    Must pass either `vocab_list` or `vocab_file`.

    Args:
      vocab_list: `list<str>`, list of tokens.
      vocab_file: `str`, filepath with 1 token per line.
      oov_buckets: `int`, the number of `int`s to reserve for OOV hash buckets.
        Tokens that are OOV will be hash-modded into a OOV bucket in `encode`.
      oov_token: `str`, the string to use for OOV ids in `decode`.
      lowercase: `bool`, whether to make all text and tokens lowercase.
      tokenizer: `Tokenizer`, responsible for converting incoming text into a
        list of tokens.
    """
    if not (vocab_list or vocab_file) or (vocab_list and vocab_file):
      raise ValueError("Must provide either vocab_list or vocab_file.")
    self._vocab_list = [
        tf.compat.as_text(el).strip() for el in
        vocab_list or self._load_tokens_from_file(vocab_file)
    ]
    self._lowercase = lowercase
    if self._lowercase:
      self._vocab_list = [t.lower() for t in self._vocab_list]
    # Note that internally everything is 0-indexed. Padding is dealt with at the
    # end of encode and the beginning of decode.
    self._token_to_id = dict(
        zip(self._vocab_list, range(len(self._vocab_list))))
    self._oov_buckets = oov_buckets
    self._oov_token = tf.compat.as_text(oov_token)

    # Reserved tokens are all tokens that are mixed alphanum and non-alphanum.
    reserved_tokens = [t for t in self._vocab_list if is_mixed_alphanum(t)]
    self._tokenizer = (tokenizer or Tokenizer(reserved_tokens=reserved_tokens))

  def encode(self, s):
    s = tf.compat.as_text(s)
    if self.lowercase:
      s = s.lower()
    ids = []
    for token in self._tokenizer.tokenize(s):
      int_id = self._token_to_id.get(token, -1)
      if int_id < 0:
        int_id = self._oov_bucket(token)
        if int_id is None:
          raise ValueError("Out of vocabulary token %s" % token)
      ids.append(int_id)

    # Increment for pad id 0
    return pad_incr(ids)

  def decode(self, ids):
    ids = pad_decr(ids)

    tokens = []
    for int_id in ids:
      if int_id < len(self._vocab_list):
        tokens.append(self._vocab_list[int_id])
      else:
        tokens.append(self._oov_token)
    return u" ".join(tokens)

  @property
  def vocab_size(self):
    # Plus 1 for pad
    return len(self._vocab_list) + self._oov_buckets + 1

  @property
  def tokens(self):
    return list(self._vocab_list)

  @property
  def lowercase(self):
    return self._lowercase

  @property
  def tokenizer(self):
    return self._tokenizer

  def store_to_file(self, fname):
    with tf.gfile.Open(fname, "wb") as f:
      f.write(tf.compat.as_bytes(u"\n".join(self._vocab_list)))

  def _oov_bucket(self, token):
    if self._oov_buckets <= 0:
      return None
    if self._oov_buckets == 1:
      return len(self._vocab_list)
    hash_val = int(hashlib.md5(tf.compat.as_bytes(token)).hexdigest(), 16)
    return len(self._vocab_list) + hash_val % self._oov_buckets

  def _load_tokens_from_file(self, fname):
    with tf.gfile.Open(fname, "rb") as f:
      return [el.strip() for el in tf.compat.as_text(f.read()).split(u"\n")]


class Tokenizer(object):
  """Splits a string into tokens, and joins them back."""

  def __init__(self, alphanum_only=True, reserved_tokens=None):
    """Constructs a Tokenizer.

    Note that the Tokenizer is invertible if `alphanum_only=False`.
    i.e. `s == t.join(t.tokenize(s))`.

    Args:
      alphanum_only: `bool`, if `True`, only parse out alphanumeric tokens
        (non-alphanumeric characters are dropped);
        otherwise, keep all characters (individual tokens will still be either
        all alphanumeric or all non-alphanumeric).
      reserved_tokens: `list<str>`, a list of strings that, if any are in `s`,
        will be preserved as whole tokens, even if they contain mixed
        alphnumeric/non-alphanumeric characters.
    """
    self._alphanum_only = alphanum_only
    reserved_tokens, self._reserved_tokens_re = _prepare_reserved_tokens(
        reserved_tokens)
    self._reserved_tokens = set(reserved_tokens)
    self._alphanum_re = ALPHANUM_REGEX if self._alphanum_only else ALL_REGEX

  @property
  def alphanum_only(self):
    return self._alphanum_only

  @property
  def reserved_tokens(self):
    return self._reserved_tokens

  def tokenize(self, s):
    """Splits a string into tokens."""
    s = tf.compat.as_text(s)

    if self.reserved_tokens:
      # First split out the reserved tokens
      substrs = self._reserved_tokens_re.split(s)
    else:
      substrs = [s]

    toks = []
    for substr in substrs:
      if substr in self.reserved_tokens:
        toks.append(substr)
      else:
        toks.extend(self._alphanum_re.split(substr))

    # Filter out empty strings
    toks = [t for t in toks if t]
    return toks

  def join(self, tokens):
    """Joins tokens into a string."""
    if self._alphanum_only:
      return u" ".join(tokens)
    else:
      # Fully invertible
      return u"".join(tokens)


def pad_decr(ids):
  """Strip ID 0 and decrement ids by 1."""
  idx = -1
  while not ids[idx]:
    idx -= 1
  if idx == -1:
    ids = ids
  else:
    ids = ids[:idx + 1]
  return [i - 1 for i in ids]


def pad_incr(ids):
  """Add 1 to ids to account for pad."""
  return [i + 1 for i in ids]


def _prepare_reserved_tokens(reserved_tokens):
  """Prepare reserved tokens and a regex for splitting them out of strings."""
  reserved_tokens = [tf.compat.as_text(tok) for tok in reserved_tokens or []]
  dups = _find_duplicates(reserved_tokens)
  if dups:
    raise ValueError("Duplicates found in tokens: %s" % dups)
  reserved_tokens_re = None
  if reserved_tokens:
    escaped = [rt.replace(u"\\", u"\\\\") for rt in reserved_tokens]
    pattern = u"(%s)" % u"|".join(escaped)
    reserved_tokens_re = re.compile(pattern, flags=re.UNICODE)
  return reserved_tokens, reserved_tokens_re


def _find_duplicates(els):
  seen = set()
  dups = []
  for x in els:
    if x in seen:
      dups.append(x)
    else:
      seen.add(x)
  return dups


def is_mixed_alphanum(token):
  return len([s for s in ALL_REGEX.split(token) if s]) > 1
