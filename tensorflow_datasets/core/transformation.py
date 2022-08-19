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

"""Transformations for datasets."""

import dataclasses
from typing import Callable, Iterator, List, Optional, Mapping

import tensorflow as tf
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import split_builder as split_builder_lib

Key = split_builder_lib.Key
Example = split_builder_lib.Example
KeyExample = split_builder_lib.KeyExample


@dataclasses.dataclass()
class BaseTransformation:
  """A view that applies transformations on data."""
  name: str
  version: Optional[str] = None
  description: Optional[str] = None
  release_notes: Optional[Mapping[str, str]] = None

  def output_features(
      self,
      input_features: feature_lib.FeaturesDict,
  ) -> feature_lib.FeaturesDict:
    raise NotImplementedError()


class RowTransformation(BaseTransformation):

  def apply(self, key: Key, example: Example) -> Iterator[KeyExample]:
    raise NotImplementedError


class CompositeRowTransformation(RowTransformation):
  """A sequence of row transformations that should be applied."""

  def __init__(self, row_transformations: List[Callable[[Key, Example],
                                                        Iterator[KeyExample]]],
               **kwargs):
    self.row_transformations = row_transformations
    super().__init__(**kwargs)

  def apply(self, key: Key, example: Example) -> Iterator[KeyExample]:
    results = [(key, example)]
    for fn in self.row_transformations:
      tmp_results = []
      for k, v in results:
        for tmp_k, tmp_v in fn(k, v):
          tmp_results.append((tmp_k, tmp_v))
      results = tmp_results
    for result in results:
      yield result


class DatasetTransformation(BaseTransformation):

  def apply(self, input_dataset: tf.data.Dataset) -> tf.data.Dataset:
    raise NotImplementedError()
