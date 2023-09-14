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

"""Defined Reader and ReadInstruction to read tfrecord files."""

from __future__ import annotations

import functools
import os
import re
from typing import Any, Callable, List, NamedTuple, Optional, Sequence

from absl import logging
import numpy as np
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import tf_compat
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.core.utils import shard_utils
from tensorflow_datasets.core.utils import tree_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

Tree = utils.Tree
TreeDict = utils.TreeDict
Tensor = utils.Tensor

ParseFn = Callable[[Tensor], TreeDict[Tensor]]
DecodeFn = Callable[[TreeDict[Tensor]], TreeDict[Tensor]]


# Use NamedTuple, as it is preserved by `tf.data.Dataset`
class _IdExample(NamedTuple):
  id: Any  # tf.string
  example: Any  # TreeDict[tf.any]


class _Instruction(NamedTuple):
  filepath: tf.string  # e.g. '/path/to/../train.tfrecord'
  filename: tf.string  # e.g. 'train.tfrecord'
  tfds_id_prefix: tf.string  # e.g. 'train.tfrecord' or 'folder1/train.tfrecord'
  skip: tf.int64
  take: tf.int64


def _get_dataset_from_filename(
    instruction: _Instruction,
    do_skip: bool,
    do_take: bool,
    file_format: file_adapters.FileFormat,
    add_tfds_id: bool,
    override_buffer_size: Optional[int] = None,
) -> tf.data.Dataset:
  """Returns a tf.data.Dataset instance from given instructions."""
  ds = file_adapters.ADAPTER_FOR_FORMAT[file_format].make_tf_data(
      instruction.filepath, buffer_size=override_buffer_size
  )
  if do_skip:
    ds = ds.skip(instruction.skip)
  if do_take:
    ds = ds.take(instruction.take)
  if add_tfds_id:  # For each example, generate a unique id.
    id_ds = _make_id_dataset(
        filename=instruction.tfds_id_prefix,
        start_index=instruction.skip if do_skip else 0,
    )
    ds = tf.data.Dataset.zip(_IdExample(id=id_ds, example=ds))
  return ds


def _make_id(
    filename: tf.Tensor,  # tf.Tensor[tf.string]
    index: tf.Tensor,  # tf.Tensor[tf.int64]
) -> tf.Tensor:  # tf.Tensor[tf.int64]
  """Creates the unique example ID."""
  return tf.strings.join(
      [filename, tf.strings.as_string(index)],
      separator='__',
  )


def _make_id_dataset(
    filename: tf.Tensor,  # tf.Tensor[tf.string]
    start_index: tf.Tensor,  # tf.Tensor[tf.int64]
) -> tf.data.Dataset:
  """Creates the dataset generating unique example IDs."""
  ds = tf.data.experimental.Counter(start_index)
  ds = ds.map(lambda index: _make_id(filename=filename, index=index))
  return ds


def _decode_with_id(
    id_ex: _IdExample,
    decode_fn: DecodeFn,
) -> TreeDict[Tensor]:
  """Add the `'tfds_id': ...` to the decoded example `dict`."""
  if not isinstance(id_ex, _IdExample):
    raise TypeError(
        f'Reader should return _IdExample when `add_tfds_id=True`. Got: {id_ex}'
    )
  decoded_ex = decode_fn(id_ex.example)
  if not isinstance(decoded_ex, dict):
    raise TypeError(
        f'Features should be `dict` when `add_tfds_id=True`. Got: {decoded_ex}'
    )
  decoded_ex['tfds_id'] = id_ex.id
  return decoded_ex


