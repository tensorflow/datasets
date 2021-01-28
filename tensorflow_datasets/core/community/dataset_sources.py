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

"""Utils to download locally dataset code source stored remotelly."""

import os
from typing import List
import dataclasses

from tensorflow_datasets.core import utils


@dataclasses.dataclass(frozen=True, eq=True)
class DatasetSource:
  """Structure containing information required to fetch a dataset.

  Attributes:
    root_path: Root directory of the dataset package (e.g.
      `gs://.../my_dataset/`, `github://.../my_dataset/`)
    filenames: Content of the dataset package
  """
  root_path: utils.ReadWritePath
  filenames: List[str]

  @classmethod
  def from_json(cls, value: utils.JsonValue) -> 'DatasetSource':
    """Imports from JSON."""
    if isinstance(value, str):  # Single-file dataset ('.../my_dataset.py')
      path = utils.as_path(value)
      return cls(root_path=path.parent, filenames=[path.name])
    elif isinstance(value, dict):  # Multi-file dataset
      return cls(
          root_path=utils.as_path(value['root_path']),
          filenames=value['filenames'],
      )
    else:
      raise ValueError(f'Invalid input: {value}')

  def to_json(self) -> utils.JsonValue:
    """Exports to JSON."""
    if len(self.filenames) == 1:
      return os.fspath(self.root_path / self.filenames[0])
    else:
      return {
          'root_path': os.fspath(self.root_path),
          'filenames': self.filenames
      }


def download_from_source(
    source: DatasetSource,
    dst: utils.ReadWritePath,
) -> None:
  """Download the remote dataset code locally to the dst path.

  Args:
    source: Source of the dataset.
    dst: Empty directory on which copying the source
  """
  # Download the files
  # Note: We do not check for file existance before copying/downloading it to
  # not trigger unecessary queries when `source.root_path` is `GithubPath`.
  # A `FileNotFoundError` is triggered if the file can't be downloaded.
  for filename in source.filenames:
    path = source.root_path / filename
    path.copy(dst / path.name)

  # Add the `__init__` file
  (dst / '__init__.py').write_text('')
