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

"""Source-based register."""

import collections
import dataclasses
import datetime
import hashlib
import json
import tempfile
from typing import Any, List, Optional, Type

from absl import logging

from etils import epath
from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.community import cache
from tensorflow_datasets.core.community import dataset_sources as dataset_sources_lib
from tensorflow_datasets.core.community import load
from tensorflow_datasets.core.community import register_base
from tensorflow_datasets.core.download import checksums
from tensorflow_datasets.core.utils import gcs_utils

# Datasets are installed as `import tfds_community.<ns>.<ds>.<hash>`
_IMPORT_MODULE_NAME = 'tfds_community'
_METADATA_FILENAME = 'installation.json'


@dataclasses.dataclass(frozen=True, eq=True)
class DatasetPackage:
  """Dataset metadata (before installation), of a single dataset package.

  Contains the information required to fetch the dataset package.

  Attributes:
    name: Dataset name
    source: Source that contains the source code (e.g. `github://...`)
  """
  name: utils.DatasetName
  source: dataset_sources_lib.DatasetSource
  # Ideally, we should also save the version so `tfds.load('ns:ds/1.0.0')`
  # fetch a specific version (e.g. at an older commit).

  @classmethod
  def from_json(cls, data: utils.Json) -> 'DatasetPackage':
    """Factory which creates the cls from json."""
    return cls(
        name=utils.DatasetName(namespace_name=data['name']),
        source=dataset_sources_lib.DatasetSource.from_json(data['source']),
    )

  def to_json(self) -> utils.Json:
    """Exports the cls as json."""
    return {
        'name': str(self.name),
        'source': self.source.to_json(),
    }


@dataclasses.dataclass(frozen=True, eq=True)
class _InstalledPackage:
  """Dataset metadata (after installation), of a single dataset package.

  Contains the local informations of the installed dataset package. This is
  specific to the user.

  Attributes:
    package: Source of the dataset package.
    instalation_date: Date of installation of the package
    hash: base64 checksum of the installed files
  """
  package: DatasetPackage
  instalation_date: datetime.datetime
  hash: str

  @property
  def module_name(self) -> str:
    """Module name to import this dataset."""
    name = self.package.name
    return f'{_IMPORT_MODULE_NAME}.{name.namespace}.{name.name}.{self.hash}.{name.name}'

  @property
  def installation_path(self) -> epath.Path:
    """Local path of the package."""
    name = self.package.name
    sub_dir = f'{_IMPORT_MODULE_NAME}/{name.namespace}/{name.name}/{self.hash}'
    return cache.module_path() / sub_dir

  @classmethod
  def from_json(cls, data: utils.Json) -> '_InstalledPackage':
    """Factory which creates the cls from json."""
    return cls(
        package=DatasetPackage.from_json(data['package']),
        # TODO(py3.7): Should use `datetime.fromisoformat`
        instalation_date=datetime.datetime.strptime(data['instalation_date'],
                                                    '%Y-%m-%dT%H:%M:%S.%f'),
        hash=data['hash'],
    )

  def to_json(self) -> utils.Json:
    """Exports the cls as json."""
    return {
        'package': self.package.to_json(),
        'instalation_date': self.instalation_date.isoformat(),
        'hash': self.hash,
    }


# TODO(py3.9): Should be `UserDict[utils.DatasetName, _DatasetPackage]`
class _PackageIndex(collections.UserDict):
  """Package index.

  Package index is a `Dict[DatasetName, _DatasetPackage]` loaded from cache.
  It has an additional `.refresh()` method to update the local cache by
  querying the remote index (stored in `gs://tfds-data`).

  On disk, the package index is a simple list of datasets with their
  associated source:

  ```jsonl
  {"name": "kaggle:ds0", "source": "github://..."}
  {"name": "kaggle:ds1", "source": "github://..."}
  {"name": "tensorflow_graphics:shapenet", "source": "github://..."}
  [...]
  ```

  """

  def __init__(self, path: epath.PathLike):
    """Contructor.

    Args:
      path: Remote location of the package index (file containing the list of
        dataset packages)
    """
    super().__init__()
    self._remote_path: epath.Path = epath.Path(path)
    self._cached_path: epath.Path = (
        cache.cache_path() / 'community-datasets-list.jsonl')

    # Pre-load the index from the cache
    if self._cached_path.exists():
      self._refresh_from_content(self._cached_path.read_text())

  def _refresh_from_content(self, content: str) -> None:
    """Update the index from the given `jsonl` content."""
    dataset_packages = [
        DatasetPackage.from_json(json.loads(line))
        for line in content.splitlines()
        if line.strip()
    ]
    self.clear()
    self.update({src.name: src for src in dataset_packages})

  def refresh(self) -> None:
    """Update the cache."""
    # Should have a timer to avoid refreshing the cache immediatelly
    # (and a force=True option to ignore this)
    # e.g. with os.path.getmtime(cached_path) - time.gmtime()

    try:
      content = self._remote_path.read_text()
    except gcs_utils.GCS_UNAVAILABLE_EXCEPTIONS as e:
      # Do not crash if GCS access not available, but instead silently reuse
      # the cache.
      logging.info('Could not refresh the package index (GCS unavailable): %s',
                   e)
      return

    # If read was sucessful, update the cache with the new dataset list
    self._cached_path.write_text(content)  # pytype: disable=attribute-error  # attribute-variable-annotations
    self._refresh_from_content(content)


