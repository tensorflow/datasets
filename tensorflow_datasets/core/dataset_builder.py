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

"""DatasetBuilder base class."""

from __future__ import annotations

import abc
import collections
from collections.abc import Iterable, Iterator, Mapping, Sequence
import dataclasses
import functools
import inspect
import json
import os
import sys
from typing import Any, ClassVar, Type

from absl import logging
from etils import epy
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf
from tensorflow_datasets.core.utils.lazy_imports_utils import tree

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  from etils import epath
  import importlib_resources
  import termcolor

  from tensorflow_datasets.core import constants
  from tensorflow_datasets.core import dataset_info
  from tensorflow_datasets.core import dataset_metadata
  from tensorflow_datasets.core import decode
  from tensorflow_datasets.core import download
  from tensorflow_datasets.core import file_adapters
  from tensorflow_datasets.core import lazy_imports_lib
  from tensorflow_datasets.core import logging as tfds_logging
  from tensorflow_datasets.core import naming
  from tensorflow_datasets.core import reader as reader_lib
  from tensorflow_datasets.core import registered
  from tensorflow_datasets.core import split_builder as split_builder_lib
  from tensorflow_datasets.core import splits as splits_lib
  from tensorflow_datasets.core import tf_compat
  from tensorflow_datasets.core import units
  from tensorflow_datasets.core import utils
  from tensorflow_datasets.core import writer as writer_lib
  from tensorflow_datasets.core.data_sources import array_record
  from tensorflow_datasets.core.data_sources import parquet
  from tensorflow_datasets.core.proto import dataset_info_pb2
  from tensorflow_datasets.core.utils import file_utils
  from tensorflow_datasets.core.utils import gcs_utils
  from tensorflow_datasets.core.utils import read_config as read_config_lib
  from tensorflow_datasets.core.utils import type_utils
  # pylint: enable=g-import-not-at-top

ListOrTreeOrElem = type_utils.ListOrTreeOrElem
Tree = type_utils.Tree
TreeDict = type_utils.TreeDict
VersionOrStr = utils.Version | str

FORCE_REDOWNLOAD = download.GenerateMode.FORCE_REDOWNLOAD
REUSE_CACHE_IF_EXISTS = download.GenerateMode.REUSE_CACHE_IF_EXISTS
REUSE_DATASET_IF_EXISTS = download.GenerateMode.REUSE_DATASET_IF_EXISTS
UPDATE_DATASET_INFO = download.GenerateMode.UPDATE_DATASET_INFO

GCS_HOSTED_MSG = """\
Dataset %s is hosted on GCS. It will automatically be downloaded to your
local data directory. If you'd instead prefer to read directly from our public
GCS bucket (recommended if you're running on GCP), you can instead pass
`try_gcs=True` to `tfds.load` or set `data_dir=gs://tfds-data/datasets`.
"""


@dataclasses.dataclass(eq=False)
class BuilderConfig:
  """Base class for `DatasetBuilder` data configuration.

  DatasetBuilder subclasses with data configuration options should subclass
  `BuilderConfig` and add their own properties.

  Attributes:
    name: The name of the config.
    version: The version of the config.
    release_notes: A dictionary associating versions to changes.
    supported_versions: A list of versions which this Builder Config supports.
    description: a human description of the config.
    tags: [Experimental] a list of freeform tags applying to the config. This is
      not used by TFDS, but can be retrieved later from a ConfigBuilder
      instance.
  """

  # TODO(py3.10): Should update dataclass to be:
  # * Frozen (https://bugs.python.org/issue32953)
  # * Kwargs-only (https://bugs.python.org/issue33129)

  name: str
  version: VersionOrStr | None = None
  release_notes: dict[str, str] | None = None
  supported_versions: list[VersionOrStr] = dataclasses.field(
      default_factory=list
  )
  description: str | None = None
  tags: list[str] = dataclasses.field(default_factory=list)

  @classmethod
  def from_dataset_info(
      cls,
      info_proto: dataset_info_pb2.DatasetInfo,
  ) -> BuilderConfig | None:
    """Instantiates a BuilderConfig from the given proto.

    Args:
      info_proto: DatasetInfo proto which documents the requested dataset
        config, including its name, version, and features.

    Returns:
      A BuilderConfig for the requested config.
    """
    if not info_proto.config_name:
      return None
    return BuilderConfig(
        name=info_proto.config_name,
        description=info_proto.config_description,
        version=info_proto.version,
        release_notes=info_proto.release_notes or {},
        tags=info_proto.config_tags or [],
    )


def _get_builder_datadir_path(builder_cls: Type[Any]) -> epath.Path:
  """Returns the path to ConfigBuilder data dir.

  Args:
    builder_cls: a Builder class.

  Returns:
    The path to directory where the config data files of `builders_cls` can be
    read from. e.g. "/usr/lib/[...]/tensorflow_datasets/datasets/foo".
  """
  pkg_names = builder_cls.__module__.split(".")
  # -1 to remove the xxx.py python file.
  return epath.resource_path(pkg_names[0]).joinpath(*pkg_names[1:-1])


