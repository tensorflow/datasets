# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Util to generate the dataset documentation content.

Used by tensorflow_datasets/scripts/documentation/build_catalog.py
"""

from concurrent import futures
import dataclasses
import functools
from typing import Any, Iterator, List, Optional, Set, Type

from absl import logging
import tensorflow_datasets as tfds
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.scripts.documentation import collection_markdown_builder
from tensorflow_datasets.scripts.documentation import dataset_markdown_builder
from tensorflow_datasets.scripts.documentation import doc_utils
import tqdm

_WORKER_COUNT_DATASETS = 50
_WORKER_COUNT_CONFIGS = 20

# In the section headers we have different spellings of the same word. This
# mapping is used to convert to a single spelling.
_SECTION_WORD_MAPPING = {'modelling': 'modeling'}

# WmtTranslate: The raw wmt can only be instantiated with the config kwargs
_BUILDER_BLACKLIST = [
    'wmt_translate',
]

# pylint: disable=logging-format-interpolation


def _format_section(section: str) -> str:
  section = section.replace('_', ' ').replace('-', ' ').lower()
  for orig_word, new_word in _SECTION_WORD_MAPPING.items():
    section = section.replace(orig_word, new_word)
  return section.capitalize()


@dataclasses.dataclass(eq=False)
class BuilderToDocument:
  """Structure containing metadata."""

  sections: Set[str]
  namespace: Optional[str]
  builder: tfds.core.DatasetBuilder
  config_builders: List[tfds.core.DatasetBuilder]

  def __post_init__(self):
    # Make sure section names are formatted correctly.
    self.sections = {_format_section(section) for section in self.sections}


@dataclasses.dataclass(eq=False)
class BuilderDocumentation:
  """Documentation output of a single builder.

  Attributes:
    name: Documentation page name (e.g. `mnist`, `kaggle:mnist`)
    filestem: Documentation page name without suffix (e.g. `mnist`,
      `kaggle_mnist`)
    content: Documentation content
    sections: Documentation sections (e.g `text`, `image`,...)
    namespace: Dataset namespace
    is_manual: Whether the dataset require manual download
    is_nightly: Whether the dataset was recently added in `tfds-nightly`
  """

  name: str
  filestem: str
  content: str
  sections: Set[str]
  is_manual: bool
  is_nightly: bool

  def __post_init__(self):
    # Make sure section names are formatted correctly.
    self.sections = {_format_section(section) for section in self.sections}


@dataclasses.dataclass(eq=False, frozen=True)
class CollectionDocumentation:
  """Documentation output of a single builder.

  Attributes:
    name: Documentation page name (e.g. `xtreme`)
    content: Documentation content
    is_nightly: Whether the dataset was recently added in `tfds-nightly`
  """

  name: str
  content: str
  is_nightly: bool


def _load_builder(
    name: str,
) -> Optional[BuilderToDocument]:
  """Load the builder to document.

  Args:
    name: Builder to load

  Returns:
    BuilderToDocument or None.
  """
  try:
    dataset_name = tfds.core.naming.DatasetName(name)
  except ValueError as e:
    logging.warning('Could not parse dataset with name %s', name, exc_info=e)
    return None
  if dataset_name.namespace:  # Community dataset
    return _load_builder_from_location(name=name, dataset_name=dataset_name)
  else:  # Code dataset
    return _load_builder_from_code(name)


def _load_builder_from_location(
    name: str,
    dataset_name: tfds.core.naming.DatasetName,
) -> Optional[BuilderToDocument]:
  """Load the builder, config,... to document."""
  logging.info('Loading builder %s from location', dataset_name)
  try:
    builder = tfds.builder(name)
    logging.debug('Loaded builder from location: %s', builder)
  except tfds.core.DatasetNotFoundError as e:
    logging.info(
        'Dataset %s not found, will now try to load from sub-folder',
        dataset_name,
        exc_info=e,
    )
    # If tfds.core.DatasetNotFoundError, it might be the default
    # config isn't found. Should try to load a sub-folder (to check).
    builder = _maybe_load_config(name)
    if not builder:
      logging.error('Dataset %s not found', dataset_name, exc_info=e)
      return None
  except (OSError, tf.errors.PermissionDeniedError) as e:
    logging.error('Permission denied for %s', dataset_name, exc_info=e)
    tqdm.tqdm.write(f'Warning: Skip dataset {name} due to permission error')
    return None
  except Exception as e:  # pylint: disable=broad-except
    logging.error('CorruptedDatasetError: %s', repr(name), exc_info=e)
    return None
  if builder.builder_config:
    config_builders = _load_all_configs(name, builder)
  else:
    config_builders = []
  return BuilderToDocument(
      sections={dataset_name.namespace},
      namespace=dataset_name.namespace,
      builder=builder,
      config_builders=config_builders,
  )


def _maybe_load_config(name: str) -> Optional[tfds.core.DatasetBuilder]:
  del name  # unused
  return None


def _load_all_configs(
    name: str,
    builder: tfds.core.DatasetBuilder,
) -> List[tfds.core.DatasetBuilder]:
  """Load all builder configs."""
  # `data_dir/name/config/version/` -> `data_dir/name/`
  common_dir = builder.data_path.parent.parent
  filtered_dirs = {builder.builder_config.name, '.config'}

  def get_config_builder(path):
    if path.name in filtered_dirs:
      return None  # Default config is already loaded
    try:
      builder_conf = tfds.builder(f'{name}/{path.name}')
    except tfds.core.DatasetNotFoundError:
      return None
    if not builder_conf.builder_config:
      # Unexpected sub-config with wrong metadata.
      # This can happen if the user manually messed up with the directories.
      return None
    return builder_conf

  with futures.ThreadPoolExecutor(max_workers=_WORKER_COUNT_CONFIGS) as tpool:
    config_names = sorted(common_dir.iterdir())
    config_builders = [
        config_builder
        for config_builder in tpool.map(get_config_builder, config_names)
        if config_builder is not None  # Filter invalid configs
    ]

  return [builder] + config_builders


def _load_builder_from_code(
    name: str,
) -> BuilderToDocument:
  """Load the builder, config,... to document."""
  builder_cls = tfds.builder_cls(name)
  sections = _get_sections(builder_cls)

  if builder_cls.BUILDER_CONFIGS:  # Builder with configs

    def get_config_builder(config) -> tfds.core.DatasetBuilder:
      return tfds.builder(builder_cls.name, config=config)

    with futures.ThreadPoolExecutor(max_workers=_WORKER_COUNT_CONFIGS) as tpool:
      config_builders = list(
          tpool.map(get_config_builder, builder_cls.BUILDER_CONFIGS),
      )
    return BuilderToDocument(
        sections=sections,
        namespace=None,
        builder=config_builders[0],
        config_builders=config_builders,
    )
  else:  # Builder without configs
    return BuilderToDocument(
        sections=sections,
        namespace=None,
        builder=builder_cls(),  # pytype: disable=not-instantiable
        config_builders=[],
    )


def _get_sections(builder_cls: Type[tfds.core.DatasetBuilder]) -> Set[str]:
  """Returns the sections associated with the builder."""
  module_parts = builder_cls.__module__.split('.')
  if module_parts[0] != 'tensorflow_datasets':
    raise AssertionError(f'Unexpected builder {builder_cls}: module')
  # Legacy datasets: a single section, inferred from module path.
  _, category, *_ = module_parts  # tfds.<category>.xyz
  if category != 'datasets':
    return {category}
  # Sections are inferred from tags.
  ds_metadata = builder_cls.get_metadata()
  if ds_metadata.tags:
    sections = set()
    for tag in ds_metadata.tags:
      # Ignore languages until we have a better way to display them.
      if tag.startswith('content.language'):
        continue
      section = tag.rsplit('.')[-1]
      sections.add(section)
    return sections
  return {'uncategorized'}


def _document_single_collection(
    name: str,
) -> CollectionDocumentation:
  """Returns the documentation for a single dataset collection."""
  logging.info('Documenting dataset collection %s', name)
  collection = tfds.dataset_collection(name=name)
  out_str = collection_markdown_builder.get_collection_markdown_string(
      collection=collection
  )
  return CollectionDocumentation(
      name=name,
      content=out_str,
      # TODO(tfds): Add support for display of nightly icon when necessary.
      is_nightly=False,
  )


def _document_single_builder(
    name: str,
    **kwargs: Any,
) -> Optional[BuilderDocumentation]:
  """Doc string for a single builder, with or without configs."""
  with tfds.core.utils.try_reraise(f'Error for `{name}`: '):
    return _document_single_builder_inner(name, **kwargs)


def _document_single_builder_inner(
    name: str,
    nightly_doc_util: doc_utils.NightlyDocUtil,
    **kwargs: Any,
) -> Optional[BuilderDocumentation]:
  """Doc string for a single builder, with or without configs."""
  tqdm.tqdm.write(f'Document builder {name}...')
  doc_info = _load_builder(name)
  if doc_info is None:
    logging.warning(
        'No doc info was found for document builder %s. Skipping.', name
    )
    return None

  out_str = dataset_markdown_builder.get_markdown_string(
      namespace=doc_info.namespace,
      builder=doc_info.builder,
      config_builders=doc_info.config_builders,
      nightly_doc_util=nightly_doc_util,
      **kwargs,
  )
  is_nightly = bool(
      nightly_doc_util and nightly_doc_util.is_builder_nightly(name)
  )
  return BuilderDocumentation(
      name=name,
      filestem=name.replace(':', '_'),
      content=out_str,
      sections=doc_info.sections,
      is_manual=bool(doc_info.builder.MANUAL_DOWNLOAD_INSTRUCTIONS),
      is_nightly=is_nightly,
  )


def _all_tfds_datasets() -> List[str]:
  """Returns all "official" TFDS dataset names."""
  datasets = []
  for name in tfds.list_builders(with_community_datasets=True):
    if name in _BUILDER_BLACKLIST:
      continue
    try:
      _ = tfds.core.naming.parse_builder_name_kwargs(name=name)
      datasets.append(name)
    except ValueError as e:
      logging.error('Could not parse dataset with name `%s`!', name, exc_info=e)
  return sorted(datasets)


def iter_collections_documentation(
    collection_names: Optional[List[str]] = None,
) -> Iterator[CollectionDocumentation]:
  logging.info('Retrieving dataset collection names...')
  collection_names = collection_names or sorted(tfds.list_dataset_collections())
  for collection_name in collection_names:
    yield _document_single_collection(name=collection_name)
  print('All collections documentations generated!')


def iter_documentation_builders(
    datasets: Optional[List[str]] = None,
    *,
    doc_util_paths: Optional[doc_utils.DocUtilPaths] = None,
) -> Iterator[BuilderDocumentation]:
  """Creates dataset documentation string for given datasets.

  Args:
    datasets: list of datasets for which to create documentation. If None, then
      all available datasets will be used.
    doc_util_paths: Additional path for visualization, nightly info,...

  Yields:
    builder_documetation: The documentation information for each builder
  """
  print('Retrieving the list of builders...')
  datasets = datasets or _all_tfds_datasets()

  # pytype: disable=attribute-error
  if doc_util_paths.fig_base_path:
    visu_doc_util = doc_utils.VisualizationDocUtil(
        base_path=doc_util_paths.fig_base_path,
        base_url=doc_util_paths.fig_base_url,
    )
  else:
    visu_doc_util = None

  if doc_util_paths.df_base_path:
    df_doc_util = doc_utils.DataframeDocUtil(
        base_path=doc_util_paths.df_base_path,
        base_url=doc_util_paths.df_base_url,
    )
  else:
    df_doc_util = None

  if doc_util_paths.fig_base_path:
    nightly_doc_util = doc_utils.NightlyDocUtil(
        path=doc_util_paths.nightly_path,
    )
  else:
    nightly_doc_util = None
  # pytype: enable=attribute-error

  document_single_builder_fn = functools.partial(
      _document_single_builder,
      visu_doc_util=visu_doc_util,
      df_doc_util=df_doc_util,
      nightly_doc_util=nightly_doc_util,
  )

  # Document all builders
  print(f'Document {len(datasets)} builders...')
  with futures.ThreadPoolExecutor(max_workers=_WORKER_COUNT_DATASETS) as tpool:
    tasks = [
        tpool.submit(document_single_builder_fn, name) for name in datasets
    ]
    for future in tqdm.tqdm(futures.as_completed(tasks), total=len(tasks)):
      builder_doc = future.result()
      if builder_doc is None:  # Builder filtered
        continue
      else:
        tqdm.tqdm.write(f'Documentation generated for {builder_doc.name}...')
        yield builder_doc
  print('All builder documentations generated!')
