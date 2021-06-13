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

"""To write records into sharded tfrecord files."""

import itertools
import json
import os

from typing import Any, Iterable, List, Optional, Tuple

from absl import logging
import dataclasses
import six
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import hashing
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import shuffle
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import shard_utils
from tensorflow_datasets.core.utils import type_utils

# TODO(tfds): Should be `TreeDict[FeatureValue]`
Example = Any

MIN_SHARD_SIZE = 64 << 20  # 64 MiB
MAX_SHARD_SIZE = 1024 << 20  # 2 GiB

# TFRECORD overheads.
# https://github.com/tensorflow/tensorflow/blob/27325fabed898880fa1b33a04d4b125a6ef4bbc8/tensorflow/core/lib/io/record_writer.h#L104
TFRECORD_REC_OVERHEAD = 16

# Number of temp buckets for beam writer.
# 100K buckets at 1G per bucket gives us ~100TB. Each bucket can go bigger, as
# long as it can hold in memory. So if each bucket goes to 5GB, that's 500TB.
# It seems reasonable to require 10GB of RAM per worker to handle a 1PB split.
_BEAM_NUM_TEMP_SHARDS = int(100e3)

_INDEX_PATH_SUFFIX = "_index.json"


@dataclasses.dataclass(frozen=True)
class _ShardSpec:
  """Spec to write a final records shard.

  Attributes:
    shard_index: Index of the shard.
    path: The path where to write the shard.
    index_path: The path where to write index of the records in the
      corresponding shard. NOTE: Value for this attribute is always set, but
        usage depends on whether `write_examples` returned a list of record
        positions for each example.
    examples_number: Number of examples in shard.
    file_instructions: Reading instructions.
  """
  shard_index: int
  path: str
  index_path: str
  examples_number: int
  file_instructions: List[shard_utils.FileInstruction]


def _raise_error_for_duplicated_keys(example1, example2, example_specs):
  """Log information about the examples and raise an AssertionError."""
  msg = "Two examples share the same hashed key!"
  logging.error(msg)
  parser = example_parser.ExampleParser(example_specs)
  ex1 = parser.parse_example(example1)
  ex2 = parser.parse_example(example2)
  logging.error("1st example: %s", ex1)
  logging.error("2nd example: %s", ex2)
  raise AssertionError(msg + " See logs above to view the examples.")


def _get_index_path(path: str) -> type_utils.PathLike:
  """Returns path to the index file of the records stored at the given path.

  E.g: Say the path to a shard of records (of a particular split) are stored at
  `your/path/to/records/foo.riegeli-00001-of-00005`, it is transformed into
  `your/path/to/records/foo.riegeli-00001-of-00005_index.json`.

  Args:
    path: Path to the record file.

  Returns:
    Path of the index file of a shard of records stored at given path.
  """
  return path + _INDEX_PATH_SUFFIX


def _get_shard_specs(
    num_examples: int,
    total_size: int,
    bucket_lengths: List[int],
    path: str,
) -> List[_ShardSpec]:
  """Returns list of _ShardSpec instances, corresponding to shards to write.

  Args:
    num_examples: int, number of examples in split.
    total_size: int (bytes), sum of example sizes.
    bucket_lengths: list of ints, number of examples in each bucket.
    path: string, path to tfrecord. `-xxxxx-of-xxxxx` will be added.
  """
  num_shards = _get_number_shards(total_size, num_examples)
  shard_boundaries = _get_shard_boundaries(num_examples, num_shards)
  shard_specs = []
  bucket_indexes = [str(i) for i in range(len(bucket_lengths))]
  from_ = 0
  for shard_index, to in enumerate(shard_boundaries):
    # Read the bucket indexes
    file_instructions = shard_utils.get_file_instructions(
        from_, to, bucket_indexes, bucket_lengths)
    shard_path = "%s-%05d-of-%05d" % (path, shard_index, num_shards)
    index_path = _get_index_path(shard_path)
    shard_specs.append(
        _ShardSpec(
            shard_index=shard_index,
            path=shard_path,
            index_path=index_path,
            examples_number=to - from_,
            file_instructions=file_instructions,
        ))
    from_ = to
  return shard_specs


def _get_shard_boundaries(
    num_examples: int,
    number_of_shards: int,
) -> List[int]:
  if num_examples == 0:
    raise AssertionError("No examples were yielded.")
  if num_examples < number_of_shards:
    raise AssertionError("num_examples ({}) < number_of_shards ({})".format(
        num_examples, number_of_shards))
  return [
      int(round(num_examples * (float(i) / number_of_shards)))
      for i in range(1, number_of_shards + 1)
  ]


