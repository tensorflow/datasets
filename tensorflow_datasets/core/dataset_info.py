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

"""DatasetInfo records the information we know about a dataset.

This includes things that we know about the dataset statically, i.e.:
 - schema
 - description
 - canonical location
 - does it have validation and tests splits
 - size
 - etc.

This also includes the things that can and should be computed once we've
processed the dataset as well:
 - number of examples (in each split)
 - feature statistics (in each split)
 - etc.
"""

from __future__ import annotations

import abc
from collections.abc import Iterable, Sequence
import dataclasses
import json
import os
import posixpath
import tempfile
import time
from typing import Any

from absl import logging
from etils import epath
from etils import epy
from tensorflow_datasets.core import constants
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import top_level_feature
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.core.utils.lazy_imports_utils import apache_beam as beam
from tensorflow_datasets.core.utils.lazy_imports_utils import tensorflow as tf

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  from tensorflow_datasets.core.utils import file_utils
  from tensorflow_datasets.core.utils import gcs_utils

  from google.protobuf import json_format
  # pylint: enable=g-import-not-at-top


Nest = tuple["Nest", ...] | dict[str, "Nest"] | str
SupervisedKeysType = tuple[Nest, Nest] | tuple[Nest, Nest, Nest]


def dataset_info_path(dataset_info_dir: epath.PathLike) -> epath.Path:
  return epath.Path(dataset_info_dir) / constants.DATASET_INFO_FILENAME


def license_path(dataset_info_dir: epath.PathLike) -> epath.Path:
  return epath.Path(dataset_info_dir) / constants.LICENSE_FILENAME


class Metadata(dict, metaclass=abc.ABCMeta):
  """Abstract base class for DatasetInfo metadata container.

  `builder.info.metadata` allows the dataset to expose additional general
  information about the dataset which are not specific to a feature or
  individual example.

  To implement the interface, overwrite `save_metadata` and
  `load_metadata`.

  See `tfds.core.MetadataDict` for a simple implementation that acts as a
  dict that saves data to/from a JSON file.
  """

  @abc.abstractmethod
  def save_metadata(self, data_dir):
    """Save the metadata."""
    raise NotImplementedError()

  @abc.abstractmethod
  def load_metadata(self, data_dir):
    """Restore the metadata."""
    raise NotImplementedError()


@dataclasses.dataclass
class DatasetIdentity:
  """Identity of a dataset that completely identifies a dataset."""

  name: str
  version: utils.Version
  data_dir: str
  module_name: str
  config_name: str | None = None
  config_description: str | None = None
  config_tags: list[str] | None = None
  release_notes: dict[str, str] | None = None

  @classmethod
  def from_builder(cls, builder) -> "DatasetIdentity":
    """Constructs a `DatasetIdentity` from a given dataset builder."""
    if builder.builder_config:
      config_name = builder.builder_config.name
      config_description = builder.builder_config.description
      config_tags = builder.builder_config.tags
    else:
      config_name = None
      config_description = None
      config_tags = None

    return cls(
        name=builder.name,
        version=utils.Version(builder.version),
        data_dir=builder.data_dir,
        module_name=str(builder.__module__),
        config_name=config_name,
        config_description=config_description,
        config_tags=config_tags,
        release_notes=builder.release_notes,
    )

  @classmethod
  def from_proto(
      cls,
      info_proto: dataset_info_pb2.DatasetInfo,
      data_dir: str,
  ) -> "DatasetIdentity":
    """Constructs a `DatasetIdentity` for a given dataset.

    Args:
      info_proto: The `DatasetInfo` proto for the dataset.
      data_dir: Path to the data_dir for the dataset.

    Returns:
      A `DatasetIdentity` object for the required dataset.
    """
    return cls(
        name=info_proto.name,
        version=utils.Version(info_proto.version),
        data_dir=data_dir,
        module_name=info_proto.module_name,
        config_name=info_proto.config_name,
        config_description=info_proto.config_description,
        config_tags=info_proto.config_tags or [],
        release_notes={k: v for k, v in info_proto.release_notes.items()},
    )


