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

"""Library of helper functions to handle dealing with files."""

import collections
from collections.abc import Iterator, Sequence
import functools
import os
import re
import time

from absl import logging
from etils import epath
from etils import epy
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
    given_data_dir: ListOrElem[PathLike] | None = None,
    dataset: str | None = None,
) -> Sequence[PathLike]:
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
    given_data_dir: str | None = None, dataset: str | None = None
) -> str:
  """Returns the default data_dir."""
  if given_data_dir:
    return os.path.expanduser(given_data_dir)
  elif 'TFDS_DATA_DIR' in os.environ:
    return os.environ['TFDS_DATA_DIR']
  else:
    del dataset
    return constants.DATA_DIR


def _looks_like_a_tfds_file(filename: str) -> bool:
  filename_has_shard_re = re.compile(r'.*\d{5,}-of-\d{5,}.*')
  return bool(filename_has_shard_re.match(filename)) or filename.endswith(
      '.json'
  )


def _find_files_without_glob(
    folder: epath.Path, globs: list[str], file_names: list[str]
) -> Iterator[epath.Path]:
  """Finds files without using globs over nested folders.

  When there is a folder with no permission, then the entire glob fails. This
  function uses `iterdir` to find subfolders.

  Args:
    folder: the folder in which to find files.
    globs: the glob patterns to use to find files.
    file_names: the file names that we are interested in. Used to filter
      results.

  Yields:
    the matching file paths.
  """
  for glob in globs:
    glob_parts = glob.split('/')
    if len(glob_parts) == 1:
      try:
        for file in folder.iterdir():
          if file.name in file_names:
            yield file
      except OSError:
        logging.exception('Could not find files in %s', folder)
        continue
    else:
      if glob_parts[0] != '*':
        raise NotImplementedError()
      remaining_glob = '/'.join(glob_parts[1:])
      for subfolder in folder.iterdir():
        if not subfolder.is_dir() or subfolder.name.startswith('.'):
          # Ignore files and folders starting with a dot.
          continue
        yield from _find_files_with_glob(
            subfolder, globs=[remaining_glob], file_names=file_names
        )


def _find_files_with_glob(
    folder: epath.Path, globs: list[str], file_names: list[str]
) -> Iterator[epath.Path]:
  """Finds files matching any of the given globs and given file names."""
  for glob in globs:
    try:
      for file in folder.glob(glob):
        if file.name in file_names:
          yield file
    except OSError:
      # If permission was denied on any subfolder, then the glob fails. Manually
      # iterate through the subfolders instead to be more robust against this.
      yield from _find_files_without_glob(folder, globs, file_names)


def _find_references_with_glob(
    folder: epath.Path,
    is_data_dir: bool,
    is_dataset_dir: bool,
    namespace: str | None = None,
    include_old_tfds_version: bool = True,
) -> Iterator[naming.DatasetReference]:
  """Yields all dataset references in the given folder.

  Args:
    folder: the folder where to look for datasets. Can be either a root data
      dir, or a dataset folder.
    is_data_dir: Whether `folder` is a root TFDS data dir.
    is_dataset_dir: Whether `folder` is the folder of one specific dataset.
    namespace: Optional namespace to which the found datasets belong to.
    include_old_tfds_version: include datasets that have been generated with
      TFDS before 4.0.0.

  Yields:
    all dataset references in the given folder.
  """
  if is_dataset_dir and is_data_dir:
    raise ValueError('Folder cannot be both a data dir and dataset dir!')
  if not is_data_dir and not is_dataset_dir:
    raise ValueError('Folder must be either a data dir or a dataset dir!')

  if is_data_dir:
    data_dir = folder
    dataset_name = None
    globs = ['*/*/*/*.json', '*/*/*.json']
  else:
    data_dir = folder.parent
    dataset_name = folder.name
    globs = ['*/*/*.json', '*/*.json']

  # Check files matching the globs and are files we are interested in.
  matched_files_per_folder = collections.defaultdict(set)
  file_names = [constants.FEATURES_FILENAME, constants.DATASET_INFO_FILENAME]
  for file in _find_files_with_glob(folder, globs=globs, file_names=file_names):
    matched_files_per_folder[file.parent].add(file.name)

  for data_folder, matched_files in matched_files_per_folder.items():
    if constants.DATASET_INFO_FILENAME not in matched_files:
      logging.warning(
          'Ignoring dataset folder %s, which has no dataset_info.json',
          os.fspath(data_folder),
      )
      continue
    if (
        not include_old_tfds_version
        and constants.FEATURES_FILENAME not in matched_files
    ):
      logging.info(
          'Ignoring dataset folder %s, which has no features.json',
          os.fspath(data_folder),
      )
      continue

    version = data_folder.name
    if not version_lib.Version.is_valid(version):
      logging.warning(
          'Ignoring dataset folder %s, which has invalid version %s',
          os.fspath(data_folder),
          version,
      )
      continue

    config = None
    if is_data_dir:
      if data_folder.parent.parent == folder:
        dataset_name = data_folder.parent.name
      elif data_folder.parent.parent.parent == folder:
        dataset_name = data_folder.parent.parent.name
        config = data_folder.parent.name
      else:
        raise ValueError(
            f'Could not detect dataset and config from path {data_folder} in'
            f' {folder}'
        )
    else:
      if data_folder.parent != folder:
        config = data_folder.parent.name

    if not naming.is_valid_dataset_name(dataset_name):
      logging.warning('Invalid dataset name: %s', dataset_name)
      continue

    yield naming.DatasetReference(
        namespace=namespace,
        data_dir=data_dir,
        dataset_name=dataset_name,
        config=config,
        version=version,
    )


