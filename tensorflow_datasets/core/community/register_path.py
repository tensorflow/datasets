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

"""Location-based register."""

import difflib
from typing import Any, Dict, Iterator, List, Optional, Type

import tensorflow as tf
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import read_only_builder
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
      path: Path to the register files containing the mapping
        namespace -> data_dir
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

  def list_builders(self) -> List[str]:
    """Returns the list of registered builders."""
    return sorted(_iter_builder_names(self._ns2data_dir))

  def builder_cls(
      self, ns_name: Optional[str], builder_name: str, **builder_kwargs: Any,
  ) -> Type[dataset_builder.DatasetBuilder]:
    """Returns the builder classes."""
    raise NotImplementedError(
        'builder_cls does not support data_dir-based community datasets. Got: '
        f'{ns_name}:{builder_name}'
    )

  def builder(
      self, ns_name: Optional[str], builder_name: str, **builder_kwargs: Any,
  ) -> dataset_builder.DatasetBuilder:
    """Returns the dataset builder."""
    if 'data_dir' in builder_kwargs:
      raise ValueError(
          '`data_dir` cannot be set for data_dir-based community datasets. '
          'Dataset should already be generated.'
      )
    if ns_name is None:
      raise AssertionError(f'No namespace found: {builder_name}')
    if ns_name not in self._ns2data_dir:
      close_matches = difflib.get_close_matches(ns_name, self._ns2data_dir, n=1)
      hint = f'\nDid you meant: {close_matches[0]}' if close_matches else ''
      raise KeyError(
          f'Namespace `{ns_name}` for `{builder_name}` not found. '
          f'Should be one of {sorted(self._ns2data_dir)}{hint}'
      )
    return read_only_builder.builder_from_files(
        builder_name,
        data_dir=self._ns2data_dir[ns_name],
        **builder_kwargs,
    )


def _maybe_iterdir(path: utils.ReadOnlyPath) -> Iterator[utils.ReadOnlyPath]:
  """Same as `path.iterdir()`, but don't fail if path does not exists."""
  # Use try/except rather than `.exists()` to avoid an extra RPC call
  # per namespace
  try:
    for f in path.iterdir():
      yield f
  except (FileNotFoundError, tf.errors.NotFoundError):
    pass


def _iter_builder_names(
    ns2data_dir: Dict[str, utils.ReadOnlyPath],
) -> Iterator[str]:
  """Yields the `ns:name` dataset names."""
  FILTERED_DIRNAME = frozenset(('downloads',))  # pylint: disable=invalid-name
  # For better performances, could try to load all namespaces asynchonously
  for ns_name, data_dir in ns2data_dir.items():
    # Note: `data_dir` might contain non-dataset folders, but checking
    # individual dataset would have significant performance drop, so
    # this is an acceptable trade-of.
    for builder_dir in _maybe_iterdir(data_dir):
      if builder_dir.name in FILTERED_DIRNAME:
        continue
      yield f'{ns_name}:{builder_dir.name}'
