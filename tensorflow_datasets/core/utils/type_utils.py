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

"""Typing annotation utils."""

import typing
from typing import cast, Any, Dict, List, Optional, Tuple, TypeVar, Union

from etils import enp
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

_symbols_to_exclude = set(globals().keys())

T = TypeVar('T')

# Note: `TupleOrList` avoid abiguity from `Sequence` (`str` is `Sequence[str]`,
# `bytes` is `Sequence[int]`).
TupleOrList = Union[Tuple[T, ...], List[T]]
ListOrElem = Union[T, List[T]]

TreeDict = Union[T, Dict[str, 'TreeDict']]  # pytype: disable=not-supported-yet
Tree = Union[T, Any]

if typing.TYPE_CHECKING:
  Tensor = Union[tf.Tensor, tf.SparseTensor, tf.RaggedTensor]
else:
  Tensor = Any

# Nested dict of tensor
TensorDict = TreeDict[Tensor]

Dim = Optional[int]
Shape = TupleOrList[Dim]

JsonValue = Union[str, bool, int, float, None, List['JsonValue'],
                  Dict[str, 'JsonValue'],  # pytype: disable=not-supported-yet
                 ]
Json = Dict[str, JsonValue]

# Types for the tfrecord example construction.

Key = Union[int, str, bytes]
KeySerializedExample = Tuple[Key, bytes]  # `(key, serialized_proto)`

TfdsDType = Union[np.dtype, tf.DType, tf.dtypes.DType]


def cast_to_numpy(dtype: TfdsDType) -> np.dtype:
  """Casts any np.dtype or tf.dtypes.DType to np.dtype.

  Args:
    dtype: input DType.

  Returns:
    Equivalent NumPy DType.
  """
  tf_already_loaded = enp.lazy.has_tf
  if tf_already_loaded and isinstance(dtype, tf.dtypes.DType):
    if dtype == tf.string:
      numpy_dtype = np.object_
    else:
      numpy_dtype = dtype.as_numpy_dtype
    return numpy_dtype
  return cast(np.dtype, dtype)


__all__ = sorted(k for k in globals()
                 if k not in _symbols_to_exclude and not k.startswith('_'))
