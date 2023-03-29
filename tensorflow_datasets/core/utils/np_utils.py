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

"""NumPy utils."""

from typing import Tuple

from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import type_utils


@py_utils.memoize()
def to_np_shape(shape: type_utils.Shape, replace_int=-1) -> Tuple[int]:
  return tuple(dim if dim is not None else replace_int for dim in shape)
