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

r"""Tool to generate the dataset community catalog documentation.
"""

import argparse
import dataclasses
import datetime
import json
import os
import re
import textwrap
from typing import Any, Iterator, List, Mapping, MutableMapping, Optional, Sequence, Tuple

from absl import app
from absl.flags import argparse_flags

from etils import epath
import tensorflow_datasets as tfds
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import register_package
from tensorflow_datasets.core.github_api import github_path
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.core.proto import feature_pb2
from tensorflow_datasets.core.utils import gcs_utils
from tensorflow_datasets.core.utils import py_utils
import yaml

DatasetPackage = register_package.DatasetPackage

_INDEX_TEMPLATE_PATH = (
    'scripts/documentation/templates/community_catalog_overview.md'
)
_DATASET_DETAILS_TEMPLATE_PATH = (
    'scripts/documentation/templates/community_namespace_dataset.md'
)
_NAMESPACE_TOC_TEMPLATE_PATH = (
    'scripts/documentation/templates/community_namespace_toc.md'
)


@dataclasses.dataclass()
class _Options:
  catalog_dir: epath.Path
  local_cache: Optional[str] = None


def _parse_flags(_: List[str]) -> argparse.Namespace:
  """Command line flags."""
  parser = argparse_flags.ArgumentParser(
      prog='build_community_catalog',
      description='Tool to generate the community dataset catalog',
  )
  parser.add_argument(
      '--catalog_dir',
      help='Directory path where to generate the catalog. Default to TFDS dir.',
  )
  parser.add_argument(
      '--local_cache',
      help=(
          'If specified, where to store temporarily downloaded files so that '
          'they can be reused when running multiple times.'
      ),
  )
  return parser.parse_args()


def _load_template(template_path: str) -> str:
  return tfds.core.tfds_path(template_path).read_text()


def _to_toc_yaml(
    *,
    title: str,
    relative_path: str,
    page: str,
) -> Mapping[str, Any]:
  return {
      'title': title,
      'path': os.path.join(relative_path, page),
  }


def _clean_up_text(text: str) -> str:
  """Removes illegal characters from the given text."""
  return re.sub(r'```', '', text).strip()


def _get_huggingface_features(config: Mapping[str, Any]) -> feature_pb2.Feature:
  """Parses a huggingface config to a Feature proto."""
  return feature_pb2.Feature(
      json_feature=feature_pb2.JsonFeature(
          json=json.dumps(config['features'], indent=4)
      )
  )


