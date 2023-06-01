# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Transformation library.

Note that this is an experimental new feature, so the API may change.
"""

from __future__ import annotations

import functools
from typing import Any, Callable, Iterator, List, Mapping, Optional, Union

import numpy as np

from tensorflow_datasets.core import split_builder as split_builder_lib

Key = split_builder_lib.Key
Example = split_builder_lib.Example
KeyExample = split_builder_lib.KeyExample
ExampleTransformFn = Callable[[Example], Iterator[Example]]


def remove_feature(feature_name: Union[str, List[str]]) -> ExampleTransformFn:
  """Removes the feature(s) with the given name."""

  if isinstance(feature_name, str):
    feature_name = [feature_name]

  def apply_on_example(example: Example) -> Iterator[Example]:
    for name in feature_name:
      del example[name]
    yield example

  return apply_on_example


def rename_feature(from_: str, to: str) -> ExampleTransformFn:
  """Renames the feature.

  Note that if `to` already exists in the example, then it will be overridden.

  Arguments:
    from_: the name of the feature that must be renamed.
    to: the feature name to which it must be renamed.

  Returns:
    function that renames the feature of an example.
  """

  def apply_on_example(example: Example) -> Iterator[Example]:
    example[to] = example.pop(from_)
    yield example

  return apply_on_example


def rename_features(name_mapping: Mapping[str, str]) -> ExampleTransformFn:
  """Renames all the feature specified in the given mapping.

  Note that if the 'to feature name' already exists in the example, then it will
  be overridden. The order in which the renames are doing is not guaranteed, so
  this should not be used to swap the content of two features.

  Arguments:
    name_mapping: mapping from the feature name that must be renamed to the new
      feature name.

  Returns:
    function that renames the feature of an example.
  """

  def apply_on_example(example: Example) -> Iterator[Example]:
    for from_name, to_name in name_mapping.items():
      example[to_name] = example.pop(from_name)
    yield example

  return apply_on_example


def _transform_example(
    example: Example,
    fn: Callable[[Any], Any],
    in_parts: List[str],
    out_parts: List[str],
) -> Example:
  """Transforms the specified input entry with `fn`.

  Note that the given example data is transformed in place.

  Arguments:
    example: the example data that needs to be transformed.
    fn: the function used to transform data.
    in_parts: what feature in the example should be transformed. For example, if
      `in_parts` is `["a", "b"]`, then `fn` will be applied to the nested
      feature `b` inside `a`.
    out_parts: where the transformed data should be stored in the example. Note
      that this needs to be at the same level as `in_parts`. For example, if
      `in_parts=["a", "b", "c"]`, then the output feature needs to be inside
      `["a", "b']`, e.g. `out_parts=["a", "b", "new_feature"]`.

  Returns:
    the transformed example.
  """
  if not in_parts:
    raise ValueError("Should be called with non-empty `in_parts`!")
  in_key = in_parts[0]
  out_key = out_parts[0]
  if len(in_parts) > 1:
    in_rest = in_parts[1:]
    out_rest = out_parts[1:]
    if isinstance(example[in_key], np.ndarray) or isinstance(
        example[in_key], list
    ):
      example[out_key] = [
          _transform_example(
              example=ex, fn=fn, in_parts=in_rest, out_parts=out_rest
          )
          for ex in example[in_key]
      ]
    else:
      example[out_key] = _transform_example(
          example=example[in_key], fn=fn, in_parts=in_rest, out_parts=out_rest
      )
  elif len(in_parts) == 1:
    input_data = example[in_key]
    if isinstance(input_data, List):
      example[out_key] = [fn(x) for x in input_data]
    else:
      example[out_key] = fn(example[in_key])
  return example


def apply_fn(
    fn: Callable[[Any], Any],
    input_feature: str,
    output_feature: Optional[str] = None,
) -> ExampleTransformFn:
  """Returns a function that applies the given `fn` on the `input_feature`.

  Arguments:
    fn: the function to apply.
    input_feature: the name of the feature on which `fn` should be applied. If a
      nested feature needs to be transformed, then specify it using slashes. For
      example, to transform feature `b` inside `a`, use `a/b`.
    output_feature: the name of the feature where the result should be stored.
      If `None`, then `input_feature` will be overridden.

  Returns:
    a function that applies `fn` to `input_feature` field of examples and stores
    the result in `output_feature`.
  """
  input_parts = input_feature.split("/")
  if output_feature is not None:
    output_parts = output_feature.split("/")
  else:
    output_parts = input_parts
  if (
      len(input_parts) != len(output_parts)
      or input_parts[:-1] != output_parts[:-1]
  ):
    raise ValueError(
        "The out-feature must have the same ancestor as the "
        f"in-feature! Got in={input_parts}, out={output_parts}."
    )

  def transform(example: Example) -> Iterator[Example]:
    yield _transform_example(
        example=example, fn=fn, in_parts=input_parts, out_parts=output_parts
    )

  return transform


def _apply_filter(
    example: Example,
    fn: Callable[[Any], Any],
    in_parts: List[str],
) -> Iterator[Example]:
  in_data = example
  for part in in_parts:
    in_data = in_data[part]
  if fn(in_data):
    yield example


def apply_filter(
    fn: Callable[[Any], bool],
    input_feature: Optional[str] = None,
) -> ExampleTransformFn:
  """Filters examples for whom `fn` returns true on `input_feature`.

  Arguments:
    fn: the function that returns whether the input feature of an example should
      be filtered.
    input_feature: the input feature to apply `fn` to. If this is the empty
      string, then `fn` will receive the entire example.

  Returns:
    function that can be applied to filter examples.
  """
  if input_feature:
    input_parts = input_feature.split("/")
  else:
    input_parts = []
  return functools.partial(_apply_filter, fn=fn, in_parts=input_parts)


def _apply_do_fn(
    example: Example,
    fn: Callable[[Any], Iterator[Any]],
) -> Iterator[Example]:
  yield from fn(example)


def apply_do_fn(
    fn: Callable[[Any], Iterator[Any]],
) -> ExampleTransformFn:
  """Applies `fn` that can return any number of examples based on an input.

  A do_fn can be used for multiple purposes such as augmentations, but also to
  filter examples.

  Arguments:
    fn: the function that takes an example and outputs 0 or more examples.

  Returns:
    function that can be applied to perform a do fn.
  """
  return functools.partial(_apply_do_fn, fn=fn)


def _apply_transformations_no_key(
    example: Example,
    transformations: List[ExampleTransformFn],
) -> Iterator[Example]:
  """Transforms the example with the given transformations."""
  if transformations:
    fn = transformations[0]
    other_fns = transformations[1:]
    for v in fn(example):
      yield from _apply_transformations_no_key(
          example=v, transformations=other_fns
      )
  else:
    yield example


def apply_transformations(
    key: Key,
    example: Example,
    transformations: List[ExampleTransformFn],
) -> Iterator[KeyExample]:
  for i, transformed_example in enumerate(
      _apply_transformations_no_key(
          example=example, transformations=transformations
      )
  ):
    yield f"{key}_{i}", transformed_example
