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

"""Writer to sequentially write examples to disk."""

from __future__ import annotations

import dataclasses
import os
from typing import Any, Dict, List, Optional

from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import features as features_lib
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf



def _serialize_example(example: Any, features: features_lib.FeaturesDict,
                       serializer: example_serializer.ExampleSerializer) -> str:
  try:
    encoded_example = features.encode_example(example)
  except Exception as e:  # pylint: disable=broad-except
    py_utils.reraise(
        e, prefix='Failed to encode example:\n', suffix=f'{example}\n')

  return serializer.serialize_example(encoded_example)


@dataclasses.dataclass
class Shard(object):
  """Shard that is being written."""
  writer: tf.io.TFRecordWriter  # TODO(sabela): use a file adapter
  num_examples: int = 0
  num_bytes: int = 0

  def add_example(self, serialized_example: str) -> None:
    """Writes a new example."""
    self.writer.write(serialized_example)
    self.num_examples += 1
    self.num_bytes += len(serialized_example)

  def close_writer(self) -> None:
    """CLoses the writer."""
    self.writer.flush()
    self.writer.close()


@dataclasses.dataclass
class Split(object):
  """Information of a split that is being created."""
  info: splits_lib.SplitInfo
  current_shard: Optional[Shard] = None
  complete_shards: int = 0
  # The dataset name is taken from the builder class.
  ds_name: str = ''
  closed: bool = False

  def add_example(self, serialized_example: str) -> None:
    """Adds an example to the shard.

    If there is no open shard, it starts a new one.

    Args:
      serialized_example: example to add to the shard.

    Raises:
      ValueError: if the split is already closed.
    """
    if self.closed:
      raise ValueError(f'Split {self.info.name} is already closed.')
    if self.current_shard is None:
      path = self.info.filename_template.sharded_filepath(
          shard_index=self.complete_shards, num_shards=None)
      self.current_shard = Shard(writer=tf.io.TFRecordWriter(os.fspath(path)))
    self.current_shard.add_example(serialized_example)

  def close_shard(self) -> None:
    """Finalizes a shard and updates the split metadata accordingly."""
    if not self.current_shard:
      return
    self.current_shard.close_writer()
    self.info = splits_lib.SplitInfo(
        name=self.info.name,
        shard_lengths=self.info.shard_lengths +
        [self.current_shard.num_examples],
        num_bytes=self.info.num_bytes + self.current_shard.num_bytes,
        filename_template=self.info.filename_template)
    self.complete_shards += 1
    self.current_shard = None

  def close(self) -> None:
    """Closes the split (and the shard if it is still open)."""
    if not self.closed and self.current_shard:
      self.close_shard()
    self.closed = True


def _split_dict(splits: Dict[str, Split]) -> splits_lib.SplitDict:
  return splits_lib.SplitDict([split.info for _, split in splits.items()])


def _initialize_split(split_name: str,
                      data_directory: Any,
                      ds_name: str,
                      filetype_suffix: str,
                      shard_lengths: Optional[List[int]] = None,
                      num_bytes: int = 0) -> Split:
  """Initializes a split.

  Args:
    split_name: name of the split.
    data_directory: directory where the split data will be located.
    ds_name: name of the dataset.
    filetype_suffix: file format.
    shard_lengths: if the split already has shards, it contains the list of the
      shard lenghts. If None, it assumes that the split is empty.
    num_bytes: number of bytes that have been written already.
  Returns:
    A Split.
  """
  if not shard_lengths:
    shard_lengths = []
  filename_template = naming.ShardedFileTemplate(
      dataset_name=ds_name,
      data_dir=data_directory,
      split=split_name,
      filetype_suffix=filetype_suffix,
      template='{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_INDEX}',
  )
  return Split(
      info=splits_lib.SplitInfo(
          name=split_name,
          shard_lengths=shard_lengths,
          num_bytes=num_bytes,
          filename_template=filename_template),
      complete_shards=len(shard_lengths),
      ds_name=ds_name)


