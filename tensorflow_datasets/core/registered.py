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

"""Access registered datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import inspect

from absl import flags
from absl import logging
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import naming


FLAGS = flags.FLAGS

__all__ = [
    "RegisteredDataset",
    "list_builders",
    "builder",
    "load",
]

# Internal registry containing <str registered_name, DatasetBuilder subclass>
_DATASET_REGISTRY = {}

# Internal registry containing:
# <str snake_cased_name, abstract DatasetBuilder subclass>
_ABSTRACT_DATASET_REGISTRY = {}

# Datasets that are under active development and which we can't therefore load.
# <str snake_cased_name, in development DatasetBuilder subclass>
_IN_DEVELOPMENT_REGISTRY = {}


_NAME_STR_ERR = """\
Parsing builder name string failed.
The builder name string must be in one of the following formats:
  * "dataset_name"
  * "dataset_name/config_name"
  * "dataset_name/kwarg1=val1,kwarg2=val2"
  * "dataset_name/config_name/kwarg1=val1,kwarg2=val2"
"""

_DATASET_NOT_FOUND_ERR = """\
Check that:
    - the dataset name is spelled correctly
    - dataset class defines all base class abstract methods
    - dataset class is not in development, i.e. if IN_DEVELOPMENT=True
    - the module defining the dataset class is imported
"""


class DatasetNotFoundError(ValueError):
  """The requested Dataset was not found."""

  def __init__(self, name, is_abstract=False, in_development=False):
    all_datasets_str = "\n\t- ".join([""] + list_builders())
    if is_abstract:
      error_string = ("Dataset %s is an abstract class so cannot be created. "
                      "Please make sure to instantiate all abstract methods.\n"
                      "%s") % (name, _DATASET_NOT_FOUND_ERR)
    elif in_development:
      error_string = ("Dataset %s is under active development and is not "
                      "available yet.\n") % name
    else:
      error_string = ("Dataset %s not found. Available datasets:%s\n"
                      "%s") % (name, all_datasets_str, _DATASET_NOT_FOUND_ERR)
    ValueError.__init__(self, error_string)


class RegisteredDataset(abc.ABCMeta):
  """Subclasses will be registered and given a `name` property."""

  def __new__(mcs, cls_name, bases, class_dict):
    name = naming.camelcase_to_snakecase(cls_name)
    class_dict["name"] = name
    cls = super(RegisteredDataset, mcs).__new__(
        mcs, cls_name, bases, class_dict)

    if name in _DATASET_REGISTRY:
      raise ValueError("Dataset with name %s already registered." % name)
    if name in _IN_DEVELOPMENT_REGISTRY:
      raise ValueError(
          "Dataset with name %s already registered as in development." % name)
    if name in _ABSTRACT_DATASET_REGISTRY:
      raise ValueError(
          "Dataset with name %s already registered as abstract." % name)

    if inspect.isabstract(cls):
      _ABSTRACT_DATASET_REGISTRY[name] = cls
    elif class_dict.get("IN_DEVELOPMENT"):
      _IN_DEVELOPMENT_REGISTRY[name] = cls
    else:
      _DATASET_REGISTRY[name] = cls
    return cls


def list_builders():
  """Returns the string names of all `tfds.core.DatasetBuilder`s."""
  return sorted(list(_DATASET_REGISTRY))


def builder(name, **builder_init_kwargs):
  """Fetches a `tfds.core.DatasetBuilder` by string name.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the snake case
      version of the class name). This can be either `"dataset_name"` or
      `"dataset_name/config_name"` for datasets with `BuilderConfig`s.
      As a convenience, this string may contain comma-separated keyword
      arguments for the builder. For example `"foo_bar/a=True,b=3"` would use
      the `FooBar` dataset passing the keyword arguments `a=True` and `b=3`
      (for builders with configs, it would be `"foo_bar/zoo/a=True,b=3"` to
      use the `"zoo"` config and pass to the builder keyword arguments `a=True`
      and `b=3`).
    **builder_init_kwargs: `dict` of keyword arguments passed to the
      `DatasetBuilder`. These will override keyword arguments passed in `name`,
      if any.

  Returns:
    A `tfds.core.DatasetBuilder`.

  Raises:
    DatasetNotFoundError: if `name` is unrecognized.
  """
  name, builder_kwargs = _dataset_name_and_kwargs_from_name_str(name)
  builder_kwargs.update(builder_init_kwargs)
  if name in _ABSTRACT_DATASET_REGISTRY:
    raise DatasetNotFoundError(name, is_abstract=True)
  if name in _IN_DEVELOPMENT_REGISTRY:
    raise DatasetNotFoundError(name, in_development=True)
  if name not in _DATASET_REGISTRY:
    raise DatasetNotFoundError(name)
  try:
    return _DATASET_REGISTRY[name](**builder_kwargs)
  except BaseException:
    logging.error("Failed to construct dataset %s", name)
    raise


@api_utils.disallow_positional_args(allowed=["name"])
def load(name,
         split=None,
         data_dir=None,
         batch_size=1,
         download=True,
         as_supervised=False,
         with_info=False,
         builder_kwargs=None,
         download_and_prepare_kwargs=None,
         as_dataset_kwargs=None):
  """Loads the named dataset into a `tf.data.Dataset`.

  If `split=None` (the default), returns all splits for the dataset. Otherwise,
  returns the specified split.

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

  If you'd like NumPy arrays instead of `tf.data.Dataset`s or `tf.Tensor`s,
  you can pass the return value to `tfds.as_numpy`.

  Callers must pass arguments as keyword arguments.

  **Warning**: calling this function might potentially trigger the download
  of hundreds of GiB to disk. Refer to the `download` argument.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the snake case
      version of the class name). This can be either `"dataset_name"` or
      `"dataset_name/config_name"` for datasets with `BuilderConfig`s.
      As a convenience, this string may contain comma-separated keyword
      arguments for the builder. For example `"foo_bar/a=True,b=3"` would use
      the `FooBar` dataset passing the keyword arguments `a=True` and `b=3`
      (for builders with configs, it would be `"foo_bar/zoo/a=True,b=3"` to
      use the `"zoo"` config and pass to the builder keyword arguments `a=True`
      and `b=3`).
    split: `tfds.Split` or `str`, which split of the data to load. If None,
      will return a `dict` with all splits (typically `tfds.Split.TRAIN` and
      `tfds.Split.TEST`).
    data_dir: `str` (optional), directory to read/write data.
      Defaults to "~/tensorflow_datasets".
    batch_size: `int`, set to > 1 to get batches of examples. Note that
      variable length features will be 0-padded. If
      `batch_size=-1`, will return the full dataset as `tf.Tensor`s.
    download: `bool` (optional), whether to call
      `tfds.core.DatasetBuilder.download_and_prepare`
      before calling `tf.DatasetBuilder.as_dataset`. If `False`, data is
      expected to be in `data_dir`. If `True` and the data is already in
      `data_dir`, `download_and_prepare` is a no-op.
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
    ds: `tf.data.Dataset`, the dataset requested, or if `split` is None, a
      `dict<key: tfds.Split, value: tfds.data.Dataset>`. If `batch_size=-1`,
      these will be full datasets as `tf.Tensor`s.
    ds_info: `tfds.core.DatasetInfo`, if `with_info` is True, then `tfds.load`
      will return a tuple `(ds, ds_info)` containing dataset information
      (version, features, splits, num_examples,...). Note that the `ds_info`
      object documents the entire dataset, regardless of the `split` requested.
      Split-specific information is available in `ds_info.splits`.
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
  as_dataset_kwargs["batch_size"] = batch_size

  ds = dbuilder.as_dataset(**as_dataset_kwargs)
  if with_info:
    return ds, dbuilder.info
  return ds


