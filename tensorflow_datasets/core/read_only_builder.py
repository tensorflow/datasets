# coding=utf-8
# Copyright 2025 The TensorFlow Datasets Authors.
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

"""Load Datasets without reading dataset generation code."""

from __future__ import annotations

from collections.abc import Sequence
import concurrent.futures
import functools
import os
import typing
from typing import Any, Type

from etils import epy
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  from etils import epath
  from etils import etree
  from tensorflow_datasets.core import dataset_builder
  from tensorflow_datasets.core import dataset_info
  from tensorflow_datasets.core import file_adapters
  from tensorflow_datasets.core import logging as tfds_logging
  from tensorflow_datasets.core import naming
  from tensorflow_datasets.core import registered
  from tensorflow_datasets.core import splits as splits_lib
  from tensorflow_datasets.core import utils
  from tensorflow_datasets.core.features import feature as feature_lib
  from tensorflow_datasets.core.proto import dataset_info_pb2
  from tensorflow_datasets.core.utils import error_utils
  from tensorflow_datasets.core.utils import file_utils
  from tensorflow_datasets.core.utils import version as version_lib
  # pylint: enable=g-import-not-at-top


class ReadOnlyBuilder(
    dataset_builder.FileReaderBuilder, skip_registration=True
):
  """Generic DatasetBuilder loading from a directory."""

  @tfds_logging.builder_init(is_read_only_builder=True)
  def __init__(
      self,
      builder_dir: epath.PathLike,
      *,
      info_proto: dataset_info_pb2.DatasetInfo | None = None,
      file_format: str | file_adapters.FileFormat | None = None,
  ):
    """Constructor.

    Args:
      builder_dir: Directory of the dataset to load (e.g.
        `~/tensorflow_datasets/mnist/3.0.0/`)
      info_proto: DatasetInfo describing the name, config, etc of the requested
        dataset. Note that this overwrites dataset info that may be present in
        builder_dir.
      file_format: The desired file format to use for the dataset. If not
        specified, the file format in the DatasetInfo is used.

    Raises:
      FileNotFoundError: If the builder_dir does not exist.
    """
    builder_dir = os.path.expanduser(builder_dir)
    if not info_proto:
      info_proto = dataset_info.read_proto_from_builder_dir(builder_dir)
    self._info_proto = info_proto
    if file_format is not None:
      file_format = file_adapters.FileFormat.from_value(file_format)
      available_formats = set([self._info_proto.file_format])
      available_formats.update(self._info_proto.alternative_file_formats)
      if file_format.file_suffix not in available_formats:
        raise ValueError(
            f'File format {file_format.file_suffix} does not match the file'
            f' formats in the DatasetInfo: {sorted(available_formats)}.'
        )

    self.name = info_proto.name
    self.VERSION = version_lib.Version(info_proto.version)  # pylint: disable=invalid-name
    self.RELEASE_NOTES = info_proto.release_notes or {}  # pylint: disable=invalid-name
    self.BLOCKED_VERSIONS = self._restore_blocked_versions(info_proto)  # pylint: disable=invalid-name

    if info_proto.module_name:
      # Overwrite the module so documenting `ReadOnlyBuilder` point to the
      # original source code.
      self.__module__ = info_proto.module_name

    builder_config = dataset_builder.BuilderConfig.from_dataset_info(info_proto)
    # __init__ will call _build_data_dir, _create_builder_config,
    # _pick_version to set the data_dir, config, and version
    super().__init__(
        data_dir=builder_dir,
        config=builder_config,
        version=info_proto.version,
        file_format=file_format,
    )
    self.assert_is_not_blocked()

    # For pickling, should come after super.__init__ which is setting that same
    # _original_state attribute.
    self._original_state = dict(builder_dir=builder_dir)

    if self.info.features is None:
      raise ValueError(
          f'Cannot restore {self.info.full_name}. It likely means the dataset '
          'was generated with an old TFDS version (<=3.2.1).'
      )

  def _restore_blocked_versions(
      self, info_proto: dataset_info_pb2.DatasetInfo
  ) -> version_lib.BlockedVersions | None:
    """Restores the blocked version information from the dataset info proto.

    Args:
      info_proto: DatasetInfo describing the name, config, etc of the requested
        dataset.

    Returns:
      None if the dataset is not blocked, or a populated BlockedVersions object.
    """
    if info_proto.is_blocked:
      configs = {
          info_proto.version: {info_proto.config_name: info_proto.is_blocked}
      }
      return version_lib.BlockedVersions(configs=configs)
    return None

  def _create_builder_config(
      self,
      builder_config: str | dataset_builder.BuilderConfig | None,
      version: str | utils.Version | None,
  ) -> dataset_builder.BuilderConfig | None:
    del version
    if isinstance(builder_config, str):
      raise ValueError(
          "'builder_config' must be a BuilderConfig, not a str. Value is"
          f" '{builder_config}"
      )
    return builder_config  # BuilderConfig is created in __init__

  def _pick_version(self, version: str) -> utils.Version:
    return utils.Version(version)

  def _build_data_dir(self, data_dir: str) -> tuple[str, str]:
    return data_dir, data_dir  # _data_dir_root, _data_dir are builder_dir.

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo.from_proto(self, self._info_proto)

  def _download_and_prepare(self, **kwargs):  # pylint: disable=arguments-differ
    # DatasetBuilder.download_and_prepare is a no-op as self.data_dir already
    # exists.
    raise AssertionError("ReadOnlyBuilder can't be generated.")


