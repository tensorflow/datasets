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

"""Tests for collection_markdown_builder."""
import textwrap

import pytest

import tensorflow_datasets as tfds
from tensorflow_datasets import testing
from tensorflow_datasets.scripts.documentation import collection_markdown_builder


@pytest.fixture(scope='session')
def dummy_dc_loader() -> tfds.core.DatasetCollectionLoader:
  return tfds.core.DatasetCollectionLoader(
      collection=testing.DummyDatasetCollection())


def test_collection_homepage_section(
    dummy_dc_loader: tfds.core.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  homepage_section = collection_markdown_builder.CollectionHomepageSection()
  assert not homepage_section.content(loader=dummy_dc_loader)


def test_collection_description_section(
    dummy_dc_loader: tfds.core.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  description_section = collection_markdown_builder.CollectionDescriptionSection(
  )
  expected_description = dummy_dc_loader.collection.info.description
  assert description_section.content(
      loader=dummy_dc_loader) == expected_description


def test_collection_citation_section(
    dummy_dc_loader: tfds.core.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  citation_section = collection_markdown_builder.CollectionCitationSection()
  expected_citation = (
      textwrap.dedent(f"""
            ```
            {tfds.core.utils.indent(dummy_dc_loader.collection.info.citation, '            ')}
            ```
            """))
  assert citation_section.content(loader=dummy_dc_loader) == expected_citation


def test_collection_versions_section(
    dummy_dc_loader: tfds.core.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  versions_section = collection_markdown_builder.CollectionVersionSection()
  expected_lines = [
      '    * `1.0.0`: notes 1.0.0',
      '    * `1.1.0`: notes 1.1.0',
      '    * **`2.0.0`** (default): notes 2.0.0',
  ]
  assert versions_section.content(
      loader=dummy_dc_loader) == '\n'.join(expected_lines)


def test_collection_datasets_section(
    dummy_dc_loader: tfds.core.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  datasets_section = collection_markdown_builder.CollectionDatasetsSection()
  expected_lines = [
      '    * `a`: [`a/c:1.3.5`](https://www.tensorflow.org/datasets/catalog/a#c)',
      '    * `b`: [`b/d:2.4.8`](https://www.tensorflow.org/datasets/catalog/b#d)',
      '    * `c`: [`c/e:3.5.7`](https://www.tensorflow.org/datasets/catalog/c#e)',
  ]
  assert datasets_section.content(
      loader=dummy_dc_loader) == '\n'.join(expected_lines)


def test_get_collection_markdown_string(
    dummy_dc_loader: tfds.core.DatasetCollectionLoader):  # pylint: disable=redefined-outer-name
  doc = collection_markdown_builder.get_collection_markdown_string(
      collection=dummy_dc_loader)

  assert 'dummy_dataset_collection' in doc  # Collection heading.
  assert 'my description' in doc  # Collection description.
  assert '@misc{citekey' in doc  # Collection citation.
  assert ('[`c/e:3.5.7`](https://www.tensorflow.org/datasets/catalog/c#e)'
          in doc)  # Collection dataset.
