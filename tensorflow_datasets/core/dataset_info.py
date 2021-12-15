# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

import abc
import json
import os
import posixpath
import tempfile
from typing import Dict, Optional, Tuple, Union

from absl import logging
import six
import tensorflow as tf

from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.features import feature as feature_lib
from tensorflow_datasets.core.features import top_level_feature
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.core.utils import gcs_utils
from tensorflow_datasets.core.utils import type_utils

from google.protobuf import json_format

# TODO(b/109648354): Remove the "pytype: disable" comment.
Nest = Union[Tuple["Nest", ...], Dict[str, "Nest"], str]  # pytype: disable=not-supported-yet
SupervisedKeysType = Union[Tuple[Nest, Nest], Tuple[Nest, Nest, Nest]]

# Name of the file to output the DatasetInfo protobuf object.
DATASET_INFO_FILENAME = "dataset_info.json"
LICENSE_FILENAME = "LICENSE"
METADATA_FILENAME = "metadata.json"


@six.add_metaclass(abc.ABCMeta)
class Metadata(dict):
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


class DatasetInfo(object):
  """Information about a dataset.

  `DatasetInfo` documents datasets, including its name, version, and features.
  See the constructor arguments and properties for a full list.

  Note: Not all fields are known if the dataset hasn't been generated yet
  (before the first `builder.download_and_prepare()` call). For example splits
  names or number of examples might be missing (as they are computed
  at dataset creation time).

  """

  def __init__(
      self,
      *,
      builder,
      description: Optional[str] = None,
      features: Optional[feature_lib.FeatureConnector] = None,
      supervised_keys: Optional[SupervisedKeysType] = None,
      disable_shuffling: bool = False,
      homepage: Optional[str] = None,
      citation: Optional[str] = None,
      metadata: Optional[Metadata] = None,
      license: Optional[str] = None,  # pylint: disable=redefined-builtin
      redistribution_info: Optional[Dict[str, str]] = None):
    """Constructs DatasetInfo.

    Args:
      builder: `DatasetBuilder`, dataset builder for this info.
      description: `str`, description of this dataset.
      features: `tfds.features.FeaturesDict`, Information on the feature dict of
        the `tf.data.Dataset()` object from the `builder.as_dataset()` method.
      supervised_keys: Specifies the input structure for supervised learning,
        if applicable for the dataset, used with "as_supervised". The keys
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
    """
    self._builder = builder

    if builder.builder_config:
      config_name = builder.builder_config.name
      config_description = builder.builder_config.description
    else:
      config_name = None
      config_description = None

    self._info_proto = dataset_info_pb2.DatasetInfo(
        name=builder.name,
        description=utils.dedent(description),
        version=str(builder.version),
        release_notes=builder.release_notes,
        disable_shuffling=disable_shuffling,
        config_name=config_name,
        config_description=config_description,
        citation=utils.dedent(citation),
        module_name=str(builder.__module__),
        redistribution_info=dataset_info_pb2.RedistributionInfo(
            license=utils.dedent(license or redistribution_info.pop("license")),
            **redistribution_info) if redistribution_info else None)

    if homepage:
      self._info_proto.location.urls[:] = [homepage]

    if features:
      if not isinstance(features, top_level_feature.TopLevelFeature):
        raise ValueError(
            "DatasetInfo.features only supports FeaturesDict or Sequence at "
            "the top-level. Got {}".format(features))
    self._features = features
    self._splits = splits_lib.SplitDict([], dataset_name=self._builder.name)
    if supervised_keys is not None:
      self._info_proto.supervised_keys.CopyFrom(
          _supervised_keys_to_proto(supervised_keys))

    if metadata and not isinstance(metadata, Metadata):
      raise ValueError(
          "Metadata should be a `tfds.core.Metadata` instance. Received "
          "{}".format(metadata))
    self._metadata = metadata

    # Is this object initialized with both the static and the dynamic data?
    self._fully_initialized = False

  @classmethod
  def from_proto(cls, builder,
                 proto: dataset_info_pb2.DatasetInfo) -> "DatasetInfo":
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
    return cls(
        builder=builder,
        description=proto.description,
        features=features,
        supervised_keys=supervised_keys,
        disable_shuffling=proto.disable_shuffling,
        citation=proto.citation,
        license=proto.redistribution_info.license,
    )

  @property
  def as_proto(self) -> dataset_info_pb2.DatasetInfo:
    return self._info_proto

  @property
  def name(self) -> str:
    return self.as_proto.name

  @property
  def config_name(self) -> str:
    return self.as_proto.config_name

  @property
  def full_name(self):
    """Full canonical name: (<dataset_name>/<config_name>/<version>)."""
    names = [self._builder.name]
    if self._builder.builder_config:
      names.append(self._builder.builder_config.name)
    names.append(str(self.version))
    return posixpath.join(*names)

  @property
  def description(self):
    return self.as_proto.description

  @property
  def version(self):
    return self._builder.version

  @property
  def release_notes(self) -> Optional[Dict[str, str]]:
    return self._builder.release_notes

  @property
  def disable_shuffling(self) -> bool:
    return self.as_proto.disable_shuffling

  @property
  def homepage(self):
    urls = self.as_proto.location.urls
    tfds_homepage = f"https://www.tensorflow.org/datasets/catalog/{self.name}"
    return urls and urls[0] or tfds_homepage

  @property
  def citation(self):
    return self.as_proto.citation

  @property
  def data_dir(self):
    return self._builder.data_dir

  @property
  def dataset_size(self) -> utils.Size:
    """Generated dataset files size, in bytes."""
    # For old datasets, maybe empty.
    return utils.Size(sum(split.num_bytes for split in self.splits.values()))

  @property
  def download_size(self) -> utils.Size:
    """Downloaded files size, in bytes."""
    # Fallback to deprecated `size_in_bytes` if `download_size` is empty.
    return utils.Size(self.as_proto.download_size or
                      self.as_proto.size_in_bytes)

  @download_size.setter
  def download_size(self, size):
    self.as_proto.download_size = size

  @property
  def features(self):
    return self._features

  @property
  def metadata(self):
    return self._metadata

  @property
  def supervised_keys(self):
    if not self.as_proto.HasField("supervised_keys"):
      return None
    supervised_keys = self.as_proto.supervised_keys
    return _supervised_keys_from_proto(supervised_keys)

  @property
  def redistribution_info(self):
    return self.as_proto.redistribution_info

  @property
  def module_name(self):
    return self.as_proto.module_name

  @property
  def file_format(self) -> Optional[file_adapters.FileFormat]:
    if not self.as_proto.file_format:
      return None
    return file_adapters.FileFormat(self.as_proto.file_format)

  def set_file_format(
      self,
      file_format: Union[None, str, file_adapters.FileFormat],
  ) -> None:
    """Internal function to define the file format.

    The file format is set during `FileReaderBuilder.__init__`,
    not `DatasetInfo.__init__`.

    Args:
      file_format: The file format.
    """
    # If file format isn't present already, fallback to `DEFAULT_FILE_FORMAT`
    file_format = (
        file_format  # Format explicitly given: tfds.builder(..., file_format=x)
        or self.file_format  # Format restored from dataset_info.json
        or file_adapters.DEFAULT_FILE_FORMAT)
    try:
      new_file_format = file_adapters.FileFormat(file_format)
    except ValueError as e:
      all_values = [f.value for f in file_adapters.FileFormat]
      utils.reraise(e, suffix=f". Valid file formats: {all_values}")

    # If the file format has been set once, file format should be consistent
    if self.file_format and self.file_format != new_file_format:
      raise ValueError(f"File format is already set to {self.file_format}. "
                       f"Got {new_file_format}")
    self.as_proto.file_format = new_file_format.value

  @property
  def splits(self):
    return self._splits

  def set_splits(self, split_dict: splits_lib.SplitDict) -> None:
    """Split setter (private method)."""
    if self._builder.name != split_dict._dataset_name:  # pylint: disable=protected-access
      raise AssertionError(
          "SplitDict dataset_name does not seems to match dataset_info. "  # pylint: disable=protected-access
          f"{self._builder.name} != {split_dict._dataset_name}")

    # If the statistics have been pre-loaded, forward the statistics
    # into the new split_dict
    new_split_infos = []
    for split_info in split_dict.values():
      old_split_info = self._splits.get(split_info.name)
      if (not split_info.statistics.ByteSize() and old_split_info and
          old_split_info.statistics.ByteSize() and
          old_split_info.shard_lengths == split_info.shard_lengths):
        split_info = split_info.replace(statistics=old_split_info.statistics)
      new_split_infos.append(split_info)

    # Update the dictionary representation.
    self._splits = splits_lib.SplitDict(
        new_split_infos,
        dataset_name=self._builder.name,
    )

    # Update the proto
    del self.as_proto.splits[:]  # Clear previous
    for split_info in split_dict.to_proto():
      self.as_proto.splits.add().CopyFrom(split_info)

  @property
  def initialized(self):
    """Whether DatasetInfo has been fully initialized."""
    return self._fully_initialized

  def _dataset_info_path(self, dataset_info_dir):
    return os.path.join(dataset_info_dir, DATASET_INFO_FILENAME)

  def _license_path(self, dataset_info_dir):
    return os.path.join(dataset_info_dir, LICENSE_FILENAME)

  @property
  def as_json(self):
    return json_format.MessageToJson(self.as_proto, sort_keys=True)

  def write_to_directory(self, dataset_info_dir):
    """Write `DatasetInfo` as JSON to `dataset_info_dir`."""
    # Save the features structure & metadata (vocabulary, labels,...)
    if self.features:
      self.features.save_config(dataset_info_dir)

    # Save any additional metadata
    if self.metadata is not None:
      self.metadata.save_metadata(dataset_info_dir)

    if self.redistribution_info.license:
      with tf.io.gfile.GFile(self._license_path(dataset_info_dir), "w") as f:
        f.write(self.redistribution_info.license)

    with tf.io.gfile.GFile(self._dataset_info_path(dataset_info_dir), "w") as f:
      f.write(self.as_json)

  def read_from_directory(self, dataset_info_dir):
    """Update DatasetInfo from the JSON files in `dataset_info_dir`.

    This function updates all the dynamically generated fields (num_examples,
    hash, time of creation,...) of the DatasetInfo.

    This will overwrite all previous metadata.

    Args:
      dataset_info_dir: `str` The directory containing the metadata file. This
        should be the root directory of a specific dataset version.

    Raises:
      FileNotFoundError: If the dataset_info.json can't be found.
    """
    logging.info("Load dataset info from %s", dataset_info_dir)

    json_filename = self._dataset_info_path(dataset_info_dir)
    if not tf.io.gfile.exists(json_filename):
      raise FileNotFoundError(
          "Try to load `DatasetInfo` from a directory which does not exist or "
          "does not contain `dataset_info.json`. Please delete the directory "
          f"`{dataset_info_dir}`  if you are trying to re-generate the "
          "dataset.")

    # Load the metadata from disk
    parsed_proto = read_from_json(json_filename)

    # Update splits
    split_dict = splits_lib.SplitDict.from_proto(self.name, parsed_proto.splits)
    self.set_splits(split_dict)

    # Restore the feature metadata (vocabulary, labels names,...)
    if self.features:
      self.features.load_metadata(dataset_info_dir)
    # For `ReadOnlyBuilder`, reconstruct the features from the config.
    elif tf.io.gfile.exists(feature_lib.make_config_path(dataset_info_dir)):
      self._features = feature_lib.FeatureConnector.from_config(
          dataset_info_dir)
    # Restore the MetaDataDict from metadata.json if there is any
    if (self.metadata is not None or
        tf.io.gfile.exists(_metadata_filepath(dataset_info_dir))):
      # If the dataset was loaded from file, self.metadata will be `None`, so
      # we create a MetadataDict first.
      if self.metadata is None:
        self._metadata = MetadataDict()
      self.metadata.load_metadata(dataset_info_dir)

    # Update fields which are not defined in the code. This means that
    # the code will overwrite fields which are present in
    # dataset_info.json.
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

      # If field is defined in code, we ignore the value
      if is_defined:
        if field_value != field_value_restored:
          logging.info(
              "Field info.%s from disk and from code do not match. Keeping "
              "the one from code.", field_name)
        continue
      # If the field is also not defined in JSON file, we do nothing
      if not is_defined_in_restored:
        continue
      # Otherwise, we restore the dataset_info.json value
      if field.type == field.TYPE_MESSAGE:
        field_value.MergeFrom(field_value_restored)
      else:
        setattr(self._info_proto, field_name, field_value_restored)

    if self._builder._version != self.version:  # pylint: disable=protected-access
      raise AssertionError(
          "The constructed DatasetInfo instance and the restored proto version "
          "do not match. Builder version: {}. Proto version: {}".format(
              self._builder._version, self.version))  # pylint: disable=protected-access

    # Mark as fully initialized.
    self._fully_initialized = True

  def initialize_from_bucket(self):
    """Initialize DatasetInfo from GCS bucket info files."""
    # In order to support Colab, we use the HTTP GCS API to access the metadata
    # files. They are copied locally and then loaded.
    tmp_dir = tempfile.mkdtemp("tfds")
    data_files = gcs_utils.gcs_dataset_info_files(self.full_name)
    if not data_files:
      return
    logging.info(
        "Load pre-computed DatasetInfo (eg: splits, num examples,...) "
        "from GCS: %s", self.full_name)
    for fname in data_files:
      out_fname = os.path.join(tmp_dir, os.path.basename(fname))
      tf.io.gfile.copy(os.fspath(gcs_utils.gcs_path(fname)), out_fname)
    self.read_from_directory(tmp_dir)

  def __repr__(self):
    SKIP = object()  # pylint: disable=invalid-name

    splits = _indent("\n".join(
        ["{"] +
        [f"    '{k}': {split}," for k, split in sorted(self.splits.items())] +
        ["}"]))

    if self._info_proto.config_description:
      config_description = _indent(
          f'"""\n{self._info_proto.config_description}\n"""')
    else:
      config_description = SKIP

    lines = ["tfds.core.DatasetInfo("]
    for key, value in [
        ("name", repr(self.name)),
        ("full_name", repr(self.full_name)),
        ("description", _indent(f'"""\n{self.description}\n"""')),
        ("config_description", config_description),
        ("homepage", repr(self.homepage)),
        ("data_path", repr(self.data_dir)),
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
    raise ValueError("The nested structures in `supervised_keys` must only "
                     "contain instances of (tuple, dict, str), no subclasses.\n"
                     f"Found type: {nest_type}")

  return proto


def _supervised_keys_to_proto(
    keys: SupervisedKeysType) -> dataset_info_pb2.SupervisedKeys:
  """Converts a `supervised_keys` tuple to a SupervisedKeys proto."""
  if not isinstance(keys, tuple) or len(keys) not in [2, 3]:
    raise ValueError(
        "`supervised_keys` must contain a tuple of 2 or 3 elements.\n"
        f"got: {keys!r}")

  proto = dataset_info_pb2.SupervisedKeys(
      tuple=dataset_info_pb2.SupervisedKeys.Tuple(
          items=(_nest_to_proto(key) for key in keys)))
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
        key: _nest_from_proto(value) for key, value in proto.dict.dict.items()
    }
  elif proto.HasField("feature_key"):
    return proto.feature_key
  else:
    raise ValueError("`SupervisedKeys.Nest` proto must contain one of "
                     f"(tuple, dict, feature_key). Got: {proto}")


