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

"""Utilities for dealing with tf.data.Dataset."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core import utils

__all__ = [
    "build_dataset",
    "iterate_over_dataset",
]


def build_dataset(filepattern,
                  dataset_from_file_fn,
                  shuffle_files=False,
                  parallel_reads=64):
  """Constructs a `tf.data.Dataset` from TFRecord files.

  Args:
    filepattern (str): Glob pattern for TFRecord files.
    dataset_from_file_fn (function): returns a `tf.data.Dataset` given a
      filename.
    shuffle_files (bool): Whether to shuffle the input filenames.
    parallel_reads (int): how many files to read in parallel.

  Returns:
    `tf.data.Dataset`
  """
  dataset = tf.data.Dataset.list_files(filepattern, shuffle=shuffle_files)
  dataset = dataset.interleave(
      dataset_from_file_fn,
      cycle_length=parallel_reads,
      num_parallel_calls=parallel_reads)
  return dataset


def iterate_over_dataset(dataset):
  """Yields numpy elements of `tf.data.Dataset`."""
  if tf.executing_eagerly():
    for item in dataset:
      flat = tf.contrib.framework.nest.flatten(item)
      flat = [el.numpy() for el in flat]
      yield tf.contrib.framework.nest.pack_sequence_as(item, flat)
  else:
    item = dataset.make_one_shot_iterator().get_next()
    with utils.nogpu_session() as sess:
      while True:
        try:
          yield sess.run(item)
        except tf.errors.OutOfRangeError:
          break