class DatasetBuilder(registered.RegisteredDataset):
  """Abstract base class for all datasets.

  `DatasetBuilder` has 3 key methods:

    * `DatasetBuilder.info`: documents the dataset, including feature
      names, types, and shapes, version, splits, citation, etc.
    * `DatasetBuilder.download_and_prepare`: downloads the source data
      and writes it to disk.
    * `DatasetBuilder.as_dataset`: builds an input pipeline using
      `tf.data.Dataset`s.

  **Configuration**: Some `DatasetBuilder`s expose multiple variants of the
  dataset by defining a `tfds.core.BuilderConfig` subclass and accepting a
  config object (or name) on construction. Configurable datasets expose a
  pre-defined set of configurations in `DatasetBuilder.builder_configs`.

  Typical `DatasetBuilder` usage:

  ```python
  mnist_builder = tfds.builder("mnist")
  mnist_info = mnist_builder.info
  mnist_builder.download_and_prepare()
  datasets = mnist_builder.as_dataset()

  train_dataset, test_dataset = datasets["train"], datasets["test"]
  assert isinstance(train_dataset, tf.data.Dataset)

  # And then the rest of your input pipeline
  train_dataset = train_dataset.repeat().shuffle(1024).batch(128)
  train_dataset = train_dataset.prefetch(2)
  features = tf.compat.v1.data.make_one_shot_iterator(train_dataset).get_next()
  image, label = features['image'], features['label']
  ```
  """

  # Semantic version of the dataset (ex: tfds.core.Version('1.2.0'))
  VERSION: utils.Version | None = None

  # Release notes
  # Metadata only used for documentation. Should be a dict[version,description]
  # Multi-lines are automatically dedent
  RELEASE_NOTES: ClassVar[dict[str, str]] = {}

  # List dataset versions which can be loaded using current code.
  # Data can only be prepared with canonical VERSION or above.
  SUPPORTED_VERSIONS: list[utils.Version] = []

  # Named configurations that modify the data generated by download_and_prepare.
  BUILDER_CONFIGS = []

  # Name of the builder config that should be used in case the user doesn't
  # specify a config when loading a dataset. If None, then the first config in
  # `BUILDER_CONFIGS` is used.
  DEFAULT_BUILDER_CONFIG_NAME: str | None = None

  # Must be set for datasets that use 'manual_dir' functionality - the ones
  # that require users to do additional steps to download the data
  # (this is usually due to some external regulations / rules).
  #
  # This field should contain a string with user instructions, including
  # the list of files that should be present. It will be
  # displayed in the dataset documentation.
  MANUAL_DOWNLOAD_INSTRUCTIONS = None

  # Optional max number of simultaneous downloads. Setting this value will
  # override download config settings if necessary.
  MAX_SIMULTANEOUS_DOWNLOADS: int | None = None

  # If not set, pkg_dir_path is inferred. However, if user of class knows better
  # then this can be set directly before init, to avoid heuristic inferences.
  # Example: `imported_builder_cls` function in `registered.py` module sets it.
  pkg_dir_path: epath.Path | None = None

  # Holds information on versions and configs that should not be used.
  BLOCKED_VERSIONS: ClassVar[utils.BlockedVersions | None] = None

  @classmethod
  def _get_pkg_dir_path(cls) -> epath.Path:
    """Returns class pkg_dir_path, infer it first if not set."""
    # We use cls.__dict__.get to check whether `pkg_dir_path` attribute has been
    # set on the class, and not on a parent class. If we were accessing the
    # attribute directly, a dataset Builder inheriting from another would read
    # its metadata from its parent directory (which would be wrong).
    if cls.pkg_dir_path is None:
      cls.pkg_dir_path = _get_builder_datadir_path(cls)
    return cls.pkg_dir_path

  @classmethod
  def get_metadata(cls) -> dataset_metadata.DatasetMetadata:
    """Returns metadata (README, CITATIONS, ...) specified in config files.

    The config files are read from the same package where the DatasetBuilder has
    been defined, so those metadata might be wrong for legacy builders.
    """
    return dataset_metadata.load(cls._get_pkg_dir_path())

  @tfds_logging.builder_init()
  def __init__(
      self,
      *,
      data_dir: epath.PathLike | None = None,
      config: None | str | BuilderConfig = None,
      version: None | str | utils.Version = None,
  ):
    """Constructs a DatasetBuilder.

    Callers must pass arguments as keyword arguments.

    Args:
      data_dir: directory to read/write data. Defaults to the value of the
        environment variable TFDS_DATA_DIR, if set, otherwise falls back to
        "~/tensorflow_datasets".
      config: `tfds.core.BuilderConfig` or `str` name, optional configuration
        for the dataset that affects the data generated on disk. Different
        `builder_config`s will have their own subdirectories and versions.
      version: Optional version at which to load the dataset. An error is raised
        if specified version cannot be satisfied. Eg: '1.2.3', '1.2.*'. The
        special value "experimental_latest" will use the highest version, even
        if not default. This is not recommended unless you know what you are
        doing, as the version could be broken.
    """  # fmt: skip
    if data_dir:
      data_dir = os.fspath(data_dir)  # Pathlib -> str
    # For pickling:
    self._original_state = dict(
        data_dir=data_dir, config=config, version=version
    )
    # To do the work:
    self._builder_config = self._create_builder_config(config, version=version)
    # Extract code version (VERSION or config)
    self._version = self._pick_version(version)
    # Compute the base directory (for download) and dataset/version directory.
    self._data_dir_root, self._data_dir = self._build_data_dir(data_dir)
    # If the dataset info is available, use it.
    if dataset_info.dataset_info_path(self.data_path).exists():
      self.info.read_from_directory(self._data_dir)
    else:  # Use the code version (do not restore data)
      self.info.initialize_from_bucket()
    if self.BLOCKED_VERSIONS is not None:
      if is_blocked := self.BLOCKED_VERSIONS.is_blocked(
          version=self._version, config=self.builder_config_name
      ):
        default_msg = (
            f"Dataset {self.name} is blocked at version {self._version} and"
            f" config {self.builder_config_name}."
        )
        self.info.set_is_blocked(
            is_blocked.blocked_msg if is_blocked.blocked_msg else default_msg
        )

  @utils.classproperty
  @classmethod
  @utils.memoize()
  def code_path(cls) -> epath.Path | None:
    """Returns the path to the file where the Dataset class is located.

    Note: As the code can be run inside zip file. The returned value is
    a `Path` by default. Use `tfds.core.utils.to_write_path()` to cast
    the path into `Path`.

    Returns:
      path: pathlib.Path like abstraction
    """
    modules = cls.__module__.split(".")
    if len(modules) >= 2:  # Filter `__main__`, `python my_dataset.py`,...
      # If the dataset can be loaded from a module, use this to support zipapp.
      # Note: `utils.resource_path` will return either `zipfile.Path` (for
      # zipapp) or `pathlib.Path`.
      try:
        path = epath.resource_path(modules[0])
      except TypeError:  # Module is not a package
        pass
      else:
        # For dynamically added modules, `importlib.resources` returns
        # `pathlib.Path('.')` rather than the real path, so filter those by
        # checking for `parts`.
        # Check for `zipfile.Path` (`ResourcePath`) or
        # `importlib_resources.abc.Traversable` (e.g. `MultiplexedPath`) as they
        # do not have `.parts`.
        if (
            isinstance(path, epath.resource_utils.ResourcePath)
            or isinstance(path, importlib_resources.abc.Traversable)
            or path.parts
        ):
          modules[-1] += ".py"
          return path.joinpath(*modules[1:])
    # Otherwise, fallback to `pathlib.Path`. For non-zipapp, it should be
    # equivalent to the above return.
    try:
      filepath = inspect.getfile(cls)
    except (TypeError, OSError):  # Module is not a package
      # Could happen when the class is defined in Colab.
      return None
    else:
      return epath.Path(filepath)

  def __getstate__(self):
    # This needs to be of the same format as __dict__,
    # to match with the pickling implementation of the derived classes.
    return dict(_original_state=self._original_state)

  def __setstate__(self, state):
    original_state = state["_original_state"]
    self.__init__(**original_state)

  @functools.cached_property
  def canonical_version(self) -> utils.Version:
    return canonical_version_for_config(self, self._builder_config)

  @functools.cached_property
  def supported_versions(self):
    if self._builder_config and self._builder_config.supported_versions:
      return self._builder_config.supported_versions
    else:
      return self.SUPPORTED_VERSIONS

  @functools.cached_property
  def versions(self) -> list[utils.Version]:
    """Versions (canonical + availables), in preference order."""
    return [
        utils.Version(v) if isinstance(v, str) else v
        for v in [self.canonical_version] + self.supported_versions
    ]

  def _pick_version(
      self, requested_version: str | utils.Version | None
  ) -> utils.Version:
    """Returns utils.Version instance, or raise AssertionError."""
    # Validate that `canonical_version` is correctly defined
    assert self.canonical_version
    # If requested_version is of type utils.Version, convert to its string
    # representation. This is necessary to properly execute the equality check
    # with "experimental_latest".
    if isinstance(requested_version, utils.Version):
      requested_version = str(requested_version)
    if requested_version == "experimental_latest":
      return max(self.versions)
    for version in self.versions:
      if requested_version is None or version.match(requested_version):
        return version
    available_versions = [str(v) for v in self.versions]
    msg = "Dataset {} cannot be loaded at version {}, only: {}.".format(
        self.name, requested_version, ", ".join(available_versions)
    )
    raise AssertionError(msg)

  @property
  def version(self) -> utils.Version:
    return self._version

  @property
  def release_notes(self) -> dict[str, str]:
    if self.builder_config and self.builder_config.release_notes:
      return self.builder_config.release_notes
    else:
      return self.RELEASE_NOTES

  @property
  def blocked_versions(self) -> utils.BlockedVersions | None:
    return self.BLOCKED_VERSIONS

  @property
  def data_dir_root(self) -> epath.Path:
    """Returns the root directory where all TFDS datasets are stored.

    Note that this is different from `data_dir`, which includes the dataset
    name, config, and version. For example, if `data_dir` is
    `/data/tfds/my_dataset/my_config/1.2.3`, then `data_dir_root` is
    `/data/tfds`.

    Returns:
      the root directory where all TFDS datasets are stored.
    """
    return epath.Path(self._data_dir_root)

  @property
  def data_dir(self) -> str:
    """Returns the directory where this version + config is stored.

    Note that this is different from `data_dir_root`. For example, if
    `data_dir_root` is `/data/tfds`, then `data_dir` would be
    `/data/tfds/my_dataset/my_config/1.2.3`.

    Returns:
      the directory where this version + config is stored.
    """
    return self._data_dir

  @property
  def data_path(self) -> epath.Path:
    """Returns the path where this version + config is stored."""
    # Instead, should make `_data_dir` be Path everywhere
    return epath.Path(self.data_dir)

  @utils.classproperty
  @classmethod
  def _checksums_path(cls) -> epath.Path | None:
    """Returns the checksums path."""
    # Used:
    # * To load the checksums (in url_infos)
    # * To save the checksums (in DownloadManager)
    if not cls.code_path:
      return None
    new_path = cls.code_path.parent / constants.CHECKSUMS_FILENAME
    # Checksums of legacy datasets are located in a separate dir.
    legacy_path = utils.tfds_path() / "url_checksums" / f"{cls.name}.txt"
    if (
        # zipfile.Path does not have `.parts`. Additionally, `os.fspath`
        # will extract the file, so use `str`.
        "tensorflow_datasets" in str(new_path)
        and legacy_path.exists()
        and not new_path.exists()
    ):
      return legacy_path
    else:
      return new_path

  @utils.classproperty
  @classmethod
  @functools.lru_cache(maxsize=None)
  def url_infos(cls) -> dict[str, download.checksums.UrlInfo] | None:
    """Load `UrlInfo` from the given path."""
    # Note: If the dataset is downloaded with `record_checksums=True`, urls
    # might be updated but `url_infos` won't as it is memoized.

    # Search for the url_info file.
    checksums_path = cls._checksums_path
    # If url_info file is found, load the urls
    if checksums_path and checksums_path.exists():
      return download.checksums.load_url_infos(checksums_path)
    else:
      return None

  @property
  @tfds_logging.builder_info()
  # Warning: This unbounded cache is required for correctness. See b/238762111.
  @functools.lru_cache(maxsize=None)
  def info(self) -> dataset_info.DatasetInfo:
    """`tfds.core.DatasetInfo` for this builder."""
    # Ensure .info hasn't been called before versioning is set-up
    # Otherwise, backward compatibility cannot be guaranteed as some code will
    # depend on the code version instead of the restored data version
    if not getattr(self, "_version", None):
      # Message for developers creating new dataset. Will trigger if they are
      # using .info in the constructor before calling super().__init__
      raise AssertionError(
          "Info should not been called before version has been defined. "
          "Otherwise, the created .info may not match the info version from "
          "the restored dataset."
      )
    info = self._info()
    if not isinstance(info, dataset_info.DatasetInfo):
      raise TypeError(
          "DatasetBuilder._info should returns `tfds.core.DatasetInfo`, not "
          f" {type(info)}."
      )
    return info

  @utils.classproperty
  @classmethod
  def default_builder_config(cls) -> BuilderConfig | None:
    return _get_default_config(
        builder_configs=cls.BUILDER_CONFIGS,
        default_config_name=cls.DEFAULT_BUILDER_CONFIG_NAME,
    )

  def get_default_builder_config(self) -> BuilderConfig | None:
    """Returns the default builder config if there is one.

    Note that for dataset builders that cannot use the `cls.BUILDER_CONFIGS`, we
    need a method that uses the instance to get `BUILDER_CONFIGS` and
    `DEFAULT_BUILDER_CONFIG_NAME`.

    Returns:
      the default builder config if there is one
    """
    return _get_default_config(
        builder_configs=self.BUILDER_CONFIGS,
        default_config_name=self.DEFAULT_BUILDER_CONFIG_NAME,
    )

  def get_reference(
      self,
      namespace: str | None = None,
  ) -> naming.DatasetReference:
    """Returns a reference to the dataset produced by this dataset builder.

    Includes the config if specified, the version, and the data_dir that should
    contain this dataset.

    Arguments:
      namespace: if this dataset is a community dataset, and therefore has a
        namespace, then the namespace must be provided such that it can be set
        in the reference. Note that a dataset builder is not aware that it is
        part of a namespace.

    Returns:
      a reference to this instantiated builder.
    """
    return naming.DatasetReference(
        dataset_name=self.name,
        namespace=namespace,
        config=self.builder_config_name,
        version=self.version,
        data_dir=self.data_dir_root,
    )

  def get_file_spec(self, split: str) -> str:
    """Returns the file spec of the split."""
    split_info: splits_lib.SplitInfo = self.info.splits[split]
    return split_info.file_spec(self.info.file_format)

  def is_prepared(self) -> bool:
    """Returns whether this dataset is already downloaded and prepared."""
    return self.data_path.exists()

  def is_blocked(self) -> utils.IsBlocked:
    """Returns whether this builder (version, config) is blocked."""
    if blocked_versions := self.blocked_versions:
      return blocked_versions.is_blocked(
          version=self.version, config=self.builder_config_name
      )
    return utils.IsBlocked(False)

  def assert_is_not_blocked(self) -> None:
    """Checks that the dataset is not blocked."""
    if blocked_versions := self.blocked_versions:
      is_blocked = blocked_versions.is_blocked(
          version=self.version, config=self.builder_config_name
      )
      if is_blocked.result:
        raise utils.DatasetVariantBlockedError(is_blocked.blocked_msg)

  @tfds_logging.download_and_prepare()
  def download_and_prepare(
      self,
      *,
      download_dir: epath.PathLike | None = None,
      download_config: download.DownloadConfig | None = None,
      file_format: str | file_adapters.FileFormat | None = None,
      permissions: file_utils.Permissions = file_utils.Permissions(mode=0o775),
  ) -> None:
    """Downloads and prepares dataset for reading.

    Args:
      download_dir: directory where downloaded files are stored. Defaults to
        "~/tensorflow-datasets/downloads".
      download_config: `tfds.download.DownloadConfig`, further configuration for
        downloading and preparing dataset.
      file_format: optional `str` or `file_adapters.FileFormat`, format of the
        record files in which the dataset will be written.
      permissions: permissions to set on the generated folder and files.
        Defaults to 0o775 instead of gFile's default 0o750.

    Raises:
      IOError: if there is not enough disk space available.
      RuntimeError: when the config cannot be found.
      DatasetBlockedError: if the given version, or combination of version and
        config, has been marked as blocked in the builder's BLOCKED_VERSIONS.
    """
    self.assert_is_not_blocked()


    download_config = download_config or download.DownloadConfig()
    data_path = self.data_path
    data_exists = data_path.exists()

    if download_config.download_mode == UPDATE_DATASET_INFO:
      self._update_dataset_info()
      return

    if data_exists:
      if download_config.download_mode.overwrite_dataset:
        logging.info(
            "Deleting pre-existing dataset %s (%s)", self.name, self.data_dir
        )
        data_path.rmtree()  # Delete pre-existing data.
        data_exists = data_path.exists()
      else:
        logging.info("Reusing dataset %s (%s)", self.name, self.data_dir)
        return

    if self.version.tfds_version_to_prepare:
      available_to_prepare = ", ".join(
          str(v) for v in self.versions if not v.tfds_version_to_prepare
      )
      raise AssertionError(
          "The version of the dataset you are trying to use ({}:{}) can only "
          "be generated using TFDS code synced @ {} or earlier. Either sync to "
          "that version of TFDS to first prepare the data or use another "
          "version of the dataset (available for `download_and_prepare`: "
          "{}).".format(
              self.name,
              self.version,
              self.version.tfds_version_to_prepare,
              available_to_prepare,
          )
      )

    # Only `cls.VERSION` or `experimental_latest` versions can be generated.
    # Otherwise, users may accidentally generate an old version using the
    # code from newer versions.
    installable_versions = {
        str(v) for v in (self.canonical_version, max(self.versions))
    }
    if str(self.version) not in installable_versions:
      msg = (
          "The version of the dataset you are trying to use ({}) is too "
          "old for this version of TFDS so cannot be generated."
      ).format(self.info.full_name)
      if self.version.tfds_version_to_prepare:
        msg += (
            "{} can only be generated using TFDS code synced @ {} or earlier "
            "Either sync to that version of TFDS to first prepare the data or "
            "use another version of the dataset. "
        ).format(self.version, self.version.tfds_version_to_prepare)
      else:
        msg += (
            "Either sync to a previous version of TFDS to first prepare the "
            "data or use another version of the dataset. "
        )
      msg += "Available for `download_and_prepare`: {}".format(
          list(sorted(installable_versions))
      )
      raise ValueError(msg)

    # Currently it's not possible to overwrite the data because it would
    # conflict with versioning: If the last version has already been generated,
    # it will always be reloaded and data_dir will be set at construction.
    if data_exists:
      raise ValueError(
          "Trying to overwrite an existing dataset {} at {}. A dataset with "
          "the same version {} already exists. If the dataset has changed, "
          "please update the version number.".format(
              self.name, self.data_dir, self.version
          )
      )

    logging.info("Generating dataset %s (%s)", self.name, self.data_dir)
    if not utils.has_sufficient_disk_space(
        self.info.dataset_size + self.info.download_size,
        directory=os.fspath(self.data_dir_root),
    ):
      raise IOError(
          "Not enough disk space. Needed: {} (download: {}, generated: {})"
          .format(
              self.info.dataset_size + self.info.download_size,
              self.info.download_size,
              self.info.dataset_size,
          )
      )
    self._log_download_bytes()

    dl_manager = self._make_download_manager(
        download_dir=download_dir,
        download_config=download_config,
    )

    # Maybe save the `builder_cls` metadata common to all builder configs.
    if self.BUILDER_CONFIGS:
      default_builder_config = self.get_default_builder_config()
      if default_builder_config is None:
        raise RuntimeError(
            "Could not find default builder config while there "
            "are builder configs!"
        )
      _save_default_config_name(
          # `data_dir/ds_name/config/version/` -> `data_dir/ds_name/`
          common_dir=self.data_path.parent.parent,
          default_config_name=default_builder_config.name,
      )

    # If the file format was specified, set it in the info such that it is used
    # to generate the files.
    if file_format:
      self.info.set_file_format(file_format, override=True)

    # Create a tmp dir and rename to self.data_dir on successful exit.
    with utils.incomplete_dir(
        dirname=self.data_dir,
        permissions=permissions,
        overwrite=download_config.download_mode.overwrite_dataset,
    ) as tmp_data_dir:
      # Temporarily assign _data_dir to tmp_data_dir to avoid having to forward
      # it to every sub function.
      with utils.temporary_assignment(self, "_data_dir", tmp_data_dir):
        if (
            download_config.try_download_gcs
            and gcs_utils.is_dataset_on_gcs(self.info.full_name)
            and self.info.file_format == file_adapters.FileFormat.TFRECORD
        ):
          logging.info(GCS_HOSTED_MSG, self.name)
          gcs_utils.download_gcs_dataset(
              dataset_name=self.info.full_name, local_dataset_dir=self.data_dir
          )
          self.info.read_from_directory(self.data_dir)
        else:
          self._download_and_prepare(
              dl_manager=dl_manager,
              download_config=download_config,
          )

          # NOTE: If modifying the lines below to put additional information in
          # DatasetInfo, you'll likely also want to update
          # DatasetInfo.read_from_directory to possibly restore these attributes
          # when reading from package data.
          self.info.download_size = dl_manager.downloaded_size
          # Write DatasetInfo to disk, even if we haven't computed statistics.
          self.info.write_to_directory(self.data_dir)
      # The generated DatasetInfo contains references to `tmp_data_dir`
      self.info.update_data_dir(self.data_dir)

    # Clean up incomplete files from preempted workers.
    deleted_incomplete_files = []
    for f in self.data_path.glob(f"*{constants.INCOMPLETE_PREFIX}*"):
      if utils.is_incomplete_file(f):
        deleted_incomplete_files.append(os.fspath(f))
        f.unlink()
    if deleted_incomplete_files:
      logging.info(
          "Deleted %d incomplete files. A small selection: %s",
          len(deleted_incomplete_files),
          "\n".join(deleted_incomplete_files[:3]),
      )

    self._log_download_done()

    # Execute post download and prepare hook if it exists.
    self._post_download_and_prepare_hook()


  def _post_download_and_prepare_hook(self) -> None:
    """Hook to be executed after download and prepare.

    Override this in custom dataset builders to execute custom logic after
    download and prepare.
    """
    pass

  def _update_dataset_info(self) -> None:
    """Updates the `dataset_info.json` file in the dataset dir."""
    info_file = self.data_path / constants.DATASET_INFO_FILENAME
    if not info_file.exists():
      raise AssertionError(f"To update {info_file}, it must already exist.")
    new_info = self.info
    new_info.read_from_directory(self.data_path)
    new_info.write_to_directory(self.data_path, all_metadata=False)

  @tfds_logging.as_data_source()
  def as_data_source(
      self,
      split: Tree[splits_lib.SplitArg] | None = None,
      *,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None = None,
      deserialize_method: decode.DeserializeMethod = decode.DeserializeMethod.DESERIALIZE_AND_DECODE,
  ) -> ListOrTreeOrElem[Sequence[Any]]:
    """Constructs an `ArrayRecordDataSource`.

    Args:
      split: Which split of the data to load (e.g. `'train'`, `'test'`,
        `['train', 'test']`, `'train[80%:]'`,...). See our [split API
        guide](https://www.tensorflow.org/datasets/splits). If `None`, will
        return all splits in a `dict[Split, Sequence]`.
      decoders: Nested dict of `Decoder` objects which allow to customize the
        decoding. The structure should match the feature structure, but only
        customized feature keys need to be present. See [the
        guide](https://github.com/tensorflow/datasets/blob/master/docs/decode.md)
        for more info.
      deserialize_method: Whether the read examples should be deserialized
        and/or decoded. If not specified, it'll deserialize the data and decode
        the features. Decoding is only supported if the examples are tf
        examples. Note that if the deserialize_method method is other than
        PARSE_AND_DECODE, then the `decoders` argument is ignored.

    Returns:
      `Sequence` if `split`,
      `dict<key: tfds.Split, value: Sequence>` otherwise.

    Raises:
      NotImplementedError if the data was not generated using ArrayRecords.
    """
    self.assert_is_not_blocked()

    # By default, return all splits
    if split is None:
      split = {s: s for s in self.info.splits}

    info = self.info

    random_access_formats = file_adapters.FileFormat.with_random_access()
    random_access_formats_msg = " or ".join(
        [f.value for f in random_access_formats]
    )
    unsupported_format_msg = (
        f"Random access data source for file format {info.file_format} is not"
        " supported. Possible root causes:\n\t* You have to run"
        " download_and_prepare with"
        f" file_format={random_access_formats_msg}.\n\t* The dataset is already"
        f" prepared at {self.data_dir} in the {info.file_format} format. Either"
        " choose another data_dir or delete the data."
    )

    available_formats = info.available_file_formats()
    if not available_formats:
      raise ValueError(
          "Dataset info file format is not set! For random access, one of the"
          f" following formats is required: {random_access_formats_msg}"
      )

    suitable_formats = available_formats.intersection(random_access_formats)
    if suitable_formats:
      chosen_format = suitable_formats.pop()
      logging.info(
          "Found random access formats: %s. Chose to use %s. Overriding file"
          " format in the dataset info.",
          ", ".join([f.name for f in suitable_formats]),
          chosen_format,
      )
      # Change the dataset info to read from a random access format.
      info.set_file_format(
          chosen_format, override=True, override_if_initialized=True
      )
    else:
      raise NotImplementedError(unsupported_format_msg)

    # Create a dataset for each of the given splits
    def build_single_data_source(split: str) -> Sequence[Any]:
      if info.file_format is None:
        raise ValueError(
            "Dataset info file format is not set! For random access, one of the"
            f" following formats is required: {random_access_formats_msg}"
        )

      match info.file_format:
        case file_adapters.FileFormat.ARRAY_RECORD:
          return array_record.ArrayRecordDataSource(
              info,
              split=split,
              decoders=decoders,
              deserialize_method=deserialize_method,
          )
        case file_adapters.FileFormat.PARQUET:
          return parquet.ParquetDataSource(
              info,
              split=split,
              decoders=decoders,
              deserialize_method=deserialize_method,
          )
        case _:
          raise NotImplementedError(unsupported_format_msg)

    all_ds = tree.map_structure(build_single_data_source, split)
    return all_ds

  @tfds_logging.as_dataset()
  def as_dataset(
      self,
      split: Tree[splits_lib.SplitArg] | None = None,
      *,
      batch_size: int | None = None,
      shuffle_files: bool = False,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None = None,
      read_config: read_config_lib.ReadConfig | None = None,
      as_supervised: bool = False,
  ):
    # pylint: disable=line-too-long
    """Constructs a `tf.data.Dataset`.

    Callers must pass arguments as keyword arguments.

    The output types vary depending on the parameters. Examples:

    ```python
    builder = tfds.builder('imdb_reviews')
    builder.download_and_prepare()

    # Default parameters: Returns the dict of tf.data.Dataset
    ds_all_dict = builder.as_dataset()
    assert isinstance(ds_all_dict, dict)
    print(ds_all_dict.keys())  # ==> ['test', 'train', 'unsupervised']

    assert isinstance(ds_all_dict['test'], tf.data.Dataset)
    # Each dataset (test, train, unsup.) consists of dictionaries
    # {'label': <tf.Tensor: .. dtype=int64, numpy=1>,
    #  'text': <tf.Tensor: .. dtype=string, numpy=b"I've watched the movie ..">}
    # {'label': <tf.Tensor: .. dtype=int64, numpy=1>,
    #  'text': <tf.Tensor: .. dtype=string, numpy=b'If you love Japanese ..'>}

    # With as_supervised: tf.data.Dataset only contains (feature, label) tuples
    ds_all_supervised = builder.as_dataset(as_supervised=True)
    assert isinstance(ds_all_supervised, dict)
    print(ds_all_supervised.keys())  # ==> ['test', 'train', 'unsupervised']

    assert isinstance(ds_all_supervised['test'], tf.data.Dataset)
    # Each dataset (test, train, unsup.) consists of tuples (text, label)
    # (<tf.Tensor: ... dtype=string, numpy=b"I've watched the movie ..">,
    #  <tf.Tensor: ... dtype=int64, numpy=1>)
    # (<tf.Tensor: ... dtype=string, numpy=b"If you love Japanese ..">,
    #  <tf.Tensor: ... dtype=int64, numpy=1>)

    # Same as above plus requesting a particular split
    ds_test_supervised = builder.as_dataset(as_supervised=True, split='test')
    assert isinstance(ds_test_supervised, tf.data.Dataset)
    # The dataset consists of tuples (text, label)
    # (<tf.Tensor: ... dtype=string, numpy=b"I've watched the movie ..">,
    #  <tf.Tensor: ... dtype=int64, numpy=1>)
    # (<tf.Tensor: ... dtype=string, numpy=b"If you love Japanese ..">,
    #  <tf.Tensor: ... dtype=int64, numpy=1>)
    ```

    Args:
      split: Which split of the data to load (e.g. `'train'`, `'test'`,
        `['train', 'test']`, `'train[80%:]'`,...). See our [split API
        guide](https://www.tensorflow.org/datasets/splits). If `None`, will
        return all splits in a `Dict[Split, tf.data.Dataset]`.
      batch_size: `int`, batch size. Note that variable-length features will be
        0-padded if `batch_size` is set. Users that want more custom behavior
        should use `batch_size=None` and use the `tf.data` API to construct a
        custom pipeline. If `batch_size == -1`, will return feature dictionaries
        of the whole dataset with `tf.Tensor`s instead of a `tf.data.Dataset`.
      shuffle_files: `bool`, whether to shuffle the input files. Defaults to
        `False`.
      decoders: Nested dict of `Decoder` objects which allow to customize the
        decoding. The structure should match the feature structure, but only
        customized feature keys need to be present. See [the
        guide](https://github.com/tensorflow/datasets/blob/master/docs/decode.md)
        for more info.
      read_config: `tfds.ReadConfig`, Additional options to configure the input
        pipeline (e.g. seed, num parallel reads,...).
      as_supervised: `bool`, if `True`, the returned `tf.data.Dataset` will have
        a 2-tuple structure `(input, label)` according to
        `builder.info.supervised_keys`. If `False`, the default, the returned
        `tf.data.Dataset` will have a dictionary with all the features.

    Returns:
      `tf.data.Dataset`, or if `split=None`, `dict<key: tfds.Split, value:
      tf.data.Dataset>`.

      If `batch_size` is -1, will return feature dictionaries containing
      the entire dataset in `tf.Tensor`s instead of a `tf.data.Dataset`.
    """
    self.assert_is_not_blocked()

    # pylint: enable=line-too-long
    if not self.data_path.exists():
      raise AssertionError(
          "Dataset %s: could not find data in %s. Please make sure to call "
          "dataset_builder.download_and_prepare(), or pass download=True to "
          "tfds.load() before trying to access the tf.data.Dataset object."
          % (self.name, self.data_dir_root)
      )

    # By default, return all splits
    if split is None:
      split = {s: s for s in self.info.splits}

    read_config = read_config or read_config_lib.ReadConfig()

    # Create a dataset for each of the given splits
    build_single_dataset = functools.partial(
        self._build_single_dataset,
        shuffle_files=shuffle_files,
        batch_size=batch_size,
        decoders=decoders,
        read_config=read_config,
        as_supervised=as_supervised,
    )
    all_ds = tree.map_structure(build_single_dataset, split)
    return all_ds

  def _build_single_dataset(
      self,
      split: splits_lib.Split,
      batch_size: int | None,
      shuffle_files: bool,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None,
      read_config: read_config_lib.ReadConfig,
      as_supervised: bool,
  ) -> tf.data.Dataset:
    """as_dataset for a single split."""
    wants_full_dataset = batch_size == -1
    if wants_full_dataset:
      batch_size = self.info.splits.total_num_examples or sys.maxsize

    # Build base dataset
    ds = self._as_dataset(
        split=split,
        shuffle_files=shuffle_files,
        decoders=decoders,
        read_config=read_config,
    )
    # Auto-cache small datasets which are small enough to fit in memory.
    if self._should_cache_ds(
        split=split, shuffle_files=shuffle_files, read_config=read_config
    ):
      ds = ds.cache()

    if batch_size:
      # Use padded_batch so that features with unknown shape are supported.
      ds = ds.padded_batch(batch_size, tf.compat.v1.data.get_output_shapes(ds))

    if as_supervised:
      if not self.info.supervised_keys:
        raise ValueError(
            f"as_supervised=True but {self.name} does not support a supervised "
            "structure."
        )

      def lookup_nest(features: dict[str, Any]) -> tuple[Any, ...]:
        """Converts `features` to the structure described by `supervised_keys`.

        Note that there is currently no way to access features in nested
        feature dictionaries.

        Args:
          features: dictionary of features

        Returns:
          A tuple with elements structured according to `supervised_keys`
        """
        return tree.map_structure(
            lambda key: features[key], self.info.supervised_keys
        )

      ds = ds.map(lookup_nest)

    # Add prefetch by default
    if not read_config.skip_prefetch:
      ds = ds.prefetch(tf.data.experimental.AUTOTUNE)

    if wants_full_dataset:
      return tf_compat.get_single_element(ds)
    return ds

  def _should_cache_ds(self, split, shuffle_files, read_config) -> bool:
    """Returns True if TFDS should auto-cache the dataset."""
    # The user can explicitly opt-out from auto-caching
    if not read_config.try_autocache:
      return False

    # Skip datasets with unknown size.
    # Even by using heuristic with `download_size` and
    # `MANUAL_DOWNLOAD_INSTRUCTIONS`, it wouldn't catch datasets which hardcode
    # the non-processed data-dir, nor DatasetBuilder not based on tf-record.
    if not self.info.dataset_size:
      return False

    # Do not cache big datasets
    # Instead of using the global size, we could infer the requested bytes:
    # `self.info.splits[split].num_bytes`
    # The info is available for full splits, and could be approximated
    # for subsplits `train[:50%]`.
    # However if the user is creating multiple small splits from a big
    # dataset, those could adds up and fill up the entire RAM.
    # 250 MiB is arbitrary picked. For comparison, Cifar10 is about 150 MiB.
    if self.info.dataset_size > 250 * units.MiB:
      return False

    # We do not want to cache data which has more than one shards when
    # shuffling is enabled, as this would effectively disable shuffling.
    # An exception is for single shard (as shuffling is a no-op).
    # Another exception is if reshuffle is disabled (shuffling already cached)
    num_shards = self.info.splits[split].num_shards
    if (
        shuffle_files
        and
        # Shuffling only matter when reshuffle is True or None (default)
        read_config.shuffle_reshuffle_each_iteration is not False
        and num_shards > 1  # pylint: disable=g-bool-id-comparison
    ):
      return False

    # If the dataset satisfy all the right conditions, activate autocaching.
    return True

  def _build_data_dir(self, given_data_dir: str | None) -> tuple[str, str]:
    """Return the data directory for the current version.

    Args:
      given_data_dir: Root `data_dir` passed as `__init__` argument.

    Returns:
      data_dir: Root directory containing all datasets, downloads,...
      dataset_dir: Dataset data directory (e.g.
        `<data_dir>/<ds_name>/<config>/<version>`)
    """
    data_dir, dataset_dir = file_utils.get_data_dir_and_dataset_dir(
        given_data_dir=given_data_dir,
        builder_name=self.name,
        config_name=self.builder_config_name,
        version=self.version,
    )
    return os.fspath(data_dir), os.fspath(dataset_dir)

  def _log_download_done(self) -> None:
    msg = (
        f"Dataset {self.name} downloaded and prepared to {self.data_dir}. "
        "Subsequent calls will reuse this data."
    )
    termcolor.cprint(msg, attrs=["bold"])

  def _log_download_bytes(self) -> None:
    # Print is intentional: we want this to always go to stdout so user has
    # information needed to cancel download/preparation if needed.
    # This comes right before the progress bar.
    termcolor.cprint(
        (
            f"Downloading and preparing dataset {self.info.download_size} "
            f"(download: {self.info.download_size}, "
            f"generated: {self.info.dataset_size}, "
            f"total: {self.info.download_size + self.info.dataset_size}) "
            f"to {self.data_dir}..."
        ),
        attrs=["bold"],
    )

  def dataset_info_from_configs(self, **kwargs):
    """Returns the DatasetInfo using given kwargs and config files.

    Sub-class should call this and add information not present in config files
    using kwargs directly passed to tfds.core.DatasetInfo object.

    If information is present both in passed arguments and config files, config
    files will prevail.

    Args:
      **kwargs: kw args to pass to DatasetInfo directly.
    """
    metadata = self.get_metadata()
    if metadata.description:
      kwargs["description"] = metadata.description
    if metadata.citation:
      kwargs["citation"] = metadata.citation
    return dataset_info.DatasetInfo(builder=self, **kwargs)

  @abc.abstractmethod
  @utils.docs.doc_private
  def _info(self) -> dataset_info.DatasetInfo:
    """Returns the `tfds.core.DatasetInfo` object.

    This function is called once and the result is cached for all
    following calls.

    Returns:
      dataset_info: The dataset metadata.
    """
    raise NotImplementedError

  @abc.abstractmethod
  def _download_and_prepare(
      self,
      dl_manager: download.DownloadManager,
      download_config: download.DownloadConfig | None = None,
  ) -> None:
    """Downloads and prepares dataset for reading.

    Internal implementation to overwrite when inheriting from DatasetBuilder.
    Called when `builder.download_and_prepare` is called.
    It should download all required data and generate
    the pre-processed datasets files.

    Args:
      dl_manager: `tfds.download.DownloadManager` used to download and cache
        data.
      download_config: `DownloadConfig`, Additional options.
    """
    raise NotImplementedError

  @abc.abstractmethod
  def _as_dataset(
      self,
      split: splits_lib.Split,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None = None,
      read_config: read_config_lib.ReadConfig | None = None,
      shuffle_files: bool = False,
  ) -> tf.data.Dataset:
    """Constructs a `tf.data.Dataset`.

    Internal implementation to overwrite when inheriting from DatasetBuilder.
    Called when `builder.as_dataset` is called.
    It should read the pre-processed datasets files and generate
    the `tf.data.Dataset` object.

    Args:
      split: `tfds.Split` which subset of the data to read.
      decoders: Nested structure of `Decoder` object to customize the dataset
        decoding.
      read_config: `tfds.ReadConfig`
      shuffle_files: `bool`, whether to shuffle the input files. Optional,
        defaults to `False`.

    Returns:
      `tf.data.Dataset`
    """
    raise NotImplementedError

  def _make_download_manager(
      self,
      download_dir: epath.PathLike | None,
      download_config: download.DownloadConfig,
  ) -> download.DownloadManager:
    """Creates a new download manager object."""
    download_dir = epath.Path(download_dir or self.data_dir_root / "downloads")
    extract_dir = download_config.extract_dir or download_dir / "extracted"
    manual_dir = download_config.manual_dir or download_dir / "manual"

    if download_config.register_checksums:
      # Note: Error will be raised here if user try to record checksums
      # from a `zipapp`
      try:
        register_checksums_path = utils.to_write_path(self._checksums_path)
        download.validate_checksums_path(register_checksums_path)
      except Exception:  # pylint: disable=broad-except
        raise
    else:
      register_checksums_path = None

    max_simultaneous_downloads = (
        download_config.override_max_simultaneous_downloads
        or self.MAX_SIMULTANEOUS_DOWNLOADS
    )
    if (
        max_simultaneous_downloads
        and self.MAX_SIMULTANEOUS_DOWNLOADS
        and self.MAX_SIMULTANEOUS_DOWNLOADS < max_simultaneous_downloads
    ):
      logging.warning(
          (
              "The dataset %r sets `MAX_SIMULTANEOUS_DOWNLOADS`=%s. The"
              " download config overrides it with value"
              " `override_max_simultaneous_downloads`=%s. Using the higher"
              " value might cause `ConnectionRefusedError`"
          ),
          self.name,
          self.MAX_SIMULTANEOUS_DOWNLOADS,
          download_config.override_max_simultaneous_downloads,
      )

    return download.DownloadManager(
        download_dir=download_dir,
        extract_dir=extract_dir,
        manual_dir=manual_dir,
        url_infos=self.url_infos,
        manual_dir_instructions=self.MANUAL_DOWNLOAD_INSTRUCTIONS,
        force_download=download_config.download_mode.force_download,
        force_extraction=download_config.download_mode.force_download,
        force_checksums_validation=download_config.force_checksums_validation,
        register_checksums=download_config.register_checksums,
        register_checksums_path=register_checksums_path,
        verify_ssl=download_config.verify_ssl,
        dataset_name=self.name,
        max_simultaneous_downloads=max_simultaneous_downloads,
    )

  @utils.docs.do_not_doc_in_subclasses
  @utils.classproperty
  @classmethod
  def builder_config_cls(cls) -> type[BuilderConfig] | None:
    """Returns the builder config class."""
    if not cls.BUILDER_CONFIGS:
      return None

    all_cls = {type(b) for b in cls.BUILDER_CONFIGS}
    if len(all_cls) != 1:
      raise ValueError(
          f"Could not infer the config class for {cls}. Detected: {all_cls}"
      )

    (builder_cls,) = all_cls
    return builder_cls

  @property
  def builder_config(self) -> Any | None:
    """`tfds.core.BuilderConfig` for this builder."""
    return self._builder_config

  @property
  def builder_config_name(self) -> str | None:
    """Name of the `tfds.core.BuilderConfig` for this builder."""
    return self._builder_config.name if self._builder_config else None

  def _create_builder_config(
      self,
      builder_config: str | BuilderConfig | None,
      version: str | utils.Version | None,
  ) -> BuilderConfig | None:
    """Create and validate BuilderConfig object."""
    if builder_config is None:
      builder_config = self.get_default_builder_config()
      if builder_config is not None:
        logging.info(
            "No config specified, defaulting to config: %s/%s",
            self.name,
            builder_config.name,
        )
    if not builder_config:
      return None
    if isinstance(builder_config, str):
      name = builder_config
      builder_config = self.builder_configs.get(name)
      if builder_config is None and version is not None:
        builder_config = self.builder_configs.get(f"{name}:{version}")
      if builder_config is None:
        raise ValueError(
            "BuilderConfig %s not found with version %s. Available: %s"
            % (name, version, list(self.builder_configs.keys()))
        )
    name = builder_config.name
    if not name:
      raise ValueError("BuilderConfig must have a name, got %s" % name)
    is_custom = name not in self.builder_configs
    if is_custom:
      logging.warning("Using custom data configuration %s", name)
    else:
      if builder_config is not self.builder_configs[name]:
        raise ValueError(
            "Cannot name a custom BuilderConfig the same as an available "
            "BuilderConfig. Change the name. Available BuilderConfigs: %s"
            % (list(self.builder_configs.keys()))
        )
    return builder_config

  @utils.classproperty
  @classmethod
  @utils.memoize()
  def builder_configs(cls) -> dict[str, BuilderConfig]:
    """Returns pre-defined list of configurations for this builder class.

    If the builder contains multiple versions of the same config, then the key
    of the dict will be "config_name:version".
    """
    # Determine whether there are configs with multiple versions.
    versions_per_config = collections.defaultdict(set)
    for config in cls.BUILDER_CONFIGS:
      version = config.version or cls.VERSION
      if version:
        versions_per_config[config.name].add(version)
    config_with_multiple_versions = any(
        [len(versions) > 1 for versions in versions_per_config.values()]
    )
    if config_with_multiple_versions:
      config_dict = {
          f"{config.name}:{config.version}": config
          for config in cls.BUILDER_CONFIGS
      }
    else:
      config_dict = {config.name: config for config in cls.BUILDER_CONFIGS}
    if len(config_dict) != len(cls.BUILDER_CONFIGS):
      names = [config.name for config in cls.BUILDER_CONFIGS]
      raise ValueError(
          "Names in BUILDER_CONFIGS must not be duplicated. Got %s" % names
      )
    return config_dict

  @classmethod
  def get_builder_config(
      cls, name: str, version: str | utils.Version | None = None
  ) -> BuilderConfig | None:
    """Returns the builder config with the given name and version."""
    if version is not None:
      name_with_version = f"{name}:{version}"
      if builder_config := cls.builder_configs.get(name_with_version):
        return builder_config
    if builder_config := cls.builder_configs.get(name):
      return builder_config
    return None

  def _get_filename_template(
      self, split_name: str
  ) -> naming.ShardedFileTemplate:
    """Returns a filename template for the given split."""
    return naming.ShardedFileTemplate(
        split=split_name,
        dataset_name=self.name,
        data_dir=self.data_path,
        filetype_suffix=self.info.file_format.file_suffix,  # pytype: disable=attribute-error
    )