def builder_from_directory(
    builder_dir: epath.PathLike,
    file_format: str | file_adapters.FileFormat | None = None,
) -> dataset_builder.DatasetBuilder:
  """Loads a `tfds.core.DatasetBuilder` from the given generated dataset path.

  Reconstructs the `tfds.core.DatasetBuilder` without requiring the original
  generation code.

  From `<builder_dir>/features.json` it infers the structure (feature names,
  nested dict,...) and content (image, sequence,...) of the dataset. The
  serialization format is defined in
  `tfds.features.FeatureConnector` in `to_json()`.

  Note: This function only works for datasets generated with TFDS `4.0.0` or
  above.

  Args:
    builder_dir: Path of the directory containing the dataset to read ( e.g.
      `~/tensorflow_datasets/mnist/3.0.0/`).
    file_format: The desired file format to use for the dataset. If not
      specified, the default file format in the DatasetInfo is used.

  Returns:
    builder: `tfds.core.DatasetBuilder`, builder for dataset at the given path.
  """
  return ReadOnlyBuilder(builder_dir=builder_dir, file_format=file_format)


def builder_from_directories(
    builder_dirs: Sequence[epath.PathLike],
    *,
    filetype_suffix: str | None = None,  # DEPRECATED
) -> dataset_builder.DatasetBuilder:
  """Loads a `tfds.core.DatasetBuilder` from the given generated dataset path.

  When a dataset is spread out over multiple folders, then this function can be
  used to easily read from all builder dirs.

  Note that the data in each folder must have the same features, dataset name,
  and version.

  Some examples of when a dataset might be spread out over multiple folders:

  - in reinforcement learning, multiple agents each produce a dataset
  - each day a new dataset is produced based on new incoming events

  Arguments:
    builder_dirs: the list of builder dirs from which the data should be read.
    filetype_suffix: DEPRECATED PLEASE DO NOT USE. The filetype suffix (e.g.
      'tfrecord') that is used if the file format is not specified in the
      DatasetInfo.

  Returns:
    the read only dataset builder that is configured to read from all the given
    builder dirs.
  """
  if not builder_dirs:
    raise ValueError('No builder dirs were given!')

  dataset_infos = etree.parallel_map(
      dataset_info.read_proto_from_builder_dir, {d: d for d in builder_dirs}
  )

  # TODO(tfds): assert that the features of all datasets are identical.

  def get_split_dict(builder_dir, dataset_info_proto) -> splits_lib.SplitDict:
    filename_template = naming.ShardedFileTemplate(
        dataset_name=dataset_info_proto.name,
        data_dir=builder_dir,
        filetype_suffix=dataset_info_proto.file_format or filetype_suffix,
    )
    return splits_lib.SplitDict.from_proto(
        repeated_split_infos=dataset_info_proto.splits,
        filename_template=filename_template,
    )

  merged_split_dict = splits_lib.SplitDict.merge_multiple([
      get_split_dict(builder_dir, dataset_info_proto)
      for builder_dir, dataset_info_proto in dataset_infos.items()
  ])

  # We create the ReadOnlyBuilder for a random builder_dir and then update the
  # splits to capture the splits from all builder dirs.
  random_builder_dir = builder_dirs[0]
  random_builder = ReadOnlyBuilder(
      builder_dir=random_builder_dir,
      info_proto=dataset_infos[random_builder_dir],
  )
  random_builder.info.set_splits(merged_split_dict)
  return random_builder


