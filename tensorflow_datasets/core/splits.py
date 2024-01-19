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

"""Splits related API."""

from __future__ import annotations

import abc
import dataclasses
import functools
import itertools
import math
import operator
import os
import re
import typing
from typing import Any, Dict, Iterable, List, Optional, Union

from absl import logging
from etils import epath
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import proto as proto_lib
from tensorflow_datasets.core import units
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import shard_utils

from tensorflow_metadata.proto.v0 import statistics_pb2

# Accepted split values (in `as_dataset(split=...)`)
SplitArg = Union[str, 'AbstractSplit']

# <split_name>[<split_selector>] (e.g. `train[54%:]`)
_SUB_SPEC_RE = re.compile(
    r"""^
    (?P<split_name>[\w-]+)
    (\[
      (?P<split_selector>[\d\w%:.-]+)
    \])?
    $""",
    re.X,  # Ignore whitespace
)
# <val><unit> (e.g. `-54%`)
_SLICE_RE = re.compile(
    r"""^
    (
        (?P<val>-?[\d_.]+)
        (?P<unit>(?:%|shard))?
    )?
    $""",
    re.X,  # Ignore whitespace
)

_ADDITION_SEP_RE = re.compile(r'\s*\+\s*')


@dataclasses.dataclass(frozen=True)
class _AbsoluteInstruction:
  """A machine friendly slice: defined absolute positive boundaries."""

  splitname: str
  from_: int  # uint (starting index).
  to: int  # uint (ending index).

  def to_absolute(self, split_infos) -> List['_AbsoluteInstruction']:
    del split_infos  # unused
    return [self]


@dataclasses.dataclass(eq=False, frozen=True)
class SplitInfo:
  """Wraps `proto.SplitInfo` with an additional property.

  Attributes:
    name: Name of the split (e.g. `train`, `test`,...)
    shard_lengths: List of length <number of files> containing the number of
      examples stored in each file.
    filename_template: The template used to create sharded filenames.
    num_examples: Total number of examples (`sum(shard_lengths)`)
    num_shards: Number of files (`len(shard_lengths)`)
    num_bytes: Size of the files (in bytes)
    statistics: Additional statistics of the split.
  """

  name: str
  shard_lengths: List[int]
  num_bytes: int
  filename_template: Optional[naming.ShardedFileTemplate] = None
  statistics: statistics_pb2.DatasetFeatureStatistics = dataclasses.field(
      default_factory=statistics_pb2.DatasetFeatureStatistics,
  )

  def __post_init__(self):
    if (
        self.filename_template
        and self.filename_template.split
        and self.name != self.filename_template.split
    ):
      raise ValueError(
          f'Split name {self.name} must be equal to split name '
          f'in template {self.filename_template.split}'
      )
    if self.filename_template and not self.filename_template.split:
      super().__setattr__(
          'filename_template', self.filename_template.replace(split=self.name)
      )
    # Normalize bytes
    super().__setattr__('num_bytes', units.Size(self.num_bytes))

  @classmethod
  def from_proto(
      cls,
      proto: proto_lib.SplitInfo,
      filename_template: naming.ShardedFileTemplate,
  ) -> 'SplitInfo':
    """Returns a SplitInfo class instance from a SplitInfo proto."""
    return cls(
        name=proto.name,
        shard_lengths=list(proto.shard_lengths),
        num_bytes=proto.num_bytes,
        filename_template=filename_template.replace(
            split=proto.name, template=proto.filepath_template
        ),
        statistics=proto.statistics,
    )

  def to_proto(self) -> proto_lib.SplitInfo:
    if self.filename_template:
      filepath_template = self.filename_template.template
    else:
      filepath_template = naming.DEFAULT_FILENAME_TEMPLATE
    return proto_lib.SplitInfo(
        name=self.name,
        shard_lengths=self.shard_lengths,
        num_bytes=self.num_bytes,
        statistics=self.statistics if self.statistics.ByteSize() else None,
        filepath_template=filepath_template,
    )

  @property
  def num_examples(self) -> int:
    return sum(self.shard_lengths)

  @property
  def num_shards(self) -> int:
    return len(self.shard_lengths)

  def __repr__(self) -> str:
    num_examples = self.num_examples or 'unknown'
    return (
        f'<SplitInfo num_examples={num_examples}, num_shards={self.num_shards}>'
    )

  @property
  def file_instructions(self) -> List[shard_utils.FileInstruction]:
    """Returns the list of dict(filename, take, skip).

    This allows for creating your own `tf.data.Dataset` using the low-level
    TFDS values.

    Example:

    ```
    file_instructions = info.splits['train[75%:]'].file_instructions
    instruction_ds = tf.data.Dataset.from_generator(
        lambda: file_instructions,
        output_types={
            'filename': tf.string,
            'take': tf.int64,
            'skip': tf.int64,
        },
    )
    ds = instruction_ds.interleave(
        lambda f: tf.data.TFRecordDataset(
            f['filename']).skip(f['skip']).take(f['take'])
    )
    ```

    When `skip=0` and `take=-1`, the full shard will be read, so the `ds.skip`
    and `ds.take` could be skipped.

    Returns:
      A `dict(filename, take, skip)`
    """
    return _make_file_instructions(
        split_infos=[self],
        instruction=str(self.name),
    )

  @property
  def filenames(self) -> List[str]:
    """Returns the list of filenames."""
    if not self.filename_template:
      raise ValueError('No filename templates available.')
    return sorted(
        self.filename_template.sharded_filenames(len(self.shard_lengths))
    )

  @property
  def filepaths(self) -> List[epath.Path]:
    """All the paths for all the files that are part of this split."""
    if not self.filename_template:
      raise ValueError('No filename templates available.')
    return sorted(
        self.filename_template.sharded_filepaths(len(self.shard_lengths))
    )

  def replace(self, **kwargs: Any) -> 'SplitInfo':
    """Returns a copy of the `SplitInfo` with updated attributes."""
    return dataclasses.replace(self, **kwargs)


