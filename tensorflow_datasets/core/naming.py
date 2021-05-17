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

"""Utilities for file names."""

import os
import re
import textwrap
from typing import Any, Dict, Optional, Tuple, Union

import dataclasses

from tensorflow_datasets.core.utils import py_utils

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


def _kwargs_str_to_kwargs(kwargs_str):
  """Converts given `kwargs` as str into kwargs dict."""
  if not kwargs_str:
    return {}
  kwarg_strs = kwargs_str.split(',')
  kwargs = {}
  for kwarg_str in kwarg_strs:
    kwarg_name, kwarg_val = kwarg_str.split('=')
    kwargs[kwarg_name] = _cast_to_pod(kwarg_val)
  return kwargs


def _cast_to_pod(val: str) -> Union[Value]:
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


def sharded_filenames(filename_prefix, num_shards):
  """Sharded filenames given prefix and number of shards."""
  shard_suffix = '%05d-of-%05d'
  return [
      '%s-%s' % (filename_prefix, shard_suffix % (i, num_shards))
      for i in range(num_shards)
  ]


def filepattern_for_dataset_split(dataset_name,
                                  split,
                                  data_dir,
                                  filetype_suffix=None):
  prefix = filename_prefix_for_split(dataset_name, split)
  if filetype_suffix:
    prefix += '.%s' % filetype_suffix
  filepath = os.path.join(data_dir, prefix)
  return '%s*' % filepath


def filenames_for_dataset_split(dataset_name,
                                split,
                                num_shards,
                                filetype_suffix=None):
  prefix = filename_prefix_for_split(dataset_name, split)
  if filetype_suffix:
    prefix += '.%s' % filetype_suffix
  return sharded_filenames(prefix, num_shards)


def filepaths_for_dataset_split(dataset_name,
                                split,
                                num_shards,
                                data_dir,
                                filetype_suffix=None):
  """File paths of a given dataset split."""
  filenames = filenames_for_dataset_split(
      dataset_name=dataset_name,
      split=split,
      num_shards=num_shards,
      filetype_suffix=filetype_suffix,
  )
  filepaths = [os.path.join(data_dir, fname) for fname in filenames]
  return filepaths
