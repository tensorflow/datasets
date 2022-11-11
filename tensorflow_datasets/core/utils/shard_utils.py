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
from typing import Any, List, Sequence


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
