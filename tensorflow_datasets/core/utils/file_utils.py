# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""Library of helper functions to handle dealing with files."""

import collections
import functools
import os
import re
import time
from typing import Iterator, List, Optional

from absl import logging
from etils import epath
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import naming
from tensorflow_datasets.core.utils import docs
from tensorflow_datasets.core.utils import py_utils
from tensorflow_datasets.core.utils import read_config
from tensorflow_datasets.core.utils import type_utils
from tensorflow_datasets.core.utils import version as version_lib

PathLike = epath.PathLike
ListOrElem = type_utils.ListOrElem
Path = epath.Path

_registered_data_dir = set()
_GLOB_CHARS = ['*', '?', '[']


@docs.deprecated
def as_path(path: PathLike) -> Path:
  """DEPRECATED. Please use `from etils import epath` with `epath.Path()`."""
  msg = py_utils.dedent(
      """
      `tfds.core.as_path` is deprecated. Pathlib API has been moved to a
      separate module. To migrate, use:

      ```
      from etils import epath
      path = epath.Path('gs://path/to/f.txt')
      ```

      Alternatively `tfds.core.Path` is an alias of `epath.Path`.

      Installation: `pip install etils[epath]`

      """
  )
  logging.warning(msg)
  return epath.Path(path)


def add_data_dir(data_dir):
  """Registers a new default `data_dir` to search for datasets.

  When a `tfds.core.DatasetBuilder` is created with `data_dir=None`, TFDS
  will look in all registered `data_dir` (including the default one) to
  load existing datasets.

  * An error is raised if a dataset can be loaded from more than 1 registered
    data_dir.
  * This only affects reading datasets. Generation always uses the
    `data_dir` kwargs when specified or `tfds.core.constant.DATA_DIR` otherwise.

  Args:
    data_dir: New data_dir to register.
  """
  # Remove trailing / to avoid same directory being included twice in the set
  # with and without a final slash.
  data_dir = data_dir.rstrip('/')
  _registered_data_dir.add(data_dir)


def list_data_dirs(
    given_data_dir: Optional[ListOrElem[PathLike]] = None,
    dataset: Optional[str] = None,
) -> List[PathLike]:
  """Return the list of all `data_dir` to look-up.

  Args:
    given_data_dir: If a `data_dir` is provided, only the explicitly given
      `data_dir` will be returned, otherwise the list of all registered data_dir
      is returned
    dataset: Dataset to load.

  Returns:
    The list of all data_dirs to look-up.
  """
  # If the data dir is explicitly given, no need to search everywhere.
  if given_data_dir:
    if isinstance(given_data_dir, list):
      return given_data_dir
    else:
      return [given_data_dir]
  else:
    default_data_dir = get_default_data_dir(
        given_data_dir=given_data_dir, dataset=dataset
    )
    all_data_dirs = _registered_data_dir | {default_data_dir}
    return sorted(os.path.expanduser(d) for d in all_data_dirs)


def get_default_data_dir(
    given_data_dir: Optional[str] = None, dataset: Optional[str] = None
) -> str:
  """Returns the default data_dir."""
  if given_data_dir:
    return os.path.expanduser(given_data_dir)
  elif 'TFDS_DATA_DIR' in os.environ:
    return os.environ['TFDS_DATA_DIR']
  else:
    return constants.DATA_DIR


def _looks_like_a_tfds_file(filename: str) -> bool:
  filename_has_shard_re = re.compile(r'.*\d{5,}-of-\d{5,}.*')
  return bool(filename_has_shard_re.match(filename)) or filename.endswith(
      '.json'
  )


