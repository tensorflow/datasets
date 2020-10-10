# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

import os
from typing import Dict, List, Optional, Tuple, TypeVar, Union

import tensorflow as tf

# Accept both `str` and `pathlib.Path`-like
PathLike = Union[str, os.PathLike]

T = TypeVar('T')

# Note: `TupleOrList` avoid abiguity from `Sequence` (`str` is `Sequence[str]`,
# `bytes` is `Sequence[int]`).
TupleOrList = Union[Tuple[T, ...], List[T]]

TreeDict = Union[T, Dict[str, 'TreeDict']]  # pytype: disable=not-supported-yet
Tree = Union[T, TupleOrList['Tree'], Dict[str, 'Tree']]  # pytype: disable=not-supported-yet


Tensor = Union[tf.Tensor, tf.SparseTensor, tf.RaggedTensor]

Dim = Optional[int]
Shape = TupleOrList[Dim]

JsonValue = Union[
    str, bool, int, float, None, List['JsonValue'], Dict[str, 'JsonValue'],  # pytype: disable=not-supported-yet
]
Json = Dict[str, JsonValue]
