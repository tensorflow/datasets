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

"""Utilities for file names."""

import dataclasses
import os
import re
import textwrap
from typing import Any, Dict, List, Optional, Tuple, Union

from tensorflow_datasets.core.utils import generic_path
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils

_DEFAULT_NUM_DIGITS_FOR_SHARDS = 5

_first_cap_re = re.compile('(.)([A-Z][a-z0-9]+)')
_all_cap_re = re.compile('([a-z0-9])([A-Z])')

_NAME_CLASS = r'[a-zA-Z][\w]*'
_NAME_CLASS_REG = re.compile(r'^' + _NAME_CLASS + r'$')

# Regex matching 'dataset/config:1.*.*/arg=123'
_NAME_REG = re.compile(r'^'
                       r'(?P<dataset_name>([\w\-]+:)?' + _NAME_CLASS + r')'
                       r'(/(?P<config>[\w\-\.]+))?'
                       r'(:(?P<version>(\d+|\*)(\.(\d+|\*)){2}))?'
                       r'(/(?P<kwargs>(\w+=\w+)(,\w+=[^,]+)*))?'
                       r'$')

Value = Union[str, int, float, bool]


@dataclasses.dataclass(eq=True, order=True, frozen=True)
class DatasetName:
  """Dataset namespace+name."""
  namespace: Optional[str]
  name: str

  def __init__(
      self,
      namespace_name: Optional[str] = None,
      # TODO(py3.8): Positional-only arg /,
      *,
      namespace: Optional[str] = None,
      name: Optional[str] = None,
  ):
    if namespace_name and bool(namespace or name):
      raise ValueError(
          "Name should be defined by `DatasetName('ns:name')` or "
          "`DatasetName(namespace='ns', name='name'). Mixing args and kwargs "
          'is invalid.')
    if namespace_name:
      if ':' in namespace_name:
        namespace, name = namespace_name.split(':')
      else:
        namespace, name = None, namespace_name
    super().__setattr__('namespace', namespace)
    super().__setattr__('name', name)

  def __str__(self) -> str:
    return f'{self.namespace}:{self.name}' if self.namespace else self.name

  def __repr__(self) -> str:
    return f'{type(self).__name__}({str(self)!r})'


def is_valid_dataset_name(name_str: str) -> bool:
  """Returns True is the given name is a valid dataset name."""
  res = _NAME_REG.match(name_str)
  return bool(res)


def is_valid_dataset_and_class_name(name_str: str) -> bool:
  """Returns True is the given name is a valid dataset and class name."""
  res = _NAME_CLASS_REG.match(name_str)
  return bool(res)


def parse_builder_name_kwargs(
    name: str,
    **builder_kwargs: Any,
) -> Tuple[DatasetName, Dict[str, Any]]:
  """Normalize builder kwargs.

  Example:

  ```python
  ds_name, builder_kwargs = parse_builder_name_kwargs(
      'kaggle:ds/cfg:1.2.3', data_dir='...'
  )
  ds_name.namespace == 'kaggle'
  ds_name.name == 'ds'
  builder_kwargs == {'config': 'cfg', 'version': '1.2.3', 'data_dir': '...'}
  ```

  Args:
    name: Name
    **builder_kwargs: Builder kwargs

  Returns:
    ns_name: Dataset namespace, or None
    ds_name: Dataset name
    builder_kwargs: Builder kwargs (version, config, data_dir,...)
  """
  name, parsed_builder_kwargs = _dataset_name_and_kwargs_from_name_str(name)
  builder_kwargs = dict(**parsed_builder_kwargs, **builder_kwargs)
  return DatasetName(name), builder_kwargs


