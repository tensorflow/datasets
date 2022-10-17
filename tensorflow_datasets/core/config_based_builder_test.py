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

"""Tests for config_based_builder."""

import inspect
from unittest import mock

from tensorflow_datasets import testing
from tensorflow_datasets.core import config_based_builder
from tensorflow_datasets.testing.dummy_config_based_datasets.dummy_ds_1 import dummy_ds_1_dataset_builder


class GetBuilderDatadirPathTest(testing.TestCase):

  def test_inspect_module_can_find_src(self):
    path = config_based_builder._get_builder_datadir_path(
        dummy_ds_1_dataset_builder.Builder)
    self.assertEndsWith(
        str(path), "testing/dummy_config_based_datasets/dummy_ds_1")

  def test_inspect_module_cannot_find_src(self):
    with mock.patch.object(inspect, "getsourcefile", return_value=None):
      path = config_based_builder._get_builder_datadir_path(
          dummy_ds_1_dataset_builder.Builder)
    self.assertEndsWith(
        str(path),
        "/tensorflow_datasets/testing/dummy_config_based_datasets/dummy_ds_1")


class ConfigBasedBuilderTest(testing.TestCase):

  def test_class_named_after_pkg_name(self):
    ds_builder = dummy_ds_1_dataset_builder.Builder()
    self.assertEqual(ds_builder.name, "dummy_ds_1")

  def test_get_metadata(self):
    builder_cls = dummy_ds_1_dataset_builder.Builder()
    metadata = builder_cls.get_metadata()
    self.assertEqual(metadata.tags, ["content.data-type.image"])

  def test_dummy_ds_1_read_from_config(self):
    ds_builder = dummy_ds_1_dataset_builder.Builder()
    info = ds_builder._info()
    self.assertEqual(info.description,
                     "Description of `dummy_ds_1` dummy config-based dataset.")
    self.assertEqual(
        info.citation, """@Article{google22tfds,
author = "The TFDS team",
title = "TFDS: a collection of ready-to-use datasets for use with TensorFlow, Jax, and other Machine Learning frameworks.",
journal = "ML gazette",
year = "2022"
}""")


if __name__ == "__main__":
  testing.test_main()
