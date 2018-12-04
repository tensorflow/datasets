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

"""FileFormatAdapters for GeneratorBasedDatasetBuilder.

FileFormatAdapters implement methods to write and read data from a
particular file format.

Currently, two FileAdapter are available:
 * TFRecordExampleAdapter: To store the pre-processed dataset as .tfrecord file
 * CSVAdapter: To store the dataset as CSV file

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
import collections
import contextlib
import csv
import itertools
import random
import string

import numpy as np
import six
import tensorflow as tf
import tqdm

__all__ = [
    "FileFormatAdapter",
    "TFRecordExampleAdapter",
    "CSVAdapter",
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
  """Writes/Reads serialized Examples protos to/from TFRecord files.

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
    wrapped = (
        _dict_to_tf_example(d).SerializeToString() for d in generator_fn())
    _write_tfrecords_from_generator(wrapped, output_files)

  def dataset_from_filename(self, filename):
    dataset = tf.data.TFRecordDataset(filename, buffer_size=int(16 * 1e6))
    return dataset.map(self._decode,
                       num_parallel_calls=tf.data.experimental.AUTOTUNE)

  def _decode(self, record):
    return tf.parse_single_example(record, self._example_reading_spec)

  @property
  def filetype_suffix(self):
    return "tfrecord"


class CSVAdapter(FileFormatAdapter):
  """Writes/reads features to/from CSV files.

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
      csv_dataset_kwargs (dict): forwarded to `tf.data.experimental.CsvDataset`.
      csv_writer_ctor (function): takes file handle and returns writer.

    Raises:
      ValueError: if csv_dataset_kwargs["header"] is present.
    """
    self._csv_kwargs = csv_dataset_kwargs or {}
    if "header" in self._csv_kwargs:
      raise ValueError("header must not be present")
    self._feature_types = collections.OrderedDict(sorted(feature_types.items()))
    self._csv_kwargs["header"] = True
    # TODO(epot): Should check feature_types and raise error is some are
    # not supported with CSV. Currently CSV files only support single
    # values, no array.
    if "record_defaults" not in self._csv_kwargs:
      types = [f.dtype for f in self._feature_types.values()]
      self._csv_kwargs["record_defaults"] = types
    self._csv_writer_ctor = csv_writer_ctor

  # TODO(rsepassi): Add support for non-scalar features (e.g. list of integers).
  def write_from_generator(self, generator_fn, output_files):
    # Flatten the dict returned by the generator and add the header
    header_keys = list(self._feature_types.keys())
    rows_generator = ([d[k] for k in header_keys] for d in generator_fn())
    generator_with_header = itertools.chain([header_keys], rows_generator)
    _write_csv_from_generator(
        generator_with_header,
        output_files,
        self._csv_writer_ctor)

  def dataset_from_filename(self, filename):
    dataset = tf.data.experimental.CsvDataset(filename, **self._csv_kwargs)
    return dataset.map(self._decode,
                       num_parallel_calls=tf.data.experimental.AUTOTUNE)

  def _decode(self, *record):
    return {
        k: v for k, v in zip(self._feature_types.keys(), record)
    }

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
      tf.gfile.Rename(tmp, output)
  finally:
    for tmp in tmp_files:
      if tf.gfile.Exists(tmp):
        tf.gfile.Remove(tmp)


@contextlib.contextmanager
def incomplete_dir(dirname):
  """Create temporary dir for dirname and rename on exit."""
  tmp_dir = get_incomplete_path(dirname)
  try:
    yield tmp_dir
    tf.gfile.Rename(tmp_dir, dirname)
  finally:
    if tf.gfile.Exists(tmp_dir):
      tf.gfile.DeleteRecursively(tmp_dir)


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
  for i, example in enumerate(tqdm.tqdm(generator, unit=" examples",
                                        mininterval=10)):
    writers[i % len(writers)].write(example)


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

    if not isinstance(v, (list, tuple, np.ndarray)):
      v = [v]
    elif isinstance(v, np.ndarray):
      v = v.flatten()

    if isinstance(v[0], six.integer_types + (np.integer,)):
      features[k] = tf.train.Feature(int64_list=tf.train.Int64List(value=v))
    elif isinstance(v[0], (float, np.floating)):
      features[k] = tf.train.Feature(float_list=tf.train.FloatList(value=v))
    elif isinstance(v[0], six.string_types + (bytes,)):
      v = [tf.compat.as_bytes(x) for x in v]
      features[k] = tf.train.Feature(bytes_list=tf.train.BytesList(value=v))
    else:
      raise ValueError(
          "tf.train.Example does not support type {} of {} for feature key {}. "
          "This may indicate that one of the FeatureConnectors received an "
          "unsupported value as input.".format(repr(type(v[0])), repr(v[0]), k)
      )

  return tf.train.Example(features=tf.train.Features(feature=features))
