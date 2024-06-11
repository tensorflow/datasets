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

"""Access registered datasets."""

from __future__ import annotations

from collections.abc import Sequence
import dataclasses
import difflib
import json
import os
import posixpath
import re
import textwrap
import typing
from typing import Any, Callable, Dict, Iterable, Iterator, List, Mapping, Optional, Type, Union

from absl import logging
from tensorflow_datasets.core import community
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_collection_builder
from tensorflow_datasets.core import decode
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import logging as tfds_logging
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core import visibility
from tensorflow_datasets.core.dataset_builders import huggingface_dataset_builder  # pylint:disable=unused-import
from tensorflow_datasets.core.download import util
from tensorflow_datasets.core.utils import error_utils
from tensorflow_datasets.core.utils import gcs_utils
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils import version
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

# pylint: disable=logging-format-interpolation

Tree = type_utils.Tree
TreeDict = type_utils.TreeDict

PredicateFn = Callable[[Type[dataset_builder.DatasetBuilder]], bool]


# Regex matching 'dataset/config/1.3.0'
_FULL_NAME_REG = re.compile(
    r'^{ds_name}/({config_name}/)?{version}$'.format(
        ds_name=r'\w+',
        config_name=r'[\w\-\.]+',
        version=r'[0-9]+\.[0-9]+\.[0-9]+',
    )
)


@tfds_logging.list_builders()
def list_builders(
    *,
    with_community_datasets: bool = True,
) -> List[str]:
  """Returns the string names of all `tfds.core.DatasetBuilder`s."""
  datasets = registered.list_imported_builders()
  if with_community_datasets:
    if visibility.DatasetType.COMMUNITY_PUBLIC.is_available():
      datasets += community.community_register().list_builders()
  return datasets


def list_dataset_collections() -> List[str]:
  """Returns the string names of all `tfds.core.DatasetCollectionBuilder`s."""
  collections = registered.list_imported_dataset_collections()
  return collections


@error_utils.reraise_with_context(registered.DatasetNotFoundError)
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
        f"version or arguments. Got: name='{name}', kwargs={kwargs}"
    )

  if ds_name.namespace:
    # `namespace:dataset` are loaded from the community register
    if visibility.DatasetType.COMMUNITY_PUBLIC.is_available():
      return community.community_register().builder_cls(ds_name)
    else:
      raise ValueError(
          f'Cannot load {ds_name} when community datasets are disabled'
      )
  else:
    try:
      cls = registered.imported_builder_cls(str(ds_name))
      cls = typing.cast(Type[dataset_builder.DatasetBuilder], cls)
      return cls
    except registered.DatasetNotFoundError:
      _add_list_builders_context(name=ds_name)  # pytype: disable=bad-return-type
      raise