class DatasetInfo:
  """Information about a dataset.

  `DatasetInfo` documents datasets, including its name, version, and features.
  See the constructor arguments and properties for a full list.

  Note: Not all fields are known if the dataset hasn't been generated yet
  (before the first `builder.download_and_prepare()` call). For example splits
  names or number of examples might be missing (as they are computed
  at dataset creation time).
  """

  def __init__(
      # LINT.IfChange(dataset_info_args)
      self,
      *,
      builder: DatasetIdentity | Any,
      description: str | None = None,
      features: feature_lib.FeatureConnector | None = None,
      supervised_keys: SupervisedKeysType | None = None,
      disable_shuffling: bool = False,
      homepage: str | None = None,
      citation: str | None = None,
      metadata: Metadata | None = None,
      license: str | None = None,  # pylint: disable=redefined-builtin
      redistribution_info: dict[str, str] | None = None,
      split_dict: splits_lib.SplitDict | None = None,
      alternative_file_formats: (
          Sequence[str | file_adapters.FileFormat] | None
      ) = None,
      is_blocked: str | None = None,
      # LINT.ThenChange(:setstate)
  ):
    # pyformat: disable
    """Constructs DatasetInfo.

    Args:
      builder: `DatasetBuilder` or `DatasetIdentity`. The dataset builder or
        identity will be used to populate this info.
      description: `str`, description of this dataset.
      features: `tfds.features.FeaturesDict`, Information on the feature dict of
        the `tf.data.Dataset()` object from the `builder.as_dataset()` method.
      supervised_keys: Specifies the input structure for supervised learning, if
        applicable for the dataset, used with "as_supervised". The keys
        correspond to the feature names to select in `info.features`. When
        calling `tfds.core.DatasetBuilder.as_dataset()` with
        `as_supervised=True`, the `tf.data.Dataset` object will yield the
        structure defined by the keys passed here, instead of that defined by
        the `features` argument. Typically this is a `(input_key, target_key)`
        tuple, and the dataset yields a tuple of tensors `(input, target)`
        tensors.

        To yield a more complex structure, pass a tuple of `tf.nest` compatible
        structures of feature keys. The resulting `Dataset` will yield
        structures with each key replaced by the coresponding tensor. For
        example, passing a triple of keys would return a dataset
        that yields `(feature, target, sample_weights)` triples for keras.
        Using `supervised_keys=({'a':'a','b':'b'}, 'c')` would create a dataset
        yielding a tuple with a dictionary of features in the `features`
        position.

        Note that selecting features in nested `tfds.features.FeaturesDict`
        objects is not supported.
      disable_shuffling: `bool`, specify whether to shuffle the examples.
      homepage: `str`, optional, the homepage for this dataset.
      citation: `str`, optional, the citation to use for this dataset.
      metadata: `tfds.core.Metadata`, additonal object which will be
        stored/restored with the dataset. This allows for storing additional
        information with the dataset.
      license: license of the dataset.
      redistribution_info: information needed for redistribution, as specified
        in `dataset_info_pb2.RedistributionInfo`. The content of the `license`
        subfield will automatically be written to a LICENSE file stored with the
        dataset.
      split_dict: information about the splits in this dataset.
      alternative_file_formats: alternative file formats that are availablefor
        this dataset.
      is_blocked: A message explaining why the dataset, in its version and
        config, is blocked. If empty or None, the dataset is not blocked.
    """
    # pyformat: enable
    self._builder_or_identity = builder
    if isinstance(builder, DatasetIdentity):
      self._identity = builder
    else:
      self._identity = DatasetIdentity.from_builder(builder)

    # Convert alternative_file_formats to a list of `FileFormat`.
    self._alternative_file_formats: list[file_adapters.FileFormat] = []
    if alternative_file_formats is not None:
      for f in alternative_file_formats:
        if isinstance(f, str):
          f = file_adapters.FileFormat.from_value(f)
        self._alternative_file_formats.append(f)

    self._is_blocked = is_blocked

    self._info_proto = dataset_info_pb2.DatasetInfo(
        name=self._identity.name,
        description=utils.dedent(description),
        version=str(self._identity.version),
        release_notes=self._identity.release_notes,
        disable_shuffling=disable_shuffling,
        config_name=self._identity.config_name,
        config_description=self._identity.config_description,
        config_tags=self._identity.config_tags,
        citation=utils.dedent(citation),
        module_name=self._identity.module_name,
        redistribution_info=_create_redistribution_info_proto(
            license=license, redistribution_info=redistribution_info
        ),
        alternative_file_formats=[
            f.value for f in self._alternative_file_formats
        ],
        is_blocked=self._is_blocked,
    )

    if homepage:
      self._info_proto.location.urls[:] = [homepage]

    if features:
      if not isinstance(features, top_level_feature.TopLevelFeature):
        raise ValueError(
            "DatasetInfo.features only supports FeaturesDict or Sequence at "
            "the top-level. Got {}".format(features)
        )
    self._features = features
    self._splits = splits_lib.SplitDict([])
    if split_dict:
      self.set_splits(split_dict)
    if supervised_keys is not None:
      self._info_proto.supervised_keys.CopyFrom(
          _supervised_keys_to_proto(supervised_keys)
      )

    if metadata and not isinstance(metadata, Metadata):
      raise ValueError(
          "Metadata should be a `tfds.core.Metadata` instance. Received "
          "{}".format(metadata)
      )
    self._metadata = metadata

    # Is this object initialized with both the static and the dynamic data?
    self._fully_initialized = False

  @property
  def _builder(self) -> Any:
    logging.warning("DEPRECATED: please do not use _builder as this may change")
    return self._builder_or_identity

  @classmethod
  def from_proto(
      cls,
      builder,
      proto: dataset_info_pb2.DatasetInfo,
  ) -> "DatasetInfo":
    """Instantiates DatasetInfo from the given builder and proto."""
    if builder.builder_config:
      assert builder.builder_config.name == proto.config_name
    assert str(builder.version) == proto.version
    features = None
    if proto.HasField("features"):
      features = feature_lib.FeatureConnector.from_proto(proto.features)
    supervised_keys = None
    if proto.HasField("supervised_keys"):
      supervised_keys = _supervised_keys_from_proto(proto.supervised_keys)
    filename_template = naming.ShardedFileTemplate(
        dataset_name=builder.name,
        data_dir=builder.data_dir,
        filetype_suffix=proto.file_format or "tfrecord",
    )
    return cls(
        builder=builder,
        description=proto.description,
        features=features,
        supervised_keys=supervised_keys,
        disable_shuffling=proto.disable_shuffling,
        citation=proto.citation,
        license=proto.redistribution_info.license,
        split_dict=splits_lib.SplitDict.from_proto(
            repeated_split_infos=proto.splits,
            filename_template=filename_template,
        ),
        alternative_file_formats=proto.alternative_file_formats,
    )

  @property
  def as_proto(self) -> dataset_info_pb2.DatasetInfo:
    return self._info_proto

  @property
  def as_proto_with_features(self) -> dataset_info_pb2.DatasetInfo:
    return update_info_proto_with_features(self._info_proto, self.features)

  @property
  def name(self) -> str:
    return self._identity.name

  @property
  def config_name(self) -> str:
    return self._info_proto.config_name

  @property
  def config_description(self) -> str | None:
    return self._identity.config_description

  @property
  def config_tags(self) -> list[str] | None:
    return self._identity.config_tags

  @property
  def full_name(self):
    """Full canonical name: (<dataset_name>/<config_name>/<version>)."""
    names = [self.name]
    if self.config_name:
      names.append(self.config_name)
    names.append(str(self.version))
    return posixpath.join(*names)

  @property
  def description(self):
    return self.as_proto.description

  @property
  def version(self):
    return self._identity.version

  @property
  def release_notes(self) -> dict[str, str] | None:
    return self._identity.release_notes

  @property
  def disable_shuffling(self) -> bool:
    return self.as_proto.disable_shuffling

  @property
  def homepage(self) -> str:
    urls = self.as_proto.location.urls
    tfds_homepage = f"https://www.tensorflow.org/datasets/catalog/{self.name}"
    return urls and urls[0] or tfds_homepage

  @property
  def citation(self) -> str:
    return self.as_proto.citation

  @property
  def data_dir(self) -> str:
    return self._identity.data_dir

  @property
  def dataset_size(self) -> utils.Size:
    """Generated dataset files size, in bytes."""
    # For old datasets, maybe empty.
    return utils.Size(sum(split.num_bytes for split in self.splits.values()))

  @property
  def download_size(self) -> utils.Size:
    """Downloaded files size, in bytes."""
    # Fallback to deprecated `size_in_bytes` if `download_size` is empty.
    return utils.Size(
        self.as_proto.download_size or self.as_proto.size_in_bytes
    )

  @download_size.setter
  def download_size(self, size: int):
    self.as_proto.download_size = size

  @property
  def features(self):
    return self._features

  @property
  def alternative_file_formats(self) -> list[file_adapters.FileFormat]:
    return self._alternative_file_formats

  @property
  def metadata(self) -> Metadata | None:
    return self._metadata

  @property
  def is_blocked(self) -> str | None:
    return self._is_blocked

  def set_is_blocked(self, is_blocked: str) -> None:
    self._is_blocked = is_blocked

  @property
  def supervised_keys(self) -> SupervisedKeysType | None:
    if not self.as_proto.HasField("supervised_keys"):
      return None
    supervised_keys = self.as_proto.supervised_keys
    return _supervised_keys_from_proto(supervised_keys)

  @property
  def redistribution_info(self):
    return self.as_proto.redistribution_info

  @property
  def module_name(self) -> str:
    return self._identity.module_name

  @property
  def file_format(self) -> file_adapters.FileFormat | None:
    if not self.as_proto.file_format:
      return None
    return file_adapters.FileFormat(self.as_proto.file_format)

  def set_file_format(
      self,
      file_format: None | str | file_adapters.FileFormat,
      override: bool = False,
      override_if_initialized: bool = False,
  ) -> None:
    """Internal function to define the file format.

    The file format is set during `FileReaderBuilder.__init__`,
    not `DatasetInfo.__init__`.

    Args:
      file_format: The file format.
      override: Whether the file format should be overridden if it is already
        set.
      override_if_initialized: Whether the file format should be overridden if
        the DatasetInfo is already fully initialized.

    Raises:
      ValueError: if the file format was already set and the `override`
      parameter was False.
      RuntimeError: if an incorrect combination of options is given, e.g.
      `override=True` when the DatasetInfo is already fully initialized.
    """
    # If file format isn't present already, fallback to `DEFAULT_FILE_FORMAT`
    file_format = (
        file_format  # Format explicitly given: tfds.builder(..., file_format=x)
        or self.file_format  # Format restored from dataset_info.json
        or file_adapters.DEFAULT_FILE_FORMAT
    )
    file_format = file_adapters.FileFormat.from_value(file_format)

    # If the file format has been set once, file format should be consistent
    if not override and self.file_format and self.file_format != file_format:
      raise ValueError(
          f"File format is already set to {self.file_format}. Got {file_format}"
      )
    if override and self._fully_initialized and not override_if_initialized:
      raise RuntimeError(
          "Cannot override the file format when the DatasetInfo is already"
          " fully initialized!"
      )
    self._info_proto.file_format = file_format.value
    if override_if_initialized:
      # Update the splits to point to the new file format.
      updated_split_infos = []
      for split_info in self.splits.values():
        if split_info.filename_template is None:
          continue
        updated_split_info = split_info.replace(
            filename_template=split_info.filename_template.replace(
                filetype_suffix=file_format.file_suffix
            )
        )
        updated_split_infos.append(updated_split_info)
      self._splits = splits_lib.SplitDict(updated_split_infos)

  def add_alternative_file_format(
      self,
      file_format: str | file_adapters.FileFormat,
  ) -> None:
    """Adds an alternative file format to the dataset info."""
    if isinstance(file_format, str):
      file_format = file_adapters.FileFormat.from_value(file_format)
    if file_format in self.alternative_file_formats:
      raise ValueError(
          f"Alternative file format {file_format} is already present."
      )
    self._alternative_file_formats.append(file_format)
    self.as_proto.alternative_file_formats.append(file_format.value)

  def available_file_formats(self) -> set[file_adapters.FileFormat]:
    formats = set()
    if self.file_format:
      formats.add(self.file_format)
    formats.update(self.alternative_file_formats)
    return formats

  @property
  def splits(self) -> splits_lib.SplitDict:
    return self._splits

  def set_splits(self, split_dict: splits_lib.SplitDict) -> None:
    """Split setter (private method)."""
    for split, split_info in split_dict.items():
      if isinstance(split_info, splits_lib.MultiSplitInfo):
        # When splits are from multiple folders, the dataset can be different.
        continue
      if (
          split_info.filename_template
          and self.name != split_info.filename_template.dataset_name
      ):
        raise AssertionError(
            f"SplitDict contains SplitInfo for split {split} whose "
            "dataset_name does not match to the dataset name in dataset_info. "
            f"{self.name} != {split_info.filename_template.dataset_name}"
        )

    # If the statistics have been pre-loaded, forward the statistics
    # into the new split_dict. Also add the filename template if it's not set.
    new_split_infos = []
    incomplete_filename_template = naming.ShardedFileTemplate(
        data_dir=epath.Path(self.data_dir),
        dataset_name=self.name,
        filetype_suffix=(
            self.as_proto.file_format or file_adapters.DEFAULT_FILE_FORMAT.value
        ),
    )
    for split_info in split_dict.values():
      if isinstance(split_info, splits_lib.MultiSplitInfo):
        new_split_infos.append(split_info)
        continue
      old_split_info = self._splits.get(split_info.name)
      if (
          not split_info.statistics.ByteSize()
          and old_split_info
          and old_split_info.statistics.ByteSize()
          and old_split_info.shard_lengths == split_info.shard_lengths
      ):
        split_info = split_info.replace(statistics=old_split_info.statistics)
      if not split_info.filename_template:
        filename_template = incomplete_filename_template.replace(
            split=split_info.name
        )
        split_info = split_info.replace(filename_template=filename_template)
      new_split_infos.append(split_info)

    # Update the dictionary representation.
    self._splits = splits_lib.SplitDict(new_split_infos)

    # Update the proto
    # Note that the proto should not be saved or used for multi-folder datasets.
    del self.as_proto.splits[:]  # Clear previous
    for split_info in self._splits.values():
      if isinstance(split_info, splits_lib.MultiSplitInfo):
        for si in split_info.split_infos:
          self.as_proto.splits.add().CopyFrom(si.to_proto())
      else:
        self.as_proto.splits.add().CopyFrom(split_info.to_proto())

  def update_data_dir(self, data_dir: str) -> None:
    """Updates the data dir for each split."""
    new_split_infos = []
    for split_info in self._splits.values():
      if isinstance(split_info, splits_lib.MultiSplitInfo):
        raise RuntimeError(
            "Updating the data_dir for MultiSplitInfo is not supported!"
        )
      if not split_info.filename_template:
        continue
      filename_template = split_info.filename_template.replace(
          data_dir=data_dir
      )
      new_split_info = split_info.replace(filename_template=filename_template)
      new_split_infos.append(new_split_info)
    self.set_splits(splits_lib.SplitDict(new_split_infos))

  @property
  def initialized(self) -> bool:
    """Whether DatasetInfo has been fully initialized."""
    return self._fully_initialized

  @property
  def as_json(self) -> str:
    return get_dataset_info_json(self.as_proto)

  def write_to_directory(
      self, dataset_info_dir: epath.PathLike, all_metadata=True
  ) -> None:
    """Write `DatasetInfo` as JSON to `dataset_info_dir` + labels & features.

    Args:
      dataset_info_dir: path to directory in which to save the
        `dataset_info.json` file, as well as `features.json` and `*.labels.txt`
        if applicable.
      all_metadata: defaults to True. If False, will not write metadata which
        may have an impact on how the data is read (features.json). Should be
        set to True whenever `write_to_directory` is called for the first time
        for a new dataset.
    """
    if all_metadata:
      # Save the features structure & metadata (vocabulary, labels,...)
      if self.features:
        self.features.save_config(dataset_info_dir)

    # Save any additional metadata
    if self.metadata is not None:
      self.metadata.save_metadata(dataset_info_dir)

    if self.redistribution_info.license:
      license_path(dataset_info_dir).write_text(
          self.redistribution_info.license
      )

    self.write_dataset_info_json(dataset_info_dir)

  def write_dataset_info_json(self, dataset_info_dir: epath.PathLike) -> None:
    """Writes only the dataset_info.json file to the given directory."""
    write_dataset_info_proto(self.as_proto, dataset_info_dir=dataset_info_dir)

  def read_from_directory(self, dataset_info_dir: epath.PathLike) -> None:
    """Update DatasetInfo from the metadata files in `dataset_info_dir`.

    This function updates all the dynamically generated fields (num_examples,
    hash, time of creation,...) of the DatasetInfo.

    This will overwrite all previous metadata.

    Args:
      dataset_info_dir: The directory containing the metadata file. This should
        be the root directory of a specific dataset version.

    Raises:
      FileNotFoundError: If the dataset_info.json can't be found.
    """
    logging.info("Load dataset info from %s", dataset_info_dir)

    # Load the metadata from disk
    try:
      parsed_proto = read_from_json(dataset_info_path(dataset_info_dir))
    except Exception as e:
      raise FileNotFoundError(
          "Tried to load `DatasetInfo` from a directory which does not exist or"
          " does not contain `dataset_info.json`. Please delete the directory "
          f"`{dataset_info_dir}`  if you are trying to re-generate the "
          "dataset."
      ) from e

    if str(self.version) != parsed_proto.version:
      raise AssertionError(
          "The constructed DatasetInfo instance and the restored proto version "
          "do not match. Builder version: {}. Proto version: {}".format(
              self.version, parsed_proto.version
          )
      )

    self._identity = DatasetIdentity.from_proto(
        info_proto=parsed_proto, data_dir=dataset_info_dir
    )

    # Update splits
    filename_template = naming.ShardedFileTemplate(  # pytype: disable=wrong-arg-types  # always-use-property-annotation
        dataset_name=self.name,
        data_dir=self.data_dir,
        filetype_suffix=parsed_proto.file_format or "tfrecord",
    )
    split_dict = splits_lib.SplitDict.from_proto(
        repeated_split_infos=parsed_proto.splits,
        filename_template=filename_template,
    )
    self.set_splits(split_dict)

    # Restore the feature metadata (vocabulary, labels names,...)
    if self.features:
      self.features.load_metadata(dataset_info_dir, feature_name=None)
    # For `ReadOnlyBuilder`, reconstruct the features from the config.
    elif feature_lib.make_config_path(dataset_info_dir).exists():
      self._features = top_level_feature.TopLevelFeature.from_config(
          dataset_info_dir
      )

    # Restore the MetaDataDict from metadata.json if there is any
    if _metadata_filepath(dataset_info_dir).exists():
      # If the dataset was loaded from file, self.metadata will be `None`, so
      # we create a MetadataDict first.
      if self._metadata is None:
        self._metadata = MetadataDict()
      self._metadata.load_metadata(dataset_info_dir)

    # Update fields which are not defined in the code. This means that
    # the code will overwrite fields which are present in
    # dataset_info.json.
    fields_taken_from_code = []
    for field_name, field in self.as_proto.DESCRIPTOR.fields_by_name.items():
      field_value = getattr(self._info_proto, field_name)
      field_value_restored = getattr(parsed_proto, field_name)

      try:
        is_defined = self._info_proto.HasField(field_name)
      except ValueError:
        is_defined = bool(field_value)

      try:
        is_defined_in_restored = parsed_proto.HasField(field_name)
      except ValueError:
        is_defined_in_restored = bool(field_value_restored)

      # If field is defined in code, we ignore the value.
      if is_defined:
        if field_value != field_value_restored:
          fields_taken_from_code.append(field_name)
        continue
      # If the field is also not defined in JSON file, we do nothing
      if not is_defined_in_restored:
        continue
      # Otherwise, we restore the dataset_info.json value
      if field.type == field.TYPE_MESSAGE:
        field_value.MergeFrom(field_value_restored)
      elif field.label == field.LABEL_REPEATED:
        del field_value[:]
        field_value.extend(field_value_restored)
      else:
        setattr(self._info_proto, field_name, field_value_restored)

    if fields_taken_from_code:
      logging.info(
          (
              "For '%s': fields info.[%s] differ on disk and in the code. "
              "Keeping the one from code."
          ),
          self.full_name,
          ", ".join(fields_taken_from_code),
      )

    # Mark as fully initialized.
    self._fully_initialized = True

  def add_file_data_source_access(
      self,
      path: epath.PathLike | Iterable[epath.PathLike],
      url: str | None = None,
  ) -> None:
    """Records that the given query was used to generate this dataset.

    Arguments:
      path: path or paths of files that were read. Can be a file pattern.
        Multiple paths or patterns can be specified as a comma-separated string
        or a list.
      url:  URL referring to the data being used.
    """
    access_timestamp_ms = _now_in_milliseconds()
    if isinstance(path, str) or isinstance(path, epath.Path):
      path = os.fspath(path).split(",")
    for p in path:
      for file in file_utils.expand_glob(p):
        self._info_proto.data_source_accesses.append(
            dataset_info_pb2.DataSourceAccess(
                access_timestamp_ms=access_timestamp_ms,
                file_system=dataset_info_pb2.FileSystem(path=os.fspath(file)),
                url=dataset_info_pb2.Url(url=url),
            )
        )

  def add_url_access(
      self,
      url: str,
      checksum: str | None = None,
  ) -> None:
    """Records the URL used to generate this dataset."""
    self._info_proto.data_source_accesses.append(
        dataset_info_pb2.DataSourceAccess(
            access_timestamp_ms=_now_in_milliseconds(),
            url=dataset_info_pb2.Url(url=url, checksum=checksum),
        )
    )

  def add_sql_data_source_access(
      self,
      sql_query: str,
  ) -> None:
    """Records that the given query was used to generate this dataset."""
    self._info_proto.data_source_accesses.append(
        dataset_info_pb2.DataSourceAccess(
            access_timestamp_ms=_now_in_milliseconds(),
            sql_query=dataset_info_pb2.SqlQuery(sql_query=sql_query),
        )
    )

  def add_tfds_data_source_access(
      self,
      dataset_reference: naming.DatasetReference,
      url: str | None = None,
  ) -> None:
    """Records that the given query was used to generate this dataset.

    Args:
      dataset_reference:
      url: a URL referring to the TFDS dataset.
    """
    add_tfds_data_source_access(
        dataset_info_proto=self._info_proto,
        dataset_reference=dataset_reference,
        url=url,
    )

  def initialize_from_bucket(self) -> None:
    """Initialize DatasetInfo from GCS bucket info files."""
    # In order to support Colab, we use the HTTP GCS API to access the metadata
    # files. They are copied locally and then loaded.
    tmp_dir = epath.Path(tempfile.mkdtemp("tfds"))
    data_files = gcs_utils.gcs_dataset_info_files(self.full_name)
    if not data_files:
      return
    logging.info(
        (
            "Load pre-computed DatasetInfo (eg: splits, num examples,...) "
            "from GCS: %s"
        ),
        self.full_name,
    )
    for path in data_files:
      out_fname = tmp_dir / path.name
      epath.Path(path).copy(out_fname)
    self.read_from_directory(tmp_dir)

  def __repr__(self):
    SKIP = object()  # pylint: disable=invalid-name

    splits = _indent(
        "\n".join(
            ["{"]
            + [
                f"    '{k}': {split},"
                for k, split in sorted(self.splits.items())
            ]
            + ["}"]
        )
    )

    if self._info_proto.config_description:
      config_description = _indent(
          f'"""\n{self._info_proto.config_description}\n"""'
      )
    else:
      config_description = SKIP

    if self._info_proto.config_tags:
      config_tags = ", ".join(self.config_tags)
    else:
      config_tags = SKIP

    file_format_str = (
        self.file_format.value
        if self.file_format
        else file_adapters.DEFAULT_FILE_FORMAT.value
    )
    lines = ["tfds.core.DatasetInfo("]
    for key, value in [
        ("name", repr(self.name)),
        ("full_name", repr(self.full_name)),
        ("description", _indent(f'"""\n{self.description}\n"""')),
        ("config_description", config_description),
        ("config_tags", config_tags),
        ("homepage", repr(self.homepage)),
        ("data_dir", repr(self.data_dir)),
        ("file_format", file_format_str),
        ("download_size", self.download_size),
        ("dataset_size", self.dataset_size),
        ("features", _indent(repr(self.features))),
        ("supervised_keys", self.supervised_keys),
        ("disable_shuffling", self.disable_shuffling),
        ("splits", splits),
        ("citation", _indent(f'"""{self.citation}"""')),
        # Proto add a \n that we strip.
        ("redistribution_info", str(self.redistribution_info).strip() or SKIP),
    ]:
      if value != SKIP:
        lines.append(f"    {key}={value},")
    lines.append(")")
    return "\n".join(lines)

  def __getstate__(self):
    return {
        "builder": self._builder_or_identity,
        "description": self.description,
        "features": self.features,
        "supervised_keys": self.supervised_keys,
        "disable_shuffling": self.disable_shuffling,
        "homepage": self.homepage,
        "citation": self.citation,
        "metadata": self.metadata,
        "license": self.redistribution_info.license,
        "split_dict": self.splits,
        "alternative_file_formats": self.alternative_file_formats,
        "is_blocked": self.is_blocked,
    }
  def __setstate__(self, state):
    # LINT.IfChange(setstate)
    self.__init__(
        builder=state["builder"],
        description=state["description"],
        features=state["features"],
        supervised_keys=state["supervised_keys"],
        disable_shuffling=state["disable_shuffling"],
        homepage=state["homepage"],
        citation=state["citation"],
        metadata=state["metadata"],
        license=state["license"],
        split_dict=state["split_dict"],
        alternative_file_formats=state["alternative_file_formats"],
        is_blocked=state["is_blocked"],
    )
    # LINT.ThenChange(:dataset_info_args)


