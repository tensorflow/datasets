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

"""Tests for huggingface_dataset_builder."""
import datetime

import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core.dataset_builders import huggingface_dataset_builder


def test_convert_dataset_name():
  assert huggingface_dataset_builder._convert_dataset_name("x") == "x"
  assert huggingface_dataset_builder._convert_dataset_name("X") == "x"
  assert huggingface_dataset_builder._convert_dataset_name("x-y") == "x_y"
  assert huggingface_dataset_builder._convert_dataset_name("x/y") == "x__y"


def test_convert_config_name():
  assert huggingface_dataset_builder._convert_config_name("x") == "x"
  assert huggingface_dataset_builder._convert_config_name("X") == "x"


def test_convert_to_np_dtype():
  assert huggingface_dataset_builder._convert_to_np_dtype("bool_") == np.bool_
  assert huggingface_dataset_builder._convert_to_np_dtype("float") == np.float32
  assert huggingface_dataset_builder._convert_to_np_dtype(
      "double") == np.float64
  assert huggingface_dataset_builder._convert_to_np_dtype(
      "large_string") == np.object_
  assert huggingface_dataset_builder._convert_to_np_dtype("utf8") == np.object_
  assert huggingface_dataset_builder._convert_to_np_dtype("int32") == np.int32
  assert huggingface_dataset_builder._convert_to_np_dtype("int64") == np.int64
  assert huggingface_dataset_builder._convert_to_np_dtype(
      "timestamp[s, tz=UTC]") == np.int64
  with pytest.raises(ValueError, match="Unrecognized type.+"):
    huggingface_dataset_builder._convert_to_np_dtype("I am no dtype")


def test_convert_value_datetime():
  feature = feature_lib.Scalar(dtype=np.int64)
  epoch_start = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
  assert huggingface_dataset_builder._convert_value(epoch_start, feature) == 0
  assert huggingface_dataset_builder._convert_value(
      datetime.datetime(1970, 1, 2, tzinfo=datetime.timezone.utc),
      feature) == 86400


def test_convert_value_scalar():
  int64_feature = feature_lib.Scalar(dtype=np.int64)
  assert huggingface_dataset_builder._convert_value(None, int64_feature) == 0
  assert huggingface_dataset_builder._convert_value(42, int64_feature) == 42

  int32_feature = feature_lib.Scalar(dtype=np.int32)
  assert huggingface_dataset_builder._convert_value(None, int32_feature) == 0
  assert huggingface_dataset_builder._convert_value(42, int32_feature) == 42

  string_feature = feature_lib.Scalar(dtype=np.object_)
  assert not huggingface_dataset_builder._convert_value(None, string_feature)
  assert huggingface_dataset_builder._convert_value("abc",
                                                    string_feature) == "abc"

  bool_feature = feature_lib.Scalar(dtype=np.bool_)
  assert not huggingface_dataset_builder._convert_value(None, bool_feature)
  assert huggingface_dataset_builder._convert_value(True, bool_feature)
  assert not huggingface_dataset_builder._convert_value(False, bool_feature)

  float_feature = feature_lib.Scalar(dtype=np.float32)
  assert huggingface_dataset_builder._convert_value(None, float_feature) == 0.0
  assert huggingface_dataset_builder._convert_value(42.0, float_feature) == 42.0


def test_convert_value_sequence():
  sequence_feature = feature_lib.Sequence(feature=tf.int64)
  assert huggingface_dataset_builder._convert_value([42],
                                                    sequence_feature) == [42]
  assert huggingface_dataset_builder._convert_value(42,
                                                    sequence_feature) == [42]


def test_convert_value_image():
  image_feature = feature_lib.Image()
  image = lazy_imports_lib.lazy_imports.PIL_Image.new(mode="RGB", size=(4, 4))
  assert huggingface_dataset_builder._convert_value(image, image_feature)
