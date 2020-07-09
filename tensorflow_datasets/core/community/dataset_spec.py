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

"""Community utils."""

import abc
from typing import ClassVar, Dict

import dataclasses
from tensorflow_datasets.core import github_api
from tensorflow_datasets.core import utils

Json = utils.Json


class DatasetSource(abc.ABC):
  """Source indicating the dataset location (abstract class).

  Additional user-defined sources can be registered by subclassing this class.

  Attributes:
    SCHEME: URI scheme (e.g. `github://`).
  """

  # Abstract class attribute
  SCHEME: ClassVar[str]

  # Use non-mutable dict to prevent collision if two subclass try to use the
  # same scheme
  _subclasses: Dict[str, 'DatasetSource'] = utils.NonMutableDict()

  def __init_subclass__(cls, **kwargs):
    """Subclasses are automatically registered."""
    super().__init_subclass__(**kwargs)
    cls._subclasses[cls.SCHEME] = cls  # Subclasses should have a unique SCHEME

  @classmethod
  @abc.abstractmethod
  def from_json(cls, value: Json) -> 'DatasetSource':
    """Factory which will instancite the source from the registered class.

    ```
    source = DatasetSource.from_json({'type': 'github://', ...})
    assert isinstance(source, GithubSource)
    ```

    Args:
      value: Json dict containing the constructor information.

    Returns:
      The created source instance.
    """
    source_type = dict(value).pop('scheme')
    subclass = cls._subclasses.get(source_type)
    if subclass is None:
      raise ValueError(
          f'Invalid source type {source_type} of: {value}\n'
          f'Supported: {list(cls._subclasses)}'
      )
    return subclass.from_json(value)

  @abc.abstractmethod
  def to_json(self) -> Json:
    """Exports the object to Json. Subclasses should call `super()`."""
    return {'scheme': self.SCHEME}


@dataclasses.dataclass
class GithubSource(DatasetSource):
  """Dataset loaded from Github.

  Attributes:
    path: The github path of the dataset
    SCHEME: See parent class
  """
  path: github_api.GithubPath

  SCHEME: ClassVar[str] = 'github://'  # pylint: disable=invalid-name

  @classmethod
  def from_json(cls, value: Json):
    return cls(path=github_api.GithubPath(value['path']))

  def to_json(self) -> Json:
    value = super().to_json()
    value['path'] = str(self.path)
    return value


@dataclasses.dataclass(frozen=True)
class DatasetSpec:
  """Contains specs required to lazily load a dataset.

  The specs match the `COMMUNITY_EXPORTED_PATH` content (one row == one spec)

  Attributes:
    name: dataset name (e.g. `mnist`)
    namespace: user/organization namespace (e.g. `mlds`)
    source: Location of the dataset (e.g. Github)
  """
  name: str
  namespace: str
  source: DatasetSource

  @classmethod
  def from_json(cls, value: Json) -> 'DatasetSpec':
    """Load the specs from a Json dict."""
    return cls(
        name=value['name'],
        namespace=value['namespace'],
        source=DatasetSource.from_json(value['source']),
    )

  def to_json(self) -> Json:
    """Export the specs as a Json dict."""
    return {
        'name': self.name,
        'namespace': self.namespace,
        'source': self.source.to_json(),
    }

  @property
  def cannonical_name(self) -> str:
    """Returns the `namespace/dataset_name` string."""
    return f'{self.namespace}/{self.name}'