def _nest_to_proto(nest: Nest) -> dataset_info_pb2.SupervisedKeys.Nest:
  """Creates a `SupervisedKeys.Nest` from a limited `tf.nest` style structure.

  Args:
    nest: A `tf.nest` structure of tuples, dictionaries or string feature keys.

  Returns:
    The same structure as a `SupervisedKeys.Nest` proto.
  """
  nest_type = type(nest)
  proto = dataset_info_pb2.SupervisedKeys.Nest()
  if nest_type is tuple:
    for item in nest:
      proto.tuple.items.append(_nest_to_proto(item))
  elif nest_type is dict:
    nest = {key: _nest_to_proto(value) for key, value in nest.items()}
    proto.dict.CopyFrom(dataset_info_pb2.SupervisedKeys.Dict(dict=nest))
  elif nest_type is str:
    proto.feature_key = nest
  else:
    raise ValueError(
        "The nested structures in `supervised_keys` must only "
        "contain instances of (tuple, dict, str), no subclasses.\n"
        f"Found type: {nest_type}"
    )

  return proto


def _supervised_keys_to_proto(
    keys: SupervisedKeysType,
) -> dataset_info_pb2.SupervisedKeys:
  """Converts a `supervised_keys` tuple to a SupervisedKeys proto."""
  if not isinstance(keys, tuple) or len(keys) not in [2, 3]:
    raise ValueError(
        "`supervised_keys` must contain a tuple of 2 or 3 elements.\n"
        f"got: {keys!r}"
    )

  proto = dataset_info_pb2.SupervisedKeys(
      tuple=dataset_info_pb2.SupervisedKeys.Tuple(
          items=(_nest_to_proto(key) for key in keys)
      )
  )
  return proto


