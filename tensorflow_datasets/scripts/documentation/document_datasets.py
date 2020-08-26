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

"""Util to generate the dataset documentation content.

Used by tensorflow_datasets/scripts/documentation/build_catalog.py

"""

import collections
from concurrent import futures
import os
from typing import Dict, List, Tuple, Union, Set

import mako.lookup
import tensorflow.compat.v2 as tf
import tensorflow_datasets as tfds
from tensorflow_datasets.scripts.documentation import dataset_markdown_builder

WORKER_COUNT_DATASETS = 200
WORKER_COUNT_CONFIGS = 50

BASE_URL = 'https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets'

# WmtTranslate: The raw wmt can only be instantiated with the config kwargs
# TODO(tfds): Document image_label_folder datasets in a separate section
BUILDER_BLACKLIST = ['wmt_translate']


# Dict of `full_names_dict['dataset']['config']['version']`
FullNamesDict = Dict[str, Dict[str, Set[str]]]
# Same as `FullNamesDict`, but contains `True` for nightly datasets:
# * New dataset: nightly_dict['dataset'] is True
# * New config: nightly_dict['dataset']['config'] is True
# * New version: nightly_dict['dataset']['config']['version'] is True
NightlyDict = Dict[str, Union[bool, Dict[str, Union[bool, Dict[str, bool]]]]]


class VisualizationDocUtil(object):
  """Small util which generate the path/urls for the visualizations."""
  # Url used to display images
  BASE_PATH = tfds.core.gcs_path('visualization/fig/')
  BASE_URL = 'https://storage.googleapis.com/tfds-data/visualization/fig/'

  def _get_name(self, builder):
    return builder.info.full_name.replace('/', '-') + '.png'

  def get_url(self, builder):
    return self.BASE_URL + self._get_name(builder)

  def get_html_tag(self, builder: tfds.core.DatasetBuilder) -> str:
    """Returns the <img> html tag."""
    url = self.get_url(builder)
    return f'<img src="{url}" alt="Visualization" width="500px">'

  def has_visualization(self, builder):
    filepath = os.path.join(self.BASE_PATH, self._get_name(builder))
    return tf.io.gfile.exists(filepath)


def _split_full_name(full_name: str) -> Tuple[str, str, str]:
  """Extracts the `(ds name, config, version)` from the full_name."""
  if not tfds.core.load.is_full_name(full_name):
    raise ValueError(
        f'Parsing builder name string {full_name} failed.'
        'The builder name string must be of the following format:'
        '`dataset_name[/config_name]/version`')
  ds_name, *optional_config, version = full_name.split('/')
  assert len(optional_config) <= 1
  config = next(iter(optional_config)) if optional_config else ''
  return ds_name, config, version


def _full_names_to_dict(full_names: List[str]) -> FullNamesDict:
  """Creates the dict `d['dataset']['config']['version']`."""
  full_names_dict = collections.defaultdict(
      lambda: collections.defaultdict(set))
  for full_name in full_names:
    ds_name, config, version = _split_full_name(full_name)
    full_names_dict[ds_name][config].add(version)
  return full_names_dict


def _build_nightly_dict(
    registered_ds: FullNamesDict,
    stable_version_ds: FullNamesDict,
) -> NightlyDict:
  """Computes the nightly dict from the registered and stable dict."""
  nightly_ds = collections.defaultdict(
      lambda: collections.defaultdict(  # pylint: disable=g-long-lambda
          lambda: collections.defaultdict(bool)))
  for dataset in registered_ds:
    if dataset in stable_version_ds:
      for config in registered_ds[dataset]:
        if config in stable_version_ds[dataset]:
          for version in registered_ds[dataset][config]:
            if version in stable_version_ds[dataset][config]:
              # (dataset, config, version) already exists
              # We add it to the nightly dict to make sure the
              # key exists
              nightly_ds[dataset][config][version] = False
            else:
              # New version only present in tfds-nightly
              nightly_ds[dataset][config][version] = True
        else:
          # New config only present in tfds-nightly
          nightly_ds[dataset][config] = True
    else:
      # New dataset only present in tfds-nightly
      nightly_ds[dataset] = True
  return nightly_ds


@tfds.core.utils.memoize()
def _load_nightly_dict() -> NightlyDict:
  """Loads (and caches) the nightly dict."""
  version_path = tfds.core.utils.get_tfds_path('stable_versions.txt')
  with tf.io.gfile.GFile(version_path, 'r') as f:
    stable_versions = f.read().splitlines()

  # Build the `full_names_dict['dataset']['config']['version']` for both
  # nightly and stable version
  registered_ds = _full_names_to_dict(
      tfds.core.load.list_full_names())
  stable_version_ds = _full_names_to_dict(stable_versions)

  # Nightly versions are `registered - stable`
  return _build_nightly_dict(registered_ds, stable_version_ds)


