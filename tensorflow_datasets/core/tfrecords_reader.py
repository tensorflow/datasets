# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import functools
import itertools
import math
import os
import re

import attr

import numpy as np
import tensorflow as tf
from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import utils

_BUFFER_SIZE = 8<<20  # 8 MiB per file.

_SUB_SPEC_RE = re.compile(r'''
^
 (?P<split>\w+)
 (\[
  ((?P<from>-?\d+)
   (?P<from_pct>%)?)?
  :
  ((?P<to>-?\d+)
   (?P<to_pct>%)?)?
 \])?
$
''', re.X)

_ADDITION_SEP_RE = re.compile(r'\s*\+\s*')


def _with_options(dataset):
  """Applies optimization options to given dataset."""
  options = tf.data.Options()
  options.experimental_threading.max_intra_op_parallelism = 1
  options.experimental_threading.private_threadpool_size = 16
  options.experimental_optimization.apply_default_optimizations = True
  options.experimental_optimization.map_fusion = True
  options.experimental_optimization.map_parallelization = True
  return dataset.with_options(options)


def _get_dataset_from_filename(filename_skip_take, do_skip, do_take):
  """Returns a tf.data.Dataset instance from given (filename, skip, take)."""
  filename, skip, take = (filename_skip_take['filename'],
                          filename_skip_take['skip'],
                          filename_skip_take['take'],)
  dataset = tf.data.TFRecordDataset(
      filename,
      buffer_size=_BUFFER_SIZE,
      num_parallel_reads=1,
      )
  if do_skip:
    dataset = dataset.skip(skip)
  if do_take:
    dataset = dataset.take(take)
  dataset = _with_options(dataset)
  return dataset


def _get_dataset_files(name, path, instruction, name2shard_lengths):
  """Returns a list of files (+skip/take) corresponding to given instruction.

  This is the core of the reading logic, to translate from absolute instructions
  (split + left/right boundaries) to files + skip/take.

  Args:
    name: Name of the dataset.
    path: path to tfrecords.
    instruction: _AbsoluteInstruction instance.
    name2shard_lengths: dict associating split names to shard lengths.

  Returns:
    list of dict(filename, skip, take).
  """
  shard_lengths = name2shard_lengths[instruction.splitname]
  if not shard_lengths:
    msg = ('`DatasetInfo.SplitInfo.num_shards` is empty. S3 tfrecords_reader '
           'cannot be used. Make sure the data you are trying to read was '
           'generated using tfrecords_writer module (S3).')
    raise AssertionError(msg)
  filenames = naming.filepaths_for_dataset_split(
      dataset_name=name, split=instruction.splitname,
      num_shards=len(shard_lengths),
      data_dir=path,
      filetype_suffix='tfrecord')
  from_ = 0 if instruction.from_ is None else instruction.from_
  to = sum(shard_lengths) if instruction.to is None else instruction.to
  index_start = 0  # Beginning (included) of moving window.
  index_end = 0  # End (excluded) of moving window.
  files = []
  for filename, length in zip(filenames, shard_lengths):
    index_end += length
    if from_ < index_end and to > index_start:  # There is something to take.
      skip = from_ - index_start if from_ > index_start else 0
      take = to - index_start - skip if to < index_end else -1
      files.append(dict(filename=filename, skip=skip, take=take))
    index_start += length
  return files


def _read_single_instruction(
    instruction,
    parse_fn, name, path, name2len, name2shard_lengths, shuffle_files):
  """Returns tf.data.Dataset for given instruction.

  Args:
    instruction (ReadInstruction or str): if str, a ReadInstruction will be
      constructed using `ReadInstruction.from_spec(str)`.
    parse_fn (callable): function used to parse each record.
    name (str): name of the dataset.
    path (str): path to directory where to read tfrecords from.
    name2len: dict associating split names to number of examples.
    name2shard_lengths: dict associating split names to shard lengths.
    shuffle_files (bool): Defaults to False. True to shuffle input files.
  """
  if not isinstance(instruction, ReadInstruction):
    instruction = ReadInstruction.from_spec(instruction)
  absolute_instructions = instruction.to_absolute(name2len)
  files = list(itertools.chain.from_iterable([
      _get_dataset_files(name, path, abs_instr, name2shard_lengths)
      for abs_instr in absolute_instructions]))
  if not files:
    msg = 'Instruction "%s" corresponds to no data!' % instruction
    raise AssertionError(msg)

  do_skip = any(f['skip'] > 0 for f in files)
  do_take = any(f['take'] > -1 for f in files)

  # Transpose the list[dict] into dict[list]
  tensor_inputs = {
      # skip/take need to be converted to int64 explicitly
      k: list(vals) if k == 'filename' else np.array(vals, dtype=np.int64)
      for k, vals in utils.zip_dict(*files)
  }

  # Both parallel_reads and block_length have empirically been tested to give
  # good results on imagenet.
  # This values might be changes in the future, with more performance test runs.
  parallel_reads = 16
  block_length = 16

  instruction_ds = tf.data.Dataset.from_tensor_slices(tensor_inputs)

  # If shuffle is True, we shuffle the instructions/shards
  if shuffle_files:
    instruction_ds = instruction_ds.shuffle(len(tensor_inputs))

  dataset = instruction_ds.interleave(
      functools.partial(_get_dataset_from_filename,
                        do_skip=do_skip, do_take=do_take),
      cycle_length=parallel_reads,
      block_length=block_length,
      num_parallel_calls=tf.data.experimental.AUTOTUNE,
      )

  # TODO(pierrot): `parse_example` uses
  # `tf.io.parse_single_example`. It might be faster to use `parse_example`,
  # after batching.
  # https://www.tensorflow.org/api_docs/python/tf/io/parse_example
  return dataset.map(parse_fn)


