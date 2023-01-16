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

"""Meta register that uses other registers."""

import dataclasses
import difflib
import functools
import os
from typing import Any, Iterable, List, Mapping, Type

from absl import logging
from etils import epath
from tensorflow_datasets.core import dataset_builder
# Make sure that github paths are registered
from tensorflow_datasets.core import github_api  # pylint: disable=unused-import
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import register_base
from tensorflow_datasets.core.community import register_package
from tensorflow_datasets.core.community import register_path
from tensorflow_datasets.core.utils import gcs_utils
import toml


def _as_path_list(path_or_paths: utils.ListOrElem[str]) -> List[epath.Path]:
  if isinstance(path_or_paths, list):
    return [epath.Path(p) for p in path_or_paths]
  else:
    return [epath.Path(path_or_paths)]


def _load_register_for_paths(
    namespace: str,
    paths: List[epath.Path],
) -> List[register_base.BaseRegister]:
  """Returns a list of registers for the given paths."""
  code_paths = []
  data_paths = []
  for path in paths:
    if os.fspath(path).startswith('github'):
      code_paths.append(path)
    else:
      data_paths.append(path)

  if code_paths and data_paths:
    raise RuntimeError(
        f'Both a path containing code ({code_paths}) and '
        f'a path containing data ({data_paths} are specified. '
        'This is not supported'
    )

  registers = []
  if data_paths:
    register = register_path.DataDirRegister(
        namespace_to_data_dirs={namespace: data_paths}
    )
    registers.append(register)
  if code_paths:
    registers.append(
        register_package.PackageRegister(
            path=gcs_utils.GCS_COMMUNITY_INDEX_PATH
        )
    )
  return registers


@dataclasses.dataclass(eq=True, frozen=True)
class NamespaceConfig:
  """Config what namespaces there are and where to find their datasets.

  The config file should be in `.toml` format and have the follow structure:

  ```toml
  [Namespaces]
  huggingface='github://huggingface/datasets/tree/master/datasets'
  kaggle=['/path/to/datasets/', '/path/to/more_datasets/']
  tensorflow_graphics='gs://tensorflow-graphics/datasets'
  ```
  """

  config_path: epath.Path

  @functools.lru_cache()
  def registers_per_namespace(
      self,
  ) -> Mapping[str, List[register_base.BaseRegister]]:
    """Returns the registry containing all repositories in the given config.

    Raises:
      RuntimeError: when the config contains errors.
    """
    config = toml.loads(self.config_path.read_text())
    registers_per_namespace = {}
    for namespace, path_or_paths in config['Namespaces'].items():
      if namespace in registers_per_namespace:
        raise RuntimeError(
            f'Namespace {namespace} is defined twice in config'
            f' {self.config_path}'
        )
      registers_per_namespace[namespace] = _load_register_for_paths(
          namespace=namespace, paths=_as_path_list(path_or_paths)
      )
    return registers_per_namespace


