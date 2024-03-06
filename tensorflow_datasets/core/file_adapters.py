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

"""Adapters for file formats."""

from __future__ import annotations

import abc
from collections.abc import Iterator
import enum
import itertools
import os
from typing import Any, ClassVar, Dict, Iterable, List, Optional, Type, TypeVar, Union

from etils import epath
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import array_record_module
from tensorflow_datasets.core.utils.lazy_imports_utils import parquet as pq
from tensorflow_datasets.core.utils.lazy_imports_utils import pyarrow as pa
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

ExamplePositions = List[Any]
T = TypeVar('T')


class FileFormat(enum.Enum):
  """Format of the record files.

  The values of the enumeration are used as filename endings/suffix.
  """

  TFRECORD = 'tfrecord'
  RIEGELI = 'riegeli'
  ARRAY_RECORD = 'array_record'
  PARQUET = 'parquet'

  @property
  def file_suffix(self) -> str:
    return ADAPTER_FOR_FORMAT[self].FILE_SUFFIX

  @classmethod
  def with_random_access(cls) -> set[FileFormat]:
    """File formats with random access."""
    return {
        file_format
        for file_format, adapter in ADAPTER_FOR_FORMAT.items()
        if adapter.SUPPORTS_RANDOM_ACCESS
    }

  @classmethod
  def from_value(cls, file_format: Union[str, 'FileFormat']) -> 'FileFormat':
    try:
      return cls(file_format)
    except ValueError as e:
      all_values = [f.value for f in cls]
      raise ValueError(
          f'{file_format} is not a valid FileFormat! '
          f'Valid file formats: {all_values}'
      ) from e


DEFAULT_FILE_FORMAT = FileFormat.TFRECORD


class FileAdapter(abc.ABC):
  """Interface for Adapter objects which read and write examples in a format."""

  FILE_SUFFIX: ClassVar[str]
  SUPPORTS_RANDOM_ACCESS: ClassVar[bool]
  BUFFER_SIZE = 8 << 20  # 8 MiB per file.

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
  SUPPORTS_RANDOM_ACCESS = False

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: Optional[int] = None,
  ) -> tf.data.Dataset:
    """Returns TensorFlow Dataset comprising given record file."""
    buffer_size = buffer_size or cls.BUFFER_SIZE
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
  SUPPORTS_RANDOM_ACCESS = False

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: Optional[int] = None,
  ) -> tf.data.Dataset:
    buffer_size = buffer_size or cls.BUFFER_SIZE
    from riegeli.tensorflow.ops import riegeli_dataset_ops as riegeli_tf  # pylint: disable=g-import-not-at-top  # pytype: disable=import-error

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


class ArrayRecordFileAdapter(FileAdapter):
  """File adapter for ArrayRecord file format."""

  FILE_SUFFIX = 'array_record'
  SUPPORTS_RANDOM_ACCESS = True

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: Optional[int] = None,
  ) -> tf.data.Dataset:
    """Returns TensorFlow Dataset comprising given array record file."""
    raise NotImplementedError(
        '`.as_dataset()` not implemented for ArrayRecord files. Please, use'
        ' `.as_data_source()`.'
    )

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
    writer = array_record_module.ArrayRecordWriter(
        os.fspath(path), 'group_size:1'
    )
    for _, serialized_example in iterator:
      writer.write(serialized_example)
    writer.close()


class ParquetFileAdapter(FileAdapter):
  """File adapter for the [Parquet](https://parquet.apache.org) file format.

  This FileAdapter requires `pyarrow` as a dependency and builds upon
  `pyarrow.parquet`.

  At the moment, the Parquet adapter doesn't leverage Parquet's columnar
  features and behaves like any other adapter. Instead of saving the features in
  the columns, we use one single `data` column where we store the serialized
  tf.Example proto.

  TODO(b/317277518): Let Parquet handle the serialization/deserialization.
  """

  FILE_SUFFIX = 'parquet'
  SUPPORTS_RANDOM_ACCESS = True
  _PARQUET_FIELD = 'data'
  _BATCH_SIZE = 100

  @classmethod
  def _schema(cls) -> pa.Schema:
    """Returns the Parquet schema as a one-column `data` binary field."""
    return pa.schema([pa.field(cls._PARQUET_FIELD, pa.binary())])

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: int | None = None,
  ) -> tf.data.Dataset:
    """Reads a Parquet file as a tf.data.Dataset.

    Args:
      filename: Path to the Parquet file.
      buffer_size: Unused buffer size.

    Returns:
      A tf.data.Dataset with the serialized examples.
    """
    del buffer_size  # unused

    def get_data(py_filename: bytes) -> Iterator[tf.Tensor]:
      table = pq.read_table(py_filename.decode(), schema=cls._schema())
      for batch in table.to_batches():
        for example in batch.to_pylist():
          yield tf.constant(example[cls._PARQUET_FIELD])

    return tf.data.Dataset.from_generator(
        get_data,
        args=(filename,),
        output_signature=tf.TensorSpec(shape=(), dtype=tf.string),
    )

  @classmethod
  def write_examples(
      cls,
      path: epath.PathLike,
      iterator: Iterable[type_utils.KeySerializedExample],
  ) -> None:
    """Writes the serialized tf.Example proto in a binary field named `data`.

    Args:
      path: Path to the Parquet file.
      iterator: Iterable of serialized examples.
    """
    with pq.ParquetWriter(path, schema=cls._schema()) as writer:
      for examples in _batched(iterator, cls._BATCH_SIZE):
        examples = [{cls._PARQUET_FIELD: example} for _, example in examples]
        batch = pa.RecordBatch.from_pylist(examples)
        writer.write_batch(batch)
    return None


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
    FileFormat.ARRAY_RECORD: ArrayRecordFileAdapter,
    FileFormat.PARQUET: ParquetFileAdapter,
}

_FILE_SUFFIX_TO_FORMAT = {
    adapter.FILE_SUFFIX: file_format
    for file_format, adapter in ADAPTER_FOR_FORMAT.items()
}


def file_format_from_suffix(file_suffix: str) -> FileFormat:
  """Returns the file format associated with the file extension (`tfrecord`)."""
  if file_suffix not in _FILE_SUFFIX_TO_FORMAT:
    raise ValueError(
        'Unrecognized file extension: Should be one of '
        f'{list(_FILE_SUFFIX_TO_FORMAT.values())}'
    )
  return _FILE_SUFFIX_TO_FORMAT[file_suffix]


def is_example_file(filename: str) -> bool:
  """Whether the given filename is a record file."""
  return any(
      f'.{adapter.FILE_SUFFIX}' in filename
      for adapter in ADAPTER_FOR_FORMAT.values()
  )


def _batched(iterator: Iterator[T] | Iterable[T], n: int) -> Iterator[List[T]]:
  """Batches the result of an iterator into lists of length n.

  This function is built-in the standard library from 3.12 (source:
  https://docs.python.org/3/library/itertools.html#itertools.batched). However,
  TFDS supports older versions of Python.

  Args:
    iterator: The iterator to batch.
    n: The maximal length of each batch.

  Yields:
    The next list of n elements.
  """
  i = 0
  while True:
    batch = list(itertools.islice(iterator, i, i + n))
    if not batch:
      return
    yield batch
    i += n
