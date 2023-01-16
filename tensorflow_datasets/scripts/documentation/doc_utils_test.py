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

"""Tests for tensorflow_datasets.scripts.documentation.doc_utils."""

from unittest import mock

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import doc_utils


class DummyNewDs(tfds.testing.DummyDataset):
  pass


class DummyNewConfig(tfds.testing.DummyDataset):
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


class DocumentNightlyDatasetsTest(tfds.testing.TestCase):

  def test_full_names_to_dict(self):
    full_names_dict = doc_utils._full_names_to_dict([
        'ds1/c1/1.0.0',
        'ds1/c1/2.0.0',
        'ds1/c2/2.0.0',
        'ds2/1.0.0',
        'ds2/2.0.0',
    ])
    self.assertEqual(
        full_names_dict,
        {
            'ds1': {
                'c1': {'1.0.0': None, '2.0.0': None},
                'c2': {'2.0.0': None},
            },
            'ds2': {'': {'1.0.0': None, '2.0.0': None}},
        },
    )

  def test_build_nightly_dict(self):
    nightly_dict = doc_utils._build_nightly_dict(
        # Registered datasets
        doc_utils._full_names_to_dict([
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
        doc_utils._full_names_to_dict([
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
    self.assertEqual(
        nightly_dict,
        {
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
        },
    )

  def test_nightly_doc_util(self):
    data_dir = '/tmp/dummy_dir'

    nightly_dict = {
        'dummy_dataset': {'': {'1.0.0': False}},
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
        doc_utils, '_load_nightly_dict', return_value=nightly_dict
    ):
      ndu = doc_utils.NightlyDocUtil(path='/tmp/some/patched/path')

    dummy_dataset = tfds.testing.DummyDataset(data_dir=data_dir)
    dummy_new_ds = DummyNewDs(data_dir=data_dir)
    dummy_new_config = DummyNewConfig(data_dir=data_dir, config='new_config')
    dummy_new_version = DummyNewConfig(data_dir=data_dir, config='old_config')

    # Only `dummy_new_ds` is a new builder
    self.assertFalse(ndu.is_builder_nightly(dummy_dataset))
    self.assertTrue(ndu.is_builder_nightly(dummy_new_ds))
    self.assertFalse(ndu.is_builder_nightly(dummy_new_config))
    self.assertFalse(ndu.is_builder_nightly(dummy_new_version))

    # Only `dummy_new_ds/new_config` is a new config
    self.assertFalse(ndu.is_config_nightly(dummy_dataset))
    self.assertFalse(ndu.is_config_nightly(dummy_new_ds))
    self.assertTrue(ndu.is_config_nightly(dummy_new_config))
    self.assertFalse(ndu.is_config_nightly(dummy_new_version))

    # Only `dummy_new_ds/new_version/2.0.0` is a new version
    self.assertFalse(ndu.is_version_nightly(dummy_dataset, '1.0.0'))
    self.assertFalse(ndu.is_version_nightly(dummy_new_ds, 'x.x.x'))
    self.assertFalse(ndu.is_version_nightly(dummy_new_config, 'x.x.x'))
    self.assertFalse(ndu.is_version_nightly(dummy_new_version, '1.0.0'))
    self.assertTrue(ndu.is_version_nightly(dummy_new_version, '2.0.0'))

    # Only `dummy_dataset` don't have a nightly version
    self.assertFalse(ndu.has_nightly(dummy_dataset))
    self.assertTrue(ndu.has_nightly(dummy_new_ds))
    self.assertTrue(ndu.has_nightly(dummy_new_config))
    self.assertTrue(ndu.has_nightly(dummy_new_version))


def test_format_hompepage_url():
  url = 'https://a/b'
  assert doc_utils.format_homepage_url(url) == f'[{url}]({url})'