@dataclasses.dataclass()
class DatasetRegistry(register_base.BaseRegister):
  """Registry of dataset registries.

  Each namespace is associated with one or more registers. Those registers can
  be any type of register, e.g. code on Github or datasets stored somewhere.

  Attributes:
    namespace_config: config where to find the datasets of a namespace.
    registers_per_namespace: per namespace a list of registers it consists of.
  """

  namespace_config: NamespaceConfig

  @property
  def registers_per_namespace(
      self,
  ) -> Mapping[str, List[register_base.BaseRegister]]:
    return self.namespace_config.registers_per_namespace()

  def has_namespace(self, namespace: str) -> bool:
    if not namespace:
      return False
    return namespace in self.registers_per_namespace

  def list_namespaces(self) -> List[str]:
    return sorted(self.registers_per_namespace.keys())

  def list_builders(self) -> List[str]:
    builders = []
    for registers in self.registers_per_namespace.values():
      for register in registers:
        builders.extend(register.list_builders())
    return builders

  def list_dataset_references(self) -> Iterable[naming.DatasetReference]:
    for registers in self.registers_per_namespace.values():
      for register in registers:
        try:
          yield from register.list_dataset_references()
        except Exception:  # pylint: disable=broad-except
          logging.exception(
              'Exception while getting dataset references from register %s',
              register,
          )

  def list_builders_per_namespace(self, namespace: str) -> List[str]:
    """Lists the builders available for a specific namespace."""
    builders = []
    if self.has_namespace(namespace):
      for register in self.registers_per_namespace[namespace]:
        builders.extend(register.list_builders())
    return builders

  def _get_list_builders_context(self, name: naming.DatasetName) -> str:
    """Adds relevant information to the error context."""
    # Add list of available datasets to error context.
    all_datasets = self.list_builders_per_namespace(name.namespace)
    all_datasets_str = '\n\t- '.join([''] + all_datasets)
    error_msg = (
        f'Available datasets under the same namespace:{all_datasets_str}\n'
    )
    # Add closest match to error context.
    close_matches = difflib.get_close_matches(str(name), all_datasets, n=1)
    if close_matches:
      error_msg += f'\nDid you mean: {name} -> {close_matches[0]} ?\n'
    return error_msg

  def _get_registers(
      self, name: naming.DatasetName
  ) -> List[register_base.BaseRegister]:
    """Returns all available registers for a given namespace, if any.

    Args:
      name: str, the namespace's name.

    Raises:
      DatasetNotFound error if the namespace is not found.
    """
    if not self.has_namespace(name.namespace):
      error_msg = f'\nNamespace {name.namespace} not found. '
      error_msg += (
          'Note that the namespace should be one of: '
          f'{sorted(self.registers_per_namespace.keys())}.\n'
      )
      close_matches = difflib.get_close_matches(
          name.namespace, self.registers_per_namespace, n=1
      )
      if close_matches:
        error_msg += f'Did you mean: {name.namespace} -> {close_matches[0]} ?\n'
      raise registered.DatasetNotFoundError(error_msg)
    return self.registers_per_namespace[name.namespace]

  def builder_cls(
      self,
      name: naming.DatasetName,
  ) -> Type[dataset_builder.DatasetBuilder]:
    """Loads the builder class for the given dataset.

    Arguments:
      name: the name and namespace of the dataset to load the builder class for.

    Returns:
      DatasetNotFoundError if data is not found.
    """
    registers = self._get_registers(name)

    # Typically there's only 1, so add special case so that more informative
    # exceptions are raised.
    if len(registers) == 1:
      return registers[0].builder_cls(name)

    # If this dataset has multiple registers, use the first that can be found.
    for register in registers:
      try:
        return register.builder_cls(name)
      except registered.DatasetNotFoundError:
        pass

    raise registered.DatasetNotFoundError(
        f'Namespace {name.namespace} found, '
        f'but could not load dataset {name.name}.'
        f'{self._get_list_builders_context(name)}'
    )

  def builder(
      self,
      name: naming.DatasetName,
      **builder_kwargs: Any,
  ) -> dataset_builder.DatasetBuilder:
    """Loads the builder class for the given dataset."""
    registers = self._get_registers(name)

    # Typically there's only 1, so add special case so that more informative
    # exceptions are raised.
    if len(registers) == 1:
      return registers[0].builder(name, **builder_kwargs)

    if len(registers) > 1:
      raise ValueError(
          f'Namespace {name.namespace} has multiple registers! '
          f'This should not happen! Registers: {registers}'
      )

    raise registered.DatasetNotFoundError(
        f'Namespace {name.namespace} found with {len(registers)} registers, '
        f'but could not load dataset {name.name}.'
    )

  def get_builder_root_dirs(self, name: naming.DatasetName) -> List[epath.Path]:
    """Returns root dir of the generated builder (without version/config)."""
    result = []
    registers = self.registers_per_namespace[name.namespace]
    for register in registers:
      if isinstance(register, register_path.DataDirRegister):
        result.extend(register.get_builder_root_dirs(name))
      else:
        raise RuntimeError(f'Not supported for non datadir registers ({name})!')
    return result


def registry_for_config(config_path: epath.PathLike) -> DatasetRegistry:
  return DatasetRegistry(NamespaceConfig(config_path=epath.Path(config_path)))


community_register = registry_for_config(
    config_path=(utils.tfds_path() / 'community-datasets.toml')
)