class PackageRegister(register_base.BaseRegister):
  """Dataset register based on a list of remotely stored datasets definitions.

  Package register is similar to a dataset package manager. It contains a
  package index containing the list of all registered datasets with their
  associated location.
  When a specific dataset is requested, `PackageRegister` will download
  and cache the original source code locally.

  Usage:

  ```python
  register = PackageRegister(path='/path/to/datasets-source-list.jsonl')

  # List all registered datasets: ['kaggle:ds0', 'kaggle:ds1',...]
  register.list_builders()

  # Load a specific dataset
  builder = register.builder('tensorflow_graphics:shapenet')
  ```

  """

  def __init__(self, path: epath.PathLike):
    """Contructor.

    Args:
      path: Path to the register files containing the list of dataset sources,
        forwarded to `_PackageIndex`
    """
    self._path = path

  @utils.memoized_property
  def _package_index(self) -> _PackageIndex:
    """`Dict[DatasetName, _DatasetPackage]` containg the community datasets."""
    # Use property to lazy-initialize the cache (and create the tmp dir) only
    # if it is used.
    return _PackageIndex(self._path)

  def list_builders(self) -> List[str]:
    """Returns the list of registered builders."""
    if not self._package_index:  # Package index not loaded nor cached
      self._package_index.refresh()  # Try updating the index
    return sorted(str(name) for name in self._package_index)  # pylint: disable=not-an-iterable

  def builder_cls(
      self,
      name: utils.DatasetName,
  ) -> Type[dataset_builder.DatasetBuilder]:
    """Returns the builder class."""
    # Download the dataset generation code, or reuse the cache
    # TODO(tfds): Should add the option to request a specific code version
    installed_dataset = _download_or_reuse_cache(
        name=name,
        package_index=self._package_index,
    )

    # Load the dataset from the module
    return load.builder_cls_from_module(installed_dataset.module_name)

  def builder(
      self,
      name: utils.DatasetName,
      **builder_kwargs: Any,
  ) -> dataset_builder.DatasetBuilder:
    """Returns the dataset builder."""
    return self.builder_cls(name)(**builder_kwargs)  # pytype: disable=not-instantiable


def list_ds_packages_for_namespace(
    namespace: str,
    path: epath.Path,
) -> List[DatasetPackage]:
  """Returns the dataset names found in a specific directory.

  Directories that contain code should have the following structure:

  ```
  <path>/
      <dataset0>/
          <dataset0>.py
      <dataset1>/
          <dataset1>.py
      ...
  ```

  Additional files or folders which are not detected as datasets will be
  ignored (e.g. `__init__.py`).

  Args:
    namespace: Namespace of the datasets
    path: The directory path containing the datasets.

  Returns:
    ds_packages: The dataset packages found in the directory (sorted for
      determinism).

  Raises:
    FileNotFoundError: If the path cannot be reached.
  """
  if not path.exists():
    # Should be fault-tolerant in the future
    raise FileNotFoundError(f'Could not find datasets at {path}')

  all_packages = []
  for ds_path in path.iterdir():
    source = get_dataset_source(ds_path)
    if source:
      pkg = DatasetPackage(
          name=utils.DatasetName(namespace=namespace, name=ds_path.name),
          source=source,
      )
      all_packages.append(pkg)

  return all_packages


def get_dataset_source(
    ds_path: epath.Path,) -> Optional[dataset_sources_lib.DatasetSource]:
  """Returns a `DatasetSource` instance if the given path corresponds to a dataset.

  To determine whether the given path contains a dataset, a simple heuristic is
  used that checks whether the path has the following structure:

  ```
  <ds_name>/
      <ds_name>.py
  ```

  If so, all `.py`, `.txt`, `.tsv`, `.json` files will be added to the package.

  Args:
    ds_path: Path of the dataset module

  Returns:
    A `DatasetSource` instance if the path matches the expected file structure.
  """
  filter_list = {'__init__.py'}
  suffixes_list = ('.txt', '.tsv', '.py', '.json')

  def is_interesting_file(fname: str) -> bool:
    return fname.endswith(suffixes_list) and fname not in filter_list

  if not ds_path.is_dir():
    return None
  all_filenames = set(f.name for f in ds_path.iterdir())
  if f'{ds_path.name}.py' not in all_filenames:
    return None

  return dataset_sources_lib.DatasetSource(
      root_path=ds_path,
      filenames=sorted(
          [fname for fname in all_filenames if is_interesting_file(fname)]),
  )