@dataclasses.dataclass(eq=False, frozen=True)
class MultiSplitInfo(SplitInfo):
  """SplitInfo for when a split is spread out over multiple folders.

  This should only be used to read data and not when producing data.
  """

  split_infos: List[SplitInfo] = dataclasses.field(default_factory=list)

  def __init__(self, name: str, split_infos: List[SplitInfo]):
    if not split_infos:
      raise ValueError('Need to pass a non-empty list of SplitInfos')
    object.__setattr__(self, 'split_infos', split_infos)

    # Compute attributes of parent class SplitInfo
    shard_lengths = []
    for split_info in split_infos:
      shard_lengths.extend(split_info.shard_lengths)
    # Note that num_bytes=0 means that the size isn't known. However, we do
    # compute the sum because it will provide at least some information about
    # the size, even though it may be incomplete.
    num_bytes = sum(si.num_bytes for si in split_infos)
    super().__init__(
        name=name,
        shard_lengths=shard_lengths,
        num_bytes=num_bytes,
        filename_template=None,
    )

  def to_proto(self) -> proto_lib.SplitInfo:
    # The SplitInfo proto only supports a single split.
    raise RuntimeError('to_proto is not supported on MultiSplitInfo')

  def __repr__(self) -> str:
    return (
        f'{self.__class__.__name__}('
        f'name={self.name!r}, '
        f'split_infos={self.split_infos!r})'
    )

  @property
  def file_instructions(self) -> List[shard_utils.FileInstruction]:
    result = []
    for split_info in self.split_infos:
      result.extend(split_info.file_instructions)
    return result

  @property
  def filenames(self) -> List[str]:
    """Returns the list of filenames."""
    result = []
    for split_info in self.split_infos:
      result.extend(split_info.filenames)
    return result

  @property
  def filepaths(self) -> List[epath.Path]:
    """All the paths for all the files that are part of this split."""
    result = []
    for split_info in self.split_infos:
      result.extend(split_info.filepaths)
    return result

  def replace(self, **kwargs: Any) -> 'MultiSplitInfo':
    raise RuntimeError('replace is not supported on MultiSplitInfo')


@dataclasses.dataclass(eq=False, frozen=True)
class SubSplitInfo:
  """Wrapper around a sub split info.

  This class expose info on the subsplit:

  ```
  ds, info = tfds.load(..., split='train[75%:]', with_info=True)
  info.splits['train[75%:]'].num_examples
  ```
  """

  name: str
  file_instructions: List[shard_utils.FileInstruction]

  @property
  def shard_lengths(self) -> List[int]:
    return [f.take for f in self.file_instructions]

  @property
  def num_examples(self) -> int:
    """Returns the number of example in the subsplit."""
    return sum(self.shard_lengths)

  @property
  def num_bytes(self) -> int:
    return 0  # Unknown

  @property
  def num_shards(self) -> int:
    return len(self.file_instructions)

  @property
  def filenames(self) -> List[str]:
    """Returns the list of filenames."""
    return sorted(os.path.basename(f.filename) for f in self.file_instructions)

  @property
  def filepaths(self) -> List[epath.Path]:
    """Returns the list of filepaths."""
    return sorted(epath.Path(f.filename) for f in self.file_instructions)

  def to_proto(self) -> proto_lib.SplitInfo:
    return proto_lib.SplitInfo(
        name=self.name,
        shard_lengths=self.shard_lengths,
        num_bytes=self.num_bytes,
        statistics=None,
    )


