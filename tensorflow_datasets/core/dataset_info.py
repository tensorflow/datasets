# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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
 - number of records (in each split)
 - feature statistics (in each split)
 - etc.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import os
import numpy as np
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core.proto import dataset_info_pb2
from google.protobuf import json_format
from tensorflow_metadata.proto.v0 import schema_pb2
from tensorflow_metadata.proto.v0 import statistics_pb2


__all__ = [
    "DatasetInfo",
]

# Name of the file to output the DatasetInfo protobuf object.
DATASET_INFO_FILENAME = "dataset_info.json"


# TODO(tfds): Do we require to warn the user about the peak memory used while
# constructing the dataset?
class DatasetInfo(object):
  """Structure defining the info of the dataset.

  Information on the datasets are available through the builder.info property.
  Properties:
    name: `str`, name of this dataset.
    description: `str`, description of this dataset.
    features: `tfds.features.FeaturesDict`: Information on the feature dict of
      the `tf.data.Dataset` object from the `builder.as_dataset()` method.
    splits: `SplitDict`, the available Splits for this dataset.
    urls: `list(str)`, the homepage(s) for this dataset.
    size_in_bytes: `integer`, approximate size in bytes of the raw size of the
      dataset that we will be downloading from the internet.
    num_examples: `integer`, number of examples across all splits.
    examples_per_split: `dict(string, integer)`, number of examples per split.

  Note that some of those fields are dynamically computed at data generation
  time, and updated by `compute_dynamic_properties`.

  """

  @api_utils.disallow_positional_args
  def __init__(self,
               name=None,
               description=None,
               features=None,
               supervised_keys=None,
               splits=None,
               urls=None,
               size_in_bytes=0,
               citation=None):
    """Constructor of the DatasetInfo.

    Args:
      name: (`str`) Name of the dataset, usually set to builder.name.
      description: `str`, description of this dataset.
      features: (`tfds.features.FeaturesDict`) Information on the feature dict
        of the `tf.data.Dataset()` object from the `builder.as_dataset()`
        method.
      supervised_keys: (`tuple`) Specifies the input feature and the label for
        supervised learning, if applicable for the dataset.
      splits: `SplitDict`, the available Splits for this dataset.
      urls: `list(str)`, optional, the homepage(s) for this dataset.
      size_in_bytes: `integer`, optional, approximate size in bytes of the raw
        size of the dataset that we will be downloading from the internet.
      citation: `str`, optional, the citation to use for this dataset.
    """
    self._info_proto = dataset_info_pb2.DatasetInfo(
        name=name,
        description=description,
        size_in_bytes=int(size_in_bytes),
        citation=citation)
    if urls:
      self._info_proto.location.urls[:] = urls

    self._features = features
    self._splits = splits or splits_lib.SplitDict()
    if supervised_keys is not None:
      assert isinstance(supervised_keys, tuple)
      assert len(supervised_keys) == 2
      self._info_proto.supervised_keys.input = supervised_keys[0]
      self._info_proto.supervised_keys.output = supervised_keys[1]

    # Is this object initialized with both the static and the dynamic data?
    self._fully_initialized = False

  @property
  def as_proto(self):
    return self._info_proto

  @property
  def name(self):
    return self._info_proto.name

  @property
  def description(self):
    return self._info_proto.description

  @property
  def citation(self):
    return self._info_proto.citation

  @property
  def features(self):
    return self._features

  @property
  def supervised_keys(self):
    if not self._info_proto.HasField("supervised_keys"):
      return None
    supervised_keys = self._info_proto.supervised_keys
    return (supervised_keys.input, supervised_keys.output)

  @property
  def splits(self):
    if not self._fully_initialized:
      # TODO(epot): Consider raising an error here instead?
      tf.logging.info("`splits` hasn't been fully initialized, statistics maybe"
                      " missing.")
    return self._splits

  @splits.setter
  def splits(self, split_dict):
    assert isinstance(split_dict, splits_lib.SplitDict)

    # Update the dictionary representation.
    self._splits = split_dict

    # Update the proto representation.
    for split_info in self._splits.to_proto():
      self._info_proto.splits.add().CopyFrom(split_info)

  @property
  def urls(self):
    return self._info_proto.location.urls

  @property
  def size_in_bytes(self):
    return self._info_proto.size_in_bytes

  @property
  def num_examples(self):
    return sum(self.examples_per_split().values())

  @property
  def initialized(self):
    return self._fully_initialized

  # TODO(epot): Wrap SplitInfo into a class and expose num_samples.
  def examples_per_split(self):
    """Returns a dict of split name and number of samples."""
    if not self._fully_initialized:
      raise tf.errors.FailedPreconditionError(
          "Please call `compute_dynamic_properties` first to initialize the"
          " dynamic properties in DatasetInfo.")

    examples_per_split = {}
    for split_info in self._info_proto.splits:
      examples_per_split[split_info.name] = split_info.statistics.num_examples

    return examples_per_split

  def _dataset_info_filename(self, dataset_info_dir):
    return os.path.join(dataset_info_dir, DATASET_INFO_FILENAME)

  def write_to_directory(self, dataset_info_dir):
    with tf.gfile.Open(self._dataset_info_filename(dataset_info_dir), "w") as f:
      f.write(json_format.MessageToJson(self._info_proto))

  def compute_dynamic_properties(self, builder):
    update_dataset_info(builder, self.as_proto)
    self._fully_initialized = True

  def read_from_directory(self, dataset_info_dir):
    """Update the DatasetInfo properties from the metadata file.

    This function updates all the dynamically generated fields (num_samples,
    hash, time of creation,...) of the DatasetInfo. This reads the metadata
    file on the dataset directory to extract the info and expose them.
    This function is called after the data has been generated in
    .download_and_prepare() and when the data is loaded and already exists.

    This will overwrite all previous metadata.

    Args:
      dataset_info_dir: `str` The directory containing the metadata file. This
        should be the root directory of a specific dataset version.
    """
    if not dataset_info_dir:
      raise ValueError(
          "Calling read_from_directory with undefined dataset_info_dir.")

    json_filename = self._dataset_info_filename(dataset_info_dir)

    # Load the metadata from disk
    if not tf.gfile.Exists(json_filename):
      return

    with tf.gfile.Open(json_filename, "r") as f:
      dataset_info_json_str = f.read()

    # Parse it back into a proto.
    self._info_proto = json_format.Parse(dataset_info_json_str,
                                         dataset_info_pb2.DatasetInfo())

    # Restore the Splits
    self._splits = splits_lib.SplitDict.from_proto(self._info_proto.splits)

    # Mark as fully initialized.
    self._fully_initialized = True


