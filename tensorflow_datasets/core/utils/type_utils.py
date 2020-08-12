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

from typing import Dict, List, Tuple, TypeVar, Union

import tensorflow as tf

T = TypeVar('T')
TreeDict = Union[T, Dict[str, 'TreeDict']]  # pytype: disable=not-supported-yet
Tree = Union[T, List['Tree'], Tuple['Tree'], Dict[str, 'Tree']]  # pytype: disable=not-supported-yet

Tensor = Union[tf.Tensor, tf.SparseTensor, tf.RaggedTensor]
