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

"""Tests for tensorflow_datasets.core.tfrecords_writer."""

import json
import os
from unittest import mock

import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import dataset_utils
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import example_serializer
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import lazy_imports_lib
from tensorflow_datasets.core import tfrecords_writer
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.tfrecords_writer import _ShardSpec
from tensorflow_datasets.core.utils import shard_utils


class GetShardSpecsTest(testing.TestCase):
  # Here we don't need to test all possible reading configs, as this is tested
  # by shard_utils.py.

  @mock.patch.object(tfrecords_writer, '_get_number_shards',
                     mock.Mock(return_value=6))
  def test_1bucket_6shards(self):
    specs = tfrecords_writer._get_shard_specs(
        num_examples=8, total_size=16, bucket_lengths=[8], path='/bar.tfrecord')
    self.assertEqual(
        specs,
        [
            # Shard#, path, from_bucket, examples_number, reading instructions.
            _ShardSpec(0, '/bar.tfrecord-00000-of-00006',
                       '/bar.tfrecord-00000-of-00006_index.json', 1, [
                           shard_utils.FileInstruction(
                               filename='0', skip=0, take=1, num_examples=1),
                       ]),
            _ShardSpec(1, '/bar.tfrecord-00001-of-00006',
                       '/bar.tfrecord-00001-of-00006_index.json', 2, [
                           shard_utils.FileInstruction(
                               filename='0', skip=1, take=2, num_examples=2),
                       ]),
            _ShardSpec(2, '/bar.tfrecord-00002-of-00006',
                       '/bar.tfrecord-00002-of-00006_index.json', 1, [
                           shard_utils.FileInstruction(
                               filename='0', skip=3, take=1, num_examples=1),
                       ]),
            _ShardSpec(3, '/bar.tfrecord-00003-of-00006',
                       '/bar.tfrecord-00003-of-00006_index.json', 1, [
                           shard_utils.FileInstruction(
                               filename='0', skip=4, take=1, num_examples=1),
                       ]),
            _ShardSpec(4, '/bar.tfrecord-00004-of-00006',
                       '/bar.tfrecord-00004-of-00006_index.json', 2, [
                           shard_utils.FileInstruction(
                               filename='0', skip=5, take=2, num_examples=2),
                       ]),
            _ShardSpec(5, '/bar.tfrecord-00005-of-00006',
                       '/bar.tfrecord-00005-of-00006_index.json', 1, [
                           shard_utils.FileInstruction(
                               filename='0', skip=7, take=-1, num_examples=1),
                       ]),
        ])

  @mock.patch.object(tfrecords_writer, '_get_number_shards',
                     mock.Mock(return_value=2))
  def test_4buckets_2shards(self):
    specs = tfrecords_writer._get_shard_specs(
        num_examples=8,
        total_size=16,
        bucket_lengths=[2, 3, 0, 3],
        path='/bar.tfrecord')
    self.assertEqual(
        specs,
        [
            # Shard#, path, examples_number, reading instructions.
            _ShardSpec(0, '/bar.tfrecord-00000-of-00002',
                       '/bar.tfrecord-00000-of-00002_index.json', 4, [
                           shard_utils.FileInstruction(
                               filename='0', skip=0, take=-1, num_examples=2),
                           shard_utils.FileInstruction(
                               filename='1', skip=0, take=2, num_examples=2),
                       ]),
            _ShardSpec(1, '/bar.tfrecord-00001-of-00002',
                       '/bar.tfrecord-00001-of-00002_index.json', 4, [
                           shard_utils.FileInstruction(
                               filename='1', skip=2, take=-1, num_examples=1),
                           shard_utils.FileInstruction(
                               filename='3', skip=0, take=-1, num_examples=3),
                       ]),
        ])


class GetNumberShardsTest(testing.TestCase):

  def test_imagenet_train(self):
    size = 137 << 30  # 137 GiB
    num_examples = 1281167
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 1024)

  def test_imagenet_evaluation(self):
    size = 6300 * (1 << 20)  # 6.3 GiB
    num_examples = 50000
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 64)

  def test_verylarge_few_examples(self):
    size = 52 << 30  # 52 GiB
    num_examples = 512
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 512)

  def test_xxl(self):
    size = 10 << 40  # 10 TiB
    num_examples = 10**9  # 1G
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 11264)

  def test_xs(self):
    size = 100 << 20  # 100 MiB
    num_examples = 100 * 10**3  # 100K
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 1)

  def test_m(self):
    size = 400 << 20  # 499 MiB
    num_examples = 200 * 10**3  # 200K
    n = tfrecords_writer._get_number_shards(size, num_examples)
    self.assertEqual(n, 4)


def _read_records(path, file_format=file_adapters.DEFAULT_FILE_FORMAT):
  """Returns (files_names, list_of_records_in_each_file).

  Args:
    path: path to tfrecord, omitting suffix.
    file_format: format of the record files.
  """
  # Ignore _index.json files.
  paths = sorted(tf.io.gfile.glob('%s-*-of-*' % path))
  paths = [
      p for p in paths if not p.endswith(tfrecords_writer._INDEX_PATH_SUFFIX)
  ]
  all_recs = []
  for fpath in paths:
    all_recs.append(
        list(
            dataset_utils.as_numpy(
                file_adapters.ADAPTER_FOR_FORMAT[file_format].make_tf_data(
                    fpath))))
  return [os.path.basename(p) for p in paths], all_recs