class NightlyDocUtil(object):
  """Small util to format the doc."""

  def __init__(self):
    self._nightly_dict: NightlyDict = _load_nightly_dict()

  def is_builder_nightly(
      self,
      builder: Union[tfds.core.DatasetBuilder, str],
  ) -> bool:
    """Returns `True` if the builder is new."""
    if isinstance(builder, tfds.core.DatasetBuilder):
      builder_name = builder.name
    else:
      builder_name = builder
    return self._nightly_dict[builder_name] is True  # pylint: disable=g-bool-id-comparison

  def is_config_nightly(self, builder: tfds.core.DatasetBuilder) -> bool:
    """Returns `True` if the config is new."""
    ds_name, config, _ = _split_full_name(builder.info.full_name)
    if self.is_builder_nightly(builder):
      return False
    return self._nightly_dict[ds_name][config] is True  # pylint: disable=g-bool-id-comparison

  def is_version_nightly(
      self,
      builder: tfds.core.DatasetBuilder,
      version: str,
  ) -> bool:
    """Returns `True` if the version is new."""
    ds_name, config, _ = _split_full_name(builder.info.full_name)
    if self.is_builder_nightly(builder) or self.is_config_nightly(builder):
      return False
    return self._nightly_dict[ds_name][config][version] is True  # pylint: disable=g-bool-id-comparison

  def has_nightly(self, builder: tfds.core.DatasetBuilder) -> bool:
    """Returns True if any of the builder/config/version is new."""
    def reduce(value):
      if isinstance(value, bool):
        return value
      elif isinstance(value, dict):
        return any(reduce(x) for x in value.values())
      else:
        raise AssertionError(f'Invalid nightly_dict value: {value}')

    return reduce(self._nightly_dict[builder.name])

  icon = (
      '<span class="material-icons" '
      'title="Available only in the tfds-nightly package">nights_stay</span>')


@tfds.core.utils.memoize()
def get_mako_template(tmpl_name):
  """Returns mako.lookup.Template object to use to render documentation.

  Args:
    tmpl_name: string, name of template to load.

  Returns:
    mako 'Template' instance that can be rendered.
  """
  tmpl_path = tfds.core.utils.get_tfds_path(
      'scripts/documentation/templates/%s.mako.md' % tmpl_name)
  with tf.io.gfile.GFile(tmpl_path, 'r') as tmpl_f:
    tmpl_content = tmpl_f.read()
  return mako.lookup.Template(tmpl_content, default_filters=['str', 'trim'])


def document_single_builder(builder):
  """Doc string for a single builder, with or without configs."""
  print('Document builder %s...' % builder.name)
  get_config_builder = lambda config: tfds.builder(builder.name, config=config)
  config_builders = []
  if builder.builder_configs:
    with futures.ThreadPoolExecutor(max_workers=WORKER_COUNT_CONFIGS) as tpool:
      config_builders = list(
          tpool.map(get_config_builder, builder.BUILDER_CONFIGS))
  visu_doc_util = VisualizationDocUtil()
  out_str = dataset_markdown_builder.get_markdown_string(
      builder=builder,
      config_builders=config_builders,
      visu_doc_util=visu_doc_util,
      nightly_doc_util=NightlyDocUtil(),
  )
  schema_org_tmpl = get_mako_template('schema_org')
  schema_org_out_str = schema_org_tmpl.render_unicode(
      builder=builder,
      config_builders=config_builders,
      visu_doc_util=visu_doc_util,
  ).strip()
  out_str = schema_org_out_str + '\n' + out_str
  return out_str


def make_module_to_builder_dict(datasets=None):
  """Get all builders organized by module in nested dicts."""
  # pylint: disable=g-long-lambda
  # dict to hold tfds->image->mnist->[builders]
  module_to_builder = collections.defaultdict(
      lambda: collections.defaultdict(
          lambda: collections.defaultdict(list)))
  # pylint: enable=g-long-lambda

  if not datasets:
    datasets = [
        name for name in tfds.list_builders() if name not in BUILDER_BLACKLIST
    ]
  print('Creating the vanilla builders for %s datasets...' % len(datasets))
  with futures.ThreadPoolExecutor(max_workers=WORKER_COUNT_DATASETS) as tpool:
    builders = tpool.map(tfds.builder, datasets)
  print('Vanilla builders built, constructing module_to_builder dict...')

  for builder in builders:
    module_name = builder.__class__.__module__
    modules = module_name.split('.')
    if 'testing' in modules:
      continue

    current_mod_ctr = module_to_builder
    for mod in modules:
      current_mod_ctr = current_mod_ctr[mod]
    current_mod_ctr.append(builder)  # pytype: disable=attribute-error

  module_to_builder = module_to_builder['tensorflow_datasets']
  return module_to_builder


def dataset_docs_str(datasets=None):
  """Create dataset documentation string for given datasets.

  Args:
    datasets: list of datasets for which to create documentation.
              If None, then all available datasets will be used.

  Returns:
    - overview document
    - a dictionary of sections. Each dataset in a section is represented by a
    tuple (dataset_name, is_manual_dataset, string describing the datasets
    (in the MarkDown format))
  """

  print('Retrieving the list of builders...')
  module_to_builder = make_module_to_builder_dict(datasets)
  sections = sorted(list(module_to_builder.keys()))
  section_docs = collections.defaultdict(list)

  for section in sections:
    builders = tf.nest.flatten(module_to_builder[section])
    builders = sorted(builders, key=lambda b: b.name)
    with futures.ThreadPoolExecutor(max_workers=WORKER_COUNT_DATASETS) as tpool:
      builder_docs = tpool.map(document_single_builder, builders)
    builder_docs = [(builder.name, builder.MANUAL_DOWNLOAD_INSTRUCTIONS,
                     builder_doc)
                    for (builder, builder_doc) in zip(builders, builder_docs)]
    section_docs[section] = builder_docs
  tmpl = get_mako_template('catalog_overview')
  catalog_overview = tmpl.render_unicode().lstrip()
  return [catalog_overview, section_docs]
