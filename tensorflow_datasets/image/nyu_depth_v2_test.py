# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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
"""Tests for NYU Depth V2 Dataset."""

from tensorflow_datasets.image import nyu_depth_v2
import tensorflow_datasets.public_api as tfds


class NyuDepthV2FastdepthTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = nyu_depth_v2.NyuDepthV2
  BUILDER_CONFIG_NAMES_TO_TEST = ["depth"]
  SPLITS = {"train": 2, "validation": 1}
  DL_EXTRACT_RESULT = "fastdepth"


class NyuDepthV2LabeledTest(tfds.testing.DatasetBuilderTestCase):
  DATASET_CLASS = nyu_depth_v2.NyuDepthV2
  BUILDER_CONFIG_NAMES_TO_TEST = ["labeled"]
  SPLITS = {"train": 2}
  DL_EXTRACT_RESULT = "nyu_unit_test.mat"


if __name__ == "__main__":
  tfds.testing.test_main()
