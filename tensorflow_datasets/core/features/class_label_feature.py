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

"""ClassLabel feature."""

import tensorflow as tf
from tensorflow_datasets.core.features import feature


class ClassLabel(feature.FeatureConnector):
  """Feature encoding an integer class label."""

  def __init__(self, num_classes, names=None, names_file=None):
    """Constructs a ClassLabel FeatureConnector.

    Args:
      num_classes: `int`, number of classes. All labels must be < num_classes.
      names: `list<str>`, optional string names for the integer classes.
      names_file: `str`, optional path to a file with names for the integer
        classes, one per line.
    """
    self._num_classes = num_classes

    if names and names_file:
      raise ValueError("Must provide either names or names_file, not both.")
    if names or names_file:
      names = names or self._load_names_from_file(names_file)
      self._names = [tf.compat.as_text(name) for name in names]
      if len(self._names) != self._num_classes:
        raise ValueError("num_classes=%d but found %d names. Those must match" %
                         (self._num_classes, len(self._names)))

  @property
  def num_classes(self):
    return self._num_classes

  @property
  def names(self):
    return self._names

  def get_tensor_info(self):
    return feature.TensorInfo(shape=(), dtype=tf.int64)

  def encode_sample(self, sample_data):
    # Allowing -1 to mean no label.
    if not -1 <= sample_data < self._num_classes:
      raise ValueError("Class label %d greater than configured num_classes %d" %
                       (sample_data, self._num_classes))
    return sample_data

  def decode_sample(self, tfexample_data):
    return tf.reshape(tfexample_data, tuple())

  def _load_names_from_file(self, names_file):
    with tf.gfile.Open(names_file, "rb") as f:
      return [name.strip() for name in tf.compat.as_text(f.read()).split("\n")]
