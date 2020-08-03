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

"""Text feature.

"""

import html
import textwrap

import tensorflow.compat.v2 as tf

from tensorflow_datasets.core.features import feature


class Text(feature.Tensor):
  """`FeatureConnector` for text, encoding to integers with a `TextEncoder`."""

  def __init__(self):
    """Constructs a Text FeatureConnector."""
    super(Text, self).__init__(shape=(), dtype=tf.string)

  def repr_html(self, ex: bytes) -> str:
    """Text are decoded."""
    ex = ex.decode("utf-8")
    ex = html.escape(ex)
    ex = textwrap.shorten(ex, width=1000)  # Truncate long text
    return ex
