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

"""Logic to read sharded files (tfrecord, buckets, ...).

This logic is shared between:
 - tfrecord_reader, to read sharded tfrecord files, based on user instructions.
 - tfrecord_writer, to read sharded bucket files (temp files), based on final
 sharding needs.
"""

import dataclasses
import math
import os
from typing import Any, List, Optional, Sequence

DEFAULT_MIN_SHARD_SIZE: int = 64 << 20  # 64 MiB
DEFAULT_MAX_SHARD_SIZE: int = 1024 << 20  # 1 GiB


@dataclasses.dataclass(frozen=True)
class ShardConfig:
  """Configuration of how shards should be created.

  Attributes:
    num_shards: number of shards that should be used. If `None`, then the number
      of shards is computed based on the total size of the dataset and the min
      and max shard size.
    min_shard_size: minimum shard size in bytes.
    max_shard_size: maximum shard size in bytes.
    overhead: the amount of overhead when writing a file. By default, it is the
      TFRecord overhead. See
      https://github.com/tensorflow/tensorflow/blob/27325fabed898880fa1b33a04d4b125a6ef4bbc8/tensorflow/core/lib/io/record_writer.h#L104
  """
  num_shards: Optional[int] = None
  min_shard_size: int = DEFAULT_MIN_SHARD_SIZE
  max_shard_size: int = DEFAULT_MAX_SHARD_SIZE
  overhead: int = 16

  def get_number_shards(
      self,
      total_size: int,
      num_examples: int,
      uses_precise_sharding: bool = True,
  ) -> int:
    """Returns number of shards for num_examples of total_size in bytes.

    Each shard should be at least 128MB.
    A pod has 16*16=256 TPU devices containing 1024 TPU chips (2048 cores).
    So if the dataset is large enough, we want the number of shards to be a
    multiple of 1024, but with shards as big as possible.
    If the dataset is too small, we want the number of shards to be a power
    of two so it distributes better on smaller TPU configs (8, 16, 32, ...
    cores).

    Args:
      total_size: the size of the data (serialized, not couting any overhead).
      num_examples: the number of records in the data.
      uses_precise_sharding: whether a mechanism is used to exactly control how
        many examples go in each shard.

    Returns:
      number of shards to use.
    """
    if self.num_shards:
      return self.num_shards

    total_size += num_examples * self.overhead
    max_shards_number = total_size // self.min_shard_size
    if uses_precise_sharding:
      max_shard_size = self.max_shard_size
    else:
      # When the pipeline does not control exactly how many rows go into each
      # shard (called 'precise sharding' here), we use a smaller max shard size
      # so that the pipeline doesn't fail if a shard gets some more examples.
      max_shard_size = 0.9 * self.max_shard_size
    min_shards_number = total_size // max_shard_size
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


@dataclasses.dataclass(eq=True, frozen=True)
class FileInstruction(object):
  """Instruction to read a single shard/file.

  Attributes:
    filename: The filename including the path.
    skip: Indicates which example read in the shard (`ds.skip().take()`). `0` if
      no skipping.
    take: Indicates how many examples to read (`-1` to read all).
    num_examples: `int`, The total number of examples.
  """
  filename: str
  skip: int
  take: int
  num_examples: int

  def dirname(self) -> str:
    return os.path.dirname(self.filename)

  def basename(self) -> str:
    return os.path.basename(self.filename)

  def replace(self, **kwargs: Any) -> 'FileInstruction':
    return dataclasses.replace(self, **kwargs)


def split_file_instruction(
    file_instruction: FileInstruction,
    num_splits: int,
) -> List[FileInstruction]:
  """Instructions for reading the given file instruction in several splits.

  Note that this function may return fewer splits than `num_splits` in case the
  number of examples cannot be split into that many. For example, if
  `file_instruction` has `num_examples=1` and `num_splits=2`, then only a single
  file instruction is returned.

  Arguments:
    file_instruction: the file instruction that should be split into multiple
      file instructions.
    num_splits: the number of splits the file instruction should be split into.

  Returns:
    list of file instructions into which it is split.
  """
  if file_instruction.take != -1:
    raise ValueError('Only file instructions that read all rows are supported!')
  examples_per_split = math.ceil(file_instruction.num_examples / num_splits)
  splits = []
  index = file_instruction.skip
  while index < file_instruction.num_examples:
    # If there are fewer examples left in the file than `examples_per_split`,
    # then only take what's left.
    take = min(examples_per_split, file_instruction.num_examples - index)
    splits.append(file_instruction.replace(skip=index, take=take))
    index += take
  return splits


def get_file_instructions(
    from_: int,
    to: int,
    filenames: Sequence[str],
    shard_lengths: Sequence[int],
) -> List[FileInstruction]:
  """Returns a list of files (+skip/take) to read [from_:to] items from shards.

  Args:
    from_: int, Index (included) of element from which to read.
    to: int, Index (excluded) of element to which to read.
    filenames: list of strings or ints, the filenames of the shards. Not really
      used, but to place in result.
    shard_lengths: the number of elements in every shard.

  Returns:
    list of dict(filename, skip, take).
  """
  index_start = 0  # Beginning (included) of moving window.
  index_end = 0  # End (excluded) of moving window.
  file_instructions = []
  for filename, length in zip(filenames, shard_lengths):
    if not length:
      continue  # Empty shard - can happen with temporary buckets.
    index_end += length
    if from_ < index_end and to > index_start:  # There is something to take.
      skip = from_ - index_start if from_ > index_start else 0
      take = to - index_start - skip if to < index_end else -1
      if take == 0:
        continue
      file_instructions.append(
          FileInstruction(
              filename=filename,
              skip=skip,
              take=take,
              num_examples=length - skip if take == -1 else take,
          ))
    index_start += length
  return file_instructions