def _supervised_keys_from_proto(
    proto: dataset_info_pb2.SupervisedKeys) -> SupervisedKeysType:
  """Converts a `SupervisedKeys` proto back to a simple python tuple."""
  if proto.input and proto.output:
    return (proto.input, proto.output)
  elif proto.tuple:
    return tuple(_nest_from_proto(item) for item in proto.tuple.items)
  else:
    raise ValueError("A `SupervisedKeys` proto must have either `input` and "
                     "`output` defined, or `tuple`, got: {proto}")


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


def get_dataset_feature_statistics(builder, split):
  """Calculate statistics for the specified split."""
  tfdv = lazy_imports_lib.lazy_imports.tensorflow_data_validation
  # TODO(epot): Avoid hardcoding file format.
  filetype_suffix = "tfrecord"
  if filetype_suffix not in ["tfrecord", "csv"]:
    raise ValueError(
        "Cannot generate statistics for filetype {}".format(filetype_suffix))
  filepattern = naming.filepattern_for_dataset_split(builder.name, split,
                                                     builder.data_dir,
                                                     filetype_suffix)
  # Avoid generating a large number of buckets in rank histogram
  # (default is 1000).
  stats_options = tfdv.StatsOptions(
      num_top_values=10, num_rank_histogram_buckets=10)
  if filetype_suffix == "csv":
    statistics = tfdv.generate_statistics_from_csv(
        filepattern, stats_options=stats_options)
  else:
    statistics = tfdv.generate_statistics_from_tfrecord(
        filepattern, stats_options=stats_options)
  schema = tfdv.infer_schema(statistics)
  schema_features = {feature.name: feature for feature in schema.feature}
  # Override shape in the schema.
  for feature_name, feature in builder.info.features.items():
    _populate_shape(feature.shape, [feature_name], schema_features)

  # Remove legacy field.
  if getattr(schema, "generate_legacy_feature_spec", None) is not None:
    schema.ClearField("generate_legacy_feature_spec")
  return statistics.datasets[0], schema


