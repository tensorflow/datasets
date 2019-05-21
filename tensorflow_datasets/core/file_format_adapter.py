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

  def __init__(self, example_specs):
    """Constructor.

    Args:
      example_specs: Nested `dict` of `tfds.features.TensorInfo`, corresponding
        to the structure of data to write/read.
    """
    self._example_specs = example_specs
    self._flat_example_specs = utils.flatten_nest_dict(self._example_specs)

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

  def _build_feature_specs(self):
    """Returns the `tf.train.Example` feature specification.

    Returns:
      The `dict` of `tf.io.FixedLenFeature`, `tf.io.VarLenFeature`, ...
    """
    # Convert individual fields into tf.train.Example compatible format
    def build_single_spec(k, v):
      with utils.try_reraise(
          "Specification error for feature {} ({}): ".format(k, v)):
        return _to_tf_example_spec(v)

    return {
        k: build_single_spec(k, v) for k, v in self._flat_example_specs.items()
    }

  def serialize_example(self, example):
    """Serialize the given example.

    Args:
      example: Nested `dict` containing the input to serialize. The input
        structure and values dtype/shape must match the `example_specs`
        provided at construction.

    Returns:
      serialize_proto: `str`, the serialized `tf.train.Example` proto
    """
    example = utils.flatten_nest_dict(example)
    example = _dict_to_tf_example(example, self._flat_example_specs)
    return example.SerializeToString()

  def parse_example(self, serialized_example):
    """Deserialize a single `tf.train.Example` proto.

    Usage:
    ```
    ds = tf.data.TFRecordDataset(filepath)
    ds = ds.map(file_adapter.parse_example)
    ```

    Args:
      serialized_example: `tf.Tensor`, the `tf.string` tensor containing the
        serialized proto to decode.

    Returns:
      example: A nested `dict` of `tf.Tensor` values. The structure and tensors
        shape/dtype match the  `example_specs` provided at construction.
    """
    example = tf.io.parse_single_example(
        serialized=serialized_example,
        features=self._build_feature_specs(),
    )
    example = {
        k: _deserialize_single_field(example_data, tensor_info)
        for k, (example_data, tensor_info)
        in utils.zip_dict(example, self._flat_example_specs)
    }
    # Reconstruct all nesting
    example = utils.pack_as_nest_dict(example, self._example_specs)
    return example

  def write_from_generator(self, generator_fn, output_files):
    wrapped = (
        self.serialize_example(example) for example in generator_fn())
    _write_tfrecords_from_generator(wrapped, output_files, shuffle=True)

  def write_from_pcollection(self, pcollection, file_path_prefix, num_shards):
    beam = lazy_imports.lazy_imports.apache_beam

    # WARNING: WriteToTFRecord do not support long in python2 with the default,
    # beam implementation, so need to convert the long value (from the proto
    # field) into int, otherwise, the number of shards will be random.
    num_shards = int(num_shards)

    return (
        pcollection
        | "SerializeDict" >> beam.Map(self.serialize_example)
        | "Shuffle" >> beam.Reshuffle()
        | "WriteToExamples" >> beam.io.WriteToTFRecord(
            file_path_prefix=".".join([file_path_prefix, self.filetype_suffix]),
            num_shards=num_shards,
        )
    )

  def dataset_from_filename(self, filename):
    dataset = tf.data.TFRecordDataset(filename, buffer_size=int(16 * 1e6))
    return dataset.map(self.parse_example,
                       num_parallel_calls=tf.data.experimental.AUTOTUNE)

  @property
  def filetype_suffix(self):
    return "tfrecord"


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


def _dict_to_tf_example(example_dict, tensor_info_dict=None):
  """Builds tf.train.Example from (string -> int/float/str list) dictionary.

  Args:
    example_dict: `dict`, dict of values, tensor,...
    tensor_info_dict: `dict` of `tfds.feature.TensorInfo` If given, perform
      additional checks on the example dict (check dtype, shape, number of
      fields...)
  """
  def serialize_single_field(k, example_data, tensor_info):
    with utils.try_reraise(
        "Error while serializing feature {} ({}): ".format(k, tensor_info)):
      return _item_to_tf_feature(example_data, tensor_info)

  if tensor_info_dict:
    example_dict = {
        k: serialize_single_field(k, example_data, tensor_info)
        for k, (example_data, tensor_info)
        in utils.zip_dict(example_dict, tensor_info_dict)
    }
  else:
    example_dict = {
        k: serialize_single_field(k, example_data, None)
        for k, example_data in example_dict.items()
    }

  return tf.train.Example(features=tf.train.Features(feature=example_dict))


