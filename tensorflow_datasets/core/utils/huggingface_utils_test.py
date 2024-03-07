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
from tensorflow_datasets.core.utils import huggingface_utils
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf


def test_convert_to_np_dtype_raises():
  with pytest.raises(ValueError, match='Unrecognized type.+'):
    huggingface_utils.convert_to_np_dtype('I am no dtype')


@pytest.mark.parametrize(
    'hf_dtype,np_dtype',
    [
        # from mapping
        ('bool', np.bool_),
        ('float', np.float32),
        ('double', np.float64),
        ('large_string', np.object_),
        ('utf8', np.object_),
        ('string', np.object_),
        # from np
        ('bool_', np.bool_),
        ('int32', np.int32),
        ('int64', np.int64),
        # from timestamp
        ('timestamp[s, tz=UTC]', np.int64),
        # from tf
        ('bfloat16', tf.bfloat16),
    ],
)
def test_convert_to_np_dtype(hf_dtype, np_dtype):
  assert huggingface_utils.convert_to_np_dtype(hf_dtype) is np_dtype