def _nest_from_proto(proto: dataset_info_pb2.SupervisedKeys.Nest) -> Nest:
  """Creates a `tf.nest` style structure from a `SupervisedKeys.Nest` proto.

  Args:
    proto: A `SupervisedKeys.Nest` proto.

  Returns:
    The proto converted to a `tf.nest` style structure of tuples, dictionaries
    or strings.
  """
  if proto.HasField("tuple"):
    return tuple(_nest_from_proto(item) for item in proto.tuple.items)
  elif proto.HasField("dict"):
    return {
        key: _nest_from_proto(value)
        for key, value in sorted(proto.dict.dict.items())
    }
  elif proto.HasField("feature_key"):
    return proto.feature_key
  else:
    raise ValueError(
        "`SupervisedKeys.Nest` proto must contain one of "
        f"(tuple, dict, feature_key). Got: {proto}"
    )


def _supervised_keys_from_proto(
    proto: dataset_info_pb2.SupervisedKeys,
) -> SupervisedKeysType:
  """Converts a `SupervisedKeys` proto back to a simple python tuple."""
  if proto.input and proto.output:
    return (proto.input, proto.output)
  elif proto.tuple:
    return tuple(_nest_from_proto(item) for item in proto.tuple.items)
  else:
    raise ValueError(
        "A `SupervisedKeys` proto must have either `input` and "
        "`output` defined, or `tuple`, got: {proto}"
    )


