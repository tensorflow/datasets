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

"""Access registered datasets."""

import difflib
import json
import posixpath
import re
import textwrap
import typing
from typing import Any, Callable, Dict, Iterable, Iterator, List, NoReturn, Optional, Type

from absl import logging
from tensorflow_datasets.core import community
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core import visibility
from tensorflow_datasets.core.utils import gcs_utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils import version

# pylint: disable=logging-format-interpolation

Tree = type_utils.Tree
TreeDict = type_utils.TreeDict

PredicateFn = Callable[[Type[dataset_builder.DatasetBuilder]], bool]

# Regex matching 'dataset/config/1.3.0'
_FULL_NAME_REG = re.compile(r'^{ds_name}/({config_name}/)?{version}$'.format(
    ds_name=r'\w+',
    config_name=r'[\w\-\.]+',
    version=r'[0-9]+\.[0-9]+\.[0-9]+',
))


def list_builders(
    *,
    with_community_datasets: bool = True,
) -> List[str]:
  """Returns the string names of all `tfds.core.DatasetBuilder`s."""
  datasets = registered.list_imported_builders()
  if with_community_datasets:
    if visibility.DatasetType.COMMUNITY_PUBLIC.is_available():
      datasets += community.community_register.list_builders()
  return datasets


def builder_cls(name: str) -> Type[dataset_builder.DatasetBuilder]:
  """Fetches a `tfds.core.DatasetBuilder` class by string name.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the class name as
      camel or snake case: `MyDataset` or `my_dataset`).

  Returns:
    A `tfds.core.DatasetBuilder` class.

  Raises:
    DatasetNotFoundError: if `name` is unrecognized.
  """
  ds_name, kwargs = naming.parse_builder_name_kwargs(name)
  if kwargs:
    raise ValueError(
        '`builder_cls` only accept the `dataset_name` without config, '
        f"version or arguments. Got: name='{name}', kwargs={kwargs}")
  try:
    if ds_name.namespace:
      # `namespace:dataset` are loaded from the community register
      if visibility.DatasetType.COMMUNITY_PUBLIC.is_available():
        return community.community_register.builder_cls(ds_name)
      else:
        raise ValueError(
            f'Cannot load {ds_name} when community datasets are disabled')
    else:
      cls = registered.imported_builder_cls(str(ds_name))
      cls = typing.cast(Type[dataset_builder.DatasetBuilder], cls)
    return cls
  except registered.DatasetNotFoundError as e:
    _reraise_with_list_builders(e, name=ds_name)  # pytype: disable=bad-return-type


def builder(
    name: str,
    *,
    try_gcs: bool = False,
    **builder_kwargs: Any,
) -> dataset_builder.DatasetBuilder:
  """Fetches a `tfds.core.DatasetBuilder` by string name.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the class name as
      camel or snake case: `MyDataset` or `my_dataset`). This can be either
      `'dataset_name'` or `'dataset_name/config_name'` for datasets with
      `BuilderConfig`s. As a convenience, this string may contain
      comma-separated keyword arguments for the builder. For example
      `'foo_bar/a=True,b=3'` would use the `FooBar` dataset passing the keyword
      arguments `a=True` and `b=3` (for builders with configs, it would be
      `'foo_bar/zoo/a=True,b=3'` to use the `'zoo'` config and pass to the
      builder keyword arguments `a=True` and `b=3`).
    try_gcs: `bool`, if True, tfds.load will see if the dataset exists on the
      public GCS bucket before building it locally.
    **builder_kwargs: `dict` of keyword arguments passed to the
      `tfds.core.DatasetBuilder`.

  Returns:
    A `tfds.core.DatasetBuilder`.

  Raises:
    DatasetNotFoundError: if `name` is unrecognized.
  """
  # 'kaggle:my_ds/config:1.0.0' -> (
  #     DatasetName('kaggle:my_ds'), {'version': '1.0.0', 'config': 'conf0'}
  # )
  name, builder_kwargs = naming.parse_builder_name_kwargs(
      name, **builder_kwargs)

  # `try_gcs` currently only supports non-community datasets
  if (try_gcs and not name.namespace and
      gcs_utils.is_dataset_on_gcs(str(name))):
    data_dir = builder_kwargs.get('data_dir')
    if data_dir:
      raise ValueError(
          f'Cannot have both `try_gcs=True` and `data_dir={data_dir}` '
          'explicitly set')
    builder_kwargs['data_dir'] = gcs_utils.gcs_path('datasets')
  if (visibility.DatasetType.COMMUNITY_PUBLIC.is_available() and
      community.community_register.has_namespace(name.namespace)):
    return community.community_register.builder(name=name, **builder_kwargs)

  # First check whether we can find the corresponding dataset builder code
  try:
    cls = builder_cls(str(name))
  except registered.DatasetNotFoundError as e:
    cls = None  # Class not found
    not_found_error = e  # Save the exception to eventually reraise

  # Eventually try loading from files first
  if _try_load_from_files_first(cls, **builder_kwargs):
    try:
      return read_only_builder.builder_from_files(str(name), **builder_kwargs)
    except registered.DatasetNotFoundError:
      pass

  # If code exists and loading from files was skipped (e.g. files not found),
  # load from the source code.
  if cls:
    with py_utils.try_reraise(prefix=f'Failed to construct dataset {name}: '):
      return cls(**builder_kwargs)  # pytype: disable=not-instantiable

  # If neither the code nor the files are found, raise DatasetNotFoundError
  raise not_found_error


