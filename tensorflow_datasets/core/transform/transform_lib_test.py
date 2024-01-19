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

"""Tests for transform."""
import functools
from typing import Iterator

import pytest
from tensorflow_datasets.core.transform import transform_lib


def add_number(number: int, increment: int) -> int:
  return number + increment


def is_even(number: int) -> bool:
  return number % 2 == 0


def duplicate(
    example: transform_lib.Example,
) -> Iterator[transform_lib.Example]:
  yield example
  yield example


def test_apply_fn_simple():
  add_two = functools.partial(add_number, increment=2)
  apply_fn = transform_lib.apply_fn(
      fn=add_two, input_feature="a", output_feature="c"
  )
  example = {"a": 1, "d": "left alone"}
  expected = [{"a": 1, "c": 3, "d": "left alone"}]
  assert list(apply_fn(example)) == expected


def test_apply_fn_nested_dict():
  add_two = functools.partial(add_number, increment=2)
  apply_fn = transform_lib.apply_fn(
      fn=add_two, input_feature="a/b", output_feature="a/c"
  )
  example = {"a": {"b": 1}, "d": "something"}
  expected = [{"a": {"b": 1, "c": 3}, "d": "something"}]
  assert list(apply_fn(example)) == expected


def test_apply_fn_sequence():
  add_two = functools.partial(add_number, increment=2)
  apply_fn = transform_lib.apply_fn(
      fn=add_two, input_feature="a", output_feature="b"
  )
  example = {"a": [1, 2, 3]}
  expected = [{"a": [1, 2, 3], "b": [3, 4, 5]}]
  assert list(apply_fn(example)) == expected


def test_apply_fn_sequence_of_dicts():
  add_two = functools.partial(add_number, increment=2)
  apply_fn = transform_lib.apply_fn(
      fn=add_two, input_feature="a/b", output_feature="a/c"
  )
  example = {"a": [{"b": [1, 2]}, {"b": [2, 3]}]}
  expected = [{"a": [{"b": [1, 2], "c": [3, 4]}, {"b": [2, 3], "c": [4, 5]}]}]
  assert list(apply_fn(example)) == expected


def test_apply_fn_different_ancestor():
  add_two = functools.partial(add_number, increment=2)
  with pytest.raises(
      ValueError, match="The out-feature must have the same ancestor"
  ):
    transform_lib.apply_fn(
        fn=add_two, input_feature="a/b", output_feature="c/d"
    )


def test_apply_filter_on_feature():
  apply_filter_fn = transform_lib.apply_filter(fn=is_even, input_feature="a")
  assert list(apply_filter_fn(example={"a": 2}))
  assert not list(apply_filter_fn(example={"a": 1}))


def test_apply_filter_on_example():
  def a_is_even(example) -> bool:
    return example["a"] % 2 == 0

  apply_filter_fn = transform_lib.apply_filter(fn=a_is_even, input_feature="")
  assert list(apply_filter_fn(example={"a": 2}))
  assert not list(apply_filter_fn(example={"a": 1}))


def test_do_fn():
  apply_do_fn = transform_lib.apply_do_fn(fn=duplicate)
  example = {"a": 1}
  assert list(apply_do_fn(example)) == [example, example]


def test_remove_feature():
  remove_fn = transform_lib.remove_feature("a")
  assert list(remove_fn(example={"a": 1, "b": 2})) == [{"b": 2}]


def test_remove_feature_multiple():
  remove_fn = transform_lib.remove_feature(["a", "b"])
  assert list(remove_fn(example={"a": 1, "b": 2, "c": 3})) == [{"c": 3}]


def test_rename_feature():
  rename_fn = transform_lib.rename_feature("a", "b")
  assert list(rename_fn(example={"a": 1})) == [{"b": 1}]


def test_rename_features():
  rename_fn = transform_lib.rename_features({"a": "x", "b": "y"})
  example = {"a": 1, "b": 2, "c": 3}
  expected = {"x": 1, "y": 2, "c": 3}
  assert list(rename_fn(example=example)) == [expected]
