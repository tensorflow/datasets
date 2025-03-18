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

"""Meta register that uses other registers."""

from collections.abc import Iterable, Mapping, Sequence
import concurrent.futures
import difflib
import functools
import multiprocessing
import os
from typing import Any, Type

from absl import logging
from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.community import config as config_lib
from tensorflow_datasets.core.community import register_base
from tensorflow_datasets.core.community import register_package
from tensorflow_datasets.core.community import register_path
from tensorflow_datasets.core.utils import gcs_utils


def _load_registry(
    namespace: str,
    config: config_lib.NamespaceConfig,
) -> register_base.BaseRegister:
  """Returns a list of registers for the given paths."""
  code_paths = []
  data_paths = []
  for path in config.paths:
    if os.fspath(path).startswith('github'):
      code_paths.append(path)
    else:
      data_paths.append(path)

  if code_paths and data_paths:
    raise RuntimeError(
        f'Both a path containing code ({code_paths}) and a path containing data'
        f' ({data_paths} are specified. This is not supported'
    )

  if data_paths:
    return register_path.DataDirRegister(namespaces={namespace: config})
  elif code_paths:
    return register_package.PackageRegister(
        path=gcs_utils.GCS_COMMUNITY_INDEX_PATH
    )
  raise RuntimeError(f'No paths specified for {namespace}')


def _registers_per_namespace(
    config_per_namespace: Mapping[str, config_lib.NamespaceConfig],
) -> Mapping[str, Sequence[register_base.BaseRegister]]:
  return {
      namespace: [_load_registry(namespace, config)]
      for namespace, config in config_per_namespace.items()
  }


class DatasetRegistry(register_base.BaseRegister):
  """Registry of dataset registries.

  Each namespace is associated with one or more registers. Those registers can
  be any type of register, e.g. code on Github or datasets stored somewhere.

  Attributes:
    namespace_registry: registry of all the namespaces and their configs.
    config_per_namespace: mapping from namespace to configuration.
    registers_per_namespace: mapping from namespace to a sequence of registers
      for that namespace.
  """

  def __init__(self, namespace_registry: config_lib.NamespaceRegistry):
    self.namespace_registry = namespace_registry
    self._registers_per_namespace: dict[
        str, Sequence[register_base.BaseRegister]
    ] = {}
    self._is_registers_per_namespace_initialized = False

  @property
  def config_per_namespace(self) -> Mapping[str, config_lib.NamespaceConfig]:
    return self.namespace_registry.config_per_namespace

  def _init_registers_per_namespace(self):
    if self._is_registers_per_namespace_initialized:
      return
    self._registers_per_namespace.update(
        _registers_per_namespace(self.config_per_namespace)
    )
    self._is_registers_per_namespace_initialized = True

  @property
  def registers_per_namespace(
      self,
  ) -> Mapping[str, Sequence[register_base.BaseRegister]]:
    self._init_registers_per_namespace()
    return self._registers_per_namespace

  def add_namespace(
      self,
      namespace: str,
      config: config_lib.NamespaceConfig,
      registers: Sequence[register_base.BaseRegister],
  ):
    self._init_registers_per_namespace()
    if namespace in self._registers_per_namespace:
      raise ValueError(
          f'Namespace {namespace} already exists! Existing namespace config is'
          f' {self.config_per_namespace[namespace]}.'
      )
    self._registers_per_namespace[namespace] = registers
    self.namespace_registry.add_namespace(namespace=namespace, config=config)

  def has_namespace(self, namespace: str) -> bool:
    if not namespace:
      return False
    return namespace in self.config_per_namespace

  def list_namespaces(self) -> Sequence[str]:
    return sorted(self.config_per_namespace.keys())

  def list_builders(self) -> Sequence[str]:
    builders = []
    for registers in self.registers_per_namespace.values():
      for register in registers:
        builders.extend(register.list_builders())
    return builders

  def list_dataset_references(
      self, max_workers: int = multiprocessing.cpu_count()
  ) -> Iterable[naming.DatasetReference]:
    all_registers = []
    for registers in self.registers_per_namespace.values():
      all_registers.extend(registers)

    def _get_references(
        register: register_base.BaseRegister,
    ) -> Iterable[naming.DatasetReference]:
      try:
        yield from register.list_dataset_references()
      except Exception:  # pylint: disable=broad-except
        logging.exception(
            'Exception while getting dataset references from register %s',
            register,
        )

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=max_workers
    ) as executor:
      output = list(executor.map(_get_references, all_registers))
      for dataset_references in output:
        yield from dataset_references

  def list_dataset_references_for_namespace(
      self, namespace: str
  ) -> Iterable[naming.DatasetReference]:
    """Lists the dataset references available for a specific namespace.

    Args:
      namespace: a namespace.

    Yields:
      An iterator over the datasets references for the given namespace.

    Raises:
      ValueError if the given namespace doesn't exist in the registry.
    """
    if not self.has_namespace(namespace):
      raise ValueError(f'Namespace {namespace} not found.')
    for register in self.registers_per_namespace[namespace]:
      try:
        yield from register.list_dataset_references()
      except Exception as e:  # pylint: disable=broad-except
        logging.exception(
            'Exception while getting dataset references from register %s: %s',
            register,
            e,
        )

  def list_builders_per_namespace(self, namespace: str) -> Sequence[str]:
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
    all_datasets_str = '\n\t- '.join([''] + list(all_datasets))
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
  ) -> Sequence[register_base.BaseRegister]:
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

  def get_builder_root_dirs(
      self, name: naming.DatasetName
  ) -> Sequence[epath.Path]:
    """Returns root dir of the generated builder (without version/config)."""
    result = []
    registers = self.registers_per_namespace[name.namespace]
    for register in registers:
      if isinstance(register, register_path.DataDirRegister):
        result.extend(register.get_builder_root_dirs(name))
      else:
        raise RuntimeError(f'Not supported for non datadir registers ({name})!')
    return result


@functools.lru_cache(maxsize=1)
def community_register() -> DatasetRegistry:
  return DatasetRegistry(config_lib.get_community_config())