def builder_from_metadata(
    builder_dir: epath.PathLike,
    info_proto: dataset_info_pb2.DatasetInfo,
) -> dataset_builder.DatasetBuilder:
  """Loads a `tfds.core.DatasetBuilder` from the given metadata.

  Reconstructs the `tfds.core.DatasetBuilder` without requiring the original
  generation code. The given `info_proto` overrides whatever dataset info is in
  `builder_dir`.

  The dataset structure (feature names, nested dict,...) and content (image,
  sequence, ...) is used from the given DatasetInfo.

  Args:
    builder_dir: path of the directory containing the dataset to read (e.g.
      `~/tensorflow_datasets/mnist/3.0.0/`). Dataset info in this folder is
      overridden by the `info_proto`.
    info_proto: DatasetInfo describing the name, config, features, etc of the
      requested dataset.

  Returns:
    builder: `tfds.core.DatasetBuilder`, builder for dataset at the given path.
  """
  builder = ReadOnlyBuilder(builder_dir=builder_dir, info_proto=info_proto)
  return builder


@error_utils.reraise_with_context(registered.DatasetNotFoundError)
def builder_from_files(
    name: str,
    **builder_kwargs: Any,
) -> dataset_builder.DatasetBuilder:
  """Loads a `tfds.core.DatasetBuilder` from files, auto-inferring location.

  This function is similar to `tfds.builder` (same signature), but creates
  the `tfds.core.DatasetBuilder` directly from files, without loading
  original generation source code.

  It does not support:

   * namespaces (e.g. 'kaggle:dataset')
   * config objects (`dataset/config` valid, but not `config=MyConfig()`)
   * `version='experimental_latest'`

  Args:
    name: Dataset name.
    **builder_kwargs: `tfds.core.DatasetBuilder` kwargs.

  Returns:
    builder: The loaded dataset builder.

  Raises:
    DatasetNotFoundError: If the dataset cannot be loaded.
  """
  # Find and load dataset builder.
  builder_dir = _find_builder_dir(name, **builder_kwargs)
  if builder_dir is None:
    data_dirs = file_utils.list_data_dirs(
        given_data_dir=builder_kwargs.get('data_dir')
    )
    raise registered.DatasetNotFoundError(
        f'Could not find dataset files for: {name}. Make sure you have the'
        ' correct permissions to access the dataset '
        f'and that it has been generated in: {data_dirs}. If the dataset has'
        ' configs, you might have to specify the config name.'
    )
  file_format = builder_kwargs.pop('file_format', None)
  return builder_from_directory(builder_dir, file_format=file_format)


