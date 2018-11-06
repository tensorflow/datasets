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
  """Feature which encodes/decodes text.

  By default, text will be byte-encoded with utf-8 (if not already bytes).
  """

  def get_specs(self):
    return tf.VarLenFeature(tf.string)

  def encode_sample(self, sample_data):
    return tf.compat.as_bytes(sample_data)

  def decode_sample(self, tfexample_data):
    # Decoded as SparseTensor, only interested in the values
    return tf.reshape(tfexample_data.values, tuple())
