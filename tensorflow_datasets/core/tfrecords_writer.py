# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

import collections
import itertools
import json
import os

from typing import Any, Iterable, List, Tuple

from absl import logging
import six
import tensorflow.compat.v2 as tf

from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import hashing
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import shuffle
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import shard_utils

# TODO(tfds): Should be `TreeDict[FeatureValue]`
Example = Any

MIN_SHARD_SIZE = 64<<20  # 64 MiB
MAX_SHARD_SIZE = 1024<<20  # 2 GiB

# TFRECORD overheads.
# https://github.com/tensorflow/tensorflow/blob/27325fabed898880fa1b33a04d4b125a6ef4bbc8/tensorflow/core/lib/io/record_writer.h#L104
TFRECORD_REC_OVERHEAD = 16

# Number of temp buckets for beam writer.
# 100K buckets at 1G per bucket gives us ~100TB. Each bucket can go bigger, as
# long as it can hold in memory. So if each bucket goes to 5GB, that's 500TB.
# It seems reasonable to require 10GB of RAM per worker to handle a 1PB split.
_BEAM_NUM_TEMP_SHARDS = int(100e3)

# Spec to write a final tfrecord shard.
_ShardSpec = collections.namedtuple("_ShardSpec", [
    # Index of shard.
    "shard_index",
    # The path where to write shard.
    "path",
    # Number of examples in shard
    "examples_number",
    # Reading instructions (List[FileInstruction]).
    "file_instructions",
])