def _find_builder_dir(name: str, **builder_kwargs: Any) -> epath.Path | None:
  """Search whether the given dataset is present on disk and return its path.

  Note:

   * If the dataset is present, but is legacy (no feature config file), None
     is returned.
   * If the config isn't specified, the function tries to infer the default
     config name from the original `DatasetBuilder`.
   * The function searches in all `data_dir` registered with
     `tfds.core.add_data_dir`. If the dataset exists in multiple dirs, an error
     is raised.

  Args:
    name: Builder name (e.g. `my_ds`, `my_ds/config`, `my_ds:1.2.0`,...)
    **builder_kwargs: `tfds.core.DatasetBuilder` kwargs.

  Returns:
    path: The dataset path found, or None if the dataset isn't found.
  """
  # Normalize builder kwargs
  name, builder_kwargs = naming.parse_builder_name_kwargs(
      name, **builder_kwargs
  )
  version = builder_kwargs.pop('version', None)
  version = str(version) if version else None
  config = builder_kwargs.pop('config', None)
  data_dir = builder_kwargs.pop('data_dir', None)
  _ = builder_kwargs.pop('file_format', None)

  # Builder cannot be found if it uses:
  # * namespace
  # * version='experimental_latest'
  # * config objects (rather than `str`)
  # * custom DatasetBuilder.__init__ kwargs
  if (
      name.namespace
      or version == 'experimental_latest'
      or isinstance(config, dataset_builder.BuilderConfig)
      or builder_kwargs
  ):
    error_msgs = ['Builder cannot be loaded from files if it uses:']
    if name.namespace:
      error_msgs.append(f'* namespaces (here, {name.namespace} is used)')
    if version == 'experimental_latest':
      error_msgs.append('* `experimental_latest` as requested version.')
    if isinstance(config, dataset_builder.BuilderConfig):
      error_msgs.append('* config objects (rather than `str`).')
    if builder_kwargs:
      error_msgs.append('* custom DatasetBuilder.__init__ kwargs.')
    error_utils.add_context('\t'.join(error_msgs))
    return None

  # Search the dataset across all registered data_dirs
  all_builder_dirs: set[epath.Path] = set()
  all_data_dirs = set(file_utils.list_data_dirs(given_data_dir=data_dir))
  find_builder_fn = functools.partial(
      _find_builder_dir_single_dir,
      builder_name=name.name,
      config_name=config,
      version=version,
  )
  if len(all_data_dirs) <= 1:
    for current_data_dir in all_data_dirs:
      if builder_dir := find_builder_fn(data_dir=current_data_dir):
        all_builder_dirs.add(builder_dir)
  else:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
      # Keep track of each new thread's error context, and add it to the main
      # error context when each thread finishes.
      def wrapped_find_builder_fn(data_dir):
        with error_utils.record_error_context() as thread_context:
          builder_dir = find_builder_fn(data_dir)
        return thread_context, builder_dir

      for context, builder_dir in executor.map(
          wrapped_find_builder_fn, all_data_dirs
      ):
        if builder_dir:
          all_builder_dirs.add(builder_dir)
        for msg in context.messages:
          error_utils.add_context(msg)

  if not all_builder_dirs:
    all_dirs_str = '\n\t- '.join([''] + [str(dir) for dir in all_data_dirs])
    error_msg = f'No registered data_dirs were found in:{all_dirs_str}\n'

    # If the dataset root_dir exists, a common error is that the config name
    # was not specified. So we list the possible configs and display them.
    possible_configs = _list_possible_configs(name.name, all_data_dirs)
    if possible_configs:
      configs_str = '\n\t- '.join([''] + possible_configs)
      error_msg = (
          f'However, a folder for "{name.name}" does exist. Is it possible that'
          ' you specified the wrong config? You can add a config by replacing'
          f' `tfds.load({name.name})` by `tfds.load("{name.name}/my_config")`.'
          f' Possible configs are:{configs_str}\n'
      )

    error_utils.add_context(error_msg)
    return None

  elif len(all_builder_dirs) != 1:
    # Rather than raising error every time, we could potentially be smarter
    # and load the most recent version across all files, but should be
    # careful when partial version is requested ('my_dataset:3.*.*').
    # Could add some `MultiDataDirManager` API:
    # ```
    # manager = MultiDataDirManager(given_data_dir=data_dir)
    # with manager.merge_data_dirs() as virtual_data_dir:
    #  virtual_builder_dir = _find_builder_dir(name, data_dir=virtual_data_dir)
    #  builder_dir = manager.resolve(virtual_builder_dir)
    # ```
    raise ValueError(
        f'Dataset {name} detected in multiple locations: {all_builder_dirs}. '
        'Please resolve the ambiguity by explicitly setting `data_dir=`.'
    )

  return all_builder_dirs.pop()


def _list_possible_configs(
    builder_name: str, all_data_dirs: set[epath.PathLike]
) -> list[str]:
  configs = []
  for data_dir in all_data_dirs:
    builder_dir = epath.Path(data_dir) / builder_name
    if builder_dir.exists():
      for path in builder_dir.iterdir():
        if path.is_dir():
          configs.append(path.name)
  return configs