def _get_cached_copy(file_path: epath.Path, max_age_days: int) -> Optional[str]:
  if file_path.exists():
    stats = os.stat(file_path)
    modified_time = datetime.datetime.fromtimestamp(stats.st_mtime)
    if modified_time > datetime.datetime.now() - datetime.timedelta(
        days=max_age_days
    ):
      return file_path.read_text()
  return None


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
  options: _Options

  @property
  def tfds_id(self) -> str:
    """Returns the ID to use when loading this dataset in TFDS."""
    return str(self.dataset.name)

  @property
  def name(self) -> str:
    return self.dataset.name.name

  @property
  def namespace(self) -> str:
    return self.dataset.name.namespace

  def code_url(self, title: str = 'Code') -> str:
    return f'[{title}]({self.dataset.source.root_path})'

  def to_namespace_overview(self) -> str:
    """Returns the entry to be shown in the overview for a single namespace."""
    template = textwrap.dedent('*  [{dataset}]({namespace}/{dataset}.md)')
    return template.format(
        dataset=self.name,
        namespace=self.namespace,
    )

  def to_details_markdown(self) -> str:
    """ "Markdown to be shown on the details page for the namespace."""
    extra_links = self.format_extra_links(prefix='*   ', infix='\n')
    details = self.templates.dataset_details_template.format(
        name=self.name,
        description=self.documentation(),
        namespace=self.namespace,
        tfds_id=self.tfds_id,
        references_bulleted_list=extra_links,
    )
    if len(details) < 2 * 1024 * 1024:
      return details
    return self.templates.dataset_details_template.format(
        name=self.name,
        description=self.documentation(keep_short=True),
        namespace=self.namespace,
        tfds_id=self.tfds_id,
        references_bulleted_list=extra_links,
    )

  def dataset_info_per_config(
      self,
  ) -> Mapping[str, dataset_info_pb2.DatasetInfo]:
    return {}

  def documentation(self, keep_short: bool = False) -> str:
    """Returns detailed documentation for all configs of this dataset."""
    # TODO(weide): if e.g. the description contains markdown chars, then it
    # messes up the page. Try escaping backticks or using code blocks.
    # TODO(weide): how to format citation?
    header_template = '## {config_name}'
    template = textwrap.dedent(
        """
      Use the following command to load this dataset in TFDS:

      ```python
      ds = tfds.load('{tfds_id}')
      ```

      *   **Description**:

      ```
      {description}
      ```

      *   **License**: {license}
      *   **Version**: {version}
      *   **Splits**:
      {splits}
      *   **Features**:
      {features}
    """
    )

    #       *   **Citation**: `{citation}`

    def format_splits(split_infos: Sequence[dataset_info_pb2.SplitInfo]) -> str:
      splits_str = ('\n').join(
          sorted(
              [
                  f"`'{split.name}'` | {sum(split.shard_lengths)}"
                  for split in split_infos
              ]
          )
      )
      return textwrap.dedent(
          f"""
            Split  | Examples
            :----- | -------:
            {py_utils.indent(splits_str, '            ')}
            """
      )

    def format_feature(feature: feature_pb2.Feature) -> str:
      if feature.HasField('json_feature'):
        return textwrap.dedent(
            f"""
```json
{feature.json_feature.json}
```
                               """
        )
      if feature.HasField('features_dict'):
        descriptions = [
            f'    *   `{name}`'
            for name, _ in feature.features_dict.features.items()
        ]
        return '\n'.join(descriptions)
      return ''

    def format_template(
        config_name: str, info: dataset_info_pb2.DatasetInfo
    ) -> str:
      if config_name == 'default':
        tfds_id = self.tfds_id
      else:
        tfds_id = f'{self.tfds_id}/{config_name}'
      if keep_short:
        features = ''
      else:
        features = format_feature(info.features)
      content = template.format(
          description=_clean_up_text(info.description),
          tfds_id=tfds_id,
          license=info.redistribution_info.license or 'No known license',
          version=info.version,
          splits=format_splits(info.splits),
          features=features,
          citation=info.citation,
      )
      if config_name == 'default':
        return content
      return '{header}\n\n{content}'.format(
          header=header_template.format(config_name=config_name),
          content=content,
      )

    # homepage=default_dataset['homepage'],
    config_descriptions = [
        format_template(config_name, info)
        for config_name, info in self.dataset_info_per_config().items()
    ]

    return '\n\n'.join(config_descriptions)

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

  @utils.memoized_property
  def dataset_infos(self) -> utils.JsonValue:
    """Retrieves the dataset info from either a cached copy or from Github."""

    content = None
    tmp_file_path = None
    if self.options.local_cache:
      tmp_ds_path = epath.Path(self.options.local_cache) / self.name
      tmp_ds_path.mkdir(exist_ok=True, parents=True)
      tmp_file_path = tmp_ds_path / 'dataset_infos.json'
      content = _get_cached_copy(file_path=tmp_file_path, max_age_days=14)

    if not content:
      try:
        dataset_info_path = self.gh_path / 'dataset_infos.json'
        print(f'Retrieving {dataset_info_path.as_raw_url()}')
        content = github_path.get_content(dataset_info_path.as_raw_url())
        if tmp_file_path:
          tmp_file_path.write_text(content.decode())
      except FileNotFoundError:
        return {}
    return json.loads(content)

  def extra_links(self) -> Sequence[str]:
    return [self.code_url(), self.huggingface_link()]

  def _parse_dataset_info_proto(
      self, config_name: str, config: Mapping[str, Any]
  ) -> dataset_info_pb2.DatasetInfo:
    """Parses a DatasetInfo proto from the given Json."""

    splits = []
    for name, details in config['splits'].items():
      splits.append(
          dataset_info_pb2.SplitInfo(
              name=name,
              num_shards=1,
              shard_lengths=[details['num_examples']],
              num_bytes=details['num_bytes'],
          )
      )

    if isinstance(config['version'], dict):
      version = config['version']['version_str']
    elif isinstance(config['version'], str):
      version = config['version']
    return dataset_info_pb2.DatasetInfo(
        name=config_name,
        module_name=config_name,
        description=config['description'],
        version=version,
        citation=config['citation'],
        redistribution_info=dataset_info_pb2.RedistributionInfo(
            license=config['license']
        ),
        splits=splits,
        features=_get_huggingface_features(config),
    )

  def dataset_info_per_config(
      self,
  ) -> Mapping[str, dataset_info_pb2.DatasetInfo]:
    if not isinstance(self.dataset_infos, dict):
      return {}
    return {
        config_name: self._parse_dataset_info_proto(config_name, config)
        for config_name, config in self.dataset_infos.items()
    }


@dataclasses.dataclass()
class NamespaceFormatter:
  """A documentation formatter for a namespace and all its datasets."""

  namespace: str
  datasets: Sequence[DatasetPackage]
  templates: DocumentationTemplates
  options: _Options

  @property
  def name(self) -> str:
    return self.namespace.capitalize()

  @property
  def overview_page(self) -> str:
    return f'{self.namespace}.md'

  def sections(self) -> Sequence[DatasetDocumentation]:
    return [
        DatasetDocumentation(
            dataset=ds, templates=self.templates, options=self.options
        )
        for ds in self.datasets
    ]

  def to_namespace_overview(self) -> str:
    """Markdown with dataset details for the namespace dataset overview."""
    sections = '\n'.join(
        [section.to_namespace_overview() for section in self.sections()]
    )
    template = textwrap.dedent(
        """
      # {self.name} datasets


      {sections}
      """
    )
    return template.format(sections=sections)

  def to_toc_markdown(self) -> str:
    datasets_for_toc = '\n'.join(
        [f'*   {section.to_toc_markdown()}' for section in self.sections()]
    )
    return self.templates.namespace_toc_template.format(
        name=self.name,
        namespace=self.namespace,
        overview_page=self.overview_page,
        num_datasets=len(self.datasets),
        datasets_for_toc=datasets_for_toc,
    )

  def to_toc_yaml(self, toc_relative_path: str):
    return _to_toc_yaml(
        title=self.name, relative_path=toc_relative_path, page=self.namespace
    )