def _raise_error_for_duplicated_keys(example1, example2, example_specs):
  """Log information about the examples and raise an AssertionError."""
  msg = "Two records share the same hashed key!"
  logging.error(msg)
  parser = example_parser.ExampleParser(example_specs)
  ex1 = parser.parse_example(example1)
  ex2 = parser.parse_example(example2)
  logging.error("1st example: %s", ex1)
  logging.error("2nd example: %s", ex2)
  raise AssertionError(msg)


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
    shard_specs.append(_ShardSpec(
        shard_index=shard_index,
        path="%s-%05d-of-%05d" % (path, shard_index, num_shards),
        examples_number=to-from_,
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
      int(round(num_examples * (float(i)/number_of_shards)))
      for i in range(1, number_of_shards+1)
  ]


def _write_tfrecord(
    path: str,
    iterator: Iterable[bytes],
):
  """Write single (non sharded) TFrecord file from iterator."""
  with tf.io.TFRecordWriter(path) as writer:
    for serialized_example in iterator:
      writer.write(serialized_example)
    writer.flush()


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

  def __init__(self, example_specs, path, hash_salt):
    self._example_specs = example_specs
    self._serializer = example_serializer.ExampleSerializer(example_specs)
    self._shuffler = shuffle.Shuffler(os.path.dirname(path), hash_salt)
    self._num_examples = 0
    self._path = path

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
    print("Shuffling and writing examples to %s" % self._path)
    shard_specs = _get_shard_specs(self._num_examples, self._shuffler.size,
                                   self._shuffler.bucket_lengths, self._path)
    # Here we just loop over the examples, and don't use the instructions, just
    # the final number of examples in every shard. Instructions could be used to
    # parallelize, but one would need to be careful not to sort buckets twice.
    examples_generator = iter(utils.tqdm(
        self._shuffler, total=self._num_examples, unit=" examples",
        leave=False))
    try:
      for shard_spec in shard_specs:
        iterator = itertools.islice(
            examples_generator, 0, shard_spec.examples_number)
        _write_tfrecord(shard_spec.path, iterator)
    except shuffle.DuplicatedKeysError as err:
      _raise_error_for_duplicated_keys(err.item1, err.item2,
                                       self._example_specs)
    shard_lengths = [int(spec.examples_number) for spec in shard_specs]
    logging.info("Done writing %s. Shard lengths: %s",
                 self._path, shard_lengths)
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

  def __init__(self, example_specs, path, hash_salt):
    """Init BeamWriter.

    Args:
      example_specs:
      path: str, path where to write tfrecord file. Eg:
        "/foo/mnist-train.tfrecord".
        The suffix (eg: `.00000-of-00004` will be added by the BeamWriter.
        Note that file "{path}.shard_lengths.json" is also created. It contains
          a list with the number of examples in each final shard. Eg:
          "[10,11,10,11]".
      hash_salt: string, the salt to use for hashing of keys.
    """
    self._original_state = dict(example_specs=example_specs, path=path,
                                hash_salt=hash_salt)
    self._path = path
    self._split_info_path = "%s.split_info.json" % path
    self._serializer = example_serializer.ExampleSerializer(example_specs)
    self._example_specs = example_specs
    self._hasher = hashing.Hasher(hash_salt)
    self._split_info = None

  def __getstate__(self):
    return self._original_state

  def __setstate__(self, state):
    self.__init__(**state)

  def _serialize_shard(
      self,
      key_example: Tuple[hashing.HashKey, Example],
  ) -> Tuple[int, Tuple[int, bytes]]:
    """Returns (shard#, (hkey, serialized_example))."""
    key, example = key_example
    serialized_example = self._serializer.serialize_example(example)
    hkey = self._hasher.hash_key(key)
    bucketid = shuffle.get_bucket_number(hkey, _BEAM_NUM_TEMP_SHARDS)
    hkey = _long_for_py2(hkey)
    bucketid = _long_for_py2(bucketid)
    return (bucketid, (hkey, serialized_example))

  def _sort_bucket(self, bucketid_examples):
    """Sort the examples in bucket, emits total size and len on side."""
    beam = lazy_imports_lib.lazy_imports.apache_beam
    bucketid, examples = bucketid_examples
    examples = sorted(examples)  # We know by design it fits in memory.
    for i in range(len(examples)-1):
      if examples[i][0] == examples[i+1][0]:
        _raise_error_for_duplicated_keys(examples[i][1], examples[i+1][1],
                                         self._example_specs)
    examples = [ex[1] for ex in examples]
    total_size = sum(len(ex) for ex in examples)
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
    bucket_lengths = [bucket2length.get(i, 0)
                      for i in range(max(bucket2length.keys()) + 1)]
    shard_specs = _get_shard_specs(
        total_num_examples, total_size, bucket_lengths, self._path)
    with tf.io.gfile.GFile(self._split_info_path, "w") as json_f:
      json_f.write(json.dumps(
          {
              "total_size": total_size,
              "shard_lengths": [
                  int(shard.examples_number) for shard in shard_specs]
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

  def _write_final_shard(self, shardid_examples):
    shard_path, examples_by_bucket = shardid_examples
    examples = list(itertools.chain(*[
        ex[1] for ex in sorted(examples_by_bucket)]))
    _write_tfrecord(shard_path, examples)

  def write_from_pcollection(self, examples_pcollection):
    """Returns PTransform to write (key, example) PCollection to tfrecords."""
    beam = lazy_imports_lib.lazy_imports.apache_beam
    # Here bucket designates a temporary shard, to help differenciate between
    # temporary and final shards.
    buckets, buckets_len_size = (
        examples_pcollection
        # (key, example)
        | "SerializeBucketize" >> beam.Map(self._serialize_shard)
        # (bucket_id, (hkey, serialized_example))
        | "GroupByBucket" >> beam.GroupByKey()
        # (bucket_id, [(hkey0, serialized0), ...])
        | "SortBucketsGetSizeLen" >> (
            beam.ParDo(self._sort_bucket)
            .with_outputs(self._OUTPUT_TAG_BUCKETS_LEN_SIZE, main="buckets")))
        # buckets = (bucketid, [serialized0, serialized1, ...])
        # buckets_len_size = (bucketid, (num_examples_bucket, bucket_byte_size))

    boundaries = (
        buckets_len_size
        | "CombineBucketsSizes" >> beam.transforms.combiners.ToDict()
        # {bucketid: (num_examples_bucket, bucket_byte_size)}
        | "GetBoundaries"  >> beam.ParDo(
            self._get_boundaries_per_bucket_shard))
        # (bucketid, (shard_path, from, to)

    return (
        {"examples": buckets, "boundaries": boundaries}
        # {
        #     "examples": (bucketid, [serialized0, serialized1, ...])
        #     "boundaries": (bucketid, (shard_path, from, to)
        # }
        | "GroupBucketsAndBoundaries" >> beam.CoGroupByKey()
        # (bucketid, {
        #     "examples": [[serialized0, serialized1, ...]],
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
