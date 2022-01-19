# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""This module contains the reader config."""

import dataclasses
import enum
from typing import Callable, Optional, Sequence, Union

import tensorflow as tf
from tensorflow_datasets.core.utils import shard_utils

InterleaveSortFn = Callable[[Sequence[shard_utils.FileInstruction]],
                            Sequence[shard_utils.FileInstruction],]


class _MISSING:
  pass


MISSING = _MISSING()


@dataclasses.dataclass(eq=False)
class ReadConfig:
  """Configures input reading pipeline.

  Attributes:
    options: `tf.data.Options()`, dataset options to use. Note that when
      `shuffle_files` is True and no seed is defined, deterministic will be set
      to False internally, unless it is defined here.
    try_autocache: If True (default) and the dataset satisfy the right
      conditions (dataset small enough, files not shuffled,...) the dataset will
      be cached during the first iteration (through `ds = ds.cache()`).
    add_tfds_id: If True, examples `dict` in `tf.data.Dataset` will have an
      additional key `'tfds_id': tf.Tensor(shape=(), dtype=tf.string)`
        containing the example unique identifier (e.g.
        'train.tfrecord-000045-of-001024__123').
       Note: IDs might changes in future version of TFDS.
    shuffle_seed: `tf.int64`, seed forwarded to `tf.data.Dataset.shuffle` during
      file shuffling (which happens when `tfds.load(..., shuffle_files=True)`).
    shuffle_reshuffle_each_iteration: `bool`, forwarded to
      `tf.data.Dataset.shuffle` during file shuffling (which happens when
      `tfds.load(..., shuffle_files=True)`).
    interleave_cycle_length: `int`, forwarded to `tf.data.Dataset.interleave`.
    interleave_block_length: `int`, forwarded to `tf.data.Dataset.interleave`.
    input_context: `tf.distribute.InputContext`, if set, each worker will read a
      different set of file. For more info, see the
      [distribute_datasets_from_function
      documentation](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_datasets_from_function).
      Note:  * Each workers will always read the same subset of files.
        `shuffle_files` only shuffle files within each worker. * If
        `info.splits[split].num_shards < input_context.num_input_pipelines`, an
        error will be raised, as some workers would be empty.
    experimental_interleave_sort_fn: Function with signature `List[FileDict] ->
      List[FileDict]`, which takes the list of
      `dict(file: str, take: int, skip: int)` and returns the modified version
        to read. This can be used to sort/shuffle the shards to read in a custom
        order, instead of relying on `shuffle_files=True`.
    skip_prefetch: If False (default), add a `ds.prefetch()` op at the end.
      Might be set for performance optimization in some cases (e.g. if you're
      already calling `ds.prefetch()` at the end of your pipeline)
    num_parallel_calls_for_decode: The number of parallel calls for decoding
      record. By default using tf.data's AUTOTUNE.
    num_parallel_calls_for_interleave_files: The number of parallel calls for
      interleaving files. By default using tf.data's AUTOTUNE.
    enable_ordering_guard: When True (default), an exception is raised if
      shuffling or interleaving are used on an ordered dataset.
    assert_cardinality: When True (default), an exception is raised if at the
      end of an Epoch the number of read examples does not match the expected
      number from dataset metadata. A power user would typically want to set
      False if input files have been tempered with and they don't mind missing
      records or have too many of them.
  """
  # General tf.data.Dataset parametters
  options: tf.data.Options = dataclasses.field(default_factory=tf.data.Options)
  try_autocache: bool = True
  add_tfds_id: bool = False
  # tf.data.Dataset.shuffle parameters
  shuffle_seed: Optional[int] = None
  shuffle_reshuffle_each_iteration: Optional[bool] = None
  # Interleave parameters
  # Ideally, we should switch interleave values to None to dynamically set
  # those value depending on the user system. However, this would make the
  # generation order non-deterministic accross machines.
  interleave_cycle_length: Union[Optional[int], _MISSING] = MISSING
  interleave_block_length: Optional[int] = 16
  input_context: Optional[tf.distribute.InputContext] = None
  experimental_interleave_sort_fn: Optional[InterleaveSortFn] = None
  skip_prefetch: bool = False
  num_parallel_calls_for_decode: Optional[int] = tf.data.experimental.AUTOTUNE
  num_parallel_calls_for_interleave_files: Optional[int] = (
      tf.data.experimental.AUTOTUNE)
  enable_ordering_guard: bool = True
  assert_cardinality: bool = True
