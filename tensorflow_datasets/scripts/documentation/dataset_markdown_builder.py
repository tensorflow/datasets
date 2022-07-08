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

"""Dataset catalog documentation template.

Displayed in https://www.tensorflow.org/datasets/catalog/.

"""

import abc
import html
import os
import re
import textwrap
from typing import List, Optional, Union

import tensorflow_datasets as tfds
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.scripts.documentation import doc_utils

Key = Union[int, str]


class Block(str):
  """Indicates whether the content should be blocked (vs inlined).

  Inlined content:

  ```
  * Section: <inlined>
  ```

  Block content:

  ```
  * Section:

  <block>
  ```

  """
  pass


class IntentedBlock(Block):
  """Intented block.

  By default, blocks are stripped to correctly remove extra end-line & cie.
  Intented block will keep the returned formatting.

  """


# Token used to indicate the section shouldn't be displayed
_SKIP_SECTION = object()


class Section(abc.ABC):
  """Abstract class for a documentation Section (description, homepage, ...)."""

  NAME: str
  EXTRA_DOC: str = ''

  @abc.abstractmethod
  def get_key(self, builder: tfds.core.DatasetBuilder) -> Key:
    """Get the key of the section.

    The key is used to merge similar sections across builder configs. For
    instance, https://www.tensorflow.org/datasets/catalog/wiki40b only display
    once the `FeatureDict`, homepage,... as those sections are the same for
    all configs.

    Args:
      builder: The builder to document.

    Returns:
      key: The section key.
    """
    pass

  @abc.abstractmethod
  def content(self, builder: tfds.core.DatasetBuilder) -> str:
    """Returns the section content."""
    pass

  def display(self, builder: tfds.core.DatasetBuilder) -> str:
    """Returns the section content."""
    content = self.content(builder)
    if content is _SKIP_SECTION:
      return ''
    header = f'*   **{self.NAME}**{self.EXTRA_DOC}'
    is_block = isinstance(content, Block)
    if not isinstance(content, IntentedBlock):
      content = content.strip()  # Note: `strip()` cast `Block` -> `str`
    if is_block:
      content = f'{header}:\n\n{content}\n\n'
    else:
      content = f'{header}: {content}\n\n'
    return content


# --------------------------- Builder sections ---------------------------

# pylint:disable = missing-class-docstring


class HomepageSection(Section):

  NAME = 'Homepage'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return builder.info.homepage

  def content(self, builder: tfds.core.DatasetBuilder):
    homepage = builder.info.homepage
    return f'[{homepage}]({homepage})'


class DatasetDescriptionSection(Section):

  NAME = 'Description'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return builder.info.description

  def content(self, builder: tfds.core.DatasetBuilder):
    return Block(builder.info.description)


class ConfigDescriptionSection(Section):

  NAME = 'Config description'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return builder.builder_config.description

  def content(self, builder: tfds.core.DatasetBuilder):
    if not builder.builder_config or not builder.builder_config.description:
      return _SKIP_SECTION
    return builder.builder_config.description


class SourceCodeSection(Section):

  NAME = 'Source code'

  def get_key(self, _):
    return True  # Always common to all configs

  def content(self, builder: tfds.core.DatasetBuilder):
    # TODO(tfds): Display the source code
    if isinstance(builder, tfds.core.read_only_builder.ReadOnlyBuilder):
      return _get_read_only_builder_source_code_link(builder)
    class_path = tfds.core.utils.get_class_path(builder).split('.')
    del class_path[-2]
    class_path = '.'.join(class_path)
    class_url = tfds.core.utils.get_class_url(builder)
    return f'[`{class_path}`]({class_url})'


def _get_read_only_builder_source_code_link(
    builder: tfds.core.DatasetBuilder) -> str:
  """Extract the source code for read-only builder."""
  if 'read_only_builder' in builder.__module__:  # module unknown
    return ('Missing (dataset generated before '
            '[#2813](https://github.com/tensorflow/datasets/issues/2813))')
  url_title = builder.__module__
  module_url = 'https://github.com/tensorflow/datasets'
  # TODO(epot): For datasets built with `tfds build` __module__ correspond
  # to the relative path, not absolute so can't be recover.
  return f'[{url_title}]({module_url})'