# TODO(epot): `: tfds.Split` type should be `Union[str, Split]`
class Split(str):
  # pylint: disable=line-too-long
  """`Enum` for dataset splits.

  Datasets are typically split into different subsets to be used at various
  stages of training and evaluation.

  * `TRAIN`: the training data.
  * `VALIDATION`: the validation data. If present, this is typically used as
    evaluation data while iterating on a model (e.g. changing hyperparameters,
    model architecture, etc.).
  * `TEST`: the testing data. This is the data to report metrics on. Typically
    you do not want to use this during model iteration as you may overfit to it.
  * `ALL`: All splits from the dataset merged together (`'train+test+...'`).

  See the
  [guide on
  splits](https://github.com/tensorflow/datasets/blob/master/docs/splits.md)
  for more information.
  """

  def __repr__(self) -> str:
    return '{}({})'.format(type(self).__name__, super(Split, self).__repr__())  # pytype: disable=wrong-arg-types


Split.TRAIN = Split('train')
Split.TEST = Split('test')
Split.VALIDATION = Split('validation')
Split.ALL = Split('all')

if typing.TYPE_CHECKING:
  # For type checking, `tfds.Split` is an alias for `str` with additional
  # `.TRAIN`, `.TEST`,... attributes. All strings are valid split type.
  Split = Union[Split, str]


class SplitDict(utils.NonMutableDict[str, SplitInfo]):
  """Split info object."""

  def __init__(
      self,
      split_infos: Iterable[SplitInfo],
      *,
      # TODO(b/216470058): remove this parameter
      dataset_name: Optional[str] = None,  # deprecated, please don't use
  ):
    super(SplitDict, self).__init__(
        {split_info.name: split_info for split_info in split_infos},
        error_msg='Split {key} already present',
    )
    if dataset_name:
      logging.warning(
          "DEPRECATED: SplitDict's dataset_name parameter is "
          'deprecated and can be removed.'
      )
    self._dataset_name = dataset_name  # deprecated, please don't use

  def __getitem__(self, key):
    if not self:
      raise KeyError(
          f'Trying to access `splits[{key!r}]` but `splits` is empty. '
          'This likely indicate the dataset has not been generated yet.'
      )
    # 1st case: The key exists: `info.splits['train']`
    elif str(key) in self.keys():
      return super(SplitDict, self).__getitem__(str(key))
    # 2nd case: Uses instructions: `info.splits['train[50%]']`
    else:
      instructions = _make_file_instructions(
          split_infos=list(self.values()),
          instruction=key,
      )
      return SubSplitInfo(name=key, file_instructions=instructions)

  @classmethod
  def from_proto(
      cls,
      repeated_split_infos: Iterable[proto_lib.SplitInfo],
      filename_template: naming.ShardedFileTemplate,
  ) -> 'SplitDict':
    """Returns a new SplitDict initialized from the `repeated_split_infos`."""
    split_infos = [
        SplitInfo.from_proto(
            proto=s, filename_template=filename_template.replace(split=s.name)
        )
        for s in repeated_split_infos
    ]
    return cls(split_infos)

  def to_proto(self):
    """Returns a list of SplitInfo protos that we have."""
    return [s.to_proto() for s in self.values()]

  @property
  def total_num_examples(self):
    """Return the total number of examples."""
    return sum(s.num_examples for s in self.values())

  @classmethod
  def merge_multiple(cls, split_dicts: List['SplitDict']) -> 'SplitDict':
    info_per_split = []
    for split in set(itertools.chain(*split_dicts)):
      infos_of_split = []
      for split_dict in split_dicts:
        if split not in split_dict:
          continue
        split_info = split_dict[split]
        if isinstance(split_info, MultiSplitInfo):
          infos_of_split.extend(split_info.split_infos)
        else:
          infos_of_split.append(split_info)
      info_per_split.append(
          MultiSplitInfo(name=split, split_infos=infos_of_split)
      )

    return cls(split_infos=info_per_split)