def _contains_dataset(dataset_dir: epath.Path) -> bool:
  try:
    return feature_lib.make_config_path(dataset_dir).exists()
  except (OSError, tf.errors.PermissionDeniedError):
    return False


def _find_builder_dir_single_dir(
    data_dir: epath.PathLike,
    builder_name: str,
    config_name: str | None = None,
    version: version_lib.Version | str | None = None,
) -> epath.Path | None:
  """Same as `find_builder_dir` but requires explicit dir."""

  # If the version is specified, check if the dataset dir exists and return.
  if version_lib.Version.is_valid(version):
    dataset_dir = file_utils.get_dataset_dir(
        data_dir=data_dir,
        builder_name=builder_name,
        config_name=config_name,
        version=version,
    )
    if _contains_dataset(dataset_dir):
      return dataset_dir

  # If no config_name or an empty string was given, we try to find the default
  # config and load the dataset for that.
  if not config_name:
    config_name = _get_default_config_name(
        data_dir=data_dir, builder_name=builder_name
    )
    if version_lib.Version.is_valid(version):
      dataset_dir = file_utils.get_dataset_dir(
          data_dir=data_dir,
          builder_name=builder_name,
          config_name=config_name,
          version=version,
      )
      if _contains_dataset(dataset_dir):
        return dataset_dir

  # Dataset wasn't found, try to find a suitable available version.
  found_version = _get_version(
      data_dir=data_dir,
      builder_name=builder_name,
      config_name=config_name,
      requested_version=version,
  )
  if found_version and str(found_version) != str(version):
    dataset_dir = file_utils.get_dataset_dir(
        data_dir=data_dir,
        builder_name=builder_name,
        config_name=config_name,
        version=found_version,
    )
    if _contains_dataset(dataset_dir):
      return dataset_dir

  # If no builder found, we populate the error_context with useful information
  # and return None.
  error_utils.add_context(
      'No builder could be found in the directory: '
      f'{data_dir} for the builder: {builder_name}.'
  )
  return None


def _get_default_config_name(
    data_dir: epath.Path,
    builder_name: str,
) -> str | None:
  """Returns the default config of the given dataset, None if not found."""
  builder_dir = file_utils.get_dataset_dir(
      data_dir=data_dir, builder_name=builder_name
  )
  # Search for the DatasetBuilder generation code
  try:
    # Warning: The registered dataset may not match the files (e.g. if
    # the imported datasets has the same name as the generated files while
    # being 2 differents datasets)
    cls = registered.imported_builder_cls(builder_name)
    cls = typing.cast(Type[dataset_builder.DatasetBuilder], cls)
  except registered.DatasetNotFoundError:
    pass
  except PermissionError as e:
    error_msg = f'Permission error when accessing: {builder_dir}: {e}'
    error_utils.add_context(error_msg)
  else:
    # If code found, return the default config
    if cls.BUILDER_CONFIGS:
      return cls.default_builder_config.name

  # Otherwise, try to load default config from common metadata
  return dataset_builder.load_default_config_name(builder_dir)


def _get_version(
    data_dir: epath.Path,
    builder_name: str,
    config_name: str | None = None,
    requested_version: version_lib.Version | str | None = None,
) -> version_lib.Version | None:
  """Returns the version name found in the builder directory.

  Args:
    data_dir: Directory containing the builder.
    builder_name: Name of the builder.
    config_name: Name of the config.
    requested_version: Optional version to search (e.g. `1.0.0`, `2.*.*`,...)
  """
  config_dir = file_utils.get_dataset_dir(
      data_dir=data_dir, builder_name=builder_name, config_name=config_name
  )
  all_versions = version_lib.list_all_versions(config_dir)
  # Version not given, using the latest one.
  if not requested_version and all_versions:
    return all_versions[-1]
  # Version given, return the highest version matching `requested_version`.
  for v in reversed(all_versions):
    if v.match(requested_version):
      return v
  # Directory doesn't have version, or requested_version doesn't match
  if requested_version:
    error_msg = (
        f'No version matching the requested {requested_version} was '
        f'found in the builder directory: {config_dir}.'
    )
  else:
    error_msg = (
        f"The builder directory {config_dir} doesn't contain any versions."
    )
  error_utils.add_context(error_msg)
  return None