def _dataset_name_and_kwargs_from_name_str(
    name_str: str,) -> Tuple[str, Dict[str, Value]]:
  """Extract kwargs from name str."""
  err_msg = textwrap.dedent(f"""\
      Parsing builder name string {name_str} failed.
      The builder name string must be of the following format:
        dataset_name[/config_name][:version][/kwargs]

        Where:

          * dataset_name and config_name are string following python variable naming.
          * version is of the form x.y.z where {{x,y,z}} can be any digit or *.
          * kwargs is a comma list separated of arguments and values to pass to
            builder.

        Examples:
          my_dataset
          my_dataset:1.2.*
          my_dataset/config1
          my_dataset/config1:1.*.*
          my_dataset/config1/arg1=val1,arg2=val2
          my_dataset/config1:1.2.3/right=True,foo=bar,rate=1.2
      """)

  res = _NAME_REG.match(name_str)
  if not res:
    raise ValueError(err_msg)
  name = res.group('dataset_name')
  # Normalize the name to accept CamelCase
  name = camelcase_to_snakecase(name)
  kwargs = _kwargs_str_to_kwargs(res.group('kwargs'))
  try:
    for attr in ['config', 'version']:
      val = res.group(attr)
      if val is None:
        continue
      if attr in kwargs:
        raise ValueError('Dataset %s: cannot pass %s twice.' % (name, attr))
      kwargs[attr] = val
    return name, kwargs
  except Exception as e:  # pylint: disable=broad-except
    py_utils.reraise(e, prefix=err_msg)  # pytype: disable=bad-return-type


def _kwargs_str_to_kwargs(kwargs_str: str):
  """Converts given `kwargs` as str into kwargs dict."""
  if not kwargs_str:
    return {}
  kwarg_strs = kwargs_str.split(',')
  kwargs = {}
  for kwarg_str in kwarg_strs:
    kwarg_name, kwarg_val = kwarg_str.split('=')
    kwargs[kwarg_name] = _cast_to_pod(kwarg_val)
  return kwargs


def _cast_to_pod(val: str) -> Value:
  """Try cast to bool, int, float, str, in that order."""
  bools = {'True': True, 'False': False}
  if val in bools:
    return bools[val]
  try:
    return int(val)
  except ValueError:
    try:
      return float(val)
    except ValueError:
      return val


def camelcase_to_snakecase(name: str) -> str:
  """Convert camel-case string to snake-case."""
  s1 = _first_cap_re.sub(r'\1_\2', name)
  return _all_cap_re.sub(r'\1_\2', s1).lower()


def snake_to_camelcase(name: str) -> str:
  """Convert snake-case string to camel-case string."""
  return ''.join(n.capitalize() for n in name.split('_'))


def filename_prefix_for_name(name: str) -> str:
  if os.path.basename(name) != name:
    raise ValueError('Should be a dataset name, not a path: %s' % name)
  return camelcase_to_snakecase(name)


def filename_prefix_for_split(name: str, split: str) -> str:
  if os.path.basename(name) != name:
    raise ValueError('Should be a dataset name, not a path: %s' % name)
  return '%s-%s' % (filename_prefix_for_name(name), split)


def shard_suffix_template(*, append_num_shards: bool,
                          num_shards: Optional[int]) -> str:
  """Returns the template for the shard suffix.

  Note that if num_shards is not provided, we use 5 digits for shard numbers.

  Arguments:
    append_num_shards: whether to use xxxxx-of-yyyyy or just xxxxx suffix.
    num_shards: optional number of shards. Required if append_num_shards is
      True.

  Returns:
    the template for the shard suffix in the filename. The template contains two
    parameters: 'shard_index' (required), and 'num_shards' (optional, only
    required when 'append_num_shards' is True).
  """
  if (not num_shards or num_shards < 1) and append_num_shards:
    raise ValueError('num_shards must be >0 when append_num_shards is True')
  if num_shards:
    num_digits = max(len(str(num_shards)), _DEFAULT_NUM_DIGITS_FOR_SHARDS)
  else:
    num_digits = _DEFAULT_NUM_DIGITS_FOR_SHARDS
  assert num_digits < 10
  index_template = '{shard_index:0%d}' % num_digits
  if append_num_shards:
    num_shards_template = '{num_shards:0%d}' % num_digits
    return f'{index_template}-of-{num_shards_template}'
  else:
    return index_template