class Reader(object):
  """Build a tf.data.Dataset object out of Instruction instance(s).

  This class should not typically be exposed to the TFDS user.
  """

  def __init__(self, path, example_specs):
    """Initializes Reader.

    Args:
      path (str): path where tfrecords are stored.
      example_specs: spec to build ExampleParser.
    """
    self._path = path
    self._parser = example_parser.ExampleParser(example_specs)

  def read(self, name, instructions, split_infos, shuffle_files=False):
    """Returns tf.data.Dataset instance(s).

    Args:
      name (str): name of the dataset.
      instructions (ReadInstruction, List[], Dict[]): instruction(s) to read.
        Instructions can be string and will then be passed to the Instruction
        constructor as it.
      split_infos (list of SplitInfo proto): the available splits for dataset.
      shuffle_files (bool): defaults to False. If True, input files are shuffled
        before being read.

    Returns:
       a single tf.data.Dataset instance if instruction is a single
       ReadInstruction instance. Otherwise a dict/list of tf.data.Dataset
       corresponding to given instructions param shape.
    """
    name2shard_lengths = {info.name: info.shard_lengths for info in split_infos}
    name2len = {name: sum(lengths)
                for name, lengths in name2shard_lengths.items()}
    read_instruction = functools.partial(
        _read_single_instruction,
        parse_fn=self._parser.parse_example,
        name=name, path=self._path,
        name2len=name2len, name2shard_lengths=name2shard_lengths,
        shuffle_files=shuffle_files)
    datasets = utils.map_nested(read_instruction, instructions, map_tuple=True)
    return datasets


@attr.s(frozen=True)
class _AbsoluteInstruction(object):
  """A machine friendly slice: defined absolute positive boundaries."""
  splitname = attr.ib()  # type: Text
  from_ = attr.ib()  # uint (starting index).
  to = attr.ib()  # uint (ending index).


@attr.s(frozen=True)
class _RelativeInstruction(object):
  """Represents a single parsed slicing instruction, can use % and negatives."""
  splitname = attr.ib()  # type: Text
  from_ = attr.ib()  # int (starting index) or None if no lower boundary.
  to = attr.ib()  # int (ending index) or None if no upper boundary.
  unit = attr.ib(validator=attr.validators.in_(['%', 'abs']))  # str
  rounding = attr.ib(validator=attr.validators.in_([
      'closest', 'pct1_dropremainder']))  # str

  @from_.validator
  @to.validator
  def check_boundary_pct(self, unused_attribute, value):
    if self.unit == '%' and value is not None and abs(value) > 100:
      raise AssertionError('Percent slice boundaries must be > -100 and < 100.')


def _str_to_relative_instruction(spec):
  """Returns ReadInstruction for given string."""
  res = _SUB_SPEC_RE.match(spec)
  if not res:
    raise AssertionError('Unrecognized instruction format: %s' % spec)
  unit = '%' if res.group('from_pct') or res.group('to_pct') else 'abs'
  return ReadInstruction(
      split_name=res.group('split'),
      rounding='closest',
      from_=int(res.group('from')) if res.group('from') else None,
      to=int(res.group('to')) if res.group('to') else None,
      unit=unit,
      )


def _pct_to_abs_pct1(boundary, num_examples):
  # Using math.trunc here, since -99.5% should give -99%, not -100%.
  if num_examples < 100:
    msg = ('Using "pct1_dropremainder" rounding on a split with less than 100 '
           'elements is forbidden: it always results in an empty dataset.')
    raise AssertionError(msg)
  return boundary * math.trunc(num_examples / 100.)


def _pct_to_abs_closest(boundary, num_examples):
  return int(round(boundary * num_examples / 100.))


def _rel_to_abs_instr(rel_instr, name2len):
  """Returns _AbsoluteInstruction instance for given RelativeInstruction.

  Args:
    rel_instr: RelativeInstruction instance.
    name2len: dict {split_name: num_examples}.
  """
  pct_to_abs = (_pct_to_abs_closest if rel_instr.rounding == 'closest'
                else _pct_to_abs_pct1)
  split = rel_instr.splitname
  if split not in name2len:
    raise AssertionError('Requested split "%s" does not exist.' % split)
  num_examples = name2len[split]
  from_ = rel_instr.from_
  to = rel_instr.to
  if rel_instr.unit == '%':
    from_ = 0 if from_ is None else pct_to_abs(from_, num_examples)
    to = num_examples if to is None else pct_to_abs(to, num_examples)
  else:
    from_ = 0 if from_ is None else from_
    to = num_examples if to is None else to
  if abs(from_) > num_examples or abs(to) > num_examples:
    msg = 'Requested slice [%s:%s] incompatible with %s examples.' % (
        from_ or '', to or '', num_examples)
    raise AssertionError(msg)
  if from_ < 0:
    from_ = num_examples + from_
  elif from_ == 0:
    from_ = None
  if to < 0:
    to = num_examples + to
  elif to == num_examples:
    to = None
  return _AbsoluteInstruction(split, from_, to)


