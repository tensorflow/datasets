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

"""Location-based register."""

import concurrent.futures
import difflib
from typing import Any, Dict, FrozenSet, Iterator, List, Type

import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import register_base
import toml


class DataDirRegister(register_base.BaseRegister):
  """Dataset register based on generated `data_dir` paths.

  This register map `namespace` strings to `data_dir` paths. Mapping is defined
  in `.toml` format:

  ```toml
  [Namespaces]
  kaggle='/path/to/datasets/'
  tensorflow_graphics='gs://tensorflow-graphics/datasets'
  ```

  Usage:

  ```python
  register = DataDirRegister(path='/path/to/namespaces.toml')

  # List all registered datasets: ['kaggle:ds0', 'kaggle:ds1',...]
  register.list_builders()

  # Load a specific dataset
  builder = register.builder('tensorflow_graphics:shapenet')
  ```

  """

  def __init__(self, path: utils.PathLike):
    """Contructor.

    Args:
      path: Path to the register files containing the mapping namespace ->
        data_dir
    """
    self._path: utils.ReadOnlyPath = utils.as_path(path)

  @utils.memoized_property
  def _ns2data_dir(self) -> Dict[str, utils.ReadWritePath]:
    """Mapping `namespace` -> `data_dir`."""
    # Lazy-load the namespaces the first requested time.
    config = toml.loads(self._path.read_text())
    return {
        namespace: utils.as_path(path)
        for namespace, path in config['Namespaces'].items()
    }

  @utils.memoized_property
  def namespaces(self) -> FrozenSet[str]:
    """Available namespaces."""
    return frozenset(self._ns2data_dir)

  def list_builders(self) -> List[str]:
    """Returns the list of registered builders."""
    return sorted(_iter_builder_names(self._ns2data_dir))

  def builder_cls(
      self,
      name: utils.DatasetName,
  ) -> Type[dataset_builder.DatasetBuilder]:
    """Returns the builder classes."""
    if name.namespace not in self.namespaces:  # pylint: disable=unsupported-membership-test
      raise registered.DatasetNotFoundError(
          f'Namespace {name.namespace} not found. Should be one of: '
          f'{sorted(self.namespaces)}')
    raise NotImplementedError(
        'builder_cls does not support data_dir-based community datasets. Got: '
        f'{name}')

  def builder(
      self,
      name: utils.DatasetName,
      **builder_kwargs: Any,
  ) -> dataset_builder.DatasetBuilder:
    """Returns the dataset builder."""
    data_dir = builder_kwargs.pop('data_dir', None)
    if data_dir:
      raise ValueError(
          '`data_dir` cannot be set for data_dir-based community datasets. '
          f'Dataset should already be generated. Got: {data_dir}')
    if name.namespace is None:
      raise AssertionError(f'No namespace found: {name}')
    if name.namespace not in self._ns2data_dir:  # pylint: disable=unsupported-membership-test
      close_matches = difflib.get_close_matches(
          name.namespace, self._ns2data_dir, n=1)
      hint = f'\nDid you mean: {close_matches[0]}' if close_matches else ''
      raise KeyError(f'Namespace `{name.namespace}` for `{name}` not found. '
                     f'Should be one of {sorted(self._ns2data_dir)}{hint}')
    return read_only_builder.builder_from_files(
        name.name,
        data_dir=self._ns2data_dir[name.namespace],
        **builder_kwargs,
    )

  def get_builder_root_dir(self,
                           name: utils.DatasetName) -> utils.ReadWritePath:
    """Returns root dir of the generated builder (without version/config)."""
    return self._ns2data_dir[name.namespace] / name.name


def _maybe_iterdir(path: utils.ReadOnlyPath) -> Iterator[utils.ReadOnlyPath]:
  """Same as `path.iterdir()`, but don't fail if path does not exists."""
  # Use try/except rather than `.exists()` to avoid an extra RPC call
  # per namespace
  try:
    for f in path.iterdir():
      yield f
  except (
      FileNotFoundError,
      tf.errors.NotFoundError,
      tf.errors.PermissionDeniedError,
  ):
    pass


def _iter_builder_names(
    ns2data_dir: Dict[str, utils.ReadOnlyPath],) -> Iterator[str]:
  """Yields the `ns:name` dataset names."""
  FILTERED_DIRNAME = frozenset(('downloads',))  # pylint: disable=invalid-name

  def _is_valid_dataset_name(dataset_name: str) -> bool:
    return (dataset_name not in FILTERED_DIRNAME and
            naming.is_valid_dataset_name(dataset_name))

  # For better performances, load all namespaces asynchonously
  def _get_builder_names_single_namespace(
      ns_name: str,
      data_dir: utils.ReadOnlyPath,
  ) -> List[str]:
    # Note: `data_dir` might contain non-dataset folders, but checking
    # individual dataset would have significant performance drop, so
    # this is an acceptable trade-of.
    return [
        str(utils.DatasetName(namespace=ns_name, name=builder_dir.name))
        for builder_dir in _maybe_iterdir(data_dir)
        if _is_valid_dataset_name(builder_dir.name)
    ]

  with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex:
    builder_names_futures = [
        ex.submit(_get_builder_names_single_namespace, ns_name, data_dir)
        for ns_name, data_dir in ns2data_dir.items()
    ]
    for future in concurrent.futures.as_completed(builder_names_futures):
      yield from future.result()