def _get_tfds_id_prefixes(
    file_instructions: Sequence[shard_utils.FileInstruction],
) -> dict[str, str]:
  """Returns the tfds id prefix per filename.

  If the file instructions are for files in different directories, then the TFDS
  id prefix includes part of the folder. This is to avoid duplicate TFDS ids
  when different directories contain the same filenames. For example, if the
  file instructions contain file paths `['/a/b/c', '/x/y/c']`, then this returns
  `{'/a/b/c': 'b/c', '/x/y/c': 'y/c'}`.

  Arguments:
    file_instructions: the file instructions for which to get TFDS id prefixes.

  Returns:
    the TFDS id prefix per filename.
  """
  dirnames = set(i.dirname() for i in file_instructions)
  reversed_dirnames = [d[::-1] for d in dirnames]
  common_suffix = os.path.commonprefix(reversed_dirnames)[::-1]

  def get_tfds_id(instruction: shard_utils.FileInstruction) -> str:
    # Return the file name when all files are in the same directory.
    if len(dirnames) == 1:
      return instruction.basename()
    # Otherwise, return the relative path starting from the deepest folder that
    # differs.
    return re.sub(
        rf'.*\/([^/]+{common_suffix}/[^/]+)', r'\1', instruction.filename
    )

  return {fi.filename: get_tfds_id(fi) for fi in file_instructions}


def _read_files(
    file_instructions: Sequence[shard_utils.FileInstruction],
    read_config: read_config_lib.ReadConfig,
    shuffle_files: bool,
    disable_shuffling: bool,
    file_format: file_adapters.FileFormat,
) -> tf.data.Dataset:
  """Returns tf.data.Dataset for given file instructions.

  Args:
    file_instructions: the information on the files to read including
      `ds.skip().take()`
    read_config: Additional options to configure the input pipeline (e.g. seed,
      num parallel reads,...).
    shuffle_files: Defaults to False. True to shuffle input files.
    disable_shuffling: Specifies if the dataset being read has shuffling
      disabled.
    file_format: Format of the record files in which the dataset will be
      read/written from.

  Returns:
    The dataset object.
  """

  def assert_cardinality_and_apply_options(ds):
    # If the number of examples read in the tf-record is known, we forward
    # the information to the tf.data.Dataset object.
    # Check the `tf.data.experimental` for backward compatibility with TF <= 2.1
    if (
        read_config.assert_cardinality
        and not read_config.input_context
        and hasattr(  # TODO(epot): Restore cardinality
            tf.data.experimental, 'assert_cardinality'
        )
    ):
      # TODO(b/154963426): Replace by per-shard cardinality (warning if
      # `experimental_interleave_sort_fn` is set).
      cardinality = sum(f.take for f in file_instructions)
      ds = ds.apply(tf.data.experimental.assert_cardinality(cardinality))

    return ds.with_options(read_config.options)  # Additional users options

  def validate_input_context():
    if not read_config.input_context:
      raise ValueError(
          'Cannot shard the pipeline with undefined `input_context`.'
      )
    try:
      num_input_pipelines = int(read_config.input_context.num_input_pipelines)
    except TypeError as e:
      logging.warning('Unable to validate `read_config.input_context`: %s', e)
      return
    if num_input_pipelines > 1 and len(file_instructions) < num_input_pipelines:
      raise ValueError(
          'Cannot shard the pipeline with given `input_context`.'
          '`num_shards={}` but `num_input_pipelines={}`. This means that some '
          "workers won't read any data. To shard the data, you may want to "
          'use the subsplit API instead: '
          'https://www.tensorflow.org/datasets/splits'.format(
              len(file_instructions),
              read_config.input_context.num_input_pipelines,
          )
      )

  # Eventually apply a transformation to the instruction function.
  # This allow the user to have direct control over the interleave order.
  if read_config.experimental_interleave_sort_fn is not None:
    file_instructions = read_config.experimental_interleave_sort_fn(
        file_instructions
    )

  do_skip = any(f.skip > 0 for f in file_instructions)
  do_take = any(not f.takes_all for f in file_instructions)

  tfds_id_prefixes = _get_tfds_id_prefixes(file_instructions)

  # Transpose the list[dict] into dict[list]
  tensor_inputs = _Instruction(
      filename=[os.path.basename(i.filename) for i in file_instructions],
      filepath=[os.fspath(i.filename) for i in file_instructions],
      tfds_id_prefix=[tfds_id_prefixes[i.filename] for i in file_instructions],
      # skip/take need to be converted to int64 explicitly
      skip=np.array([i.skip for i in file_instructions], dtype=np.int64),
      take=np.array([i.take for i in file_instructions], dtype=np.int64),
  )

  cycle_length = read_config.interleave_cycle_length
  block_length = read_config.interleave_block_length

  if cycle_length == read_config_lib.MISSING:
    cycle_length = _get_default_interleave_cycle_length(
        disable_shuffling=disable_shuffling
    )

  if disable_shuffling:
    _verify_read_config_for_ordered_dataset(
        read_config,
        interleave_cycle_length=cycle_length,
        shuffle_files=shuffle_files,
    )


  unique_folders = set(os.path.dirname(path) for path in tensor_inputs.filepath)
  logging.info(
      'Creating a tf.data.Dataset reading %d files located in folders: %s.',
      len(tensor_inputs.filepath),
      ', '.join(sorted(unique_folders)),
  )

  instruction_ds = tf.data.Dataset.from_tensor_slices(tensor_inputs)

  # On distributed environments, we can shard per-file if a
  # `tf.distribute.InputContext` object is provided (e.g. from
  # `experimental_distribute_datasets_from_function`)
  if read_config.input_context:
    validate_input_context()
    instruction_ds = instruction_ds.shard(
        num_shards=read_config.input_context.num_input_pipelines,
        index=read_config.input_context.input_pipeline_id,
    )

  # If shuffle is True, we shuffle the instructions/shards
  if shuffle_files:
    instruction_ds = instruction_ds.shuffle(
        len(file_instructions),
        seed=read_config.shuffle_seed,
        reshuffle_each_iteration=read_config.shuffle_reshuffle_each_iteration,
    )

  if read_config.repeat_filenames:
    instruction_ds = instruction_ds.repeat()

  deterministic = True
  # If shuffling is true and the seed is not set, then the pipeline is allowed
  # to be non-deterministic. Note that setting the deterministic option in
  # tf.data.Options() sets this option globally. This means that also nested
  # fields will appear in undeterministic order.
  if (
      shuffle_files
      and read_config.shuffle_seed is None
      and tf_compat.get_option_deterministic(read_config.options) is None
  ):
    deterministic = False

  ds = instruction_ds.interleave(
      functools.partial(
          _get_dataset_from_filename,
          do_skip=do_skip,
          do_take=do_take,
          file_format=file_format,
          add_tfds_id=read_config.add_tfds_id,
          override_buffer_size=read_config.override_buffer_size,
      ),
      cycle_length=cycle_length,
      block_length=block_length,
      num_parallel_calls=read_config.num_parallel_calls_for_interleave_files,
      deterministic=deterministic,
  )

  return assert_cardinality_and_apply_options(ds)


