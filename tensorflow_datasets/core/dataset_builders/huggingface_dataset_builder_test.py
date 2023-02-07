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
from unittest import mock

import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.dataset_builders import huggingface_dataset_builder


class FakeHfDatasets:

  def list_datasets(self):
    return ["mnist", "bigscience/P3", "x", "x/Y-z", "fashion_mnist"]


def test_from_hf_to_tfds():
  assert huggingface_dataset_builder._from_hf_to_tfds("x") == "x"
  assert huggingface_dataset_builder._from_hf_to_tfds("X") == "x"
  assert huggingface_dataset_builder._from_hf_to_tfds("x-y") == "x_y"
  assert huggingface_dataset_builder._from_hf_to_tfds("x/y") == "x__y"


@mock.patch.object(lazy_imports_lib.lazy_imports, "datasets", FakeHfDatasets())
def test_from_tfds_to_hf():
  assert huggingface_dataset_builder._from_tfds_to_hf("x") == "x"
  assert huggingface_dataset_builder._from_tfds_to_hf("X") == "x"
  assert (
      huggingface_dataset_builder._from_tfds_to_hf("bigscience__p3")
      == "bigscience/P3"
  )
  assert (
      huggingface_dataset_builder._from_tfds_to_hf("fashion_mnist")
      == "fashion_mnist"
  )
  assert huggingface_dataset_builder._from_tfds_to_hf("x__y_z") == "x/Y-z"
  with pytest.raises(
      registered.DatasetNotFoundError,
      match='"z" is not listed in Hugging Face datasets.',
  ):
    assert huggingface_dataset_builder._from_tfds_to_hf("z")


def test_convert_config_name():
  assert huggingface_dataset_builder._convert_config_name(None) is None
  assert huggingface_dataset_builder._convert_config_name("x") == "x"
  assert huggingface_dataset_builder._convert_config_name("X") == "x"


def test_convert_to_np_dtype():
  assert huggingface_dataset_builder._convert_to_np_dtype("bool_") == np.bool_
  assert huggingface_dataset_builder._convert_to_np_dtype("float") == np.float32
  assert (
      huggingface_dataset_builder._convert_to_np_dtype("double") == np.float64
  )
  assert (
      huggingface_dataset_builder._convert_to_np_dtype("large_string")
      == np.object_
  )
  assert (
      huggingface_dataset_builder._convert_to_np_dtype("string") == np.object_
  )
  assert huggingface_dataset_builder._convert_to_np_dtype("utf8") == np.object_
  assert huggingface_dataset_builder._convert_to_np_dtype("int32") == np.int32
  assert huggingface_dataset_builder._convert_to_np_dtype("int64") == np.int64
  assert huggingface_dataset_builder._convert_to_np_dtype("int64") == tf.int64
  assert (
      huggingface_dataset_builder._convert_to_np_dtype("timestamp[s, tz=UTC]")
      == np.int64
  )
  with pytest.raises(ValueError, match="Unrecognized type.+"):
    huggingface_dataset_builder._convert_to_np_dtype("I am no dtype")


def test_convert_value_datetime():
  feature = feature_lib.Scalar(dtype=np.int64)
  epoch_start = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
  assert huggingface_dataset_builder._convert_value(epoch_start, feature) == 0
  assert (
      huggingface_dataset_builder._convert_value(
          datetime.datetime(1970, 1, 2, tzinfo=datetime.timezone.utc), feature
      )
      == 86400
  )


def test_convert_value_scalar():
  int64_feature = feature_lib.Scalar(dtype=np.int64)
  assert huggingface_dataset_builder._convert_value(None, int64_feature) == 0
  assert huggingface_dataset_builder._convert_value(42, int64_feature) == 42

  int32_feature = feature_lib.Scalar(dtype=np.int32)
  assert huggingface_dataset_builder._convert_value(None, int32_feature) == 0
  assert huggingface_dataset_builder._convert_value(42, int32_feature) == 42

  string_feature = feature_lib.Scalar(dtype=np.object_)
  assert not huggingface_dataset_builder._convert_value(None, string_feature)
  assert (
      huggingface_dataset_builder._convert_value("abc", string_feature) == "abc"
  )

  bool_feature = feature_lib.Scalar(dtype=np.bool_)
  assert not huggingface_dataset_builder._convert_value(None, bool_feature)
  assert huggingface_dataset_builder._convert_value(True, bool_feature)
  assert not huggingface_dataset_builder._convert_value(False, bool_feature)

  float_feature = feature_lib.Scalar(dtype=np.float32)
  assert huggingface_dataset_builder._convert_value(None, float_feature) == 0.0
  assert huggingface_dataset_builder._convert_value(42.0, float_feature) == 42.0


def test_convert_value_sequence():
  sequence_feature = feature_lib.Sequence(feature=tf.int64)
  assert huggingface_dataset_builder._convert_value([42], sequence_feature) == [
      42
  ]
  assert huggingface_dataset_builder._convert_value(42, sequence_feature) == [
      42
  ]


def test_convert_value_image():
  image_feature = feature_lib.Image()
  image = lazy_imports_lib.lazy_imports.PIL_Image.new(mode="RGB", size=(4, 4))
  assert huggingface_dataset_builder._convert_value(image, image_feature)


# Encapsulate test parameters into a fixture to avoid `datasets` import during
# tests collection.
# https://docs.pytest.org/en/7.2.x/example/parametrize.html#deferring-the-setup-of-parametrized-resources
@pytest.fixture(params=["feat_dict", "audio"], name="features")
def get_features(request):
  hf_datasets = pytest.importorskip(
      "datasets",
      reason=(
          "`datasets` library has to be installed separately for Python >= 3.10"
          " due to conflicts between `multiprocess` and `apache-beam`"
          " libraries. See"
          " https://github.com/uqfoundation/multiprocess/issues/125"
      ),
  )

  return {
      "feat_dict": (
          hf_datasets.Features({
              "id": hf_datasets.Value("string"),
              "meta": {
                  "left_context": hf_datasets.Value("string"),
                  "partial_evidence": [{
                      "start_id": hf_datasets.Value("int32"),
                      "meta": {"evidence_span": [hf_datasets.Value("string")]},
                  }],
              },
          }),
          feature_lib.FeaturesDict({
              "id": feature_lib.Scalar(dtype=np.str_),
              "meta": feature_lib.FeaturesDict({
                  "left_context": feature_lib.Scalar(dtype=np.str_),
                  "partial_evidence": feature_lib.Sequence({
                      "meta": feature_lib.FeaturesDict(
                          {
                              "evidence_span": feature_lib.Sequence(
                                  feature_lib.Scalar(dtype=np.str_)
                              ),
                          }
                      ),
                      "start_id": feature_lib.Scalar(dtype=np.int32),
                  }),
              }),
          }),
      ),
      "audio": (
          hf_datasets.Audio(sampling_rate=48000),
          feature_lib.Audio(sample_rate=48000),
      ),
  }[request.param]


def test_extract_features(features):
  hf_features, tfds_features = features
  assert repr(
      huggingface_dataset_builder.extract_features(hf_features)
  ) == repr(tfds_features)
