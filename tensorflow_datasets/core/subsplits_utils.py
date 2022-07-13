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

"""Even split utils."""

import dataclasses
import functools
import operator
from typing import List, Optional

from absl import logging
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import splits as splits_lib


@dataclasses.dataclass(frozen=True)
class _EvenSplit(splits_lib.AbstractSplit):
  """Split matching a subsplit of the given split."""
  split: splits_lib.SplitArg
  index: int
  count: int
  drop_remainder: bool

  def to_absolute(self, split_infos: splits_lib.SplitDict):
    # Extract the absolute instructions
    # One absolute instruction is created per `+`, so `train[:54%]+train[60%:]`
    # will create 2 absolute instructions.
    read_instruction = splits_lib.AbstractSplit.from_spec(self.split)
    absolute_instructions = read_instruction.to_absolute(split_infos)

    # Create the subsplit
    read_instructions_for_index = [
        self._absolute_to_read_instruction_for_index(abs_inst, split_infos)
        for abs_inst in absolute_instructions
    ]
    instuctions = functools.reduce(operator.add, read_instructions_for_index)
    return instuctions.to_absolute(split_infos)

  def _absolute_to_read_instruction_for_index(
      self,
      abs_inst,
      split_infos: splits_lib.SplitDict,
  ) -> splits_lib.ReadInstruction:
    start = abs_inst.from_ or 0
    if abs_inst.to is None:  # Note: `abs_inst.to == 0` is valid
      end = split_infos[abs_inst.splitname].num_examples
    else:
      end = abs_inst.to

    assert end >= start, f'start={start}, end={end}'
    num_examples = end - start

    examples_per_split = num_examples // self.count
    split_start = start + examples_per_split * self.index
    split_end = start + examples_per_split * (self.index + 1)

    # Handle remaining examples.
    num_unused_examples = num_examples % self.count
    assert num_unused_examples >= 0, num_unused_examples
    assert num_unused_examples < self.count, num_unused_examples
    if num_unused_examples > 0:
      if self.drop_remainder:
        logging.warning('Dropping %d examples of %d examples (host count: %d).',
                        num_unused_examples, num_examples, self.count)
      else:
        split_start += min(self.index, num_unused_examples)
        split_end += min(self.index + 1, num_unused_examples)

    return splits_lib.ReadInstruction(
        abs_inst.splitname,
        from_=split_start,
        to=split_end,
        unit='abs',
    )


def even_splits(
    split: str,
    n: int,
    *,
    drop_remainder: bool = False,
) -> List[splits_lib.SplitArg]:
  """Generates a list of non-overlapping sub-splits of same size.

  Example:

  ```python
  split0, split1, split2 = tfds.even_splits('train', n=3, drop_remainder=True)

  # Load 1/3 of the train split.
  ds = tfds.load('my_dataset', split=split0)
  ```

  `tfds.even_splits` supports arbitrary
  [sub-splits](https://www.tensorflow.org/datasets/splits) inputs, including
  other `tfds.even_splits` outputs.

  Args:
    split: Split (e.g. 'train', 'test[75%:]',...)
    n: Number of sub-splits to create
    drop_remainder: Drop examples if the number of examples in the datasets is
      not evenly divisible by `n`. If `False`, examples are distributed evenly
      across subsplits, starting by the first. For example, if there is 11
      examples with `n=3`, splits will contain `[4, 4, 3]` examples
      respectivelly.

  Returns:
    The list of subsplits. Those splits can be combined together (with
      `+`) or with other subsplits (e.g. `split + 'test[75%:]'`).
  """
  return [
      _EvenSplit(split=split, index=i, count=n, drop_remainder=drop_remainder)
      for i in range(n)
  ]


def split_for_jax_process(
    split: str,
    *,
    process_index: Optional[int] = None,
    process_count: Optional[int] = None,
    drop_remainder: bool = False,
) -> splits_lib.SplitArg:
  """Returns the subsplit of the data for the process.

  In distributed setting, all process/hosts should get a non-overlapping,
  equally sized slice of the entire data. This function takes as input a split
  and extracts the slice for the current process index.

  Usage:

  ```python
  tfds.load(..., split=tfds.split_for_jax_process('train'))
  ```

  This funtion is an alias for:

  ```python
  tfds.even_splits(split, n=jax.process_count())[jax.process_index()]
  ```

  By default, if examples can't be evenly distributed across processes, you can
  drop extra examples with `drop_remainder=True`.

  Args:
    split: Split to distribute across host (e.g. `train[75%:]`,
      `train[:800]+validation[:100]`).
    process_index: Process index in `[0, count)`. Defaults to
      `jax.process_index()`.
    process_count: Number of processes. Defaults to `jax.process_count()`.
    drop_remainder: Drop examples if the number of examples in the datasets is
      not evenly divisible by `n`. If `False`, examples are distributed evenly
      across subsplits, starting by the first. For example, if there is 11
      examples with `n=3`, splits will contain `[4, 4, 3]` examples
      respectivelly.

  Returns:
    subsplit: The sub-split of the given `split` for the current
      `process_index`.
  """
  if process_index is None:
    process_index = lazy_imports_lib.lazy_imports.jax.process_index()
  if process_count is None:
    process_count = lazy_imports_lib.lazy_imports.jax.process_count()
  return even_splits(
      split,
      n=process_count,
      drop_remainder=drop_remainder,
  )[process_index]