def _get_default_interleave_cycle_length(disable_shuffling: bool) -> int:
  if disable_shuffling:
    logging.info(
        '`interleave_cycle_length` set to 1 to read examples in order.'
    )
    return 1
  else:
    return 16


def _verify_read_config_for_ordered_dataset(
    read_config: read_config_lib.ReadConfig,
    interleave_cycle_length: int,
    shuffle_files: bool,
) -> None:
  """Check that read parameters will not affect the ordering of the dataset.

  The user can bypass the error by setting `enable_ordering_guard=False`.

  Args:
    read_config: The input pipeline options.
    interleave_cycle_length: Cycle length for `tf.data.Dataset.interleave`.
    shuffle_files: If True, input files are shuffled before being read.
  """
  error_messages = []
  if shuffle_files:
    error_messages.append(
        "Dataset is an ordered dataset ('disable_shuffling=True'), but examples"
        ' will not be read in order because `shuffle_files=True`.'
    )
  if interleave_cycle_length != 1:
    error_messages.append(
        "Dataset is an ordered dataset ('disable_shuffling=True'), but examples"
        ' will not be read in order because `ReadConfig.interleave_cycle_length'
        ' != 1`.'
    )
  if error_messages:
    error_message = '\n'.join(error_messages)
    if read_config.enable_ordering_guard:
      raise ValueError(error_message)
    else:
      logging.warning(error_message)


