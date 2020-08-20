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

"""Test of `document_datasets.py`."""

# import collections
import mock

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import document_datasets

DummyMnist = tfds.testing.DummyMnist


class DummyNewDs(DummyMnist):
  pass


class DummyNewConfig(DummyMnist):
  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name='new_config',
          version=tfds.core.Version('1.0.0'),
          description='Config description.',
      ),
      tfds.core.BuilderConfig(
          name='old_config',
          version=tfds.core.Version('2.0.0'),
          supported_versions=[
              tfds.core.Version('1.0.0'),
          ],
          description='Config description.',
      ),
  ]


class DummyMnistConfigs(DummyMnist):
  """Builder with config and manual instructions."""
  MANUAL_DOWNLOAD_INSTRUCTIONS = """Some manual instructions."""
  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name='config_name',
          version=tfds.core.Version('0.0.1'),
          description='Config description.',
      ),
  ]


class DocumentDatasetsTest(tfds.testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(DocumentDatasetsTest, cls).setUpClass()
    cls._tfds_tmp_dir = tfds.testing.make_tmp_dir()
    builder = DummyMnist(data_dir=cls._tfds_tmp_dir)
    builder.download_and_prepare()

    # Patch the visualization util (to avoid GCS access during test)
    cls._old_path = document_datasets.VisualizationDocUtil.BASE_PATH
    document_datasets.VisualizationDocUtil.BASE_PATH = cls._tfds_tmp_dir

    # Patch the register
    # `pytest` do not execute the tests in isolation.
    # All tests seems to be imported before execution, which leak the
    # registration. Datasets from `register_test.py` are registered when
    # `document_dataset_test.py` is executed.
    # As `_load_nightly_dict` load the full register, we patch it
    # to avoid invalid dataset errors.
    # Context: https://github.com/tensorflow/datasets/issues/1960
    cls._patch_register = mock.patch.object(
        tfds.core.load, 'list_full_names', return_value=[])
    cls._patch_register.start()

  @classmethod
  def tearDownClass(cls):
    super(DocumentDatasetsTest, cls).tearDownClass()
    tfds.testing.rm_tmp_dir(cls._tfds_tmp_dir)
    document_datasets.VisualizationDocUtil.BASE_PATH = cls._old_path

    cls._patch_register.stop()

  def setUp(self):
    super(DocumentDatasetsTest, self).setUp()
    self.builder = DummyMnist(data_dir=self._tfds_tmp_dir)

  def test_document_datasets(self):
    document_datasets.dataset_docs_str(datasets=['mnist', 'cifar10'])

  def test_schema_org(self):
    schema_str = document_datasets.document_single_builder(self.builder)
    self.assertIn('http://schema.org/Dataset', schema_str)
    self.assertIn(
        '<meta itemprop="url" '
        'content="https://www.tensorflow.org'
        '/datasets/catalog/%s" />' % self.builder.name, schema_str)

  def test_with_config(self):
    """Test that builder with configs are correctly generated."""
    with tfds.testing.tmp_dir() as tmp_dir:
      builder = DummyMnistConfigs(data_dir=tmp_dir)
      builder.download_and_prepare()
    doc_str = document_datasets.document_single_builder(builder)

    self.assertIn('Some manual instructions.', doc_str)
    self.assertIn('Mnist description.', doc_str)  # Shared description.
    self.assertIn('Config description.', doc_str)  # Config-specific description


class DocumentNightlyDatasetsTest(tfds.testing.TestCase):

  def test_full_names_to_dict(self):
    full_names_dict = document_datasets._full_names_to_dict([
        'ds1/c1/1.0.0',
        'ds1/c1/2.0.0',
        'ds1/c2/2.0.0',
        'ds2/1.0.0',
        'ds2/2.0.0',
    ])
    self.assertEqual(full_names_dict, {
        'ds1': {
            'c1': {'1.0.0', '2.0.0'},
            'c2': {'2.0.0'},
        },
        'ds2': {
            '': {'1.0.0', '2.0.0'}
        }
    })

  def test_build_nightly_dict(self):
    nightly_dict = document_datasets._build_nightly_dict(
        # Registered datasets
        document_datasets._full_names_to_dict([
            'ds_same/config/1.0.0',
            'ds_with_config/config_new/2.0.0',  # Added config
            'ds_with_config/config_same/2.0.0',  # Added version
            'ds_with_config/config_same/1.0.0',
            'ds_new/1.0.0',  # Added dataset
            'ds_changed/2.0.0',  # Added version
            'ds_changed/1.0.0',
            'ds_type/config/1.0.0',  # `ds/version` -> `ds/config/version`
        ]),
        # Stable datasets
        document_datasets._full_names_to_dict([
            'ds_same/config/1.0.0',
            'ds_with_config/config_same/1.0.0',
            'ds_with_config/config_same/0.0.0',  # Removed version
            'ds_with_config/config_removed/1.0.0',  # Removed config
            'ds_changed/1.0.0',
            'ds_changed/0.0.0',  # Removed version
            'ds_removed/1.0.0',  # Removed dataset',
            'ds_type/1.0.0',  # `ds/version` -> `ds/config/version`
        ]),
    )
    # Check that the added datasets, config, versions are marked as nightly
    self.assertEqual(nightly_dict, {
        'ds_with_config': {
            'config_new': True,
            'config_same': {
                '2.0.0': True,
                '1.0.0': False,
            },
        },
        'ds_new': True,
        'ds_changed': {
            '': {
                '2.0.0': True,
                '1.0.0': False,
            },
        },
        'ds_same': {'config': {'1.0.0': False}},
        'ds_type': {'config': True},
    })

  def test_nightly_doc_util(self):
    data_dir = '/tmp/dummy_dir'

    nightly_dict = {
        'dummy_mnist': {'': {'1.0.0': False}},
        'dummy_new_ds': True,
        'dummy_new_config': {
            'new_config': True,
            'old_config': {
                '2.0.0': True,  # New versions
                '1.0.0': False,
            },
        },
    }
    with mock.patch.object(
        document_datasets, '_load_nightly_dict', return_value=nightly_dict):
      ndu = document_datasets.NightlyDocUtil()

    dummy_mnist = DummyMnist(data_dir=data_dir)
    dummy_new_ds = DummyNewDs(data_dir=data_dir)
    dummy_new_config = DummyNewConfig(data_dir=data_dir, config='new_config')
    dummy_new_version = DummyNewConfig(data_dir=data_dir, config='old_config')

    # Only `dummy_new_ds` is a new builder
    self.assertFalse(ndu.is_builder_nightly(dummy_mnist))
    self.assertTrue(ndu.is_builder_nightly(dummy_new_ds))
    self.assertFalse(ndu.is_builder_nightly(dummy_new_config))
    self.assertFalse(ndu.is_builder_nightly(dummy_new_version))

    # Only `dummy_new_ds/new_config` is a new config
    self.assertFalse(ndu.is_config_nightly(dummy_mnist))
    self.assertFalse(ndu.is_config_nightly(dummy_new_ds))
    self.assertTrue(ndu.is_config_nightly(dummy_new_config))
    self.assertFalse(ndu.is_config_nightly(dummy_new_version))

    # Only `dummy_new_ds/new_version/2.0.0` is a new version
    self.assertFalse(ndu.is_version_nightly(dummy_mnist, '1.0.0'))
    self.assertFalse(ndu.is_version_nightly(dummy_new_ds, 'x.x.x'))
    self.assertFalse(ndu.is_version_nightly(dummy_new_config, 'x.x.x'))
    self.assertFalse(ndu.is_version_nightly(dummy_new_version, '1.0.0'))
    self.assertTrue(ndu.is_version_nightly(dummy_new_version, '2.0.0'))

    # Only `dummy_mnist` don't have a nightly version
    self.assertFalse(ndu.has_nightly(dummy_mnist))
    self.assertTrue(ndu.has_nightly(dummy_new_ds))
    self.assertTrue(ndu.has_nightly(dummy_new_config))
    self.assertTrue(ndu.has_nightly(dummy_new_version))


if __name__ == '__main__':
  tfds.testing.test_main()
