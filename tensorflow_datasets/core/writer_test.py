# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.writer."""

import os
from typing import List, Optional, Tuple
from unittest import mock

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_info as dataset_info_lib
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import utils
from tensorflow_datasets.core import writer as writer_lib
from tensorflow_datasets.core.proto import dataset_info_pb2
from tensorflow_datasets.core.utils import shard_utils
from tensorflow_datasets.core.writer import _ShardSpec


class GetShardSpecsTest(testing.TestCase):
  # Here we don't need to test all possible reading configs, as this is tested
  # by shard_utils.py.

  def test_1bucket_6shards(self):
    specs = writer_lib._get_shard_specs(
        num_examples=8,
        total_size=16,
        bucket_lengths=[8],
        filename_template=naming.ShardedFileTemplate(
            dataset_name='bar',
            split='train',
            data_dir='/',
            filetype_suffix='tfrecord',
        ),
        shard_config=shard_utils.ShardConfig(num_shards=6),
    )
    self.assertEqual(
        specs,
        [
            # Shard#, path, from_bucket, examples_number, reading instructions.
            _ShardSpec(
                0,
                '/bar-train.tfrecord-00000-of-00006',
                1,
                [
                    shard_utils.FileInstruction(
                        filename='0', skip=0, take=1, examples_in_shard=8
                    ),
                ],
            ),
            _ShardSpec(
                1,
                '/bar-train.tfrecord-00001-of-00006',
                2,
                [
                    shard_utils.FileInstruction(
                        filename='0', skip=1, take=2, examples_in_shard=8
                    ),
                ],
            ),
            _ShardSpec(
                2,
                '/bar-train.tfrecord-00002-of-00006',
                1,
                [
                    shard_utils.FileInstruction(
                        filename='0', skip=3, take=1, examples_in_shard=8
                    ),
                ],
            ),
            _ShardSpec(
                3,
                '/bar-train.tfrecord-00003-of-00006',
                1,
                [
                    shard_utils.FileInstruction(
                        filename='0', skip=4, take=1, examples_in_shard=8
                    ),
                ],
            ),
            _ShardSpec(
                4,
                '/bar-train.tfrecord-00004-of-00006',
                2,
                [
                    shard_utils.FileInstruction(
                        filename='0', skip=5, take=2, examples_in_shard=8
                    ),
                ],
            ),
            _ShardSpec(
                5,
                '/bar-train.tfrecord-00005-of-00006',
                1,
                [
                    shard_utils.FileInstruction(
                        filename='0', skip=7, take=1, examples_in_shard=8
                    ),
                ],
            ),
        ],
    )

  def test_4buckets_2shards(self):
    specs = writer_lib._get_shard_specs(
        num_examples=8,
        total_size=16,
        bucket_lengths=[2, 3, 0, 3],
        filename_template=naming.ShardedFileTemplate(
            dataset_name='bar',
            split='train',
            data_dir='/',
            filetype_suffix='tfrecord',
        ),
        shard_config=shard_utils.ShardConfig(num_shards=2),
    )
    self.assertEqual(
        specs,
        [
            # Shard#, path, examples_number, reading instructions.
            _ShardSpec(
                0,
                '/bar-train.tfrecord-00000-of-00002',
                4,
                [
                    shard_utils.FileInstruction(
                        filename='0', skip=0, take=2, examples_in_shard=2
                    ),
                    shard_utils.FileInstruction(
                        filename='1', skip=0, take=2, examples_in_shard=3
                    ),
                ],
            ),
            _ShardSpec(
                1,
                '/bar-train.tfrecord-00001-of-00002',
                4,
                [
                    shard_utils.FileInstruction(
                        filename='1', skip=2, take=-1, examples_in_shard=3
                    ),
                    shard_utils.FileInstruction(
                        filename='3', skip=0, take=-1, examples_in_shard=3
                    ),
                ],
            ),
        ],
    )


