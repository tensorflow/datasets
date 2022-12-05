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

import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets.core.utils import dtype_utils


@pytest.mark.parametrize('input_args,expected_output', [
    (np.int64, np.int64),
    (tf.int64, np.int64),
    (tf.string, np.object_),
    (np.str_, np.object_),
])
def test_tree_parallel_map(input_args, expected_output):
  assert dtype_utils.cast_to_numpy(input_args) == expected_output