class Reader(object):
  """Build a tf.data.Dataset object out of Instruction instance(s).

  This class should not typically be exposed to the TFDS user.
  """

  def __init__(
      self,
      path,  # TODO(b/216427814) remove this as it isn't used anymore
      example_specs,
      file_format=file_adapters.DEFAULT_FILE_FORMAT,
  ):
    """Initializes Reader.

    Args:
      path (str): path where tfrecords are stored.
      example_specs: spec to build ExampleParser.
      file_format: file_adapters.FileFormat, format of the record files in which
        the dataset will be read/written from.
    """
    self._path = path
    self._parser = example_parser.ExampleParser(example_specs)
    self._file_format = file_format

  def read(
      self,
      *,
      instructions: Tree[splits_lib.SplitArg],
      split_infos: List[splits_lib.SplitInfo],
      read_config: read_config_lib.ReadConfig,
      shuffle_files: bool,
      disable_shuffling: bool = False,
      decode_fn: Optional[DecodeFn] = None,
  ) -> Tree[tf.data.Dataset]:
    """Returns tf.data.Dataset instance(s).

    Args:
      instructions (ReadInstruction, List[], Dict[]): instruction(s) to read.
        Instructions can be string and will then be passed to the Instruction
        constructor as it.
      split_infos: the available splits for dataset.
      read_config: `tfds.ReadConfig`, the input pipeline options
      shuffle_files (bool): If True, input files are shuffled before being read.
      disable_shuffling: Specifies if the dataset being read has shuffling
        disabled.
      decode_fn: Eventual additional processing to apply to the example after
        deserialization.

    Returns:
       a single tf.data.Dataset instance if instruction is a single
       ReadInstruction instance. Otherwise a dict/list of tf.data.Dataset
       corresponding to given instructions param shape.
    """

    splits_dict = splits_lib.SplitDict(split_infos=split_infos)

    def _read_instruction_to_ds(instruction):
      file_instructions = splits_dict[instruction].file_instructions
      return self.read_files(
          file_instructions,
          read_config=read_config,
          shuffle_files=shuffle_files,
          disable_shuffling=disable_shuffling,
          decode_fn=decode_fn,
      )

    return tree_utils.map_structure(_read_instruction_to_ds, instructions)

  def read_files(
      self,
      file_instructions: Sequence[shard_utils.FileInstruction],
      *,
      read_config: read_config_lib.ReadConfig,
      shuffle_files: bool,
      disable_shuffling: bool = False,
      decode_fn: Optional[DecodeFn] = None,
  ) -> tf.data.Dataset:
    """Returns single tf.data.Dataset instance for the set of file instructions.

    Args:
      file_instructions: The files information. The filenames contains the
        relative path, not absolute. skip/take indicates which example read in
        the shard: `ds.skip().take()`
      read_config: The input pipeline options
      shuffle_files: If True, input files are shuffled before being read.
      disable_shuffling: Specifies if the dataset being read has shuffling
        disabled.
      decode_fn: Eventual additional processing to apply to the example after
        deserialization.

    Returns:
       a tf.data.Dataset instance.
    """
    if not file_instructions:
      msg = f'Instruction {file_instructions} corresponds to no data!'
      raise ValueError(msg)

    # Read serialized example (eventually with `tfds_id`)
    ds = _read_files(
        file_instructions=file_instructions,
        read_config=read_config,
        shuffle_files=shuffle_files,
        disable_shuffling=disable_shuffling,
        file_format=self._file_format,
    )

    # Parse and decode
    def parse_and_decode(ex: Tensor) -> TreeDict[Tensor]:
      # TODO(pierrot): `parse_example` uses
      # `tf.io.parse_single_example`. It might be faster to use `parse_example`,
      # after batching.
      # https://www.tensorflow.org/api_docs/python/tf/io/parse_example
      ex = self._parser.parse_example(ex)
      if decode_fn:
        ex = decode_fn(ex)
      return ex

    # Eventually add the `tfds_id` after the decoding
    if read_config and read_config.add_tfds_id:
      parse_and_decode = functools.partial(
          _decode_with_id, decode_fn=parse_and_decode
      )

    ds = ds.map(
        parse_and_decode,
        num_parallel_calls=read_config.num_parallel_calls_for_decode,
    )
    return ds