def _dataset_name_and_kwargs_from_name_str(name_str):
  """Extract kwargs from name str."""
  num_slashes = name_str.count("/")
  has_kwargs = "," in name_str or "=" in name_str

  try:
    if not num_slashes:
      # 1. dataset_name
      if has_kwargs:
        raise ValueError(_NAME_STR_ERR)
      return name_str, {}

    name_splits = name_str.split("/")
    if has_kwargs:
      if num_slashes == 1:
        # 2. dataset_name/kwargs
        dataset_name, kwargs_str = name_splits
        config = None
      else:
        if num_slashes > 2:
          raise ValueError(_NAME_STR_ERR)
        assert num_slashes == 2
        # 3. dataset_name/config_name/kwargs
        dataset_name, config, kwargs_str = name_splits
    else:
      # 4. dataset_name/config_name
      dataset_name, config = name_splits
      kwargs_str = ""

    kwargs = _kwargs_str_to_kwargs(kwargs_str)
    if "config" in kwargs and config:
      raise ValueError("Cannot pass config twice. Got %s" % name_str)
    kwargs["config"] = config
    return dataset_name, kwargs
  except:
    logging.error(_NAME_STR_ERR)
    raise


def _kwargs_str_to_kwargs(kwargs_str):
  if not kwargs_str:
    return {}
  kwarg_strs = kwargs_str.split(",")
  kwargs = {}
  for kwarg_str in kwarg_strs:
    kwarg_name, kwarg_val = kwarg_str.split("=")
    kwargs[kwarg_name] = _cast_to_pod(kwarg_val)
  return kwargs


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
