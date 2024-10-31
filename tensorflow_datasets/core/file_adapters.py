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
from collections.abc import Iterable, Iterator
import enum
import itertools
import os
import re
from typing import Any, ClassVar, Type, TypeVar

from etils import epy
from tensorflow_datasets.core.utils.lazy_imports_utils import array_record_module
from tensorflow_datasets.core.utils.lazy_imports_utils import parquet as pq
from tensorflow_datasets.core.utils.lazy_imports_utils import pyarrow as pa
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  from etils import epath
  from tensorflow_datasets.core.utils import file_utils
  from tensorflow_datasets.core.utils import type_utils

  # pylint: enable=g-import-not-at-top

ExamplePositions = list[Any]
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

  def deserialize(self, raw_example: bytes) -> Any:
    """Deserializes bytes into an object, but does not decode features."""
    return ADAPTER_FOR_FORMAT[self].deserialize(raw_example)

  @classmethod
  def with_random_access(cls) -> set[FileFormat]:
    """File formats with random access."""
    return {
        file_format
        for file_format, adapter in ADAPTER_FOR_FORMAT.items()
        if adapter.SUPPORTS_RANDOM_ACCESS
    }

  @classmethod
  def with_tf_data(cls) -> set[FileFormat]:
    """File formats with tf.data support."""
    return {
        file_format
        for file_format, adapter in ADAPTER_FOR_FORMAT.items()
        if adapter.SUPPORTS_TF_DATA
    }

  @classmethod
  def with_suffix_before_shard_spec(cls) -> set[FileFormat]:
    """File formats with suffix before shard spec."""
    return {
        file_format
        for file_format, adapter in ADAPTER_FOR_FORMAT.items()
        if adapter.SUFFIX_BEFORE_SHARD_SPEC
    }

  @classmethod
  def with_suffix_after_shard_spec(cls) -> set[FileFormat]:
    """File formats with suffix after shard spec."""
    return {
        file_format
        for file_format, adapter in ADAPTER_FOR_FORMAT.items()
        if not adapter.SUFFIX_BEFORE_SHARD_SPEC
    }

  @classmethod
  def from_value(cls, file_format: str | FileFormat) -> FileFormat:
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

  # Whether the file format suffix should go before the shard spec.
  # For example, `dataset-train.tfrecord-00000-of-00001` if `True`,
  # otherwise `dataset-train-00000-of-00001.tfrecord`.
  SUFFIX_BEFORE_SHARD_SPEC: ClassVar[bool] = True

  SUPPORTS_RANDOM_ACCESS: ClassVar[bool]
  SUPPORTS_TF_DATA: ClassVar[bool]
  BUFFER_SIZE = 8 << 20  # 8 MiB per file.

  @classmethod
  @abc.abstractmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: int | None = None,
  ) -> tf.data.Dataset:
    """Returns TensorFlow Dataset comprising given record file."""
    raise NotImplementedError()

  @classmethod
  @abc.abstractmethod
  def write_examples(
      cls,
      path: epath.PathLike,
      iterator: Iterable[type_utils.KeySerializedExample],
  ) -> ExamplePositions | None:
    """Write examples from given iterator in given path.

    Args:
      path: Path where to write the examples.
      iterator: Iterable of examples.

    Returns:
      List of record positions for each record in the given iterator. In case of
      TFRecords, does not return anything.
    """
    raise NotImplementedError()

  @classmethod
  def deserialize(cls, raw_example: bytes) -> Any:
    """Returns the deserialized example, but does not decode features.

    If custom serialization is used, override this method in the file adapter.

    Args:
      raw_example: the bytes read from the source that should be deserialized.
    """
    return tf.train.Example.FromString(raw_example)


class TfRecordFileAdapter(FileAdapter):
  """File adapter for TFRecord file format."""

  FILE_SUFFIX = 'tfrecord'
  SUPPORTS_RANDOM_ACCESS = False
  SUPPORTS_TF_DATA = True

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: int | None = None,
  ) -> tf.data.Dataset:
    """Returns TensorFlow Dataset comprising given record file."""
    buffer_size = buffer_size or cls.BUFFER_SIZE
    return tf.data.TFRecordDataset(filename, buffer_size=buffer_size)

  @classmethod
  def write_examples(
      cls,
      path: epath.PathLike,
      iterator: Iterable[type_utils.KeySerializedExample],
  ) -> ExamplePositions | None:
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
  SUPPORTS_TF_DATA = True

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: int | None = None,
  ) -> tf.data.Dataset:
    buffer_size = buffer_size or cls.BUFFER_SIZE
    from riegeli.tensorflow.ops import riegeli_dataset_ops as riegeli_tf  # pylint: disable=g-import-not-at-top  # pytype: disable=import-error

    return riegeli_tf.RiegeliDataset(filename, buffer_size=buffer_size)

  @classmethod
  def write_examples(
      cls,
      path: epath.PathLike,
      iterator: Iterable[type_utils.KeySerializedExample],
  ) -> ExamplePositions | None:
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
  SUPPORTS_TF_DATA = False

  @classmethod
  def make_tf_data(
      cls,
      filename: epath.PathLike,
      buffer_size: int | None = None,
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
  ) -> ExamplePositions | None:
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
  SUPPORTS_TF_DATA = True
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
ADAPTER_FOR_FORMAT: dict[FileFormat, Type[FileAdapter]] = {
    FileFormat.ARRAY_RECORD: ArrayRecordFileAdapter,
    FileFormat.PARQUET: ParquetFileAdapter,
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


def _batched(iterator: Iterator[T] | Iterable[T], n: int) -> Iterator[list[T]]:
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


def convert_path_to_file_format(
    path: epath.PathLike, file_format: FileFormat
) -> epath.Path:
  """Returns the path to a specific shard for a different file format.

  TFDS can store the file format in the filename as a suffix or as an infix. For
  example:

  - `dataset-train.<FILE_FORMAT>-00000-of-00001`, a so-called infix format
    because the file format comes before the shard spec.
  - `dataset-train-00000-of-00001.<FILE_FORMAT>`, a so-called suffix format
    because the file format comes after the shard spec.

  Args:
    path: The path of a specific to convert. Can be the path for different file
      formats.
    file_format: The file format to which the shard path should be converted.
  """
  path = epath.Path(path)
  file_name: str = path.name
  if file_format.file_suffix in file_name:
    # Already has the right file format in the file name.
    return path

  infix_formats = FileFormat.with_suffix_before_shard_spec()
  suffix_formats = FileFormat.with_suffix_after_shard_spec()

  # Remove any existing file format from the file name.
  infix_format_concat = '|'.join(f.file_suffix for f in infix_formats)
  file_name = re.sub(rf'(\.({infix_format_concat}))', '', file_name)

  suffix_formats_concat = '|'.join(f.file_suffix for f in suffix_formats)
  file_name = re.sub(rf'(\.({suffix_formats_concat}))$', '', file_name)

  # Add back the proper file format.
  if file_format in suffix_formats:
    file_name = f'{file_name}.{file_format.file_suffix}'
  else:
    file_name = re.sub(
        r'-(\d+)-of-(\d+)',
        rf'.{file_format.file_suffix}-\1-of-\2',
        file_name,
    )
  return path.parent / file_name
