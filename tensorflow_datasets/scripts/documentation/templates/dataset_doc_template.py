"""Dataset catalog documentation template.

Displayed in https://www.tensorflow.org/datasets/catalog/.

"""
import collections
import dataclasses
import functools
import textwrap
from typing import Callable, List

import tensorflow_datasets as tfds


@dataclasses.dataclass
class Section(object):
  get_signature: Callable[[tfds.core.DatasetBuilder], str]
  make: Callable[[tfds.core.DatasetBuilder], str]

# --------------------------- Builder sections ---------------------------


def display_description(builder):
  return textwrap.dedent(
      f"""\
      *   **Description**:

      """
  ) + tfds.core.utils.dedent(builder.info.description) + '\n'


def display_config_description(builder):
  if builder.builder_config:
    return textwrap.dedent(
        f"""\
        *   **Config description**: {builder.builder_config.description}
        """
    )
  return ""


def display_homepage(builder):
  return textwrap.dedent(
      f"""\
      *   **Homepage**: [{builder.info.homepage}]({builder.info.homepage})
      """
  )


def display_source(builder):
  class_path = tfds.core.utils.get_class_path(builder).split('.')
  del class_path[-2]
  class_path = '.'.join(class_path)
  return textwrap.dedent(
      f"""\
      *   **Source code**: [`{class_path}`]({tfds.core.utils.get_class_url(builder)})
      """
  )


def display_versions(nightly_doc_util, builder):
  def list_versions():
    for v in builder.versions:  # List all available versions (in default order)
      if v == builder.version:  # Highlight the default version
        version_name = '**`{}`** (default)'.format(str(v))
      else:
        version_name = '`{}`'.format(str(v))
      if nightly_doc_util.is_version_nightly(builder, str(v)):
        nightly_str = ' ' + nightly_doc_util.icon
      else:
        nightly_str = ''
      yield '{}{}: {}'.format(
          version_name, nightly_str, v.description or 'No release notes.')

  version_list = ('\n').join(
      [f'    *   {version_str}' for version_str in list_versions()])

  return textwrap.dedent(
      f"""\
      *   **Versions**:

      {version_list}
      """
  )


def display_download_size(builder):
  return textwrap.dedent(
      f"""\
      *   **Download size**: `{tfds.units.size_str(builder.info.download_size)}`
      """
  )


def display_dataset_size(builder):
  return textwrap.dedent(
      f"""\
      *   **Dataset size**: `{tfds.units.size_str(builder.info.dataset_size)}`
      """
  )


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


def display_autocache(builder):
  return textwrap.dedent(
      f"""\
      *   **Auto-cached**
          ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
          {build_autocached_info(builder)}
      """
  )


def display_manual(builder):
  if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
    return textwrap.dedent(
        f"""\
        *   **Manual download instructions**: This dataset requires you to download the
            source data manually into `download_config.manual_dir`
            (defaults to `~/tensorflow_datasets/download/manual/`):<br/>
        """
    ) + textwrap.indent(tfds.core.utils.dedent(
        builder.MANUAL_DOWNLOAD_INSTRUCTIONS), '    ') + '\n'
  return ""


def display_splits(builder):
  def get_num_examples(split_info):
    if split_info.num_examples:
      return '{:,}'.format(split_info.num_examples)
    return 'Not computed'

  splits_str = ('\n').join([
      f"'{split_name}' | {get_num_examples(split_info)}"
      for split_name, split_info in sorted(builder.info.splits.items())
  ])

  return textwrap.dedent(
      f"""\
      *   **Splits**:

      Split  | Examples
      :----- | -------:
      """
  ) + f"{splits_str}\n"


def display_features(builder):
  return textwrap.dedent(
      f"""\
      *   **Features**:

      ```python
      """
  ) + str(builder.info.features) + "\n```\n"


def display_supervised(builder):
  return textwrap.dedent(
      f"""\
      *   **Supervised keys** (See
          [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
          `{str(builder.info.supervised_keys)}`
      """
  )


def display_citation(builder):
  if builder.info.citation:
    return textwrap.dedent(
        f"""\
        *   **Citation**:

        ```
        """
    ) + tfds.core.utils.dedent(builder.info.citation) + "\n```\n"
  return ""


def display_figure(visu_doc_util, builder):
  visu_str = "    Not supported."
  if visu_doc_util.has_visualization(builder):
    visu_str = visu_doc_util.get_html_tag(builder)

  return textwrap.dedent(
      f"""\
      *   **Visualization
          ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:

      {visu_str}
      """
  )