class LocationSection(Section):

  NAME = 'Path'

  def get_key(self, _):
    return True  # Always common to all configs

  def content(self, builder: tfds.core.DatasetBuilder):
    # Path is only documented for community datasets
    if (not isinstance(builder, tfds.core.read_only_builder.ReadOnlyBuilder)
        # If datasets have not yet been regenerated after update, even TFDS
        # datasets can be ReadOnlyBuilder
        or builder.__module__.startswith('tensorflow_datasets')):
      return _SKIP_SECTION

    # /.../ds/config/1.0.0/ -> /.../ds/
    path = builder.data_path.parent
    if builder.builder_config:
      path = path.parent
    path = os.fspath(path)

    # Link is automatically added, so can just return the path
    return path  # pylint: disable=protected-access


class VersionSection(Section):

  NAME = 'Versions'

  def __init__(self, nightly_doc_util: Optional[doc_utils.NightlyDocUtil]):
    self._nightly_doc_util = nightly_doc_util

  def _list_versions(self, builder: tfds.core.DatasetBuilder):
    """List versions."""
    curr_versions = set(builder.versions)  # Registered version
    # Merge all versions
    all_versions = [*builder.versions, *builder.release_notes]
    # Normalize and remove duplicates
    all_versions = set(tfds.core.Version(v) for v in all_versions)
    for v in sorted(all_versions):  # List all available versions
      if v == builder.version:  # Highlight the default version
        version_name = '**`{}`** (default)'.format(str(v))
      else:
        version_name = '`{}`'.format(str(v))
      if (v in curr_versions  # Filter versions only present in RELEASE_NOTES
          and self._nightly_doc_util and
          self._nightly_doc_util.is_version_nightly(builder, str(v))):
        nightly_str = ' ' + self._nightly_doc_util.icon
      else:
        nightly_str = ''
      description = builder.release_notes.get(str(v), 'No release notes.')
      yield f'    * {version_name}{nightly_str}: {description}'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    release_key = tuple((k, v) for k, v in builder.release_notes.items())
    return (tuple(builder.versions), release_key)

  def content(self, builder: tfds.core.DatasetBuilder):
    return IntentedBlock('\n'.join(self._list_versions(builder)))


class DownloadSizeSection(Section):

  NAME = 'Download size'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return builder.info.download_size

  def content(self, builder: tfds.core.DatasetBuilder):
    return f'`{builder.info.download_size}`'


class DatasetSizeSection(Section):

  NAME = 'Dataset size'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return builder.info.dataset_size

  def content(self, builder: tfds.core.DatasetBuilder):
    return f'`{builder.info.dataset_size}`'


class ManualDatasetSection(Section):

  NAME = 'Manual download instructions'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return builder.MANUAL_DOWNLOAD_INSTRUCTIONS

  def content(self, builder: tfds.core.DatasetBuilder):
    manual_instructions = builder.MANUAL_DOWNLOAD_INSTRUCTIONS
    if not manual_instructions:
      return _SKIP_SECTION
    manual_instructions = tfds.core.utils.dedent(manual_instructions)
    return textwrap.dedent(f"""
        This dataset requires you to
        download the source data manually into `download_config.manual_dir`
        (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
        {tfds.core.utils.indent(manual_instructions, '        ')}
        """)


