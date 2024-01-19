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

"""Tests for view_builder."""
import functools

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.core.dataset_builders import view_builder


def add_number(number: int, increment: int) -> int:
  return number + increment


def is_even(number: int) -> bool:
  return number % 2 == 0


_MNIST_TRANSFORMATIONS = [
    tfds.transform.remove_feature(feature_name="image"),
    tfds.transform.apply_filter(fn=is_even, input_feature="label"),
    tfds.transform.apply_fn(
        fn=functools.partial(add_number, increment=10),
        input_feature="label",
        output_feature="label_plus_10",
    ),
    tfds.transform.apply_fn(
        fn=functools.partial(add_number, increment=2),
        input_feature="label",
        output_feature="label_plus_2",
    ),
]

_TRANSFORMED_MNIST_FEATURES = tfds.features.FeaturesDict({
    "label": tfds.features.ClassLabel(num_classes=10),
    "label_plus_10": tfds.features.Scalar(dtype=tf.int64),
    "label_plus_2": tfds.features.Scalar(dtype=tf.int64),
})


def add_number_map_fn(
    dataset: tf.data.Dataset,
    increment: int,
    input_name: str,
    output_name: str,
) -> tf.data.Dataset:
  def f(ex):
    ex[output_name] = ex[input_name] + increment
    return ex

  return dataset.map(f)


def remove_feature_map_fn(
    dataset: tf.data.Dataset,
    feature_name: str,
) -> tf.data.Dataset:
  def f(ex):
    del ex[feature_name]
    return ex

  return dataset.map(f)


_MNIST_DATASET_TRANSFORMATIONS = [
    functools.partial(
        add_number_map_fn,
        increment=10,
        input_name="label",
        output_name="label_plus_10",
    ),
    functools.partial(
        add_number_map_fn,
        increment=2,
        input_name="label",
        output_name="label_plus_2",
    ),
    functools.partial(remove_feature_map_fn, feature_name="image"),
]


class DummyMnistViewWithoutConfigs(view_builder.ViewBuilder):
  VERSION = "1.0.0"
  INPUT_DATASET = "dummy_mnist"
  EX_TRANSFORMATIONS = _MNIST_TRANSFORMATIONS

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        features=_TRANSFORMED_MNIST_FEATURES,
        description="A different view on Mnist.",
    )


class DummyMnistViewWithConfigs(view_builder.ViewBuilder):
  VERSION = "1.0.0"
  BUILDER_CONFIGS = [
      view_builder.ViewConfig(
          name="add_stuff",
          input_dataset="dummy_mnist",
          ex_transformations=_MNIST_TRANSFORMATIONS,
      )
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        features=_TRANSFORMED_MNIST_FEATURES,
        description="A different view on Mnist.",
    )


class BeamDummyMnistViewWithConfigs(view_builder.ViewBuilder):
  VERSION = "1.0.0"
  BUILDER_CONFIGS = [
      view_builder.ViewConfig(
          name="add_stuff",
          input_dataset="dummy_mnist",
          ex_transformations=_MNIST_TRANSFORMATIONS,
      )
  ]
  USE_BEAM = True

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        features=_TRANSFORMED_MNIST_FEATURES,
        description="A different view on Mnist.",
    )


class DummyMnistViewDatasetTransform(view_builder.ViewBuilder):
  VERSION = "1.0.0"
  BUILDER_CONFIGS = [
      view_builder.ViewConfig(
          name="add_stuff",
          input_dataset="dummy_mnist",
          ds_transformations=_MNIST_DATASET_TRANSFORMATIONS,
      )
  ]

  def _info(self):
    return tfds.core.DatasetInfo(
        builder=self,
        features=_TRANSFORMED_MNIST_FEATURES,
        description="A different view on Mnist.",
    )


def test_view_builder_with_configs_load():
  with tfds.testing.tmp_dir() as data_dir:
    tfds.testing.DummyMnist(data_dir=data_dir).download_and_prepare()

    ds_train = tfds.load(
        "dummy_mnist_view_with_configs", split="train", data_dir=data_dir
    )
    assert len(list(ds_train)) == 10
    for example in ds_train:
      assert example["label"] + 10 == example["label_plus_10"]
      assert example["label"] + 2 == example["label_plus_2"]


def test_beam_view_builder_with_configs_load():
  with tfds.testing.tmp_dir() as data_dir:
    tfds.testing.DummyMnist(data_dir=data_dir).download_and_prepare()

    ds_train = tfds.load(
        "beam_dummy_mnist_view_with_configs", split="train", data_dir=data_dir
    )
    assert len(list(ds_train)) == 10
    for example in ds_train:
      assert example["label"] + 10 == example["label_plus_10"]
      assert example["label"] + 2 == example["label_plus_2"]


def test_view_builder_without_configs_load():
  with tfds.testing.tmp_dir() as data_dir:
    tfds.testing.DummyMnist(data_dir=data_dir).download_and_prepare()

    ds_train = tfds.load(
        "dummy_mnist_view_without_configs", split="train", data_dir=data_dir
    )
    assert len(list(ds_train)) == 10
    for example in ds_train:
      assert example["label"] + 10 == example["label_plus_10"]
      assert example["label"] + 2 == example["label_plus_2"]


def test_view_builder_tf_dataset_with_configs_load():
  with tfds.testing.tmp_dir() as data_dir:
    tfds.testing.DummyMnist(data_dir=data_dir).download_and_prepare()

    ds_train = tfds.load(
        "dummy_mnist_view_dataset_transform", split="train", data_dir=data_dir
    )
    assert len(list(ds_train)) == 20
    for example in ds_train:
      assert example["label"] + 10 == example["label_plus_10"]
      assert example["label"] + 2 == example["label_plus_2"]
