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

"""Titanic dataset."""

import collections
import csv

from etils import epath
import numpy as np
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
import tensorflow_datasets.public_api as tfds

_EMBARKED_DICT = collections.OrderedDict([
    ("C", "Cherbourg"),
    ("Q", "Queenstown"),
    ("S", "Southampton"),
    ("?", "Unknown"),
])

_PCLASS_DICT = collections.OrderedDict(
    [("1", "1st_class"), ("2", "2nd_class"), ("3", "3rd_class")]
)

_SURVIVED_DICT = {"0": "died", "1": "survived"}


def convert_to_float(d):
  return -1.0 if d == "?" else np.float32(d)


def convert_to_int(d):
  return -1 if d == "?" else np.int32(d)


def convert_to_string(d):
  return "Unknown" if d == "?" else d


def convert_to_label(d, dictionary):
  return dictionary[d]


def return_same(d):
  return d


def _feature_dict():
  return collections.OrderedDict([
      (
          "pclass",
          (
              tfds.features.ClassLabel(names=_PCLASS_DICT.values()),
              lambda d: convert_to_label(d, _PCLASS_DICT),
          ),
      ),
      (
          "survived",
          (
              tfds.features.ClassLabel(names=_SURVIVED_DICT.values()),
              lambda d: convert_to_label(d, _SURVIVED_DICT),
          ),
      ),
      ("name", (tf.string, convert_to_string)),
      (
          "sex",
          (tfds.features.ClassLabel(names=["male", "female"]), return_same),
      ),
      ("age", (tf.float32, convert_to_float)),
      ("sibsp", (tf.int32, convert_to_int)),
      ("parch", (tf.int32, convert_to_int)),
      ("ticket", (tf.string, convert_to_string)),
      ("fare", (tf.float32, convert_to_float)),
      ("cabin", (tf.string, convert_to_string)),
      (
          "embarked",
          (
              tfds.features.ClassLabel(names=_EMBARKED_DICT.values()),
              lambda d: convert_to_label(d, _EMBARKED_DICT),
          ),
      ),
      ("boat", (tf.string, convert_to_string)),
      ("body", (tf.int32, convert_to_int)),
      ("home.dest", (tf.string, convert_to_string)),
  ])


_URL = "https://www.openml.org/data/get_csv/16826755/phpMYEkMl"


class Builder(tfds.core.GeneratorBasedBuilder):
  """Titanic dataset."""

  VERSION = tfds.core.Version("4.0.0")
  SUPPORTED_VERSIONS = [tfds.core.Version("2.0.0")]
  RELEASE_NOTES = {
      "4.0.0": "Fix inverted labels which were inverted in the 3.0.0.",
      "3.0.0": (
          "Use a standard flat dictionary of features for the dataset. "
          "Use `as_supervised=True` to split the dataset into "
          "a `(features_dict, survived)` tuple."
      ),
      "2.0.0": "New split API (https://tensorflow.org/datasets/splits)",
  }

  def _info(self):
    supervised_features = _feature_dict()
    survived_feature, unused_func = supervised_features.pop("survived")

    if self.version >= "3.0.0":
      supervised_keys = (
          {key: key for key in supervised_features.keys()},
          "survived",
      )
      features = features = tfds.features.FeaturesDict(
          {name: dtype for name, (dtype, func) in _feature_dict().items()}
      )
    else:
      supervised_keys = ("features", "survived")
      features = tfds.features.FeaturesDict({
          "survived": survived_feature,
          "features": {
              name: dtype for name, (dtype, func) in supervised_features.items()
          },
      })
    return self.dataset_info_from_configs(
        features=features,
        supervised_keys=supervised_keys,
        homepage="https://www.openml.org/d/40945",
    )

  def _split_generators(self, dl_manager):
    path = dl_manager.download(_URL)

    # There is no predefined train/val/test split for this dataset.
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN, gen_kwargs={"file_path": path}
        ),
    ]

  def _generate_examples(self, file_path):
    """Generate features and target given the directory path.

    Args:
      file_path: path where the csv file is stored

    Yields:
      The features and the target
    """
    with epath.Path(file_path).open() as f:
      raw_data = csv.DictReader(f)
      if self.version >= "3.0.0":
        for i, row in enumerate(raw_data):
          yield i, {
              name: _feature_dict()[name][1](value)
              for name, value in row.items()
          }
      else:
        for i, row in enumerate(raw_data):
          survive_val = row.pop("survived")
          yield i, {
              "survived": convert_to_label(survive_val, _SURVIVED_DICT),
              "features": {
                  name: _feature_dict()[name][1](value)
                  for name, value in row.items()
              },
          }
