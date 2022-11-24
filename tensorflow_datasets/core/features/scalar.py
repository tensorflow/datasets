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

"""Scalar feature, e.g. tf.int32."""

from __future__ import annotations

from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import tensor_feature
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import type_utils


class Scalar(tensor_feature.Tensor):
  """A scalar feature of a particular dtype (e.g.

  np.int64 or np.float).

  Equivalent to `tfds.features.Tensor(shape=(), dtype=dtype)`.

  """

  def __init__(
      self,
      dtype: type_utils.TfdsDType,
      *,
      doc: feature_lib.DocArg = None,
  ):
    super().__init__(shape=(), dtype=dtype, doc=doc)

  @classmethod
  def from_json_content(cls, value: feature_pb2.TensorFeature) -> 'Scalar':
    return cls(dtype=feature_lib.dtype_from_str(value.dtype))