def _write_examples(
    path: type_utils.PathLike,
    iterator: Iterable[type_utils.KeySerializedExample],
    file_format: file_adapters.FileFormat = file_adapters.DEFAULT_FILE_FORMAT
) -> Optional[file_adapters.ExamplePositions]:
  """Write examples from iterator in the given `file_format`."""
  return file_adapters.ADAPTER_FOR_FORMAT[file_format].write_examples(
      path, iterator)


def _write_index_file(sharded_index_path: type_utils.PathLike,
                      record_keys: List[Any]):
  """Writes index file for records of a shard at given `sharded_index_path`.

  NOTE: Each record position (i.e shard_key in shard_keys) is stored as a
  string for better readability of the index files. The reader should parse the
  position from string using `RecordPosition.from_str()` method.

  Args:
    sharded_index_path: Path to the sharded index path.
    record_keys: List of keys/indices of the records in the shard.
  """
  # Store string representation of each record position.
  #
  # NOTE: This makes the index file more readable. Although the reader should
  # parse the record position from a string.
  index_info = {"index": [str(record_key) for record_key in record_keys]}
  with tf.io.gfile.GFile(sharded_index_path, "w") as json_f:
    json_f.write(json.dumps(index_info))


def _get_number_shards(
    total_size: int,
    num_examples: int,
) -> int:
  """Returns number of shards for num_examples of total_size in bytes.

  Each shard should be at least 128MB.
  A pod has 16*16=256 TPU devices containing 1024 TPU chips (2048 cores).
  So if the dataset is large enough, we want the number of shards to be a
  multiple of 1024, but with shards as big as possible.
  If the dataset is too small, we want the number of shards to be a power
  of two so it distributes better on smaller TPU configs (8, 16, 32, ... cores).

  Args:
    total_size: the size of the data (serialized, not couting any overhead).
    num_examples: the number of records in the data.

  Returns:
    number of shards to use.
  """
  total_size += num_examples * TFRECORD_REC_OVERHEAD
  max_shards_number = total_size // MIN_SHARD_SIZE
  min_shards_number = total_size // MAX_SHARD_SIZE
  if min_shards_number <= 1024 <= max_shards_number and num_examples >= 1024:
    return 1024
  elif min_shards_number > 1024:
    i = 2
    while True:
      n = 1024 * i
      if n >= min_shards_number and num_examples >= n:
        return n
      i += 1
  else:
    for n in [512, 256, 128, 64, 32, 16, 8, 4, 2]:
      if min_shards_number <= n <= max_shards_number and num_examples >= n:
        return n
  return 1


class Writer(object):
  """Shuffles and writes Examples to sharded TFRecord files.

  The number of shards is computed automatically.

  """

  def __init__(
      self,
      example_specs,
      path,
      hash_salt,
      disable_shuffling: bool,
      file_format=file_adapters.DEFAULT_FILE_FORMAT,
  ):
    """Initializes Writer.

    Args:
      example_specs: spec to build ExampleSerializer.
      path (str): path where records should be written in.
      hash_salt (str or bytes): salt to hash keys.
      disable_shuffling (bool): Specifies whether to shuffle the records.
      file_format (FileFormat): format of the record files in which the dataset
        should be written in.
    """
    self._example_specs = example_specs
    self._serializer = example_serializer.ExampleSerializer(example_specs)
    self._shuffler = shuffle.Shuffler(
        os.path.dirname(path), hash_salt, disable_shuffling)
    self._num_examples = 0
    self._path = path
    self._file_format = file_format

  def write(self, key, example):
    """Writes given Example.

    The given example is not directly written to the tfrecord file, but to a
    temporary file (or memory). The finalize() method does write the tfrecord
    files.

    Args:
      key (int|bytes): the key associated with the example. Used for shuffling.
      example: the Example to write to the tfrecord file.
    """
    serialized_example = self._serializer.serialize_example(example)
    self._shuffler.add(key, serialized_example)
    self._num_examples += 1

  def finalize(self):
    """Effectively writes examples to the tfrecord files."""
    filename = os.path.basename(self._path)
    shard_specs = _get_shard_specs(self._num_examples, self._shuffler.size,
                                   self._shuffler.bucket_lengths, self._path)
    # Here we just loop over the examples, and don't use the instructions, just
    # the final number of examples in every shard. Instructions could be used to
    # parallelize, but one would need to be careful not to sort buckets twice.
    examples_generator = iter(
        utils.tqdm(
            self._shuffler,
            desc=f"Shuffling {filename}...",
            total=self._num_examples,
            unit=" examples",
            leave=False,
        ))
    try:
      for shard_spec in shard_specs:
        iterator = itertools.islice(examples_generator, 0,
                                    shard_spec.examples_number)
        record_keys = _write_examples(shard_spec.path, iterator,
                                      self._file_format)

        # No shard keys returned (e.g: TFRecord format), index cannot be
        # created.
        if not record_keys:
          continue

        # Number of `shard_keys` received should match the number of examples
        # written in this shard.
        if len(record_keys) != int(shard_spec.examples_number):
          raise RuntimeError(
              f"Length of example `keys` ({len(record_keys)}) does not match "
              f"`shard_spec.examples_number: (`{shard_spec.examples_number})")
        _write_index_file(shard_spec.index_path, record_keys)

    except shuffle.DuplicatedKeysError as err:
      _raise_error_for_duplicated_keys(err.item1, err.item2,
                                       self._example_specs)

    # Finalize the iterator to clear-up TQDM
    try:
      val = next(examples_generator)
    except StopIteration:
      pass
    else:
      raise ValueError(
          f"Shuffling more elements than expected. Additional element: {val}")

    shard_lengths = [int(spec.examples_number) for spec in shard_specs]
    logging.info("Done writing %s. Number of examples: %s (shards: %s)",
                 filename, sum(shard_lengths), shard_lengths)
    return shard_lengths, self._shuffler.size


