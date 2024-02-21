# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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

"""To write records into sharded records files."""

import dataclasses
import functools
import itertools
import json
import os
from typing import Any, Iterable, List, Optional, Tuple

from absl import logging
from etils import epath
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import hashing
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import shuffle
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.utils import file_utils
from tensorflow_datasets.core.utils import shard_utils
from tensorflow_datasets.core.utils import type_utils


# TODO(tfds): Should be `TreeDict[FeatureValue]`
Example = Any

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


def _get_index_path(path: str) -> epath.PathLike:
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
    filename_template: naming.ShardedFileTemplate,
    shard_config: shard_utils.ShardConfig,
) -> List[_ShardSpec]:
  """Returns list of _ShardSpec instances, corresponding to shards to write.

  Args:
    num_examples: int, number of examples in split.
    total_size: int (bytes), sum of example sizes.
    bucket_lengths: list of ints, number of examples in each bucket.
    filename_template: template to format sharded filenames.
    shard_config: the configuration for creating shards.
  """
  num_shards = shard_config.get_number_shards(total_size, num_examples)
  shard_boundaries = _get_shard_boundaries(num_examples, num_shards)
  shard_specs = []
  bucket_indexes = [str(i) for i in range(len(bucket_lengths))]
  from_ = 0
  for shard_index, to in enumerate(shard_boundaries):
    # Read the bucket indexes
    file_instructions = shard_utils.get_file_instructions(
        from_, to, bucket_indexes, bucket_lengths
    )
    shard_path = filename_template.sharded_filepath(
        shard_index=shard_index, num_shards=num_shards
    )
    index_path = _get_index_path(os.fspath(shard_path))
    shard_specs.append(
        _ShardSpec(
            shard_index=shard_index,
            path=os.fspath(shard_path),
            index_path=index_path,
            examples_number=to - from_,
            file_instructions=file_instructions,
        )
    )
    from_ = to
  return shard_specs


def _get_shard_boundaries(
    num_examples: int,
    number_of_shards: int,
) -> List[int]:
  if num_examples == 0:
    raise AssertionError("No examples were yielded.")
  if num_examples < number_of_shards:
    raise AssertionError(
        "num_examples ({}) < number_of_shards ({})".format(
            num_examples, number_of_shards
        )
    )
  return [
      int(round(num_examples * (float(i) / number_of_shards)))
      for i in range(1, number_of_shards + 1)
  ]


def _write_examples(
    path: epath.PathLike,
    iterator: Iterable[type_utils.KeySerializedExample],
    file_format: file_adapters.FileFormat = file_adapters.DEFAULT_FILE_FORMAT,
) -> Optional[file_adapters.ExamplePositions]:
  """Write examples from iterator in the given `file_format`."""
  return file_adapters.ADAPTER_FOR_FORMAT[file_format].write_examples(
      path, iterator
  )


def _write_index_file(
    sharded_index_path: epath.PathLike, record_keys: List[Any]
):
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
  epath.Path(sharded_index_path).write_text(json.dumps(index_info))
  logging.info("Wrote index file to %s", os.fspath(sharded_index_path))


