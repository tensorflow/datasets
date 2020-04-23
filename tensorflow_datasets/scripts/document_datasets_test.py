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

# Lint as: python3
"""Test of `document_datasets.py`."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import mock

import tensorflow.compat.v2 as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import utils
from tensorflow_datasets.scripts import document_datasets

DummyMnist = testing.DummyMnist


_DS_FULL_NAMES = [
    'ds1/c1/1.0.0',
    'ds1/c1/2.0.0',
    'ds1/c2/2.0.0',
    'ds2/1.0.0',
    'ds2/2.0.0',
]

_DS_FULL_NAMES_DICT = {
    'ds1': {
        'c1': {'1.0.0', '2.0.0'},
        'c2': {'2.0.0'},
    },
    'ds2': {
        '': {'1.0.0', '2.0.0'}
    }
}

_DATASET_NIGHTLY_PROPS = {
    'dummy_mnist': {'': {'1.0.0': False}},
    'dummy_mnist_configs': {'config_name': {'0.0.1': False}},
    'dummy_new_ds': True,
    'dummy_new_config': {'new_config': True},
    'dummy_new_version': {'old_config': {'3.0.0': True}}
}

document_datasets.get_datasets_nightly_properties = mock.Mock(
    return_value=_DATASET_NIGHTLY_PROPS)


class DummyNewDs(DummyMnist):
  pass


class DummyNewConfig(DummyMnist):
  BUILDER_CONFIGS = [
      dataset_builder.BuilderConfig(
          name="new_config",
          version=utils.Version("1.0.0"),
          description="Config description.",
      ),
  ]


class DummyNewVersion(DummyMnist):
  BUILDER_CONFIGS = [
      dataset_builder.BuilderConfig(
          name="old_config",
          version=utils.Version("3.0.0"),
          description="Config description.",
      ),
  ]


class DummyMnistConfigs(DummyMnist):
  """Builder with config and manual instructions."""
  MANUAL_DOWNLOAD_INSTRUCTIONS = """Some manual instructions."""
  BUILDER_CONFIGS = [
      dataset_builder.BuilderConfig(
          name="config_name",
          version=utils.Version("0.0.1"),
          description="Config description.",
      ),
  ]


class DocumentDatasetsTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DocumentDatasetsTest, cls).setUpClass()
    cls._tfds_tmp_dir = testing.make_tmp_dir()
    cls._nightly_ds = document_datasets.NightlyUtil()
    builder = DummyMnist(data_dir=cls._tfds_tmp_dir)
    builder.download_and_prepare()

  @classmethod
  def tearDownClass(cls):
    super(DocumentDatasetsTest, cls).tearDownClass()
    testing.rm_tmp_dir(cls._tfds_tmp_dir)

  def setUp(self):
    super(DocumentDatasetsTest, self).setUp()
    self.builder = DummyMnist(data_dir=self._tfds_tmp_dir)

  @testing.run_in_graph_and_eager_modes()
  def test_schema_org(self):
    schema_str = document_datasets.document_single_builder(self.builder)
    self.assertIn("http://schema.org/Dataset", schema_str)
    self.assertIn(
        '<meta itemprop="url" '
        'content="https://www.tensorflow.org'
        '/datasets/catalog/%s" />' % self.builder.name, schema_str)

  def test_with_config(self):
    """Test that builder with configs are correctly generated."""
    with testing.tmp_dir() as tmp_dir:
      builder = DummyMnistConfigs(data_dir=tmp_dir)
      builder.download_and_prepare()
    doc_str = document_datasets.document_single_builder(builder)

    self.assertIn("Some manual instructions.", doc_str)
    self.assertIn("Mnist description.", doc_str)  # Shared description.
    self.assertIn("Config description.", doc_str)  # Config-specific description

  def test_func(self):
    ds_collection = document_datasets.make_full_name_to_ds_dict(_DS_FULL_NAMES)
    ds_dict = {k: dict(v) for k, v in ds_collection.items()}
    self.assertDictEqual(
        _DS_FULL_NAMES_DICT,
        ds_dict,
        "Function make_full_name_to_ds_dict() does not work as expected.")

  def test_old_ds(self):
    self.assertFalse(self._nightly_ds.is_builder_nightly(self.builder),
                     "DummyMnist is a old dataset")

  def test_new_nightly_ds(self):
    with testing.tmp_dir() as tmp_dir:
      builder = DummyNewDs(data_dir=tmp_dir)
      builder.download_and_prepare()
    self.assertTrue(self._nightly_ds.is_builder_nightly(builder),
                     "DummyNewDs is a new dataset")
    
  # def test_ds_updated_in_nightly(self):
  #   ds_updated = {
  #     DummyMnist: False,
  #     DummyNewDs: True,
  #     DummyNewConfig: True,
  #     DummyNewVersion: True,
  #     DummyMnistConfigs: False,
  #   }
  #   for ds, updated in ds_updated.items():
  #     with testing.tmp_dir() as tmp_dir:
  #       builder = ds(data_dir=tmp_dir)
  #       builder.download_and_prepare()
  #     self.assertEqual(updated, self._nightly_ds.updated_in_nightly(builder))

  def test_new_config_in_nightly(self):
    with testing.tmp_dir() as tmp_dir:
      builder = DummyNewConfig(data_dir=tmp_dir)
      builder.download_and_prepare()
    self.assertTrue(self._nightly_ds.is_config_nightly(builder),
                     "DummyNewConfig has a new config dataset")

  def test_new_version_in_nightly(self):
    with testing.tmp_dir() as tmp_dir:
      builder = DummyNewVersion(data_dir=tmp_dir)
      builder.download_and_prepare()
    self.assertTrue(self._nightly_ds.is_version_nightly(builder),
                     "DummyNewVersion has a new config dataset")


if __name__ == "__main__":
  testing.test_main()