class ReadInstruction(object):
  """Reading instruction for a dataset.

  Examples of usage:

  # The following lines are equivalent:
  ds = tfds.load('mnist', split='test[:33%]')
  ds = tfds.load('mnist', split=ReadInstruction.from_spec('test[:33%]'))
  ds = tfds.load('mnist', split=ReadInstruction('test', to=33, unit='%'))
  ds = tfds.load('mnist', split=ReadInstruction(
      'test', from_=0, to=33, unit='%'))

  # The following lines are equivalent:
  ds = tfds.load('mnist', split='test[:33%]+train[1:-1]')
  ds = tfds.load('mnist', split=ReadInstruction.from_spec(
      'test[:33%]+train[1:-1]'))
  ds = tfds.load('mnist', split=(
      ReadInstruction.('test', to=33, unit='%') +
      ReadInstruction.('train', from_=1, to=-1, unit='abs')))

  # 10-fold validation:
  tests = tfds.load(
      'mnist',
      [ReadInstruction('train', from_=k, to=k+10, unit='%')
       for k in range(0, 100, 10)])
  trains = tfds.load(
      'mnist',
      [RI('train', to=k, unit='%') + RI('train', from_=k+10, unit='%')
       for k in range(0, 100, 10)])
  """

  def _init(self, relative_instructions):
    # Private initializer.
    self._relative_instructions = relative_instructions

  @classmethod
  def _read_instruction_from_relative_instructions(cls, relative_instructions):
    """Returns ReadInstruction obj initialized with relative_instructions."""
    # Use __new__ to bypass __init__ used by public API and not conveniant here.
    result = cls.__new__(cls)
    result._init(relative_instructions)  # pylint: disable=protected-access
    return result

  @api_utils.disallow_positional_args(allowed=['split_name'])
  def __init__(self, split_name, rounding='closest', from_=None, to=None,
               unit=None):
    """Initialize ReadInstruction.

    Args:
      split_name (str): name of the split to read. Eg: 'train'.
      rounding (str): The rounding behaviour to use when percent slicing is
        used. Ignored when slicing with absolute indices.
        Possible values:
         - 'closest' (default): The specified percentages are rounded to the
           closest value. Use this if you want specified percents to be as
           much exact as possible.
         - 'pct1_dropremainder': the specified percentages are treated as
           multiple of 1%. Use this option if you want consistency. Eg:
             len(5%) == 5 * len(1%).
           Using this option, one might not be able to use the full set of
           examples, if the number of those is not a multiple of 100.
      from_ (int):
      to (int): alternative way of specifying slicing boundaries. If any of
        {from_, to, unit} argument is used, slicing cannot be specified as
        string.
      unit (str): optional, one of:
        '%': to set the slicing unit as percents of the split size.
        'abs': to set the slicing unit as absolute numbers.
    """
    # This constructor is not always called. See factory method
    # `_read_instruction_from_relative_instructions`. Common init instructions
    # MUST be placed in the _init method.
    self._init(
        [_RelativeInstruction(split_name, from_, to, unit, rounding)])

  @classmethod
  def from_spec(cls, spec):
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
      ReadInstruction instance.
    """
    spec = str(spec)  # Need to convert to str in case of NamedSplit instance.
    subs = _ADDITION_SEP_RE.split(spec)
    if not subs:
      raise AssertionError('No instructions could be built out of %s' % spec)
    instruction = _str_to_relative_instruction(subs[0])
    return sum([_str_to_relative_instruction(sub) for sub in subs[1:]],
               instruction)

  def __add__(self, other):
    """Returns a new ReadInstruction obj, result of appending other to self."""
    if not isinstance(other, ReadInstruction):
      msg = 'ReadInstruction can only be added to another ReadInstruction obj.'
      raise AssertionError(msg)
    other_ris = other._relative_instructions  # pylint: disable=protected-access
    if self._relative_instructions[0].rounding != other_ris[0].rounding:
      raise AssertionError('It is forbidden to sum ReadInstruction instances '
                           'with different rounding values.')
    return self._read_instruction_from_relative_instructions(
        self._relative_instructions + other_ris)

  def __str__(self):
    return 'ReadInstruction(%s)' % self._relative_instructions

  def to_absolute(self, name2len):
    """Translate instruction into a list of absolute instructions.

    Those absolute instructions are then to be added together.

    Args:
      name2len: dict associating split names to number of examples.

    Returns:
      list of _AbsoluteInstruction instances (corresponds to the + in spec).
    """
    return [_rel_to_abs_instr(rel_instr, name2len)
            for rel_instr in self._relative_instructions]