class AutocacheSection(Section):

  NAME = 'Auto-cached'
  EXTRA_DOC = (
      ' ([documentation]'
      '(https://www.tensorflow.org/datasets/performances#auto-caching))')

  def _build_autocached_info(self, builder: tfds.core.DatasetBuilder):
    """Returns the auto-cache information string."""
    always_cached = {}
    never_cached = {}
    unshuffle_cached = {}
    for split_name in sorted(builder.info.splits.keys()):
      split_name = str(split_name)
      cache_shuffled = builder._should_cache_ds(  # pylint: disable=protected-access
          split_name,
          shuffle_files=True,
          read_config=tfds.ReadConfig())
      cache_unshuffled = builder._should_cache_ds(  # pylint: disable=protected-access
          split_name,
          shuffle_files=False,
          read_config=tfds.ReadConfig())

      if all((cache_shuffled, cache_unshuffled)):
        always_cached[split_name] = None
      elif not any((cache_shuffled, cache_unshuffled)):
        never_cached[split_name] = None
      else:  # Dataset is only cached when shuffled_files is False
        assert not cache_shuffled and cache_unshuffled
        unshuffle_cached[split_name] = None

    if not len(builder.info.splits) or not builder.info.dataset_size:  # pylint: disable=g-explicit-length-test
      autocached_info = 'Unknown'
    elif len(always_cached) == len(builder.info.splits.keys()):
      autocached_info = 'Yes'  # All splits are auto-cached.
    elif len(never_cached) == len(builder.info.splits.keys()):
      autocached_info = 'No'  # Splits never auto-cached.
    else:  # Some splits cached, some not.
      autocached_info_parts = []
      if always_cached:
        split_names_str = ', '.join(always_cached)
        autocached_info_parts.append('Yes ({})'.format(split_names_str))
      if never_cached:
        split_names_str = ', '.join(never_cached)
        autocached_info_parts.append('No ({})'.format(split_names_str))
      if unshuffle_cached:
        split_names_str = ', '.join(unshuffle_cached)
        autocached_info_parts.append(
            'Only when `shuffle_files=False` ({})'.format(split_names_str))
      autocached_info = ', '.join(autocached_info_parts)
    return autocached_info

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return self._build_autocached_info(builder)

  def content(self, builder: tfds.core.DatasetBuilder):
    return self._build_autocached_info(builder)


class SplitInfoSection(Section):

  NAME = 'Splits'

  def _get_num_examples(self, split_info):
    if split_info.num_examples:
      return '{:,}'.format(split_info.num_examples)
    return 'Not computed'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return tuple((str(s.name), int(s.num_examples))
                 for s in builder.info.splits.values())

  def content(self, builder: tfds.core.DatasetBuilder):
    splits_str = ('\n').join([
        f'`\'{split_name}\'` | {self._get_num_examples(split_info)}'
        for split_name, split_info in sorted(builder.info.splits.items())
    ])
    return Block(
        textwrap.dedent(f"""
            Split  | Examples
            :----- | -------:
            {tfds.core.utils.indent(splits_str, '            ')}
            """))


class FeatureInfoSection(Section):

  NAME = 'Feature structure'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return repr(builder.info.features)

  def features_content(self, features: tfds.features.FeatureConnector) -> Block:
    code = textwrap.dedent("""
        ```python
        {}
        ```
        """).format(features)
    return Block(code)

  def content(self, builder: tfds.core.DatasetBuilder):
    return self.features_content(builder.info.features)