def _is_string(item):
  """Check if the object contains string or bytes."""
  if isinstance(item, (six.binary_type, six.string_types)):
    return True
  elif (isinstance(item, (tuple, list)) and
        all(isinstance(x, (six.binary_type, six.string_types)) for x in item)):
    return True
  elif (isinstance(item, np.ndarray) and  # binary or unicode
        (item.dtype.kind in ("U", "S") or item.dtype == object)):
    return True
  return False


def _item_to_tf_feature(item, tensor_info=None):
  """Single item to a tf.train.Feature."""
  v = item
  if not tensor_info and isinstance(v, (list, tuple)) and not v:
    raise ValueError(
        "Received an empty list value, so is unable to infer the "
        "feature type to record. To support empty value, the corresponding "
        "FeatureConnector should return a numpy array with the correct dtype "
        "instead of a Python list."
    )

  # Handle strings/bytes first
  is_string = _is_string(v)

  if tensor_info:
    np_dtype = np.dtype(tensor_info.dtype.as_numpy_dtype)
  elif is_string:
    np_dtype = object  # Avoid truncating trailing '\x00' when converting to np
  else:
    np_dtype = None

  v = np.array(v, dtype=np_dtype)

  # Check that the shape is expected
  if tensor_info:
    utils.assert_shape_match(v.shape, tensor_info.shape)
    if tensor_info.dtype == tf.string and not is_string:
      raise ValueError(
          "Unsuported value: {}\nCould not convert to bytes list.".format(item))

  # Convert boolean to integer (tf.train.Example does not support bool)
  if v.dtype == np.bool_:
    v = v.astype(int)

  v = v.flatten()  # Convert v into a 1-d array
  if np.issubdtype(v.dtype, np.integer):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=v))
  elif np.issubdtype(v.dtype, np.floating):
    return tf.train.Feature(float_list=tf.train.FloatList(value=v))
  elif is_string:
    v = [tf.compat.as_bytes(x) for x in v]
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=v))
  else:
    raise ValueError(
        "Unsuported value: {}.\n"
        "tf.train.Feature does not support type {}. "
        "This may indicate that one of the FeatureConnectors received an "
        "unsupported value as input.".format(repr(v), repr(type(v)))
    )


def _deserialize_single_field(example_data, tensor_info):
  """Reconstruct the serialized field."""

  # Restore shape if possible. TF Example flattened it.
  if tensor_info.shape.count(None) < 2:
    shape = [-1 if i is None else i for i in tensor_info.shape]
    example_data = tf.reshape(example_data, shape)

  # Restore dtype
  if example_data.dtype != tensor_info.dtype:
    example_data = tf.dtypes.cast(example_data, tensor_info.dtype)
  return example_data


def _to_tf_example_spec(tensor_info):
  """Convert a `TensorInfo` into a feature proto object."""
  # Convert the dtype

  # TODO(b/119937875): TF Examples proto only support int64, float32 and string
  # This create limitation like float64 downsampled to float32, bool converted
  # to int64 which is space ineficient, no support for complexes or quantized
  # It seems quite space inefficient to convert bool to int64
  if tensor_info.dtype.is_integer or tensor_info.dtype.is_bool:
    dtype = tf.int64
  elif tensor_info.dtype.is_floating:
    dtype = tf.float32
  elif tensor_info.dtype == tf.string:
    dtype = tf.string
  else:
    # TFRecord only support 3 types
    raise NotImplementedError(
        "Serialization not implemented for dtype {}".format(tensor_info))

  # Convert the shape

  # Select the feature proto type in function of the unknown shape
  if all(s is not None for s in tensor_info.shape):
    return tf.io.FixedLenFeature(  # All shaped defined
        shape=tensor_info.shape,
        dtype=dtype,
        default_value=tensor_info.default_value,
    )
  elif (tensor_info.shape.count(None) == 1 and tensor_info.shape[0] is None):
    return tf.io.FixedLenSequenceFeature(  # First shape undefined
        shape=tensor_info.shape[1:],
        dtype=dtype,
        allow_missing=True,
        default_value=tensor_info.default_value,
    )
  else:
    raise NotImplementedError(
        "Tensor with a unknown dimension not at the first position not "
        "supported: {}".format(tensor_info))
