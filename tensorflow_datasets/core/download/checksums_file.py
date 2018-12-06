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

"""Functions to load/dump checksums files."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os

import tensorflow as tf
from tensorflow_datasets.core.utils import py_utils



def _open_checksums_file(dataset_name):
  path = os.path.normpath(
      os.path.join(py_utils.tfds_dir(),
                   'url_checksums',
                   '%s.csv' % dataset_name))
  return tf.gfile.Open(path)




def load(dataset_name):
  """Returns dict: {"url": "checksum"} for given dataset."""
  checksums = {}
  csv_f = _open_checksums_file(dataset_name)
  try:
    reader = csv.reader(csv_f, delimiter=' ')
    for row in reader:
      checksums[row[0]] = row[1]
  finally:
    csv_f.close()
  return checksums


def dump(path, url_to_checksum):
  # TODO(pierrot): make load and dump consistent. They should either both accept
  # a path or both accept a name.
  with tf.gfile.Open(path, 'w') as csv_f:
    writer = csv.writer(csv_f, delimiter=' ')
    writer.writerows(sorted(url_to_checksum.items()))