@dataclasses.dataclass()
class ShardedFileTemplate:
  """Template to produce filenames for sharded datasets.

  Attributes:
    dataset_name: the name of the dataset.
    data_dir: the directory that contains the files for the shards.
    filetype_suffix: the filetype suffix to denote the type of file. For
      example, `tfrecord`.
    split: the split of the dataset.
    append_num_shards: whether to use the xxxxx-of-yyyyy notation or just xxxxx.
    filename_prefix: the part of the filename up until the shard information.
    filepath_prefix: the part of the filename up until the shard information,
      but now also includes the directory of the file if it is given.
  """
  dataset_name: str
  data_dir: type_utils.ReadWritePath
  filetype_suffix: Optional[str]
  split: Optional[str] = None
  append_num_shards: bool = True

  def __post_init__(self):
    self.data_dir = generic_path.as_path(self.data_dir)
    if self.split is not None and not self.split:
      raise ValueError(f'Split must be a non-empty string: {self}')
    if self.filetype_suffix is not None and not self.filetype_suffix:
      raise ValueError(f'Filetype suffix must be a non-empty string: {self}')

  def is_complete(self) -> bool:
    return bool(self.split and self.filetype_suffix)

  def _assert_is_complete(self) -> None:
    if not self.is_complete():
      raise ValueError(f'Template is incomplete: {self}')

  @property
  def filename_prefix(self) -> str:
    """The part of the filename up until the shard information."""
    if not self.split:
      raise ValueError(f'Split must be a non-empty string: {self}')
    if not self.filetype_suffix:
      raise ValueError(f'Filetype suffix must be a non-empty string: {self}')
    filename_prefix = filename_prefix_for_split(
        name=self.dataset_name, split=self.split)
    return f'{filename_prefix}.{self.filetype_suffix}'

  @property
  def filepath_prefix(self) -> str:
    """The part of the filename up until the shard info, including the folder if given."""
    self._assert_is_complete()
    assert self.data_dir
    return os.path.join(self.data_dir, self.filename_prefix)

  def sharded_filename(
      self,
      *,
      shard_index: int,
      num_shards: Optional[int],
  ) -> str:
    """Returns the filename (excluding the path) for the given shard.

    Arguments:
      shard_index: the shard index for which to generate the filename.
      num_shards: the total number of shards. If unknown, use None.

    Returns:
      The filename for the given shard.
    """
    assert shard_index >= 0
    if self.append_num_shards:
      assert shard_index < num_shards
    template = shard_suffix_template(
        append_num_shards=self.append_num_shards, num_shards=num_shards)
    shard_suffix = template.format(
        shard_index=shard_index, num_shards=num_shards)
    return f'{self.filename_prefix}-{shard_suffix}'

  def sharded_filepath(
      self,
      *,
      shard_index: int,
      num_shards: Optional[int],
  ) -> generic_path.ReadWritePath:
    """Returns the filename (including full path if `data_dir` is set) for the given shard."""
    self._assert_is_complete()
    assert self.data_dir
    filename = self.sharded_filename(
        shard_index=shard_index, num_shards=num_shards)
    return generic_path.as_path(os.path.join(self.data_dir, filename))

  def sharded_filepaths_pattern(
      self,
      *,
      num_shards: Optional[int] = None,
  ) -> str:
    """Returns a pattern describing all the file paths captured by this template.

    If `num_shards` is given, then it returns
    '/path/dataset_name-split.fileformat@num_shards`.
    If `num_shards` is not given, then it returns
    '/path/dataset_name-split.fileformat*`.

    Args:
      num_shards: optional specification of the number of shards.

    Returns:
      the pattern describing all shards captured by this template.
    """
    if num_shards and self.append_num_shards:
      return f'{self.filepath_prefix}@{num_shards}'
    return f'{self.filepath_prefix}*'

  def sharded_filepaths(self,
                        num_shards: int) -> List[generic_path.ReadWritePath]:
    return [
        self.sharded_filepath(shard_index=i, num_shards=num_shards)
        for i in range(num_shards)
    ]

  def sharded_filenames(self, num_shards: int) -> List[str]:
    return [
        self.sharded_filename(shard_index=i, num_shards=num_shards)
        for i in range(num_shards)
    ]

  def replace(self, **kwargs: Any) -> 'ShardedFileTemplate':
    """Returns a copy of the `ShardedFileTemplate` with updated attributes."""
    return dataclasses.replace(self, **kwargs)


