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
from typing import Any

from etils import epath
# Make sure that github paths are registered. This import makes sure that epath
# understands paths that start with github://.
from tensorflow_datasets.core import github_api  # pylint: disable=unused-import
from tensorflow_datasets.core import utils
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
    # Load the namespace config only when it is needed.
    self._config_per_namespace: dict[str, NamespaceConfig] = {}
    self._is_config_per_namespace_initialized = False

  @property
  def config_per_namespace(self) -> Mapping[str, NamespaceConfig]:
    """Returns a mapping from namespace to configuration."""
    if not self._is_config_per_namespace_initialized:
      raw_config = toml.loads(self.config_path.read_text())
      for namespace, raw_namespace_config in raw_config.items():
        namespace_config = _load_config(config=raw_namespace_config)
        self.add_namespace(namespace, namespace_config)
      self._is_config_per_namespace_initialized = True
    return self._config_per_namespace

  def add_namespace(self, namespace: str, config: NamespaceConfig) -> None:
    if namespace in self._config_per_namespace:
      raise RuntimeError(
          f'NamespaceRegistry({self.config_path}): namespace {namespace} is'
          ' already defined!'
      )
    self._config_per_namespace[namespace] = config


community_config = NamespaceRegistry(
    config_path=utils.tfds_path('community-datasets.toml')
)