class FeatureDocumentationSection(Section):

  NAME = 'Feature documentation'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return repr(builder.info.features)

  def _format_feature_rows(
      self,
      feature_docs: List[feature_lib.CatalogFeatureDocumentation],
      should_show_value_range: bool,
  ) -> List[str]:
    """Return the formatted rows for each feature (sorted by feature name)."""

    def format_row(doc: feature_lib.CatalogFeatureDocumentation) -> str:
      if doc.tensor_info:
        shape = str(doc.tensor_info.shape) if doc.tensor_info.shape else ''
        dtype = repr(doc.tensor_info.dtype) if doc.tensor_info.dtype else ''
      else:
        shape = ''
        dtype = ''
      parts = [doc.name, doc.cls_name, shape, dtype, doc.description]
      if should_show_value_range:
        parts.append(doc.value_range)
      parts = [part or '' for part in parts]
      return ' | '.join(parts)

    rows = []
    for feature_doc in sorted(feature_docs):
      rows.append(format_row(feature_doc))
    return rows

  def _should_show_value_range(
      self,
      feature_docs: List[feature_lib.CatalogFeatureDocumentation]) -> bool:
    return any(doc.value_range for doc in feature_docs)

  def _format_block(
      self,
      feature_docs: List[feature_lib.CatalogFeatureDocumentation],
  ) -> Block:
    """Formats a block containing all the feature documentation."""
    should_show_value_range = self._should_show_value_range(feature_docs)
    feature_rows = self._format_feature_rows(feature_docs,
                                             should_show_value_range)
    header = ['Feature', 'Class', 'Shape', 'Dtype', 'Description']
    if should_show_value_range:
      header.append('Value range')
    header_line = map(lambda h: ':' + ('-' * (len(h) - 1)), header)
    col_sep = ' | '
    return Block('\n'.join(
        [col_sep.join(header), col_sep.join(header_line)] + feature_rows))

  def content(self, builder: tfds.core.DatasetBuilder) -> str:
    if builder.info is None or builder.info.features is None:
      return ''
    return self._format_block(builder.info.features.catalog_documentation())


class SupervisedKeySection(Section):

  NAME = 'Supervised keys'
  EXTRA_DOC = (
      ' (See [`as_supervised` doc]'
      '(https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args))')

  def get_key(self, builder: tfds.core.DatasetBuilder) -> Key:
    # get_key() must return a Key (str/int), but supervised_keys can be a tuple
    # or dict. Keys also need to be hashable, but dicts are mutable and tuples
    # can contain mutable entries, so use repr as a snapshot.
    return repr(builder.info.supervised_keys)

  def content(self, builder: tfds.core.DatasetBuilder):
    return f'`{str(builder.info.supervised_keys)}`'


class DatasetCitationSection(Section):

  NAME = 'Citation'

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return builder.info.citation

  def content(self, builder: tfds.core.DatasetBuilder):
    if not builder.info.citation:
      return ''
    return Block(
        textwrap.dedent(f"""
            ```
            {tfds.core.utils.indent(builder.info.citation, '            ')}
            ```
            """))


class KnowYourDataSection(Section):

  NAME = 'Visualization'

  def __init__(self):
    super().__init__()
    self._catalog_urls = {}

  def get_key(self, builder: tfds.core.DatasetBuilder):
    return None  # Single url for all configs

  def content(self, builder: tfds.core.DatasetBuilder):
    url = self._catalog_urls.get(builder.name)
    if url:
      return f"""
        <a class="button button-with-icon" href="{url}">
          Explore in Know Your Data
          <span class="material-icons icon-after" aria-hidden="true">
            north_east
          </span>
        </a>
      """
    else:
      return _SKIP_SECTION


class DatasetVisualizationSection(Section):

  NAME = 'Figure'
  EXTRA_DOC = (
      ' ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))'
  )

  def __init__(self, visualization_util):
    self._visualization_util = visualization_util

  def get_key(self, builder: tfds.core.DatasetBuilder):
    if self._visualization_util.has_visualization(builder):
      return builder.info.full_name
    return None  # Fuse the sections together if no configs are available

  def content(self, builder: tfds.core.DatasetBuilder):
    if not self._visualization_util.has_visualization(builder):
      return 'Not supported.'
    return Block(self._visualization_util.get_html_tag(builder))


class DatasetDataframeSection(Section):

  NAME = 'Examples'
  EXTRA_DOC = (
      ' ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe))'
  )
  # Artificially limit the amount of dataframe blocks to optimize page loading.
  _MAX_DATAFRAME_BLOCKS = 100

  def __init__(self, dataframe_util):
    self._dataframe_util = dataframe_util
    self._blocks_generated = 0

  def get_key(self, builder: tfds.core.DatasetBuilder):
    if self._dataframe_util.has_visualization(builder):
      return builder.info.full_name
    return None  # Fuse the sections together if no configs are available

  def content(self, builder: tfds.core.DatasetBuilder):
    if self._blocks_generated >= self._MAX_DATAFRAME_BLOCKS:
      return f'Only shown for the first {self._MAX_DATAFRAME_BLOCKS} configs.'
    if not self._dataframe_util.has_visualization(builder):
      return 'Missing.'
    self._blocks_generated += 1
    return Block(self._dataframe_util.get_html_tag(builder))


