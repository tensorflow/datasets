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

"""Library of helper functions to handle dealing with files."""

import concurrent.futures
import functools
import multiprocessing
import os
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


@docs.deprecated
def as_path(path: PathLike) -> Path:
  """DEPRECATED. Please use `from etils import epath` with `epath.Path()`."""
  msg = py_utils.dedent("""
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


def list_data_dirs(given_data_dir: Optional[ListOrElem[PathLike]] = None,
                   dataset: Optional[str] = None) -> List[PathLike]:
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
        given_data_dir=given_data_dir, dataset=dataset)
    all_data_dirs = _registered_data_dir | {default_data_dir}
    return sorted(os.path.expanduser(d) for d in all_data_dirs)


def get_default_data_dir(given_data_dir: Optional[str] = None,
                         dataset: Optional[str] = None) -> str:
  """Returns the default data_dir."""
  if given_data_dir:
    return os.path.expanduser(given_data_dir)
  elif 'TFDS_DATA_DIR' in os.environ:
    return os.environ['TFDS_DATA_DIR']
  else:
    return constants.DATA_DIR


def is_version_folder(
    folder: epath.PathLike,
    check_content: bool = True,
    include_old_tfds_version: bool = False,
) -> bool:
  """Returns whether `folder` is a version folder and contains dataset metadata.

  Checks that the deepest directory is a semantic version (e.g. `3.1.4`) and
  whether it contains dataset metadata files.

  Arguments:
    folder: the folder to check.
    check_content: whether to check the content for the folder if it contains
      files required for a dataset.
    include_old_tfds_version: include datasets that have been generated with
      TFDS before 4.0.0. This is only used if `check_content=True`.

  Returns:
    whether `folder` is a version folder and contains dataset metadata.
  """
  folder = epath.Path(folder)
  looks_like_a_version = version_lib.Version.is_valid(folder.name)
  if check_content:
    if include_old_tfds_version:
      # If TFDS version before 4.0.0 was used, then the generated dataset
      # doesn't contain `features.json`, but has `dataset_info.json`.
      content_to_check = folder / constants.DATASET_INFO_FILENAME
    else:
      content_to_check = folder / constants.FEATURES_FILENAME
    return looks_like_a_version and content_to_check.exists()
  else:
    return looks_like_a_version


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
      dataset_name=dataset_name, namespace=namespace, data_dir=data_dir)

  is_version_folder_ = functools.partial(
      is_version_folder,
      check_content=include_versions,
      include_old_tfds_version=include_old_tfds_version)

  def get_dataset_references(
      config_or_version_dir: epath.Path) -> Iterator[naming.DatasetReference]:
    logging.info('Getting configs and versions in %s', config_or_version_dir)
    if is_version_folder_(config_or_version_dir):
      if include_versions:
        yield base_reference.replace(version=config_or_version_dir.name)
      else:
        yield base_reference
    elif config_or_version_dir.is_dir():
      config = config_or_version_dir.name
      if not include_versions:
        yield base_reference.replace(config=config)
      else:
        for version_dir in config_or_version_dir.iterdir():
          if is_version_folder_(version_dir):
            yield base_reference.replace(
                config=config, version=version_dir.name)

  with concurrent.futures.ThreadPoolExecutor(
      max_workers=multiprocessing.cpu_count()) as executor:
    for references in executor.map(get_dataset_references,
                                   dataset_dir.iterdir()):
      yield from references


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
          include_old_tfds_version=include_old_tfds_version)
    else:
      yield naming.DatasetReference(
          dataset_name=dataset_dir.name, namespace=namespace, data_dir=data_dir)


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
