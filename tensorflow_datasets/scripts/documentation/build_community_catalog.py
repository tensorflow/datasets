# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

r"""Tool to generate the dataset community catalog documentation.
"""

import argparse
import dataclasses
import json
import os
import textwrap
from typing import Any, Iterator, List, Mapping, MutableMapping, Sequence, Tuple

from absl import app
from absl.flags import argparse_flags

import tensorflow_datasets as tfds
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import register_package
from tensorflow_datasets.core.github_api import github_path
from tensorflow_datasets.core.utils import gcs_utils
import yaml

DatasetPackage = register_package.DatasetPackage

_INDEX_TEMPLATE_PATH = 'scripts/documentation/templates/community_catalog_overview.md'
_DATASET_DETAILS_TEMPLATE_PATH = 'scripts/documentation/templates/community_namespace_dataset.md'
_NAMESPACE_TOC_TEMPLATE_PATH = 'scripts/documentation/templates/community_namespace_toc.md'


def _parse_flags(_) -> argparse.Namespace:
  """Command line flags."""
  parser = argparse_flags.ArgumentParser(
      prog='build_community_catalog',
      description='Tool to generate the community dataset catalog',
  )
  parser.add_argument(
      '--catalog_dir',
      help='Directory path where to generate the catalog. Default to TFDS dir.',
  )
  return parser.parse_args()


def _load_template(path: str) -> str:
  return tfds.core.tfds_path(path).read_text()


def _to_toc_yaml(title: str, path: str, page: str) -> Mapping[str, Any]:
  return {
      'title': title,
      'path': os.path.join(path, page),
  }


@dataclasses.dataclass()
class DocumentationTemplates:
  index_template: str
  dataset_details_template: str
  namespace_toc_template: str

  @classmethod
  def load(cls) -> 'DocumentationTemplates':
    return cls(
        index_template=_load_template(_INDEX_TEMPLATE_PATH),
        dataset_details_template=_load_template(_DATASET_DETAILS_TEMPLATE_PATH),
        namespace_toc_template=_load_template(_NAMESPACE_TOC_TEMPLATE_PATH),
    )


@dataclasses.dataclass()
class DatasetDocumentation:
  """Functionality to generate documentation for a community dataset."""
  dataset: DatasetPackage
  templates: DocumentationTemplates

  @property
  def tfds_id(self) -> str:
    return str(self.dataset.name)

  @property
  def name(self) -> str:
    return self.dataset.name.name

  def code_url(self, title: str = 'Code') -> str:
    return f'[{title}]({self.dataset.source.root_path})'

  def to_details_markdown(self) -> str:
    """"Markdown to be shown on the details page for the namespace."""
    extra_links = self.format_extra_links(prefix='*   ', infix='\n')
    return self.templates.dataset_details_template.format(
        name=self.name,
        namespace=self.dataset.name.namespace,
        tfds_id=self.tfds_id,
        references_bulleted_list=extra_links,
    )

  def extra_links(self) -> Sequence[str]:
    """List of extra links (formatted in Markdown) relevant for this dataset."""
    return [self.code_url()]

  def format_extra_links(self, prefix: str, infix: str) -> str:
    return infix.join([f'{prefix}{link}' for link in self.extra_links()])

  def to_toc_markdown(self) -> str:
    """Markdown to be shown in the TOC in the overview page."""
    extra_links = self.format_extra_links(prefix='', infix=' / ')
    return f'{self.name} ({extra_links})'


@dataclasses.dataclass()
class GithubDatasetDocumentation(DatasetDocumentation):
  """Specialized formatter for datasets whose dataset builder code is on Github."""

  @property
  def gh_path(self) -> github_path.GithubPath:
    return github_path.GithubPath(self.dataset.source.root_path)

  def code_url(self, title: str = 'Code') -> str:
    return f'[{title}]({self.gh_path.as_human_friendly_url()})'


@dataclasses.dataclass()
class HuggingfaceDatasetDocumentation(GithubDatasetDocumentation):
  """Specialized formatter for Huggingface."""

  def huggingface_link(self) -> str:
    return f'[Huggingface](https://huggingface.co/datasets/{self.name})'

  def extra_links(self) -> Sequence[str]:
    return [self.code_url(), self.huggingface_link()]


@dataclasses.dataclass()
class NamespaceFormatter:
  """A documentation formatter for a namespace and all its datasets."""
  namespace: str
  datasets: Sequence[DatasetPackage]
  templates: DocumentationTemplates

  @property
  def name(self) -> str:
    return self.namespace.capitalize()

  @property
  def overview_page(self) -> str:
    return f'{self.namespace}.md'

  def sections(self) -> Sequence[DatasetDocumentation]:
    return [
        DatasetDocumentation(dataset=ds, templates=self.templates)
        for ds in self.datasets
    ]

  def to_details_markdown(self) -> str:
    """Markdown with dataset details for the namespace dataset overview."""
    sections = '\n'.join(
        [section.to_details_markdown() for section in self.sections()])
    template = textwrap.dedent("""
      # {self.name} datasets


      {sections}
      """)
    return template.format(sections=sections)

  def to_toc_markdown(self) -> str:
    datasets_for_toc = '\n'.join(
        [f'*   {section.to_toc_markdown()}' for section in self.sections()])
    return self.templates.namespace_toc_template.format(
        name=self.name,
        namespace=self.namespace,
        overview_page=self.overview_page,
        num_datasets=len(self.datasets),
        datasets_for_toc=datasets_for_toc)

  def to_toc_yaml(self, toc_relative_path: str):
    return _to_toc_yaml(
        title=self.name, path=toc_relative_path, page=self.namespace)


