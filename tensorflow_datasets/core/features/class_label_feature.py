# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

import json
import os
import six
import tensorflow as tf
from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core.features import feature


class ClassLabel(feature.Tensor):
  """`FeatureConnector` for integer class labels."""

  @api_utils.disallow_positional_args
  def __init__(self, num_classes=None, names=None, names_file=None):
    """Constructs a ClassLabel FeatureConnector.

    There are 3 ways to define a ClassLabel, which correspond to the 3
    arguments:

     * `num_classes`: create 0 to (num_classes-1) labels
     * `names`: a list of label strings or a list of label/mapping dicts
     * `names_file`: a file containing the list of labels.

    Note: On python2, the strings are encoded as utf-8.

    Args:
      num_classes: `int`, number of classes. All labels must be < num_classes.
      names: `list<str>`, string names for the integer classes. The
        order in which the names are provided is kept.
             `list<dict>`, dict features for the integer classes. The
        order in which the names are provided is kept.
      names_file: `str`, path to a file with names for the integer
        classes, one per line.
    """
    super(ClassLabel, self).__init__(shape=(), dtype=tf.int64)

    self._num_classes = None
    self._str2int = None
    self._int2str = None
    self._is_multilabel = False

    # The label is explicitly set as undefined (no label defined)
    if not sum(bool(a) for a in (num_classes, names, names_file)):
      return

    if sum(bool(a) for a in (num_classes, names, names_file)) != 1:
      raise ValueError(
          "Only a single argument of ClassLabel() should be provided.")

    if num_classes:
      self._num_classes = num_classes
    else:
      self.names = names or _load_names_from_file(names_file)

  @property
  def num_classes(self):
    return self._num_classes

  @property
  def names(self):
    if self._is_multilabel:
      return list(self._int2str)
    if not self._int2str:
      return [tf.compat.as_text(str(i)) for i in range(self._num_classes)]
    return list(self._int2str)

  @names.setter
  def names(self, new_names):
    if type(new_names) == list and type(new_names[0]) == dict:
      self._is_multilabel = True
      self._num_classes = len(new_names)
      int2str = [name for name in new_names]
    else:
      int2str = [tf.compat.as_text(name) for name in new_names]
    # Names can only be defined once
    if self._int2str is not None and self._int2str != int2str:
      raise ValueError(
          "Trying to overwrite already defined ClassLabel names. Previous: {} "
          ", new: {}".format(self._int2str, int2str))

    # Set-up [new] names
    self._int2str = int2str
    # str2int only for string labels not for dict labels for now
    if not self._is_multilabel:
      self._str2int = {name: i for i, name in enumerate(self._int2str)}

      # If num_classes has been defined, ensure that num_classes and names match
      num_classes = len(self._str2int)
      if self._num_classes is None:
        self._num_classes = num_classes
      elif self._num_classes != num_classes:
        raise ValueError(
            "ClassLabel number of names do not match the defined num_classes. "
            "Got {} names VS {} num_classes".format(
                num_classes, self._num_classes)
        )

  def str2int(self, str_value):
    """Conversion class name string/dict => integer."""
    # Linear Search for dict values to find the integer class
    if self._is_multilabel:
      for i in range(len(self._int2str)):
        if self._int2str[i] == str_value:
          return i
      else:
        raise ValueError("Invalid dict class label %s" % str_value)
    str_value = tf.compat.as_text(str_value)
    if self._str2int:
      return self._str2int[str_value]

    # No names provided, try to integerize
    failed_parse = False
    try:
      int_value = int(str_value)
    except ValueError:
      failed_parse = True
    if failed_parse or not 0 <= int_value < self._num_classes:
      raise ValueError("Invalid string class label %s" % str_value)
    return int_value

  def int2str(self, int_value):
    """Conversion integer => class name string."""
    if self._int2str:
      # Maybe should support batched np array/eager tensors, to allow things
      # like
      # out_ids = model(inputs)
      # labels = cifar10.info.features['label'].int2str(out_ids)
      return self._int2str[int_value]

    # No names provided, return str(int)
    if not 0 <= int_value < self._num_classes:
      raise ValueError("Invalid integer class label %d" % int_value)
    return tf.compat.as_text(str(int_value))

  def encode_example(self, example_data):
    if self._num_classes is None:
      raise ValueError(
          "Trying to use ClassLabel feature with undefined number of class. "
          "Please set ClassLabel.names or num_classes."
      )

    # If a string is given, convert to associated integer
    if isinstance(example_data, six.string_types):
      example_data = self.str2int(example_data)

    # Allowing -1 to mean no label.
    if not -1 <= example_data < self._num_classes:
      raise ValueError("Class label %d greater than configured num_classes %d" %
                       (example_data, self._num_classes))
    return example_data

  def save_metadata(self, data_dir, feature_name=None):
    """See base class for details."""
    # Save names if defined
    if not self._is_multilabel and self._str2int is not None:
      names_filepath = _get_names_filepath(data_dir, feature_name)
      _write_names_to_file(names_filepath, self.names)
    # For dict feature
    if self._is_multilabel:
      names_filepath = _get_names_filepath(data_dir, feature_name, self._is_multilabel)
      _write_names_to_file(names_filepath, self.names, self._is_multilabel)

  def load_metadata(self, data_dir, feature_name=None):
    """See base class for details."""
    # Restore names if defined
    names_filepath = _get_names_filepath(data_dir, feature_name, self._is_multilabel)
    if tf.io.gfile.exists(names_filepath):
      self.names = _load_names_from_file(names_filepath, self._is_multilabel)

  def _additional_repr_info(self):
    return {"num_classes": self.num_classes}


def _get_names_filepath(data_dir, feature_name, is_multilabel=False):
  if is_multilabel:
    return os.path.join(data_dir, "{}.labels.json".format(feature_name))
  return os.path.join(data_dir, "{}.labels.txt".format(feature_name))


def _load_names_from_file(names_filepath, is_multilabel=False):
  if is_multilabel:
    with open(names_filepath, "r") as f:
      names = json.load(f)
    return names  
  with tf.io.gfile.GFile(names_filepath, "r") as f:
    return [
        name.strip()
        for name in tf.compat.as_text(f.read()).split("\n")
        if name.strip()  # Filter empty names
    ]


def _write_names_to_file(names_filepath, names, is_multilabel=False):
  if is_multilabel:
    with open(names_filepath, "w") as f:
      json.dump(names, f)
  else:
    with tf.io.gfile.GFile(names_filepath, "w") as f:
      f.write("\n".join(names) + "\n")
