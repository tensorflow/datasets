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

"""Text feature.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

from tensorflow_datasets.core.features import feature


class Text(feature.FeatureConnector):
  """Feature which encodes/decodes text, possibly to integers."""

  def __init__(self, encoder=None):
    """Constructs a Text FeatureConnector.

    Args:
      encoder: `TextEncoder`, an encoder that can convert text to integers.
        If None, the text will be utf-8 byte-encoded.
    """
    self._encoder = encoder

  @property
  def encoder(self):
    return self._encoder

  @property
  def vocab_size(self):
    return self.encoder and self.encoder.vocab_size

  def str2ints(self, str_value):
    """Conversion list[int] => decoded string."""
    if not self._encoder:
      raise ValueError(
          "Text.str2ints is not available because encoder hasn't been defined.")
    return self._encoder.encode(tf.compat.as_text(str_value))

  def ints2str(self, int_values):
    """Conversion string => encoded list[int]."""
    if not self._encoder:
      raise ValueError(
          "Text.ints2str is not available because encoder hasn't been defined.")
    return self._encoder.decode(int_values)

  def get_tensor_info(self):
    if self.encoder:
      return feature.TensorInfo(shape=(None,), dtype=tf.int64)
    else:
      return feature.TensorInfo(shape=(), dtype=tf.string)

  def encode_example(self, example_data):
    if self.encoder:
      return self.encoder.encode(example_data)
    else:
      return tf.compat.as_bytes(example_data)

  def decode_example(self, tfexample_data):
    return tfexample_data
