# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

import abc
import dataclasses
import functools
import math
import operator
import os
import re
from typing import Any, Callable, Dict, Iterable, List, NamedTuple, Optional, Sequence, Union

from absl import logging

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.core.utils import shard_utils

SplitInfo = Any

# Accepted split values (in `as_dataset(split=...)`)
SplitArg = Union[str, 'AbstractSplit']

Tree = utils.Tree
TreeDict = utils.TreeDict
Tensor = utils.Tensor

ParseFn = Callable[[Tensor], TreeDict[Tensor]]
DecodeFn = Callable[[TreeDict[Tensor]], TreeDict[Tensor]]

_BUFFER_SIZE = 8 << 20  # 8 MiB per file.

# <split_name>[<split_selector>] (e.g. `train[54%:]`)
_SUB_SPEC_RE = re.compile(
    r"""^
    (?P<split_name>[\w-]+)
    (\[
      (?P<split_selector>[\d\w%:-]+)
    \])?
    $""",
    re.X,  # Ignore whitespace
)
# <val><unit> (e.g. `-54%`)
_SLICE_RE = re.compile(
    r"""^
    (
        (?P<val>-?\d+)
        (?P<unit>(?:%|shard))?
    )?
    $""",
    re.X,  # Ignore whitespace
)

_ADDITION_SEP_RE = re.compile(r'\s*\+\s*')


# Use NamedTuple, as it is preserved by `tf.data.Dataset`
class _IdExample(NamedTuple):
  id: Any  # tf.string
  example: Any  # TreeDict[tf.any]


class _Instruction(NamedTuple):
  filepath: Any  # tf.string '/path/to/../train.tfrecord'
  filename: Any  # tf.string 'train.tfrecord'
  skip: Any  #  tf.int64
  take: Any  # tf.int64


def _get_dataset_from_filename(
    instruction: _Instruction,
    do_skip: bool,
    do_take: bool,
    file_format: file_adapters.FileFormat,
    add_tfds_id: bool,
):
  """Returns a tf.data.Dataset instance from given instructions."""
  ds = file_adapters.ADAPTER_FOR_FORMAT[file_format].make_tf_data(
      instruction.filepath, buffer_size=_BUFFER_SIZE)
  if do_skip:
    ds = ds.skip(instruction.skip)
  if do_take:
    ds = ds.take(instruction.take)
  if add_tfds_id:  # For each example, generate a unique id.
    id_ds = _make_id_dataset(
        filename=instruction.filename,
        start_index=instruction.skip if do_skip else 0)
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
        f'Features should be `dict` when `add_tfds_id=True`. Got: {decoded_ex}')
  decoded_ex['tfds_id'] = id_ex.id
  return decoded_ex


def make_file_instructions(
    name: str,
    split_infos: Iterable[SplitInfo],
    instruction: SplitArg,
    file_format: file_adapters.FileFormat = file_adapters.DEFAULT_FILE_FORMAT,
) -> List[shard_utils.FileInstruction]:
  """Returns instructions of the split dict.

  Args:
    name: Name of the dataset.
    split_infos: Dataset splits information
    instruction: `ReadInstruction` or `str`
    file_format: Format of the record files in which the dataset will be
      read/written from.

  Returns:
    file_intructions: FileInstructions instance
  """
  from tensorflow_datasets.core import splits as splits_lib  # pytype: disable=import-error  # pylint: disable=g-import-not-at-top

  # The code could be simplified by forwarding SplitDict everywhere
  split_infos = splits_lib.SplitDict(list(split_infos), dataset_name=name)

  if isinstance(instruction, str):
    instruction = AbstractSplit.from_spec(instruction)

  # Create the absolute instruction (per split)
  absolute_instructions = instruction.to_absolute(split_infos)

  # TODO(epot): Should try to merge the instructions together as well as
  # performing additional validation. For example, should raise an error
  # if there is overlapp between splits (`train[:50]+train[:25]`)
  # If there is a single shard, `train[:25]+train[50:75]` could be optimized
  # into a single `ds.take(25).skip(50-25).take(75-50)`

  return _make_file_instructions_from_absolutes(
      name=name,
      split_infos=split_infos,
      absolute_instructions=absolute_instructions,
      file_format=file_format,
  )