def _try_load_from_files_first(
    cls: Optional[Type[dataset_builder.DatasetBuilder]],
    **builder_kwargs: Any,
) -> bool:
  """Returns True if files should be used rather than code."""
  if set(builder_kwargs) - {'version', 'config', 'data_dir'}:
    return False  # Has extra kwargs, requires original code.
  elif builder_kwargs.get('version') == 'experimental_latest':
    return False  # Requested version requires original code
  elif not cls:
    return True  # Code does not exist
  elif 'version' in builder_kwargs:
    return True  # Version explicitly given (unlocks backward compatibility)
  elif ('config' in builder_kwargs and
        isinstance(builder_kwargs['config'], str) and
        builder_kwargs['config'] not in cls.builder_configs):
    return True  # Requested config isn't found in the code
  else:
    return False  # Code exists and no version is given, so use code.


def load(
    name: str,
    *,
    split: Optional[Tree[splits_lib.SplitArg]] = None,
    data_dir: Optional[str] = None,
    batch_size: Optional[int] = None,
    shuffle_files: bool = False,
    download: bool = True,
    as_supervised: bool = False,
    decoders: Optional[TreeDict[decode.partial_decode.DecoderArg]] = None,
    read_config: Optional[read_config_lib.ReadConfig] = None,
    with_info: bool = False,
    builder_kwargs: Optional[Dict[str, Any]] = None,
    download_and_prepare_kwargs: Optional[Dict[str, Any]] = None,
    as_dataset_kwargs: Optional[Dict[str, Any]] = None,
    try_gcs: bool = False,
):
  # pylint: disable=line-too-long
  """Loads the named dataset into a `tf.data.Dataset`.

  `tfds.load` is a convenience method that:

  1. Fetch the `tfds.core.DatasetBuilder` by name:

     ```python
     builder = tfds.builder(name, data_dir=data_dir, **builder_kwargs)
     ```

  2. Generate the data (when `download=True`):

     ```python
     builder.download_and_prepare(**download_and_prepare_kwargs)
     ```

  3. Load the `tf.data.Dataset` object:

     ```python
     ds = builder.as_dataset(
         split=split,
         as_supervised=as_supervised,
         shuffle_files=shuffle_files,
         read_config=read_config,
         decoders=decoders,
         **as_dataset_kwargs,
     )
     ```

  See: https://www.tensorflow.org/datasets/overview#load_a_dataset for more
  examples.

  If you'd like NumPy arrays instead of `tf.data.Dataset`s or `tf.Tensor`s,
  you can pass the return value to `tfds.as_numpy`.

  **Warning**: calling this function might potentially trigger the download
  of hundreds of GiB to disk. Refer to the `download` argument.

  Args:
    name: `str`, the registered name of the `DatasetBuilder` (the snake case
      version of the class name). The config and version can also be specified
      in the name as follows: `'dataset_name[/config_name][:version]'`. For
      example, `'movielens/25m-ratings'` (for the latest version of
      `'25m-ratings'`), `'movielens:0.1.0'` (for the default config and version
      0.1.0), or`'movielens/25m-ratings:0.1.0'`. Note that only the latest
      version can be generated, but old versions can be read if they are present
      on disk. For convenience, the `name` parameter can contain comma-separated
      keyword arguments for the builder. For example, `'foo_bar/a=True,b=3'`
      would use the `FooBar` dataset passing the keyword arguments `a=True` and
      `b=3` (for builders with configs, it would be `'foo_bar/zoo/a=True,b=3'`
      to use the `'zoo'` config and pass to the builder keyword arguments
      `a=True` and `b=3`).
    split: Which split of the data to load (e.g. `'train'`, `'test'`, `['train',
      'test']`, `'train[80%:]'`,...). See our [split API
      guide](https://www.tensorflow.org/datasets/splits). If `None`, will return
      all splits in a `Dict[Split, tf.data.Dataset]`
    data_dir: `str`, directory to read/write data. Defaults to the value of the
      environment variable TFDS_DATA_DIR, if set, otherwise falls back to
      datasets are stored.
    batch_size: `int`, if set, add a batch dimension to examples. Note that
      variable length features will be 0-padded. If `batch_size=-1`, will return
      the full dataset as `tf.Tensor`s.
    shuffle_files: `bool`, whether to shuffle the input files. Defaults to
      `False`.
    download: `bool` (optional), whether to call
      `tfds.core.DatasetBuilder.download_and_prepare` before calling
      `tf.DatasetBuilder.as_dataset`. If `False`, data is expected to be in
      `data_dir`. If `True` and the data is already in `data_dir`,
      when data_dir is a Placer path.
    as_supervised: `bool`, if `True`, the returned `tf.data.Dataset` will have a
      2-tuple structure `(input, label)` according to
      `builder.info.supervised_keys`. If `False`, the default, the returned
      `tf.data.Dataset` will have a dictionary with all the features.
    decoders: Nested dict of `Decoder` objects which allow to customize the
      decoding. The structure should match the feature structure, but only
      customized feature keys need to be present. See [the
      guide](https://github.com/tensorflow/datasets/tree/master/docs/decode.md)
      for more info.
    read_config: `tfds.ReadConfig`, Additional options to configure the input
      pipeline (e.g. seed, num parallel reads,...).
    with_info: `bool`, if `True`, `tfds.load` will return the tuple
      (`tf.data.Dataset`, `tfds.core.DatasetInfo`), the latter containing the
      info associated with the builder.
    builder_kwargs: `dict` (optional), keyword arguments to be passed to the
      `tfds.core.DatasetBuilder` constructor. `data_dir` will be passed through
      by default.
    download_and_prepare_kwargs: `dict` (optional) keyword arguments passed to
      `tfds.core.DatasetBuilder.download_and_prepare` if `download=True`. Allow
      to control where to download and extract the cached data. If not set,
      cache_dir and manual_dir will automatically be deduced from data_dir.
    as_dataset_kwargs: `dict` (optional), keyword arguments passed to
      `tfds.core.DatasetBuilder.as_dataset`.
    try_gcs: `bool`, if True, tfds.load will see if the dataset exists on the
      public GCS bucket before building it locally.

  Returns:
    ds: `tf.data.Dataset`, the dataset requested, or if `split` is None, a
      `dict<key: tfds.Split, value: tf.data.Dataset>`. If `batch_size=-1`,
      these will be full datasets as `tf.Tensor`s.
    ds_info: `tfds.core.DatasetInfo`, if `with_info` is True, then `tfds.load`
      will return a tuple `(ds, ds_info)` containing dataset information
      (version, features, splits, num_examples,...). Note that the `ds_info`
      object documents the entire dataset, regardless of the `split` requested.
      Split-specific information is available in `ds_info.splits`.
  """
  # pylint: enable=line-too-long
  if builder_kwargs is None:
    builder_kwargs = {}

  dbuilder = builder(name, data_dir=data_dir, try_gcs=try_gcs, **builder_kwargs)
  if download:
    download_and_prepare_kwargs = download_and_prepare_kwargs or {}
    dbuilder.download_and_prepare(**download_and_prepare_kwargs)

  if as_dataset_kwargs is None:
    as_dataset_kwargs = {}
  as_dataset_kwargs = dict(as_dataset_kwargs)
  as_dataset_kwargs.setdefault('split', split)
  as_dataset_kwargs.setdefault('as_supervised', as_supervised)
  as_dataset_kwargs.setdefault('batch_size', batch_size)
  as_dataset_kwargs.setdefault('decoders', decoders)
  as_dataset_kwargs.setdefault('shuffle_files', shuffle_files)
  as_dataset_kwargs.setdefault('read_config', read_config)

  ds = dbuilder.as_dataset(**as_dataset_kwargs)
  if with_info:
    return ds, dbuilder.info
  return ds


