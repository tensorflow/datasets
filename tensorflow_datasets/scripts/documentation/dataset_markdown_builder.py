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

"""Dataset catalog documentation template.

Displayed in https://www.tensorflow.org/datasets/catalog/.

"""

import abc
import textwrap
from typing import List, Union

import tensorflow_datasets as tfds


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
      return f'{header}:\n\n{content}\n\n'
    else:
      return f'{header}: {content}\n\n'

# --------------------------- Builder sections ---------------------------

# pylint:disable = missing-class-docstring


class HomepageSection(Section):

  NAME = 'Homepage'

  def get_key(self, builder):
    return builder.info.homepage

  def content(self, builder):
    homepage = builder.info.homepage
    return f'[{homepage}]({homepage})'


class DatasetDescriptionSection(Section):

  NAME = 'Description'

  def get_key(self, builder):
    return builder.info.description

  def content(self, builder):
    return Block(builder.info.description)


class ConfigDescriptionSection(Section):

  NAME = 'Config description'

  def get_key(self, builder):
    return builder.builder_config.description

  def content(self, builder):
    if not builder.builder_config:
      return _SKIP_SECTION
    return builder.builder_config.description


class SourceCodeSection(Section):

  NAME = 'Source code'

  def get_key(self, _):
    return True  # Always common to all configs

  def content(self, builder):
    class_path = tfds.core.utils.get_class_path(builder).split('.')
    del class_path[-2]
    class_path = '.'.join(class_path)
    class_url = tfds.core.utils.get_class_url(builder)
    return f'[`{class_path}`]({class_url})'


class VersionSection(Section):

  NAME = 'Versions'

  def __init__(self, nightly_doc_util):
    self._nightly_doc_util = nightly_doc_util

  def _list_versions(self, builder):
    """List versions."""
    for v in builder.versions:  # List all available versions (in default order)
      if v == builder.version:  # Highlight the default version
        version_name = '**`{}`** (default)'.format(str(v))
      else:
        version_name = '`{}`'.format(str(v))
      if self._nightly_doc_util.is_version_nightly(builder, str(v)):
        nightly_str = ' ' + self._nightly_doc_util.icon
      else:
        nightly_str = ''
      yield '    * {}{}: {}'.format(
          version_name, nightly_str, v.description or 'No release notes.'
      )

  def get_key(self, builder):
    return tuple((str(v), v.description) for v in builder.versions)

  def content(self, builder):
    return IntentedBlock('\n'.join(self._list_versions(builder)))


class DownloadSizeSection(Section):

  NAME = 'Download size'

  def get_key(self, builder):
    return builder.info.download_size

  def content(self, builder):
    return f'`{tfds.units.size_str(builder.info.download_size)}`'


class DatasetSizeSection(Section):

  NAME = 'Dataset size'

  def get_key(self, builder):
    return builder.info.dataset_size

  def content(self, builder):
    return f'`{tfds.units.size_str(builder.info.dataset_size)}`'


class ManualDatasetSection(Section):

  NAME = 'Manual download instructions'

  def get_key(self, builder):
    return builder.MANUAL_DOWNLOAD_INSTRUCTIONS

  def content(self, builder):
    manual_instructions = builder.MANUAL_DOWNLOAD_INSTRUCTIONS
    if not manual_instructions:
      return _SKIP_SECTION
    return textwrap.dedent(
        f"""
        This dataset requires you to
        download the source data manually into `download_config.manual_dir`
        (defaults to `~/tensorflow_datasets/downloads/manual/`):<br/>
        {tfds.core.utils.indent(manual_instructions, '        ')}
        """
    )


class AutocacheSection(Section):

  NAME = 'Auto-cached'
  EXTRA_DOC = (
      ' ([documentation]'
      '(https://www.tensorflow.org/datasets/performances#auto-caching))'
  )

  def _build_autocached_info(self, builder):
    """Returns the auto-cache information string."""
    always_cached = {}
    never_cached = {}
    unshuffle_cached = {}
    for split_name in sorted(builder.info.splits.keys()):
      split_name = str(split_name)
      cache_shuffled = builder._should_cache_ds(  # pylint: disable=protected-access
          split_name, shuffle_files=True, read_config=tfds.ReadConfig())
      cache_unshuffled = builder._should_cache_ds(  # pylint: disable=protected-access
          split_name, shuffle_files=False, read_config=tfds.ReadConfig())

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

  def get_key(self, builder):
    return self._build_autocached_info(builder)

  def content(self, builder):
    return self._build_autocached_info(builder)


class SplitInfoSection(Section):

  NAME = 'Splits'

  def _get_num_examples(self, split_info):
    if split_info.num_examples:
      return '{:,}'.format(split_info.num_examples)
    return 'Not computed'

  def get_key(self, builder):
    return tuple(
        (str(s.name), int(s.num_examples)) for s in builder.info.splits.values()
    )

  def content(self, builder):
    splits_str = ('\n').join([
        f'`\'{split_name}\'` | {self._get_num_examples(split_info)}'
        for split_name, split_info in sorted(builder.info.splits.items())
    ])
    return Block(
        textwrap.dedent(
            f"""
            Split  | Examples
            :----- | -------:
            {tfds.core.utils.indent(splits_str, '            ')}
            """
        )
    )