def _make_file_instructions_from_absolutes(
    name: str,
    split_infos: Dict[str, SplitInfo],
    absolute_instructions: List['_AbsoluteInstruction'],
    file_format: file_adapters.FileFormat = file_adapters.DEFAULT_FILE_FORMAT,
) -> List[shard_utils.FileInstruction]:
  """Returns the files instructions from the absolute instructions list."""
  # For each split, return the files instruction (skip/take)
  file_instructions = []
  for abs_instr in absolute_instructions:
    split_info = split_infos[abs_instr.splitname]
    if not split_info.num_examples:
      raise ValueError(
          'Shard empty. This might means that dataset hasn\'t been generated '
          'yet and info not restored from GCS, or that legacy dataset is used.')
    filenames = naming.filenames_for_dataset_split(
        dataset_name=name,
        split=abs_instr.splitname,
        num_shards=split_info.num_shards,
        filetype_suffix=file_adapters.ADAPTER_FOR_FORMAT[file_format]
        .FILE_SUFFIX)
    from_ = 0 if abs_instr.from_ is None else abs_instr.from_
    to = split_info.num_examples if abs_instr.to is None else abs_instr.to
    single_file_instructions = shard_utils.get_file_instructions(
        from_, to, filenames, split_info.shard_lengths)
    file_instructions.extend(single_file_instructions)
  return file_instructions


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
  # Eventually apply a transformation to the instruction function.
  # This allow the user to have direct control over the interleave order.
  if read_config.experimental_interleave_sort_fn is not None:
    file_instructions = read_config.experimental_interleave_sort_fn(
        file_instructions)

  do_skip = any(f.skip > 0 for f in file_instructions)
  do_take = any(f.take > -1 for f in file_instructions)

  # Transpose the list[dict] into dict[list]
  tensor_inputs = _Instruction(
      filename=[os.path.basename(i.filename) for i in file_instructions],
      filepath=[i.filename for i in file_instructions],
      # skip/take need to be converted to int64 explicitly
      skip=np.array([i.skip for i in file_instructions], dtype=np.int64),
      take=np.array([i.take for i in file_instructions], dtype=np.int64),
  )

  cycle_length = read_config.interleave_cycle_length
  block_length = read_config.interleave_block_length

  if cycle_length == read_config_lib.MISSING:
    cycle_length = _get_default_interleave_cycle_length(
        disable_shuffling=disable_shuffling)

  if disable_shuffling:
    _verify_read_config_for_ordered_dataset(
        read_config,
        interleave_cycle_length=cycle_length,
        shuffle_files=shuffle_files,
    )


  instruction_ds = tf.data.Dataset.from_tensor_slices(tensor_inputs)

  # On distributed environments, we can shard per-file if a
  # `tf.distribute.InputContext` object is provided (e.g. from
  # `experimental_distribute_datasets_from_function`)
  if (read_config.input_context and
      read_config.input_context.num_input_pipelines > 1):
    if len(file_instructions) < read_config.input_context.num_input_pipelines:
      raise ValueError(
          'Cannot shard the pipeline with given `input_context`.'
          '`num_shards={}` but `num_input_pipelines={}`. '
          'This means that some workers won\'t read any data. '
          'To shard the data, you may want to use the subsplit API '
          'instead: https://www.tensorflow.org/datasets/splits'.format(
              len(file_instructions),
              read_config.input_context.num_input_pipelines))
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

  ds = instruction_ds.interleave(
      functools.partial(
          _get_dataset_from_filename,
          do_skip=do_skip,
          do_take=do_take,
          file_format=file_format,
          add_tfds_id=read_config.add_tfds_id,
      ),
      cycle_length=cycle_length,
      block_length=block_length,
      num_parallel_calls=read_config.num_parallel_calls_for_interleave_files,
  )

  # If the number of examples read in the tf-record is known, we forward
  # the information to the tf.data.Dataset object.
  # Check the `tf.data.experimental` for backward compatibility with TF <= 2.1
  if (read_config.assert_cardinality and
      not read_config.input_context and  # TODO(epot): Restore cardinality
      hasattr(tf.data.experimental, 'assert_cardinality')):
    # TODO(b/154963426): Replace by per-shard cardinality (warning if
    # `experimental_interleave_sort_fn` is set).
    cardinality = sum(f.num_examples for f in file_instructions)
    ds = ds.apply(tf.data.experimental.assert_cardinality(cardinality))

  ds = ds.with_options(read_config.options)  # Additional users options
  return ds