class FileReaderBuilder(DatasetBuilder):
  """Base class for datasets reading files.

  Subclasses are:

   * `GeneratorBasedBuilder`: Can both generate and read generated dataset.
   * `ReadOnlyBuilder`: Can only read pre-generated datasets. A user can
     generate a dataset with `GeneratorBasedBuilder`, and read them with
     `ReadOnlyBuilder` without requiring the original generation code.
  """

  @tfds_logging.builder_init()
  def __init__(
      self,
      *,
      file_format: str | file_adapters.FileFormat | None = None,
      **kwargs: Any,
  ):
    """Initializes an instance of FileReaderBuilder.

    Callers must pass arguments as keyword arguments.

    Args:
      file_format: EXPERIMENTAL, may change at any time; Format of the record
        files in which dataset will be read/written to. If `None`, defaults to
        `tfrecord`.
      **kwargs: Arguments passed to `DatasetBuilder`.
    """
    super().__init__(**kwargs)
    self.info.set_file_format(file_format)

  @functools.cached_property
  def _example_specs(self):
    return self.info.features.get_serialized_info()

  def _as_dataset(  # pytype: disable=signature-mismatch  # overriding-parameter-type-checks
      self,
      split: splits_lib.Split,
      decoders: TreeDict[decode.partial_decode.DecoderArg] | None,
      read_config: read_config_lib.ReadConfig,
      shuffle_files: bool,
  ) -> tf.data.Dataset:
    # Partial decoding
    # TODO(epot): Should be moved inside `features.decode_example`
    if isinstance(decoders, decode.PartialDecoding):
      features = decoders.extract_features(self.info.features)
      example_specs = features.get_serialized_info()
      decoders = decoders.decoders
    # Full decoding (all features decoded)
    else:
      features = self.info.features
      example_specs = self._example_specs
      decoders = decoders  # pylint: disable=self-assigning-variable

    reader = reader_lib.Reader(
        self.data_dir,
        example_specs=example_specs,
        file_format=self.info.file_format,
    )
    decode_fn = functools.partial(features.decode_example, decoders=decoders)
    return reader.read(
        instructions=split,
        split_infos=self.info.splits.values(),
        decode_fn=decode_fn,
        read_config=read_config,
        shuffle_files=shuffle_files,
        disable_shuffling=self.info.disable_shuffling,
    )