def get_description(builder):
  return builder.info.description


def get_config_description(builder):
  return builder.builder_config.description


def get_homepage(builder):
  return builder.info.homepage


def get_source(_):
  return True  # Always common to all configs


def get_versions(builder):
  return tuple((str(v), v.description) for v in builder.versions)


def get_download_size(builder):
  return builder.info.download_size


def get_dataset_size(builder):
  return builder.info.dataset_size


def get_manual(builder):
  return builder.MANUAL_DOWNLOAD_INSTRUCTIONS


def get_autocache(builder):
  return build_autocached_info(builder)


def get_splits(builder):
  return tuple(
      (str(s.name), int(s.num_examples)) for s in builder.info.splits.values()
  )


def get_features(builder):
  return repr(builder.info.features)


def get_supervised(builder):
  return builder.info.supervised_keys


def get_citation(builder):
  return builder.info.citation


def get_figure(visu_doc_util, builder):
  if visu_doc_util.has_visualization(builder):
    return builder.info.full_name
  return None  # Fuse the sections together if no configs are available


# --------------------------- Single builder ---------------------------

def display_builder(builder, sections):
  return ('\n').join([section.make(builder)
                      for section in sections if section.make(builder)])


# --------------------------- Builder configs ---------------------------

def display_all_builders(nightly_doc_util, builders, all_sections):
  # For each fields, extract if the field is shared or unique accross builder.
  common_sections = []
  unique_sections = []
  for section in all_sections:
    if len(set(section.get_signature(b) for b in builders)) == 1:
      common_sections.append(section)
    else:
      unique_sections.append(section)

  common_builder_str = display_builder(next(iter(builders)), common_sections)

  unique_builder_str = []
  for i, builder in enumerate(builders):
    header_suffix = ' (default config)' if i == 0 else ''
    nightly_str = (' ' + nightly_doc_util.icon) \
        if nightly_doc_util.is_config_nightly(builder) else ''
    unique_builder_str.append(
        f'## {builder.name}/{builder.builder_config.name}'
        f'{header_suffix}{nightly_str}\n')
    unique_builder_str.append(display_builder(builder, unique_sections))
  unique_builder_str = ('\n').join(unique_builder_str)

  return common_builder_str + '\n' + unique_builder_str


# --------------------------- Main page ---------------------------

def display_builder_configs(builder, nightly_doc_util, config_builders, all_sections):
  # First case: Single builder
  if not builder.builder_config:
    return display_builder(builder, all_sections)
  # Second case: Builder configs
  return display_all_builders(nightly_doc_util, config_builders, all_sections)


def display_nightly_str(nightly_doc_util, builder):
  if nightly_doc_util.is_builder_nightly(builder):
    return textwrap.dedent(
        f"""\
        Note: This dataset was added recently and is only available in our
        `tfds-nightly` package  {nightly_doc_util.icon}.
        """
    )
  if nightly_doc_util.has_nightly(builder):
    return textwrap.dedent(
        f"""\
        Note: This dataset has been updated since the last stable release. The new
        versions and config marked with {nightly_doc_util.icon} are only available
        in the `tfds-nightly` package.
        """
    )
  return ""


def display_manual_instructions(builder):
  if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
    return "Warning: Manual download required. See instructions below.\n"
  return ""


def display_dataset_heading(builder):
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
      Section(get_description, display_description),
      Section(get_config_description, display_config_description),
      Section(get_homepage, display_homepage),
      Section(get_source, display_source),
      Section(get_versions, functools.partial(
          display_versions, nightly_doc_util)),
      Section(get_download_size, display_download_size),
      Section(get_dataset_size, display_dataset_size),
      Section(get_manual, display_manual),
      Section(get_autocache, display_autocache),
      Section(get_splits, display_splits),
      Section(get_features, display_features),
      Section(get_supervised, display_supervised),
      Section(get_citation, display_citation),
      Section(functools.partial(get_figure, visu_doc_util),
              functools.partial(display_figure, visu_doc_util)),
  ]

  doc_str = [
      display_dataset_heading(builder),
      display_nightly_str(nightly_doc_util, builder),
      display_manual_instructions(builder),
      display_builder_configs(builder, nightly_doc_util,
                              config_builders, all_sections)
  ]

  return ('\n').join([s for s in doc_str if s])
