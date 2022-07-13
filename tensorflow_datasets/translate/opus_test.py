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

# -*- coding: utf-8 -*-
"""Tests for OPUS translate dataset module."""

from tensorflow_datasets import testing
import tensorflow_datasets.public_api as tfds
from tensorflow_datasets.translate import opus


class OpusTestCustomConfigTest(tfds.testing.DatasetBuilderTestCase):

  @classmethod
  def setUpClass(cls):
    super(OpusTestCustomConfigTest, cls).setUpClass()

    config = opus.OpusConfig(
        version=tfds.core.Version("0.1.0"),
        language_pair=("de", "en"),
        subsets=["Tanzil", "EMEA"])
    opus.Opus.BUILDER_CONFIGS = [config]

  @classmethod
  def tearDownClass(cls):
    super(OpusTestCustomConfigTest, cls).tearDownClass()
    opus.Opus.BUILDER_CONFIGS.pop()

  DATASET_CLASS = opus.Opus

  SPLITS = {
      "train": 30,
  }


if __name__ == "__main__":
  testing.test_main()