def _indent(content):
  """Add indentation to all lines except the first."""
  lines = content.split("\n")
  return "\n".join([lines[0]] + ["    " + l for l in lines[1:]])


def _populate_shape(shape_or_dict, prefix, schema_features):
  """Populates shape in the schema."""
  if isinstance(shape_or_dict, (tuple, list)):
    feature_name = "/".join(prefix)
    if shape_or_dict and feature_name in schema_features:
      schema_feature = schema_features[feature_name]
      schema_feature.ClearField("shape")
      for dim in shape_or_dict:
        # We denote `None`s as -1 in the shape proto.
        schema_feature.shape.dim.add().size = -1 if dim is None else dim
    return
  for name, val in shape_or_dict.items():
    prefix.append(name)
    _populate_shape(val, prefix, schema_features)
    prefix.pop()


def get_dataset_info_json(
    dataset_info_proto: dataset_info_pb2.DatasetInfo,
) -> str:
  return json_format.MessageToJson(dataset_info_proto, sort_keys=True)


def write_dataset_info_proto(
    dataset_info_proto: dataset_info_pb2.DatasetInfo,
    dataset_info_dir: epath.PathLike,
) -> None:
  """Writes the dataset info proto to the given path."""
  dataset_info_dir = epath.Path(dataset_info_dir)
  json_str = get_dataset_info_json(dataset_info_proto)
  dataset_info_path(dataset_info_dir).write_text(json_str)