def _download_or_reuse_cache(
    name: utils.DatasetName,
    package_index: _PackageIndex,
) -> _InstalledPackage:
  """Downloads the dataset generation source code.

  Search the dataset in the cache, or download it from the package index
  otherwise.

  Args:
    name: Dataset name to load.
    package_index: Index of all community datasets. Might be updated.

  Returns:
    The installed dataset information.

  Raises:
    DatasetNotFoundError: If the dataset can't be loaded.
  """
  # Dataset can be:
  # * Installed locally (in the cache) -> reuse
  # * Not installed but present in the package index -> install
  # * Not present in the package index -> raise error

  # Check if the file is already downloaded/cached
  # TODO(tfds): To force a download even if file already present, we
  # should add a `ignore_cache=True` option in `tfds.load`. Or should always
  # try to download the file ?
  last_installed_version = _get_last_installed_version(name)
  if last_installed_version:
    return last_installed_version

  # If file isn't cached yet, we need to download it.
  # First need to find it's location.
  if name not in package_index:
    # If not, we need to update the package index cache
    package_index.refresh()
  # If the dataset is present in the package index cache, use this
  package = package_index.get(name)
  if not package:
    # If still not found, raise an DatasetNotFoundError
    raise registered.DatasetNotFoundError(
        f'Could not find dataset {name}: Dataset not found among the '
        f'{len(package_index)} datasets of the community index.')

  # If package was found, download it.
  installed_package = _download_and_cache(package)
  return installed_package


def _get_last_installed_version(
    name: utils.DatasetName,) -> Optional[_InstalledPackage]:
  """Checks whether the datasets is installed locally and returns it."""
  root_dir = (
      cache.module_path() / _IMPORT_MODULE_NAME / name.namespace / name.name)
  if not root_dir.exists():  # Dataset not found
    return None

  all_installed_package_metadatas = [
      package / _METADATA_FILENAME for package in root_dir.iterdir()
  ]
  all_installed_packages = [
      _InstalledPackage.from_json(json.loads(metadata.read_text()))
      for metadata in all_installed_package_metadatas
      if metadata.exists()
  ]
  all_installed_packages = sorted(
      all_installed_packages, key=lambda p: p.instalation_date)

  if not all_installed_packages:  # No valid package found
    return None
  else:
    return all_installed_packages[-1]  # Most recently installed package


def _download_and_cache(package: DatasetPackage) -> _InstalledPackage:
  """Downloads and installs locally the dataset source.

  This function install the dataset package in:
  `<module_path>/<namespace>/<ds_name>/<hash>/...`.

  Args:
    package: Package to install.

  Returns:
    installed_dataset: The installed dataset package.
  """
  tmp_dir = epath.Path(tempfile.mkdtemp())
  try:
    # Download the package in a tmp directory
    dataset_sources_lib.download_from_source(
        package.source,
        tmp_dir,
    )

    # Compute the package hash (to install the dataset in a unique dir)
    package_hash = _compute_dir_hash(tmp_dir)

    # Add package metadata
    installed_package = _InstalledPackage(
        package=package,
        instalation_date=datetime.datetime.now(),
        hash=package_hash,
    )
    package_metadata = json.dumps(installed_package.to_json())
    (tmp_dir / _METADATA_FILENAME).write_text(package_metadata)

    # Rename the package to it's final destination
    installation_path = installed_package.installation_path
    if installation_path.exists():  # Package already exists (with same hash)
      # In the future, we should be smarter to allow overwrite.
      raise ValueError(
          f'Package {package} already installed in {installation_path}.')
    installation_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_dir.rename(installation_path)
  finally:
    # Cleanup the tmp directory if it still exists.
    if tmp_dir.exists():
      tmp_dir.rmtree()

  return installed_package


def _compute_dir_hash(path: epath.Path) -> str:
  """Computes the checksums of the given directory deterministically."""
  all_files = sorted(path.iterdir())

  if any(f.is_dir() for f in all_files):
    raise ValueError('Installed package should only contains files.')

  # Concatenate the filenames and files content to create the directory hash
  all_checksums = [f.name for f in all_files]
  all_checksums += [checksums.compute_url_info(f).checksum for f in all_files]
  return hashlib.sha256(''.join(all_checksums).encode()).hexdigest()
