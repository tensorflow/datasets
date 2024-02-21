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

"""Tests for universal_dependencies_utils."""

from tensorflow_datasets.text.universal_dependencies import universal_dependencies_utils as ud_utils


def test_prepare_ud_filepaths():
  expected_output = ["https://a/b"]

  filepaths_1 = ud_utils.prepare_ud_filepaths(
      path_prefix="https://a", filepaths="b")
  filepaths_2 = ud_utils.prepare_ud_filepaths(
      path_prefix="https://a", filepaths=["b"])

  assert filepaths_1 == expected_output
  assert filepaths_2 == expected_output