def read_from_json(path: epath.PathLike) -> dataset_info_pb2.DatasetInfo:
  """Read JSON-formatted proto into DatasetInfo proto.

  Args:
    path: the path of the dataset info json file.

  Returns:
    the DatasetInfo proto.

  Raises:
    FileNotFoundError: If the builder_dir does not exist.
  """
  try:
    json_str = epath.Path(path).read_text()
  except OSError as e:
    raise FileNotFoundError(f"Could not load dataset info from {path}") from e
  # Parse it back into a proto.
  parsed_proto = json_format.Parse(json_str, dataset_info_pb2.DatasetInfo())
  return parsed_proto


def read_proto_from_builder_dir(
    builder_dir: epath.PathLike,
) -> dataset_info_pb2.DatasetInfo:
  """Reads the dataset info from the given builder dir.

  Args:
    builder_dir: The folder that contains the dataset info files.

  Returns:
    The DatasetInfo proto as read from the builder dir.

  Raises:
    FileNotFoundError: If the builder_dir does not exist.
  """
  builder_dir = epath.Path(builder_dir).expanduser()
  info_path = builder_dir / constants.DATASET_INFO_FILENAME
  return read_from_json(info_path)


def read_full_proto_from_builder_dir(
    builder_dir: epath.PathLike,
) -> dataset_info_pb2.DatasetInfo:
  """Reads the dataset info from the given builder dir.

  Also reads data from the features files and puts it inside the dataset info.

  Args:
    builder_dir: The folder that contains the dataset info files.

  Returns:
    The DatasetInfo proto including feature information as read from the builder
    dir.

  Raises:
    FileNotFoundError: If the builder_dir does not exist or it doesn't contain
    dataset_info.json.
  """
  builder_dir = epath.Path(builder_dir).expanduser()
  info_path = builder_dir / constants.DATASET_INFO_FILENAME
  info_proto = read_from_json(info_path)
  if not info_proto.HasField("features"):
    try:
      features = feature_lib.FeatureConnector.from_config(
          os.fspath(builder_dir)
      )
      info_proto.features.CopyFrom(features.to_proto())
    except IOError:
      logging.warning("Could not read features from %s", builder_dir)
  return info_proto


