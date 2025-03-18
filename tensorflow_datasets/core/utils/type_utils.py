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

"""Typing annotation utils."""

import typing
from typing import Any, Type, TypeVar

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

_symbols_to_exclude = set(globals().keys())

T = TypeVar('T')

# Note: `TupleOrList` avoid abiguity from `Sequence` (`str` is `Sequence[str]`,
# `bytes` is `Sequence[int]`).
TupleOrList = tuple[T, ...] | list[T]
ListOrElem = T | list[T]

TreeDict = T | dict[str, 'TreeDict']
Tree = T | Any
ListOrTreeOrElem = T | TreeDict[T] | list[T]
NpArrayOrScalar = bytes | float | int | np.ndarray | str

if typing.TYPE_CHECKING:
  Tensor = tf.Tensor | tf.SparseTensor | tf.RaggedTensor
  TfdsDType = np.dtype | Type[np.generic] | tf.DType | tf.dtypes.DType
else:
  Tensor = Any
  TfdsDType = Any

# Nested dict of tensor
TensorDict = TreeDict[Tensor]
NpArrayOrScalarDict = TreeDict[NpArrayOrScalar]

Dim = int | None
Shape = TupleOrList[Dim]

JsonValue = (
    str | bool | int | float | None | list['JsonValue'] | dict[str, 'JsonValue']
)
Json = dict[str, JsonValue]

# Types for the tfrecord example construction.

Key = int | str | bytes
KeySerializedExample = tuple[Key, bytes]  # `(key, serialized_proto)`


__all__ = sorted(
    k
    for k in globals()
    if k not in _symbols_to_exclude and not k.startswith('_')
)
