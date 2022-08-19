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

"""Tests for transformation."""
from typing import Iterator

from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import transformation as transform_lib


def add_one(
    key: transform_lib.Key,
    example: transform_lib.Example,
) -> Iterator[transform_lib.KeyExample]:
  example["number"] += 1
  yield key, example


class DummyRowTransformation(transform_lib.RowTransformation):

  def __init__(self):
    super().__init__(name="dummy")

  def output_features(
      self,
      input_features: feature_lib.FeaturesDict,
  ) -> feature_lib.FeaturesDict:
    return input_features

  def apply(
      self,
      key: transform_lib.Key,
      example: transform_lib.Example,
  ) -> Iterator[transform_lib.KeyExample]:
    return add_one(key, example)


def test_row_transformation_apply():
  key = "a"
  example = {"number": 0}
  transformation = DummyRowTransformation()
  results = list(transformation.apply(key, example))
  assert len(results) == 1
  actual_key, actual_example = results[0]
  assert actual_key == key
  assert actual_example == {"number": 1}


def test_composite_row_transformation_apply():
  key = "a"
  example = {"number": 0}
  transformation = transform_lib.CompositeRowTransformation(
      name="add_two", row_transformations=[add_one, add_one])
  results = list(transformation.apply(key, example))
  assert len(results) == 1
  actual_key, actual_example = results[0]
  assert actual_key == key
  assert actual_example == {"number": 2}
