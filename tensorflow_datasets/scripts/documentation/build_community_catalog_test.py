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

"""Tests for build_community."""
from unittest import mock

from etils import epath

import tensorflow_datasets as tfds  # pylint: disable=unused-import
from tensorflow_datasets.core import naming
from tensorflow_datasets.scripts.documentation import build_community_catalog

DatasetSource = tfds.core.community.dataset_sources.DatasetSource
DatasetPackage = tfds.core.community.register_package.DatasetPackage
DatasetName = naming.DatasetName


def _create_dataset_package(namespace: str, name: str) -> DatasetPackage:
  path = epath.Path(
      f'github://huggingface/datasets/tree/master/datasets/{name}'
  )
  return DatasetPackage(
      name=DatasetName(namespace_name=f'{namespace}:{name}'),
      source=DatasetSource(root_path=path, filenames=[f'{name}.py']),
  )


def _create_templates(
    index_template: str = '',
    dataset_details_template: str = '',
    namespace_toc_template: str = '',
) -> build_community_catalog.DocumentationTemplates:
  return build_community_catalog.DocumentationTemplates(
      index_template=index_template,
      dataset_details_template=dataset_details_template,
      namespace_toc_template=namespace_toc_template,
  )


def _create_options() -> build_community_catalog._Options:
  return build_community_catalog._Options(catalog_dir='/tmp')


def test_dataset_documentation_properties():
  dataset = _create_dataset_package('community1', 'ds1')
  templates = _create_templates()
  dataset_doc = build_community_catalog.DatasetDocumentation(
      dataset=dataset, templates=templates, options=_create_options()
  )
  assert dataset_doc.tfds_id == 'community1:ds1'
  assert dataset_doc.name == 'ds1'


def test_dataset_documentation_links():
  dataset = _create_dataset_package('community1', 'ds1')
  templates = _create_templates()
  dataset_doc = build_community_catalog.DatasetDocumentation(
      dataset=dataset, templates=templates, options=_create_options()
  )
  expected_code_url = (
      '[Code](github://huggingface/datasets/tree/master/datasets/ds1)'
  )
  assert dataset_doc.code_url() == expected_code_url
  assert dataset_doc.extra_links() == [expected_code_url]
  assert (
      dataset_doc.format_extra_links(prefix='* ', infix=' / ')
      == f'* {expected_code_url}'
  )


def test_dataset_documentation_to_details_markdown():
  dataset = _create_dataset_package('community1', 'ds1')
  templates = _create_templates(
      dataset_details_template='{tfds_id}\n{references_bulleted_list}'
  )
  dataset_doc = build_community_catalog.DatasetDocumentation(
      dataset=dataset, templates=templates, options=_create_options()
  )
  assert (
      dataset_doc.to_details_markdown()
      == 'community1:ds1\n*   '
      '[Code](github://huggingface/datasets/tree/master/datasets/ds1)'
  )


def test_dataset_documentation_to_toc_markdown():
  dataset = _create_dataset_package('community1', 'ds1')
  templates = _create_templates()
  dataset_doc = build_community_catalog.DatasetDocumentation(
      dataset=dataset, templates=templates, options=_create_options()
  )
  assert (
      dataset_doc.to_toc_markdown()
      == 'ds1 ([Code](github://huggingface/datasets/tree/master/datasets/ds1))'
  )


def test_huggingface_dataset_documentation():
  dataset = _create_dataset_package('community1', 'ds1')
  templates = _create_templates()
  dataset_doc = build_community_catalog.HuggingfaceDatasetDocumentation(
      dataset=dataset, templates=templates, options=_create_options()
  )
  assert dataset_doc.extra_links() == [
      '[Code](https://github.com/huggingface/datasets/blob/master/datasets/ds1)',
      '[Huggingface](https://huggingface.co/datasets/ds1)',
  ]


def test_huggingface_formatter_overview_page():
  namespace1 = 'community1'
  datasets = []
  templates = _create_templates()
  formatter = build_community_catalog.HuggingfaceFormatter(
      namespace=namespace1,
      datasets=datasets,
      templates=templates,
      options=_create_options(),
  )
  assert formatter.overview_page == 'community1.md'


@mock.patch('tensorflow_datasets.core.github_api.github_path.get_content')
def test_huggingface_formatter_to_namespace_overview(get_content_mock):
  get_content_mock.return_value = '{}'
  namespace1 = 'huggingface'
  datasets = [
      _create_dataset_package(namespace1, 'ds1'),
      _create_dataset_package(namespace1, 'ds2'),
  ]
  templates = _create_templates(dataset_details_template='{tfds_id}')
  get_content_mock.return_value = '{}'
  formatter = build_community_catalog.HuggingfaceFormatter(
      namespace=namespace1,
      datasets=datasets,
      templates=templates,
      options=_create_options(),
  )
  assert (
      formatter.to_namespace_overview()
      == """\
# Huggingface datasets

Huggingface has forked TFDS and provides a lot of text datasets. See
[here](https://huggingface.co/docs/datasets/) for more documentation.
Next you can find the list of all the datasets that can be used with TFDS.


*  [ds1](huggingface/ds1.md)
*  [ds2](huggingface/ds2.md)
"""
  )


@mock.patch('tensorflow_datasets.core.github_api.github_path.get_content')
def test_huggingface_formatter_to_toc_markdown(get_content_mock):
  get_content_mock.return_value = '{}'
  namespace1 = 'community1'
  datasets = [
      _create_dataset_package(namespace1, 'ds1'),
      _create_dataset_package(namespace1, 'ds2'),
  ]
  templates = _create_templates(namespace_toc_template='{name}')

  formatter = build_community_catalog.HuggingfaceFormatter(
      namespace=namespace1,
      datasets=datasets,
      templates=templates,
      options=_create_options(),
  )
  assert formatter.to_toc_markdown() == 'Community1'
