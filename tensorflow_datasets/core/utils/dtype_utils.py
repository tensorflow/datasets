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

"""TFDS DType utils to handle both NumPy and TensorFlow DTypes."""

from typing import cast

from etils import enp
import numpy as np
from tensorflow_datasets.core.utils import tf_utils
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


def cast_to_numpy(dtype: type_utils.TfdsDType) -> np.dtype:
  """Casts any np.dtype or tf.dtypes.DType to np.dtype.

  Args:
    dtype: input DType.

  Returns:
    Equivalent NumPy DType.
  """
  tf_already_loaded = enp.lazy.has_tf
  if tf_already_loaded and isinstance(dtype, tf.dtypes.DType):
    return np.dtype(dtype.as_numpy_dtype)
  # Strings are managed as np.object_ (rather than np.str_) in order to
  # optimize for memory and for consistency with tf.string:
  # np.array(['', '1234567890'], dtype=np.str_).nbytes == 80
  # np.array(['', '1234567890'], dtype=np.object_).nbytes == 16
  if tf_utils.is_string(dtype):
    return np.object_
  return cast(np.dtype, dtype)
