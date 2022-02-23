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

"""Location-based register."""

import concurrent.futures
import difflib
from typing import Any, Dict, FrozenSet, Iterator, List, Type

from absl import flags
from absl import logging

from etils import epath
import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import read_only_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import register_base
import toml

TFDS_DEBUG_VERBOSE = flags.DEFINE_boolean('tfds_debug_list_dir', False,
                                          'Debug the catalog generation')

ListOrElem = utils.ListOrElem

# pylint: disable=logging-fstring-interpolation


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

  def __init__(self, path: epath.PathLike):
    """Contructor.

    Args:
      path: Path to the register files containing the mapping namespace ->
        data_dir
    """
    self._path: epath.Path = epath.Path(path)

  @utils.memoized_property
  def _ns2data_dir(self) -> Dict[str, List[epath.Path]]:
    """Mapping `namespace` -> `data_dir`."""
    # Lazy-load the namespaces the first requested time.
    config = toml.loads(self._path.read_text())
    return {
        namespace: _as_path_list(path_or_paths)
        for namespace, path_or_paths in config['Namespaces'].items()
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

  def get_builder_root_dirs(self, name: utils.DatasetName) -> List[epath.Path]:
    """Returns root dir of the generated builder (without version/config)."""
    return [d / name.name for d in self._ns2data_dir[name.namespace]]


def _as_path_list(path_or_paths: ListOrElem[str]) -> List[epath.Path]:
  if isinstance(path_or_paths, list):
    return [epath.Path(p) for p in path_or_paths]
  else:
    return [epath.Path(path_or_paths)]


def _maybe_iterdir(path: epath.Path) -> Iterator[epath.Path]:
  """Same as `path.iterdir()`, but don't fail if path does not exist."""
  # Use try/except rather than `.exists()` to avoid an extra RPC call
  # per namespace
  try:
    for f in path.iterdir():
      yield f
  except (
      FileNotFoundError,
      tf.errors.NotFoundError,
      tf.errors.PermissionDeniedError,
  ) as e:
    pass


def _iter_builder_names(
    ns2data_dir: Dict[str, List[epath.Path]],) -> Iterator[str]:
  """Yields the `ns:name` dataset names."""
  FILTERED_DIRNAME = frozenset(('downloads',))  # pylint: disable=invalid-name

  def _is_valid_dataset_name(dataset_name: str) -> bool:
    return (dataset_name not in FILTERED_DIRNAME and
            naming.is_valid_dataset_name(dataset_name))

  # For better performances, load all namespaces asynchonously
  def _get_builder_names_single_namespace(
      ns_name: str,
      data_dir: epath.Path,
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
    builder_names_futures = []
    for ns_name, data_dirs in ns2data_dir.items():
      for data_dir in data_dirs:
        future = ex.submit(
            _get_builder_names_single_namespace,
            ns_name,
            data_dir,
        )
        builder_names_futures.append(future)

    for future in concurrent.futures.as_completed(builder_names_futures):
      yield from future.result()