def _make_absolute_instructions(
    split_infos: Iterable[SplitInfo],
    instruction: SplitArg,
) -> List[_AbsoluteInstruction]:
  if isinstance(instruction, str):
    instruction = AbstractSplit.from_spec(instruction)

  # Create the absolute instruction (per split)
  split_info_map = {split_info.name: split_info for split_info in split_infos}
  return instruction.to_absolute(split_info_map)


def _file_instructions_for_split(
    instruction: _AbsoluteInstruction,
    split_info: SplitInfo,
) -> List[shard_utils.FileInstruction]:
  """Returns the file instructions from the given instruction applied to the given split info."""
  if not split_info.num_examples:
    raise ValueError(
        "Shard empty. This might means that dataset hasn't been generated "
        'yet and info not restored from GCS, or that legacy dataset is used.'
    )
  to = split_info.num_examples if instruction.to is None else instruction.to
  return shard_utils.get_file_instructions(
      from_=instruction.from_ or 0,
      to=to,
      filenames=[os.fspath(fp) for fp in split_info.filepaths],
      shard_lengths=split_info.shard_lengths,
  )


def _make_file_instructions(
    split_infos: List[SplitInfo],
    instruction: SplitArg,
) -> List[shard_utils.FileInstruction]:
  """Returns file instructions by applying the given instruction on the given splits.

  Args:
    split_infos: Dataset splits information
    instruction: `ReadInstruction` or `str`

  Returns:
    List of FileInstruction instances
  """

  # TODO(epot): Should try to merge the instructions together as well as
  # performing additional validation. For example, should raise an error
  # if there is overlap between splits (`train[:50]+train[:25]`)
  # If there is a single shard, `train[:25]+train[50:75]` could be optimized
  # into a single `ds.take(25).skip(50-25).take(75-50)`

  absolute_instructions = _make_absolute_instructions(
      split_infos=split_infos, instruction=instruction
  )
  instructions = []
  info_per_split = {split_info.name: split_info for split_info in split_infos}
  for abs_instr in absolute_instructions:
    split_info = info_per_split[str(abs_instr.splitname)]
    instructions.extend(
        _file_instructions_for_split(
            instruction=abs_instr, split_info=split_info
        )
    )
  return instructions


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
        `test`: test split. `test + validation`: test split + validation split.
        `test[10:]`: test split, minus its first 10 records. `test[:10%]`: first
        10% records of test split. `test[:-5%]+train[40%:60%]`: first 95% of
        test + middle 20% of train.

    Returns:
      The split instance.
    """
    if isinstance(spec, AbstractSplit):
      return spec

    spec = str(spec)  # Need to convert to str in case of `Split` instance.

    subs = _ADDITION_SEP_RE.split(spec)
    if not subs:
      raise ValueError(f'No instructions could be built out of {spec!r}')
    with utils.try_reraise(
        f'Error parsing split {spec!r}. See format at: '
        'https://www.tensorflow.org/datasets/splits\n'
    ):
      instructions = [_str_to_relative_instruction(s) for s in subs]
    # Merge all splits together (_SplitAll)
    return functools.reduce(operator.add, instructions)

  @abc.abstractmethod
  def to_absolute(self, split_infos) -> List[_AbsoluteInstruction]:
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
    return self.left.to_absolute(split_infos) + self.right.to_absolute(
        split_infos
    )


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
    from_: Starting position, or None if no lower boundary.
    to: Ending position, or None if no upper boundary.
    unit: optional, one of: '%': to set the slicing unit as percents of the
      split size. 'abs': to set the slicing unit as absolute numbers. 'shard':
      to set the slicing unit as shard.
    rounding: The rounding behaviour to use when percent slicing is used.
      Ignored when slicing with absolute indices. Possible values: - 'closest'
      (default): The specified percentages are rounded to the closest value. Use
      this if you want specified percents to be as much exact as possible. -
      'pct1_dropremainder': the specified percentages are treated as multiple of
      1%. Use this option if you want consistency. Eg: len(5%) == 5 * len(1%).
      Using this option, one might not be able to use the full set of examples,
      if the number of those is not a multiple of 100.
  """

  split_name: str
  # TODO(py3.10): Add `_ = dataclasses.KW_ONLY`
  from_: Optional[int | float] = None
  to: Optional[int | float] = None
  unit: str = 'abs'
  rounding: str = 'closest'

  def __post_init__(self):
    # Perform validation
    allowed_units = ['%', 'abs', 'shard']
    allowed_rounding = ['closest', 'pct1_dropremainder']
    if self.unit not in allowed_units:
      raise ValueError(
          f'Unit should be one of {allowed_units}. Got {self.unit!r}'
      )
    if self.rounding not in allowed_rounding:
      raise ValueError(
          f'Rounding should be one of {allowed_rounding}. '
          f'Got: {self.rounding!r}'
      )
    if self.unit == '%':
      if abs(self.from_ or 0) > 100 or abs(self.to or 0) > 100:
        raise ValueError(
            'When unit=%, percent slice boundaries should be '
            f'in [-100, 100]. Got: {self}'
        )

  def __repr__(self) -> str:
    unit = '' if self.unit == 'abs' else self.unit
    from_ = '' if self.from_ is None else f'{self.from_:g}{unit}'
    to = '' if self.to is None else f'{self.to:g}{unit}'
    if self.from_ is None and self.to is None:
      slice_str = ''  # Full split selected
    else:
      slice_str = f'[{from_}:{to}]'
    rounding = f', rounding={self.rounding!r}' if self.unit == '%' else ''
    return f"ReadInstruction('{self.split_name}{slice_str}'{rounding})"

  def to_absolute(self, split_infos) -> List[_AbsoluteInstruction]:
    return [_rel_to_abs_instr(self, split_infos)]