class GeneratorBasedBuilder(FileReaderBuilder):
  """Base class for datasets with data generation based on file adapter.

  `GeneratorBasedBuilder` is a convenience class that abstracts away much
  of the data writing and reading of `DatasetBuilder`.

  It expects subclasses to overwrite `_split_generators` to return a dict of
  splits, generators. See the method docstrings for details.
  """

  @abc.abstractmethod
  @utils.docs.do_not_doc_in_subclasses
  @utils.docs.doc_private
  def _split_generators(
      self,
      dl_manager: download.DownloadManager,
  ) -> dict[splits_lib.Split, split_builder_lib.SplitGenerator]:
    """Downloads the data and returns dataset splits with associated examples.

    Example:

    ```python
    def _split_generators(self, dl_manager):
      path = dl_manager.download_and_extract('http://dataset.org/my_data.zip')
      return {
          'train': self._generate_examples(path=path / 'train_imgs'),
          'test': self._generate_examples(path=path / 'test_imgs'),
      }
    ```

    * If the original dataset do not have predefined `train`, `test`,... splits,
      this function should only returns a single `train` split here. Users can
      use the [subsplit API](https://www.tensorflow.org/datasets/splits) to
      create subsplits (e.g.
      `tfds.load(..., split=['train[:75%]', 'train[75%:]'])`).
    * `tfds.download.DownloadManager` caches downloads, so calling `download`
      on the same url multiple times only download it once.
    * A good practice is to download all data in this function, and have all the
      computation inside `_generate_examples`.
    * Splits are generated in the order defined here. `builder.info.splits` keep
      the same order.
    * This function can have an extra `pipeline` kwarg only if some
      beam preprocessing should be shared across splits. In this case,
      a dict of `beam.PCollection` should be returned.
      See `_generate_example` for details.

    Args:
      dl_manager: `tfds.download.DownloadManager` used to download/extract the
        data

    Returns:
      The dict of split name, generators. See `_generate_examples` for details
      about the generator format.
    """
    raise NotImplementedError()

  @abc.abstractmethod
  @utils.docs.do_not_doc_in_subclasses
  @utils.docs.doc_private
  def _generate_examples(
      self, **kwargs: Any
  ) -> split_builder_lib.SplitGenerator:
    """Default function to generate examples for each split.

    The function should return a collection of `(key, examples)`. Examples
    will be encoded and written to disk. See `yields` section for details.

    The function can return/yield:

    * A python generator:

    ```python
    def _generate_examples(self, path):
      for filepath in path.iterdir():
        yield filepath.name, {'image': ..., 'label': ...}
    ```

    * A `beam.PTransform` of (input_types: [] -> output_types: `KeyExample`):
    For big datasets and distributed generation. See our Apache Beam
    [datasets guide](https://www.tensorflow.org/datasets/beam_datasets)
    for more info.

    ```python
    def _generate_examples(self, path):
      return (
          beam.Create(path.iterdir())
          | beam.Map(lambda filepath: filepath.name, {'image': ..., ...})
      )
    ```

    * A `beam.PCollection`: This should only be used if you need to share some
    distributed processing across splits. In this case, you can use the
    following pattern:

    ```python
    def _split_generators(self, dl_manager, pipeline):
      ...
      # Distributed processing shared across splits
      pipeline |= beam.Create(path.iterdir())
      pipeline |= 'SharedPreprocessing' >> beam.Map(_common_processing)
      ...
      # Wrap the pipeline inside a ptransform_fn to add `'label' >> ` and avoid
      # duplicated PTransform nodes names.
      generate_examples = beam.ptransform_fn(self._generate_examples)
      return {
          'train': pipeline | 'train' >> generate_examples(is_train=True)
          'test': pipeline | 'test' >> generate_examples(is_train=False)
      }

    def _generate_examples(self, pipeline, is_train: bool):
      return pipeline | beam.Map(_split_specific_processing, is_train=is_train)
    ```

    Note: Each split should uses a different tag name (e.g.
    `'train' >> generate_examples(path)`). Otherwise Beam will raise
    duplicated name error.

    Args:
      **kwargs: Arguments from the `_split_generators`

    Yields:
      key: `str` or `int`, a unique deterministic example identification key.
        * Unique: An error will be raised if two examples are yield with the
          same key.
        * Deterministic: When generating the dataset twice, the same example
          should have the same key.
        * Comparable: If shuffling is disabled the key will be used to sort the
        dataset.
        Good keys can be the image id, or line number if examples are extracted
        from a text file.
        The example will be sorted by `hash(key)` if shuffling is enabled, and
        otherwise by `key`.
        Generating the dataset multiple times will keep examples in the
        same order.
      example: `dict<str feature_name, feature_value>`, a feature dictionary
        ready to be encoded and written to disk. The example will be
        encoded with `self.info.features.encode_example({...})`.
    """
    raise NotImplementedError()

  def _process_pipeline_result(
      self, pipeline_result: beam.runners.runner.PipelineResult
  ) -> None:
    """Processes the result of the beam pipeline if we used one.

    This can be used to (e.g) write beam counters to a file.
    Args:
      pipeline_result: PipelineResult returned by beam.Pipeline.run().
    """
    del pipeline_result

  def _example_writer(self) -> writer_lib.ExampleWriter:
    """Returns an example writer.

    If datasets should be written to a custom storage, e.g., a database, then
    implement a custom `ExampleWriter` and inject it here.
    """
    return writer_lib.ExampleWriter(file_format=self.info.file_format)

  def _generate_splits(
      self,
      dl_manager: download.DownloadManager,
      download_config: download.DownloadConfig,
  ) -> Sequence[splits_lib.SplitInfo]:
    """Generates all splits and returns the computed split infos."""
    split_builder = split_builder_lib.SplitBuilder(
        split_dict=self.info.splits,
        features=self.info.features,
        dataset_size=self.info.dataset_size,
        max_examples_per_split=download_config.max_examples_per_split,
        beam_options=download_config.beam_options,
        beam_runner=download_config.beam_runner,
        shard_config=download_config.get_shard_config(),
        example_writer=self._example_writer(),
        ignore_duplicates=download_config.ignore_duplicates,
    )
    # Wrap the generation inside a context manager.
    # If `beam` is used during generation (when a pipeline gets created),
    # the context manager is equivalent to `with beam.Pipeline()`.
    # Otherwise, this is a no-op.
    # By auto-detecting Beam, the user only has to change `_generate_examples`
    # to go from non-beam to beam dataset:
    # https://www.tensorflow.org/datasets/beam_datasets#instructions
    with split_builder.maybe_beam_pipeline() as maybe_pipeline_proxy:
      # If the signature has a `pipeline` kwargs, create the pipeline now and
      # forward it to `self._split_generators`
      # We add this magic because the pipeline kwargs is only used by c4 and
      # we do not want to make the API more verbose for a single advanced case.
      # See also the documentation at the end here:
      # https://www.tensorflow.org/datasets/api_docs/python/tfds/core/GeneratorBasedBuilder?version=nightly#_generate_examples
      signature = inspect.signature(self._split_generators)
      if "pipeline" in signature.parameters.keys():
        optional_pipeline_kwargs = dict(pipeline=split_builder.beam_pipeline)
      else:
        optional_pipeline_kwargs = {}
      split_generators = self._split_generators(  # pylint: disable=unexpected-keyword-arg
          dl_manager, **optional_pipeline_kwargs
      )
      # TODO(tfds): Could be removed once all datasets are migrated.
      # https://github.com/tensorflow/datasets/issues/2537
      # Legacy mode (eventually convert list[SplitGeneratorLegacy] -> dict)
      split_generators = split_builder.normalize_legacy_split_generators(
          split_generators=split_generators,
          generator_fn=self._generate_examples,
          is_beam=isinstance(self, BeamBasedBuilder),
      )

      # Ensure `all` isn't used as key.
      _check_split_names(split_generators.keys())

      # Start generating data for all splits
      split_info_futures = []
      for split_name, generator in utils.tqdm(
          split_generators.items(),
          desc="Generating splits...",
          unit=" splits",
          leave=False,
      ):
        filename_template = self._get_filename_template(split_name=split_name)
        future = split_builder.submit_split_generation(
            split_name=split_name,
            generator=generator,
            filename_template=filename_template,
            disable_shuffling=self.info.disable_shuffling,
        )
        split_info_futures.append(future)

    # Process the result of the beam pipeline.
    if maybe_pipeline_proxy._beam_pipeline:  # pylint:disable=protected-access
      self._process_pipeline_result(pipeline_result=maybe_pipeline_proxy.result)

    # Finalize the splits (after apache beam completed, if it was used)
    return [future.result() for future in split_info_futures]

  def _download_and_prepare(  # pytype: disable=signature-mismatch  # overriding-parameter-type-checks
      self,
      dl_manager: download.DownloadManager,
      download_config: download.DownloadConfig,
  ) -> None:
    """Generates all splits and sets the computed split infos."""
    # Writer fails if the number of example yield is `0`, so we return here.
    if download_config.max_examples_per_split == 0:
      return

    split_infos = self._generate_splits(dl_manager, download_config)

    # Update the info object with the splits.
    split_dict = splits_lib.SplitDict(split_infos)
    self.info.set_splits(split_dict)

  def read_text_file(
      self, filename: epath.PathLike, encoding: str | None = None
  ) -> str:
    """Returns the text in the given file and records the lineage."""
    filename = epath.Path(filename)
    self.info.add_file_data_source_access(filename)
    return filename.read_text(encoding=encoding)

  def read_tfrecord_as_dataset(
      self,
      filenames: str | Sequence[str],
      compression_type: str | None = None,
      num_parallel_reads: int | None = None,
  ) -> tf.data.Dataset:
    """Returns the dataset for the given tfrecord files and records the lineage."""
    if isinstance(filenames, str):
      filenames = [filenames]
    if not filenames:
      raise ValueError("No filenames given!")
    expanded_filenames = []
    for filename in filenames:
      self.info.add_file_data_source_access(filename)
      expanded_filenames.extend(file_utils.expand_glob(filename))
    filenames = [os.fspath(f) for f in expanded_filenames]

    return tf.data.TFRecordDataset(
        filenames=filenames,
        compression_type=compression_type,
        num_parallel_reads=num_parallel_reads,
    )

  def read_tfrecord_as_examples(
      self,
      filenames: str | Sequence[str],
      compression_type: str | None = None,
      num_parallel_reads: int | None = None,
  ) -> Iterator[tf.train.Example]:
    """Returns tf.Examples from the given tfrecord files and records the lineage."""
    raw_dataset = self.read_tfrecord_as_dataset(
        filenames=filenames,
        compression_type=compression_type,
        num_parallel_reads=num_parallel_reads,
    )
    for serialized_example in raw_dataset:
      example = tf.train.Example()
      example.ParseFromString(serialized_example.numpy())
      yield example

  def read_tfrecord_beam(
      self,
      file_pattern: str,
      /,
      **kwargs,
  ) -> beam.PTransform:
    """Returns a PTransform reading the TFRecords and records it in the dataset lineage.

    This function records the lineage in the DatasetInfo and then invokes
    `beam.io.ReadFromTFRecord`. The kwargs should contain any other parameters
    for `beam.io.ReadFromTFRecord`. See
    https://beam.apache.org/releases/pydoc/2.6.0/apache_beam.io.tfrecordio.html#apache_beam.io.tfrecordio.ReadFromTFRecord.

    Arguments:
      file_pattern: A file glob pattern to read TFRecords from.
      **kwargs: the other parameters for `beam.io.ReadFromTFRecord`.

    Returns:
      a Beam PTransform that reads the given TFRecord files.
    """
    self.info.add_file_data_source_access(file_pattern)
    return beam.io.ReadFromTFRecord(
        file_pattern=file_pattern,
        **kwargs,
    )


