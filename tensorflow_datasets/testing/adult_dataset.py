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

"""For generating fake examples for adult datasets.
"""

import os

import random
from absl import app
from absl import flags

import tensorflow.compat.v2 as tf

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.structured.adult import _WORK_CLASS_LABELS, \
  _EDUCATION_LABELS, _MARITAL_LABELS, _OCCUPATION_LABELS, \
  _RELATION_LABELS, _RACE_LABELS, _COUNTRY_LABELS


flags.DEFINE_string("tfds_dir", py_utils.tfds_dir(),
                    "Path to tensorflow_datasets directory")
FLAGS = flags.FLAGS

def examples_dir():
  return os.path.join(FLAGS.tfds_dir, "testing", "test_data", "fake_examples")

def adult_dir(name):
  return os.path.join(examples_dir(), name)

_TRAIN_DATA_FILENAME = "adult.data"
_TEST_DATA_FILENAME = "adult.test"

def random_label(labels):
  return labels[random.randint(0, len(labels) - 1)]

def write_file(filename, num_lines):
  """writes to the train and test files"""
  with tf.io.gfile.GFile(filename, "w") as f:
    for _ in range(num_lines):
      row = [
          str(random.randint(0, 1000)),
          random_label(_WORK_CLASS_LABELS),
          str(random.randint(0, 1000)),
          random_label(_EDUCATION_LABELS),
          str(random.randint(0, 1000)),
          random_label(_MARITAL_LABELS),
          random_label(_OCCUPATION_LABELS),
          random_label(_RELATION_LABELS),
          random_label(_RACE_LABELS),
          random_label(["Male", "Female"]),
          str(random.randint(0, 1000)),
          str(random.randint(0, 1000)),
          str(random.randint(0, 1000)),
          random_label(_COUNTRY_LABELS),
          random_label(["<=50K", ">50K"]),
      ]
      f.write(", ".join(row))
      f.write("\n")

def main(_):
  out_dir = adult_dir('adult')
  #return out_dir
  write_file(os.path.join(out_dir, _TRAIN_DATA_FILENAME), 5)
  write_file(os.path.join(out_dir, _TEST_DATA_FILENAME), 3)

if __name__ == "__main__":
  app.run(main)
