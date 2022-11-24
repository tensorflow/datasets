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
import dataclasses
import json
import os
import textwrap
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

import tensorflow_datasets as tfds
from tensorflow_datasets.core import constants
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

# Dict of `full_names_dict['dataset']['config']['version']`
FullNamesDict = Dict[str, Dict[str, Dict[str, Any]]]
# Same as `FullNamesDict`, but contains `True` for nightly datasets:
# * New dataset: nightly_dict['dataset'] is True
# * New config: nightly_dict['dataset']['config'] is True
# * New version: nightly_dict['dataset']['config']['version'] is True
NightlyDict = Dict[str, Union[bool, Dict[str, Union[bool, Dict[str, bool]]]]]


def get_pwc_catalog_urls() -> Mapping[str, str]:
  with open(constants.PWC_LINKS_PATH, 'r') as f:
    return json.load(f)


@dataclasses.dataclass
class DocUtilPaths:
  """Structure containing the utils paths."""
  # VisualizationDocUtil
  fig_base_path: Optional[tfds.typing.PathLike] = tfds.core.gcs_path(
      'visualization/fig/')
  fig_base_url: str = 'https://storage.googleapis.com/tfds-data/visualization/fig/'
  # DataframeDocUtil
  df_base_path: Optional[tfds.typing.PathLike] = tfds.core.gcs_path(
      'visualization/dataframe')
  df_base_url: str = 'https://storage.googleapis.com/tfds-data/visualization/dataframe/'
  # NightlyDocUtil
  nightly_path: Optional[tfds.typing.PathLike] = tfds.core.utils.tfds_path(
      'stable_versions.txt')


class VisualizationDocUtil(object):
  """Small util which generate the path/urls for the visualizations."""

  def __init__(self, base_path: tfds.typing.PathLike, base_url: str):
    """Constructor.

    Args:
      base_path: Path where images are stored.
      base_url: Base url where images are displayed.
    """
    self._base_path = base_path
    self._base_url = base_url

  def _get_name(self, builder):
    return builder.info.full_name.replace('/', '-') + '.png'

  def get_url(self, builder):
    return self._base_url + self._get_name(builder)

  def get_html_tag(self, builder: tfds.core.DatasetBuilder) -> str:
    """Returns the <img> html tag."""
    url = self.get_url(builder)
    return f'<img src="{url}" alt="Visualization" width="500px">'

  def has_visualization(self, builder):
    filepath = os.path.join(self._base_path, self._get_name(builder))
    return tf.io.gfile.exists(filepath)


class DataframeDocUtil(object):
  """Small util which generates the path/urls for the dataframes."""

  def __init__(self, base_path: tfds.typing.PathLike, base_url: str):
    """Constructor.

    Args:
      base_path: Path where images are stored.
      base_url: Base url where images are displayed.
    """
    self._base_path = base_path
    self._base_url = base_url

  def _get_name(self, builder):
    return builder.info.full_name.replace('/', '-') + '.html'

  def get_url(self, builder):
    return self._base_url + self._get_name(builder)

  def get_html_tag(self, builder: tfds.core.DatasetBuilder) -> str:
    """Returns the html tag."""
    url = self.get_url(builder)
    button_id = 'displaydataframe'
    content_id = 'dataframecontent'
    visualization_html = f"""
    <!-- mdformat off(HTML should not be auto-formatted) -->

    {{% framebox %}}

    <button id="{button_id}">Display examples...</button>
    <div id="{content_id}" style="overflow-x:auto"></div>
    <script>
    const url = "{url}";
    const dataButton = document.getElementById('{button_id}');
    dataButton.addEventListener('click', async () => {{
      // Disable the button after clicking (dataframe loaded only once).
      dataButton.disabled = true;

      const contentPane = document.getElementById('{content_id}');
      try {{
        const response = await fetch(url);
        // Error response codes don't throw an error, so force an error to show
        // the error message.
        if (!response.ok) throw Error(response.statusText);

        const data = await response.text();
        contentPane.innerHTML = data;
      }} catch (e) {{
        contentPane.innerHTML =
            'Error loading examples. If the error persist, please open '
            + 'a new issue.';
      }}
    }});
    </script>

    {{% endframebox %}}

    <!-- mdformat on -->
    """
    return textwrap.dedent(visualization_html)

  def has_visualization(self, builder):
    filepath = os.path.join(self._base_path, self._get_name(builder))
    return tf.io.gfile.exists(filepath)


def _split_full_name(full_name: str) -> Tuple[str, str, str]:
  """Extracts the `(ds name, config, version)` from the full_name."""
  if not tfds.core.load.is_full_name(full_name):
    raise ValueError(f'Parsing builder name string {full_name} failed.'
                     'The builder name string must be of the following format:'
                     '`dataset_name[/config_name]/version`')
  ds_name, *optional_config, version = full_name.split('/')
  assert len(optional_config) <= 1
  config = next(iter(optional_config)) if optional_config else ''
  return ds_name, config, version


def _full_names_to_dict(full_names: List[str]) -> FullNamesDict:
  """Creates the dict `d['dataset']['config']['version']`."""
  full_names_dict = collections.defaultdict(lambda: collections.defaultdict(  # pylint: disable=g-long-lambda
      lambda: collections.defaultdict(type(None))))
  for full_name in full_names:
    ds_name, config, version = _split_full_name(full_name)
    full_names_dict[ds_name][config][version]  # pylint: disable=pointless-statement
  return full_names_dict


def _build_nightly_dict(
    registered_ds: FullNamesDict,
    stable_version_ds: FullNamesDict,
) -> NightlyDict:
  """Computes the nightly dict from the registered and stable dict."""
  nightly_ds = collections.defaultdict(lambda: collections.defaultdict(  # pylint: disable=g-long-lambda
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
def _load_nightly_dict(version_path: tfds.typing.PathLike) -> NightlyDict:
  """Loads (and caches) the nightly dict."""
  with tf.io.gfile.GFile(os.fspath(version_path), 'r') as f:
    stable_versions = f.read().splitlines()

  # Build the `full_names_dict['dataset']['config']['version']` for both
  # nightly and stable version
  registered_ds = _full_names_to_dict(tfds.core.load.list_full_names())
  stable_version_ds = _full_names_to_dict(stable_versions)

  # Nightly versions are `registered - stable`
  return _build_nightly_dict(registered_ds, stable_version_ds)


class NightlyDocUtil(object):
  """Small util to format the doc."""

  def __init__(self, path: tfds.typing.PathLike):
    """Constructor.

    Args:
      path: Path containing the nightly versions
    """
    self._nightly_dict: NightlyDict = _load_nightly_dict(path)

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


def format_homepage_url(homepage):
  """Formats a URL as required for the homepage section."""
  return f'[{homepage}]({homepage})'
