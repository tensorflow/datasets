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

"""Base register class."""

import abc
from typing import Any, List, Type

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import utils


class BaseRegister(abc.ABC):
  """Abstract register class.

  The register class indicates how to load a dataset from the name. Abstract
  methods `register.xyz()` have the same API as `tfds.xyz()`.

  ```
  register = MyRegister()
  register.list_builders()
  builder = register.builder('kaggle', 'my_dataset')
  ```

  Subclasses indicates how dataset code are fetched:

  * DataDirRegister: Find the dataset by looking at pre-generated dataset
    inside `data_dir`.
  * RemoteRegister: Find the dataset by fetching remote generation script.

  """

  @abc.abstractmethod
  def list_builders(self) -> List[str]:
    """Returns the list of registered builders.

    Returns:
      builder_names: The sorted, cannonical list of builder names (including
        the eventual namespace). Example: `['kaggle:ds0', 'kaggle:ds1',...]`
    """
    raise NotImplementedError

  @abc.abstractmethod
  def builder_cls(
      self,
      name: utils.DatasetName,
  ) -> Type[dataset_builder.DatasetBuilder]:
    """Returns the `tfds.core.DatasetBuilder` instance.

    Contrary to `tfds.builder_cls`, `builder_name` here is already normalized (
    `my_dataset/my_config` -> `my_dataset`, `{'config': 'my_config'}`).

    Args:
      name: Builder name (e.g. `DatasetName('kaggle:mnist')`)

    Returns:
      builder_cls
    """
    raise NotImplementedError

  @abc.abstractmethod
  def builder(
      self,
      name: utils.DatasetName,
      **builder_kwargs: Any,
  ) -> dataset_builder.DatasetBuilder:
    """Returns the `tfds.core.DatasetBuilder` instance.

    Contrary to `tfds.builder`, `builder_name` here is already normalized (
    `my_dataset/my_config` -> `my_dataset`, `{'config': 'my_config'}`).

    Args:
      name: Builder name (e.g. `DatasetName('kaggle:mnist')`)
      **builder_kwargs: Additional kwargs forwarded to
        `tfds.core.DatasetBuilder` (version, config,...)

    Returns:
      builder
    """
    raise NotImplementedError
