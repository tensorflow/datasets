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

"""To write records into sharded tfrecord files."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import logging
import tensorflow as tf

from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import shuffle
from tensorflow_datasets.core import utils

MIN_SHARD_SIZE = 64<<20  # 64 MiB
MAX_SHARD_SIZE = 1024<<20  # 2 GiB

# TFRECORD overheads.
# https://github.com/tensorflow/tensorflow/blob/27325fabed898880fa1b33a04d4b125a6ef4bbc8/tensorflow/core/lib/io/record_writer.h#L104
TFRECORD_REC_OVERHEAD = 16


class _TFRecordWriter(object):
  """Writes examples in given order, to specified number of shards."""

  def __init__(self, path, num_examples, number_of_shards):
    """Init _TFRecordWriter instance.

    Args:
      path: where to write TFRecord file.
      num_examples (int): the number of examples which will be written.
      number_of_shards (int): the desired number of shards. The examples will be
        evenly distributed among that number of shards.
    """
    self._path = path
    self._shard_boundaries = [round(num_examples * (float(i)/number_of_shards))
                              for i in range(1, number_of_shards+1)]
    self._num_shards = number_of_shards
    self._shards_length = []  # The number of Example in each shard.
    self._number_written_examples = 0
    self._init_new_shard(0)

  def _init_new_shard(self, new_shard_number):
    self._current_shard = new_shard_number
    self._current_shard_limit = self._shard_boundaries.pop(0)
    self._current_writer = None
    self._current_shard_length = 0

  def _flush_current_shard(self):
    if self._current_shard_length == 0:
      return  # Nothing was written.
    self._current_writer.flush()
    self._current_writer.close()
    self._current_writer = None
    self._shards_length.append(self._current_shard_length)

  def _get_path(self, index):
    return '%s-%05d-of-%05d' % (self._path, index, self._num_shards)

  def _write(self, serialized_example):
    if not self._current_writer:
      fpath = self._get_path(self._current_shard)
      logging.info('Creating file %s', fpath)
      self._current_writer = tf.io.TFRecordWriter(fpath)
    self._current_writer.write(serialized_example)
    self._current_shard_length += 1
    self._number_written_examples += 1

  def write(self, serialized_example):
    """Write given example, starts new shard when needed."""
    if self._number_written_examples >= self._current_shard_limit:
      self._flush_current_shard()
      self._init_new_shard(self._current_shard + 1)
    self._write(serialized_example)

  def finalize(self):
    """Finalize files, returns list containing the length of each shard."""
    self._flush_current_shard()
    return self._shards_length


def _get_number_shards(total_size, num_examples):
  """Returns number of shards for num_examples of total_size in bytes.

  Each shard should be at least 128MB.
  A pod has 16*16=256 TPU devices containing 1024 TPU chips (2048 cores).
  So if the dataset is large enough, we want the number of shards to be a
  multiple of 1024, but with shards as big as possible.
  If the dataset is too small, we want the number of shards to be a power
  of two so it distributes better on smaller TPU configs (8, 16, 32, ... cores).

  Args:
    total_size: the size of the data (serialized, not couting any overhead).
    num_examples: the number of records in the data.

  Returns:
    number of shards to use.
  """
  total_size += num_examples * TFRECORD_REC_OVERHEAD
  max_shards_number = total_size // MIN_SHARD_SIZE
  min_shards_number = total_size // MAX_SHARD_SIZE
  if min_shards_number <= 1024 <= max_shards_number and num_examples >= 1024:
    return 1024
  elif min_shards_number > 1024:
    i = 2
    while True:
      n = 1024 * i
      if n >= min_shards_number and num_examples >= n:
        return n
      i += 1
  else:
    for n in [512, 256, 128, 64, 32, 16, 8, 4, 2]:
      if min_shards_number <= n <= max_shards_number and num_examples >= n:
        return n
  return 1


class Writer(object):
  """Shuffles and writes Examples to sharded TFRecord files.

  The number of shards is computed automatically.

  This class is a replacement for file_format_adapter.TFRecordExampleAdapter,
  which will eventually be deleted.
  """

  def __init__(self, example_specs, path):
    self._serializer = example_serializer.ExampleSerializer(example_specs)
    self._shuffler = shuffle.Shuffler(os.path.dirname(path))
    self._num_examples = 0
    self._path = path

  def write(self, key, example):
    """Writes given Example.

    The given example is not directly written to the tfrecord file, but to a
    temporary file (or memory). The finalize() method does write the tfrecord
    files.

    Args:
      key (int|bytes): the key associated with the example. Used for shuffling.
      example: the Example to write to the tfrecord file.
    """
    serialized_example = self._serializer.serialize_example(example)
    self._shuffler.add(key, serialized_example)
    self._num_examples += 1

  def finalize(self):
    """Effectively writes examples to the tfrecord files."""
    print('Shuffling and writing examples to %s' % self._path)
    number_of_shards = _get_number_shards(self._shuffler.size,
                                          self._num_examples)
    writer = _TFRecordWriter(self._path, self._num_examples, number_of_shards)
    for serialized_example in utils.tqdm(
        self._shuffler, total=self._num_examples,
        unit=' examples', leave=False):
      writer.write(serialized_example)
    shard_lengths = writer.finalize()
    logging.info('Done writing %s. Shard lengths: %s',
                 self._path, shard_lengths)
    return shard_lengths