def _read_records(path, file_format=file_adapters.DEFAULT_FILE_FORMAT):
  """Returns (files_names, list_of_records_in_each_file).

  Args:
    path: path to tfrecord, omitting suffix.
    file_format: format of the record files.
  """
  # Ignore _index.json files.
  paths = sorted(tf.io.gfile.glob('%s-*-of-*' % path))
  all_recs = []
  for fpath in paths:
    data = file_adapters.ADAPTER_FOR_FORMAT[file_format].make_tf_data(fpath)
    all_recs.append(list(dataset_utils.as_numpy(data)))
  return [os.path.basename(p) for p in paths], all_recs


def _read_dataset_info_proto(path) -> dataset_info_pb2.DatasetInfo:
  return dataset_info_lib.read_proto_from_builder_dir(path)


class WriterTest(testing.TestCase):
  EMPTY_SPLIT_ERROR = 'No examples were yielded.'
  TOO_SMALL_SPLIT_ERROR = 'num_examples (1) < number_of_shards (2)'

  NUM_SHARDS = 5
  RECORDS_TO_WRITE = [
      (1, b'a'),
      (2, b'b'),
      (3, b'c'),
      (4, b'd'),
      (5, b'e'),
      (6, b'f'),
      (7, b'g'),
      (8, b'hi'),
  ]
  RECORDS_WITH_HOLES = [
      (1, b'a'),
      (2, b'b'),
      (3, b'c'),
      (4, b'd'),
      (50000, b'e'),
      (600000, b'f'),
      (7000000, b'g'),
      (80000000, b'hi'),
  ]
  SHARDS_CONTENT = [
      [b'f', b'g'],
      [b'd'],
      [b'a', b'b'],
      [b'hi'],
      [b'e', b'c'],
  ]
  SHARDS_CONTENT_NO_SHUFFLING = [
      [b'a', b'b'],
      [b'c'],
      [b'd', b'e'],
      [b'f'],
      [b'g', b'hi'],
  ]

  def _write(
      self,
      to_write,
      salt: str = '',
      dataset_name: str = 'foo',
      split: str = 'train',
      disable_shuffling=False,
      file_format=file_adapters.DEFAULT_FILE_FORMAT,
      shard_config: Optional[shard_utils.ShardConfig] = None,
  ):
    filetype_suffix = file_adapters.ADAPTER_FOR_FORMAT[file_format].FILE_SUFFIX
    filename_template = naming.ShardedFileTemplate(
        dataset_name=dataset_name,
        split=split,
        filetype_suffix=filetype_suffix,
        data_dir=self.tmp_dir,
    )
    shard_config = shard_config or shard_utils.ShardConfig(
        num_shards=self.NUM_SHARDS
    )
    writer = writer_lib.Writer(
        serializer=testing.DummySerializer('dummy specs'),
        filename_template=filename_template,
        hash_salt=salt,
        disable_shuffling=disable_shuffling,
        file_format=file_format,
        shard_config=shard_config,
    )
    for key, record in to_write:
      writer.write(key, record)
    return writer.finalize()

  def test_write_tfrecord(self):
    """Stores records as tfrecord in a fixed number of shards with shuffling."""
    path = os.path.join(self.tmp_dir, 'foo-train.tfrecord')
    shards_length, total_size = self._write(to_write=self.RECORDS_TO_WRITE)
    self.assertEqual(self.NUM_SHARDS, len(shards_length))
    self.assertEqual(
        shards_length, [len(shard) for shard in self.SHARDS_CONTENT]
    )
    self.assertEqual(total_size, 9)
    written_files, all_recs = _read_records(path)
    self.assertEqual(
        written_files,
        [
            f'foo-train.tfrecord-{i:05d}-of-{self.NUM_SHARDS:05d}'
            for i in range(self.NUM_SHARDS)
            if shards_length[i]
        ],
    )
    self.assertEqual(all_recs, self.SHARDS_CONTENT)

  def test_write_tfrecord_sorted_by_key(self):
    """Stores records as tfrecord in a fixed number of shards without shuffling."""
    path = os.path.join(self.tmp_dir, 'foo-train.tfrecord')
    shards_length, total_size = self._write(
        to_write=self.RECORDS_TO_WRITE, disable_shuffling=True
    )
    self.assertEqual(
        shards_length,
        [len(shard) for shard in self.SHARDS_CONTENT_NO_SHUFFLING],
    )
    self.assertEqual(total_size, 9)
    written_files, all_recs = _read_records(path)
    self.assertEqual(
        written_files,
        [
            f'foo-train.tfrecord-{i:05d}-of-{self.NUM_SHARDS:05d}'
            for i in range(self.NUM_SHARDS)
            if shards_length[i]
        ],
    )
    self.assertEqual(all_recs, self.SHARDS_CONTENT_NO_SHUFFLING)

  def test_write_tfrecord_sorted_by_key_with_holes(self):
    """Stores records as tfrecord in a fixed number of shards without shuffling."""
    path = os.path.join(self.tmp_dir, 'foo-train.tfrecord')
    shards_length, total_size = self._write(
        to_write=self.RECORDS_WITH_HOLES, disable_shuffling=True
    )
    self.assertEqual(
        shards_length,
        [len(shard) for shard in self.SHARDS_CONTENT_NO_SHUFFLING],
    )
    self.assertEqual(total_size, 9)
    written_files, all_recs = _read_records(path)
    self.assertEqual(
        written_files,
        [
            f'foo-train.tfrecord-{i:05d}-of-{self.NUM_SHARDS:05d}'
            for i in range(self.NUM_SHARDS)
            if shards_length[i]
        ],
    )
    self.assertEqual(all_recs, self.SHARDS_CONTENT_NO_SHUFFLING)

  @mock.patch.object(example_parser, 'ExampleParser', testing.DummyParser)
  def test_write_duplicated_keys(self):
    to_write = [(1, b'a'), (2, b'b'), (1, b'c')]
    with self.assertRaisesWithPredicateMatch(
        AssertionError, 'Two examples share the same hashed key'
    ):
      shard_config = shard_utils.ShardConfig(num_shards=1)
      self._write(to_write=to_write, shard_config=shard_config)

  def test_empty_split(self):
    to_write = []
    with self.assertRaisesWithPredicateMatch(
        AssertionError, self.EMPTY_SPLIT_ERROR
    ):
      shard_config = shard_utils.ShardConfig(num_shards=1)
      self._write(to_write=to_write, shard_config=shard_config)

  def test_too_small_split(self):
    to_write = [(1, b'a')]
    with self.assertRaisesWithPredicateMatch(
        AssertionError, self.TOO_SMALL_SPLIT_ERROR
    ):
      shard_config = shard_utils.ShardConfig(num_shards=2)
      self._write(to_write=to_write, shard_config=shard_config)
      self._write(to_write=to_write)