def read_from_json(path: type_utils.PathLike) -> dataset_info_pb2.DatasetInfo:
  """Read JSON-formatted proto into DatasetInfo proto."""
  json_str = utils.as_path(path).read_text()
  # Parse it back into a proto.
  parsed_proto = json_format.Parse(json_str, dataset_info_pb2.DatasetInfo())
  return parsed_proto


def read_proto_from_builder_dir(
    builder_dir: type_utils.PathLike) -> dataset_info_pb2.DatasetInfo:
  """Reads the dataset info from the given builder dir.

  Args:
    builder_dir: The folder that contains the dataset info files.

  Returns:
    The DatasetInfo proto as read from the builder dir.

  Raises:
    FileNotFoundError: If the builder_dir does not exists.
  """
  info_path = os.path.join(
      os.path.expanduser(builder_dir), DATASET_INFO_FILENAME)
  if not tf.io.gfile.exists(info_path):
    raise FileNotFoundError(
        f"Could not load dataset info: {info_path} does not exists.")
  return read_from_json(info_path)


def pack_as_supervised_ds(
    ds: tf.data.Dataset,
    ds_info: DatasetInfo,
) -> tf.data.Dataset:
  """Pack `(input, label)` dataset as `{'key0': input, 'key1': label}`."""
  if (ds_info.supervised_keys and isinstance(ds.element_spec, tuple) and
      len(ds.element_spec) == 2):
    x_key, y_key = ds_info.supervised_keys
    ds = ds.map(lambda x, y: {x_key: x, y_key: y})
    return ds
  else:  # If dataset isn't a supervised tuple (input, label), return as-is
    return ds


