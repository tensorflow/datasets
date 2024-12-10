# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.reader."""

import functools
import itertools
import os
from unittest import mock

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow_datasets import testing
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import file_adapters
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import reader as reader_lib
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import writer as writer_lib
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.core.utils import shard_utils

# Skip the cardinality test for backward compatibility with TF <= 2.1.
_SKIP_CARDINALITY_TEST = not hasattr(tf.data.experimental, 'assert_cardinality')

_SHUFFLE_FILES_ERROR_MESSAGE = (
    'Dataset is an ordered dataset '
    "('disable_shuffling=True'), but examples "
    'will not be read in order because '
    '`shuffle_files=True`.'
)
_CYCLE_LENGTH_ERROR_MESSAGE = (
    'Dataset is an ordered dataset '
    "('disable_shuffling=True'), but examples will"
    ' not be read in order because '
    '`ReadConfig.interleave_cycle_length != 1`.'
)


def _write_tfrecord_from_shard_spec(shard_spec, get):
  """Write tfrecord shard given shard_spec and buckets to read data from.

  Args:
    shard_spec: _ShardSpec, the spec for shard to write.
    get: callable taking the shard index (of bucket) and returning iterator over
      its elements.
  """
  iterators = []
  for instruction in shard_spec.file_instructions:
    iterator = get(int(instruction.filename))
    skip, take = instruction.skip, instruction.take
    stop = skip + take if take > 0 else None
    iterators.append(itertools.islice(iterator, skip, stop))
  example_writer = writer_lib.ExampleWriter(
      file_format=file_adapters.FileFormat.TFRECORD
  )
  example_writer.write(shard_spec.path, itertools.chain(*iterators))


