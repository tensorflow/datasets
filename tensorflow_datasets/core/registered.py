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
import inspect

import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import constants
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


class DatasetNotFoundError(ValueError):
  """The requested Dataset was not found."""

  def __init__(self, name):
    all_datasets_str = "\n\t- ".join([""] + list_builders())
    ValueError.__init__(self, (
        "Dataset %s not found. Available datasets:%s\n"
        "Check that:\n"
        "\t- the dataset name is spelled correctly\n"
        "\t- dataset class defines all base class abstract methods\n"
        "\t- the module defining the dataset class is imported\n"
        ) % (name, all_datasets_str))


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
  """Returns the string names of all `tfds.core.DatasetBuilder`s."""
  return sorted(list(_DATASET_REGISTRY))


def builder(name, **ctor_kwargs):
  """Fetches a `tfds.core.DatasetBuilder` by string name.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the snake case
      version of the class name). As a convenience, this string may contain
      comma-separated keyword arguments for the builder separated from the name
      by a "/". For example `"foo_bar/a=True,b=3"` would use the `FooBar`
      dataset with keyword arguments `a=True` and `b=3`.
    **ctor_kwargs: `dict` of keyword arguments passed to the `DatasetBuilder`.
      These will override keyword arguments passed in `name`, if any.

  Returns:
    A `tfds.core.DatasetBuilder`.

  Raises:
    ValueError: if `name` is unrecognized.
  """
  name, builder_kwargs = _dataset_name_and_kwargs_from_name_str(name)
  builder_kwargs.update(ctor_kwargs)
  if name not in _DATASET_REGISTRY:
    raise DatasetNotFoundError(name)
  return _DATASET_REGISTRY[name](**builder_kwargs)


@api_utils.disallow_positional_args(allowed=["name"])
def load(name,
         split,
         data_dir=None,
         download=True,
         as_supervised=False,
         with_info=False,
         builder_kwargs=None,
         download_and_prepare_kwargs=None,
         as_dataset_kwargs=None):
  """Loads the given `tfds.Split` as a `tf.data.Dataset`.

  `load` is a convenience method that fetches the `tfds.core.DatasetBuilder` by
  string name, optionally calls `DatasetBuilder.download_and_prepare`
  (if `download=True`), and then calls `DatasetBuilder.as_dataset`.
  This is roughly equivalent to:

  ```
  builder = tfds.builder(name, data_dir=data_dir, **builder_kwargs)
  if download:
    builder.download_and_prepare(**download_and_prepare_kwargs)
  ds = builder.as_dataset(
      split=split, as_supervised=as_supervised, **as_dataset_kwargs)
  if with_info:
    return ds, builder.info
  return ds
  ```

  Callers must pass arguments as keyword arguments.

  **Warning**: calling this function might potentially trigger the download
  of hundreds of GiB to disk. Refer to download argument.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the snake case
      version of the class name). As a convenience, this string may contain
      comma-separated keyword arguments for the builder. For example
      `"foo_bar/a=True,b=3"` would use the `FooBar` dataset passing the keyword
      arguments `a=True` and `b=3`.
    split: `tfds.Split`, which split of the data to load.
    data_dir: `str` (optional), directory to read/write data.
      Defaults to "~/tensorflow_datasets".
    download: `bool` (optional), whether to call
      `tfds.core.DatasetBuilder.download_and_prepare`
      before calling `tf.DatasetBuilder.as_dataset`. If `False`, data is
      expected to be in `data_dir`. If `True` and the data is already in
      `data_dir`, `download_and_prepare` is a no-op.
      Defaults to `True`.
    as_supervised: `bool`, if `True`, the returned `tf.data.Dataset`
      will have a 2-tuple structure `(input, label)` according to
      `builder.info.supervised_keys`. If `False`, the default,
      the returned `tf.data.Dataset` will have a dictionary with all the
      features.
    with_info: `bool`, if True, tfds.load will return the tuple
      (tf.data.Dataset, tfds.core.DatasetInfo) containing the info associated
      with the builder.
    builder_kwargs: `dict` (optional), keyword arguments to be passed to the
      `tfds.core.DatasetBuilder` constructor. `data_dir` will be passed
      through by default.
    download_and_prepare_kwargs: `dict` (optional) keyword arguments passed to
      `tfds.core.DatasetBuilder.download_and_prepare` if `download=True`. Allow
      to control where to download and extract the cached data. If not set,
      cache_dir and manual_dir will automatically be deduced from data_dir.
    as_dataset_kwargs: `dict` (optional), keyword arguments passed to
      `tfds.core.DatasetBuilder.as_dataset`. `split` will be passed through by
      default.

  Returns:
    ds: `tf.data.Dataset`, the dataset requested.
    ds_info: `tfds.core.DatasetInfo`, if `with_info` is True, then tfds.load
      will return a tuple (ds, ds_info) containing the dataset info (version,
      features, splits, num_examples,...).
  """
  if data_dir is None:
    data_dir = constants.DATA_DIR
  builder_kwargs = builder_kwargs or {}
  dbuilder = builder(name, data_dir=data_dir, **builder_kwargs)
  if download:
    download_and_prepare_kwargs = download_and_prepare_kwargs or {}
    dbuilder.download_and_prepare(**download_and_prepare_kwargs)

  if as_dataset_kwargs is None:
    as_dataset_kwargs = {}
  as_dataset_kwargs = dict(as_dataset_kwargs)
  as_dataset_kwargs["split"] = split
  as_dataset_kwargs["as_supervised"] = as_supervised

  ds = dbuilder.as_dataset(**as_dataset_kwargs)
  if with_info:
    return ds, dbuilder.info
  return ds


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