@error_utils.reraise_with_context(registered.DatasetNotFoundError)
@tfds_logging.builder()
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
    try_gcs: `bool`, if True, `tfds.load` will see if the dataset exists on the
      public GCS bucket before building it locally. This is equivalent to
      passing `data_dir='gs://tfds-data/datasets'`. Warning: `try_gcs` is
      different than `builder_kwargs.download_config.try_download_gcs`.
      `try_gcs` (default: False) overrides `data_dir` to be the public GCS
      bucket. `try_download_gcs` (default: True) allows downloading from GCS
      while keeping a different `data_dir` than the public GCS bucket.  So, to
      fully bypass GCS, please use `try_gcs=False` and
      `download_and_prepare_kwargs={'download_config':
      tfds.core.download.DownloadConfig(try_download_gcs=False)})`.
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
      name, **builder_kwargs
  )

  def get_dataset_repr() -> str:
    return f'dataset "{name}", builder_kwargs "{builder_kwargs}"'

  # `try_gcs` currently only supports non-community datasets
  if try_gcs and not name.namespace and gcs_utils.is_dataset_on_gcs(str(name)):
    data_dir = builder_kwargs.get('data_dir')
    if data_dir:
      raise ValueError(
          f'Cannot have both `try_gcs=True` and `data_dir={data_dir}`'
          f' explicitly set. Wrong arguments for {get_dataset_repr()}'
      )
    builder_kwargs['data_dir'] = gcs_utils.gcs_path('datasets')
  if name.namespace:
    if name.namespace == 'huggingface':
      return huggingface_dataset_builder.builder(
          name=name.name, **builder_kwargs)
    if (
        visibility.DatasetType.COMMUNITY_PUBLIC.is_available()
        and community.community_register().has_namespace(name.namespace)
    ):
      return community.community_register().builder(name=name, **builder_kwargs)

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
    except registered.DatasetNotFoundError as e:
      logging.info(
          'Failed to load %s from files: %s', get_dataset_repr(), str(e)
      )

  # If code exists and loading from files was skipped (e.g. files not found),
  # load from the source code.
  if cls:
    with py_utils.try_reraise(
        prefix=f'Failed to construct {get_dataset_repr()}: '
    ):
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
  elif (
      'config' in builder_kwargs
      and isinstance(builder_kwargs['config'], str)
      and builder_kwargs['config'] not in cls.builder_configs
  ):
    return True  # Requested config isn't found in the code
  else:
    return False  # Code exists and no version is given, so use code.


