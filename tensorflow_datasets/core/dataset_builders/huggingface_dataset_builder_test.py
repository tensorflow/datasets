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

from unittest import mock

from absl import logging
import datasets as hf_datasets
import pytest
from tensorflow_datasets.core import registered
from tensorflow_datasets.core.dataset_builders import huggingface_dataset_builder


@mock.patch.object(
    hf_datasets,
    "list_datasets",
    return_value=["mnist", "bigscience/P3", "x", "x/Y-z", "fashion_mnist"],
)
def test_from_tfds_to_hf(_):
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


@pytest.fixture(name="load_dataset_builder_mock")
def get_load_dataset_builder_mock():
  with mock.patch.object(
      hf_datasets, "load_dataset_builder"
  ) as load_dataset_builder_mock:
    hf_builder = load_dataset_builder_mock.return_value
    hf_builder.info.citation = "citation"
    hf_builder.info.description = "description"
    hf_builder.info.features = None
    hf_builder.info.splits = ["all"]
    hf_builder.info.supervised_keys = None
    hf_builder.info.version = "1.0.0"

    dataset = mock.MagicMock()
    dataset.info.features = {"feature": hf_datasets.Value("int32")}
    dataset_dict = hf_datasets.DatasetDict({"test": dataset})
    hf_builder.as_dataset.return_value = dataset_dict
    yield load_dataset_builder_mock


@pytest.fixture(name="builder")
def get_huggingface_dataset_builder_mock(load_dataset_builder_mock):
  with mock.patch.object(
      huggingface_dataset_builder, "login_to_hf"
  ) as login_to_hf_mock:
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
    login_to_hf_mock.assert_called_once_with("SECRET_TOKEN")
    yield builder


def test_all_parameters_are_passed_down_to_hf(
    load_dataset_builder_mock, builder
):
  builder._split_generators(None)
  load_dataset_builder_mock.return_value.download_and_prepare.assert_called_once_with(
      verification_mode="all_checks", num_proc=100
  )
  load_dataset_builder_mock.return_value.as_dataset.assert_called_once_with(
      verification_mode="all_checks"
  )


def test_hf_features(builder):
  assert builder._hf_features() == {"feature": hf_datasets.Value("int32")}