def _get_all_versions(
    current_version: version.Version,
    extra_versions: Iterable[version.Version],
    current_version_only: bool,
) -> Iterable[str]:
  """Returns the list of all current versions."""
  # Merge current version with all extra versions
  version_list = [current_version]
  if not current_version_only:
    version_list.extend(extra_versions)
  # Filter datasets which do not have a version (version is `None`) as they
  # should not be instantiated directly (e.g wmt_translate)
  return {str(v) for v in version_list if v}


def _iter_single_full_names(
    builder_name: str,
    builder_cls: Type[dataset_builder.DatasetBuilder],  # pylint: disable=redefined-outer-name
    current_version_only: bool,
) -> Iterator[str]:
  """Iterate over a single builder full names."""
  if builder_cls.BUILDER_CONFIGS:
    for config in builder_cls.BUILDER_CONFIGS:
      for v in _get_all_versions(
          config.version or builder_cls.VERSION,
          config.supported_versions or builder_cls.SUPPORTED_VERSIONS,
          current_version_only=current_version_only,
      ):
        yield posixpath.join(builder_name, config.name, v)
  else:
    for v in _get_all_versions(
        builder_cls.VERSION,
        builder_cls.SUPPORTED_VERSIONS,
        current_version_only=current_version_only):
      yield posixpath.join(builder_name, v)