def list_dataset_variants(
    dataset_dir: epath.PathLike,
    namespace: str | None = None,
    include_versions: bool = True,
    include_old_tfds_version: bool = False,
) -> Iterator[naming.DatasetReference]:
  """Yields all variants (config + version) found in `dataset_dir`.

  Arguments:
    dataset_dir: the folder of the dataset.
    namespace: optional namespace to which this data dir belongs.
    include_versions: whether to list what versions are available.
    include_old_tfds_version: include datasets that have been generated with
      TFDS before 4.0.0.

  Yields:
    all variants of the given dataset.
  """
  dataset_dir = epath.Path(dataset_dir)
  references = {}
  for reference in _find_references_with_glob(
      folder=dataset_dir,
      is_data_dir=False,
      is_dataset_dir=True,
      namespace=namespace,
      include_old_tfds_version=include_old_tfds_version,
  ):
    if include_versions:
      key = f'{reference.dataset_name}/{reference.config}:{reference.version}'
    else:
      key = f'{reference.dataset_name}/{reference.config}'
      reference = reference.replace(version=None)
    references[key] = reference

  for reference in references.values():
    yield reference


def list_datasets_in_data_dir(
    data_dir: epath.PathLike,
    namespace: str | None = None,
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
  num_datasets = 0
  num_variants = 0
  for dataset_dir in epath.Path(data_dir).iterdir():
    if not dataset_dir.is_dir():
      continue
    if not naming.is_valid_dataset_name(dataset_dir.name):
      continue
    num_datasets += 1
    if include_configs:
      for variant in list_dataset_variants(
          dataset_dir=dataset_dir,
          namespace=namespace,
          include_versions=include_versions,
          include_old_tfds_version=include_old_tfds_version,
      ):
        num_variants += 1
        yield variant
    else:
      num_variants += 1
      yield naming.DatasetReference(
          dataset_name=dataset_dir.name, namespace=namespace, data_dir=data_dir
      )
  logging.info(
      'Found %d datasets and %d variants in %s',
      num_datasets,
      num_variants,
      data_dir,
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


def expand_glob(path: epath.PathLike) -> Sequence[epath.Path]:
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


def publish_data(
    from_data_dir: epath.Path,
    to_data_dir: epath.Path,
    overwrite: bool = False,
) -> None:
  """Publishes the data from the given `from_data_dir` to `to_data_dir`.

  Arguments:
    from_data_dir: the folder whose data needs to be published.
    to_data_dir: folder where the data should be published. Should include
      config and version.
    overwrite: whether to overwrite existing data in the `publish_root_dir` if
      it exists.
  """
  to_data_dir.mkdir(parents=True, exist_ok=True)
  for filepath in from_data_dir.iterdir():
    filepath.copy(dst=to_data_dir / filepath.name, overwrite=overwrite)