def _read_indices(path):
  """Returns (files_name, list of index in each file).

  Args:
    path: path to index, omitting suffix.
  """
  paths = sorted(tf.io.gfile.glob('%s-*-of-*_index.json' % path))
  all_indices = []
  for path in paths:
    json_str = utils.as_path(path).read_text()
    # parse it back into a proto.
    shard_index = json.loads(json_str)
    all_indices.append(list(shard_index['index']))
  return [os.path.basename(p) for p in paths], all_indices


class WriterTest(testing.TestCase):

  EMPTY_SPLIT_ERROR = 'No examples were yielded.'
  TOO_SMALL_SPLIT_ERROR = 'num_examples (1) < number_of_shards (2)'
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

  @mock.patch.object(example_serializer, 'ExampleSerializer',
                     testing.DummySerializer)
  def _write(self,
             to_write,
             path,
             salt='',
             disable_shuffling=False,
             file_format=file_adapters.DEFAULT_FILE_FORMAT):
    writer = tfrecords_writer.Writer(
        'some spec',
        path,
        hash_salt=salt,
        disable_shuffling=disable_shuffling,
        file_format=file_format)
    for key, record in to_write:
      writer.write(key, record)
    return writer.finalize()

  def test_write_tfrecord(self):
    """Writes 8 records in 5 shards.

    Number of records is evenly distributed (2-1-2-1-2).
    """
    path = os.path.join(self.tmp_dir, 'foo.tfrecord')
    with mock.patch.object(
        tfrecords_writer, '_get_number_shards', return_value=5):
      shards_length, total_size = self._write(self.RECORDS_TO_WRITE, path)
    self.assertEqual(shards_length, [2, 1, 2, 1, 2])
    self.assertEqual(total_size, 9)
    written_files, all_recs = _read_records(path)
    written_index_files, all_indices = _read_indices(path)
    self.assertEqual(written_files,
                     ['foo.tfrecord-0000%s-of-00005' % i for i in range(5)])
    self.assertEqual(all_recs, [
        [b'f', b'g'],
        [b'd'],
        [b'a', b'b'],
        [b'hi'],
        [b'e', b'c'],
    ])
    self.assertEmpty(written_index_files)
    self.assertEmpty(all_indices)

  def test_write_tfrecord_sorted_by_key(self):
    """Writes 8 records in 5 shards without shuffling.

    Number of records is evenly distributed (2-1-2-1-2).
    """
    path = os.path.join(self.tmp_dir, 'foo.tfrecord')
    with mock.patch.object(
        tfrecords_writer, '_get_number_shards', return_value=5):
      shards_length, total_size = self._write(
          self.RECORDS_TO_WRITE, path, disable_shuffling=True)
    self.assertEqual(shards_length, [2, 1, 2, 1, 2])
    self.assertEqual(total_size, 9)
    written_files, all_recs = _read_records(path)
    written_index_files, all_indices = _read_indices(path)
    self.assertEqual(written_files,
                     ['foo.tfrecord-0000%s-of-00005' % i for i in range(5)])
    self.assertEqual(all_recs, [
        [b'a', b'b'],
        [b'c'],
        [b'd', b'e'],
        [b'f'],
        [b'g', b'hi'],
    ])
    self.assertEmpty(written_index_files)
    self.assertEmpty(all_indices)

  @mock.patch.object(example_parser, 'ExampleParser', testing.DummyParser)
  def test_write_duplicated_keys(self):
    path = os.path.join(self.tmp_dir, 'foo.tfrecord')
    to_write = [(1, b'a'), (2, b'b'), (1, b'c')]
    with mock.patch.object(
        tfrecords_writer, '_get_number_shards', return_value=1):
      with self.assertRaisesWithPredicateMatch(
          AssertionError, 'Two examples share the same hashed key'):
        self._write(to_write, path)

  def test_empty_split(self):
    path = os.path.join(self.tmp_dir, 'foo.tfrecord')
    to_write = []
    with mock.patch.object(
        tfrecords_writer, '_get_number_shards', return_value=1):
      with self.assertRaisesWithPredicateMatch(AssertionError,
                                               self.EMPTY_SPLIT_ERROR):
        self._write(to_write, path)

  def test_too_small_split(self):
    path = os.path.join(self.tmp_dir, 'foo.tfrecord')
    to_write = [(1, b'a')]
    with mock.patch.object(
        tfrecords_writer, '_get_number_shards', return_value=2):
      with self.assertRaisesWithPredicateMatch(AssertionError,
                                               self.TOO_SMALL_SPLIT_ERROR):
        self._write(to_write, path)


class TfrecordsWriterBeamTest(WriterTest):

  EMPTY_SPLIT_ERROR = 'Not a single example present in the PCollection!'

  @mock.patch.object(example_serializer, 'ExampleSerializer',
                     testing.DummySerializer)
  def _write(self,
             to_write,
             path,
             salt='',
             disable_shuffling=False,
             file_format=file_adapters.DEFAULT_FILE_FORMAT):
    beam = lazy_imports_lib.lazy_imports.apache_beam
    writer = tfrecords_writer.BeamWriter(
        'some spec',
        path,
        salt,
        disable_shuffling=disable_shuffling,
        file_format=file_format,
    )
    # Here we need to disable type check as `beam.Create` is not capable of
    # inferring the type of the PCollection elements.
    options = beam.options.pipeline_options.PipelineOptions(
        pipeline_type_check=False)
    with beam.Pipeline(options=options) as pipeline:

      @beam.ptransform_fn
      def _build_pcollection(pipeline):
        pcollection = pipeline | 'Start' >> beam.Create(to_write)
        return writer.write_from_pcollection(pcollection)

      _ = pipeline | 'test' >> _build_pcollection()  # pylint: disable=no-value-for-parameter
    return writer.finalize()


if __name__ == '__main__':
  testing.test_main()
