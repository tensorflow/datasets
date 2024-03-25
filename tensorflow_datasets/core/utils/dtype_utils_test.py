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

import numpy as np
import pytest
from tensorflow_datasets.core.utils import dtype_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


@pytest.mark.parametrize(
    'input_args,expected_output',
    [
        (np.int64, np.int64),
        (tf.int64, np.int64),
        (np.float64, np.float64),
        (tf.float64, np.float64),
        (tf.string, np.object_),
        (np.uint8, np.uint8),
        (tf.uint8, np.uint8),
    ],
)
def test_cast_to_numpy(input_args, expected_output):
  assert dtype_utils.cast_to_numpy(input_args) == expected_output


@pytest.mark.parametrize(
    'fn,dtype,result',
    [
        (dtype_utils.is_integer, np.int32, True),
        (dtype_utils.is_integer, np.int64, True),
        (dtype_utils.is_integer, np.float32, False),
        (dtype_utils.is_integer, tf.int32, True),
        (dtype_utils.is_integer, tf.int64, True),
        (dtype_utils.is_integer, tf.float32, False),
        (dtype_utils.is_integer, np.uint8, True),
        (dtype_utils.is_integer, tf.uint8, True),
        (dtype_utils.is_bool, np.bool_, True),
        (dtype_utils.is_bool, np.int32, False),
        (dtype_utils.is_bool, tf.bool, True),
        (dtype_utils.is_bool, tf.int32, False),
        (dtype_utils.is_floating, np.float32, True),
        (dtype_utils.is_floating, np.float64, True),
        (dtype_utils.is_floating, np.int32, False),
        (dtype_utils.is_floating, np.int64, False),
        (dtype_utils.is_floating, tf.float32, True),
        (dtype_utils.is_floating, tf.float64, True),
        (dtype_utils.is_floating, tf.int32, False),
        (dtype_utils.is_floating, tf.int64, False),
        (dtype_utils.is_string, np.str_, True),
        (dtype_utils.is_string, np.int32, False),
        (dtype_utils.is_string, tf.string, True),
        (dtype_utils.is_string, tf.int32, False),
        (dtype_utils.is_string, np.uint8, False),
        (dtype_utils.is_string, tf.uint8, False),
    ],
)
def test_dtype(fn, dtype, result):
  assert fn(dtype) == result


def test_is_np_sub_dtype():
  assert dtype_utils.is_np_sub_dtype(np.int32, np.integer)
  assert dtype_utils.is_np_sub_dtype(np.int64, np.integer)
  assert dtype_utils.is_np_sub_dtype(float, np.floating)
  assert not dtype_utils.is_np_sub_dtype(np.int64, np.floating)
  assert not dtype_utils.is_np_sub_dtype(float, np.integer)
  assert dtype_utils.is_np_sub_dtype(np.uint8, np.integer)


def test_is_same_dtype_type():
  assert dtype_utils.is_same_dtype_type(np.int32, tf.int32)
  assert not dtype_utils.is_same_dtype_type(np.int32, np.int64)
  assert dtype_utils.is_same_dtype_type(np.dtype('<U15'), np.dtype('<U0'))