#
#
# This part is quite a bit messy and can be easily simplified with TFDV
# libraries, we can cut down the complexity by implementing cases on a need to
# do basis.
#
# My understanding of possible TF's types and shapes and kinds
# (ex: SparseTensor) is limited, please shout hard and guide on implementation.
#
#

_FEATURE_TYPE_MAP = {
    tf.uint8: schema_pb2.INT,
    tf.int64: schema_pb2.INT,
    tf.float32: schema_pb2.FLOAT,
    tf.float16: schema_pb2.FLOAT,
    tf.float64: schema_pb2.FLOAT,
    tf.int8: schema_pb2.INT,
    tf.int16: schema_pb2.INT,
    tf.int32: schema_pb2.INT,
    tf.int64: schema_pb2.INT,
    tf.uint8: schema_pb2.INT,
    tf.uint16: schema_pb2.INT,
    tf.uint32: schema_pb2.INT,
    tf.uint64: schema_pb2.INT,
}

_SCHEMA_TYPE_MAP = {
    schema_pb2.INT: statistics_pb2.FeatureNameStatistics.INT,
    schema_pb2.FLOAT: statistics_pb2.FeatureNameStatistics.FLOAT,
    schema_pb2.BYTES: statistics_pb2.FeatureNameStatistics.BYTES,
    schema_pb2.STRUCT: statistics_pb2.FeatureNameStatistics.STRUCT,
}