class ShardBasedBuilder(FileReaderBuilder):
  """Base class for datasets with data generated shard by shard.

  Like `GeneratorBasedBuilder`, this base class can be used to create datasets.
  However, `ShardBasedBuilder` gives strict control over the number of shards
  and what data ends up in what shard.

  This is useful for datasets where you want to keep the same ordering as the
  original data source, and/or where you want to keep the same sharding as the
  original data source.

  You have to implement the `_shard_iterators_per_split` method, which returns
  a mapping from split name to a list of `ExampleGeneratorFn` functions that
  return an example iterator. The signature of the function is `Callable[[],
  Iterator[KeyExample]]` where `KeyExample` is a tuple of (key, example) where
  key is a unique key for the example and example is a dict of features.

  Note that a `ExampleGeneratorFn` can also be a class that implements a
  `__call__` method that returns a `Iterator[KeyExample]`.

  Also note that shuffling is not supported. Also, the following fields in
  `DownloadConfig` are not supported:
  - `ignore_duplicates`
  - `max_examples_per_split`
  - `shard_config`
  """

  def _download_and_prepare(
      self,
      dl_manager: download.DownloadManager,
      download_config: download.DownloadConfig | None = None,
  ) -> None:
    download_config = download_config or download.DownloadConfig()

    split_builder = split_builder_lib.SplitBuilder(
        split_dict=self.info.splits,
        features=self.info.features,
        dataset_size=self.info.dataset_size,
        beam_options=download_config.beam_options,
        beam_runner=download_config.beam_runner,
        example_writer=self._example_writer(),
        # The following options are ignored by `ShardBasedBuilder`.
        ignore_duplicates=None,
        max_examples_per_split=None,
        shard_config=None,
    )

    shard_iterators_per_split = self._shard_iterators_per_split(dl_manager)
    split_info_futures = []
    for split_name, example_gen_per_shard in shard_iterators_per_split.items():
      logging.info("Generating split %s", split_name)
      split_info_future = split_builder.submit_shard_based_generation(
          split_name=split_name,
          example_gen_per_shard=example_gen_per_shard,
          filename_template=self._get_filename_template(split_name=split_name),
      )
      split_info_futures.append(split_info_future)

    # Update the info object with the splits.
    split_infos: list[splits_lib.SplitInfo] = [
        future.result() for future in split_info_futures
    ]
    split_dict = splits_lib.SplitDict(split_infos)
    self.info.set_splits(split_dict)

  @abc.abstractmethod
  @utils.docs.do_not_doc_in_subclasses
  @utils.docs.doc_private
  def _shard_iterators_per_split(
      self, dl_manager: download.DownloadManager
  ) -> Mapping[str, Sequence[split_builder_lib.ExampleGeneratorFn]]:
    """Returns a mapping from split name to example generators per shard.

    The example generators are functions with signature `Callable[[],
    Iterator[KeyExample]]` that take no parameters and return
    an iterator of tuples of (key, example). The order of the example generators
    is the order in which the shards will be written.

    Args:
      dl_manager: `tfds.download.DownloadManager` used to download/extract the
        data.
    """
    raise NotImplementedError()

  def _example_writer(self) -> writer_lib.ExampleWriter:
    """Returns an example writer.

    If datasets should be written to a custom storage, e.g., a database, then
    implement a custom `ExampleWriter` and inject it here.
    """
    return writer_lib.ExampleWriter(file_format=self.info.file_format)