def _metadata_filepath(data_dir):
  return os.path.join(data_dir, METADATA_FILENAME)


class MetadataDict(Metadata, dict):
  """A `tfds.core.Metadata` object that acts as a `dict`.

  By default, the metadata will be serialized as JSON.
  """

  def save_metadata(self, data_dir):
    """Save the metadata."""
    with tf.io.gfile.GFile(_metadata_filepath(data_dir), "w") as f:
      json.dump(self, f)

  def load_metadata(self, data_dir):
    """Restore the metadata."""
    self.clear()
    with tf.io.gfile.GFile(_metadata_filepath(data_dir), "r") as f:
      self.update(json.load(f))


class BeamMetadataDict(MetadataDict):
  """A `tfds.core.Metadata` object supporting Beam-generated datasets."""

  def __init__(self, *args, **kwargs):
    super(BeamMetadataDict, self).__init__(*args, **kwargs)
    self._tempdir = tempfile.mkdtemp("tfds_beam_metadata")

  def _temp_filepath(self, key):
    return os.path.join(self._tempdir, "%s.json" % key)

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
    beam = lazy_imports_lib.lazy_imports.apache_beam
    if isinstance(item, beam.PTransform):
      # Implementing Beam support might be possible but would
      # require very careful implementation to avoid computing the
      # PTransform twice (once for the split and once for the metadata).
      raise NotImplementedError(
          "`tfds.core.BeamMetadataDict` can\'t be used on `beam.PTransform`, "
          "only on `beam.PCollection`. See `_generate_examples` doc on how "
          "to use `beam.PCollection`, or wrap your `_generate_examples` inside "
          f"a @beam.ptransform_fn. Got: {key}: {item}")
    elif isinstance(item, beam.pvalue.PValue):
      if key in self:
        raise ValueError("Already added PValue with key: %s" % key)
      logging.info("Lazily adding metadata item with Beam: %s", key)

      def _to_json(item_list):
        if len(item_list) != 1:
          raise ValueError(
              "Each metadata PValue must contain a single element. Got %d." %
              len(item_list))
        item = item_list[0]
        return json.dumps(item)

      _ = (
          item
          | "metadata_%s_tolist" % key >> beam.combiners.ToList()
          | "metadata_%s_tojson" % key >> beam.Map(_to_json)
          | "metadata_%s_write" % key >> beam.io.WriteToText(
              self._temp_filepath(key),
              num_shards=1,
              shard_name_template="",
          ))
    super(BeamMetadataDict, self).__setitem__(key, item)

  def save_metadata(self, data_dir):
    """Save the metadata inside the beam job."""
    beam = lazy_imports_lib.lazy_imports.apache_beam
    for key, item in self.items():
      if isinstance(item, beam.pvalue.PValue):
        with tf.io.gfile.GFile(self._temp_filepath(key), "r") as f:
          self[key] = json.load(f)
    tf.io.gfile.rmtree(self._tempdir)
    super(BeamMetadataDict, self).save_metadata(data_dir)
