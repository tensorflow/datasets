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

"""Tests for tensorflow_datasets.scripts.documentation.build_catalog."""

import pathlib

import tensorflow_datasets as tfds  # pylint: disable=unused-import
from tensorflow_datasets.scripts.documentation import build_catalog
from tensorflow_datasets.scripts.documentation import doc_utils


def test_build_catalog(tmp_path: pathlib.Path):
  """Tests that build_catalog correctly generates the index."""
  build_catalog.build_catalog(
      datasets=['mnist', 'coco'],
      catalog_dir=tmp_path,
      doc_util_paths=doc_utils.DocUtilPaths(
          fig_base_path=None,
          df_base_path=None,
          nightly_path=None,
      ),
      include_collections=False,
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


def test_build_catalog_with_collections(tmp_path: pathlib.Path):
  """Tests that build_catalog generates the index including collections."""
  build_catalog.build_catalog(
      datasets=['mnist', 'coco'],
      ds_collections=['longt5'],
      catalog_dir=tmp_path,
      doc_util_paths=doc_utils.DocUtilPaths(
          fig_base_path=None,
          df_base_path=None,
          nightly_path=None,
      ),
      include_collections=True,
  )
  assert sorted(f.name for f in tmp_path.iterdir()) == [
      '_toc.yaml',
      'coco.md',
      'longt5.md',
      'mnist.md',
      'overview.md',
  ]

  content = tmp_path.joinpath('_toc.yaml').read_text()
  assert 'coco' in content
  assert 'mnist' in content
  assert 'longt5' in content

  content = tmp_path.joinpath('overview.md').read_text()
  assert 'coco' in content
  assert 'mnist' in content
  assert 'longt5' in content