@dataclasses.dataclass()
class DatasetCollectionLoader:
  """Loader class for dataset collections.

  Attributes:
    collection: the DatasetCollection to load.
    requested_version: optional version of the dataset collection to load. If
      none given, the latest version will be loaded.
    loader_kwargs: optional kwargs for the `tfds.load` function.
    datasets: initialized post-init, defines the datasets comprised in the
      requested dataset collection.
    collection_name: the name of the DatasetCollection to load.
  """

  collection: dataset_collection_builder.DatasetCollection
  requested_version: Optional[str] = None
  loader_kwargs: Optional[Dict[str, Any]] = None

  def __post_init__(self):
    self.datasets = self.collection.get_collection(self.requested_version)

  @property
  def collection_name(self) -> str:
    return self.collection.info.name

  def print_info(self) -> None:
    """Prints information about this dataset collection."""
    msg = [
        f'Dataset collection: {self.collection.info.name}',
        f'Version: {self.requested_version}',
        f'Description: {self.collection.info.description}',
    ]
    if self.collection.info.citation:
      msg.append('Citation:')
      msg.append(self.collection.info.citation)
    print('\n'.join(msg))

  def print_datasets(self) -> None:
    print(self.collection.list_datasets(version=self.requested_version))

  def get_dataset_info(self, dataset_name: str):
    # TODO(b/235343719) improve performance, e.g. by creating a method such as
    # # load_info that does this more efficiently.
    dataset_reference = self.datasets[dataset_name]
    _, info = load(
        dataset_reference.tfds_name(),
        with_info=True,
        data_dir=dataset_reference.data_dir,
    )
    return info

  def set_loader_kwargs(self, loader_kwargs: Dict[str, Any]):
    self.loader_kwargs = loader_kwargs

  def load_dataset(
      self,
      dataset: str,
      split: Optional[Tree[splits_lib.SplitArg]] = None,
      loader_kwargs: Optional[Dict[str, Any]] = None,
  ) -> Mapping[str, tf.data.Dataset]:
    """Loads the named dataset from a dataset collection by calling `tfds.load`.

    Args:
      dataset: `str`, the dataset name to load.
      split: which split(s) of the dataset to load. If `None`, will return all
        splits available for the dataset.
      loader_kwargs: `dict` (optional), keyword arguments to be passed to the
        `tfds.load` function. Refer to `tfds.load` documentation for a
        comperehensive overview of the different loading options.

    Returns:
      A `dict` of {`str`: tf.data.Dataset} for the desided dataset.

    Raises:
      KeyError: if trying to load a dataset not included in the collection.
      RuntimeError: if `load` return type is not a `dict` or a `list`.
    """
    if not dataset:
      raise TypeError('You must specify a non-empty dataset to load.')

    loader_kwargs = loader_kwargs or self.loader_kwargs or {}

    # with_info must be False (or it will change the return type of `tfds.load`)
    if 'with_info' in loader_kwargs and loader_kwargs['with_info']:
      logging.warning('`with_info` cannot be True, setting it to False')
    loader_kwargs['with_info'] = False

    try:
      dataset_reference = self.datasets[dataset]
    except KeyError as e:
      raise KeyError(
          f'Dataset {dataset} is not included in this collection. '
          f'{self.collection.list_datasets(version=self.requested_version)}'
      ) from e

    # If `split` is defined both as argument and in `loader_kwargs`, always keep
    # the one defined as argument.
    if split:
      loader_kwargs['split'] = dataset_reference.get_split(split)
    # Make sure we always return a dict of dicts.
    if 'split' in loader_kwargs and isinstance(loader_kwargs['split'], str):
      loader_kwargs['split'] = [loader_kwargs['split']]

    # Add the data dir from the reference to loader_kwargs if it is defined and
    # not overridden in loader_kwargs.
    if (
        dataset_reference.data_dir is not None
        and 'data_dir' not in loader_kwargs
    ):
      loader_kwargs['data_dir'] = dataset_reference.data_dir

    load_output = load(dataset_reference.tfds_name(), **loader_kwargs)
    loaded_datasets = {}
    # If `split` is not specified, then `load` returns a dict with the split as
    # the key.
    if isinstance(load_output, dict):
      loaded_datasets = load_output
    # If `split` is a list, then the return type of `load` is a list of datasets
    # in the same order of the splits.
    elif isinstance(load_output, list):
      for split_name, d in zip(loader_kwargs['split'], load_output):
        assert isinstance(split_name, str)
        if isinstance(d, tuple):
          ds, _ = d
          loaded_datasets[split_name] = ds
        elif isinstance(d, tf.data.Dataset):
          loaded_datasets[split_name] = d
        else:
          raise RuntimeError(
              f'Unsupported return type {type(load_output)} of `load` function.'
          )
    else:
      raise RuntimeError(
          f'Unsupported return type {type(load_output)} of `load` function.'
      )
    return loaded_datasets

  def load_datasets(
      self,
      datasets: Iterable[str],
      split: Optional[Tree[splits_lib.SplitArg]] = None,
      loader_kwargs: Optional[Dict[str, Any]] = None,
  ) -> Mapping[str, Mapping[str, tf.data.Dataset]]:
    """Loads a number of datasets from the dataset collection.

    Args:
      datasets: dataset names to load.
      split: which split(s) of the datasets to load.
      loader_kwargs: keyword arguments to be passed to the `tfds.load` function.
        Refer to `tfds.load` documentation for a comperehensive overview of the
        different loading options.

    Returns:
      mapping between a dataset name and a mapping of split name to
      tf.data.Dataset for each requested dataset.

    Raises:
      ValueError: if no dataset(s) to load are given.
    """
    if not datasets:
      raise ValueError('At least one dataset should be specified.')
    return {
        dataset_name: self.load_dataset(
            dataset_name, split=split, loader_kwargs=loader_kwargs
        )
        for dataset_name in datasets
    }

  def load_all_datasets(
      self,
      split: Optional[Tree[splits_lib.SplitArg]] = None,
      loader_kwargs: Optional[Dict[str, Any]] = None,
  ) -> Mapping[str, Mapping[str, tf.data.Dataset]]:
    """Loads all datasets of a collection.

    Args:
      split: which split(s) of the datasets to load.
      loader_kwargs: `dict` (optional), keyword arguments to be passed to the
        `tfds.load` function. Refer to `tfds.load` documentation for a
        comperehensive overview of the different loading options.

    Returns:
      `dict` of `dataset_names` mapping to a `dict` of {`split_name`:
      tf.data.Dataset} for each desired datasets.
    """
    return self.load_datasets(
        datasets=self.datasets.keys(), split=split, loader_kwargs=loader_kwargs
    )