@utils.docs.deprecated
class BeamBasedBuilder(GeneratorBasedBuilder):
  """Beam based Builder.

  DEPRECATED: Please use `tfds.core.GeneratorBasedBuilder` instead.
  """

  def _generate_examples(
      self, *args: Any, **kwargs: Any
  ) -> split_builder_lib.SplitGenerator:
    return self._build_pcollection(*args, **kwargs)


def _check_split_names(split_names: Iterable[str]) -> None:
  """Check that split names are valid."""
  if "all" in set(str(s).lower() for s in split_names):
    raise ValueError(
        "`all` is a reserved keyword. Split cannot be named like this."
    )


def _get_default_config(
    builder_configs: list[BuilderConfig],
    default_config_name: str | None,
) -> BuilderConfig | None:
  """Returns the default config from the given builder configs.

  Arguments:
    builder_configs: the configs from which the default should be picked.
    default_config_name: the name of the default config. If `None`, then it will
      use the first config.

  Returns:
    the default config. If there are no builder configs given, then None is
    returned.

  Raises:
    RuntimeError: if builder configs and a default config name are given, but no
    builder config with that name can be found.
  """
  if not builder_configs:
    return None
  if default_config_name is None:
    return builder_configs[0]
  for builder_config in builder_configs:
    if builder_config.name == default_config_name:
      return builder_config
  raise RuntimeError(
      f"Builder config with name `{default_config_name}` not found."
  )


