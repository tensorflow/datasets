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

"""Tests for huggingface_dataset_builder."""
import datetime
from unittest import mock

from absl import logging
import numpy as np
import pytest
import tensorflow as tf
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.dataset_builders import huggingface_dataset_builder


try:
  hf_datasets = lazy_imports_lib.lazy_imports.datasets
  _SKIP_TEST = False
except (ImportError, ModuleNotFoundError):
  # Some tests are only launched when `datasets` can be imported.
  _SKIP_TEST = True

skip_because_huggingface_cannot_be_imported = pytest.mark.skipif(
    _SKIP_TEST, reason="Hugging Face cannot be imported"
)


class FakeHfDatasets:

  def list_datasets(self):
    return ["mnist", "bigscience/P3", "x", "x/Y-z", "fashion_mnist"]


def test_from_hf_to_tfds():
  assert huggingface_dataset_builder.from_hf_to_tfds("x") == "x"
  assert huggingface_dataset_builder.from_hf_to_tfds("X") == "x"
  assert huggingface_dataset_builder.from_hf_to_tfds("x-y") == "x_y"
  assert huggingface_dataset_builder.from_hf_to_tfds("x/y") == "x__y"
  assert huggingface_dataset_builder.from_hf_to_tfds("x_v1.0") == "x_v1_0"


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
  assert huggingface_dataset_builder.convert_config_name(None) is None
  assert huggingface_dataset_builder.convert_config_name("x") == "x"
  assert huggingface_dataset_builder.convert_config_name("X") == "x"
  assert huggingface_dataset_builder.convert_config_name("X,y") == "x_y"


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
  assert huggingface_dataset_builder._convert_value(42, int64_feature) == 42

  int32_feature = feature_lib.Scalar(dtype=np.int32)
  assert huggingface_dataset_builder._convert_value(42, int32_feature) == 42

  string_feature = feature_lib.Scalar(dtype=np.object_)
  assert (
      huggingface_dataset_builder._convert_value("abc", string_feature) == "abc"
  )

  bool_feature = feature_lib.Scalar(dtype=np.bool_)
  assert huggingface_dataset_builder._convert_value(True, bool_feature)
  assert not huggingface_dataset_builder._convert_value(False, bool_feature)

  float_feature = feature_lib.Scalar(dtype=np.float32)
  assert huggingface_dataset_builder._convert_value(42.0, float_feature) == 42.0


def test_convert_value_sequence():
  sequence_feature = feature_lib.Sequence(feature=tf.int64)
  assert huggingface_dataset_builder._convert_value([42], sequence_feature) == [
      42
  ]
  assert huggingface_dataset_builder._convert_value(42, sequence_feature) == [
      42
  ]
  assert (
      huggingface_dataset_builder._convert_value(None, sequence_feature) == []  # pylint: disable=g-explicit-bool-comparison
  )


def test_convert_value_empty_sequence():
  assert huggingface_dataset_builder._convert_value(
      [None, "string"], feature_lib.Sequence(feature=np.str_)
  ) == [b"", "string"]


def test_convert_value_sequence_of_dict():
  sequence_feature = feature_lib.Sequence(
      {"someint": feature_lib.Scalar(dtype=np.str_)}
  )
  assert huggingface_dataset_builder._convert_value(
      {"someint": [None, "string", None]}, sequence_feature
  ) == {"someint": [b"", "string", b""]}


def test_convert_value_image():
  image_feature = feature_lib.Image()
  image = lazy_imports_lib.lazy_imports.PIL_Image.new(mode="RGB", size=(4, 4))
  assert huggingface_dataset_builder._convert_value(image, image_feature)


def test_convert_value_dict():
  translation_feature = feature_lib.Translation(languages=["en", "fr", "de"])
  translation = {
      "de": b"Hallo Welt",
      "en": b"Hello world",
      "fr": None,  # Hugging Face supports `None` values
  }
  assert huggingface_dataset_builder._convert_value(
      translation, translation_feature
  ) == {"de": b"Hallo Welt", "en": b"Hello world", "fr": b""}


