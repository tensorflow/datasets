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

"""Tests for view_builder."""
from typing import Iterator, List

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import features as feature_lib
from tensorflow_datasets.core import transformation as transformation_lib
from tensorflow_datasets.core import view_builder


class Addition(transformation_lib.RowTransformation):

  def __init__(self, columns: List[str], delta: int):
    super().__init__(name="addition")
    self.columns = columns
    self.delta = delta

  def _transformed_column(self, column: str) -> str:
    return f"{column}_add"

  def output_features(
      self,
      input_features: feature_lib.FeaturesDict) -> feature_lib.FeaturesDict:
    output_features = dict(input_features)
    for column in self.columns:
      new_column = self._transformed_column(column)
      output_features[new_column] = feature_lib.Scalar(dtype=tf.int64)
    return feature_lib.FeaturesDict(output_features)

  def apply(
      self,
      key: transformation_lib.Key,
      example: transformation_lib.Example,
  ) -> Iterator[transformation_lib.KeyExample]:
    for column in self.columns:
      example[self._transformed_column(column)] = example[column] + self.delta
    yield key, example


class DummyMnistView(view_builder.ViewBuilder):
  VERSION = "1.0.0"
  BUILDER_CONFIGS = [
      view_builder.ViewConfig(
          name="add_hundred",
          input_dataset="dummy_mnist",
          view=Addition(columns=["label"], delta=100)),
      view_builder.ViewConfig(
          name="add_one",
          input_dataset="dummy_mnist",
          view=Addition(columns=["label"], delta=1))
  ]

  def _info(self) -> dataset_info.DatasetInfo:
    view_config = self.builder_config
    input_builder = view_config.input_dataset_builder(
        data_dir=self._data_dir_root)
    features = view_config.view.output_features(input_builder.info.features)
    return dataset_info.DatasetInfo(
        builder=self,
        features=features,
        description="Add one to label of dummy_mnist",
    )


def test_download_and_prepare():
  with tfds.testing.tmp_dir() as data_dir:
    dummy_mnist = tfds.testing.DummyMnist(data_dir=data_dir)
    dummy_mnist.download_and_prepare()

    add_hundred = DummyMnistView(config="add_hundred", data_dir=data_dir)
    add_hundred.download_and_prepare()

    ds_train = add_hundred.as_dataset(split="train")
    assert len(list(ds_train)) == 20
    for example in ds_train:
      assert example["label"] + 100 == example["label_add"]

    ds_test = add_hundred.as_dataset(split="test")
    assert len(list(ds_test)) == 20
    for example in ds_test:
      assert example["label"] + 100 == example["label_add"]

    add_one = DummyMnistView(config="add_one", data_dir=data_dir)
    add_one.download_and_prepare()
    ds_train_one = add_one.as_dataset(split="train")
    assert len(list(ds_train_one)) == 20
    for example in ds_train_one:
      assert example["label"] + 1 == example["label_add"]
