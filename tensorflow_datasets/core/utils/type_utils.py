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

"""Typing annotation utils."""

import typing
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

_symbols_to_exclude = set(globals().keys())

T = TypeVar('T')

# Note: `TupleOrList` avoid abiguity from `Sequence` (`str` is `Sequence[str]`,
# `bytes` is `Sequence[int]`).
TupleOrList = Union[Tuple[T, ...], List[T]]
ListOrElem = Union[T, List[T]]

TreeDict = Union[T, Dict[str, 'TreeDict']]
Tree = Union[T, Any]
ListOrTreeOrElem = Union[T, TreeDict[T], List[T]]
NpArrayOrScalar = Union[bytes, float, int, np.ndarray, str]

if typing.TYPE_CHECKING:
  Tensor = Union[tf.Tensor, tf.SparseTensor, tf.RaggedTensor]
  TfdsDType = Union[np.dtype, Type[np.generic], tf.DType, tf.dtypes.DType]
else:
  Tensor = Any
  TfdsDType = Any

# Nested dict of tensor
TensorDict = TreeDict[Tensor]
NpArrayOrScalarDict = TreeDict[NpArrayOrScalar]

Dim = Optional[int]
Shape = TupleOrList[Dim]

JsonValue = Union[
    str,
    bool,
    int,
    float,
    None,
    List['JsonValue'],
    Dict[str, 'JsonValue'],  # pytype: disable=not-supported-yet
]
Json = Dict[str, JsonValue]

# Types for the tfrecord example construction.

Key = Union[int, str, bytes]
KeySerializedExample = Tuple[Key, bytes]  # `(key, serialized_proto)`


__all__ = sorted(
    k
    for k in globals()
    if k not in _symbols_to_exclude and not k.startswith('_')
)