def list_dataset_variants(
    dataset_name: str,
    dataset_dir: epath.PathLike,
    namespace: Optional[str] = None,
    include_versions: bool = True,
    include_old_tfds_version: bool = False,
) -> Iterator[naming.DatasetReference]:
  """Yields all variants (config + version) found in `dataset_dir`.

  Arguments:
    dataset_name: the name of the dataset for which variants are listed.
    dataset_dir: the folder of the dataset.
    namespace: optional namespace to which this data dir belongs.
    include_versions: whether to list what versions are available.
    include_old_tfds_version: include datasets that have been generated with
      TFDS before 4.0.0.

  Yields:
    all variants of the given dataset.
  """
  dataset_dir = epath.Path(dataset_dir)
  data_dir = dataset_dir.parent
  base_reference = naming.DatasetReference(
      dataset_name=dataset_name, namespace=namespace, data_dir=data_dir
  )

  json_files_per_folder = collections.defaultdict(set)
  interesting_file_names = [
      constants.FEATURES_FILENAME,
      constants.DATASET_INFO_FILENAME,
  ]
  # Check all JSON files under a config.
  for json_file in dataset_dir.glob('*/*/*.json'):
    if json_file.name in interesting_file_names:
      json_files_per_folder[json_file.parent].add(json_file.name)
  # Check all JSON files that are not under a config.
  for json_file in dataset_dir.glob('*/*.json'):
    if json_file.name in interesting_file_names:
      json_files_per_folder[json_file.parent].add(json_file.name)

  version_references_per_config = collections.defaultdict(list)
  for folder, json_files in json_files_per_folder.items():
    if constants.DATASET_INFO_FILENAME not in json_files:
      logging.warning(
          'Ignoring dataset folder %s, which has no dataset_info.json',
          os.fspath(folder),
      )
      continue
    if (
        not include_old_tfds_version
        and constants.FEATURES_FILENAME not in json_files
    ):
      logging.info(
          'Ignoring dataset folder %s, which has no features.json',
          os.fspath(folder),
      )
      continue
    version = folder.name
    if not version_lib.Version.is_valid(version):
      logging.warning(
          'Ignoring dataset folder %s, which has invalid version %s',
          os.fspath(folder),
          version,
      )
      continue
    if folder.parent == dataset_dir:
      config = None
    else:
      config = folder.parent.name
    reference = base_reference.replace(config=config, version=version)
    version_references_per_config[config].append(reference)

  if include_versions:
    for versions in version_references_per_config.values():
      yield from versions
  else:
    for config in version_references_per_config.keys():
      yield base_reference.replace(config=config)


def list_datasets_in_data_dir(
    data_dir: epath.PathLike,
    namespace: Optional[str] = None,
    include_configs: bool = True,
    include_versions: bool = True,
    include_old_tfds_version: bool = False,
) -> Iterator[naming.DatasetReference]:
  """Yields references to the datasets found in `data_dir`.

  Only finds datasets that were written to `data_dir`. This means that if
  `data_dir` contains a sub-folder with datasets in them, that these will not be
  found.

  Arguments:
    data_dir: the folder where to look for datasets.
    namespace: optional namespace to which this data dir belongs.
    include_configs: whether to list what configs are available.
    include_versions: whether to list what versions are available.
    include_old_tfds_version: include datasets that have been generated with
      TFDS before 4.0.0.

  Yields:
    references to the datasets found in `data_dir`. The references include the
    data dir.
  """
  for dataset_dir in epath.Path(data_dir).iterdir():
    if not dataset_dir.is_dir():
      continue
    if not naming.is_valid_dataset_name(dataset_dir.name):
      continue
    if include_configs:
      yield from list_dataset_variants(
          dataset_name=dataset_dir.name,
          dataset_dir=dataset_dir,
          namespace=namespace,
          include_versions=include_versions,
          include_old_tfds_version=include_old_tfds_version,
      )
    else:
      yield naming.DatasetReference(
          dataset_name=dataset_dir.name, namespace=namespace, data_dir=data_dir
      )


@functools.lru_cache(maxsize=None)
def makedirs_cached(dirname: epath.PathLike):
  """Creates the given dir with parents and exist is ok.

  Note that this operation is cached, so a dir is only created once. Use this
  with care. If during your session you remove the folder and later you want to
  recreate it, then this method will not do that.

  Arguments:
    dirname: the dir to create.
  """
  epath.Path(dirname).mkdir(parents=True, exist_ok=True)


def expand_glob(path: epath.PathLike) -> List[epath.Path]:
  """Returns all files that match the glob in the given path.

  Warning: If `path` does not contain any wildcards, we do not check whether
  `path` exists and always return `[path]`. In addition, we don't expand the
  `@*` pattern to specify shard wildcards.

  Arguments:
    path: a path that can contain a glob.

  Returns:
    all files that match the given glob.
  """
  path = epath.Path(path).expanduser()
  path_str = os.fspath(path)
  # We don't expand wildcards for number of shards, i.e. paths ending with @*.
  path_str_no_shard_wildcard = re.sub(r'@\*$', '', path_str)
  if not any([char in path_str_no_shard_wildcard for char in _GLOB_CHARS]):
    return [path]
  if not path_str.startswith('/'):
    logging.warning(
        'Can only expand globs for paths starting with a `/`. Got: %s', path
    )
    return [path]
  return list(epath.Path('/').glob(path_str[1:]))
