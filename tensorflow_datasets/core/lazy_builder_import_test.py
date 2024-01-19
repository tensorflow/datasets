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

"""Tests for lazy_builder_import."""

from unittest import mock

from tensorflow_datasets import testing
from tensorflow_datasets.core import lazy_builder_import
from tensorflow_datasets.core import registered


class FooDataset:
  name = "foo"
  version = "1.2.3"


class LazyBuilderImportTest(testing.TestCase):

  @mock.patch.object(
      registered, "imported_builder_cls", return_value=FooDataset
  )
  def test_import_on_first_attr_used(self, mock_imported_builder_cls):
    proxy_cls = lazy_builder_import.LazyBuilderImport("foo")
    self.assertFalse(mock_imported_builder_cls.called)
    ds_name = proxy_cls.name
    mock_imported_builder_cls.assert_called_with("foo")
    self.assertEqual(ds_name, "foo")
    # Subsequent calls re-use same builder cls:
    self.assertEqual(proxy_cls.version, "1.2.3")
    mock_imported_builder_cls.assert_called_once()

  @mock.patch.object(
      registered, "imported_builder_cls", return_value=FooDataset
  )
  def test_import_on_init(self, mock_imported_builder_cls):
    proxy_cls = lazy_builder_import.LazyBuilderImport("foo")
    self.assertFalse(mock_imported_builder_cls.called)
    ds_instance = proxy_cls()
    mock_imported_builder_cls.assert_called_with("foo")
    self.assertIsInstance(ds_instance, FooDataset)
    # Subsequent calls re-use same builder cls:
    self.assertEqual(proxy_cls.version, "1.2.3")
    mock_imported_builder_cls.assert_called_once()


if __name__ == "__main__":
  testing.test_main()
