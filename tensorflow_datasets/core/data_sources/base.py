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

"""DataSource base class. See the `Base` class docstring for more context."""

from collections.abc import MappingView, Sequence
import dataclasses
import typing
from typing import Any, Generic, Iterable, Protocol, SupportsIndex, TypeVar

from absl import logging
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.utils import shard_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tree

T = TypeVar('T')


@typing.runtime_checkable
class DataSource(Protocol, Generic[T]):
  """Interface for datasources where storage supports efficient random access."""

  def __len__(self) -> int:
    """Returns the total number of records in the data source."""

  def __getitem__(self, key: SupportsIndex) -> T:
    """Returns the value for the given `key`."""

  def __getitems__(self, keys: Iterable[int]) -> T:
    """Returns the value for the given `keys`."""


def file_instructions(
    dataset_info: dataset_info_lib.DatasetInfo,
    split: splits_lib.Split | None = None,
) -> list[shard_utils.FileInstruction]:
  """Retrieves the file instructions from the DatasetInfo."""
  split_infos = dataset_info.splits.values()
  split_dict = splits_lib.SplitDict(split_infos=split_infos)
  return split_dict[split].file_instructions


@dataclasses.dataclass
class BaseDataSource(MappingView, Sequence):
  """Base DataSource to override all dunder methods with the deserialization.

  In order to add a new data source, you can extend BaseDataSource. In the
  __post_init__, you need to define `data_source` which is the underlying data
  source for the file format you define. BaseDataSource will take care of the
  deserialization/decoding.

  Attributes:
    dataset_info: The DatasetInfo of the
    split: The split to load in the data source.
    decoders: Optional decoders for decoding.
    data_source: The underlying data source to initialize in the __post_init__.
    deserialize_method: How to deserialize the bytes that are read before
      returning.
  """

  dataset_info: dataset_info_lib.DatasetInfo
  split: splits_lib.Split | None = None
  decoders: type_utils.TreeDict[decode.partial_decode.DecoderArg] | None = None
  data_source: DataSource[Any] = dataclasses.field(init=False)
  deserialize_method: decode.DeserializeMethod = (
      decode.DeserializeMethod.DESERIALIZE_AND_DECODE
  )

  def _deserialize(self, record: Any) -> Any:
    match self.deserialize_method:
      case decode.DeserializeMethod.RAW_BYTES:
        return record
      case decode.DeserializeMethod.DESERIALIZE_NO_DECODE:
        if file_format := self.dataset_info.file_format:
          return file_format.deserialize(record)
        raise ValueError('No file format set, cannot deserialize bytes!')
      case decode.DeserializeMethod.DESERIALIZE_AND_DECODE:
        if features := self.dataset_info.features:
          return features.deserialize_example_np(record, decoders=self.decoders)  # pylint: disable=attribute-error
        raise ValueError('No features set, cannot decode example!')

  def __getitem__(self, key: SupportsIndex) -> Any:
    record = self.data_source[key.__index__()]
    return self._deserialize(record)

  def __getitems__(self, keys: Sequence[int]) -> Sequence[Any]:
    """Retrieves items by batch.

    This method allows PyTorch to load records by batch, rather than one by one.

    Args:
      keys: a sequence of keys.

    Returns:
      The records associated with the keys.

    Raises:
      IndexError: If the number of retrieved records is incorrect.
    """
    if not keys:
      return []
    records = self.data_source.__getitems__(keys)
    if len(keys) != len(records):
      raise IndexError(
          f'Requested {len(keys)} records but got {len(records)} records.'
          f'{keys=}, {records=}'
      )
    return [self._deserialize(record) for record in records]

  def __repr__(self) -> str:
    decoders_repr = (
        tree.map_structure(type, self.decoders) if self.decoders else None
    )
    return (
        f'{self.__class__.__name__}(name={self.dataset_info.name}, '
        f'split={self.split!r}, '
        f'decoders={decoders_repr})'
    )

  def __len__(self) -> int:
    return self.data_source.__len__()

  def __iter__(self):
    for i in range(self.__len__()):
      yield self[i]
