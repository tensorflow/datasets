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

"""Tests for feature."""

import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets.core.features import feature
from tensorflow_datasets.core.features import image_feature
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


def test_dtype_to_str():
  assert feature.dtype_to_str(np.int64) == "int64"
  assert feature.dtype_to_str(np.uint8) == "uint8"


def test_dtype_from_str():
  assert feature.dtype_from_str("int64") == np.int64
  assert feature.dtype_from_str("uint8") == np.uint8


def test_dtype_for_string_types():
  assert feature.dtype_from_str("str") == np.object_
  assert feature.dtype_from_str("string") == np.object_
  assert feature.dtype_to_str(np.str_) == "string"
  assert feature.dtype_to_str(np.object_) == "string"
  assert feature.dtype_to_str(tf.string) == "string"


def test_encode_and_dtype_from_str():
  dtypes = [
      tf.int64,
      tf.string,
      tf.bfloat16,
      tf.bool,
      np.int64,
      np.bool_,
      np.object_,
      np.uint8,
  ]
  for dtype in dtypes:
    assert feature.dtype_from_str(feature.dtype_to_str(dtype)) == dtype


@pytest.mark.parametrize(
    ["json"],
    [
        (
            {
                "type": "tensorflow_datasets.core.features.image_feature.Image",
                "content": {
                    "shape": [128, 128, 1],
                    "dtype": "uint8",
                    "encoding_format": None,
                    "use_colormap": False,
                },
            },
        ),
        (
            {
                "type": "tensorflow_datasets.core.features.labeled_image.LabeledImage",
                "content": {
                    "shape": [128, 128, 1],
                    "dtype": "uint8",
                    "encoding_format": None,
                    "labels": 2,
                },
            },
        ),
    ],
)
def test_feature_from_json(json):
  feature_connector = feature.FeatureConnector.from_json(json)
  assert isinstance(feature_connector, image_feature.Image)
  assert feature_connector.dtype == np.uint8
  assert feature_connector.shape == (128, 128, 1)


@pytest.mark.parametrize(["dtype"], [(np.int64,), (tf.int64,)])
def test_tensor_info_tensor_shape(dtype):
  tensor_shape = tf.TensorShape([28, 28, 3])
  tensor_info = feature.TensorInfo(shape=tensor_shape, dtype=dtype)
  assert tensor_info.shape == (28, 28, 3)
  assert tensor_info.to_tensor_spec() == tf.TensorSpec(
      shape=tensor_shape, dtype=np.int64
  )


@pytest.mark.parametrize(["dtype"], [(np.int64,), (tf.int64,)])
def test_tensor_info_tensor_shape_with_none(dtype):
  tensor_shape = tf.TensorShape([None, None, 3])
  tensor_info = feature.TensorInfo(shape=tensor_shape, dtype=dtype)
  assert tensor_info.shape == (None, None, 3)
  assert tensor_info.to_tensor_spec() == tf.TensorSpec(
      shape=tensor_shape, dtype=np.int64
  )


@pytest.mark.parametrize(["dtype"], [(np.int64,), (tf.int64,)])
def test_tensor_info_list_shape(dtype):
  tensor_info = feature.TensorInfo(shape=[28, 28, 3], dtype=dtype)
  assert tensor_info.shape == (28, 28, 3)


@pytest.mark.parametrize(["dtype"], [(np.int64,), (tf.int64,)])
def test_tensor_info_list_shape_with_none(dtype):
  tensor_info = feature.TensorInfo(shape=[None, None, 3], dtype=dtype)
  assert tensor_info.shape == (None, None, 3)


@pytest.mark.parametrize(
    ["feature_name", "parent_name", "expected"],
    [
        ("a", None, "a"),
        ("a/b", None, "a.b"),
        ("a", "b", "b-a"),
        ("a/b", "c/d", "c-d-a.b"),
    ],
)
def test_convert_feature_name_to_filename(feature_name, parent_name, expected):
  assert (
      feature.convert_feature_name_to_filename(
          feature_name=feature_name, parent_name=parent_name
      )
      == expected
  )


def test_feature_repr():
  json = {
      "description": "Image encoded as JPEG.",
      "image": {
          "dtype": "uint8",
          "encodingFormat": "jpeg",
          "shape": {"dimensions": ["-1", "-1", "3"]},
      },
      "pythonClassName": (
          "tensorflow_datasets.core.features.image_feature.Image"
      ),
  }
  feature_connector = feature.FeatureConnector.from_json(json)
  expected_feature_connector_repr = (
      "Image(shape=(None, None, 3), dtype=uint8, description=Image encoded as"
      " JPEG.)"
  )
  assert str(feature_connector) == expected_feature_connector_repr


def test_tensor_info_repr():
  tensor_info = feature.TensorInfo(
      shape=(), dtype=np.int32, minimum=1, maximum=42
  )
  assert (
      str(tensor_info)
      == "TensorInfo(shape=(), dtype=int32, minimum=1, maximum=42)"
  )
  tensor_info = feature.TensorInfo(shape=(), dtype=np.int32)
  assert str(tensor_info) == "TensorInfo(shape=(), dtype=int32)"
  tensor_info = feature.TensorInfo(shape=(), dtype=np.int32, optional=True)
  assert str(tensor_info) == "TensorInfo(shape=(), dtype=int32, optional=True)"