# pylint:enable = missing-class-docstring

# --------------------------- Single builder ---------------------------


def _display_builder(
    builder: tfds.core.DatasetBuilder,
    sections: List[Section],
) -> str:
  """Display a single Builder / BuilderConfig."""
  # Note: Section may be a subset of the section to display
  return ''.join(section.display(builder) for section in sections)


# --------------------------- Builder configs ---------------------------


def _display_all_builders(
    namespace: Optional[str],
    nightly_doc_util: Optional[doc_utils.NightlyDocUtil],
    builders: List[tfds.core.DatasetBuilder],
    all_sections: List[Section],
) -> str:
  """Display all sections for all Builder."""
  # For each fields, extract if the field is shared or unique accross builder.
  common_sections = []
  unique_sections = []
  for section in all_sections:
    if len(set(section.get_key(b) for b in builders)) == 1:
      common_sections.append(section)
    else:
      unique_sections.append(section)

  common_builder_str = _display_builder(next(iter(builders)), common_sections)

  unique_builder_str = []
  for i, builder in enumerate(builders):
    header_suffix = ' (default config)' if i == 0 else ''
    if nightly_doc_util and nightly_doc_util.is_config_nightly(builder):
      nightly_str = ' ' + nightly_doc_util.icon
    else:
      nightly_str = ''
    ds_name = tfds.core.naming.DatasetName(
        namespace=namespace,
        name=builder.name,
    )
    unique_builder_str.append(f'## {ds_name}/{builder.builder_config.name}'
                              f'{header_suffix}{nightly_str}\n')
    unique_builder_str.append(_display_builder(builder, unique_sections))
  unique_builder_str = '\n'.join(unique_builder_str)

  return common_builder_str + '\n' + unique_builder_str


# --------------------------- Main page ---------------------------


def _display_dataset_heading(
    namespace: Optional[str],
    builder: tfds.core.DatasetBuilder,
) -> str:
  ds_name = tfds.core.naming.DatasetName(namespace=namespace, name=builder.name)
  return f"""
      # `{ds_name}`

      """


def _display_nightly_str(
    nightly_doc_util: Optional[doc_utils.NightlyDocUtil],
    builder: tfds.core.DatasetBuilder,
) -> str:
  """Header nightly note section."""
  if nightly_doc_util and nightly_doc_util.is_builder_nightly(builder):
    return f"""\
      Note: This dataset was added recently and is only available in our
      `tfds-nightly` package  {nightly_doc_util.icon}.
      """
  elif nightly_doc_util and nightly_doc_util.has_nightly(builder):
    return f"""\
      Note: This dataset has been updated since the last stable release.
      The new versions and config marked with {nightly_doc_util.icon}
      are only available in the `tfds-nightly` package.
      """
  else:
    return ''


def _display_manual_instructions(builder: tfds.core.DatasetBuilder):
  """Header manual note section."""
  if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
    return 'Warning: Manual download required. See instructions below.'
  return ''


def _display_builder_configs(
    builder: tfds.core.DatasetBuilder,
    namespace: Optional[str],
    nightly_doc_util: Optional[doc_utils.NightlyDocUtil],
    config_builders: List[tfds.core.DatasetBuilder],
    all_sections: List[Section],
) -> str:
  """Builder configs."""
  # First case: Single builder
  if not builder.builder_config:
    return _display_builder(builder, all_sections)
  # Second case: Builder configs
  return _display_all_builders(
      nightly_doc_util=nightly_doc_util,
      namespace=namespace,
      builders=config_builders,
      all_sections=all_sections,
  )


