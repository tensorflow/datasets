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

"""Test of `document_datasets.py`."""

import functools
from typing import Set
from unittest import mock

import pytest

import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import doc_utils
from tensorflow_datasets.scripts.documentation import document_datasets


class DummyDatasetConfigs(tfds.testing.DummyDataset):
  """Builder with config and manual instructions."""

  MANUAL_DOWNLOAD_INSTRUCTIONS = """Some manual instructions."""
  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(
          name='config_name',
          version=tfds.core.Version('0.0.1'),
          description='Config description.',
      ),
  ]


class DummyDatasetConfigsSharedVersion(tfds.testing.DummyDataset):
  """Builder with config ."""

  # No BuilderConfig description, and version shared across configs.
  VERSION = tfds.core.Version('1.0.0')
  BUILDER_CONFIGS = [
      tfds.core.BuilderConfig(name='config_name'),
  ]


@pytest.fixture
def document_single_builder_fn(tmp_path):
  yield functools.partial(
      document_datasets._document_single_builder,
      visu_doc_util=doc_utils.VisualizationDocUtil(
          base_path=tmp_path,
          base_url=doc_utils.DocUtilPaths.fig_base_url,
      ),
      df_doc_util=doc_utils.DataframeDocUtil(
          base_path=tmp_path,
          base_url=doc_utils.DocUtilPaths.df_base_url,
      ),
      nightly_doc_util=None,
  )


def test_document_datasets():
  all_docs = list(
      document_datasets.iter_documentation_builders(
          # Builder with and without config, as well as config-based builder.
          datasets=['mnist', 'coco', 'pass'],
          doc_util_paths=doc_utils.DocUtilPaths(
              fig_base_path=None,
              df_base_path=None,
              nightly_path=None,
          ),
      )
  )
  assert {d.name for d in all_docs} == {'mnist', 'coco', 'pass'}


def test_document_collection():
  all_docs = list(
      document_datasets.iter_collections_documentation(
          collection_names=['xtreme', 'longt5']
      )
  )
  assert {d.name for d in all_docs} == {'xtreme', 'longt5'}


def test_with_config(document_single_builder_fn):  # pylint: disable=redefined-outer-name
  """Test that builder with configs are correctly generated."""
  doc = document_single_builder_fn(DummyDatasetConfigs.name)
  assert 'Some manual instructions.' in doc.content
  assert 'Minimal DatasetBuilder.' in doc.content  # Shared description.
  # Config-description
  assert '**Config description**: Config description.' in doc.content
  assert (
      '<meta itemprop="url" content="'
      f'https://www.tensorflow.org/datasets/catalog/{DummyDatasetConfigs.name}"'
      ' />'
      in doc.content
  )


def test_with_config_shared_version(document_single_builder_fn):  # pylint: disable=redefined-outer-name
  """Test that builder with configs are correctly generated."""
  doc = document_single_builder_fn(DummyDatasetConfigsSharedVersion.name)
  assert 'Minimal DatasetBuilder.' in doc.content  # Shared description.
  assert 'Config description:' not in doc.content  # No config description.


@pytest.mark.parametrize(
    'sections,expected',
    [
        (set(), set()),
        ({'a_b'}, {'A b'}),
        ({'a-b'}, {'A b'}),
        ({'c modelling'}, {'C modeling'}),
        ({'a_b', 'c modelling'}, {'A b', 'C modeling'}),
    ],
)
def test_builder_to_document_sections(sections: Set[str], expected: Set[str]):
  mock_builder = mock.MagicMock()
  instance = document_datasets.BuilderToDocument(
      sections=sections,
      namespace=None,
      builder=mock_builder,
      config_builders=[],
  )
  assert instance.sections == expected