def _str_to_relative_instruction(spec: str) -> AbstractSplit:
  """Returns ReadInstruction for given string."""
  # <split_name>[<split_selector>] (e.g. `train[54%:]`)
  res = _SUB_SPEC_RE.match(spec)
  err_msg = (
      f'Unrecognized split format: {spec!r}. See format at '
      'https://www.tensorflow.org/datasets/splits'
  )
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
          'if you need this feature.'
      )
    return _SplitAll()

  if split_selector is None:  # split='train'
    from_ = None
    to = None
    unit = 'abs'
  else:  # split='train[x:y]' or split='train[x]'
    slices = [_SLICE_RE.match(x) for x in split_selector.split(':')]
    # Make sure all slices are valid, and at least one is not empty
    if not all(slices) or not any(x.group(0) for x in slices):  # pytype: disable=attribute-error  # re-none
      raise ValueError(err_msg)
    if len(slices) == 1:  # split='train[x]'
      (from_match,) = slices
      from_ = from_match['val']
      to = int(from_) + 1
      unit = from_match['unit'] or 'abs'
      if unit != 'shard':
        raise ValueError('Absolute or percent only support slice syntax.')
    elif len(slices) == 2:  # split='train[x:y]'
      from_match, to_match = slices
      from_ = from_match['val']
      to = to_match['val']
      unit = from_match['unit'] or to_match['unit'] or 'abs'
    else:
      raise ValueError(err_msg)

  if from_ is not None:
    from_ = float(from_) if unit == '%' else int(from_)
  if to is not None:
    to = float(to) if unit == '%' else int(to)

  return ReadInstruction(
      split_name=split_name,
      rounding='closest',
      from_=from_,
      to=to,
      unit=unit,
  )


def _pct_to_abs_pct1(boundary, num_examples: int):
  # Using math.trunc here, since -99.5% should give -99%, not -100%.
  if num_examples < 100:
    msg = (
        'Using "pct1_dropremainder" rounding on a split with less than 100 '
        'elements is forbidden: it always results in an empty dataset.'
    )
    raise ValueError(msg)
  return boundary * math.trunc(num_examples / 100.0)


def _pct_to_abs_closest(boundary, num_examples: int) -> int:
  return int(round(boundary * num_examples / 100.0))


def _rel_to_abs_instr(
    rel_instr: ReadInstruction,
    split_infos: Dict[str, SplitInfo],
) -> _AbsoluteInstruction:
  """Returns _AbsoluteInstruction instance for given RelativeInstruction.

  Args:
    rel_instr: ReadInstruction instance.
    split_infos: dict {split_name: split_infos}.
  """
  pct_to_abs = (
      _pct_to_abs_closest
      if rel_instr.rounding == 'closest'
      else _pct_to_abs_pct1
  )
  split = rel_instr.split_name
  if split not in split_infos:
    raise ValueError(
        f'Unknown split {split!r}. Should be one of {list(split_infos)}.'
    )
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
        from_ or '',
        to or '',
        num_examples,
    )
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
