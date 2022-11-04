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

"""Transformation library.

Note that this is an experimental new feature, so the API may change.
"""

from __future__ import annotations

import dataclasses
import functools
from typing import Any, Callable, List, Optional, Union

import numpy as np

from tensorflow_datasets.core import split_builder as split_builder_lib

Key = split_builder_lib.Key
Example = split_builder_lib.Example
KeyExample = split_builder_lib.KeyExample
ExampleTransformFn = Callable[[Example],
                              Example]  # TODO(weide) return Iterator[Example]?


@dataclasses.dataclass()
class FeatureName:
  feature: str
  parts: List[str] = dataclasses.field(default_factory=list)

  def __post_init__(self):
    if not self.feature:
      raise ValueError("Feature name must not be empty!")
    if not self.parts:
      self.parts = self.feature.split("/")


def remove_feature(feature_name: str) -> ExampleTransformFn:
  """Removes a feature from examples."""

  def apply_on_example(example: Example) -> Example:
    del example[feature_name]
    return example

  return apply_on_example


def _transform_example(
    example: Example,
    fn: Callable[[Any], Any],
    input_feature: FeatureName,
    output_feature: FeatureName,
) -> Example:
  """Transforms the specified input entry with `fn`.

  Note that the given example data is transformed in place.

  Arguments:
    example: the example data that needs to be transformed.
    fn: the function used to transform data.
    input_feature: what feature in the example should be transformed.
    output_feature: where the transformed data should be stored in the example.

  Returns:
    the transformed example.
  """
  # Find the data to give to `fn` inside the possibly nested example.
  input_data = example
  for part in input_feature.parts:
    input_data = input_data[part]

  # Find where the transformed data needs to be stored.
  destination = example
  for part in output_feature.parts[:-1]:
    destination = destination[part]

  # Store the transformed data.
  destination[output_feature.parts[-1]] = fn(input_data)
  return example


def _transform_all_elements(
    example: Example,
    fn: Callable[[Any], Any],
    in_parts: List[str],
    out_parts: List[str],
    levels: int,
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
    levels: how many levels deep each element should be mapped. If 0, then `fn`
      will be applied on the whole feature and not on each element in it.

  Returns:
    the transformed example.
  """
  if not in_parts:
    raise ValueError("Should be called with non-empty `in_parts`!")
  if not out_parts:
    raise ValueError("Should be called with non-empty `out_parts`!")
  out_key = out_parts[0]
  input_data = example[in_parts[0]]
  if levels == 0:
    example[out_key] = fn(input_data)
  elif len(in_parts) > 1:
    in_rest = in_parts[1:]
    out_rest = out_parts[1:]
    if isinstance(input_data, np.ndarray):
      input_data = input_data.tolist()
    if isinstance(input_data, list):
      example[out_key] = []
      for ex in input_data:
        example[out_key].append(
            _transform_all_elements(
                example=ex,
                fn=fn,
                in_parts=in_rest,
                out_parts=out_rest,
                levels=levels - 1))
    else:
      example[out_key] = _transform_all_elements(
          example=input_data,
          fn=fn,
          in_parts=in_rest,
          out_parts=out_rest,
          levels=levels - 1)
  elif len(in_parts) == 1:
    if isinstance(input_data, np.ndarray):
      example[out_key] = np.vectorize(fn)(input_data)
    elif isinstance(input_data, List):
      example[out_key] = [fn(x) for x in input_data]
    else:
      example[out_key] = fn(input_data)
  return example


def map_each_fn(
    fn: Callable[[Any], Any],
    input_feature: Union[str, FeatureName],
    output_feature: Union[None, str, FeatureName] = None,
    levels: Optional[int] = None,
) -> ExampleTransformFn:
  """Applies `fn` to each element in the feature.

  If `input_feature` is a sequence, then `fn` will be applied to each element in
  the sequence. Similarly, if `input_feature` is a sequence nested in another
  sequence, then `fn` will be applied to each element. For example, if
  `input_feature='a/b'` and both `a` and `b` are sequences, then `fn` is applied
  to each element in `a` and then to each element in `b`.

  Arguments:
    fn: the function to apply.
    input_feature: the name of the feature on which `fn` should be applied. If a
      nested feature needs to be transformed, then specify it using slashes. For
      example, to transform feature `b` inside `a`, use `a/b`.
    output_feature: the name of the feature where the result should be stored.
      If `None`, then `input_feature` will be overridden.
    levels: how many levels deep each element should be mapped. For example, if
      feature `a` is a sequence with an image `img` in it, and you invoke
      `map_each_fn` with `input_feature="a/img"` and `levels=1`, then the `fn`
      will be applied on each image and not on each pixel.

  Returns:
    a function that applies `fn` to `input_feature` field of examples and stores
    the result in `output_feature`.
  """
  if isinstance(input_feature, str):
    input_feature = FeatureName(feature=input_feature)
  if output_feature is None:
    output_feature = input_feature
  elif isinstance(output_feature, str):
    output_feature = FeatureName(feature=output_feature)
  levels = levels or len(input_feature.parts)

  return functools.partial(
      _transform_all_elements,
      fn=fn,
      in_parts=input_feature.parts,
      out_parts=output_feature.parts,
      levels=levels)


def apply_fn(
    fn: Callable[[Any], Any],
    input_feature: Union[str, FeatureName],
    output_feature: Union[None, str, FeatureName] = None,
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
  if isinstance(input_feature, str):
    input_feature = FeatureName(feature=input_feature)
  if output_feature is None:
    output_feature = input_feature
  elif isinstance(output_feature, str):
    output_feature = FeatureName(feature=output_feature)

  if not input_feature.parts:
    raise ValueError(f"No input feature was specified! Got {input_feature}")
  if not output_feature.parts:
    raise ValueError(f"No output feature was specified! Got {output_feature}")

  if (len(output_feature.parts) > 1 and
      (len(input_feature.parts) != len(input_feature.parts) or
       input_feature.parts[:-1] != input_feature.parts[:-1])):
    raise ValueError(
        "If the out-feature is nested, then it must have the same ancestor as "
        f"the in-feature! Got in={input_feature}, out={output_feature}.")

  return functools.partial(
      _transform_example,
      fn=fn,
      input_feature=input_feature,
      output_feature=output_feature)


def apply_transformations(
    key: Key,
    example: Example,
    transformations: List[ExampleTransformFn],
) -> KeyExample:
  for transform_fn in transformations:
    example = transform_fn(example)
  return key, example
