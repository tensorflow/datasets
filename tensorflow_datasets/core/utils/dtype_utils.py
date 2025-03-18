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

"""TFDS DType utils to handle both NumPy and TensorFlow DTypes."""

from typing import cast, Any, List, Type, Union

from absl import logging
from etils import enp
import numpy as np
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

TfdsDType = type_utils.TfdsDType


@py_utils.memoize()
def cast_to_numpy(dtype: type_utils.TfdsDType) -> np.dtype:
  """Casts any np.dtype or tf.dtypes.DType to np.dtype.

  Args:
    dtype: input DType.

  Returns:
    Equivalent NumPy DType.
  """
  tf_already_loaded = enp.lazy.has_tf
  if tf_already_loaded and isinstance(dtype, tf.dtypes.DType):
    np_dtype = np.dtype(dtype.as_numpy_dtype)
    logging.log_first_n(
        logging.WARNING,
        (
            f'You use TensorFlow DType {dtype} in tfds.features '
            'This will soon be deprecated in favor of NumPy DTypes. '
            f'In the meantime it was converted to {np_dtype}.'
        ),
        10,
    )
    return np_dtype
  # Strings are managed as np.object_ (rather than np.str_) in order to
  # optimize for memory and for consistency with tf.string:
  # np.array(['', '1234567890'], dtype=np.str_).nbytes == 80
  # np.array(['', '1234567890'], dtype=np.object_).nbytes == 16
  if is_string(dtype):
    return np.dtype(np.object_)
  return cast(np.dtype, dtype)


def is_np_or_tf_dtype(value: Any) -> bool:
  """Returns True is the given value is a NumPy or TensorFlow dtype."""
  return enp.lazy.is_np_dtype(value) or enp.lazy.is_tf_dtype(value)


def _is_dtype(
    numpy_dtypes: List[Union[np.dtype, Type[np.generic]]],
    tf_dtype: Any,
    dtype: TfdsDType,
) -> bool:
  if enp.lazy.is_np_dtype(dtype):
    return any(
        [is_np_sub_dtype(dtype, numpy_dtype) for numpy_dtype in numpy_dtypes]
    )
  if enp.lazy.has_tf and isinstance(dtype, tf.dtypes.DType):
    if isinstance(tf_dtype, str):
      return getattr(dtype, tf_dtype)
    return dtype == tf_dtype
  raise TypeError(f'type {dtype} ({type(dtype)}) not recognized')


@py_utils.memoize()
def is_bool(dtype: TfdsDType) -> bool:
  return _is_dtype([np.bool_], 'is_bool', dtype)


@py_utils.memoize()
def is_floating(dtype: TfdsDType) -> bool:
  return _is_dtype([np.floating], 'is_floating', dtype)


@py_utils.memoize()
def is_integer(dtype: TfdsDType) -> bool:
  return _is_dtype([np.integer], 'is_integer', dtype)


@py_utils.memoize()
def is_string(dtype: TfdsDType) -> bool:
  return _is_dtype([np.character, np.object_], np.object_, dtype)


@py_utils.memoize()
def is_same_dtype_type(a, b):
  if a == b:
    return True
  # NumPy strings can have different DTypes and yet be of the same DType type.
  return is_string(a) and is_string(b)


@py_utils.memoize()
def is_np_sub_dtype(value: np.dtype, super_type: np.dtype) -> bool:
  try:
    return np.issubdtype(value, super_type)
  except TypeError:
    return False