def pack_as_supervised_ds(
    ds: tf.data.Dataset,
    ds_info: DatasetInfo,
) -> tf.data.Dataset:
  """Pack `(input, label)` dataset as `{'key0': input, 'key1': label}`."""
  if (
      ds_info.supervised_keys
      and isinstance(ds.element_spec, tuple)
      and len(ds.element_spec) == 2
  ):
    x_key, y_key = ds_info.supervised_keys  # pytype: disable=bad-unpacking
    ds = ds.map(lambda x, y: {x_key: x, y_key: y})
    return ds
  else:  # If dataset isn't a supervised tuple (input, label), return as-is
    return ds


def _metadata_filepath(data_dir: epath.PathLike) -> epath.Path:
  return epath.Path(data_dir) / constants.METADATA_FILENAME


def _now_in_milliseconds() -> int:
  return time.time_ns() // 1000000


def _create_redistribution_info_proto(
    license: str | None = None,  # pylint: disable=redefined-builtin
    redistribution_info: dict[str, str] | None = None,
) -> dataset_info_pb2.RedistributionInfo | None:
  """Returns a consistent redistribution info.

  Note that the license can be specified in both `license` and in
  `redistribution_info`. Please prefer the `license` field.

  Arguments:
    license: the license of a dataset.
    redistribution_info: mapping of other information about redistribution. Can
      contain `license` as well.

  Returns:
    consistent redistribution info or `None` when no info is specified.
  """
  redistribution_info = redistribution_info or {}

  if "license" in redistribution_info:
    redistribution_info_license = redistribution_info.pop("license")
    # Make sure `license` and `redistribution_info_license` are the same.
    if license is not None and license != redistribution_info_license:
      raise ValueError(
          f"License specified twice and inconsistently: {license=} and"
          f" {redistribution_info_license=}"
      )
    license = redistribution_info_license

  if redistribution_info:
    raise ValueError(
        "`redistribution_info` contains unsupported keys:"
        f" {redistribution_info.keys()}"
    )

  if license is not None:
    return dataset_info_pb2.RedistributionInfo(
        license=utils.dedent(str(license))
    )
  return None


def update_info_proto_with_features(
    info_proto: dataset_info_pb2.DatasetInfo,
    features: feature_lib.FeatureConnector,
) -> dataset_info_pb2.DatasetInfo:
  """Update the info proto with the given features, if any.

  Args:
    info_proto: the info proto to update.
    features: the features to use.

  Returns:
    the updated info proto.
  """
  completed_info_proto = dataset_info_pb2.DatasetInfo()
  completed_info_proto.CopyFrom(info_proto)
  completed_info_proto.features.CopyFrom(features.to_proto())
  return completed_info_proto


def available_file_formats(
    dataset_info_proto: dataset_info_pb2.DatasetInfo,
) -> set[str]:
  """Returns the available file formats for the given dataset."""
  return set(
      [dataset_info_proto.file_format]
      + list(dataset_info_proto.alternative_file_formats)
  )


def supports_file_format(
    dataset_info_proto: dataset_info_pb2.DatasetInfo,
    file_format: str | file_adapters.FileFormat,
) -> bool:
  """Returns whether the given file format is supported by the dataset."""
  if isinstance(file_format, file_adapters.FileFormat):
    file_format = file_format.value
  return file_format in available_file_formats(dataset_info_proto)


