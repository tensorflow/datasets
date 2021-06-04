# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Tests for file_adapters."""

from tensorflow_datasets.core import file_adapters


def test_is_example_file():
  assert file_adapters.is_example_file('example1.tfrecord')
  assert file_adapters.is_example_file('example1.riegeli')
  assert file_adapters.is_example_file('example1.tfrecord-00000-of-00001')
  assert not file_adapters.is_example_file('example1.info')


def test_format_suffix():
  assert file_adapters.ADAPTER_FOR_FORMAT[
      file_adapters.DEFAULT_FILE_FORMAT].FILE_SUFFIX == 'tfrecord'
  assert file_adapters.ADAPTER_FOR_FORMAT[
      file_adapters.FileFormat.TFRECORD].FILE_SUFFIX == 'tfrecord'
  assert file_adapters.ADAPTER_FOR_FORMAT[
      file_adapters.FileFormat.RIEGELI].FILE_SUFFIX == 'riegeli'


# TODO(mohitreddy): Add tests for `make_tf_data` and `write_examples` methods.