class SequentialWriter():
  """Class to write a TFDS dataset sequentially.

  The SequentialWriter can be used to generate TFDS datasets by directly
  appending TF Examples to the desired splits.

  Once the user creates a SequentialWriter with a given DatasetInfo, they can
  create splits, append examples to them, and close them whenever they are
  finished.

  Note that:
  * Not closing a split may cause data to be lost.
  * The examples are written to disk in the same order that they are given to
    the writer.
  * Since the SequentialWriter doesn't know how many examples are going to be
    written, it can't estimate the optimal number of shards per split. Use the
    `max_examples_per_shard` parameter in the constructor to control how many
    elements there should be per shard.

  The datasets written with this writer can be read directly with
  `tfds.builder_from_directories`.

  Example:

  writer = SequentialWriter(ds_info=ds_info, max_examples_per_shard=1000)
  writer.initialize_splits(['train', 'test'])

  while (...):
    # Code that generates the examples
    writer.add_examples({'train': [example1, example2],
                         'test':  [example3]})
    ...

  writer.close_splits()

  """

  # TODO(sabela): add support for beam.
  # TODO(sabela): add support for build_configs.
  # TODO(sabela): support non-TFRecord writers. At the moment, the FileAdapters
  # API only suports writing a set of examples, so the support for other formats
  # would have to be manual.
  def __init__(self,
               ds_info: dataset_info.DatasetInfo,
               max_examples_per_shard: int,
               overwrite: bool = True):
    """Creates a SequentialWriter.

    Args:
      ds_info: DatasetInfo for this dataset.
      max_examples_per_shard: maximum number of examples to write per shard.
      overwrite: if True, it ignores and overwrites any existing data.
        Otherwise, it loads the existing dataset and appends the new data (new
        data will always be created as new shards).
    """

    self._data_dir = ds_info.data_dir
    self._ds_name = ds_info.name
    self._ds_info = ds_info
    if not overwrite:
      try:
        self._ds_info.read_from_directory(self._data_dir)
        # read_from_directory does some checks but not on the dataset name.
        if self._ds_info.name != self._ds_name:
          raise ValueError(
              f'Trying to append a dataset with name {ds_info.name}'
              f' to an existing dataset with name {self._ds_info.name}')
      except FileNotFoundError:
        self._ds_info.set_file_format(
            file_format=file_adapters.FileFormat.TFRECORD,
            # if it was set, we want this to fail to warn the user
            override=False)
    else:
      self._ds_info.set_file_format(
          file_format=file_adapters.FileFormat.TFRECORD,
          # if it was set, we want this to fail to warn the user
          override=False)

    self._filetype_suffix = ds_info.file_format.file_suffix
    self._max_examples_per_shard = max_examples_per_shard
    self._splits = {}
    if not overwrite:
      for split_name, split in ds_info.splits.items():
        self._splits[split_name] = _initialize_split(
            split_name=split_name,
            data_directory=self._data_dir,
            ds_name=self._ds_name,
            filetype_suffix=self._filetype_suffix,
            shard_lengths=split.shard_lengths,
            num_bytes=split.num_bytes)
    self._serializer = example_serializer.ExampleSerializer(
        self._ds_info.features.get_serialized_info())

  def initialize_splits(self,
                        splits: List[str],
                        fail_if_exists: bool = True) -> None:
    """Adds new splits to the dataset.

    Args:
      splits: list of split names to add.
      fail_if_exists: will fail if this split already contains data.

    Raises:
      KeyError: if the split is already present.
    """
    for split in splits:
      if split in self._splits:
        if fail_if_exists:
          raise KeyError(f'Split {split} was already initialized.')
        else:
          continue
      self._splits[split] = _initialize_split(
          split_name=split,
          data_directory=self._data_dir,
          ds_name=self._ds_name,
          filetype_suffix=self._filetype_suffix)
    self._write_splits_metadata()

  def add_examples(self, split_examples: Dict[str, List[Any]]) -> None:
    """Adds examples to the splits.

    Args:
      split_examples: dictionary of `split_name`:list_of_examples that includes
        the list of examples that has to be added to each of the splits. Not
        all the existing splits have to be in the dictionary

    Raises:
      KeyError: if any of the splits doesn't exist.
    """
    # Write the example and update the shard
    for split_name, examples in split_examples.items():
      split = self._splits.get(split_name, None)
      if not split:
        raise KeyError(f'Split {split} was not initialized.')
      for example in examples:
        serialized_example = _serialize_example(example, self._ds_info.features,
                                                self._serializer)
        split.add_example(serialized_example)
        if split.current_shard.num_examples >= self._max_examples_per_shard:
          split.close_shard()
    self._write_splits_metadata()

  def _write_splits_metadata(self) -> None:
    self._ds_info.set_splits(_split_dict(self._splits))
    # Either writes the first metadata, or overwrites it.
    self._ds_info.write_to_directory(self._data_dir)

  def close_splits(self, splits: List[str]) -> None:
    """Closes the given list of splits.

    Args:
      splits: list of split names.

    Raises:
      KeyError: if any of the splits doesn't exist.
    """
    for split_name in splits:
      if split_name not in self._splits:
        raise KeyError(f'Split {split_name} was not created.')
      split = self._splits[split_name]
      split.close()
    self._write_splits_metadata()

  def close_all(self) -> None:
    """Closes all the open splits."""
    for _, split in self._splits.items():
      split.close()
    self._write_splits_metadata()
