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

"""Parquet DataSource class."""

from collections.abc import Iterable, Sequence
import dataclasses
from typing import Any

import numpy as np
from tensorflow_datasets.core.data_sources import base
from tensorflow_datasets.core.utils.lazy_imports_utils import parquet as pq
from tensorflow_datasets.core.utils.lazy_imports_utils import pyarrow as pa


@dataclasses.dataclass
class _ParquetTable:
  """Overloads pa.Table to transform it into a valid data source."""

  table: pa.Table

  def __getitems__(self, keys: Iterable[int]) -> Sequence[Any]:
    """Retrieves ranges/slices/lists of indexes from the Parquet table."""
    keys = np.fromiter(keys, np.int64)
    if not keys.size:
      return []
    # All elements are written in the first column (see core.ParquetFileAdapter)
    elements = self.table.take(keys).column(0)
    return [memoryview(element.as_buffer()) for element in elements]

  def __getitem__(self, key: int) -> Any:
    """Retrieves the n-th element from the Parquet table."""
    # The element is written in the first column (see core.ParquetFileAdapter)
    element = self.table.slice(key, 1).column(0)
    if len(element) == 1:
      return memoryview(element[0].as_buffer())
    raise IndexError(f'Could not find element at index {key}')

  def __len__(self) -> int:
    return self.table.num_rows


@dataclasses.dataclass(repr=False)
class ParquetDataSource(base.BaseDataSource):
  """ParquetDataSource to read from a ParquetDataset."""

  def __post_init__(self):
    file_instructions = base.file_instructions(self.dataset_info, self.split)
    filenames = [
        file_instruction.filename for file_instruction in file_instructions
    ]
    dataset = pq.ParquetDataset(filenames)
    table = dataset.read()
    self.data_source = _ParquetTable(table=table)
