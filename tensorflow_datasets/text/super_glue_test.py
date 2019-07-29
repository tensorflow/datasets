# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""Tests for super_glue dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from tensorflow_datasets import testing
from tensorflow_datasets.text import super_glue

_BASE_DIR = os.path.join(
    os.path.dirname(__file__), "../",
    "testing/test_data/fake_examples/super_glue")


class SuperGlueCbTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["cb"]
  DATASET_CLASS = super_glue.SuperGlue
  EXAMPLE_DIR = os.path.join(_BASE_DIR, "CB")
  SPLITS = {
      "train": 3,
      "validation": 2,
      "test": 1,
  }


class SuperGlueCopaTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["copa"]
  DATASET_CLASS = super_glue.SuperGlue
  EXAMPLE_DIR = os.path.join(_BASE_DIR, "COPA")
  SPLITS = {
      "train": 3,
      "validation": 2,
      "test": 1,
  }


class SuperGlueMultiRcTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["multirc"]
  DATASET_CLASS = super_glue.SuperGlue
  EXAMPLE_DIR = os.path.join(_BASE_DIR, "MultiRC")
  SPLITS = {
      "train": 58,
      "validation": 62,
      "test": 58,
  }


class SuperGlueRteTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["rte"]
  DATASET_CLASS = super_glue.SuperGlue
  EXAMPLE_DIR = os.path.join(_BASE_DIR, "RTE")
  SPLITS = {
      "train": 3,
      "validation": 2,
      "test": 1,
  }


class SuperGlueWscTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["wsc", "wsc.fixed"]
  DATASET_CLASS = super_glue.SuperGlue
  EXAMPLE_DIR = os.path.join(_BASE_DIR, "WSC")
  SPLITS = {
      "train": 3,
      "validation": 2,
      "test": 1,
  }


class SuperGlueWicTest(testing.DatasetBuilderTestCase):
  BUILDER_CONFIG_NAMES_TO_TEST = ["wic"]
  DATASET_CLASS = super_glue.SuperGlue
  EXAMPLE_DIR = os.path.join(_BASE_DIR, "WiC")
  SPLITS = {
      "train": 3,
      "validation": 2,
      "test": 1,
  }


# TODO(adarob): Add MultiRC test.

if __name__ == "__main__":
  testing.test_main()
