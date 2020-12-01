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

import contextlib
import functools
import tempfile
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


@pytest.fixture(scope='module')
def document_single_builder_fn():
  with contextlib.ExitStack() as stack:
    tmp_dir = stack.enter_context(tempfile.TemporaryDirectory())

    # Patch the visualization utils (to avoid GCS access during test)
    stack.enter_context(mock.patch.object(
        doc_utils.VisualizationDocUtil, 'BASE_PATH', tmp_dir
    ))
    stack.enter_context(mock.patch.object(
        doc_utils.DataframeDocUtil, 'BASE_PATH', tmp_dir
    ))
    # Patch the register
    # `pytest` do not execute the tests in isolation.
    # All tests seems to be imported before execution, which leak the
    # registration. Datasets from `register_test.py` are registered when
    # `document_dataset_test.py` is executed.
    # As `_load_nightly_dict` load the full register, we patch it
    # to avoid invalid dataset errors.
    # Context: https://github.com/tensorflow/datasets/issues/1960
    stack.enter_context(mock.patch.object(
        tfds.core.load, 'list_full_names', return_value=[]
    ))

    fn = functools.partial(
        document_datasets._document_single_builder,
        visu_doc_util=doc_utils.VisualizationDocUtil(),
        df_doc_util=doc_utils.DataframeDocUtil(),
        nightly_doc_util=doc_utils.NightlyDocUtil(),
    )
    yield fn


@pytest.mark.usefixtures('document_single_builder_fn')
def test_document_datasets():
  all_docs = list(document_datasets.iter_documentation_builders(
      datasets=['mnist', 'coco'],  # Builder with and without config
  ))
  assert {d.name for d in all_docs} == {'mnist', 'coco'}


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
  ) in doc.content


def test_with_config_shared_version(document_single_builder_fn):  # pylint: disable=redefined-outer-name
  """Test that builder with configs are correctly generated."""
  doc = document_single_builder_fn(DummyDatasetConfigsSharedVersion.name)
  assert 'Minimal DatasetBuilder.' in doc.content  # Shared description.
  assert 'Config description:' not in doc.content  # No config description
