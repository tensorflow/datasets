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

"""Tests for transform."""
import functools

import pytest

from tensorflow_datasets.core import transform


def add_number(number: int, increment: int) -> int:
  return number + increment


def test_apply_fn_simple():
  add_two = functools.partial(add_number, increment=2)
  apply_fn = transform.apply_fn(
      fn=add_two, input_feature="a", output_feature="c")
  example = {"a": 1, "d": "left alone"}
  expected = {"a": 1, "c": 3, "d": "left alone"}
  assert apply_fn(example) == expected


def test_apply_fn_nested_dict():
  add_two = functools.partial(add_number, increment=2)
  apply_fn = transform.apply_fn(
      fn=add_two, input_feature="a/b", output_feature="a/c")
  example = {"a": {"b": 1}, "d": "something"}
  expected = {"a": {"b": 1, "c": 3}, "d": "something"}
  assert apply_fn(example) == expected


def test_apply_fn_sequence():
  add_two = functools.partial(add_number, increment=2)
  apply_fn = transform.apply_fn(
      fn=add_two, input_feature="a", output_feature="b")
  example = {"a": [1, 2, 3]}
  expected = {"a": [1, 2, 3], "b": [3, 4, 5]}
  assert apply_fn(example) == expected


def test_apply_fn_sequence_of_dicts():
  add_two = functools.partial(add_number, increment=2)
  apply_fn = transform.apply_fn(
      fn=add_two, input_feature="a/b", output_feature="a/c")
  example = {"a": [{"b": [1, 2]}, {"b": [2, 3]}]}
  expected = {"a": [{"b": [1, 2], "c": [3, 4]}, {"b": [2, 3], "c": [4, 5]}]}
  assert apply_fn(example) == expected


def test_apply_fn_different_ancestor():
  add_two = functools.partial(add_number, increment=2)
  with pytest.raises(
      ValueError, match="The out-feature must have the same ancestor"):
    transform.apply_fn(fn=add_two, input_feature="a/b", output_feature="c/d")