def _iter_full_names(current_version_only: bool) -> Iterator[str]:
  """Yield all registered datasets full_names (see `list_full_names`)."""
  for builder_name in registered.list_imported_builders():
    builder_cls_ = builder_cls(builder_name)
    for full_name in _iter_single_full_names(
        builder_name,
        builder_cls_,
        current_version_only=current_version_only,
    ):
      yield full_name


def list_full_names(current_version_only: bool = False) -> List[str]:
  """Lists all registered datasets full_names.

  Args:
    current_version_only: If True, only returns the current version.

  Returns:
    The list of all registered dataset full names.
  """
  return sorted(_iter_full_names(current_version_only=current_version_only))


def single_full_names(
    builder_name: str,
    current_version_only: bool = True,
) -> List[str]:
  """Returns the list `['ds/c0/v0',...]` or `['ds/v']` for a single builder."""
  return sorted(
      _iter_single_full_names(
          builder_name,
          builder_cls(builder_name),
          current_version_only=current_version_only,  # pytype: disable=wrong-arg-types
      ))


def is_full_name(full_name: str) -> bool:
  """Returns whether the string pattern match `ds/config/1.2.3` or `ds/1.2.3`.

  Args:
    full_name: String to check.

  Returns:
    `bool`.
  """
  return bool(_FULL_NAME_REG.match(full_name))


def _reraise_with_list_builders(
    e: Exception,
    name: naming.DatasetName,
) -> NoReturn:
  """Add the list of available builders to the DatasetNotFoundError."""
  # Should optimize to only filter through given namespace
  all_datasets = list_builders(with_community_datasets=bool(name.namespace))
  all_datasets_str = '\n\t- '.join([''] + all_datasets)
  error_string = f'Available datasets:{all_datasets_str}\n'
  error_string += textwrap.dedent("""
      Check that:
          - if dataset was added recently, it may only be available
            in `tfds-nightly`
          - the dataset name is spelled correctly
          - dataset class defines all base class abstract methods
          - the module defining the dataset class is imported
      """)

  # Add close matches
  close_matches = difflib.get_close_matches(str(name), all_datasets, n=1)
  if close_matches:
    error_string += f'\nDid you mean: {name} -> {close_matches[0]}\n'

  raise py_utils.reraise(e, suffix=error_string)