def test_remove_empty_splits():
  splits = {"non_empty_split": range(5), "empty_split": range(0)}
  with mock.patch.object(logging, "log"):
    non_empty_splits = huggingface_dataset_builder._remove_empty_splits(splits)
    logging.log.assert_called_once_with(
        logging.WARNING,
        huggingface_dataset_builder._EMPTY_SPLIT_WARNING_MSG,
        "empty_split",
    )
  assert non_empty_splits.keys() == {"non_empty_split"}
  assert list(non_empty_splits["non_empty_split"]) == list(range(5))


@skip_because_huggingface_cannot_be_imported
def test_all_parameters_are_passed_down_to_hf():
  with mock.patch.object(
      lazy_imports_lib.lazy_imports.datasets, "load_dataset"
  ), mock.patch.object(
      lazy_imports_lib.lazy_imports.datasets, "load_dataset_builder"
  ) as load_dataset_builder_mock:
    load_dataset_builder_mock.return_value.info.citation = "citation"
    load_dataset_builder_mock.return_value.info.description = "description"
    load_dataset_builder_mock.return_value.info.supervised_keys = None
    load_dataset_builder_mock.return_value.info.version = "1.0.0"
    load_dataset_builder_mock.return_value.info.features = {
        "feature": hf_datasets.Value("int32")
    }
    huggingface_dataset_builder.login_to_hf = mock.MagicMock()

    builder = huggingface_dataset_builder.HuggingfaceDatasetBuilder(
        file_format="tfrecord",
        hf_repo_id="foo/bar",
        hf_config="config",
        ignore_verifications=True,
        data_dir="/path/to/data",
        hf_hub_token="SECRET_TOKEN",
        hf_num_proc=100,
        other_arg="this is another arg",
    )
    load_dataset_builder_mock.assert_called_once_with(
        "foo/bar", "config", other_arg="this is another arg"
    )

    builder._split_generators(None)
    huggingface_dataset_builder.login_to_hf.assert_called_once_with(
        "SECRET_TOKEN"
    )
    load_dataset_builder_mock.return_value.download_and_prepare.assert_called_once_with(
        verification_mode="all_checks", num_proc=100
    )
    load_dataset_builder_mock.return_value.as_dataset.assert_called_once_with(
        verification_mode="all_checks"
    )


# Encapsulate test parameters into a fixture to avoid `datasets` import during
# tests collection.
# https://docs.pytest.org/en/7.2.x/example/parametrize.html#deferring-the-setup-of-parametrized-resources
@pytest.fixture(params=["feat_dict", "audio"], name="features")
def get_features(request):
  datasets = pytest.importorskip(
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
          datasets.Features({
              "id": datasets.Value("string"),
              "meta": {
                  "left_context": datasets.Value("string"),
                  "partial_evidence": [{
                      "start_id": datasets.Value("int32"),
                      "meta": {"evidence_span": [datasets.Value("string")]},
                  }],
              },
          }),
          feature_lib.FeaturesDict({
              "id": feature_lib.Scalar(dtype=np.str_),
              "meta": feature_lib.FeaturesDict({
                  "left_context": feature_lib.Scalar(dtype=np.str_),
                  "partial_evidence": feature_lib.Sequence({
                      "meta": feature_lib.FeaturesDict({
                          "evidence_span": feature_lib.Sequence(
                              feature_lib.Scalar(dtype=np.str_)
                          ),
                      }),
                      "start_id": feature_lib.Scalar(dtype=np.int32),
                  }),
              }),
          }),
      ),
      "audio": (
          datasets.Audio(sampling_rate=48000),
          feature_lib.Audio(sample_rate=48000),
      ),
  }[request.param]


def test_extract_features(features):
  hf_features, tfds_features = features
  assert repr(
      huggingface_dataset_builder.extract_features(hf_features)
  ) == repr(tfds_features)


def test_default_value():
  assert (
      huggingface_dataset_builder._default_value(
          feature_lib.Scalar(dtype=np.int32)
      )
      == -2147483648
  )
  assert (
      huggingface_dataset_builder._default_value(
          feature_lib.Scalar(dtype=np.float32)
      )
      < -3.4028234e38
  )
  sequence = feature_lib.Sequence(np.int32)
  assert huggingface_dataset_builder._default_value(sequence) == []  # pylint: disable=g-explicit-bool-comparison
  features_dict = feature_lib.FeaturesDict({
      "foo": feature_lib.Scalar(dtype=np.str_),
  })
  assert huggingface_dataset_builder._default_value(features_dict) == {
      "foo": b""
  }
