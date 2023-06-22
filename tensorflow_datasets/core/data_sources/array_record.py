# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""ArrayRecord DataSource base class.

Warning: this is an experimental module. The interface might change in the
future without backwards compatibility.
"""

from collections.abc import Sequence as AbcSequence
import dataclasses
from typing import Any, Optional, Sequence, TypeVar

from absl import logging
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import array_record_data_source
import tree

T = TypeVar('T')

_DEFAULT_ITERATION_STEP = 1000


@dataclasses.dataclass
class ArrayRecordDataSource(AbcSequence):
  """Grain DataSource class.

  Warning: this is an experimental class. The interface might change in the
  future without backwards compatibility.

  It acts as a wrapper around `array_record.ArrayRecordDataSource` that can read
  from ArrayRecords. It exposes `__len__` and `__getitem__` to serve as a data
  source.
  """

  dataset_info: dataset_info_lib.DatasetInfo
  split: splits_lib.Split = None
  decoders: Optional[type_utils.TreeDict[decode.partial_decode.DecoderArg]] = (
      None
  )
  # In order to lazy load array_record, we don't load
  # `array_record_data_source.ArrayRecordDataSource` here.
  data_source: Any = dataclasses.field(init=False)
  length: int = dataclasses.field(init=False)

  def __post_init__(self):
    file_format = self.dataset_info.file_format
    if file_format != file_adapters.FileFormat.ARRAY_RECORD:
      raise NotImplementedError(
          f'No random access data source for file format {file_format}. Please,'
          ' generate your data using `tfds.builder(...,'
          f' file_format={file_adapters.FileFormat.ARRAY_RECORD})`.'
      )
    split_infos = self.dataset_info.splits.values()
    splits_dict = splits_lib.SplitDict(split_infos=split_infos)
    file_instructions = splits_dict[self.split].file_instructions
    self.data_source = array_record_data_source.ArrayRecordDataSource(
        file_instructions
    )
    self.length = len(self.data_source)

  def __len__(self) -> int:
    return self.length

  def __iter__(self):
    for i in range(self.length):
      yield self[i]

  def __getitem__(self, record_key: int) -> Any:
    if not isinstance(record_key, int):
      logging.error(
          'Calling ArrayRecordDataSource.__getitem__() with sequence '
          'of record keys (%s) is deprecated. Either pass a single '
          'integer or switch to __getitems__().',
          record_key,
      )
      return self.__getitems__(record_key)
    record = self.data_source[record_key]
    return self.dataset_info.features.deserialize_example_np(
        record, decoders=self.decoders
    )

  def __getitems__(self, record_keys: Sequence[int]) -> Sequence[Any]:
    """Retrieves items by batch.

    This method allows PyTorch to load records by batch, rather than one by one.

    Args:
      record_keys: a sequence of keys.

    Returns:
      The records associated with the keys.

    Raises:
      IndexError: If the number of retrieved records is incorrect.
    """
    records = self.data_source.__getitems__(record_keys)
    features = self.dataset_info.features
    if len(record_keys) != len(records):
      raise IndexError(
          f'Requested {len(record_keys)} records but got'
          f' {len(records)} records.'
          f'{record_keys=}, {records=}'
      )
    return [
        features.deserialize_example_np(record, decoders=self.decoders)
        for record in records
    ]

  def __repr__(self) -> str:
    decoders_repr = (
        tree.map_structure(type, self.decoders) if self.decoders else None
    )
    return (
        f'DataSource(name={self.dataset_info.name}, '
        f'split={self.split!r}, '
        f'decoders={decoders_repr})'
    )
