# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

from __future__ import annotations

from collections.abc import Iterable, Sequence
import dataclasses
import math
import os
from typing import Any

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

  num_shards: int | None = None
  min_shard_size: int = DEFAULT_MIN_SHARD_SIZE
  max_shard_size: int = DEFAULT_MAX_SHARD_SIZE
  overhead: int = 16

  @classmethod
  def calculate_number_shards(
      cls,
      total_size: int,
      num_examples: int,
      uses_precise_sharding: bool = True,
  ) -> int:
    """Returns number of shards for num_examples of total_size in bytes.

    Args:
      total_size: the size of the data (serialized, not couting any overhead).
      num_examples: the number of records in the data.
      uses_precise_sharding: whether a mechanism is used to exactly control how
        many examples go in each shard.
    """
    total_size += num_examples * cls.overhead
    max_shards_number = total_size // cls.min_shard_size
    if uses_precise_sharding:
      max_shard_size = cls.max_shard_size
    else:
      # When the pipeline does not control exactly how many rows go into each
      # shard (called 'precise sharding' here), we use a smaller max shard size
      # so that the pipeline doesn't fail if a shard gets some more examples.
      max_shard_size = 0.9 * cls.max_shard_size
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

  def get_number_shards(
      self,
      total_size: int,
      num_examples: int,
      uses_precise_sharding: bool = True,
  ) -> int:
    if self.num_shards:
      return self.num_shards
    return self.calculate_number_shards(
        total_size, num_examples, uses_precise_sharding
    )


def get_shard_boundaries(
    num_examples: int,
    number_of_shards: int,
) -> Sequence[int]:
  """Returns the offsets of all shards."""
  if num_examples == 0:
    raise AssertionError('No examples were yielded.')
  if num_examples < number_of_shards:
    raise AssertionError(
        'num_examples ({}) < number_of_shards ({})'.format(
            num_examples, number_of_shards
        )
    )
  return [
      round(num_examples * shard_index / number_of_shards)
      for shard_index in range(1, number_of_shards + 1)
  ]


@dataclasses.dataclass(eq=True, frozen=True)
class FileInstruction:
  """Instruction to read a single shard/file.

  Attributes:
    filename: The filename including the path.
    skip: Indicates which example read in the shard (`ds.skip().take()`). `0` if
      no skipping.
    take: Indicates how many examples to read (`-1` to read all). If `-1`, then
      `take` is overridden with the number of examples to read is calculated.
    examples_in_shard: The total number of examples in the shard. To get the
      number of examples to read, use `take`.
    takes_all: whether all examples after skipping are read.
  """

  filename: str
  skip: int
  take: int
  examples_in_shard: int

  def __post_init__(self):
    if self.take == -1:
      object.__setattr__(self, 'take', self.examples_in_shard - self.skip)
    if self.examples_in_shard < 0:
      raise ValueError(
          f'examples_in_shard should be >= 0! Was {self.examples_in_shard}.'
      )
    if self.skip < 0 or self.skip > self.examples_in_shard:
      raise ValueError(
          f'skip should be between 0 and {self.examples_in_shard}! '
          f'Was {self.skip}.'
      )
    if self.skip + self.take > self.examples_in_shard:
      raise ValueError(
          f'skip ({self.skip}) + take ({self.take}) should be '
          f'<= examples_in_shard ({self.examples_in_shard})!'
      )

  @property
  def takes_all(self) -> bool:
    return self.skip + self.take == self.examples_in_shard

  def dirname(self) -> str:
    return os.path.dirname(self.filename)

  def basename(self) -> str:
    return os.path.basename(self.filename)

  def replace(self, **kwargs: Any) -> FileInstruction:
    return dataclasses.replace(self, **kwargs)


def split_file_instruction(
    file_instruction: FileInstruction,
    num_splits: int,
) -> list[FileInstruction]:
  """Instructions for reading the given file instruction in several splits.

  Note that this function may return fewer splits than `num_splits` in case the
  number of examples cannot be split into that many. For example, if
  `file_instruction` has `take=1` and `num_splits=2`, then only a single
  file instruction is returned.

  Arguments:
    file_instruction: the file instruction that should be split into multiple
      file instructions. It is currently not supported to have `skip>0` or not
      take all examples in the file.
    num_splits: the number of splits the file instruction should be split into.

  Returns:
    list of file instructions into which it is split.
  """
  if not file_instruction.takes_all or file_instruction.skip > 0:
    raise ValueError('Only file instructions that read all rows are supported!')
  examples_per_split = math.ceil(file_instruction.take / num_splits)
  splits = []
  index = file_instruction.skip
  while index < file_instruction.examples_in_shard:
    # If there are fewer examples left in the file than `examples_per_split`,
    # then only take what's left.
    take = min(examples_per_split, file_instruction.examples_in_shard - index)
    splits.append(file_instruction.replace(skip=index, take=take))
    index += take
  return splits


def get_file_instructions(
    from_: int,
    to: int,
    filenames: Sequence[str],
    shard_lengths: Sequence[int],
    examples_in_shards: Sequence[int] | None = None,
) -> list[FileInstruction]:
  """Returns a list of files (+skip/take) to read [from_:to] items from shards.

  Args:
    from_: int, Index (included) of element from which to read.
    to: int, Index (excluded) of element to which to read.
    filenames: list of strings or ints, the filenames of the shards. Not really
      used, but to place in result.
    shard_lengths: the number of elements in every shard.
    examples_in_shards: the number of examples in every shard. If not provided,
      then `shard_lengths` is used.

  Returns:
    list of dict(filename, skip, take).
  """
  index_start = 0  # Beginning (included) of moving window.
  index_end = 0  # End (excluded) of moving window.
  file_instructions = []
  for shard_index, (filename, length) in enumerate(
      zip(filenames, shard_lengths)
  ):
    if not length:
      continue  # Empty shard - can happen with temporary buckets.
    index_end += length
    if from_ < index_end and to > index_start:  # There is something to take.
      skip = from_ - index_start if from_ > index_start else 0
      take = to - index_start - skip if to < index_end else -1
      if take == 0:
        continue
      if examples_in_shards is not None:
        examples_in_shard = examples_in_shards[shard_index]
        if take == -1 and examples_in_shard != length:
          take = length
      else:
        examples_in_shard = length
      file_instructions.append(
          FileInstruction(
              filename=filename,
              skip=skip,
              take=take,
              examples_in_shard=examples_in_shard,
          )
      )
    index_start += length
  return file_instructions
