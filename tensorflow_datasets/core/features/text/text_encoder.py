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

import abc
import hashlib
import re

import six
import tensorflow as tf

# TODO(rsepassi):
# * Add more complex tokenization and knobs (check T2T tokenization)
# * Add support for reserved tokens (PAD, EOS, etc.)
# * Add SubwordTextEncoder


@six.add_metaclass(abc.ABCMeta)
class TextEncoder(object):
  """Base class for converting between text and integers."""

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

  def encode(self, s):
    return list(bytearray(tf.compat.as_bytes(s)))

  def decode(self, ids):
    return tf.compat.as_text(bytes(bytearray(ids)))

  @property
  def vocab_size(self):
    return 2**8


class TokenTextEncoder(TextEncoder):
  r"""TextEncoder backed by a list of tokens.

  Tokenization splits on (and drops) non-alphanumeric characters with
  regex "\W+".
  """

  def __init__(self,
               vocab_list=None,
               vocab_file=None,
               oov_buckets=1,
               oov_token=u"UNK"):
    if not (vocab_list or vocab_file) or (vocab_list and vocab_file):
      raise ValueError("Must provide either vocab_list or vocab_file.")
    self._vocab_list = [
        tf.compat.as_text(el).strip() for el in
        vocab_list or self._load_tokens_from_file(vocab_file)
    ]
    self._token_to_id = dict(
        zip(self._vocab_list, range(len(self._vocab_list))))
    self._oov_buckets = oov_buckets
    self._oov_token = tf.compat.as_text(oov_token)

  def encode(self, s):
    ids = []
    for token in tokenize(tf.compat.as_text(s)):
      int_id = self._token_to_id.get(token, -1)
      if int_id < 0:
        int_id = self._oov_bucket(token)
        if int_id is None:
          raise ValueError("Out of vocabulary token %s" % token)
      ids.append(int_id)
    return ids

  def decode(self, ids):
    tokens = []
    for int_id in ids:
      if int_id < len(self._vocab_list):
        tokens.append(self._vocab_list[int_id])
      else:
        tokens.append(self._oov_token)
    return u" ".join(tokens)

  @property
  def vocab_size(self):
    return len(self._vocab_list) + self._oov_buckets

  @property
  def tokens(self):
    return list(self._vocab_list)

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


def tokenize(s):
  """Split on (and drop) non-alphanumeric characters."""
  return [tok for tok in
          re.split(r"\W+", tf.compat.as_text(s), flags=re.UNICODE) if tok]
