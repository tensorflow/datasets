# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Access registered datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import functools
import inspect

import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import naming

__all__ = [
    "RegisteredDataset",
    "list_builders",
    "builder",
    "load",
]

# Internal registry containing <str registered_name, DatasetBuilder subclass>
_DATASET_REGISTRY = {}

_STR_KWARGS_ERR = ("To pass keyword arguments to DatasetBuilders by string, "
                   "the format must be 'dataset_name/kwarg1=val1,kwarg2=val2'")


class RegisteredDataset(abc.ABCMeta):
  """Subclasses will be registered and given a `name` property."""

  def __new__(mcs, cls_name, bases, class_dict):
    name = naming.camelcase_to_snakecase(cls_name)
    class_dict["name"] = name
    cls = super(RegisteredDataset, mcs).__new__(
        mcs, cls_name, bases, class_dict)

    if name in _DATASET_REGISTRY:
      raise ValueError("Dataset with name %s already registered." % name)
    if not inspect.isabstract(cls):
      _DATASET_REGISTRY[name] = cls
    return cls


def list_builders():
  """Returns the string names of all `tfds.DatasetBuilder`s."""
  return sorted(list(_DATASET_REGISTRY))


def builder(name):
  """Fetches a `tfds.DatasetBuilder` by string name.

  Args:
    name (str): the registered name of the `DatasetBuilder` (the snake case
      version of the class name). As a convenience, this string may contain
      comma-separated keyword arguments for the builder. For example
      `"foo_bar/a=True,b=3"` would use the `FooBar` dataset passing the keyword
      arguments `a=True` and `b=3`.

  Returns:
    Constructor for the named `DatasetBuilder`.

    If `name` does not contain keyword arguments, this will be the named
    `DatasetBuilder` class itself. If `name` does contain kwargs, this will be a
    wrapper function with the keyword arguments partially applied.

  Raises:
    ValueError: if `name` is unrecognized.
  """
  name, str_kwargs = _dataset_name_and_kwargs_from_name_str(name)
  if name not in _DATASET_REGISTRY:
    all_datasets_str = "".join(["  * %s\n" % d for d in list_builders()])
    raise ValueError("Dataset %s not found. Available datasets:\n%s" %
                     (name, all_datasets_str))

  if not str_kwargs:
    return _DATASET_REGISTRY[name]

  @functools.wraps(_DATASET_REGISTRY[name])
  def wrapped_dataset_constructor(**dataset_kwargs):
    all_kwargs = {}
    all_kwargs.update(str_kwargs)
    all_kwargs.update(dataset_kwargs)
    return _DATASET_REGISTRY[name](**all_kwargs)

  return wrapped_dataset_constructor


@api_utils.disallow_positional_args
def load(name,
         data_dir=api_utils.REQUIRED_ARG,
         download=False,
         **as_dataset_kwargs):
  """Loads the given `tfds.Split` as a `tf.data.Dataset`.

  `load` is a convenience method that fetches the `tfds.DatasetBuilder` by
  string name, optionally calls `DatasetBuilder.download_and_prepare`
  (if `download=True`), and then calls `DatasetBuilder.as_dataset`.

  Callers must pass arguments as keyword arguments.

  Args:
    name (str): the registered name of the `DatasetBuilder` (the snake case
      version of the class name). As a convenience, this string may contain
      comma-separated keyword arguments for the builder. For example
      `"foo_bar/a=True,b=3"` would use the `FooBar` dataset passing the keyword
      arguments `a=True` and `b=3`.
    data_dir (str): directory to read/write data.
    download (bool): whether to call `tfds.DatasetBuilder.download_and_prepare`
      before calling `tf.DatasetBuilder.as_dataset`. If `False`, data is
      expected to be in `data_dir`. If `True` and the data is already in
      `data_dir`, `download_and_prepare` is a no-op. Optional,
      defaults to `False`.
    **as_dataset_kwargs (dict): Keyword arguments passed to
      `tfds.DatasetBuilder.as_dataset`.

  Returns:
    `tf.data.Dataset`
  """
  name, str_kwargs = _dataset_name_and_kwargs_from_name_str(name)
  all_kwargs = dict(data_dir=data_dir)
  all_kwargs.update(str_kwargs)
  dbuilder = builder(name)(**all_kwargs)
  if download:
    dbuilder.download_and_prepare()
  return dbuilder.as_dataset(**as_dataset_kwargs)


def _dataset_name_and_kwargs_from_name_str(name_str):
  """Extract kwargs from name str."""
  if "/" not in name_str:
    if "," in name_str:
      raise ValueError(_STR_KWARGS_ERR)
    return name_str, {}

  try:
    dataset_name, kwargs_str = name_str.split("/")
    kwarg_strs = kwargs_str.split(",")
    kwargs = {}
    for kwarg_str in kwarg_strs:
      kwarg_name, kwarg_val = kwarg_str.split("=")
      kwargs[kwarg_name] = _cast_to_pod(kwarg_val)
    return dataset_name, kwargs
  except:
    tf.logging.error()
    raise


def _cast_to_pod(val):
  """Try cast to int, float, bool, str, in that order."""
  bools = {"True": True, "False": False}
  if val in bools:
    return bools[val]
  try:
    return int(val)
  except ValueError:
    try:
      return float(val)
    except ValueError:
      return tf.compat.as_text(val)
