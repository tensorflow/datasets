"""Dataset statisitics util.
"""

import json
import os

from absl import logging
from google.protobuf import json_format
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import dataset_builder
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits as splits_lib
from tensorflow_datasets.core import utils


class StatisticsInfo:
  """Information about a dataset statisitics."""

  def __init__(self, info):
    self._info = info
    self._statistics_info_path = os.path.join(
        self._info.data_dir, "statistics.json")

  @property
  def statistics_info_path(self) -> str:
    return self._statistics_info_path

  def __bool__(self) -> bool:
    """Return True if statistics are present, false otherwise."""
    return tf.io.gfile.exists(self.statistics_info_path)

  def compute_and_save(self):
    """Compute and save dataset statistics info to statistics_info_path"""
    logging.info("Computing statistics.")

    self._info.compute_dynamic_properties()
    statistics = {
        "splits": [{
            "name": split_name,
            # TODO: Save only neccessary fields
            "statistics": json_format.MessageToDict(split.statistics)
        } for split_name, split in self._info.splits.items()]
    }
    with tf.io.gfile.GFile(self.statistics_info_path, "w") as f:
      f.write(json.dumps(statistics, indent=4))

  def compute_dynamic_properties(self, builder: dataset_builder.DatasetBuilder):
    """Update from the DatasetBuilder."""
    # Fill other things by going over the dataset.
    splits = self._info.splits
    for split_info in utils.tqdm(splits.values(),
                                 desc="Computing statistics...", unit=" split"):
      try:
        split_name = split_info.name
        # Fill DatasetFeatureStatistics.
        dataset_feature_statistics, schema = get_dataset_feature_statistics(
            builder, split_name)

        # Add the statistics to this split.
        split_info.statistics.CopyFrom(dataset_feature_statistics)

        # Set the schema at the top-level since this is independent of the
        # split.
        self._info.as_proto.schema.CopyFrom(schema)

      except tf.errors.InvalidArgumentError:
        # This means there is no such split, even though it was specified in the
        # info, the least we can do is to log this.
        logging.error(("%s's info() property specifies split %s, but it "
                       "doesn't seem to have been generated. Please ensure "
                       "that the data was downloaded for this split and re-run "
                       "download_and_prepare."), self._info.name, split_name)
        raise

    # Set splits to trigger proto update in setter
    self._info._set_splits(splits)  # pylint: disable = protected-access

  def _repr_html_(self):  # Display the FACET display
    pass


def get_dataset_feature_statistics(
    builder: dataset_builder.DatasetBuilder,
    split: splits_lib.SplitDict
):
  """Calculate statistics for the specified split."""
  tfdv = lazy_imports_lib.lazy_imports.tensorflow_data_validation
  # TODO(epot): Avoid hardcoding file format.
  filetype_suffix = "tfrecord"
  if filetype_suffix not in ["tfrecord", "csv"]:
    raise ValueError(
        "Cannot generate statistics for filetype {}".format(filetype_suffix))
  filepattern = naming.filepattern_for_dataset_split(
      builder.name, split, builder.data_dir, filetype_suffix)
  # Avoid generating a large number of buckets in rank histogram
  # (default is 1000).
  stats_options = tfdv.StatsOptions(num_top_values=10,
                                    num_rank_histogram_buckets=10)
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
