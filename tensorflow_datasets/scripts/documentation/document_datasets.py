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

"""Util to generate the dataset documentation content.

Used by tensorflow_datasets/scripts/documentation/build_catalog.py

"""

import collections
from concurrent import futures
import dataclasses
import functools
from typing import Any, Dict, Iterator, List, Optional, Type

from absl import logging
import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import dataset_markdown_builder
from tensorflow_datasets.scripts.documentation import doc_utils
import tqdm

_WORKER_COUNT_DATASETS = 50
_WORKER_COUNT_CONFIGS = 20

# WmtTranslate: The raw wmt can only be instantiated with the config kwargs
_BUILDER_BLACKLIST = [
    'wmt_translate',
]

# pylint: disable=logging-format-interpolation


@dataclasses.dataclass(eq=False, frozen=True)
class BuilderToDocument:
  """Structure containing metadata."""
  section: str
  namespace: Optional[str]
  builder: tfds.core.DatasetBuilder
  config_builders: List[tfds.core.DatasetBuilder]


@dataclasses.dataclass(eq=False, frozen=True)
class BuilderDocumentation:
  """Documentation output of a single builder.

  Attributes:
    name: Documentation page name (e.g. `mnist`, `kaggle:mnist`)
    filestem: Documentation page name without suffix (e.g. `mnist`,
      `kaggle_mnist`)
    content: Documentation content
    section: Documentation section (e.g `text`, `image`,...)
    namespace: Dataset namespace
    is_manual: Whether the dataset require manual download
    is_nightly: Whether the dataset was recently added in `tfds-nightly`
  """
  name: str
  filestem: str
  content: str
  section: str
  is_manual: bool
  is_nightly: bool


def _load_builder(name: str,) -> Optional[BuilderToDocument]:
  """Load the builder to document.

  Args:
    name: Builder to load

  Returns:
    section: The section in which the builder is documented
    builder: Main builder instance
    config_builders: Additional builders (one of each configs)
  """
  if tfds.core.utils.DatasetName(name).namespace:  # Community dataset
    return _load_builder_from_location(name)
  else:  # Code dataset
    return _load_builder_from_code(name)


def _load_builder_from_location(name: str,) -> Optional[BuilderToDocument]:
  """Load the builder, config,... to document."""
  dataset_name = tfds.core.utils.DatasetName(name)
  logging.info(f'Loading builder {dataset_name} from location')
  try:
    builder = tfds.builder(name)
    logging.debug(f'Loaded builder from location: {builder}')
  except tfds.core.DatasetNotFoundError as e:
    logging.info(
        f'Dataset {dataset_name} not found, will now try to load from sub-folder',
        exc_info=e)
    # If tfds.core.DatasetNotFoundError, it might be the default
    # config isn't found. Should try to load a sub-folder (to check).
    builder = _maybe_load_config(name)
    if not builder:
      logging.error(f'Dataset {dataset_name} not found', exc_info=e)
      return None
  except tf.errors.PermissionDeniedError as e:
    logging.error(f'Permission denied for {dataset_name}', exc_info=e)
    tqdm.tqdm.write(f'Warning: Skip dataset {name} due to permission error')
    return None
  except Exception as e:  # pylint: disable=broad-except
    logging.error(f'CorruptedDatasetError: {name!r}', exc_info=e)
    return None
  if builder.builder_config:
    config_builders = _load_all_configs(name, builder)
  else:
    config_builders = []
  return BuilderToDocument(
      section=dataset_name.namespace,
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


def _load_builder_from_code(name: str,) -> BuilderToDocument:
  """Load the builder, config,... to document."""
  builder_cls = tfds.builder_cls(name)
  section = _get_section(builder_cls)

  if builder_cls.BUILDER_CONFIGS:  # Builder with configs

    def get_config_builder(config) -> tfds.core.DatasetBuilder:
      return tfds.builder(builder_cls.name, config=config)

    with futures.ThreadPoolExecutor(max_workers=_WORKER_COUNT_CONFIGS) as tpool:
      config_builders = list(
          tpool.map(get_config_builder, builder_cls.BUILDER_CONFIGS),)
    return BuilderToDocument(
        section=section,
        namespace=None,
        builder=config_builders[0],
        config_builders=config_builders,
    )
  else:  # Builder without configs
    return BuilderToDocument(
        section=section,
        namespace=None,
        builder=builder_cls(),  # pytype: disable=not-instantiable
        config_builders=[],
    )


def _get_section(builder_cls: Type[tfds.core.DatasetBuilder]) -> str:
  """Returns the section associated with the builder."""
  module_parts = builder_cls.__module__.split('.')
  if module_parts[0] != 'tensorflow_datasets':
    raise AssertionError(f'Unexpected builder {builder_cls}: module')
  _, category, *_ = module_parts  # tfds.<category>.xyz
  return category


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
    logging.warn(
        f'No doc info was found for document builder {name}. Skipping.')
    return None

  out_str = dataset_markdown_builder.get_markdown_string(
      namespace=doc_info.namespace,
      builder=doc_info.builder,
      config_builders=doc_info.config_builders,
      nightly_doc_util=nightly_doc_util,
      **kwargs)
  is_nightly = bool(
      nightly_doc_util and nightly_doc_util.is_builder_nightly(name))
  return BuilderDocumentation(
      name=name,
      filestem=name.replace(':', '_'),
      content=out_str,
      section=doc_info.section,
      is_manual=bool(doc_info.builder.MANUAL_DOWNLOAD_INSTRUCTIONS),
      is_nightly=is_nightly,
  )


def _all_tfds_datasets() -> List[str]:
  """Returns all "official" TFDS dataset names."""
  return sorted([
      name for name in tfds.list_builders(with_community_datasets=True)  # pylint: disable=g-complex-comprehension
      if name not in _BUILDER_BLACKLIST
  ])


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
        path=doc_util_paths.nightly_path,)
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


def make_category_to_builders_dict(
) -> Dict[str, List[tfds.core.DatasetBuilder]]:
  """Loads all builders with their associated category."""
  datasets = _all_tfds_datasets()
  print(f'Creating the vanilla builders for {len(datasets)} datasets...')
  with futures.ThreadPoolExecutor(max_workers=_WORKER_COUNT_DATASETS) as tpool:
    builders = tpool.map(tfds.builder, datasets)

  category_to_builders = collections.defaultdict(list)
  for builder in builders:
    section = _get_section(type(builder))
    category_to_builders[section].append(builder)
  return category_to_builders
