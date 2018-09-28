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

"""FileFormatAdapters for GeneratorBasedDatasetBuilder."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import collections
import contextlib
import csv
import random
import string

import six
import tensorflow as tf
import tqdm


@six.add_metaclass(abc.ABCMeta)
class FileFormatAdapter(object):
  """Provides writing and reading methods for a file format."""

  @abc.abstractmethod
  def write_from_generator(self, generator_fn, output_files):
    """Write to files from generators_and_filenames.

    Args:
      generator_fn: returns generator yielding dictionaries of feature name to
        value.
      output_files (list<str>): output files to write records to.
    """
    raise NotImplementedError

  @abc.abstractmethod
  def dataset_from_filename(self, filename):
    """Returns a `tf.data.Dataset` whose elements are dicts given a filename."""
    raise NotImplementedError

  @abc.abstractproperty
  def filetype_suffix(self):
    """Returns a str file type suffix (e.g. "csv")."""
    raise NotImplementedError


class TFRecordExampleAdapter(FileFormatAdapter):
  """Writes serialized Examples protos to TFRecord files.

  Constraints on generators:

  * The generator must yield feature dictionaries (`dict<str feature_name,
    feature_value>`).
  * The allowed feature types are `int`, `float`, and `str` (or `bytes` in
    Python 3; `unicode` strings will be encoded in `utf-8`), or lists thereof.
  """

  def __init__(self, example_reading_spec):
    """Construcs a TFRecordExampleAdapter.

    Args:
      example_reading_spec (dict): feature name to tf.FixedLenFeature or
        tf.VarLenFeature. Passed to tf.parse_single_example.
    """
    self._example_reading_spec = example_reading_spec

  def write_from_generator(self, generator_fn, output_files):
    wrapped = _generate_tf_examples(generator_fn())
    _write_tfrecords_from_generator(wrapped, output_files)

  def dataset_from_filename(self, filename):
    dataset = tf.data.TFRecordDataset(filename, buffer_size=int(16 * 1e6))
    return dataset.map(self._decode)

  def _decode(self, *record):
    record, = record
    return tf.parse_single_example(record, self._example_reading_spec)

  @property
  def filetype_suffix(self):
    return "tfrecord"


class CSVAdapter(FileFormatAdapter):
  """Writes features to CSV files.

  Constraints on generators:

  * The generator must yield feature dictionaries (`dict<str feature_name,
    feature_value>`).
  * The allowed feature types are `int`, `float`, and `str`. By default, only
    scalar features are supported (that is, not lists).

  You can modify how records are written by passing `csv_writer_ctor`.

  You can modify how records are read by passing `csv_dataset_kwargs`.

  Note that all CSV files produced will have a header row.
  """

  # TODO(rsepassi): Instead of feature_types, take record_defaults and
  # infer the types from the default values if provided.
  def __init__(self,
               feature_types,
               csv_dataset_kwargs=None,
               csv_writer_ctor=csv.writer):
    """Constructs CSVAdapter.

    Args:
      feature_types (dict<name, type>): specifies the dtypes of each of the
        features (columns in the CSV file).
      csv_dataset_kwargs (dict): forwarded to `tf.contrib.data.CsvDataset`.
      csv_writer_ctor (function): takes file handle and returns writer.

    Raises:
      ValueError: if csv_dataset_kwargs["header"] is present.
    """
    self._csv_kwargs = csv_dataset_kwargs or {}
    if "header" in self._csv_kwargs:
      raise ValueError("header must not be present")
    self._feature_types = _sort_dict_by_key(feature_types)
    self._csv_kwargs["header"] = True
    if "record_defaults" not in self._csv_kwargs:
      types = list(zip(*self._feature_types))[1]
      self._csv_kwargs["record_defaults"] = types
    self._csv_writer_ctor = csv_writer_ctor

  # TODO(rsepassi): Add support for non-scalar features (e.g. list of integers).
  def write_from_generator(self, generator_fn, output_files):
    wrapped = _generate_csv_rows(generator_fn())
    _write_csv_from_generator(wrapped, output_files,
                              self._csv_writer_ctor)

  def dataset_from_filename(self, filename):
    dataset = tf.contrib.data.CsvDataset(filename, **self._csv_kwargs)
    return dataset.map(self._decode)

  def _decode(self, *record):
    record_dict = {}
    feature_names = list(zip(*self._feature_types))[0]
    for name, feature in zip(feature_names, record):
      record_dict[name] = feature
    return record_dict

  @property
  def filetype_suffix(self):
    return "csv"


def do_files_exist(filenames):
  """Whether all filenames exist."""
  preexisting = [tf.gfile.Exists(f) for f in filenames]
  return all(preexisting)


@contextlib.contextmanager
def _close_on_exit(handles):
  """Call close on all handles on exit."""
  try:
    yield handles
  finally:
    for handle in handles:
      handle.close()


def incomplete_file(filename):
  """Returns a temporary filename based on filename."""
  random_suffix = "".join(
      random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
  return filename + ".incomplete" + random_suffix


@contextlib.contextmanager
def _incomplete_files(filenames):
  """Create temporary files for filenames and rename on exit."""
  tmp_files = [incomplete_file(f) for f in filenames]
  try:
    yield tmp_files
    for tmp, output in zip(tmp_files, filenames):
      tf.gfile.Rename(tmp, output)
  finally:
    for tmp in tmp_files:
      if tf.gfile.Exists(tmp):
        tf.gfile.Remove(tmp)


# TODO(rsepassi): Use the TFRecordWriter.write op to get multithreading
def _write_tfrecords_from_generator(generator, output_files):
  """Writes generated str records to output_files in round-robin order."""
  if do_files_exist(output_files):
    return

  with _incomplete_files(output_files) as tmp_files:
    writers = [tf.python_io.TFRecordWriter(fname) for fname in tmp_files]
    with _close_on_exit(writers) as writers:
      tf.logging.info("Writing TFRecords")
      _round_robin_write(writers, generator)


def _round_robin_write(writers, generator):
  """Write records from generator round-robin across writers."""
  for i, record in enumerate(tqdm.tqdm(generator, unit=" records",
                                       mininterval=10)):
    writers[i % len(writers)].write(record)


def _sort_dict_by_key(feature_dict):
  keys = sorted(list(feature_dict.keys()))
  return [(k, feature_dict[k]) for k in keys]


def _generate_csv_rows(generator):
  header_row = None
  for record in generator:
    this_header, record_row = zip(*_sort_dict_by_key(record))
    if header_row is None:
      header_row = this_header
      yield header_row
    yield record_row


def _write_csv_from_generator(generator, output_files, writer_ctor=None):
  """Write records to CSVs using writer_ctor (defaults to csv.writer)."""
  if do_files_exist(output_files):
    return

  if writer_ctor is None:
    writer_ctor = csv.writer

  def create_csv_writer(filename):
    with tf.gfile.Open(filename, "wb") as f:
      writer = writer_ctor(f)
      # Simple way to give the writer a "write" method proxying writerow
      writer = collections.namedtuple("_writer", ["write"])(
          write=writer.writerow)
    return f, writer

  with _incomplete_files(output_files) as tmp_files:
    handles, writers = zip(*[create_csv_writer(fname) for fname in tmp_files])
    with _close_on_exit(handles):
      tf.logging.info("Writing CSVs")
      header = next(generator)
      for w in writers:
        w.write(header)
      _round_robin_write(writers, generator)


def _dict_to_tf_example(example_dict):
  """Builds tf.train.Example from (string -> int/float/str list) dictionary."""
  features = {}
  for (k, v) in six.iteritems(example_dict):
    if v is None:
      continue
    if not isinstance(v, (list, tuple)):
      v = [v]

    if isinstance(v[0], six.integer_types):
      features[k] = tf.train.Feature(int64_list=tf.train.Int64List(value=v))
    elif isinstance(v[0], float):
      features[k] = tf.train.Feature(float_list=tf.train.FloatList(value=v))
    elif isinstance(v[0], six.string_types) or isinstance(v[0], bytes):
      v = [tf.compat.as_bytes(x) for x in v]
      features[k] = tf.train.Feature(bytes_list=tf.train.BytesList(value=v))
    else:
      raise ValueError("Value for %s is not a recognized type; v: %s type: %s" %
                       (k, str(v[0]), str(type(v[0]))))

  return tf.train.Example(features=tf.train.Features(feature=features))


def _generate_tf_examples(generator):
  """Wraps dict generator to produce serialized tf.train.Examples."""
  for example_dict in generator:
    yield _dict_to_tf_example(example_dict).SerializeToString()