# TODO(afrozm): What follows below can *VERY EASILY* be done by TFDV - rewrite
# this section once they are python 3 ready.
def get_dataset_feature_statistics(builder, split):
  """Calculate statistics for the specified split."""
  statistics = statistics_pb2.DatasetFeatureStatistics()

  # Make this to the best of our abilities.
  schema = schema_pb2.Schema()

  dataset = builder.as_dataset(split=split)

  # Just computing the number of examples for now.
  statistics.num_examples = 0

  # Feature dictionaries.
  feature_to_shape = {}
  feature_to_dtype = {}
  feature_to_num_examples = collections.defaultdict(int)
  feature_to_min = {}
  feature_to_max = {}

  for example in dataset:
    statistics.num_examples += 1

    assert isinstance(example, dict)

    feature_names = example.keys()
    for feature_name in feature_names:

      # Update the number of examples this feature appears in.
      feature_to_num_examples[feature_name] += 1

      feature_shape = example[feature_name].shape
      feature_dtype = example[feature_name].dtype
      feature_np = example[feature_name].numpy()

      feature_min, feature_max = None, None
      is_numeric = (
          feature_dtype.is_floating or feature_dtype.is_integer or
          feature_dtype.is_bool)
      if is_numeric:
        feature_min = np.min(feature_np)
        feature_max = np.max(feature_np)

      # TODO(afrozm): What if shapes don't match? Populate ValueCount? Add
      # logic for that.

      # Set the shape, or assert shapes match.
      if feature_name not in feature_to_shape:
        feature_to_shape[feature_name] = feature_shape
      else:
        assert feature_to_shape[feature_name] == feature_shape

      # Set the shape, or assert shapes match.
      if feature_name not in feature_to_dtype:
        feature_to_dtype[feature_name] = feature_dtype
      else:
        assert feature_to_dtype[feature_name] == feature_dtype

      # Set or update the min, max.
      if is_numeric:
        if ((feature_name not in feature_to_min) or
            (feature_to_min[feature_name] > feature_min)):
          feature_to_min[feature_name] = feature_min

        if ((feature_name not in feature_to_max) or
            (feature_to_max[feature_name] < feature_max)):
          feature_to_max[feature_name] = feature_max

  # Start here, we've processed all examples.

  # Assert that the keys match up.
  assert feature_to_shape.keys() == feature_to_dtype.keys()
  assert feature_to_shape.keys() == feature_to_num_examples.keys()

  for feature_name in feature_to_shape:
    # Try to fill in the schema.
    feature = schema.feature.add()
    feature.name = feature_name

    # TODO(afrozm): What do we do for non fixed size shapes?
    # What to do for scalars?
    for dim in feature_to_shape[feature_name].as_list():
      feature.shape.dim.add().size = dim
    feature_type = feature_to_dtype[feature_name]
    feature.type = _FEATURE_TYPE_MAP.get(feature_type, schema_pb2.BYTES)

    common_statistics = statistics_pb2.CommonStatistics()
    common_statistics.num_non_missing = feature_to_num_examples[feature_name]
    common_statistics.num_missing = (
        statistics.num_examples - common_statistics.num_non_missing)

    feature_name_statistics = statistics.features.add()
    feature_name_statistics.name = feature_name

    # TODO(afrozm): This can be skipped, since type information was added to
    # the Schema.
    feature_name_statistics.type = _SCHEMA_TYPE_MAP.get(
        feature.type, statistics_pb2.FeatureNameStatistics.BYTES)

    if feature.type == schema_pb2.INT or feature.type == schema_pb2.FLOAT:
      numeric_statistics = statistics_pb2.NumericStatistics()
      numeric_statistics.min = feature_to_min[feature_name]
      numeric_statistics.max = feature_to_max[feature_name]
      numeric_statistics.common_stats.CopyFrom(common_statistics)
      feature_name_statistics.num_stats.CopyFrom(numeric_statistics)
    else:
      # Let's shove it into BytesStatistics for now.
      bytes_statistics = statistics_pb2.BytesStatistics()
      bytes_statistics.common_stats.CopyFrom(common_statistics)
      feature_name_statistics.bytes_stats.CopyFrom(bytes_statistics)

  return statistics, schema


def update_dataset_info(builder, info):
  """Fill statistics in `info` by going over the dataset in the `builder`."""
  # Fill other things by going over the dataset.
  for split_info in info.splits:
    try:
      split_name = split_info.name
      # Fill DatasetFeatureStatistics.
      dataset_feature_statistics, schema = get_dataset_feature_statistics(
          builder, split_name)

      # Add the statistics to this split.
      split_info.statistics.CopyFrom(dataset_feature_statistics)

      # Set the schema at the top-level since this is independent of the split.
      info.schema.CopyFrom(schema)

    except tf.errors.InvalidArgumentError as e:
      # This means there is no such split, even though it was specified in the
      # info, the least we can do is to log this.
      raise tf.errors.InvalidArgumentError(
          "%s's info() property specifies split %s, but it "
          "doesn't seem to have been generated. Please ensure "
          "that the data was downloaded for this split and re-run "
          "download_and_prepare. Original eror is [%s]" % (info.name,
                                                           split_name, str(e)))
