"""Dataset catalog documentation template.

Displayed in https://www.tensorflow.org/datasets/catalog/.

"""
import abc
import textwrap
from typing import Any, List

import tensorflow_datasets as tfds


class Section(abc.ABC):

  @abc.abstractmethod
  def get_key(self, builder: tfds.core.DatasetBuilder) -> Any:
    pass

  @abc.abstractmethod
  def display(self, builder: tfds.core.DatasetBuilder) -> str:
    pass

# --------------------------- Builder sections ---------------------------

# pylint:disable = missing-class-docstring

class HomepageSection(Section):

  def get_key(self, builder):
    return builder.info.homepage

  def display(self, builder):
    return f"""\
    *   **Homepage**: [{builder.info.homepage}]({builder.info.homepage})
    """


class DatasetDescriptionSection(Section):

  def get_key(self, builder):
    return builder.info.description

  def display(self, builder):
    return f"""\
      *   **Description**:
      
      {tfds.core.utils.indent(builder.info.description, "      ")}
      """


class ConfigDescriptionSection(Section):

  def get_key(self, builder):
    return builder.builder_config.description

  def display(self, builder):
    if builder.builder_config:
      return f"""\
        *   **Config description**: {tfds.core.utils.indent(builder.builder_config.description, "        ")}
        """
    return ""


class SourceCodeSection(Section):

  def get_key(self, _):
    return True  # Always common to all configs

  def display(self, builder):
    class_path = tfds.core.utils.get_class_path(builder).split(".")
    del class_path[-2]
    class_path = ".".join(class_path)
    return f"""\
      *   **Source code**: [`{class_path}`]({tfds.core.utils.get_class_url(builder)})
      """


class VersionSection(Section):

  def __init__(self, nightly_doc_util):
    self._nightly_doc_util = nightly_doc_util

  def _list_versions(self, builder):
    for v in builder.versions:  # List all available versions (in default order)
      if v == builder.version:  # Highlight the default version
        version_name = "**`{}`** (default)".format(str(v))
      else:
        version_name = "`{}`".format(str(v))
      if self._nightly_doc_util.is_version_nightly(builder, str(v)):
        nightly_str = " " + self._nightly_doc_util.icon
      else:
        nightly_str = ""
      yield "{}{}: {}".format(
          version_name, nightly_str, v.description or "No release notes.")

  def get_key(self, builder):
    return tuple((str(v), v.description) for v in builder.versions)

  def display(self, builder):
    version_list = ("\n").join([f"    *   {version_str}"
      for version_str in self._list_versions(builder)])

    return f"""\
      *   **Versions**:

      {version_list}
      """


class DownloadSizeSection(Section):

  def get_key(self, builder):
    return builder.info.download_size

  def display(self, builder):
    return f"""\
      *   **Download size**: `{tfds.units.size_str(builder.info.download_size)}`
      """


class DatasetSizeSection(Section):

  def get_key(self, builder):
    return builder.info.dataset_size

  def display(self, builder):
    return f"""\
      *   **Dataset size**: `{tfds.units.size_str(builder.info.dataset_size)}`
      """


class ManualDatasetSection(Section):

  def get_key(self, builder):
    return builder.MANUAL_DOWNLOAD_INSTRUCTIONS

  def display(self, builder):
    if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
      return f"""\
        *   **Manual download instructions**: This dataset requires you to
            download the source data manually into `download_config.manual_dir`
            (defaults to `~/tensorflow_datasets/download/manual/`):<br/>
            {tfds.core.utils.indent(builder.MANUAL_DOWNLOAD_INSTRUCTIONS, "            ")}
        """
    return ""


class AutocacheSection(Section):

  @staticmethod
  def build_autocached_info(builder):
    """Returns the auto-cache information string."""
    always_cached = set()
    never_cached = set()
    unshuffle_cached = set()
    for split_name in builder.info.splits.keys():
      split_name = str(split_name)
      cache_shuffled = builder._should_cache_ds(  # pylint: disable=protected-access
          split_name, shuffle_files=True, read_config=tfds.ReadConfig())
      cache_unshuffled = builder._should_cache_ds(  # pylint: disable=protected-access
          split_name, shuffle_files=False, read_config=tfds.ReadConfig())

      if cache_shuffled == cache_unshuffled == True:
        always_cached.add(split_name)
      elif cache_shuffled == cache_unshuffled == False:
        never_cached.add(split_name)
      else:  # Dataset is only cached when shuffled_files is False
        assert not cache_shuffled and cache_unshuffled
        unshuffle_cached.add(split_name)

    if not len(builder.info.splits) or not builder.info.dataset_size:
      autocached_info = "Unknown"
    elif len(always_cached) == len(builder.info.splits.keys()):
      autocached_info = "Yes"  # All splits are auto-cached.
    elif len(never_cached) == len(builder.info.splits.keys()):
      autocached_info = "No"  # Splits never auto-cached.
    else:  # Some splits cached, some not.
      autocached_info_parts = []
      if always_cached:
        split_names_str = ", ".join(always_cached)
        autocached_info_parts.append("Yes ({})".format(split_names_str))
      if never_cached:
        split_names_str = ", ".join(never_cached)
        autocached_info_parts.append("No ({})".format(split_names_str))
      if unshuffle_cached:
        split_names_str = ", ".join(unshuffle_cached)
        autocached_info_parts.append(
            "Only when `shuffle_files=False` ({})".format(split_names_str))
      autocached_info = ", ".join(autocached_info_parts)
    return autocached_info

  def get_key(self, builder):
    return self.build_autocached_info(builder)

  def display(self, builder):
    return f"""\
      *   **Auto-cached**
          ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
          {self.build_autocached_info(builder)}
      """


