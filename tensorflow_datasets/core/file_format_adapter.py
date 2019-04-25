# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

"""`tfds.file_adapter.FileFormatAdapter`s for GeneratorBasedBuilder.

FileFormatAdapters implement methods to write and read data from a
particular file format.

Currently, a single FileAdapter is available:
 * TFRecordExampleAdapter: To store the pre-processed dataset as .tfrecord file

```python
return TFRecordExampleAdapter({
    "x": tf.FixedLenFeature(tuple(), tf.int64)
})
```

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import contextlib
import random
import string

from absl import logging
import numpy as np
import six
import tensorflow as tf

from tensorflow_datasets.core import lazy_imports
from tensorflow_datasets.core import utils


__all__ = [
    "FileFormatAdapter",
    "TFRecordExampleAdapter",
]


@six.add_metaclass(abc.ABCMeta)
class FileFormatAdapter(object):
  """Provides writing and reading methods for a file format."""

  @abc.abstractmethod
  def write_from_generator(self, generator_fn, output_files):
    """Write to files from generators_and_filenames.

    Args:
      generator_fn: returns generator yielding dictionaries of feature name to
        value.
      output_files: `list<str>`, output files to write files to.
    """
    raise NotImplementedError

  def write_from_pcollection(
      self, pcollection, file_path_prefix=None, num_shards=None):
    """Write the PCollection to file.

    Args:
      pcollection: `beam.PCollection`, the PCollection containing the examples
        to write.
      file_path_prefix: `str`, output files to write files to.
      num_shards: `int`,
    """
    # TODO(tfds): Should try to unify the write_from_generator signatures:
    # * Have the FileFormatAdapter to add the prefix when reading/writing
    raise NotImplementedError

  @abc.abstractmethod
  def dataset_from_filename(self, filename):
    """Returns a `tf.data.Dataset` whose elements are dicts given a filename."""
    raise NotImplementedError

  @abc.abstractproperty
  def filetype_suffix(self):
    """Returns a str file type suffix (e.g. "tfrecord")."""
    raise NotImplementedError


class TFRecordExampleAdapter(FileFormatAdapter):
  """Writes/Reads serialized Examples protos to/from TFRecord files.

  Constraints on generators:

  * The generator must yield feature dictionaries (`dict<str feature_name,
    feature_value>`).
  * The allowed feature types are `int`, `float`, and `str` (or `bytes` in
    Python 3; `unicode` strings will be encoded in `utf-8`), or lists thereof.
  """

  def __init__(self, example_reading_spec):
    """Constructs a TFRecordExampleAdapter.

    Args:
      example_reading_spec: `dict`, feature name to tf.FixedLenFeature or
        tf.VarLenFeature. Passed to tf.io.parse_single_example.
    """
    self._example_reading_spec = example_reading_spec

  def _serialize_record(self, record):
    return _dict_to_tf_example(record).SerializeToString()

  def write_from_generator(self, generator_fn, output_files):
    wrapped = (
        self._serialize_record(d) for d in generator_fn())
    _write_tfrecords_from_generator(wrapped, output_files, shuffle=True)

  def write_from_pcollection(self, pcollection, file_path_prefix, num_shards):
    beam = lazy_imports.lazy_imports.apache_beam

    # WARNING: WriteToTFRecord do not support long in python2 with the default,
    # beam implementation, so need to convert the long value (from the proto
    # field) into int, otherwise, the number of shards will be random.
    num_shards = int(num_shards)

    return (
        pcollection
        | "SerializeDict" >> beam.Map(self._serialize_record)
        | "Shuffle" >> beam.Reshuffle()
        | "WriteToExamples" >> beam.io.WriteToTFRecord(
            file_path_prefix=".".join([file_path_prefix, self.filetype_suffix]),
            num_shards=num_shards,
        )
    )

  def dataset_from_filename(self, filename):
    dataset = tf.data.TFRecordDataset(filename, buffer_size=int(16 * 1e6))
    return dataset.map(self._decode,
                       num_parallel_calls=tf.data.experimental.AUTOTUNE)

  def _decode(self, record):
    return tf.io.parse_single_example(
        serialized=record, features=self._example_reading_spec)

  @property
  def filetype_suffix(self):
    return "tfrecord"


class TFRecordSequenceExampleAdapter(TFRecordExampleAdapter):
  """Writes/Reads serialized SequenceExample protos to/from TFRecord files.

  Constraints on generators:

  * The generator must yield 2-tuples of (context, sequence), where context
    is a feature dictionary (`dict<str feature_name, feature_value>`), and
    sequence is a sequence feature dictionary
    (`dict<str feature_name, list<feature_value>>`).
  * The allowed feature types are `int`, `float`, and `str` (or `bytes` in
    Python 3; `unicode` strings will be encoded in `utf-8`), or lists thereof.
  """

  def __init__(self, context_reading_spec, sequence_reading_spec):  # pylint: disable=super-init-not-called
    """Constructs a TFRecordSequenceExampleAdapter.

    Args:
      context_reading_spec: `dict`, feature name to tf.FixedLenFeature or
        tf.VarLenFeature for the context features. Passed to
        tf.io.parse_single_sequence_example.
      sequence_reading_spec: `dict`, feature name to tf.FixedLenFeature or
        tf.VarLenFeature for the sequence features. Passed to
        tf.io.parse_single_sequence_example.
    """
    self._context_reading_spec = context_reading_spec
    self._sequence_reading_spec = sequence_reading_spec

  def _serialize_record(self, record):
    context, sequence = record
    return _dicts_to_tf_sequence_example(context, sequence).SerializeToString()

  def _decode(self, record):
    return tf.io.parse_single_sequence_example(
        serialized=record,
        context_features=self._context_reading_spec,
        sequence_features=self._sequence_reading_spec)


def do_files_exist(filenames):
  """Whether any of the filenames exist."""
  preexisting = [tf.io.gfile.exists(f) for f in filenames]
  return any(preexisting)


@contextlib.contextmanager
def _close_on_exit(handles):
  """Call close on all handles on exit."""
  try:
    yield handles
  finally:
    for handle in handles:
      handle.close()


def get_incomplete_path(filename):
  """Returns a temporary filename based on filename."""
  random_suffix = "".join(
      random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
  return filename + ".incomplete" + random_suffix


@contextlib.contextmanager
def _incomplete_files(filenames):
  """Create temporary files for filenames and rename on exit."""
  tmp_files = [get_incomplete_path(f) for f in filenames]
  try:
    yield tmp_files
    for tmp, output in zip(tmp_files, filenames):
      tf.io.gfile.rename(tmp, output)
  finally:
    for tmp in tmp_files:
      if tf.io.gfile.exists(tmp):
        tf.io.gfile.remove(tmp)


@contextlib.contextmanager
def incomplete_dir(dirname):
  """Create temporary dir for dirname and rename on exit."""
  tmp_dir = get_incomplete_path(dirname)
  tf.io.gfile.makedirs(tmp_dir)
  try:
    yield tmp_dir
    tf.io.gfile.rename(tmp_dir, dirname)
  finally:
    if tf.io.gfile.exists(tmp_dir):
      tf.io.gfile.rmtree(tmp_dir)


def _shuffle_tfrecord(path, random_gen):
  """Shuffle a single record file in memory."""
  # Read all records
  record_iter = tf.compat.v1.io.tf_record_iterator(path)
  all_records = [
      r for r in utils.tqdm(
          record_iter, desc="Reading...", unit=" examples", leave=False)
  ]
  # Shuffling in memory
  random_gen.shuffle(all_records)
  # Write all record back
  with tf.io.TFRecordWriter(path) as writer:
    for record in utils.tqdm(
        all_records, desc="Writing...", unit=" examples", leave=False):
      writer.write(record)


def _write_tfrecords_from_generator(generator, output_files, shuffle=True):
  """Writes generated str records to output_files in round-robin order."""
  if do_files_exist(output_files):
    raise ValueError(
        "Pre-processed files already exists: {}.".format(output_files))

  with _incomplete_files(output_files) as tmp_files:
    # Write all shards
    writers = [tf.io.TFRecordWriter(fname) for fname in tmp_files]
    with _close_on_exit(writers) as writers:
      logging.info("Writing TFRecords")
      _round_robin_write(writers, generator)
    # Shuffle each shard
    if shuffle:
      # WARNING: Using np instead of Python random because Python random
      # produce different values between Python 2 and 3 and between
      # architectures
      random_gen = np.random.RandomState(42)
      for path in utils.tqdm(
          tmp_files, desc="Shuffling...", unit=" shard", leave=False):
        _shuffle_tfrecord(path, random_gen=random_gen)


def _round_robin_write(writers, generator):
  """Write records from generator round-robin across writers."""
  for i, example in enumerate(utils.tqdm(
      generator, unit=" examples", leave=False)):
    writers[i % len(writers)].write(example)


def _dicts_to_tf_sequence_example(context_dict, sequences_dict):
  flists = {}
  for k, flist in six.iteritems(sequences_dict):
    flists[k] = tf.train.FeatureList(
        feature=[_item_to_tf_feature(el, k) for el in flist])
  return tf.train.SequenceExample(
      context=_dict_to_tf_features(context_dict),
      feature_lists=tf.train.FeatureLists(feature_list=flists),
  )


def _dict_to_tf_example(example_dict):
  """Builds tf.train.Example from (string -> int/float/str list) dictionary."""
  return tf.train.Example(features=_dict_to_tf_features(example_dict))


def _item_to_tf_feature(item, key_name):
  """Single item to a tf.train.Feature."""
  v = item
  if isinstance(v, (list, tuple)) and not v:
    raise ValueError(
        "Feature {} received an empty list value, so is unable to infer the "
        "feature type to record. To support empty value, the corresponding "
        "FeatureConnector should return a numpy array with the correct dtype "
        "instead of a Python list.".format(key_name)
    )

  # Handle strings/bytes first
  if isinstance(v, (six.binary_type, six.string_types)):
    v = [tf.compat.as_bytes(v)]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=v))
  elif (isinstance(v, (tuple, list)) and
        all(isinstance(x, (six.binary_type, six.string_types)) for x in v)):
    v = [tf.compat.as_bytes(x) for x in v]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=v))
  elif (isinstance(v, np.ndarray) and
        (v.dtype.kind in ("U", "S") or v.dtype == object)):  # binary or unicode
    v = [tf.compat.as_bytes(x) for x in v.flatten()]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=v))

  # Use NumPy for numeric types
  v = np.array(v).flatten()  # Convert v into a 1-d array

  if np.issubdtype(v.dtype, np.integer):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=v))
  elif np.issubdtype(v.dtype, np.floating):
    return tf.train.Feature(float_list=tf.train.FloatList(value=v))
  else:
    raise ValueError(
        "Value received: {}.\n"
        "tf.train.Feature does not support type {} for feature key {}. "
        "This may indicate that one of the FeatureConnectors received an "
        "unsupported value as input.".format(repr(v), repr(type(v)), key_name)
    )


def _dict_to_tf_features(example_dict):
  """Builds tf.train.Features from (string -> int/float/str list) dictionary."""
  features = {k: _item_to_tf_feature(v, k) for k, v
              in six.iteritems(example_dict)}
  return tf.train.Features(feature=features)