class Writer(object):
  """Shuffles and writes Examples to sharded TFRecord files.

  The number of shards is computed automatically.
  """

  def __init__(
      self,
      serializer: example_serializer.Serializer,
      filename_template: naming.ShardedFileTemplate,
      hash_salt,
      disable_shuffling: bool,
      file_format=file_adapters.DEFAULT_FILE_FORMAT,
      shard_config: Optional[shard_utils.ShardConfig] = None,
  ):
    """Initializes Writer.

    Args:
      serializer: class that can serialize examples.
      filename_template: template to format sharded filenames.
      hash_salt (str or bytes): salt to hash keys.
      disable_shuffling (bool): Specifies whether to shuffle the records.
      file_format (FileFormat): format of the record files in which the dataset
        should be written in.
      shard_config: the configuration for creating shards.
    """
    self._serializer = serializer
    self._shuffler = shuffle.Shuffler(
        dirpath=filename_template.data_dir,
        hash_salt=hash_salt,
        disable_shuffling=disable_shuffling,
    )
    self._num_examples = 0
    self._filename_template = filename_template
    self._file_format = file_format
    self._shard_config = shard_config or shard_utils.ShardConfig()

  def write(self, key, example):
    """Writes given Example.

    The given example is not directly written to the tfrecord file, but to a
    temporary file (or memory). The finalize() method does write the tfrecord
    files.

    Args:
      key (int|bytes): the key associated with the example. Used for shuffling.
      example: the Example to write to the tfrecord file.
    """
    serialized_example = self._serializer.serialize_example(example=example)
    self._shuffler.add(key, serialized_example)
    self._num_examples += 1

  def finalize(self) -> Tuple[List[int], int]:
    """Effectively writes examples to the tfrecord files."""
    filename = self._filename_template.sharded_filepaths_pattern()
    shard_specs = _get_shard_specs(
        self._num_examples,
        self._shuffler.size,
        self._shuffler.bucket_lengths,
        self._filename_template,
        self._shard_config,
    )
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
        )
    )
    try:
      for shard_spec in shard_specs:
        iterator = itertools.islice(
            examples_generator, 0, shard_spec.examples_number
        )
        record_keys = _write_examples(
            shard_spec.path, iterator, self._file_format
        )

        # No shard keys returned (e.g: TFRecord format), index cannot be
        # created.
        if not record_keys:
          continue

        # Number of `shard_keys` received should match the number of examples
        # written in this shard.
        if len(record_keys) != int(shard_spec.examples_number):
          raise RuntimeError(
              f"Length of example `keys` ({len(record_keys)}) does not match "
              f"`shard_spec.examples_number: (`{shard_spec.examples_number})"
          )
        _write_index_file(shard_spec.index_path, record_keys)

    except shuffle.DuplicatedKeysError as err:
      _raise_error_for_duplicated_keys(
          err.item1, err.item2, self._serializer.example_specs
      )

    # Finalize the iterator to clear-up TQDM
    try:
      val = next(examples_generator)
    except StopIteration:
      pass
    else:
      raise ValueError(
          f"Shuffling more elements than expected. Additional element: {val}"
      )

    shard_lengths = [int(spec.examples_number) for spec in shard_specs]

    logging.info(
        "Done writing %s. Number of examples: %s (shards: %s)",
        filename,
        sum(shard_lengths),
        shard_lengths,
    )
    return shard_lengths, self._shuffler.size


@dataclasses.dataclass
class _ShardInfo:
  id: int
  num_examples: int
  size: int


