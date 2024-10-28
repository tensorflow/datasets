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

r"""Config for community datasets."""

from collections.abc import Mapping, Sequence
import dataclasses
import functools
import threading
from typing import Any

from absl import logging
from etils import epath
# Make sure that github paths are registered. This import makes sure that epath
# understands paths that start with github://.
from tensorflow_datasets.core import github_api  # pylint: disable=unused-import
from tensorflow_datasets.core.utils import resource_utils
import toml


@dataclasses.dataclass(frozen=True)
class NamespaceConfig:
  """Configuration for a namespace."""

  paths: Sequence[epath.Path]
  info: str | None = None

  def __post_init__(self):
    if not self.paths:
      raise ValueError('NamespaceConfig must have at least one path.')


def _as_path_list(path_or_paths: str | Sequence[str]) -> Sequence[epath.Path]:
  if isinstance(path_or_paths, str):
    path_or_paths = [path_or_paths]
  return [epath.Path(p) for p in path_or_paths]


def _load_config(config: Mapping[str, Any]) -> NamespaceConfig:
  return NamespaceConfig(
      paths=_as_path_list(config['paths']),
      info=config.get('info', None),
  )


class NamespaceRegistry:
  """What namespaces there are and where to find their datasets.

  The config file should be in `.toml` format and have the follow structure:

  ```toml
  [huggingface]
  paths = 'github://huggingface/datasets/tree/master/datasets'
  [kaggle]
  paths = ['/path/to/datasets/', '/path/to/more_datasets/']
  [tensorflow_graphics]
  paths = 'gs://tensorflow-graphics/datasets'
  ```

  Attributes:
    config_path: path where the config is stored.
    config_per_namespace: mapping from namespace to configuration.
  """

  def __init__(self, config_path: epath.Path):
    self.config_path = config_path
    # Load the namespace config only when it is used.
    self._config_per_namespace: dict[str, NamespaceConfig] = {}
    self._is_config_per_namespace_initialized = False
    # If multiple threads all initialize the config per namespace at the same
    # time, then this will cause an exception. Use a lock to make sure it's
    # initialized only once.
    self._lock = threading.Lock()

  def _initialize_config_per_namespace(self) -> None:
    with self._lock:
      # If this thread had to wait, it might have been initialized in the
      # meantime, so check again whether it's initialized.
      if not self._is_config_per_namespace_initialized:
        logging.info('Loading namespace config from %s', self.config_path)
        raw_config = toml.loads(self.config_path.read_text())
        for namespace, raw_namespace_config in raw_config.items():
          namespace_config = _load_config(config=raw_namespace_config)
          self.add_namespace(namespace, namespace_config)
        self._is_config_per_namespace_initialized = True

  @property
  def config_per_namespace(self) -> Mapping[str, NamespaceConfig]:
    """Returns a mapping from namespace to configuration."""
    if not self._is_config_per_namespace_initialized:
      self._initialize_config_per_namespace()
    return self._config_per_namespace

  def add_namespace(self, namespace: str, config: NamespaceConfig) -> None:
    if namespace in self._config_per_namespace:
      namespaces = ', '.join(sorted(self._config_per_namespace.keys()))
      raise RuntimeError(
          f'NamespaceRegistry({self.config_path},'
          f' initialized={self._is_config_per_namespace_initialized}):'
          f' namespace {namespace} is already defined! Defined namespaces:'
          f' {namespaces}'
      )
    self._config_per_namespace[namespace] = config


COMMUNITY_CONFIG_PATH = 'community-datasets.toml'


@functools.lru_cache(maxsize=1)
def get_community_config() -> NamespaceRegistry:
  return NamespaceRegistry(
      config_path=resource_utils.tfds_path(COMMUNITY_CONFIG_PATH)
  )