@tfds_logging.dataset_collection()
def dataset_collection(
    name: str,
    loader_kwargs: Optional[Dict[str, Any]] = None,
) -> DatasetCollectionLoader:
  """Instantiates a DatasetCollectionLoader.

  Args:
    name: The name of the dataset collection to load.
    loader_kwargs: `dict` (optional), keyword arguments to be passed to the
      `tfds.load` function. Refer to `tfds.load` documentation for a
      comperehensive overview of the different loading options.

  Returns:
    A DatasetCollectionLoader object.

  Raises:
    DatasetCollectionNotFoundError if dataset collection not found in registry.
  """
  parsed_name, builder_kwargs = naming.parse_builder_name_kwargs(name)
  if not registered.is_dataset_collection(parsed_name.name):
    available_collections = registered.list_imported_dataset_collections()
    raise registered.DatasetCollectionNotFoundError(
        f'Dataset collection {name} not found. '
        f'Available dataset collections: {available_collections}'
    )

  dataset_collection_cls = registered.imported_dataset_collection_cls(
      parsed_name.name
  )
  dataset_collection_cls = typing.cast(
      Type[dataset_collection_builder.DatasetCollection], dataset_collection_cls
  )
  collection = dataset_collection_cls()

  requested_version = None
  if 'version' in builder_kwargs:
    requested_version = builder_kwargs['version']

  return DatasetCollectionLoader(
      collection,
      requested_version=requested_version,
      loader_kwargs=loader_kwargs,
  )




def _fetch_builder(
    name: str,
    data_dir: Union[None, str, os.PathLike],  # pylint: disable=g-bare-generic
    builder_kwargs: Optional[Dict[str, Any]],
    try_gcs: bool,
) -> dataset_builder.DatasetBuilder:
  """Fetches the `tfds.core.DatasetBuilder` by name."""
  if builder_kwargs is None:
    builder_kwargs = {}
  return builder(name, data_dir=data_dir, try_gcs=try_gcs, **builder_kwargs)


def _download_and_prepare_builder(
    dbuilder: dataset_builder.DatasetBuilder,
    download: bool,
    download_and_prepare_kwargs: Optional[Dict[str, Any]],
) -> None:
  """Downloads and prepares the dataset builder if necessary."""
  if dbuilder.is_prepared():
    if not download_and_prepare_kwargs:
      return
    if download_config := download_and_prepare_kwargs.get('download_config'):
      if (
          download_config.download_mode
          == util.GenerateMode.REUSE_DATASET_IF_EXISTS
      ):
        return
  if download:
    download_and_prepare_kwargs = download_and_prepare_kwargs or {}
    dbuilder.download_and_prepare(**download_and_prepare_kwargs)