# Make a long out of int. Necessary for Beam on Py2.
if six.PY2:
  _long_for_py2 = long  # pylint: disable=invalid-name,undefined-variable
else:
  _long_for_py2 = lambda int_val: int_val


class BeamWriter(object):
  """Shuffles / writes Examples beam collection to sharded TFRecord files.

  The given examples are not directly writen to the final tfrecord file, but to
  temporary files.
  """
  _OUTPUT_TAG_BUCKETS_LEN_SIZE = "tag_buckets_len_size"

  def __init__(self,
               example_specs,
               path,
               hash_salt,
               disable_shuffling,
               file_format=file_adapters.DEFAULT_FILE_FORMAT):
    """Init BeamWriter.

    Args:
      example_specs:
      path: str, path where to write tfrecord file. Eg:
        "/foo/mnist-train.tfrecord".
        The suffix (eg: `.00000-of-00004` will be added by the BeamWriter. Note
          that file "{path}.shard_lengths.json" is also created. It contains
          a list with the number of examples in each final shard. Eg:
            "[10,11,10,11]".
      hash_salt: string, the salt to use for hashing of keys.
      disable_shuffling: bool, specifies whether to shuffle the records.
      file_format: file_adapters.FileFormat, format of the record files in which
        the dataset will be read/written from.
    """
    self._original_state = dict(
        example_specs=example_specs,
        path=path,
        hash_salt=hash_salt,
        disable_shuffling=disable_shuffling,
        file_format=file_format)
    self._path = os.fspath(path)
    self._split_info_path = "%s.split_info.json" % path
    self._serializer = example_serializer.ExampleSerializer(example_specs)
    self._example_specs = example_specs
    self._hasher = hashing.Hasher(hash_salt)
    self._split_info = None
    self._file_format = file_format
    self._disable_shuffling = disable_shuffling

  def __getstate__(self):
    return self._original_state

  def __setstate__(self, state):
    self.__init__(**state)

  def _serialize_shard(
      self,
      key_example: Tuple[hashing.HashKey, Example],
  ) -> Tuple[int, Tuple[Any, bytes]]:
    """Returns (shard#, (hkey, serialized_example))."""
    key, example = key_example
    serialized_example = self._serializer.serialize_example(example)
    if self._disable_shuffling:
      hkey = key
    else:
      hkey = self._hasher.hash_key(key)
    bucketid = shuffle.get_bucket_number(hkey, _BEAM_NUM_TEMP_SHARDS)
    hkey = _long_for_py2(hkey)
    bucketid = _long_for_py2(bucketid)
    return (bucketid, (hkey, serialized_example))

  def _sort_bucket(
      self,
      bucketid_examples: Tuple[int, List[type_utils.KeySerializedExample]],
  ):
    """Sort the examples in bucket, emits total size and len on side."""
    beam = lazy_imports_lib.lazy_imports.apache_beam
    bucketid, examples = bucketid_examples
    examples = sorted(examples)  # We know by design it fits in memory.
    # Compare continuous examples
    for ex0, ex1 in zip(examples[:-1], examples[1:]):
      if ex0[0] == ex1[0]:  # Different keys
        _raise_error_for_duplicated_keys(ex0[1], ex1[1], self._example_specs)
    total_size = sum(len(ex[1]) for ex in examples)
    yield beam.pvalue.TaggedOutput(self._OUTPUT_TAG_BUCKETS_LEN_SIZE,
                                   (bucketid, (len(examples), total_size)))
    yield (bucketid, examples)

  def _get_boundaries_per_bucket_shard(self, shard_len_sizes):
    """Yields `(bucketid, (shard_path, from, to))` tuples.

    Meaning that buckets[bucketid][from:to] examples should go in shard_path.

    Args:
      shard_len_sizes: dict where the key is the id of the bucket and the value
        is a tuple (len, size) of the corresponding bucket. len is the number of
        examples in the bucket and size is the total size in bytes of the
        elements in that bucket. Buckets with no elements are not mentioned.
    """
    if not shard_len_sizes:
      raise AssertionError("Not a single example present in the PCollection!")
    total_num_examples = 0
    total_size = 0
    bucket2length = {}
    for bucket_index, (length, size) in shard_len_sizes.items():
      total_num_examples += length
      total_size += size
      bucket2length[bucket_index] = length
    bucket_lengths = [
        bucket2length.get(i, 0) for i in range(max(bucket2length.keys()) + 1)
    ]
    shard_specs = _get_shard_specs(total_num_examples, total_size,
                                   bucket_lengths, self._path)
    with tf.io.gfile.GFile(self._split_info_path, "w") as json_f:
      json_f.write(
          json.dumps({
              "total_size":
                  total_size,
              "shard_lengths": [
                  int(shard.examples_number) for shard in shard_specs
              ]
          }))
    for shard_spec in shard_specs:
      for instruction in shard_spec.file_instructions:
        bucketid = int(instruction.filename)
        from_ = instruction.skip
        take = instruction.take
        to = from_ + take if take >= 0 else None
        yield (bucketid, (shard_spec.path, from_, to))

  def _emits_examples_per_shard(self, bucketid_data):
    """Split examples of a bucket given list of instructions applying to it."""
    bucketid, data = bucketid_data
    examples = list(itertools.chain(*data["examples"]))
    for shardpath, from_, to in data["boundaries"]:
      yield (shardpath, (bucketid, examples[from_:to]))

  def _write_final_shard(
      self,
      shardid_examples: Tuple[str, List[Tuple[
          int, List[type_utils.KeySerializedExample]]]],
  ):
    """Write all examples from multiple buckets into the same shard."""
    shard_path, examples_by_bucket = shardid_examples
    examples = itertools.chain(*[ex[1] for ex in sorted(examples_by_bucket)])
    record_keys = _write_examples(shard_path, examples, self._file_format)
    # If there are no record_keys, skip creating index files.
    if not record_keys:
      return
    _write_index_file(_get_index_path(shard_path), list(record_keys))

  def write_from_pcollection(self, examples_pcollection):
    """Returns PTransform to write (key, example) PCollection to tfrecords."""
    beam = lazy_imports_lib.lazy_imports.apache_beam
    # Here bucket designates a temporary shard, to help differenciate between
    # temporary and final shards.
    buckets, buckets_len_size = (
        examples_pcollection
        # (key, example)
        | "SerializeBucketize" >> beam.Map(self._serialize_shard)
        # (bucket_id, hkey_serialized_ex))
        | "GroupByBucket" >> beam.GroupByKey()
        # (bucket_id, [hkey_serialized_ex0, ...])
        | "SortBucketsGetSizeLen" >>
        (beam.ParDo(self._sort_bucket).with_outputs(
            self._OUTPUT_TAG_BUCKETS_LEN_SIZE, main="buckets")))
    # buckets = (bucketid, [hkey_serialized_ex0, ...])
    # buckets_len_size = (bucketid, (num_examples_bucket, bucket_byte_size))

    boundaries = (
        buckets_len_size
        | "CombineBucketsSizes" >> beam.transforms.combiners.ToDict()
        # {bucketid: (num_examples_bucket, bucket_byte_size)}
        | "GetBoundaries" >> beam.ParDo(self._get_boundaries_per_bucket_shard))
    # (bucketid, (shard_path, from, to)

    return (
        {
            "examples": buckets,
            "boundaries": boundaries
        }
        # {
        #     "examples": (bucketid, [hkey_serialized_ex0, ...])
        #     "boundaries": (bucketid, (shard_path, from, to)
        # }
        | "GroupBucketsAndBoundaries" >> beam.CoGroupByKey()
        # (bucketid, {
        #     "examples": [[hkey_serialized_ex0, ...]],
        #     "boundaries": [(shard_path, from, to), ...],
        # })
        | "GetExamplesPerShard" >> beam.FlatMap(self._emits_examples_per_shard)
        # (shard_path, (bucketid, serialized_list[from_:to]))
        | "GroupShards" >> beam.GroupByKey()
        # (shard_path, [(bucketid, serialized_list[from_:to]), ...])
        # bucketid allows to sort the serialized examples
        | "WriteFinalShards" >> beam.Map(self._write_final_shard))

  def finalize(self):
    """Deletes tmp directory and returns shard_lengths and total_size."""
    if self._split_info is None:
      with tf.io.gfile.GFile(self._split_info_path, "r") as json_f:
        self._split_info = json.loads(json_f.read())
      tf.io.gfile.remove(self._split_info_path)
    return self._split_info["shard_lengths"], self._split_info["total_size"]
