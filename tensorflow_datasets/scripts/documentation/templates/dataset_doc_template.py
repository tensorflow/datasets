"""Dataset catalog documentation template.

Displayed in https://www.tensorflow.org/datasets/catalog/.

"""
import textwrap
import collections
import tensorflow_datasets as tfds

_NIGHTLY_DOC_UTIL = None
_VISU_DOC_UTIL = None


# --------------------------- Builder sections ---------------------------


def display_description(builder):
  return f"""\
*   **Description**:

{builder.info.description}
"""


def display_config_description(builder):
  if builder.builder_config:
    return f"""\
*   **Config description**: {builder.builder_config.description}
"""
  return ""


def display_homepage(builder):
  return f"""\
*   **Homepage**: 
    [{builder.info.homepage}]({builder.info.homepage})
"""


def display_source(builder):
  class_path = tfds.core.utils.get_class_path(builder).split('.')
  del class_path[-2]
  class_path = '.'.join(class_path)
  return f"""\
*   **Source code**:
    [`{class_path}`]({tfds.core.utils.get_class_url(builder)})
"""


def display_versions(builder):
  def list_versions(builder):
    for v in builder.versions:  # List all available versions (in default order)
      if v == builder.version:  # Highlight the default version
        version_name = '**`{}`** (default)'.format(str(v))
      else:
        version_name = '`{}`'.format(str(v))
      if _NIGHTLY_DOC_UTIL.is_version_nightly(builder, str(v)):
        nightly_str = ' ' + _NIGHTLY_DOC_UTIL.icon
      else:
        nightly_str = ''
      yield '{}{}: {}'.format(
          version_name, nightly_str, v.description or 'No release notes.')

  version_list = ('\n').join(
      [f'    *   {version_str}' for version_str in list_versions(builder)])

  return f"""\
*   **Versions**:
{version_list}
"""


def display_download_size(builder):
  return f"""\
*   **Download size**: `{tfds.units.size_str(builder.info.download_size)}`
"""


def display_dataset_size(builder):
  return f"""\
*   **Dataset size**: `{tfds.units.size_str(builder.info.dataset_size)}`
"""


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
  return f"""\
*   **Auto-cached**
    ([documentation](https://www.tensorflow.org/datasets/performances#auto-caching)):
    {build_autocached_info(builder)}
"""


def display_manual(builder):
  if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
    return f"""\
*   **Manual download instructions**: This dataset requires you to download the
    source data manually into `download_config.manual_dir`
    (defaults to `~/tensorflow_datasets/download/manual/`):<br/>
{textwrap.indent(tfds.core.utils.dedent(builder.MANUAL_DOWNLOAD_INSTRUCTIONS), '    ')}
"""
  return ""


def display_splits(builder):
  def get_num_examples(split_info):
    if split_info.num_examples:
      return '{:,}'.format(split_info.num_examples)
    return 'Not computed'

  splits_str = ('\n').join([
      f'{split_name} | {get_num_examples(split_info)}'
      for split_name, split_info in sorted(builder.info.splits.items())
  ])

  return f"""\
*   **Splits**:

Split  | Examples
:----- | -------:
{splits_str}
"""


def display_features(builder):
  return f"""\
*   **Features**:

```python
{builder.info.features}
```
"""


def display_supervised(builder):
  return f"""\
*   **Supervised keys** (See
    [`as_supervised` doc](https://www.tensorflow.org/datasets/api_docs/python/tfds/load#args)):
    `{str(builder.info.supervised_keys)}`
"""


def display_citation(builder):
  if builder.info.citation:
    return f"""\
*   **Citation**:

```
{builder.info.citation}
```
"""
  return ""


def display_figure(builder):
  visu_str = "Not supported."
  if _VISU_DOC_UTIL.has_visualization(builder):
    visu_str = _VISU_DOC_UTIL.get_html_tag(builder)

  return f"""\
*   **Visualization
    ([tfds.show_examples](https://www.tensorflow.org/datasets/api_docs/python/tfds/visualization/show_examples))**:

{visu_str}
"""


# Getter function returns a hashable signature of the section value
# which allow to detect sections shared accross all builders.


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


def get_figure(builder):
  if _VISU_DOC_UTIL.has_visualization(builder):
    return builder.info.full_name
  return None  # Fuse the sections together if no configs are available


# --------------------------- Single builder ---------------------------

def display_builder(builder, sections):
  return ('\n').join([section.make(builder)
                      for section in sections if section.make(builder)])


# --------------------------- Builder configs ---------------------------

def display_all_builders(builders, all_sections):
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
    nightly_str = (' ' + _NIGHTLY_DOC_UTIL.icon) \
        if _NIGHTLY_DOC_UTIL.is_config_nightly(builder) else ''
    unique_builder_str.append(
        f'## {builder.name}/{builder.builder_config.name}'
        f'{header_suffix}{nightly_str}\n')
    unique_builder_str.append(display_builder(builder, unique_sections))
  unique_builder_str = ('\n').join(unique_builder_str)

  return common_builder_str + '\n' + unique_builder_str


# --------------------------- Main page ---------------------------

def display_builder_configs(builder, config_builders, all_sections):
  # First case: Single builder
  if not builder.builder_config:
    return display_builder(builder, all_sections)
  # Second case: Builder configs
  return display_all_builders(config_builders, all_sections)


def display_nightly_str(builder):
  if _NIGHTLY_DOC_UTIL.is_builder_nightly(builder):
    return f"""\
Note: This dataset was added recently and is only available in our
`tfds-nightly` package  {_NIGHTLY_DOC_UTIL.icon}.
"""
  if _NIGHTLY_DOC_UTIL.has_nightly(builder):
    return f"""\
Note: This dataset has been updated since the last stable release. The new
versions and config marked with {_NIGHTLY_DOC_UTIL.icon} are only available
in the `tfds-nightly` package.
"""
  return ""


def display_manual_instructions(builder):
  if builder.MANUAL_DOWNLOAD_INSTRUCTIONS:
    return "Warning: Manual download required. See instructions below."
  return ""


def display_dataset_heading(builder):
  return f"""\
# `{builder.name}`
"""


def get_markdown_string(
    builder,
    config_builders,
    visu_doc_util,
    nightly_doc_util,
):
  global _NIGHTLY_DOC_UTIL, _VISU_DOC_UTIL

  _NIGHTLY_DOC_UTIL = nightly_doc_util
  _VISU_DOC_UTIL = visu_doc_util

  Section = collections.namedtuple('Section', 'get_signature, make')

  all_sections = [
      Section(get_description, display_description),
      Section(get_config_description, display_config_description),
      Section(get_homepage, display_homepage),
      Section(get_source, display_source),
      Section(get_versions, display_versions),
      Section(get_download_size, display_download_size),
      Section(get_dataset_size, display_dataset_size),
      Section(get_manual, display_manual),
      Section(get_autocache, display_autocache),
      Section(get_splits, display_splits),
      Section(get_features, display_features),
      Section(get_supervised, display_supervised),
      Section(get_citation, display_citation),
      Section(get_figure, display_figure),
  ]

  doc_str = [
      display_dataset_heading(builder),
      display_nightly_str(builder),
      display_manual_instructions(builder),
      display_builder_configs(builder, config_builders, all_sections)
  ]

  return ('\n').join([s for s in doc_str if s])