def filepattern_for_dataset_split(
    *,
    dataset_name: str,
    split: str,
    data_dir: str,
    filetype_suffix: Optional[str] = None,
    num_shards: Optional[int] = None,
) -> str:
  """Returns the file pattern for the given dataset.

  TODO(tfds): remove this by start using ShardedFileTemplate

  Args:
    dataset_name: Name of the dataset
    split: Name of the requested split
    data_dir: The base folder that contains the dataset.
    filetype_suffix: Optional suffix, e.g. tfrecord
    num_shards: Optional argument. If specified, will return file@num_shards
      notation, otherwise file*.
  """
  template = ShardedFileTemplate(
      data_dir=generic_path.as_path(data_dir),
      dataset_name=dataset_name,
      split=split,
      filetype_suffix=filetype_suffix)
  return os.fspath(template.sharded_filepaths_pattern(num_shards=num_shards))


def filenames_for_dataset_split(
    dataset_name: str,
    split: str,
    num_shards: int,
    filetype_suffix: str,
    data_dir: Optional[type_utils.PathLike] = None,
) -> List[str]:
  """Returns the list of filenames for the given dataset and split."""
  # TODO(tfds): remove this by start using ShardedFileTemplate
  template = ShardedFileTemplate(
      dataset_name=dataset_name,
      split=split,
      filetype_suffix=filetype_suffix,
      data_dir=generic_path.as_path(data_dir))
  return [
      os.fspath(fp) for fp in template.sharded_filenames(num_shards=num_shards)
  ]


def filepaths_for_dataset_split(
    dataset_name: str,
    split: str,
    num_shards: int,
    data_dir: str,
    filetype_suffix: str,
) -> List[str]:
  """File paths of a given dataset split."""
  # TODO(tfds): remove this by start using ShardedFileTemplate
  template = ShardedFileTemplate(
      dataset_name=dataset_name,
      split=split,
      filetype_suffix=filetype_suffix,
      data_dir=generic_path.as_path(data_dir))
  return [
      os.fspath(fp) for fp in template.sharded_filepaths(num_shards=num_shards)
  ]


@dataclasses.dataclass(eq=True, frozen=True)
class FilenameInfo:
  """Structure representing a filename.

  Filenames have the following specs:

  ```
  <dataset_name>-<split_name>.<file-extension>-xxxxxx-of-yyyyyy
  ```

  """
  dataset_name: str
  split: str
  filetype_suffix: str
  shard_index: int
  num_shards: int

  @classmethod
  def from_str(cls, filename: str) -> 'FilenameInfo':
    """Factory to create a `FilenameInfo` from filename."""
    # Strip of the directory if the filename contains it.
    filename = os.path.basename(filename)
    match = _parse_filename(filename)
    if not match:  # No match found
      raise ValueError(
          f'Filename {filename!r} does not follow pattern: '
          '<dataset_name>-<split_name>.<file-extension>-xxxxxx-of-yyyyyy')
    values = match.groupdict()
    return cls(
        dataset_name=values['dataset_name'],
        split=values['split'],
        filetype_suffix=values['filetype_suffix'],
        shard_index=int(values['shard_index']),
        num_shards=int(values['num_shards']),
    )

  @staticmethod
  def is_valid(filename: str) -> bool:
    """Returns True if the filename follow the given pattern."""
    return bool(_parse_filename(filename))

  def __str__(self) -> str:
    # Note: It's possible for `shard_index` and `num_shards` to exceed 5 digits,
    # e.g., "000123-of-654321", "123456-of-654321".
    num_digits = max(5, len(str(self.num_shards)))
    return (
        f'{self.dataset_name}-{self.split}.{self.filetype_suffix}-'
        f'{self.shard_index:0{num_digits}}-of-{self.num_shards:0{num_digits}}')


def _parse_filename(filename: str) -> Optional['re.Match']:
  """Parse the tf-record filename."""
  pattern = (rf'(?P<dataset_name>{_NAME_CLASS})-(?P<split>\w+)\.'
             r'(?P<filetype_suffix>\w+)-'
             r'(?P<shard_index>\d{5,})-of-(?P<num_shards>\d{5,})')
  return re.fullmatch(pattern, filename)