@dataclasses.dataclass()
class HuggingfaceFormatter(NamespaceFormatter):
  """Specialized formatter for Huggingface."""

  def sections(self) -> Sequence[DatasetDocumentation]:
    return [
        HuggingfaceDatasetDocumentation(
            dataset=ds, templates=self.templates, options=self.options
        )
        for ds in self.datasets
    ]

  def to_namespace_overview(self) -> str:
    for section in self.sections():
      section.documentation()
    sections = '\n'.join(
        [section.to_namespace_overview() for section in self.sections()]
    )
    template = textwrap.dedent(
        """\
      # Huggingface datasets

      Huggingface has forked TFDS and provides a lot of text datasets. See
      [here](https://huggingface.co/docs/datasets/) for more documentation.
      Next you can find the list of all the datasets that can be used with TFDS.


      {sections}
      """
    )
    return template.format(sections=sections)


def formatter_for(
    namespace: str,
    datasets: Sequence[DatasetPackage],
    templates: DocumentationTemplates,
    options: _Options,
) -> NamespaceFormatter:
  """Returns the formatter for the given namespace and datasets."""
  if namespace == 'huggingface':
    return HuggingfaceFormatter(
        namespace=namespace,
        datasets=datasets,
        templates=templates,
        options=options,
    )
  return NamespaceFormatter(
      namespace=namespace,
      datasets=datasets,
      templates=templates,
      options=options,
  )


def build_overview(
    formatter_per_namespace: Mapping[str, NamespaceFormatter],
    templates: DocumentationTemplates,
) -> str:
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
    namespace_overview_markdown = formatter.to_namespace_overview()
    yield namespace, namespace_overview_markdown


def build_namespace_dataset_details(
    formatter: NamespaceFormatter,
) -> Iterator[Tuple[str, str]]:
  """Generates all the detail pages for all namespaces and datasets."""
  for section in formatter.sections():
    yield section.name, section.to_details_markdown()


def build_toc_yaml(
    formatter_per_namespace: Mapping[str, NamespaceFormatter]
) -> Mapping[str, Any]:
  """Returns a mapping representing the TOC (to be converted into Yaml)."""
  toc_relative_path = '/datasets/community_catalog'
  sections = [
      _to_toc_yaml(
          title='Overview', relative_path=toc_relative_path, page='overview'
      )
  ]
  for _, formatter in sorted(formatter_per_namespace.items()):
    sections.append(formatter.to_toc_yaml(toc_relative_path))
  return {'toc': sections}


def build_and_save_community_catalog(options: _Options) -> None:
  """Builds and saves the catalog of community datasets."""
  templates = DocumentationTemplates.load()
  formatter_per_namespace = _get_formatter_per_namespace(
      templates=templates, options=options
  )

  overview = build_overview(formatter_per_namespace, templates)
  options.catalog_dir.joinpath('overview.md').write_text(overview)

  # Write the `_toc.yaml` TF documentation navigation bar
  toc_yaml = build_toc_yaml(formatter_per_namespace)
  with options.catalog_dir.joinpath('_toc.yaml').open('w') as f:
    yaml.dump(toc_yaml, f, default_flow_style=False)

  for namespace, details in build_namespace_details(formatter_per_namespace):
    namespace_file = options.catalog_dir / f'{namespace}.md'
    namespace_file.write_text(details)

  for namespace, formatter in formatter_per_namespace.items():
    namespace_folder = options.catalog_dir / namespace
    namespace_folder.mkdir(exist_ok=True)
    for dataset_name, markdown in build_namespace_dataset_details(formatter):
      dataset_file = namespace_folder / f'{dataset_name}.md'
      dataset_file.write_text(markdown)


def _get_formatter_per_namespace(
    templates: DocumentationTemplates,
    options: _Options,
) -> Mapping[str, NamespaceFormatter]:
  """Returns the formatter per namespace."""
  formatters = {}
  for namespace, datasets in _get_datasets_per_namespace().items():
    formatters[namespace] = formatter_for(
        namespace=namespace,
        datasets=datasets,
        templates=templates,
        options=options,
    )
  return formatters


def _get_datasets_per_namespace() -> Mapping[str, Sequence[DatasetPackage]]:
  """Retrieves community datasets from GCS and groups them per namespace."""
  content = epath.Path(gcs_utils.GCS_COMMUNITY_INDEX_PATH).read_text()
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

  options = _Options(
      catalog_dir=epath.Path(catalog_dir), local_cache=args.local_cache or None
  )
  build_and_save_community_catalog(options=options)


if __name__ == '__main__':
  app.run(main, flags_parser=_parse_flags)
