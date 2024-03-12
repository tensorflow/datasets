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

"""Location-based register."""

from collections.abc import Mapping
import concurrent.futures
import difflib
import functools
import os
from typing import Any, FrozenSet, Iterable, Iterator, List, Type

from absl import flags
from absl import logging
from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.community import config as config_lib
from tensorflow_datasets.core.community import register_base
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

TFDS_DEBUG_VERBOSE = flags.DEFINE_boolean(
    'tfds_debug_list_dir', False, 'Debug the catalog generation'
)


class DataDirRegister(register_base.BaseRegister):
  """Dataset register based on generated `data_dir` paths.

  Usage:

  ```python
  register = DataDirRegister(namespace_to_data_dirs=
    {'my_namespace': [epath.Path('/path/to/namespaces.toml')]})

  # List all registered datasets: ['kaggle:ds0', 'kaggle:ds1',...]
  register.list_builders()

  # Load a specific dataset
  builder = register.builder('tensorflow_graphics:shapenet')
  ```
  """

  def __init__(self, namespaces: Mapping[str, config_lib.NamespaceConfig]):
    """Contructor.

    Args:
      namespaces: Mapping from namespace to namespace config.
    """
    self._namespace_configs = namespaces

  @property
  def namespace_configs(self) -> Mapping[str, config_lib.NamespaceConfig]:
    return self._namespace_configs

  @functools.cached_property
  def namespaces(self) -> FrozenSet[str]:
    """Available namespaces."""
    return frozenset(self._namespace_configs)

  def list_builders(self) -> List[str]:
    """Returns the list of registered builders."""
    return sorted(_iter_builder_names(self._namespace_configs))

  def list_dataset_references(self) -> Iterable[naming.DatasetReference]:
    exceptions = []
    for namespace, config in self._namespace_configs.items():
      for data_dir in config.paths:
        logging.info(
            'Listing datasets for namespace %s and data dir %s',
            namespace,
            data_dir,
        )
        try:
          found_datasets = list(
              file_utils.list_datasets_in_data_dir(
                  data_dir=data_dir,
                  namespace=namespace,
                  include_configs=False,
                  include_versions=False,
              )
          )
          logging.info(
              'Found %d dataset variants in namespace %s and data dir %s',
              len(found_datasets),
              namespace,
              data_dir,
          )
          yield from found_datasets
        except Exception as e:  # pylint: disable=broad-exception-caught
          exceptions.append(e)
          logging.exception(
              'Could not get datasets for namespace %s and data dir %s',
              namespace,
              data_dir,
          )
    if exceptions:
      # TODO(b/299874845): py3.11 - raise an ExceptionGroup
      # https://realpython.com/python311-exception-groups/#group-exceptions-with-exceptiongroup
      raise exceptions[0]

  def builder_cls(
      self,
      name: naming.DatasetName,
  ) -> Type[dataset_builder.DatasetBuilder]:
    """Returns the builder classes."""
    if name.namespace not in self.namespaces:  # pylint: disable=unsupported-membership-test
      error_msg = f'\nNamespace {name.namespace} not found.'
      error_msg += (
          f'Note that namespace should be one of: {sorted(self.namespaces)}'
      )
      raise registered.DatasetNotFoundError(error_msg)
    raise NotImplementedError(
        'builder_cls does not support data_dir-based community datasets. Got: '
        f'{name}'
    )

  def builder(
      self,
      name: naming.DatasetName,
      **builder_kwargs: Any,
  ) -> dataset_builder.DatasetBuilder:
    """Returns the dataset builder."""
    data_dir = builder_kwargs.pop('data_dir', None)
    if data_dir:
      raise ValueError(
          '`data_dir` cannot be set for data_dir-based community datasets. '
          f'Dataset should already be generated. Got: {data_dir}'
      )
    if name.namespace is None:
      raise AssertionError(f'No namespace found: {name}')
    if name.namespace not in self._namespace_configs:
      close_matches = difflib.get_close_matches(
          name.namespace, self._namespace_configs, n=1
      )
      hint = f'\nDid you mean: {close_matches[0]}' if close_matches else ''
      error_msg = (
          f'Namespace `{name.namespace}` for `{name}` not found. '
          f'Should be one of {sorted(self._namespace_configs)}{hint}'
      )
      raise KeyError(error_msg)
    return read_only_builder.builder_from_files(
        name.name,
        data_dir=[
            os.fspath(path)
            for path in self._namespace_configs[name.namespace].paths
        ],
        **builder_kwargs,
    )

  def get_builder_root_dirs(self, name: naming.DatasetName) -> List[epath.Path]:
    """Returns root dir of the generated builder (without version/config)."""
    if name.namespace is None:
      raise ValueError(f'No namespace defined: {name}')
    return [
        d / name.name for d in self._namespace_configs[name.namespace].paths
    ]


def _maybe_iterdir(path: epath.Path) -> Iterator[epath.Path]:
  """Same as `path.iterdir()`, but don't fail if path does not exist."""
  # Use try/except rather than `.exists()` to avoid an extra RPC call
  # per namespace
  try:
    for f in path.iterdir():
      yield f
  except (
      OSError,
      FileNotFoundError,
      PermissionError,
      tf.errors.NotFoundError,
      tf.errors.PermissionDeniedError,
  ):
    pass


def _iter_builder_names(
    namespaces: Mapping[str, config_lib.NamespaceConfig],
) -> Iterator[str]:
  """Yields the `ns:name` dataset names."""
  FILTERED_DIRNAME = frozenset(('downloads',))  # pylint: disable=invalid-name

  def _is_valid_dataset_name(dataset_name: str) -> bool:
    return (
        dataset_name not in FILTERED_DIRNAME
        and naming.is_valid_dataset_name(dataset_name)
    )

  # For better performance, load all namespaces asynchronously
  def _get_builder_names_single_namespace(
      ns_name: str,
      data_dir: epath.Path,
  ) -> List[str]:
    # Note: `data_dir` might contain non-dataset folders, but checking
    # individual dataset would have significant performance drop, so
    # this is an acceptable trade-of.
    return [
        str(naming.DatasetName(namespace=ns_name, name=builder_dir.name))
        for builder_dir in _maybe_iterdir(data_dir)
        if _is_valid_dataset_name(builder_dir.name)
    ]

  with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    builder_names_futures = []
    for ns_name, ns_config in namespaces.items():
      for data_dir in ns_config.paths:
        future = ex.submit(
            _get_builder_names_single_namespace,
            ns_name,
            data_dir,
        )
        builder_names_futures.append(future)

    for future in concurrent.futures.as_completed(builder_names_futures):
      yield from future.result()