@tfds_logging.load()
def load(
    name: str,
    *,
    split: Optional[Tree[splits_lib.SplitArg]] = None,
    data_dir: Union[None, str, os.PathLike] = None,  # pylint: disable=g-bare-generic
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
    data_dir: directory to read/write data. Defaults to the value of the
      environment variable TFDS_DATA_DIR, if set, otherwise falls back to
      '~/tensorflow_datasets'.
    batch_size: `int`, if set, add a batch dimension to examples. Note that
      variable length features will be 0-padded. If `batch_size=-1`, will return
      the full dataset as `tf.Tensor`s.
    shuffle_files: `bool`, whether to shuffle the input files. Defaults to
      `False`.
    download: `bool` (optional), whether to call
      `tfds.core.DatasetBuilder.download_and_prepare` before calling
      `tfds.core.DatasetBuilder.as_dataset`. If `False`, data is expected to be
      in `data_dir`. If `True` and the data is already in `data_dir`,
      `download_and_prepare` is a no-op.
    as_supervised: `bool`, if `True`, the returned `tf.data.Dataset` will have a
      2-tuple structure `(input, label)` according to
      `builder.info.supervised_keys`. If `False`, the default, the returned
      `tf.data.Dataset` will have a dictionary with all the features.
    decoders: Nested dict of `Decoder` objects which allow to customize the
      decoding. The structure should match the feature structure, but only
      customized feature keys need to be present. See [the
      guide](https://github.com/tensorflow/datasets/blob/master/docs/decode.md)
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
    try_gcs: `bool`, if True, `tfds.load` will see if the dataset exists on the
      public GCS bucket before building it locally. This is equivalent to
      passing `data_dir='gs://tfds-data/datasets'`. Warning: `try_gcs` is
      different than `builder_kwargs.download_config.try_download_gcs`.
      `try_gcs` (default: False) overrides `data_dir` to be the public GCS
      bucket. `try_download_gcs` (default: True) allows downloading from GCS
      while keeping a different `data_dir` than the public GCS bucket.  So, to
      fully bypass GCS, please use `try_gcs=False` and
      `download_and_prepare_kwargs={'download_config':
      tfds.core.download.DownloadConfig(try_download_gcs=False)})`.

  Returns:
    ds: `tf.data.Dataset`, the dataset requested, or if `split` is None, a
      `dict<key: tfds.Split, value: tf.data.Dataset>`. If `batch_size=-1`,
      these will be full datasets as `tf.Tensor`s.
    ds_info: `tfds.core.DatasetInfo`, if `with_info` is True, then `tfds.load`
      will return a tuple `(ds, ds_info)` containing dataset information
      (version, features, splits, num_examples,...). Note that the `ds_info`
      object documents the entire dataset, regardless of the `split` requested.
      Split-specific information is available in `ds_info.splits`.
  """  # fmt: skip
  dbuilder = _fetch_builder(
      name,
      data_dir,
      builder_kwargs,
      try_gcs,
  )
  _download_and_prepare_builder(dbuilder, download, download_and_prepare_kwargs)

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


def _set_file_format_for_data_source(
    builder_kwargs: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
  """Normalizes file format in builder_kwargs for `tfds.data_source`."""
  if builder_kwargs is None:
    builder_kwargs = {}
  file_format = builder_kwargs.get(
      'file_format', file_adapters.FileFormat.ARRAY_RECORD
  )
  file_format = file_adapters.FileFormat.from_value(file_format)
  if file_format != file_adapters.FileFormat.ARRAY_RECORD:
    raise NotImplementedError(
        f'No random access data source for file format {file_format}. Please,'
        ' use `tfds.data_source(...,'
        ' builder_kwargs={"file_format":'
        f' {file_adapters.FileFormat.ARRAY_RECORD}}})` instead.'
    )
  builder_kwargs['file_format'] = file_format
  return builder_kwargs


@tfds_logging.data_source()
def data_source(
    name: str,
    *,
    split: Optional[Tree[splits_lib.SplitArg]] = None,
    data_dir: Union[None, str, os.PathLike] = None,  # pylint: disable=g-bare-generic
    download: bool = True,
    decoders: Optional[TreeDict[decode.partial_decode.DecoderArg]] = None,
    builder_kwargs: Optional[Dict[str, Any]] = None,
    download_and_prepare_kwargs: Optional[Dict[str, Any]] = None,
    try_gcs: bool = False,
) -> type_utils.ListOrTreeOrElem[Sequence[Any]]:
  """Gets a data source from the named dataset.

  `tfds.data_source` is a convenience method that:

  1. Fetches the `tfds.core.DatasetBuilder` by name:

     ```python
     builder = tfds.builder(name, data_dir=data_dir, **builder_kwargs)
     ```

  2. Generates the data (when `download=True`):

     ```python
     builder.download_and_prepare(**download_and_prepare_kwargs)
     ```

  3. Gets the data source:

     ```python
     ds = builder.as_data_source(split=split)
     ```

  You can consume data sources:

  - In Python by iterating over them:

  ```python
  for example in ds['train']:
    print(example)
  ```

  - With a DataLoader (e.g., with
  [Pytorch](https://pytorch.org/docs/stable/data.html)).

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
      all splits in a `Dict[Split, Sequence]`
    data_dir: directory to read/write data. Defaults to the value of the
      environment variable TFDS_DATA_DIR, if set, otherwise falls back to
      '~/tensorflow_datasets'.
    download: `bool` (optional), whether to call
      `tfds.core.DatasetBuilder.download_and_prepare` before calling
      `tfds.core.DatasetBuilder.as_data_source`. If `False`, data is expected to
      be in `data_dir`. If `True` and the data is already in `data_dir`,
      `download_and_prepare` is a no-op.
    decoders: Nested dict of `Decoder` objects which allow to customize the
      decoding. The structure should match the feature structure, but only
      customized feature keys need to be present. See [the
      guide](https://github.com/tensorflow/datasets/blob/master/docs/decode.md)
      for more info.
    builder_kwargs: `dict` (optional), keyword arguments to be passed to the
      `tfds.core.DatasetBuilder` constructor. `data_dir` will be passed through
      by default.
    download_and_prepare_kwargs: `dict` (optional) keyword arguments passed to
      `tfds.core.DatasetBuilder.download_and_prepare` if `download=True`. Allow
      to control where to download and extract the cached data. If not set,
      cache_dir and manual_dir will automatically be deduced from data_dir.
    try_gcs: `bool`, if True, `tfds.load` will see if the dataset exists on the
      public GCS bucket before building it locally. This is equivalent to
      passing `data_dir='gs://tfds-data/datasets'`. Warning: `try_gcs` is
      different than `builder_kwargs.download_config.try_download_gcs`.
      `try_gcs` (default: False) overrides `data_dir` to be the public GCS
      bucket. `try_download_gcs` (default: True) allows downloading from GCS
      while keeping a different `data_dir` than the public GCS bucket.  So, to
      fully bypass GCS, please use `try_gcs=False` and
      `download_and_prepare_kwargs={'download_config':
      tfds.core.download.DownloadConfig(try_download_gcs=False)})`.

  Returns:
    `Sequence` if `split`,
    `dict<key: tfds.Split, value: Sequence>` otherwise.
  """  # fmt:skip
  builder_kwargs = _set_file_format_for_data_source(builder_kwargs)
  dbuilder = _fetch_builder(
      name,
      data_dir,
      builder_kwargs,
      try_gcs,
  )
  _download_and_prepare_builder(dbuilder, download, download_and_prepare_kwargs)
  return dbuilder.as_data_source(split=split, decoders=decoders)


def _get_all_versions(
    current_version: version.Version | None,
    extra_versions: Iterable[version.Version],
    current_version_only: bool,
) -> Iterable[str]:
  """Returns the list of all current versions."""
  # Merge current version with all extra versions
  version_list = [current_version] if current_version else []
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
        current_version_only=current_version_only,
    ):
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
      )
  )


def is_full_name(full_name: str) -> bool:
  """Returns whether the string pattern match `ds/config/1.2.3` or `ds/1.2.3`.

  Args:
    full_name: String to check.

  Returns:
    `bool`.
  """
  return bool(_FULL_NAME_REG.match(full_name))


def _add_list_builders_context(
    name: naming.DatasetName,
) -> None:
  """Adds the list of available builders to the DatasetNotFoundError."""
  # Should optimize to only filter through given namespace
  all_datasets = list_builders(with_community_datasets=False)
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
    error_string += f'\nDid you mean: {name} -> {close_matches[0]} ?\n'

  error_utils.add_context(error_string)
