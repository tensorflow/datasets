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

"""Tests for vctk dataset module."""

from tensorflow_datasets import testing
from tensorflow_datasets.audio import vctk


class VctkTest(testing.DatasetBuilderTestCase):
  DATASET_CLASS = vctk.Vctk
  SPLITS = {
      "train": 1,
  }


if __name__ == "__main__":
  testing.test_main()
