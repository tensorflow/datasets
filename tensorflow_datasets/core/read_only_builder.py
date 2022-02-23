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

"""Load Datasets without reading dataset generation code."""

import os
import typing
from typing import Any, List, Optional, Tuple, Type

from etils import epath
import tensorflow as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import dataset_info
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import registered
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils import version as version_lib


class ReadOnlyBuilder(
    dataset_builder.FileReaderBuilder, skip_registration=True):
  """Generic DatasetBuilder loading from a directory."""

  def __init__(self,
               builder_dir: epath.PathLike,
               *,
               info_proto: Optional[dataset_info_pb2.DatasetInfo] = None):
    """Constructor.

    Args:
      builder_dir: Directory of the dataset to load (e.g.
        `~/tensorflow_datasets/mnist/3.0.0/`)
      info_proto: DatasetInfo describing the name, config, etc of the requested
        dataset. Note that this overwrites dataset info that may be present in
        builder_dir.

    Raises:
      FileNotFoundError: If the builder_dir does not exists.
    """
    builder_dir = os.path.expanduser(builder_dir)
    if not info_proto:
      info_proto = dataset_info.read_proto_from_builder_dir(builder_dir)
    self._info_proto = info_proto

    self.name = info_proto.name
    self.VERSION = version_lib.Version(info_proto.version)  # pylint: disable=invalid-name
    self.RELEASE_NOTES = info_proto.release_notes or {}  # pylint: disable=invalid-name
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
    )

    # For pickling, should come after super.__init__ which is setting that same
    # _original_state attribute.
    self._original_state = dict(builder_dir=builder_dir)

    if self.info.features is None:
      raise ValueError(
          f'Cannot restore {self.info.full_name}. It likely means the dataset '
          'was generated with an old TFDS version (<=3.2.1).')

  def _create_builder_config(
      self, builder_config: Optional[dataset_builder.BuilderConfig]
  ) -> Optional[dataset_builder.BuilderConfig]:
    return builder_config  # BuilderConfig is created in __init__

  def _pick_version(self, version: str) -> utils.Version:
    return utils.Version(version)

  def _build_data_dir(self, data_dir: str) -> Tuple[str, str]:
    return data_dir, data_dir  # _data_dir_root, _data_dir are builder_dir.

  def _info(self) -> dataset_info.DatasetInfo:
    return dataset_info.DatasetInfo.from_proto(self, self._info_proto)

  def _download_and_prepare(self, **kwargs):  # pylint: disable=arguments-differ
    # DatasetBuilder.download_and_prepare is a no-op as self.data_dir already
    # exists.
    raise AssertionError('ReadOnlyBuilder can\'t be generated.')


def builder_from_directory(
    builder_dir: epath.PathLike,) -> dataset_builder.DatasetBuilder:
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
    builder_dir: `str`, path of the directory containing the dataset to read (
      e.g. `~/tensorflow_datasets/mnist/3.0.0/`).

  Returns:
    builder: `tf.core.DatasetBuilder`, builder for dataset at the given path.
  """
  return ReadOnlyBuilder(builder_dir=builder_dir)


def builder_from_directories(
    builder_dirs: List[epath.PathLike],
    *,
    filetype_suffix: Optional[str] = None) -> dataset_builder.DatasetBuilder:
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
    filetype_suffix: the filetype suffix (e.g. 'tfrecord') that is used if the
      file format is not specified in the DatasetInfo.

  Returns:
    the read only dataset builder that is configured to read from all the given
    builder dirs.
  """
  if not builder_dirs:
    raise ValueError('No builder dirs were given!')

  dataset_infos = utils.tree.parallel_map(
      dataset_info.read_proto_from_builder_dir, {d: d for d in builder_dirs})

  # TODO(tfds): assert that the features of all datasets are identical.

  def get_split_dict(builder_dir, dataset_info_proto) -> splits_lib.SplitDict:
    filename_template = naming.ShardedFileTemplate(
        dataset_name=dataset_info_proto.name,
        data_dir=builder_dir,
        filetype_suffix=dataset_info_proto.file_format or filetype_suffix)
    return splits_lib.SplitDict.from_proto(
        repeated_split_infos=dataset_info_proto.splits,
        filename_template=filename_template)

  merged_split_dict = splits_lib.SplitDict.merge_multiple([
      get_split_dict(builder_dir, dataset_info_proto)
      for builder_dir, dataset_info_proto in dataset_infos.items()
  ])

  # We create the ReadOnlyBuilder for a random builder_dir and then update the
  # splits to capture the splits from all builder dirs.
  random_builder_dir = builder_dirs[0]
  random_builder = ReadOnlyBuilder(
      builder_dir=random_builder_dir,
      info_proto=dataset_infos[random_builder_dir])
  random_builder.info.set_splits(merged_split_dict)
  return random_builder


def builder_from_metadata(
    builder_dir: epath.PathLike,
    info_proto: dataset_info_pb2.DatasetInfo) -> dataset_builder.DatasetBuilder:
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
    builder: `tf.core.DatasetBuilder`, builder for dataset at the given path.
  """
  return ReadOnlyBuilder(builder_dir=builder_dir, info_proto=info_proto)


def builder_from_files(
    name: str,
    **builder_kwargs: Any,
) -> dataset_builder.DatasetBuilder:
  """Loads a `tfds.core.DatasetBuilder` from files, auto-infering location.

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
        given_data_dir=builder_kwargs.get('data_dir'))
    raise registered.DatasetNotFoundError(
        f'Could not find dataset files for: {name}. Make sure the dataset '
        f'has been generated in: {data_dirs}. If the dataset has configs, you '
        'might have to specify the config name.')
  return builder_from_directory(builder_dir)


