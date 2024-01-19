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

"""Python DataSource base class."""

from __future__ import annotations

from collections.abc import MappingView, Sequence
import dataclasses
from typing import Any, Callable


@dataclasses.dataclass
class PythonDataSource(MappingView, Sequence):
  """Python data source backed by Python objects: length and __getitem__."""

  length: int
  # If you have pickling issues for this function, define it in the upper scope
  # or get inspiration from _getitem in
  # tensorflow_datasets/core/features/dataset_feature.py.
  getitem: Callable[[int], Any]

  def __len__(self) -> int:
    return self.length

  def __iter__(self):
    for i in range(self.length):
      yield self[i]

  def __getitem__(self, i: int) -> Any:
    return self.getitem(i)
