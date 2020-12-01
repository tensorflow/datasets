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

"""Tests for tensorflow_datasets.scripts.documentation.build_catalog."""

import contextlib
import pathlib
import tempfile
from unittest import mock

import pytest

import tensorflow_datasets as tfds  # pylint: disable=unused-import
from tensorflow_datasets.scripts.documentation import build_catalog
from tensorflow_datasets.scripts.documentation import doc_utils


@pytest.fixture(scope='module')
def mock_gcs_access():
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

    yield


@pytest.mark.usefixtures('mock_gcs_access')
def test_build_catalog(tmp_path: pathlib.Path):
  """Tests that build_catalog correctly generate the index."""
  build_catalog.build_catalog(
      datasets=['mnist', 'coco'],
      catalog_dir=tmp_path,
  )
  assert sorted(f.name for f in tmp_path.iterdir()) == [
      '_toc.yaml',
      'coco.md',
      'mnist.md',
      'overview.md',
  ]

  content = tmp_path.joinpath('_toc.yaml').read_text()
  assert 'coco' in content
  assert 'mnist' in content

  content = tmp_path.joinpath('overview.md').read_text()
  assert 'coco' in content
  assert 'mnist' in content