def _find_builder_dir(name: str, **builder_kwargs: Any) -> Optional[str]:
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
      name, **builder_kwargs)
  version = builder_kwargs.pop('version', None)
  config = builder_kwargs.pop('config', None)
  data_dir = builder_kwargs.pop('data_dir', None)

  # Builder cannot be found if it uses:
  # * namespace
  # * version='experimental_latest'
  # * config objects (rather than `str`)
  # * custom DatasetBuilder.__init__ kwargs
  if (name.namespace or version == 'experimental_latest' or
      isinstance(config, dataset_builder.BuilderConfig) or builder_kwargs):
    return None

  # Search the dataset across all registered data_dirs
  all_builder_dirs = []
  for current_data_dir in file_utils.list_data_dirs(given_data_dir=data_dir):
    builder_dir = _find_builder_dir_single_dir(
        name.name,
        data_dir=current_data_dir,
        version_str=str(version) if version else None,
        config_name=config,
    )
    if builder_dir:
      all_builder_dirs.append(builder_dir)
  if not all_builder_dirs:
    return None
  elif len(all_builder_dirs) != 1:
    # Rather than raising error every time, we could potentially be smarter
    # and load the most recent version across all files, but should be
    # carefull when partial version is requested ('my_dataset:3.*.*').
    # Could add some `MultiDataDirManager` API:
    # ```
    # manager = MultiDataDirManager(given_data_dir=data_dir)
    # with manager.merge_data_dirs() as virtual_data_dir:
    #  virtual_builder_dir = _find_builder_dir(name, data_dir=virtual_data_dir)
    #  builder_dir = manager.resolve(virtual_builder_dir)
    # ```
    raise ValueError(
        f'Dataset {name} detected in multiple locations: {all_builder_dirs}. '
        'Please resolve the ambiguity by explicitly setting `data_dir=`.')

  return all_builder_dirs[0]


def _find_builder_dir_single_dir(
    builder_name: str,
    *,
    data_dir: str,
    config_name: Optional[str] = None,
    version_str: Optional[str] = None,
) -> Optional[str]:
  """Same as `find_builder_dir` but requires explicit dir."""
  # Construct the `ds_name/config/` path
  builder_dir = epath.Path(data_dir) / builder_name
  if not config_name:
    # If the BuilderConfig is not specified:
    # * Either the dataset doesn't have a config
    # * Either the default config should be used
    # Currently, in order to infer the default config, we are still relying on
    # the code.
    # TODO(tfds): How to avoid code dependency and automatically infer the
    # config existence and name?
    config_name = _get_default_config_name(builder_dir, builder_name)

  # If has config (explicitly given or default config), append it to the path
  if config_name:
    builder_dir = builder_dir / config_name

  # Extract the version
  version_str = _get_version_str(builder_dir, requested_version=version_str)

  if not version_str:  # Version not given or found
    return None

  builder_dir = builder_dir / version_str

  try:
    # Backward compatibility, in order to be a valid ReadOnlyBuilder, the folder
    # has to contain the feature configuration.
    builder_dir = os.fspath(builder_dir)
    if tf.io.gfile.exists(feature_lib.make_config_path(builder_dir)):
      return str(builder_dir)
  except tf.errors.PermissionDeniedError:
    return None
  return None


def _get_default_config_name(
    builder_dir: epath.Path,
    name: str,
) -> Optional[str]:
  """Returns the default config of the given dataset, None if not found."""
  # Search for the DatasetBuilder generation code
  try:
    # Warning: The registered dataset may not match the files (e.g. if
    # the imported datasets has the same name as the generated files while
    # being 2 differents datasets)
    cls = registered.imported_builder_cls(name)
    cls = typing.cast(Type[dataset_builder.DatasetBuilder], cls)
  except (registered.DatasetNotFoundError, PermissionError):
    pass
  else:
    # If code found, return the default config
    if cls.BUILDER_CONFIGS:
      return cls.BUILDER_CONFIGS[0].name

  # Otherwise, try to load default config from common metadata
  return dataset_builder.load_default_config_name(epath.Path(builder_dir))


def _get_version_str(
    builder_dir: epath.Path,
    *,
    requested_version: Optional[str] = None,
) -> Optional[str]:
  """Returns the version name found in the directory.

  Args:
    builder_dir: Directory containing the versions (`builder_dir/1.0.0/`,...)
    requested_version: Optional version to search (e.g. `1.0.0`, `2.*.*`,...)

  Returns:
    version_str: The version directory name found in `builder_dir`.
  """
  all_versions = version_lib.list_all_versions(os.fspath(builder_dir))
  # Version not given, using the last one.
  if not requested_version and all_versions:
    return str(all_versions[-1])
  # Version given, return the biggest version matching `requested_version`
  for v in reversed(all_versions):
    if v.match(requested_version):
      return str(v)
  # Directory don't has version, or requested_version don't match
  return None