def _escape(val: str) -> str:
  val = html.escape(val, quote=True)
  val = val.replace('\n', '&#10;')
  val = val.strip()
  return val


def _display_schema_org(
    builder: tfds.core.DatasetBuilder,
    visu_doc_util: Optional[doc_utils.VisualizationDocUtil],
) -> str:
  r"""Builds schema.org microdata for DatasetSearch from DatasetBuilder.

  Specs: https://developers.google.com/search/docs/data-types/dataset#dataset
  Testing tool: https://search.google.com/structured-data/testing-tool
  For Google Dataset Search: https://toolbox.google.com/datasetsearch

  Microdata format was chosen over JSON-LD due to the fact that Markdown
  rendering engines remove all \<script\> tags.

  Args:
    builder: Dataset to document
    visu_doc_util: Visualization util

  Returns:
    schema_org: The schema.org
  """
  description = f"""

  To use this dataset:

  ```python
  import tensorflow_datasets as tfds

  ds = tfds.load('{builder.info.name}', split='train')
  for ex in ds.take(4):
    print(ex)
  ```

  See [the guide](https://www.tensorflow.org/datasets/overview) for more
  informations on [tensorflow_datasets](https://www.tensorflow.org/datasets).

  """
  description = builder.info.description + textwrap.dedent(description)
  if visu_doc_util and visu_doc_util.has_visualization(builder):
    description += visu_doc_util.get_html_tag(builder) + '\n\n'

  text = f"""\
  <div itemscope itemtype="http://schema.org/Dataset">
    <div itemscope itemprop="includedInDataCatalog" itemtype="http://schema.org/DataCatalog">
      <meta itemprop="name" content="TensorFlow Datasets" />
    </div>
    <meta itemprop="name" content="{builder.info.name}" />
    <meta itemprop="description" content="{_escape(description)}" />
    <meta itemprop="url" content="https://www.tensorflow.org/datasets/catalog/{builder.info.name}" />
    <meta itemprop="sameAs" content="{_escape(builder.info.homepage)}" />
    <meta itemprop="citation" content="{_escape(builder.info.citation)}" />
  </div>
  """
  text = textwrap.dedent(text)
  return text


def get_markdown_string(
    *,
    builder: tfds.core.DatasetBuilder,
    config_builders: List[tfds.core.DatasetBuilder],
    namespace: Optional[str],
    visu_doc_util: Optional[doc_utils.VisualizationDocUtil],
    df_doc_util: Optional[doc_utils.DataframeDocUtil],
    nightly_doc_util: Optional[doc_utils.NightlyDocUtil],
) -> str:
  """Build the dataset markdown."""

  all_sections = [
      KnowYourDataSection(),
      DatasetDescriptionSection(),
      ConfigDescriptionSection(),
      HomepageSection(),
      SourceCodeSection(),
      LocationSection(),
      VersionSection(nightly_doc_util),
      DownloadSizeSection(),
      DatasetSizeSection(),
      ManualDatasetSection(),
      AutocacheSection(),
      SplitInfoSection(),
      FeatureInfoSection(),
      FeatureDocumentationSection(),
      SupervisedKeySection(),
  ]
  if visu_doc_util:
    all_sections.append(DatasetVisualizationSection(visu_doc_util))
  if df_doc_util:
    all_sections.append(DatasetDataframeSection(df_doc_util))
  all_sections.append(DatasetCitationSection())

  doc_str = [
      _display_schema_org(builder, visu_doc_util),
      _display_dataset_heading(namespace, builder),
      _display_nightly_str(nightly_doc_util, builder),
      _display_manual_instructions(builder),
      _display_builder_configs(
          builder=builder,
          namespace=namespace,
          nightly_doc_util=nightly_doc_util,
          config_builders=config_builders,
          all_sections=all_sections,
      ),
  ]
  return '\n\n'.join([tfds.core.utils.dedent(s) for s in doc_str if s])