def _save_default_config_name(
    common_dir: epath.Path,
    *,
    default_config_name: str,
) -> None:
  """Saves `builder_cls` metadata (common to all builder configs)."""
  data = {
      "default_config_name": default_config_name,
  }
  # `data_dir/ds_name/config/version/` -> `data_dir/ds_name/.config`
  config_dir = common_dir / ".config"
  config_dir.mkdir(parents=True, exist_ok=True)
  # Note:
  # * Save inside a dir to support some replicated filesystem
  # * Write inside a `.incomplete` file and rename to avoid multiple configs
  #   writing concurrently the same file
  # * Config file is overwritten each time a config is generated. If the
  #   default config is changed, this will be updated.
  config_path = config_dir / constants.METADATA_FILENAME
  with utils.incomplete_file(config_path) as tmp_config_path:
    tmp_config_path.write_text(json.dumps(data))


def load_default_config_name(builder_dir: epath.Path) -> str | None:
  """Load `builder_cls` metadata (common to all builder configs)."""
  config_path = builder_dir / ".config" / constants.METADATA_FILENAME
  if not config_path.exists():
    return None
  data = json.loads(config_path.read_text())
  return data.get("default_config_name")


def canonical_version_for_config(
    instance_or_cls: DatasetBuilder | Type[DatasetBuilder],
    config: BuilderConfig | None = None,
) -> utils.Version:
  """Get the canonical version for the given config.

  This allow to get the version without instanciating the class.
  The version can be stored either at the class or in the config object.

  Args:
    instance_or_cls: The instance or class on which get the version
    config: The config which might contain the version, or None if the dataset
      do not have config.

  Returns:
    version: The extracted version.
  """
  if instance_or_cls.BUILDER_CONFIGS and config is None:
    raise ValueError(
        f"Cannot infer version on {instance_or_cls.name}. Unknown config."
    )

  if config and config.version:
    return utils.Version(config.version)
  elif instance_or_cls.VERSION:
    return utils.Version(instance_or_cls.VERSION)
  else:
    raise ValueError(
        f"DatasetBuilder {instance_or_cls.name} does not have a defined "
        "version. Please add a `VERSION = tfds.core.Version('x.y.z')` to the "
        "class."
    )