def _get_default_interleave_cycle_length(disable_shuffling: bool) -> int:
  if disable_shuffling:
    logging.info(
        '`interleave_cycle_length` set to 1 to read examples in order.')
    return 1
  else:
    return 16


def _verify_read_config_for_ordered_dataset(
    read_config: read_config_lib.ReadConfig,
    interleave_cycle_length: int,
    shuffle_files: bool,
):
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
        'Dataset is an ordered dataset (\'disable_shuffling=True\'), but examples will not be read in order because `shuffle_files=True`.'
    )
  if interleave_cycle_length != 1:
    error_messages.append(
        'Dataset is an ordered dataset (\'disable_shuffling=True\'), but examples will not be read in order because `ReadConfig.interleave_cycle_length != 1`.'
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
      path,
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
      name,
      instructions: Tree[SplitArg],
      split_infos: List[SplitInfo],
      read_config,
      shuffle_files,
      disable_shuffling: bool = False,
      decode_fn: Optional[DecodeFn] = None,
  ):
    """Returns tf.data.Dataset instance(s).

    Args:
      name (str): name of the dataset.
      instructions (ReadInstruction, List[], Dict[]): instruction(s) to read.
        Instructions can be string and will then be passed to the Instruction
        constructor as it.
      split_infos (list of SplitInfo proto): the available splits for dataset.
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

    def _read_instruction_to_ds(instruction):
      file_instructions = make_file_instructions(
          name, split_infos, instruction, file_format=self._file_format)
      return self.read_files(
          file_instructions,
          read_config=read_config,
          shuffle_files=shuffle_files,
          disable_shuffling=disable_shuffling,
          decode_fn=decode_fn,
      )

    return tf.nest.map_structure(_read_instruction_to_ds, instructions)

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
        relative path, not absolute.
        skip/take indicates which example read in the shard: `ds.skip().take()`
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

    # Prepend path to filename
    file_instructions = [
        f.replace(filename=os.path.join(self._path, f.filename))
        for f in file_instructions
    ]

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
          _decode_with_id, decode_fn=parse_and_decode)

    ds = ds.map(
        parse_and_decode,
        num_parallel_calls=read_config.num_parallel_calls_for_decode,
    )
    return ds


def _str_to_relative_instruction(spec: str) -> 'AbstractSplit':
  """Returns ReadInstruction for given string."""
  # <split_name>[<split_selector>] (e.g. `train[54%:]`)
  res = _SUB_SPEC_RE.match(spec)
  err_msg = (f'Unrecognized split format: {spec!r}. See format at '
             'https://www.tensorflow.org/datasets/splits')
  if not res:
    raise ValueError(err_msg)
  split_name = res.group('split_name')
  split_selector = res.group('split_selector')

  if split_name == 'all':
    if split_selector:
      # TODO(tfds): `all[:75%]` could be supported by creating a
      # `_SliceSplit(split, from_=, to=, unit=)`.
      raise NotImplementedError(
          f'{split_name!r} does not support slice. Please open a github issue '
          'if you need this feature.')
    return _SplitAll()

  if split_selector is None:  # split='train'
    from_ = None
    to = None
    unit = 'abs'
  else:  # split='train[x:y]' or split='train[x]'
    slices = [_SLICE_RE.match(x) for x in split_selector.split(':')]
    # Make sure all slices are valid, and at least one is not empty
    if not all(slices) or not any(x.group(0) for x in slices):
      raise ValueError(err_msg)
    if len(slices) == 1:
      from_match, = slices
      from_ = from_match['val']
      to = int(from_) + 1
      unit = from_match['unit'] or 'abs'
      if unit != 'shard':
        raise ValueError('Absolute or percent only support slice syntax.')
    elif len(slices) == 2:
      from_match, to_match = slices
      from_ = from_match['val']
      to = to_match['val']
      unit = from_match['unit'] or to_match['unit'] or 'abs'
    else:
      raise ValueError(err_msg)

  if from_ is not None:
    from_ = int(from_)
  if to is not None:
    to = int(to)

  return ReadInstruction(
      split_name=split_name,
      rounding='closest',
      from_=from_,
      to=to,
      unit=unit,
  )


def _pct_to_abs_pct1(boundary, num_examples):
  # Using math.trunc here, since -99.5% should give -99%, not -100%.
  if num_examples < 100:
    msg = ('Using "pct1_dropremainder" rounding on a split with less than 100 '
           'elements is forbidden: it always results in an empty dataset.')
    raise ValueError(msg)
  return boundary * math.trunc(num_examples / 100.)


def _pct_to_abs_closest(boundary, num_examples):
  return int(round(boundary * num_examples / 100.))


def _rel_to_abs_instr(
    rel_instr: 'ReadInstruction',
    split_infos: Dict[str, SplitInfo],
):
  """Returns _AbsoluteInstruction instance for given RelativeInstruction.

  Args:
    rel_instr: ReadInstruction instance.
    split_infos: dict {split_name: split_infos}.
  """
  pct_to_abs = (
      _pct_to_abs_closest
      if rel_instr.rounding == 'closest' else _pct_to_abs_pct1)
  split = rel_instr.split_name
  if split not in split_infos:
    raise ValueError(
        f'Unknown split {split!r}. Should be one of {list(split_infos)}.')
  num_examples = split_infos[split].num_examples
  from_ = rel_instr.from_
  to = rel_instr.to
  if rel_instr.unit == '%':
    from_ = 0 if from_ is None else pct_to_abs(from_, num_examples)
    to = num_examples if to is None else pct_to_abs(to, num_examples)
  elif rel_instr.unit == 'shard':
    shard_lengths = split_infos[split].shard_lengths
    from_ = 0 if from_ is None else sum(shard_lengths[:from_])
    if to is not None and to <= 0:
      to = len(shard_lengths) + to
    to = num_examples if to is None else sum(shard_lengths[:to])
  elif rel_instr.unit == 'abs':
    from_ = 0 if from_ is None else from_
    to = num_examples if to is None else to
  else:
    raise ValueError(f'Invalid split unit: {rel_instr.unit}')
  if abs(from_) > num_examples or abs(to) > num_examples:
    msg = 'Requested slice [%s:%s] incompatible with %s examples.' % (
        from_ or '', to or '', num_examples)
    raise ValueError(msg)
  if from_ < 0:
    from_ = num_examples + from_
  elif from_ == 0:
    from_ = None
  if to < 0:
    to = num_examples + to
  elif to == num_examples:
    to = None
  return _AbsoluteInstruction(split, from_, to)


class AbstractSplit(abc.ABC):
  """Abstract base class of splits.

  Abstract splits are combined together, then passed to
  `tfds.load(..., split=)` or `builder.as_dataset(split=...)`.

  See the guide: https://www.tensorflow.org/datasets/splits

  """

  @classmethod
  def from_spec(cls, spec: SplitArg) -> 'AbstractSplit':
    """Creates a ReadInstruction instance out of a string spec.

    Args:
      spec (str): split(s) + optional slice(s) to read. A slice can be
        specified, using absolute numbers (int) or percentages (int). E.g.
              `test`: test split.
              `test + validation`: test split + validation split.
              `test[10:]`: test split, minus its first 10 records.
              `test[:10%]`: first 10% records of test split.
              `test[:-5%]+train[40%:60%]`: first 95% of test + middle 20% of
                train.

    Returns:
      The split instance.
    """
    if isinstance(spec, AbstractSplit):
      return spec

    spec = str(spec)  # Need to convert to str in case of `Split` instance.

    subs = _ADDITION_SEP_RE.split(spec)
    if not subs:
      raise ValueError(f'No instructions could be built out of {spec!r}')
    with utils.try_reraise(f'Error parsing split {spec!r}. See format at: '
                           'https://www.tensorflow.org/datasets/splits\n'):
      instructions = [_str_to_relative_instruction(s) for s in subs]
    # Merge all splits together (_SplitAll)
    return functools.reduce(operator.add, instructions)

  @abc.abstractmethod
  def to_absolute(self, split_infos) -> List['_AbsoluteInstruction']:
    """Translate instruction into a list of absolute instructions.

    Those absolute instructions are then to be added together.

    Args:
      split_infos: `tfds.core.SplitDict` dict associating split names to split
        info.

    Returns:
      list of _AbsoluteInstruction instances (corresponds to the + in spec).
    """
    raise NotImplementedError

  def __add__(self, other: Union[str, 'AbstractSplit']) -> 'AbstractSplit':
    """Sum of 2 splits."""
    if not isinstance(other, (str, AbstractSplit)):
      raise TypeError(f'Adding split {self!r} with non-split value: {other!r}')
    if isinstance(other, str):  # Normalize strings
      other = AbstractSplit.from_spec(other)
    return _SplitAdd(self, other)


@dataclasses.dataclass(frozen=True)
class _AbsoluteInstruction:
  """A machine friendly slice: defined absolute positive boundaries."""
  splitname: str
  from_: int  # uint (starting index).
  to: int  # uint (ending index).

  def to_absolute(self, split_infos) -> List['_AbsoluteInstruction']:
    del split_infos  # unused
    return [self]


@dataclasses.dataclass(frozen=True)
class _SplitAdd(AbstractSplit):
  """Sum of 2 splits.

  `'train+test'` is equivalent to
  `_SplitAdd(ReadInstruction('train'), ReadInstruction('test'))`

  """
  left: AbstractSplit
  right: AbstractSplit

  def __repr__(self):
    return f'{self.left!r}+{self.right!r}'

  def to_absolute(self, split_infos) -> List[_AbsoluteInstruction]:
    # Merge instructions from left and right
    return (self.left.to_absolute(split_infos) +
            self.right.to_absolute(split_infos))


class _SplitAll(AbstractSplit):
  """Union of all splits of the dataset."""

  def to_absolute(self, split_infos) -> List[_AbsoluteInstruction]:
    # Create the union of all splits
    split_names = split_infos.keys()
    split = AbstractSplit.from_spec('+'.join(split_names))
    return split.to_absolute(split_infos)


@dataclasses.dataclass(frozen=True)
class ReadInstruction(AbstractSplit):
  """Reading instruction for a dataset.

  See the guide: https://www.tensorflow.org/datasets/splits

  Attributes:
    split_name: name of the split to read. Eg: 'train'.
    from_: Starting index, or None if no lower boundary.
    to: Ending index, or None if no upper boundary.
    unit: optional, one of:
      '%': to set the slicing unit as percents of the split size.
      'abs': to set the slicing unit as absolute numbers.
      'shard': to set the slicing unit as shard.
    rounding: The rounding behaviour to use when percent slicing is used.
      Ignored when slicing with absolute indices.
      Possible values:
       - 'closest' (default): The specified percentages are rounded to the
         closest value. Use this if you want specified percents to be as much
         exact as possible.
       - 'pct1_dropremainder': the specified percentages are treated as
         multiple of 1%. Use this option if you want consistency. Eg: len(5%) ==
           5 * len(1%). Using this option, one might not be able to use the full
           set of examples, if the number of those is not a multiple of 100.
  """
  split_name: str
  # TODO(py3.10): Add `_ = dataclasses.KW_ONLY`
  from_: Optional[int] = None
  to: Optional[int] = None
  unit: str = 'abs'
  rounding: str = 'closest'

  def __post_init__(self):
    # Perform validation
    allowed_units = ['%', 'abs', 'shard']
    allowed_rounding = ['closest', 'pct1_dropremainder']
    if self.unit not in allowed_units:
      raise ValueError(
          f'Unit should be one of {allowed_units}. Got {self.unit!r}')
    if self.rounding not in allowed_rounding:
      raise ValueError(f'Rounding should be one of {allowed_rounding}. '
                       f'Got: {self.rounding!r}')
    if self.unit == '%':
      if abs(self.from_ or 0) > 100 or abs(self.to or 0) > 100:
        raise ValueError('When unit=%, percent slice boundaries should be '
                         f'in [-100, 100]. Got: {self}')

  def __repr__(self) -> str:
    unit = '' if self.unit == 'abs' else self.unit
    from_ = '' if self.from_ is None else f'{self.from_}{unit}'
    to = '' if self.to is None else f'{self.to}{unit}'
    if self.from_ is None and self.to is None:
      slice_str = ''  # Full split selected
    else:
      slice_str = f'[{from_}:{to}]'
    rounding = f', rounding={self.rounding!r}' if self.unit == '%' else ''
    return f'ReadInstruction(\'{self.split_name}{slice_str}\'{rounding})'

  def to_absolute(self, split_infos) -> List[_AbsoluteInstruction]:
    return [_rel_to_abs_instr(self, split_infos)]
