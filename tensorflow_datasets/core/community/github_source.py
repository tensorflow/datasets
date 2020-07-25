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

"""Github source."""

from typing import ClassVar

import dataclasses

from tensorflow_datasets.core import github_api
from tensorflow_datasets.core.community import dataset_spec


@dataclasses.dataclass
class GithubSource(dataset_spec.DatasetSource):
  """Dataset loaded from Github.

  Attributes:
    path: The github path of the dataset
    SCHEME: See parent class
  """
  path: github_api.GithubPath

  SCHEME: ClassVar[str] = 'github://'  # pylint: disable=invalid-name

  @classmethod
  def from_uri(cls, value: str):
    path = value[len(cls.SCHEME):]  # TODO(py3.9): Use value.removeprefix
    return cls(path=github_api.GithubPath(f'/{path}'))

  def to_uri(self) -> str:
    path = str(self.path).lstrip('/')
    return f'{self.SCHEME}{path}'