class BeamWriter(object):
  """Shuffles / writes Examples beam collection to sharded TFRecord files.

  The given examples are not directly writen to the final tfrecord file, but to
  temporary files.
  """

  _OUTPUT_TAG_BUCKETS_LEN_SIZE = "tag_buckets_len_size"

  def __init__(
      self,
      serializer: example_serializer.Serializer,
      filename_template: naming.ShardedFileTemplate,
      hash_salt,
      disable_shuffling: bool,
      file_format: file_adapters.FileFormat = file_adapters.DEFAULT_FILE_FORMAT,
      shard_config: Optional[shard_utils.ShardConfig] = None,
  ):
    """Init BeamWriter.

    Note that file "{filepath_prefix}.shard_lengths.json" is also created. It
    contains a list with the number of examples in each final shard. Eg:
    "[10,11,10,11]".

    Args:
      serializer: class that can serialize examples.
      filename_template: template to format sharded filenames.
      hash_salt: string, the salt to use for hashing of keys.
      disable_shuffling: bool, specifies whether to shuffle the records.
      file_format: file_adapters.FileFormat, format of the record files in which
        the dataset will be read/written from.
      shard_config: the configuration for creating shards.
    """
    self._original_state = dict(
        serializer=serializer,
        filename_template=filename_template,
        hash_salt=hash_salt,
        disable_shuffling=disable_shuffling,
        file_format=file_format,
        shard_config=shard_config,
    )
    self._filename_template = filename_template
    self._split_info_path = (
        f"{filename_template.filepath_prefix()}.split_info.json"
    )
    self._serializer = serializer
    self._hasher = hashing.Hasher(hash_salt)
    self._split_info = None
    self._file_format = file_format
    self._disable_shuffling = disable_shuffling
    self._shard_config = shard_config or shard_utils.ShardConfig()

  @functools.lru_cache()
  def _get_counter(self, name: str, namespace: str = "BeamWriter"):
    beam = lazy_imports_lib.lazy_imports.apache_beam
    return beam.metrics.Metrics.counter(namespace, name)

  @functools.lru_cache()
  def _get_distribution(self, name: str, namespace: str = "BeamWriter"):
    beam = lazy_imports_lib.lazy_imports.apache_beam
    return beam.metrics.Metrics.distribution(namespace, name)

  def inc_counter(self, name: str, value: int = 1) -> None:
    self._get_counter(name).inc(value)

  def __getstate__(self):
    return self._original_state

  def __setstate__(self, state):
    self.__init__(**state)

  def _serialize_example(
      self,
      key_example: Tuple[hashing.HashKey, Example],
  ) -> Tuple[Any, bytes]:
    """Returns (shard#, (hkey, serialized_example))."""
    key, example = key_example
    serialized_example = self._serializer.serialize_example(example)
    if self._disable_shuffling:
      hkey = key
    else:
      hkey = self._hasher.hash_key(key)
    self.inc_counter(name="serialized_examples")
    return (hkey, serialized_example)

  def _check_num_examples(self, num_examples: int) -> int:
    if num_examples <= 0:
      raise ValueError(
          f"The total number of generated examples is {num_examples}. This"
          " should be >0!"
      )
    return num_examples

  def _write_final_shard(
      self,
      shardid_examples: Tuple[int, Iterable[type_utils.KeySerializedExample]],
      non_empty_shard_ids: List[int],
  ) -> _ShardInfo:
    """Write all examples of a shard to disk.

    Arguments:
      shardid_examples: tuple of the shard id and the serialized examples that
        belong to that shard.
      non_empty_shard_ids: list of the shard ids of all the non-empty shards.
        Must be sorted.

    Returns:
      the shard info of the written shard.
    """
    original_shard_id, examples = shardid_examples
    if not examples:
      raise AssertionError("Not a single example present in the PCollection!")
    # There may be empty shards, this ensures there are no gaps.
    shard_id = non_empty_shard_ids.index(original_shard_id)
    examples = sorted(examples)
    self._get_distribution(name="ShardLenDistribution").update(len(examples))
    # Compare continuous examples
    for ex0, ex1 in zip(examples[:-1], examples[1:]):
      if ex0[0] == ex1[0]:  # Different keys
        _raise_error_for_duplicated_keys(
            ex0[1], ex1[1], self._serializer.example_specs
        )
    shard_path = self._filename_template.sharded_filepath(
        shard_index=shard_id, num_shards=len(non_empty_shard_ids)
    )
    with utils.incomplete_file(epath.Path(shard_path)) as tmp_path:
      logging.info(
          "Writing %d examples to %s.", len(examples), os.fspath(tmp_path)
      )
      record_keys = _write_examples(tmp_path, examples, self._file_format)
    self.inc_counter(name="written_shards")
    # If there are record_keys, create index files.
    if record_keys:
      index_path = _get_index_path(os.fspath(shard_path))
      _write_index_file(index_path, list(record_keys))
    shard_size = sum(map(len, examples))
    return _ShardInfo(id=shard_id, num_examples=len(examples), size=shard_size)

  def _number_of_shards(self, num_examples: int, total_size: int) -> int:
    """Returns the number of shards."""
    num_shards = self._shard_config.get_number_shards(
        total_size=total_size,
        num_examples=num_examples,
        uses_precise_sharding=False,
    )
    self.inc_counter(name="NumberOfShards", value=num_shards)
    return num_shards

  def _assign_shard(
      self,
      key_serialized_example: Tuple[Any, bytes],
      num_shards: int,
      largest_key: List[int],
  ) -> Tuple[int, Tuple[Any, bytes]]:
    """Assigns a shard id to the example."""
    key, _ = key_serialized_example
    largest_key = largest_key[0]
    shard_number = shuffle.get_bucket_number(
        hkey=key, num_buckets=num_shards, max_hkey=largest_key
    )
    self._get_distribution(name="ShardDistribution").update(shard_number)
    return (shard_number, key_serialized_example)

  def _store_split_info(
      self,
      shard_infos: List[_ShardInfo],
      total_size: int,
  ) -> None:
    """Stores the split info to disk."""
    shard_infos = sorted(shard_infos, key=lambda x: x.id)
    shard_lengths = [info.num_examples for info in shard_infos]
    with utils.incomplete_file(epath.Path(self._split_info_path)) as tmp_path:
      tmp_path.write_text(
          json.dumps({"total_size": total_size, "shard_lengths": shard_lengths})
      )

  def _sort_shard_ids(
      self, shard_ids: List[int], ideal_num_shards: int
  ) -> List[int]:
    """Returns the sorted shard ids and logs information."""
    if len(shard_ids) != ideal_num_shards:
      logging.info(
          "Ideally there would be %d shards, but got %d non-empty shards.",
          ideal_num_shards,
          len(shard_ids),
      )
    return sorted(shard_ids)

  def write_from_pcollection(self, examples_pcollection):
    """Returns PTransform to write (key, example) PCollection to tfrecords."""
    beam = lazy_imports_lib.lazy_imports.apache_beam
    serialized_examples = (
        examples_pcollection
        | "Serialize" >> beam.Map(self._serialize_example)
        # (key, serialized_example)
    )

    largest_key = (
        serialized_examples
        | beam.Keys()
        | "LargestKey" >> beam.combiners.Top.Largest(1)
    )
    num_examples = (
        serialized_examples
        | "CountExamples" >> beam.combiners.Count.Globally()
        | "CheckValidNumExamples" >> beam.Map(self._check_num_examples)
    )
    total_size = beam.pvalue.AsSingleton(
        serialized_examples
        | beam.Values()
        | beam.Map(len)
        | "TotalSize" >> beam.CombineGlobally(sum)
    )
    ideal_num_shards = beam.pvalue.AsSingleton(
        num_examples
        | "NumberOfShards"
        >> beam.Map(self._number_of_shards, total_size=total_size)
    )

    examples_per_shard = (
        serialized_examples
        | "AssignShard"
        >> beam.Map(
            self._assign_shard,
            largest_key=beam.pvalue.AsSingleton(largest_key),
            num_shards=ideal_num_shards,
        )
        # (shard_id, serialized_example)
        | "GroupShards" >> beam.GroupByKey()
        # (shard_id, [serialized_example])
    )

    # There may be shards that did not get assigned any examples. We will ignore
    # those shards and for that we need the ids of shards that are non-empty.
    non_empty_shard_ids = beam.pvalue.AsSingleton(
        examples_per_shard
        | "GetIdsOfNonEmptyShards" >> beam.Keys()
        | "CollectIdsOfNonEmptyShards" >> beam.transforms.combiners.ToList()
        | "SortIdsOfNonEmptyShards"
        >> beam.Map(self._sort_shard_ids, ideal_num_shards=ideal_num_shards)
    )

    return (
        examples_per_shard
        # (shard_id, [serialized_example])
        | "WriteFinalShards"
        >> beam.Map(
            self._write_final_shard, non_empty_shard_ids=non_empty_shard_ids
        )
        # (_ShardInfo)
        | "CollectShardInfo" >> beam.transforms.combiners.ToList()
        # [_ShardInfo]
        | "CalculateSplitInfo"
        >> beam.ParDo(self._store_split_info, total_size=total_size)
    )

  def finalize(self) -> Tuple[List[int], int]:
    """Deletes tmp directory and returns shard_lengths and total_size.

    Returns:
      List of length <number of shards> containing the number of examples stored
      in each shard, and size of the files (in bytes).
    """
    if self._split_info is None:
      split_info_path = epath.Path(self._split_info_path)
      self._split_info = json.loads(split_info_path.read_bytes())
      split_info_path.unlink()
    return self._split_info["shard_lengths"], self._split_info["total_size"]