class BeamWriterTest(testing.TestCase):
  EMPTY_SPLIT_ERROR = 'Not a single example present in the PCollection!'
  NUM_SHARDS = 3
  RECORDS_TO_WRITE = [(i, str(i).encode('utf-8')) for i in range(10)]
  SHARDS_CONTENT = [
      [b'6', b'9'],
      [b'7'],
      [b'4', b'1', b'2', b'8', b'0', b'5', b'3'],
  ]
  NUM_BYTES = 10
  SHARDS_CONTENT_NO_SHUFFLING = [
      [b'0', b'1', b'2'],
      [b'3', b'4', b'5'],
      [b'6', b'7', b'8', b'9'],
  ]

  def _write(
      self,
      to_write: List[Tuple[int, str]],
      salt: str = '',
      dataset_name: str = 'foo',
      split: str = 'train',
      disable_shuffling=False,
      file_format=file_adapters.DEFAULT_FILE_FORMAT,
      shard_config: Optional[shard_utils.ShardConfig] = None,
  ):
    filetype_suffix = file_adapters.ADAPTER_FOR_FORMAT[file_format].FILE_SUFFIX
    filename_template = naming.ShardedFileTemplate(
        dataset_name=dataset_name,
        split=split,
        filetype_suffix=filetype_suffix,
        data_dir=self.tmp_dir,
    )
    shard_config = shard_config or shard_utils.ShardConfig(
        num_shards=self.NUM_SHARDS
    )
    beam = lazy_imports_lib.lazy_imports.apache_beam
    writer = writer_lib.BeamWriter(
        serializer=testing.DummySerializer('dummy specs'),
        filename_template=filename_template,
        hash_salt=salt,
        disable_shuffling=disable_shuffling,
        file_format=file_format,
        shard_config=shard_config,
    )
    dataset_info = dataset_info_lib.DatasetInfo(
        builder=dataset_info_lib.DatasetIdentity(
            name=dataset_name,
            version=utils.Version('1.0.0'),
            data_dir=self.tmp_dir,
            module_name='test',
        )
    )
    info_writer = writer_lib.DatasetInfoBeamWriter(
        dataset_info=dataset_info, filename_template=filename_template
    )
    # Here we need to disable type check as `beam.Create` is not capable of
    # inferring the type of the PCollection elements.
    options = beam.options.pipeline_options.PipelineOptions(
        pipeline_type_check=False
    )
    with beam.Pipeline(options=options) as pipeline:

      @beam.ptransform_fn
      def _build_pcollection(pipeline):
        pcollection = pipeline | 'Start' >> beam.Create(to_write)
        return writer.write_from_pcollection(pcollection, split_name=split)

      split_pcollectionms = [
          pipeline | 'test' >> _build_pcollection()  # pylint: disable=no-value-for-parameter
      ]
      split_infos = split_pcollectionms | 'Flatten' >> beam.Flatten()
      info_writer.write_dataset_info(split_infos)
    return _read_dataset_info_proto(self.tmp_dir)

  def _check_results(
      self,
      path,
      dataset_info,
      num_shards,
      num_bytes,
      shards_content,
      file_format=file_adapters.DEFAULT_FILE_FORMAT,
  ) -> None:
    self.assertEqual(len(dataset_info.splits), 1)
    split_info = dataset_info.splits[0]
    self.assertEqual(num_shards, len(split_info.shard_lengths))
    self.assertEqual(
        split_info.shard_lengths, [len(shard) for shard in shards_content]
    )
    self.assertEqual(split_info.num_bytes, num_bytes)
    written_files, all_recs = _read_records(path, file_format=file_format)
    self.assertEqual(
        written_files,
        [
            f'foo-train.{file_format.file_suffix}-{i:05d}-of-{num_shards:05d}'
            for i in range(num_shards)
            if split_info.shard_lengths[i]
        ],
    )
    self.assertEqual(all_recs, shards_content)

  def test_write_tfrecord(self):
    """Stores records as tfrecord in a fixed number of shards with shuffling."""
    path = os.path.join(self.tmp_dir, 'foo-train.tfrecord')
    dataset_info = self._write(to_write=self.RECORDS_TO_WRITE)
    self._check_results(
        path=path,
        dataset_info=dataset_info,
        num_shards=self.NUM_SHARDS,
        num_bytes=self.NUM_BYTES,
        shards_content=self.SHARDS_CONTENT,
    )

  def test_write_tfrecord_sorted_by_key(self):
    """Stores records as tfrecord in a fixed number of shards without shuffling."""
    path = os.path.join(self.tmp_dir, 'foo-train.tfrecord')
    dataset_info = self._write(
        to_write=self.RECORDS_TO_WRITE, disable_shuffling=True
    )
    self._check_results(
        path=path,
        dataset_info=dataset_info,
        num_shards=self.NUM_SHARDS,
        num_bytes=self.NUM_BYTES,
        shards_content=self.SHARDS_CONTENT_NO_SHUFFLING,
    )

  def test_write_tfrecord_sorted_by_key_with_holes(self):
    """Stores records as tfrecord in a fixed number of shards without shuffling.

    Note that the keys are not consecutive but contain gaps.
    """
    path = os.path.join(self.tmp_dir, 'foo-train.tfrecord')
    records_with_holes = [
        (i**4, str(i**4).encode('utf-8')) for i in range(10)
    ]
    expected_shards = [
        [b'0', b'1', b'16', b'81', b'256', b'625', b'1296'],
        [b'2401', b'4096'],
        [b'6561'],
    ]

    dataset_info = self._write(
        to_write=records_with_holes, disable_shuffling=True
    )
    self._check_results(
        path=path,
        dataset_info=dataset_info,
        num_shards=len(expected_shards),
        num_bytes=28,
        shards_content=expected_shards,
    )


if __name__ == '__main__':
  testing.test_main()
