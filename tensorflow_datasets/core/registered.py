# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

# Lint as: python3
"""Access registered datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import contextlib
import inspect
import posixpath
import re
from typing import Any, Callable, Iterable, Iterator, List, Optional, Type

from absl import flags
from absl import logging
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import gcs_utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import version


FLAGS = flags.FLAGS

__all__ = [
    "RegisteredDataset",
    "list_builders",
    "builder",
    "load",
]


# Cannot use real typing due to circular dependencies. Could this be fixed ?
DatasetBuilder = Any

PredicateFn = Callable[[Type[DatasetBuilder]], bool]


# Internal registry containing <str registered_name, DatasetBuilder subclass>
_DATASET_REGISTRY = {}

# Internal registry containing:
# <str snake_cased_name, abstract DatasetBuilder subclass>
_ABSTRACT_DATASET_REGISTRY = {}

# Datasets that are under active development and which we can't therefore load.
# <str snake_cased_name, in development DatasetBuilder subclass>
_IN_DEVELOPMENT_REGISTRY = {}


_NAME_STR_ERR = """\
Parsing builder name string {} failed.
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
"""

_DATASET_NOT_FOUND_ERR = """\
Check that:
    - if dataset was added recently, it may only be available
      in `tfds-nightly`
    - the dataset name is spelled correctly
    - dataset class defines all base class abstract methods
    - dataset class is not in development, i.e. if IN_DEVELOPMENT=True
    - the module defining the dataset class is imported
