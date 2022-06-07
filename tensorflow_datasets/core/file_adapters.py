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

"""Adapters for file formats."""

import abc
import enum
import os
from typing import Any, ClassVar, Dict, Iterable, List, Optional, Type, Union

from etils import epath
import tensorflow as tf
from tensorflow_datasets.core.utils import type_utils

ExamplePositions = List[Any]


class FileFormat(enum.Enum):
  """Format of the record files.

  The values of the enumeration are used as filename endings/suffix.
  """
  TFRECORD = 'tfrecord'
  RIEGELI = 'riegeli'

  @property
  def file_suffix(self) -> str:
    return ADAPTER_FOR_FORMAT[self].FILE_SUFFIX

  @classmethod
  def from_value(cls, file_format: Union[str, 'FileFormat']) -> 'FileFormat':
    try:
      return cls(file_format)
    except ValueError as e:
      all_values = [f.value for f in cls]
      raise ValueError(f'{file_format} is not a valid FileFormat! '
                       f'Valid file formats: {all_values}') from e


DEFAULT_FILE_FORMAT = FileFormat.TFRECORD


class FileAdapter(abc.ABC):
  """Interface for Adapter objects which read and write examples in a format."""

  FILE_SUFFIX: ClassVar[str]

  @classmethod
  @abc.abstractmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: Optional[int] = None,
  ) -> tf.data.Dataset:
    """Returns TensorFlow Dataset comprising given record file."""
    raise NotImplementedError()

  @classmethod
  @abc.abstractmethod
  def write_examples(
      cls,
      path: epath.PathLike,
      iterator: Iterable[type_utils.KeySerializedExample],
  ) -> Optional[ExamplePositions]:
    """Write examples from given iterator in given path.

    Args:
      path: Path where to write the examples.
      iterator: Iterable of examples.

    Returns:
      List of record positions for each record in the given iterator. In case of
      TFRecords, does not return anything.
    """
    raise NotImplementedError()


class TfRecordFileAdapter(FileAdapter):
  """File adapter for TFRecord file format."""

  FILE_SUFFIX = 'tfrecord'

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: Optional[int] = None,
  ) -> tf.data.Dataset:
    """Returns TensorFlow Dataset comprising given record file."""
    return tf.data.TFRecordDataset(filename, buffer_size=buffer_size)

  @classmethod
  def write_examples(
      cls,
      path: epath.PathLike,
      iterator: Iterable[type_utils.KeySerializedExample],
  ) -> Optional[ExamplePositions]:
    """Write examples from given iterator in given path.

    Args:
      path: Path where to write the examples.
      iterator: Iterable of examples.

    Returns:
      None
    """
    with tf.io.TFRecordWriter(os.fspath(path)) as writer:
      for _, serialized_example in iterator:
        writer.write(serialized_example)
      writer.flush()


class RiegeliFileAdapter(FileAdapter):
  """File adapter for Riegeli file format."""

  FILE_SUFFIX = 'riegeli'

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: Optional[int] = None,
  ) -> tf.data.Dataset:
    from riegeli.tensorflow.ops import riegeli_dataset_ops as riegeli_tf  # pylint: disable=g-import-not-at-top
    return riegeli_tf.RiegeliDataset(filename, buffer_size=buffer_size)

  @classmethod
  def write_examples(
      cls,
      path: epath.PathLike,
      iterator: Iterable[type_utils.KeySerializedExample],
  ) -> Optional[ExamplePositions]:
    """Write examples from given iterator in given path.

    Args:
      path: Path where to write the examples.
      iterator: Iterable of examples.

    Returns:
      List of record positions for each record in the given iterator.
    """
    positions = []
    import riegeli  # pylint: disable=g-import-not-at-top
    with tf.io.gfile.GFile(os.fspath(path), 'wb') as f:
      with riegeli.RecordWriter(f, options='transpose') as writer:
        for _, record in iterator:
          writer.write_record(record)
          positions.append(writer.last_pos)
    return positions


def _to_bytes(key: type_utils.Key) -> bytes:
  """Convert the key to bytes."""
  if isinstance(key, int):
    return key.to_bytes(128, byteorder='big')  # Use 128 as this match md5
  elif isinstance(key, bytes):
    return key
  elif isinstance(key, str):
    return key.encode('utf-8')
  else:
    raise TypeError(f'Invalid key type: {type(key)}')


# Create a mapping from FileFormat -> FileAdapter.
ADAPTER_FOR_FORMAT: Dict[FileFormat, Type[FileAdapter]] = {
    FileFormat.RIEGELI: RiegeliFileAdapter,
    FileFormat.TFRECORD: TfRecordFileAdapter,
}

_FILE_SUFFIX_TO_FORMAT = {
    adapter.FILE_SUFFIX: file_format
    for file_format, adapter in ADAPTER_FOR_FORMAT.items()
}


def file_format_from_suffix(file_suffix: str) -> FileFormat:
  """Returns the file format associated with the file extension (`tfrecord`)."""
  if file_suffix not in _FILE_SUFFIX_TO_FORMAT:
    raise ValueError('Unrecognized file extension: Should be one of '
                     f'{list(_FILE_SUFFIX_TO_FORMAT.values())}')
  return _FILE_SUFFIX_TO_FORMAT[file_suffix]


def is_example_file(filename: str) -> bool:
  """Whether the given filename is a record file."""
  return any(f'.{adapter.FILE_SUFFIX}' in filename
             for adapter in ADAPTER_FOR_FORMAT.values())
