# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Tests for feature."""

import tensorflow as tf
from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core.proto import feature_pb2


def test_to_shape_proto_single_dimension():
  shape = [1]
  shape_proto = feature.to_shape_proto(shape)
  assert shape_proto.dimensions == [1]


def test_to_shape_proto_single_zero_dimension():
  shape = [0]
  shape_proto = feature.to_shape_proto(shape)
  assert shape_proto.dimensions == [0]


def test_to_shape_proto_normal():
  shape = (28, 28, 1)
  shape_proto = feature.to_shape_proto(shape)
  assert shape_proto.dimensions == [28, 28, 1]


def test_to_shape_proto_unspecified():
  shape = (28, 28, None)
  shape_proto = feature.to_shape_proto(shape)
  assert shape_proto.dimensions == [28, 28, -1]


def test_from_shape_proto_single_dimension():
  shape_proto = feature_pb2.Shape(dimensions=[28])
  assert [28] == feature.from_shape_proto(shape_proto)


def test_from_shape_proto_single_zero_dimension():
  shape_proto = feature_pb2.Shape(dimensions=[0])
  assert [0] == feature.from_shape_proto(shape_proto)


def test_from_shape_proto_normal():
  shape_proto = feature_pb2.Shape(dimensions=[28, 28, 1])
  assert [28, 28, 1] == feature.from_shape_proto(shape_proto)


def test_from_shape_proto_unspecified():
  shape_proto = feature_pb2.Shape(dimensions=[28, 28, -1])
  assert [28, 28, None] == feature.from_shape_proto(shape_proto)


def test_encode_dtype():
  assert feature.encode_dtype(tf.int64) == 'int64'


def test_parse_dtype():
  assert feature.parse_dtype('int64') == tf.int64


def test_encode_and_parse_dtype():
  dtypes = [tf.int64, tf.string, tf.bfloat16, tf.bool]
  for dtype in dtypes:
    assert feature.parse_dtype(feature.encode_dtype(dtype)) == dtype


def test_tensor_info_tensor_shape():
  tensor_info = feature.TensorInfo(
      shape=tf.TensorShape([28, 28, 3]), dtype=tf.int64)
  assert tensor_info.shape == (28, 28, 3)


def test_tensor_info_tensor_shape_with_none():
  tensor_info = feature.TensorInfo(
      shape=tf.TensorShape([None, None, 3]), dtype=tf.int64)
  assert tensor_info.shape == (None, None, 3)


def test_tensor_info_list_shape():
  tensor_info = feature.TensorInfo(shape=[28, 28, 3], dtype=tf.int64)
  assert tensor_info.shape == (28, 28, 3)


def test_tensor_info_list_shape_with_none():
  tensor_info = feature.TensorInfo(shape=[None, None, 3], dtype=tf.int64)
  assert tensor_info.shape == (None, None, 3)