class ReaderTest(testing.TestCase):

  def setUp(self):
    super(ReaderTest, self).setUp()
    with mock.patch.object(
        example_parser, 'ExampleParser', testing.DummyParser
    ):
      self.reader = reader_lib.Reader(self.tmp_dir, 'tfrecord')
      self.reader.read = functools.partial(
          self.reader.read,
          read_config=read_config_lib.ReadConfig(),
          shuffle_files=False,
      )

  def _filename_template(self, split: str) -> naming.ShardedFileTemplate:
    return naming.ShardedFileTemplate(
        dataset_name='mnist',
        split=split,
        filetype_suffix='tfrecord',
        data_dir=self.tmp_dir,
    )

  def _write_tfrecord(self, split_name, shards_number, records):
    filename_template = self._filename_template(split=split_name)
    num_examples = len(records)
    shard_specs = writer_lib._get_shard_specs(
        num_examples=num_examples,
        total_size=0,
        bucket_lengths=[num_examples],
        filename_template=filename_template,
        shard_config=shard_utils.ShardConfig(num_shards=shards_number),
    )
    serialized_records = [
        (key, bytes(rec, encoding='utf-8')) for key, rec in enumerate(records)
    ]
    for shard_spec in shard_specs:
      _write_tfrecord_from_shard_spec(
          shard_spec, lambda unused_i: iter(serialized_records)
      )
    return splits.SplitInfo(
        name=split_name,
        shard_lengths=[int(s.examples_number) for s in shard_specs],
        num_bytes=0,
        filename_template=filename_template,
    )

  def test_nodata_instruction(self):
    # Given instruction corresponds to no data.
    with self.assertRaisesWithPredicateMatch(
        ValueError, 'corresponds to no data!'
    ):
      train_info = splits.SplitInfo(
          name='train',
          shard_lengths=[2, 3, 2, 3, 2],
          num_bytes=0,
          filename_template=self._filename_template(split='train'),
      )
      self.reader.read(
          instructions='train[0:0]',
          split_infos=[train_info],
      )

  def test_noskip_notake(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    ds = self.reader.read(
        instructions='train',
        split_infos=[train_info],
    )
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(
        read_data, [bytes(l, encoding='utf-8') for l in 'abcdefghijkl']
    )

    if not _SKIP_CARDINALITY_TEST:
      # Check that the cardinality is correctly set.
      self.assertEqual(ds.cardinality().numpy(), len(read_data))

  def test_overlap(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    ds = self.reader.read(
        instructions='train+train[:2]',
        split_infos=[train_info],
    )
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(
        read_data, [bytes(l, encoding='utf-8') for l in 'abcdefghijklab']
    )

    if not _SKIP_CARDINALITY_TEST:
      # Check that the cardinality is correctly set.
      self.assertEqual(ds.cardinality().numpy(), len(read_data))

  def test_complex(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    test_info = self._write_tfrecord('test', 3, 'mnopqrs')
    self.assertEqual(train_info.name, 'train')
    self.assertEqual(test_info.name, 'test')
    self.assertEqual(train_info.shard_lengths, [2, 3, 2, 3, 2])  # 12 ex.
    self.assertEqual(test_info.shard_lengths, [2, 3, 2])  # 7 ex.
    split_info = [train_info, test_info]
    ds = self.reader.read(
        instructions='train[1:-1]+test[:-50%]',
        split_infos=split_info,
    )
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(
        read_data, [bytes(l, encoding='utf-8') for l in 'bcdefghijkmno']
    )

    if not _SKIP_CARDINALITY_TEST:
      # Check that the cardinality is correctly set.
      self.assertEqual(ds.cardinality().numpy(), len(read_data))

  def test_shuffle_files(self):
    chars = 'abcdefghijkl'
    train_info = self._write_tfrecord('train', 5, chars)
    ds = self.reader.read(
        instructions='train',
        split_infos=[train_info],
        shuffle_files=True,
    )
    ds = ds.batch(12).repeat(100)
    read_data = set(tuple(e) for e in tfds.as_numpy(ds))
    for batch in read_data:
      # Check that `batch` contains all the chars exactly once.
      batch_set = set(batch)
      self.assertEqual(len(batch_set), len(chars))
    # There are theoretically 5! (=120) different arrangements, but we would
    # need too many repeats to be sure to get them.
    self.assertGreater(len(set(read_data)), 10)

  def test_shuffle_deterministic(self):
    split_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    read_config = read_config_lib.ReadConfig(
        shuffle_seed=123,
    )
    ds = self.reader.read(
        instructions='train',
        split_infos=[split_info],
        read_config=read_config,
        shuffle_files=True,
    )
    ds_values = list(tfds.as_numpy(ds))

    # Check that shuffle=True with a seed provides deterministic results.
    self.assertEqual(
        ds_values,
        [
            b'a',
            b'b',
            b'k',
            b'l',
            b'h',
            b'i',
            b'j',
            b'c',
            b'd',
            b'e',
            b'f',
            b'g',
        ],
    )

  def test_4fold(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    instructions = [
        splits.ReadInstruction('train', from_=k, to=k + 25, unit='%')
        for k in range(0, 100, 25)
    ]
    tests = self.reader.read(
        instructions=instructions,
        split_infos=[train_info],
    )
    instructions = [
        (
            splits.ReadInstruction('train', to=k, unit='%')
            + splits.ReadInstruction('train', from_=k + 25, unit='%')
        )
        for k in range(0, 100, 25)
    ]
    trains = self.reader.read(
        instructions=instructions,
        split_infos=[train_info],
    )
    read_tests = [list(r) for r in tfds.as_numpy(tests)]
    read_trains = [list(r) for r in tfds.as_numpy(trains)]
    self.assertEqual(
        read_tests,
        [
            [b'a', b'b', b'c'],
            [b'd', b'e', b'f'],
            [b'g', b'h', b'i'],
            [b'j', b'k', b'l'],
        ],
    )
    self.assertEqual(
        read_trains,
        [
            [b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l'],
            [b'a', b'b', b'c', b'g', b'h', b'i', b'j', b'k', b'l'],
            [b'a', b'b', b'c', b'd', b'e', b'f', b'j', b'k', b'l'],
            [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i'],
        ],
    )

  def test_read_files(self):
    self._write_tfrecord('train', 4, 'abcdefghijkl')
    filename_template = self._filename_template(split='train')
    ds = self.reader.read_files(
        [
            shard_utils.FileInstruction(
                filename=os.fspath(
                    filename_template.sharded_filepath(
                        shard_index=1, num_shards=4
                    )
                ),
                skip=0,
                take=-1,
                examples_in_shard=3,
            ),
            shard_utils.FileInstruction(
                filename=os.fspath(
                    filename_template.sharded_filepath(
                        shard_index=3, num_shards=4
                    )
                ),
                skip=1,
                take=1,
                examples_in_shard=3,
            ),
        ],
        read_config=read_config_lib.ReadConfig(),
        shuffle_files=False,
    )
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(read_data, [bytes(l, encoding='utf-8') for l in 'defk'])

  def test_input_context(self):
    split_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    self.assertEqual(split_info.shard_lengths, [2, 3, 2, 3, 2])

    def read(num_workers, index):
      return list(
          tfds.as_numpy(
              self.reader.read(
                  instructions='train',
                  split_infos=[split_info],
                  read_config=read_config_lib.ReadConfig(
                      input_context=tf.distribute.InputContext(
                          num_input_pipelines=num_workers,
                          input_pipeline_id=index,
                      ),
                  ),
                  # Workers should read a deterministic subset of the examples,
                  # even if examples within one worker may be shuffled.
                  shuffle_files=True,
              )
          )
      )

    def _b(bytes_str):
      # Convert to List[bytes] (rather than List[int])
      return [bytes([b]) for b in bytes_str]

    # Read all the data (single pipeline)
    self.assertCountEqual(read(num_workers=1, index=0), _b(b'abcdefghijkl'))
    # Read part of the data (workers should not overlapp)
    self.assertCountEqual(read(num_workers=3, index=0), _b(b'abhij'))  # 0, 3
    self.assertCountEqual(read(num_workers=3, index=1), _b(b'cdekl'))  # 1, 4
    self.assertEqual(read(num_workers=3, index=2), _b(b'fg'))  # Shards 2
    # If num_workers == num_shards, then a single shard is read
    self.assertEqual(read(num_workers=5, index=1), _b(b'cde'))  # Shard 1
    # If num_workers > num_shards, raise error
    with self.assertRaisesRegex(ValueError, 'Cannot shard the pipeline'):
      read(num_workers=6, index=0)

  def test_shuffle_files_should_be_disabled(self):
    self._write_tfrecord('train', 4, 'abcdefghijkl')
    filename_template = self._filename_template(split='train')
    with self.assertRaisesWithPredicateMatch(
        ValueError, _SHUFFLE_FILES_ERROR_MESSAGE
    ):
      self.reader.read_files(
          [
              shard_utils.FileInstruction(
                  filename=os.fspath(
                      filename_template.sharded_filepath(
                          shard_index=1, num_shards=4
                      )
                  ),
                  skip=0,
                  take=-1,
                  examples_in_shard=3,
              ),
          ],
          read_config=read_config_lib.ReadConfig(),
          shuffle_files=True,
          disable_shuffling=True,
      )

  def test_cycle_length_must_be_one(self):
    self._write_tfrecord('train', 4, 'abcdefghijkl')
    filename_template = self._filename_template(split='train')
    instructions = [
        shard_utils.FileInstruction(
            filename=os.fspath(
                filename_template.sharded_filepath(shard_index=1, num_shards=4)
            ),
            skip=0,
            take=-1,
            examples_in_shard=3,
        ),
    ]
    # In ordered dataset interleave_cycle_length is set to 1 by default
    self.reader.read_files(
        instructions,
        read_config=read_config_lib.ReadConfig(),
        shuffle_files=False,
        disable_shuffling=True,
    )
    with self.assertRaisesWithPredicateMatch(
        ValueError, _CYCLE_LENGTH_ERROR_MESSAGE
    ):
      self.reader.read_files(
          instructions,
          read_config=read_config_lib.ReadConfig(interleave_cycle_length=16),
          shuffle_files=False,
          disable_shuffling=True,
      )

  def test_ordering_guard(self):
    self._write_tfrecord('train', 4, 'abcdefghijkl')
    filename_template = self._filename_template(split='train')
    instructions = [
        shard_utils.FileInstruction(
            filename=filename_template.sharded_filepath(
                shard_index=1, num_shards=4
            ),
            skip=0,
            take=-1,
            examples_in_shard=3,
        ),
    ]
    reported_warnings = []
    with mock.patch('absl.logging.warning', reported_warnings.append):
      self.reader.read_files(
          instructions,
          read_config=read_config_lib.ReadConfig(
              interleave_cycle_length=16, enable_ordering_guard=False
          ),
          shuffle_files=True,
          disable_shuffling=True,
      )
      expected_warning = (
          _SHUFFLE_FILES_ERROR_MESSAGE + '\n' + _CYCLE_LENGTH_ERROR_MESSAGE
      )
      self.assertIn(expected_warning, reported_warnings)

  @mock.patch(
      'tensorflow.data.experimental.assert_cardinality',
      wraps=tf.data.experimental.assert_cardinality,
  )
  def test_assert_cardinality_is_on_by_default(self, assert_cardinality):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    self.reader.read(instructions='train', split_infos=[train_info])
    assert_cardinality.assert_called_with(12)

  @mock.patch('tensorflow.data.experimental.assert_cardinality')
  def test_assert_cardinality_can_be_disabled_through_readconfig(
      self, assert_cardinality
  ):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    self.reader.read(
        instructions='train',
        split_infos=[train_info],
        read_config=read_config_lib.ReadConfig(assert_cardinality=False),
    )
    assert not assert_cardinality.called


def test_shard_api():
  si = tfds.core.SplitInfo(
      name='train',
      shard_lengths=[10, 20, 13],
      num_bytes=0,
      filename_template=naming.ShardedFileTemplate(
          dataset_name='ds_name',
          split='train',
          filetype_suffix='tfrecord',
          data_dir='/path',
      ),
  )
  fi = [
      shard_utils.FileInstruction(
          filename='/path/ds_name-train.tfrecord-00000-of-00003',
          skip=0,
          take=-1,
          examples_in_shard=10,
      ),
      shard_utils.FileInstruction(
          filename='/path/ds_name-train.tfrecord-00001-of-00003',
          skip=0,
          take=-1,
          examples_in_shard=20,
      ),
      shard_utils.FileInstruction(
          filename='/path/ds_name-train.tfrecord-00002-of-00003',
          skip=0,
          take=-1,
          examples_in_shard=13,
      ),
  ]
  sd = splits.SplitDict([si])
  assert sd['train[0shard]'].file_instructions == [fi[0]]
  assert sd['train[1shard]'].file_instructions == [fi[1]]
  assert sd['train[-1shard]'].file_instructions == [fi[-1]]
  assert sd['train[-2shard]'].file_instructions == [fi[-2]]
  assert sd['train[:2shard]'].file_instructions == fi[:2]
  assert sd['train[1shard:]'].file_instructions == fi[1:]
  assert sd['train[-1shard:]'].file_instructions == fi[-1:]
  assert sd['train[1:-1shard]'].file_instructions == fi[1:-1]


class AddTfdsIdTest(testing.TestCase):

  def test_get_tfds_id_prefixes_single_directory(self):
    file_instructions = [
        shard_utils.FileInstruction('/a/b/f1', 0, -1, 1),
        shard_utils.FileInstruction('/a/b/f2', 0, -1, 1),
    ]
    actual = reader_lib._get_tfds_id_prefixes(file_instructions)
    self.assertEqual(actual, {'/a/b/f1': 'f1', '/a/b/f2': 'f2'})

  def test_get_tfds_id_prefixes_multiple_directories(self):
    file_instructions = [
        shard_utils.FileInstruction('/a/b/f1', 0, -1, 1),
        shard_utils.FileInstruction('/a/b/f2', 0, -1, 1),
        shard_utils.FileInstruction('/x/y/z/f1', 0, -1, 1),
        shard_utils.FileInstruction('/a/c/f1', 0, -1, 1),
        shard_utils.FileInstruction('/a/b/c/d/e/f1', 0, -1, 1),
    ]
    actual = reader_lib._get_tfds_id_prefixes(file_instructions)
    expected = {
        '/a/b/c/d/e/f1': 'e/f1',
        '/a/b/f1': 'b/f1',
        '/a/b/f2': 'b/f2',
        '/a/c/f1': 'c/f1',
        '/x/y/z/f1': 'z/f1',
    }
    self.assertEqual(actual, expected)


if __name__ == '__main__':
  testing.test_main()