def get_split_dict_from_proto(
    dataset_info_proto: dataset_info_pb2.DatasetInfo,
    data_dir: epath.PathLike,
    file_format: str | file_adapters.FileFormat | None = None,
) -> splits_lib.SplitDict:
  """Returns the split dict with all split infos from the given dataset.

  Args:
    dataset_info_proto: the proto with the dataset info and split infos.
    data_dir: the directory where the data is stored.
    file_format: the file format for which to get the split dict. If the file
      format is not specified, the file format from the dataset info proto is
      used.
  """
  if file_format:
    file_format = file_adapters.FileFormat(file_format)
  else:
    file_format = file_adapters.FileFormat(dataset_info_proto.file_format)

  filename_template = naming.ShardedFileTemplate(
      dataset_name=dataset_info_proto.name,
      data_dir=epath.Path(data_dir),
      filetype_suffix=file_format.file_suffix,
  )
  return splits_lib.SplitDict.from_proto(
      repeated_split_infos=dataset_info_proto.splits,
      filename_template=filename_template,
  )


def get_split_info_from_proto(
    dataset_info_proto: dataset_info_pb2.DatasetInfo,
    split_name: str,
    data_dir: epath.PathLike,
    file_format: file_adapters.FileFormat,
) -> splits_lib.SplitInfo | None:
  """Returns split info from the given dataset info proto.

  Args:
    dataset_info_proto: the proto with the dataset info.
    split_name: the split for which to retrieve info for.
    data_dir: the directory where the data is stored.
    file_format: the file format for which to get the split info.
  """
  if not supports_file_format(dataset_info_proto, file_format):
    available_format = available_file_formats(dataset_info_proto)
    raise ValueError(
        f"File format {file_format.value} does not match available dataset file"
        f" formats: {sorted(available_format)}."
    )

  splits_dict = get_split_dict_from_proto(
      dataset_info_proto=dataset_info_proto,
      data_dir=data_dir,
      file_format=file_format,
  )
  return splits_dict.get(split_name)


def add_tfds_data_source_access(
    dataset_info_proto: dataset_info_pb2.DatasetInfo,
    dataset_reference: naming.DatasetReference,
    url: str | None = None,
) -> None:
  """Records that the given query was used to generate this dataset.

  Args:
    dataset_info_proto: the proto with the dataset info to update.
    dataset_reference: the dataset reference to record.
    url: a URL referring to the TFDS dataset.
  """
  dataset_info_proto.data_source_accesses.append(
      dataset_info_pb2.DataSourceAccess(
          access_timestamp_ms=_now_in_milliseconds(),
          tfds_dataset=dataset_info_pb2.TfdsDatasetReference(
              name=dataset_reference.dataset_name,
              config=dataset_reference.config,
              version=str(dataset_reference.version),
              data_dir=os.fspath(dataset_reference.data_dir),
              ds_namespace=dataset_reference.namespace,
          ),
          url=dataset_info_pb2.Url(url=url),
      )
  )


class MetadataDict(Metadata, dict):
  """A `tfds.core.Metadata` object that acts as a `dict`.

  By default, the metadata will be serialized as JSON.
  """

  def save_metadata(self, data_dir):
    """Save the metadata."""
    with _metadata_filepath(data_dir).open(mode="w") as f:
      json.dump(self, f)

  def load_metadata(self, data_dir):
    """Restore the metadata."""
    self.clear()
    with _metadata_filepath(data_dir).open(mode="r") as f:
      self.update(json.load(f))


class BeamMetadataDict(MetadataDict):
  """A `tfds.core.Metadata` object supporting Beam-generated datasets."""

  def __init__(self, *args, **kwargs):
    super(BeamMetadataDict, self).__init__(*args, **kwargs)
    self._tempdir = epath.Path(tempfile.mkdtemp("tfds_beam_metadata"))

  def _temp_filepath(self, key) -> epath.Path:
    return self._tempdir / f"{key}.json"

  def __setitem__(self, key, item):
    """Creates write sink for beam PValues or sets value of key in `dict`.

    If the item is a PValue, it is expected to contain exactly one element,
    which will be written out as a temporary JSON file once the beam pipeline
    runs. These outputs will be loaded and stored in a single JSON when
    `save_metadata` is called after the pipeline completes.

    Args:
      key: hashable type, the key for the item.
      item: `beam.pvalue.PValue` or other, the metadata value.
    """
    if isinstance(item, beam.PTransform):
      # Implementing Beam support might be possible but would
      # require very careful implementation to avoid computing the
      # PTransform twice (once for the split and once for the metadata).
      raise NotImplementedError(
          "`tfds.core.BeamMetadataDict` can't be used on `beam.PTransform`, "
          "only on `beam.PCollection`. See `_generate_examples` doc on how "
          "to use `beam.PCollection`, or wrap your `_generate_examples` inside "
          f"a @beam.ptransform_fn. Got: {key}: {item}"
      )
    elif isinstance(item, beam.pvalue.PValue):
      if key in self:
        raise ValueError("Already added PValue with key: %s" % key)
      logging.info("Lazily adding metadata item with Beam: %s", key)

      def _to_json(item_list):
        if len(item_list) != 1:
          raise ValueError(
              "Each metadata PValue must contain a single element. Got %d."
              % len(item_list)
          )
        item = item_list[0]
        return json.dumps(item)

      _ = (
          item
          | "metadata_%s_tolist" % key >> beam.combiners.ToList()
          | "metadata_%s_tojson" % key >> beam.Map(_to_json)
          | "metadata_%s_write" % key
          >> beam.io.WriteToText(
              os.fspath(self._temp_filepath(key)),
              num_shards=1,
              shard_name_template="",
          )
      )
    super(BeamMetadataDict, self).__setitem__(key, item)

  def save_metadata(self, data_dir):
    """Save the metadata inside the beam job."""
    for key, item in self.items():
      if isinstance(item, beam.pvalue.PValue):
        with self._temp_filepath(key).open(mode="r") as f:
          self[key] = json.load(f)
    self._tempdir.rmtree()
    super(BeamMetadataDict, self).save_metadata(data_dir)