@dataclasses.dataclass()
class HuggingfaceFormatter(NamespaceFormatter):
  """Specialized formatter for Huggingface."""

  def sections(self) -> Sequence[DatasetDocumentation]:
    return [
        HuggingfaceDatasetDocumentation(dataset=ds, templates=self.templates)
        for ds in self.datasets
    ]

  def to_details_markdown(self) -> str:
    sections = '\n'.join(
        [section.to_details_markdown() for section in self.sections()])
    template = textwrap.dedent("""\
      # Huggingface datasets

      Huggingface has forked TFDS and provide a lot of text datasets. See
      [here](https://huggingface.co/docs/datasets/) for more documentation.


      {sections}
      """)
    return template.format(sections=sections)


def formatter_for(
    namespace: str,
    datasets: Sequence[DatasetPackage],
    templates: DocumentationTemplates,
) -> NamespaceFormatter:
  """Returns the formatter for the given namespace and datasets."""
  if namespace == 'huggingface':
    return HuggingfaceFormatter(
        namespace=namespace, datasets=datasets, templates=templates)
  return NamespaceFormatter(
      namespace=namespace, datasets=datasets, templates=templates)


def build_overview(formatter_per_namespace: Mapping[str, NamespaceFormatter],
                   templates: DocumentationTemplates) -> str:
  """Builds and saves the overview page."""
  toc_elements = [
      formatter.to_toc_markdown()
      for namespace, formatter in formatter_per_namespace.items()
  ]
  toc = '\n'.join(toc_elements)
  return templates.index_template.format(toc=toc)


def build_namespace_details(
    formatter_per_namespace: Mapping[str, NamespaceFormatter]
) -> Iterator[Tuple[str, str]]:
  """Generates all the detail pages for all namespaces and datasets."""
  for namespace, formatter in formatter_per_namespace.items():
    details_markdown = formatter.to_details_markdown()
    yield namespace, details_markdown


def build_toc_yaml(
    formatter_per_namespace: Mapping[str,
                                     NamespaceFormatter]) -> Mapping[str, Any]:
  """Returns a mapping representing the TOC (to be converted into Yaml)."""
  toc_relative_path = '/datasets/community_catalog'
  sections = [
      _to_toc_yaml(title='Overview', path=toc_relative_path, page='overview')
  ]
  for _, formatter in formatter_per_namespace.items():
    sections.append(formatter.to_toc_yaml(toc_relative_path))
  return {'toc': sections}


def build_and_save_community_catalog(
    catalog_dir: tfds.core.ReadWritePath) -> None:
  """Builds and saves the catalog of community datasets."""
  templates = DocumentationTemplates.load()
  formatter_per_namespace = _get_formatter_per_namespace(templates)

  overview = build_overview(formatter_per_namespace, templates)
  catalog_dir.joinpath('overview.md').write_text(overview)

  # Write the `_toc.yaml` TF documentation navigation bar
  toc_yaml = build_toc_yaml(formatter_per_namespace)
  with catalog_dir.joinpath('_toc.yaml').open('w') as f:
    yaml.dump(toc_yaml, f, default_flow_style=False)

  for namespace, details in build_namespace_details(formatter_per_namespace):
    namespace_file = catalog_dir / f'{namespace}.md'
    namespace_file.write_text(details)


def _get_formatter_per_namespace(
    templates: DocumentationTemplates) -> Mapping[str, NamespaceFormatter]:
  return {
      namespace: formatter_for(
          namespace=namespace, datasets=datasets, templates=templates)
      for namespace, datasets in _get_datasets_per_namespace().items()
  }


def _get_datasets_per_namespace() -> Mapping[str, Sequence[DatasetPackage]]:
  """Retrieves community datasets from GCS and groups them per namespace."""
  content = utils.as_path(gcs_utils.GCS_COMMUNITY_INDEX_PATH).read_text()
  datasets_per_namespace: MutableMapping[str, List[DatasetPackage]] = {}
  for line in content.splitlines():
    dataset_package = DatasetPackage.from_json(json.loads(line))
    namespace = dataset_package.name.namespace
    if not namespace:
      raise ValueError(f'No namespace was specified for {dataset_package}')
    if namespace not in datasets_per_namespace:
      datasets_per_namespace[namespace] = [dataset_package]
    else:
      datasets_per_namespace[namespace].append(dataset_package)
  return datasets_per_namespace


def main(args: argparse.Namespace):
  catalog_dir = args.catalog_dir or os.path.join(
      tfds.core.utils.tfds_write_path(),
      'docs',
      'community_catalog',
  )

  catalog_dir = utils.as_path(catalog_dir)
  build_and_save_community_catalog(catalog_dir=catalog_dir)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)
