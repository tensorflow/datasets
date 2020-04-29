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

# Lint as: python3
"""This module contains the reader config.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging
import attr

import tensorflow.compat.v2 as tf


_OLD = 'interleave_parallel_reads'
_NEW = 'interleave_cycle_length'
_WARNING_MSG = (
    '`{}` argument of `tfds.ReadConfig` is '
    'deprecated and will be removed in a future version. Please use '
    '`{}` instead.').format(_OLD, _NEW)


# TODO(tfds): Use dataclasses once Py2 support is dropped
@attr.s
class _ReadConfig(object):
  """Configures input reading pipeline."""
  # General tf.data.Dataset parametters
  options = attr.ib(factory=tf.data.Options)
  try_autocache = attr.ib(default=True)
  # tf.data.Dataset.shuffle parameters
  shuffle_seed = attr.ib(default=None)
  shuffle_reshuffle_each_iteration = attr.ib(default=None)
  # Interleave parameters
  # Both parallel_reads and block_length have empirically been tested to give
  # good results on imagenet.
  # This values might be changes in the future, with more performance test runs.
  interleave_cycle_length = attr.ib(default=16)
  interleave_block_length = attr.ib(default=16)
  experimental_interleave_sort_fn = attr.ib(default=None)

  @property
  def interleave_parallel_reads(self):
    logging.warning(_WARNING_MSG)
    return self.interleave_cycle_length

  @interleave_parallel_reads.setter
  def interleave_parallel_reads(self, value):
    logging.warning(_WARNING_MSG)
    self.interleave_cycle_length = value


class ReadConfig(_ReadConfig):
  """Configures input reading pipeline.

  Attributes:
    options: `tf.data.Options()`, dataset options. Those options are added to
      the default values defined in `tfrecord_reader.py`.
      Note that when `shuffle_files` is True and no seed is defined,
      experimental_deterministic will be set to False internally,
      unless it is defined here.
    try_autocache: If True (default) and the dataset satisfy the right
      conditions (dataset small enough, files not shuffled,...) the dataset
      will be cached during the first iteration (through `ds = ds.cache()`).
    shuffle_seed: `tf.int64`, seeds forwarded to `tf.data.Dataset.shuffle` when
      `shuffle_files=True`.
    shuffle_reshuffle_each_iteration: `bool`, forwarded to
      `tf.data.Dataset.shuffle` when `shuffle_files=True`.
    interleave_cycle_length: `int`, forwarded to `tf.data.Dataset.interleave`.
      Default to 16.
    interleave_block_length: `int`, forwarded to `tf.data.Dataset.interleave`.
      Default to 16.
    experimental_interleave_sort_fn: Function with signature
      `List[FileDict] -> List[FileDict]`, which takes the list of
      `dict(file: str, take: int, skip: int)` and returns the modified version
      to read. This can be used to sort/shuffle the shards to read in
      a custom order, instead of relying on `shuffle_files=True`.
  """

  def __init__(self, **kwargs):
    if _OLD in kwargs:
      if _NEW in kwargs:
        raise ValueError('Cannot set both {} and {}'.format(_OLD, _NEW))
      logging.warning(_WARNING_MSG)
      kwargs[_OLD] = kwargs.pop(_NEW)
    super(ReadConfig, self).__init__(**kwargs)