class FeatureInfoSection(Section):

  NAME = 'Features'

  def get_key(self, builder):
    return repr(builder.info.features)

  def content(self, builder):
    code = textwrap.dedent(
        """
        ```python
        {}
        ```
        """
    ).format(builder.info.features)
    return Block(code)


class SupervisedKeySection(Section):

  NAME = 'Supervised keys'
  EXTRA_DOC = (
      ' (See [`as_supervised` doc]'
      '(https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args))'
  )

  def get_key(self, builder):
    return builder.info.supervised_keys

  def content(self, builder):
    return f'`{str(builder.info.supervised_keys)}`'


class DatasetCitationSection(Section):

  NAME = 'Citation'

  def get_key(self, builder):
    return builder.info.citation

  def content(self, builder):
    if not builder.info.citation:
      return ''
    return Block(
        textwrap.dedent(
            f"""
            ```
            {tfds.core.utils.indent(builder.info.citation, '            ')}
            ```
            """
        )
    )


class DatasetVisualizationSection(Section):

  NAME = 'Figure'
  EXTRA_DOC = (
      ' ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))'
  )

  def __init__(self, visualization_util):
    self._visualization_util = visualization_util

  def get_key(self, builder):
    if self._visualization_util.has_visualization(builder):
      return builder.info.full_name
    return None  # Fuse the sections together if no configs are available

  def content(self, builder):
    if not self._visualization_util.has_visualization(builder):
      return 'Not supported.'
    return Block(self._visualization_util.get_html_tag(builder))


class DatasetDataframeSection(Section):

  NAME = 'Examples'
  EXTRA_DOC = (
      ' ([tfds.as_dataframe](https://www.tensorflow.org/datasets/api_docs/python/tfds/as_dataframe))'
  )

  def __init__(self, dataframe_util):
    self._dataframe_util = dataframe_util

  def get_key(self, builder):
    if self._dataframe_util.has_visualization(builder):
      return builder.info.full_name
    return None  # Fuse the sections together if no configs are available

  def content(self, builder):
    if not self._dataframe_util.has_visualization(builder):
      return 'Missing.'
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
    nightly_doc_util,
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
    nightly_str = (' ' + nightly_doc_util.icon) \
        if nightly_doc_util.is_config_nightly(builder) else ''
    unique_builder_str.append(
        f'## {builder.name}/{builder.builder_config.name}'
        f'{header_suffix}{nightly_str}\n')
    unique_builder_str.append(_display_builder(builder, unique_sections))
  unique_builder_str = '\n'.join(unique_builder_str)

  return common_builder_str + '\n' + unique_builder_str


# --------------------------- Main page ---------------------------


def _display_dataset_heading(builder):
  return f'# `{builder.name}`'


def _display_nightly_str(nightly_doc_util, builder):
  """Header nightly note section."""
  if nightly_doc_util.is_builder_nightly(builder):
    return f"""\
      Note: This dataset was added recently and is only available in our
      `tfds-nightly` package  {nightly_doc_util.icon}.
      """
  elif nightly_doc_util.has_nightly(builder):
    return f"""\
      Note: This dataset has been updated since the last stable release.
      The new versions and config marked with {nightly_doc_util.icon}
      are only available in the `tfds-nightly` package.
      """
  else:
    return ''


def _display_manual_instructions(builder):
  """Header manual note section."""
  if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
    return 'Warning: Manual download required. See instructions below.'
  return ''


def _display_builder_configs(
    builder: tfds.core.DatasetBuilder,
    nightly_doc_util,
    config_builders: List[tfds.core.DatasetBuilder],
    all_sections: List[Section],
) -> str:
  """Builder configs."""
  # First case: Single builder
  if not builder.builder_config:
    return _display_builder(builder, all_sections)
  # Second case: Builder configs
  return _display_all_builders(nightly_doc_util, config_builders, all_sections)


def get_markdown_string(
    builder: tfds.core.DatasetBuilder,
    config_builders: List[tfds.core.DatasetBuilder],
    visu_doc_util,
    df_doc_util,
    nightly_doc_util,
) -> str:
  """Build the dataset markdown."""

  all_sections = [
      DatasetDescriptionSection(),
      ConfigDescriptionSection(),
      HomepageSection(),
      SourceCodeSection(),
      VersionSection(nightly_doc_util),
      DownloadSizeSection(),
      DatasetSizeSection(),
      ManualDatasetSection(),
      AutocacheSection(),
      SplitInfoSection(),
      FeatureInfoSection(),
      SupervisedKeySection(),
      DatasetCitationSection(),
      DatasetVisualizationSection(visu_doc_util),
      DatasetDataframeSection(df_doc_util),
  ]

  doc_str = [
      _display_dataset_heading(builder),
      _display_nightly_str(nightly_doc_util, builder),
      _display_manual_instructions(builder),
      _display_builder_configs(
          builder, nightly_doc_util, config_builders, all_sections
      ),
  ]

  return '\n\n'.join([tfds.core.utils.dedent(s) for s in doc_str if s])
