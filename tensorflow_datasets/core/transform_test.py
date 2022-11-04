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
from typing import List

import numpy as np
import pytest

from tensorflow_datasets.core import transform


def add_two(number: int) -> int:
  return number + 2


def compute_sum(numbers: List[int]) -> int:
  return sum(numbers)


class TestApplyFn:

  def test_simple(self):
    apply_fn = transform.apply_fn(
        fn=add_two, input_feature="a", output_feature="c")
    example = {"a": 1, "d": "left alone"}
    expected = {"a": 1, "c": 3, "d": "left alone"}
    assert apply_fn(example) == expected

  def test_nested_dict(self):
    apply_fn = transform.apply_fn(
        fn=add_two, input_feature="a/b", output_feature="a/c")
    example = {"a": {"b": 1}, "d": "something"}
    expected = {"a": {"b": 1, "c": 3}, "d": "something"}
    assert apply_fn(example) == expected

  def test_nested_dict_different_output(self):
    apply_fn = transform.apply_fn(
        fn=add_two, input_feature="a/b", output_feature="c")
    example = {"a": {"b": 1}, "d": "something"}
    expected = {"a": {"b": 1}, "c": 3, "d": "something"}
    assert apply_fn(example) == expected

  def test_sequence_sum(self):
    apply_fn = transform.apply_fn(
        fn=compute_sum, input_feature="a", output_feature="b")
    example = {"a": [1, 2, 3]}
    expected = {"a": [1, 2, 3], "b": 6}
    assert apply_fn(example) == expected

  def test_nested_sequence_sum(self):
    apply_fn = transform.apply_fn(
        fn=compute_sum, input_feature="a/b", output_feature="c")
    example = {"a": {"b": [1, 2, 3]}}
    expected = {"a": {"b": [1, 2, 3]}, "c": 6}
    assert apply_fn(example) == expected

  def test_non_existing_feature(self):
    with pytest.raises(KeyError):
      apply_fn = transform.apply_fn(
          fn=add_two, input_feature="a", output_feature="b")
      example = {"x": 1}
      apply_fn(example)


class TestMapEachFn:

  def test_sequence(self):
    apply_fn = transform.map_each_fn(
        fn=add_two, input_feature="a", output_feature="b")
    example = {"a": [1, 2, 3]}
    expected = {"a": [1, 2, 3], "b": [3, 4, 5]}
    assert apply_fn(example) == expected

  def test_sequence_numpy(self):
    apply_fn = transform.map_each_fn(
        fn=add_two, input_feature="a", output_feature="b")
    example = {"a": np.array([1, 2, 3])}
    expected = {"a": np.array([1, 2, 3]), "b": np.array([3, 4, 5])}
    actual = apply_fn(example)
    assert np.array_equal(actual["a"], expected["a"])
    assert np.array_equal(actual["b"], expected["b"])

  def test_sequence_numpy_multidim(self):
    apply_fn = transform.map_each_fn(
        fn=add_two, input_feature="a", output_feature="b")
    md_array = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    example = {"a": md_array}
    expected = {"a": md_array, "b": np.array([[3, 4, 5], [6, 7, 8]], np.int32)}
    actual = apply_fn(example)
    assert np.array_equal(actual["a"], expected["a"])
    assert np.array_equal(actual["b"], expected["b"])

  def test_sequence_in_sequence(self):
    apply_fn = transform.map_each_fn(fn=add_two, input_feature="a/b")
    example = {"a": [{"b": [1, 2]}, {"b": [2, 3]}]}
    expected = {"a": [{"b": [3, 4]}, {"b": [4, 5]}]}
    assert apply_fn(example) == expected

  def test_sequence_of_dicts(self):
    apply_fn = transform.map_each_fn(
        fn=add_two, input_feature="a/b", output_feature="a/c")
    example = {"a": [{"b": [1, 2]}, {"b": [2, 3]}]}
    expected = {"a": [{"b": [1, 2], "c": [3, 4]}, {"b": [2, 3], "c": [4, 5]}]}
    assert apply_fn(example) == expected

  def test_sequence_of_images(self):
    apply_fn = transform.map_each_fn(
        fn=np.transpose, input_feature="a/img", levels=1)
    example = {
        "a": [{
            "img": np.array([[0, 1], [2, 3]])
        }, {
            "img": np.array([[1, 2], [3, 4]])
        }]
    }
    expected = {
        "a": [{
            "img": np.array([[0, 2], [1, 3]])
        }, {
            "img": np.array([[1, 3], [2, 4]])
        }]
    }
    actual = apply_fn(example)
    assert np.array_equal(actual["a"][0]["img"], expected["a"][0]["img"])
    assert np.array_equal(actual["a"][1]["img"], expected["a"][1]["img"])


class TestApplyTransformations:

  def test_simple(self):
    transformations = [
        transform.apply_fn(fn=add_two, input_feature="a", output_feature="b"),
        transform.apply_fn(fn=add_two, input_feature="b", output_feature="c"),
        transform.apply_fn(fn=add_two, input_feature="c", output_feature="d"),
        transform.remove_feature("a")
    ]
    key = 1
    example = {"a": 1, "z": "z"}
    actual = transform.apply_transformations(
        key=key, example=example, transformations=transformations)
    assert actual == (1, {"b": 3, "c": 5, "d": 7, "z": "z"})