"""


# Regex matching 'dataset/config:1.*.*/arg=123'
_NAME_REG = re.compile(
    r"^"
    r"(?P<dataset_name>\w+)"
    r"(/(?P<config>[\w\-\.]+))?"
    r"(:(?P<version>(\d+|\*)(\.(\d+|\*)){2}))?"
    r"(/(?P<kwargs>(\w+=\w+)(,\w+=[^,]+)*))?"
    r"$")


# Regex matching 'dataset/config/1.3.0'
_FULL_NAME_REG = re.compile(r"^{ds_name}/({config_name}/)?{version}$".format(
    ds_name=r"\w+",
    config_name=r"[\w\-\.]+",
    version=r"[0-9]+\.[0-9]+\.[0-9]+",
))


_skip_registration = False


@contextlib.contextmanager
def skip_registration():
  """Context manager within which dataset builders are not registered."""
  global _skip_registration
  try:
    _skip_registration = True
    yield
  finally:
    _skip_registration = False


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

  def __new__(cls, cls_name, bases, class_dict):
    name = naming.camelcase_to_snakecase(cls_name)
    class_dict["name"] = name
    builder_cls = super(RegisteredDataset, cls).__new__(  # pylint: disable=too-many-function-args,redefined-outer-name
        cls, cls_name, bases, class_dict)

    if py_utils.is_notebook():  # On Colab/Jupyter, we allow overwriting
      pass
    elif name in _DATASET_REGISTRY:
      raise ValueError("Dataset with name %s already registered." % name)
    elif name in _IN_DEVELOPMENT_REGISTRY:
      raise ValueError(
          "Dataset with name %s already registered as in development." % name)
    elif name in _ABSTRACT_DATASET_REGISTRY:
      raise ValueError(
          "Dataset with name %s already registered as abstract." % name)

    if _skip_registration:
      pass  # Skip dataset registration within the contextmanager
    elif inspect.isabstract(builder_cls):
      _ABSTRACT_DATASET_REGISTRY[name] = builder_cls
    elif class_dict.get("IN_DEVELOPMENT"):
      _IN_DEVELOPMENT_REGISTRY[name] = builder_cls
    else:
      _DATASET_REGISTRY[name] = builder_cls
    return builder_cls


def list_builders():
  """Returns the string names of all `tfds.core.DatasetBuilder`s."""
  return sorted(list(_DATASET_REGISTRY))


def builder_cls(name: str):
  """Fetches a `tfds.core.DatasetBuilder` class by string name.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the class name
      as camel or snake case: `MyDataset` or `my_dataset`).

  Returns:
    A `tfds.core.DatasetBuilder` class.

  Raises:
    DatasetNotFoundError: if `name` is unrecognized.
  """
  name, kwargs = _dataset_name_and_kwargs_from_name_str(name)
  if kwargs:
    raise ValueError(
        "`builder_cls` only accept the `dataset_name` without config, "
        "version or arguments. Got: name='{}', kwargs={}".format(name, kwargs))

  if name in _ABSTRACT_DATASET_REGISTRY:
    raise DatasetNotFoundError(name, is_abstract=True)
  if name in _IN_DEVELOPMENT_REGISTRY:
    raise DatasetNotFoundError(name, in_development=True)
  if name not in _DATASET_REGISTRY:
    raise DatasetNotFoundError(name)
  return _DATASET_REGISTRY[name]


def builder(name, **builder_init_kwargs):
  """Fetches a `tfds.core.DatasetBuilder` by string name.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the class name
      as camel or snake case: `MyDataset` or `my_dataset`).
      This can be either `'dataset_name'` or
      `'dataset_name/config_name'` for datasets with `BuilderConfig`s.
      As a convenience, this string may contain comma-separated keyword
      arguments for the builder. For example `'foo_bar/a=True,b=3'` would use
      the `FooBar` dataset passing the keyword arguments `a=True` and `b=3`
      (for builders with configs, it would be `'foo_bar/zoo/a=True,b=3'` to
      use the `'zoo'` config and pass to the builder keyword arguments `a=True`
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
  with py_utils.try_reraise(
      prefix="Failed to construct dataset {}".format(name)):
    return builder_cls(name)(**builder_kwargs)


@api_utils.disallow_positional_args(allowed=["name"])
def load(name,
         split=None,
         data_dir=None,
         batch_size=None,
         shuffle_files=False,
         download=True,
         as_supervised=False,
         decoders=None,
         read_config=None,
         with_info=False,
         builder_kwargs=None,
         download_and_prepare_kwargs=None,
         as_dataset_kwargs=None,
         try_gcs=False):
  # pylint: disable=line-too-long
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
    batch_size: `int`, if set, add a batch dimension to examples. Note that
      variable length features will be 0-padded. If
      `batch_size=-1`, will return the full dataset as `tf.Tensor`s.
    shuffle_files: `bool`, whether to shuffle the input files.
      Defaults to `False`.
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
    decoders: Nested dict of `Decoder` objects which allow to customize the
      decoding. The structure should match the feature structure, but only
      customized feature keys need to be present. See
      [the guide](https://github.com/tensorflow/datasets/tree/master/docs/decode.md)
      for more info.
    read_config: `tfds.ReadConfig`, Additional options to configure the
      input pipeline (e.g. seed, num parallel reads,...).
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
      `tfds.core.DatasetBuilder.as_dataset`.
    try_gcs: `bool`, if True, tfds.load will see if the dataset exists on
      the public GCS bucket before building it locally.

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
  # pylint: enable=line-too-long

  name, name_builder_kwargs = _dataset_name_and_kwargs_from_name_str(name)
  name_builder_kwargs.update(builder_kwargs or {})
  builder_kwargs = name_builder_kwargs

  # Set data_dir
  if try_gcs and gcs_utils.is_dataset_on_gcs(name):
    data_dir = constants.GCS_DATA_DIR
  elif data_dir is None:
    data_dir = constants.DATA_DIR

  dbuilder = builder(name, data_dir=data_dir, **builder_kwargs)
  if download:
    download_and_prepare_kwargs = download_and_prepare_kwargs or {}
    dbuilder.download_and_prepare(**download_and_prepare_kwargs)

  if as_dataset_kwargs is None:
    as_dataset_kwargs = {}
  as_dataset_kwargs = dict(as_dataset_kwargs)
  as_dataset_kwargs.setdefault("split", split)
  as_dataset_kwargs.setdefault("as_supervised", as_supervised)
  as_dataset_kwargs.setdefault("batch_size", batch_size)
  as_dataset_kwargs.setdefault("decoders", decoders)
  as_dataset_kwargs.setdefault("shuffle_files", shuffle_files)
  as_dataset_kwargs.setdefault("read_config", read_config)

  ds = dbuilder.as_dataset(**as_dataset_kwargs)
  if with_info:
    return ds, dbuilder.info
  return ds


def _dataset_name_and_kwargs_from_name_str(name_str):
  """Extract kwargs from name str."""
  res = _NAME_REG.match(name_str)
  if not res:
    raise ValueError(_NAME_STR_ERR.format(name_str))
  name = res.group("dataset_name")
  # Normalize the name to accept CamelCase
  name = naming.camelcase_to_snakecase(name)
  kwargs = _kwargs_str_to_kwargs(res.group("kwargs"))
  try:
    for attr in ["config", "version"]:
      val = res.group(attr)
      if val is None:
        continue
      if attr in kwargs:
        raise ValueError("Dataset %s: cannot pass %s twice." % (name, attr))
      kwargs[attr] = val
    return name, kwargs
  except:
    logging.error(_NAME_STR_ERR.format(name_str))   # pylint: disable=logging-format-interpolation
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


def _get_all_versions(
    current_version: version.Version,
    extra_versions: Iterable[version.Version],
    current_version_only: bool,
) -> Iterable[str]:
  """Returns the list of all current versions."""
  # Merge current version with all extra versions
  version_list = [current_version]
  if current_version_only:
    version_list.extend(extra_versions)
  # Filter datasets which do not have a version (version is `None`) as they
  # should not be instantiated directly (e.g wmt_translate)
  return {str(v) for v in version_list if v}


def _iter_single_full_names(
    builder_name: str,
    builder_cls: Type[DatasetBuilder],  # pylint: disable=redefined-outer-name
    current_version_only: bool,
) -> Iterator[str]:
  """Iterate over a single builder full names."""
  if builder_cls.BUILDER_CONFIGS:
    for config in builder_cls.BUILDER_CONFIGS:
      for v in _get_all_versions(
          config.version,
          config.supported_versions,
          current_version_only=current_version_only,
      ):
        yield posixpath.join(builder_name, config.name, v)
  else:
    for v in _get_all_versions(
        builder_cls.VERSION,
        builder_cls.SUPPORTED_VERSIONS,
        current_version_only=current_version_only
    ):
      yield posixpath.join(builder_name, v)


def _iter_full_names(
    predicate_fn: Optional[PredicateFn],
    current_version_only: bool,
) -> Iterator[str]:
  """Yield all registered datasets full_names (see `list_full_names`)."""
  for builder_name, builder_cls in _DATASET_REGISTRY.items():  # pylint: disable=redefined-outer-name
    # Only keep requested datasets
    if predicate_fn is not None and not predicate_fn(builder_cls):
      continue
    for full_name in _iter_single_full_names(
        builder_name,
        builder_cls,
        current_version_only=current_version_only,
    ):
      yield full_name


def list_full_names(
    predicate_fn: Optional[PredicateFn] = None,
    current_version_only: bool = False,
) -> List[str]:
  """Lists all registered datasets full_names.

  Args:
    predicate_fn: `Callable[[Type[DatasetBuilder]], bool]`, if set, only
      returns the dataset names which satisfy the predicate.
    current_version_only: If True, only returns the current version.

  Returns:
    The list of all registered dataset full names.
  """
  return sorted(_iter_full_names(
      predicate_fn=predicate_fn,
      current_version_only=current_version_only,
  ))


def single_full_names(
    builder_name: str,
    current_version_only: bool = True,
) -> List[str]:
  """Returns the list `['ds/c0/v0',...]` or `['ds/v']` for a single builder."""
  return sorted(_iter_single_full_names(
      builder_name,
      _DATASET_REGISTRY[builder_name],
      current_version_only=current_version_only,
  ))


def is_full_name(full_name: str) -> bool:
  """Returns whether the string pattern match `ds/config/1.2.3` or `ds/1.2.3`.

  Args:
    full_name: String to check.

  Returns:
    `bool`.
  """
  return bool(_FULL_NAME_REG.match(full_name))