class SplitInfoSection(Section):

  @staticmethod
  def get_num_examples(split_info):
    if split_info.num_examples:
      return "{:,}".format(split_info.num_examples)
    return "Not computed"

  def get_key(self, builder):
    return tuple(
        (str(s.name), int(s.num_examples)) for s in builder.info.splits.values()
    )

  def display(self, builder):
    splits_str = ("\n").join([
        f"'{split_name}' | {self.get_num_examples(split_info)}"
        for split_name, split_info in sorted(builder.info.splits.items())
    ])

    return f"""\
      *   **Splits**:

      Split  | Examples
      :----- | -------:
      {tfds.core.utils.indent(splits_str, "      ")}
      """


class FeatureInfoSection(Section):

  def get_key(self, builder):
    return repr(builder.info.features)

  def display(self, builder):
    return f"""\
      *   **Features**:

      ```python
      {tfds.core.utils.indent(str(builder.info.features), "      ")}
      ```
      """


class SupervisedKeySection(Section):

  def get_key(self, builder):
    return builder.info.supervised_keys

  def display(self, builder):
    return f"""\
      *   **Supervised keys** (See
          [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
          `{str(builder.info.supervised_keys)}`
      """


class DatasetCitationSection(Section):

  def get_key(self, builder):
    return builder.info.citation

  def display(self, builder):
    if builder.info.citation:
      return f"""\
        *   **Citation**:
        
        ```
        {tfds.core.utils.indent(builder.info.citation, "        ")}
        ```
        """
    return ""


class DatasetVisualizationSection(Section):

  def __init__(self, visualization_util):
    self._visualization_util = visualization_util

  def get_key(self, builder):
    if self._visualization_util.has_visualization(builder):
      return builder.info.full_name
    return None  # Fuse the sections together if no configs are available

  def display(self, builder):
    visualzation_text = "    Not supported."
    if self._visualization_util.has_visualization(builder):
      visualzation_text = self._visualization_util.get_html_tag(builder)

    return f"""\
      *   **Visualization
          ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:

      {visualzation_text}
      """

# pylint:enable = missing-class-docstring

# --------------------------- Single builder ---------------------------


def _display_builder(builder, sections):
  return ("\n").join([textwrap.dedent(section.display(builder))
                      for section in sections if section.display(builder)])


# --------------------------- Builder configs ---------------------------

def _display_all_builders(nightly_doc_util, builders, all_sections):
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
    header_suffix = " (default config)" if i == 0 else ""
    nightly_str = (" " + nightly_doc_util.icon) \
        if nightly_doc_util.is_config_nightly(builder) else ""
    unique_builder_str.append(
        f"## {builder.name}/{builder.builder_config.name}"
        f"{header_suffix}{nightly_str}\n")
    unique_builder_str.append(_display_builder(builder, unique_sections))
  unique_builder_str = ("\n").join(unique_builder_str)

  return common_builder_str + "\n" + unique_builder_str


# --------------------------- Main page ---------------------------

def _display_builder_configs(
    builder,
    nightly_doc_util,
    config_builders,
    all_sections
):
  # First case: Single builder
  if not builder.builder_config:
    return _display_builder(builder, all_sections)
  # Second case: Builder configs
  return _display_all_builders(nightly_doc_util, config_builders, all_sections)


def _display_nightly_str(nightly_doc_util, builder):
  if nightly_doc_util.is_builder_nightly(builder):
    return f"""\
      Note: This dataset was added recently and is only available in our
      `tfds-nightly` package  {nightly_doc_util.icon}.
      """
  if nightly_doc_util.has_nightly(builder):
    return f"""\
      Note: This dataset has been updated since the last stable release.
      The new versions and config marked with {nightly_doc_util.icon}
      are only available in the `tfds-nightly` package.
      """
  return ""


def _display_manual_instructions(builder):
  if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
    return "Warning: Manual download required. See instructions below.\n"
  return ""


def _display_dataset_heading(builder):
  return textwrap.dedent(
      f"""
      # `{builder.name}`
      """
  )


def get_markdown_string(
    builder: tfds.core.DatasetBuilder,
    config_builders: List[tfds.core.DatasetBuilder],
    visu_doc_util,
    nightly_doc_util,
) -> str:

  all_sections = [
      DatasetDescriptionSection(),
      HomepageSection(),
      ConfigDescriptionSection(),
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
  ]

  doc_str = [
      _display_dataset_heading(builder),
      _display_nightly_str(nightly_doc_util, builder),
      _display_manual_instructions(builder),
      _display_builder_configs(builder, nightly_doc_util,
                               config_builders, all_sections)
  ]

  return ("\n").join([s for s in doc_str if s])
