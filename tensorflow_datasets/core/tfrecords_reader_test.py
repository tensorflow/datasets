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

"""Tests for tensorflow_datasets.core.tfrecords_reader."""

import functools
import itertools
import os
from unittest import mock

import six

import tensorflow.compat.v2 as tf

import tensorflow_datasets as tfds
from tensorflow_datasets import testing
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import tfrecords_reader
from tensorflow_datasets.core import tfrecords_writer
from tensorflow_datasets.core.utils import read_config as read_config_lib
from tensorflow_datasets.core.utils import shard_utils

# Skip the cardinality test for backward compatibility with TF <= 2.1.
_SKIP_CARDINALITY_TEST = not hasattr(tf.data.experimental, 'assert_cardinality')

_SHUFFLE_FILES_ERROR_MESSAGE = ('Dataset is an ordered dataset '
                                '(\'disable_shuffling=True\'), but examples '
                                'will not be read in order because '
                                '`shuffle_files=True`.')
_CYCLE_LENGTH_ERROR_MESSAGE = ('Dataset is an ordered dataset '
                               '(\'disable_shuffling=True\'), but examples will'
                               ' not be read in order because '
                               '`ReadConfig.interleave_cycle_length != 1`.')


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
  tfrecords_writer._write_examples(shard_spec.path, itertools.chain(*iterators))


class GetDatasetFilesTest(testing.TestCase):

  NAME2SHARD_LENGTHS = {
      'train': [3, 2, 3, 2, 3],  # 13 examples.
  }

  PATH_PATTERN = 'mnist-train.tfrecord-0000%d-of-00005'

  def _get_files(self, instruction):
    file_instructions = tfrecords_reader._make_file_instructions_from_absolutes(
        name='mnist',
        name2shard_lengths=self.NAME2SHARD_LENGTHS,
        absolute_instructions=[instruction],
    )
    return file_instructions

  def test_no_skip_no_take(self):
    instruction = tfrecords_reader._AbsoluteInstruction('train', None, None)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % i, skip=0, take=-1, num_examples=n)
        for i, n in enumerate([3, 2, 3, 2, 3])
    ])

  def test_skip(self):
    # One file is not taken, one file is partially taken.
    instruction = tfrecords_reader._AbsoluteInstruction('train', 4, None)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 1, skip=1, take=-1, num_examples=1),
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 2, skip=0, take=-1, num_examples=3),
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 3, skip=0, take=-1, num_examples=2),
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 4, skip=0, take=-1, num_examples=3),
    ])

  def test_take(self):
    # Two files are not taken, one file is partially taken.
    instruction = tfrecords_reader._AbsoluteInstruction('train', None, 6)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 0, skip=0, take=-1, num_examples=3),
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 1, skip=0, take=-1, num_examples=2),
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 2, skip=0, take=1, num_examples=1),
    ])

  def test_skip_take1(self):
    # A single shard with both skip and take.
    instruction = tfrecords_reader._AbsoluteInstruction('train', 1, 2)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 0, skip=1, take=1, num_examples=1),
    ])

  def test_skip_take2(self):
    # 2 elements in across two shards are taken in middle.
    instruction = tfrecords_reader._AbsoluteInstruction('train', 7, 9)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 2, skip=2, take=-1, num_examples=1),
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 3, skip=0, take=1, num_examples=1),
    ])

  def test_touching_boundaries(self):
    # Nothing to read.
    instruction = tfrecords_reader._AbsoluteInstruction('train', 0, 0)
    files = self._get_files(instruction)
    self.assertEqual(files, [])

    instruction = tfrecords_reader._AbsoluteInstruction('train', None, 0)
    files = self._get_files(instruction)
    self.assertEqual(files, [])

    instruction = tfrecords_reader._AbsoluteInstruction('train', 3, 3)
    files = self._get_files(instruction)
    self.assertEqual(files, [])

    instruction = tfrecords_reader._AbsoluteInstruction('train', 13, None)
    files = self._get_files(instruction)
    self.assertEqual(files, [])

  def test_missing_shard_lengths(self):
    with self.assertRaisesWithPredicateMatch(ValueError, 'Shard empty.'):
      split_info = [
          splits.SplitInfo(name='train', shard_lengths=[], num_bytes=0),
      ]
      tfrecords_reader.make_file_instructions('mnist', split_info, 'train')


class ReadInstructionTest(testing.TestCase):

  def setUp(self):
    super(ReadInstructionTest, self).setUp()
    self.splits = {'train': 200, 'test': 101, 'validation': 30, 'dev-train': 10}

  def check_from_ri(self, ri, expected):
    res = ri.to_absolute(self.splits)
    expected_result = []
    for split_name, from_, to_ in expected:
      expected_result.append(
          tfrecords_reader._AbsoluteInstruction(split_name, from_, to_))
    self.assertEqual(res, expected_result)
    return ri

  def check_from_spec(self, spec, expected):
    ri = tfrecords_reader.ReadInstruction.from_spec(spec)
    return self.check_from_ri(ri, expected)

  def assertRaises(self, spec, msg, exc_cls=AssertionError):
    with self.assertRaisesWithPredicateMatch(exc_cls, msg):
      ri = tfrecords_reader.ReadInstruction.from_spec(spec)
      ri.to_absolute(self.splits)

  def test_valid(self):
    # Simple split:
    ri = self.check_from_spec('train', [('train', None, None)])
    self.assertEqual(
        str(ri),
        ('ReadInstruction(['
         "_RelativeInstruction(splitname='train', from_=None, to=None, "
         "unit='abs', rounding='closest')])"))
    self.check_from_spec('test', [('test', None, None)])
    # Addition of splits:
    self.check_from_spec('train+test', [
        ('train', None, None),
        ('test', None, None),
    ])
    # Absolute slicing:
    self.check_from_spec('train[0:0]', [('train', None, 0)])
    self.check_from_spec('train[:10]', [('train', None, 10)])
    self.check_from_spec('train[0:10]', [('train', None, 10)])
    self.check_from_spec('train[-10:]', [('train', 190, None)])
    self.check_from_spec('train[-100:-50]', [('train', 100, 150)])
    self.check_from_spec('train[-10:200]', [('train', 190, None)])
    self.check_from_spec('train[10:-10]', [('train', 10, 190)])
    self.check_from_spec('train[42:99]', [('train', 42, 99)])
    # Percent slicing, closest rounding:
    self.check_from_spec('train[:10%]', [('train', None, 20)])
    self.check_from_spec('train[90%:]', [('train', 180, None)])
    self.check_from_spec('train[-1%:]', [('train', 198, None)])
    ri = self.check_from_spec('test[:99%]', [('test', None, 100)])
    self.assertEqual(
        str(ri),
        ("ReadInstruction([_RelativeInstruction(splitname='test', from_=None,"
         " to=99, unit='%', rounding='closest')])"))
    # No overlap:
    self.check_from_spec('test[100%:]', [('test', 101, None)])
    # Percent slicing, pct1_dropremainder rounding:
    ri = tfrecords_reader.ReadInstruction(
        'train', to=20, unit='%', rounding='pct1_dropremainder')
    self.check_from_ri(ri, [('train', None, 40)])
    # test split has 101 examples.
    ri = tfrecords_reader.ReadInstruction(
        'test', to=100, unit='%', rounding='pct1_dropremainder')
    self.check_from_ri(ri, [('test', None, 100)])
    # No overlap using 'pct1_dropremainder' rounding:
    ri1 = tfrecords_reader.ReadInstruction(
        'test', to=99, unit='%', rounding='pct1_dropremainder')
    ri2 = tfrecords_reader.ReadInstruction(
        'test', from_=100, unit='%', rounding='pct1_dropremainder')
    self.check_from_ri(ri1, [('test', None, 99)])
    self.check_from_ri(ri2, [('test', 100, None)])
    # Empty:
    # Slices resulting in empty datasets are valid with 'closest' rounding:
    self.check_from_spec('validation[:1%]', [('validation', None, 0)])

    # Supports splits with '-' in name.
    ri = self.check_from_spec('dev-train', [('dev-train', None, None)])

  def test_add(self):
    ri1 = tfrecords_reader.ReadInstruction.from_spec('train[10:20]')
    ri2 = tfrecords_reader.ReadInstruction.from_spec('test[10:20]')
    ri3 = tfrecords_reader.ReadInstruction.from_spec('train[1:5]')
    ri = ri1 + ri2 + ri3
    self.assertEqual(
        str(ri),
        ('ReadInstruction(['
         "_RelativeInstruction(splitname='train', from_=10, to=20, unit='abs',"
         " rounding='closest'), "
         "_RelativeInstruction(splitname='test', from_=10, to=20, unit='abs',"
         " rounding='closest'), "
         "_RelativeInstruction(splitname='train', from_=1, to=5, unit='abs',"
         " rounding='closest')])"))

  def test_add_invalid(self):
    # Mixed rounding:
    ri1 = tfrecords_reader.ReadInstruction(
        'test', unit='%', to=10, rounding='pct1_dropremainder')
    ri2 = tfrecords_reader.ReadInstruction(
        'test', unit='%', from_=90, rounding='closest')
    with self.assertRaisesWithPredicateMatch(AssertionError,
                                             'different rounding'):
      unused_ = ri1 + ri2

  def test_invalid_rounding(self):
    with self.assertRaisesWithPredicateMatch(ValueError, 'rounding'):
      tfrecords_reader.ReadInstruction('test', unit='%', rounding='unexisting')

  def test_invalid_unit(self):
    with self.assertRaisesWithPredicateMatch(ValueError, 'unit'):
      tfrecords_reader.ReadInstruction('test', unit='kg', rounding='closest')

  def test_invalid_spec(self):
    # Invalid format:
    self.assertRaises('validation[:250%:2]',
                      'Unrecognized instruction format: validation[:250%:2]')
    # Unexisting split:
    self.assertRaises(
        'imaginary', 'Unknown split "imaginary"', exc_cls=ValueError)
    # Invalid boundaries abs:
    self.assertRaises('validation[:31]', 'incompatible with 30 examples')
    # Invalid boundaries %:
    self.assertRaises('validation[:250%]',
                      'Percent slice boundaries must be > -100 and < 100')
    self.assertRaises('validation[-101%:]',
                      'Percent slice boundaries must be > -100 and < 100')
    # pct1_dropremainder with < 100 examples
    with self.assertRaisesWithPredicateMatch(
        AssertionError, 'with less than 100 elements is forbidden'):
      ri = tfrecords_reader.ReadInstruction(
          'validation', to=99, unit='%', rounding='pct1_dropremainder')
      ri.to_absolute(self.splits)


class ReaderTest(testing.TestCase):

  def setUp(self):
    super(ReaderTest, self).setUp()
    with mock.patch.object(example_parser, 'ExampleParser',
                           testing.DummyParser):
      self.reader = tfrecords_reader.Reader(self.tmp_dir, 'some_spec')
      self.reader.read = functools.partial(
          self.reader.read,
          read_config=read_config_lib.ReadConfig(),
          shuffle_files=False,
      )

  def _write_tfrecord(self, split_name, shards_number, records):
    path = os.path.join(self.tmp_dir, 'mnist-%s.tfrecord' % split_name)
    num_examples = len(records)
    with mock.patch.object(
        tfrecords_writer, '_get_number_shards', return_value=shards_number):
      shard_specs = tfrecords_writer._get_shard_specs(num_examples, 0,
                                                      [num_examples], path)
    serialized_records = [(key, six.b(rec)) for key, rec in enumerate(records)]
    for shard_spec in shard_specs:
      _write_tfrecord_from_shard_spec(shard_spec,
                                      lambda unused_i: iter(serialized_records))
    return splits.SplitInfo(
        name=split_name,
        shard_lengths=[int(s.examples_number) for s in shard_specs],
        num_bytes=0,
    )

  def test_nodata_instruction(self):
    # Given instruction corresponds to no data.
    with self.assertRaisesWithPredicateMatch(AssertionError,
                                             'corresponds to no data!'):
      train_info = splits.SplitInfo(
          name='train',
          shard_lengths=[2, 3, 2, 3, 2],
          num_bytes=0,
      )
      self.reader.read(
          name='mnist',
          instructions='train[0:0]',
          split_infos=[train_info],
      )

  def test_noskip_notake(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    ds = self.reader.read(
        name='mnist',
        instructions='train',
        split_infos=[train_info],
    )
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(read_data, [six.b(l) for l in 'abcdefghijkl'])

    if not _SKIP_CARDINALITY_TEST:
      # Check that the cardinality is correctly set.
      self.assertEqual(
          tf.data.experimental.cardinality(ds).numpy(), len(read_data))

  def test_overlap(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    ds = self.reader.read(
        name='mnist',
        instructions='train+train[:2]',
        split_infos=[train_info],
    )
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(read_data, [six.b(l) for l in 'abcdefghijklab'])

    if not _SKIP_CARDINALITY_TEST:
      # Check that the cardinality is correctly set.
      self.assertEqual(
          tf.data.experimental.cardinality(ds).numpy(), len(read_data))

  def test_complex(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    test_info = self._write_tfrecord('test', 3, 'mnopqrs')
    self.assertEqual(train_info.name, 'train')
    self.assertEqual(test_info.name, 'test')
    self.assertEqual(train_info.shard_lengths, [2, 3, 2, 3, 2])  # 12 ex.
    self.assertEqual(test_info.shard_lengths, [2, 3, 2])  # 7 ex.
    split_info = [train_info, test_info]
    ds = self.reader.read(
        name='mnist',
        instructions='train[1:-1]+test[:-50%]',
        split_infos=split_info,
    )
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(read_data, [six.b(l) for l in 'bcdefghijkmno'])

    if not _SKIP_CARDINALITY_TEST:
      # Check that the cardinality is correctly set.
      self.assertEqual(
          tf.data.experimental.cardinality(ds).numpy(), len(read_data))

  def test_shuffle_files(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    ds = self.reader.read(
        name='mnist',
        instructions='train',
        split_infos=[train_info],
        shuffle_files=True,
    )
    shards = [  # The shards of the dataset:
        [b'a', b'b'],
        [b'c', b'd', b'e'],
        [b'f', b'g'],
        [b'h', b'i', b'j'],
        [b'k', b'l'],
    ]
    # The various orders in which the dataset can be read:
    expected_permutations = [
        tuple(sum(shard, [])) for shard in itertools.permutations(shards)
    ]
    ds = ds.batch(12).repeat(100)
    read_data = set(tuple(e) for e in tfds.as_numpy(ds))
    for batch in read_data:
      self.assertIn(batch, expected_permutations)
    # There are theoritically 5! (=120) different arrangements, but we would
    # need too many repeats to be sure to get them.
    self.assertGreater(len(set(read_data)), 10)

  def test_shuffle_deterministic(self):
    split_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    read_config = read_config_lib.ReadConfig(shuffle_seed=123,)
    ds = self.reader.read(
        name='mnist',
        instructions='train',
        split_infos=[split_info],
        read_config=read_config,
        shuffle_files=True,
    )
    ds_values = list(tfds.as_numpy(ds))

    # Check that shuffle=True with a seed provides deterministic results.
    self.assertEqual(ds_values, [
        b'a', b'b', b'k', b'l', b'h', b'i', b'j', b'c', b'd', b'e', b'f', b'g'
    ])

  def test_4fold(self):
    train_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    instructions = [
        tfrecords_reader.ReadInstruction('train', from_=k, to=k + 25, unit='%')
        for k in range(0, 100, 25)
    ]
    tests = self.reader.read(
        name='mnist',
        instructions=instructions,
        split_infos=[train_info],
    )
    instructions = [
        (tfrecords_reader.ReadInstruction('train', to=k, unit='%') +
         tfrecords_reader.ReadInstruction('train', from_=k + 25, unit='%'))
        for k in range(0, 100, 25)
    ]
    trains = self.reader.read(
        name='mnist',
        instructions=instructions,
        split_infos=[train_info],
    )
    read_tests = [list(r) for r in tfds.as_numpy(tests)]
    read_trains = [list(r) for r in tfds.as_numpy(trains)]
    self.assertEqual(read_tests, [[b'a', b'b', b'c'], [b'd', b'e', b'f'],
                                  [b'g', b'h', b'i'], [b'j', b'k', b'l']])
    self.assertEqual(read_trains,
                     [[b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l'],
                      [b'a', b'b', b'c', b'g', b'h', b'i', b'j', b'k', b'l'],
                      [b'a', b'b', b'c', b'd', b'e', b'f', b'j', b'k', b'l'],
                      [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i']])

  def test_read_files(self):
    self._write_tfrecord('train', 4, 'abcdefghijkl')
    fname_pattern = 'mnist-train.tfrecord-0000%d-of-00004'
    ds = self.reader.read_files(
        [
            shard_utils.FileInstruction(
                filename=fname_pattern % 1, skip=0, take=-1, num_examples=3),
            shard_utils.FileInstruction(
                filename=fname_pattern % 3, skip=1, take=1, num_examples=1),
        ],
        read_config=read_config_lib.ReadConfig(),
        shuffle_files=False,
    )
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(read_data, [six.b(l) for l in 'defk'])

  def test_input_context(self):
    split_info = self._write_tfrecord('train', 5, 'abcdefghijkl')
    self.assertEqual(split_info.shard_lengths, [2, 3, 2, 3, 2])

    def read(num_workers, index):
      return list(
          tfds.as_numpy(
              self.reader.read(
                  name='mnist',
                  instructions='train',
                  split_infos=[split_info],
                  read_config=read_config_lib.ReadConfig(
                      input_context=tf.distribute.InputContext(
                          num_input_pipelines=num_workers,
                          input_pipeline_id=index,
                      ),),
                  # Workers should read a deterministic subset of the examples,
                  # even if examples within one worker may be shuffled.
                  shuffle_files=True,
              )))

    def _b(bytes_str):
      if six.PY2:
        return list(bytes_str)
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
    with self.assertRaisesRegexp(ValueError, 'Cannot shard the pipeline'):
      read(num_workers=6, index=0)

  def test_shuffle_files_should_be_disabled(self):
    self._write_tfrecord('train', 4, 'abcdefghijkl')
    fname_pattern = 'mnist-train.tfrecord-0000%d-of-00004'
    with self.assertRaisesWithPredicateMatch(ValueError,
                                             _SHUFFLE_FILES_ERROR_MESSAGE):
      self.reader.read_files(
          [
              shard_utils.FileInstruction(
                  filename=fname_pattern % 1, skip=0, take=-1, num_examples=3),
          ],
          read_config=read_config_lib.ReadConfig(),
          shuffle_files=True,
          disable_shuffling=True,
      )

  def test_cycle_length_must_be_one(self):
    self._write_tfrecord('train', 4, 'abcdefghijkl')
    fname_pattern = 'mnist-train.tfrecord-0000%d-of-00004'
    instructions = [
        shard_utils.FileInstruction(
            filename=fname_pattern % 1, skip=0, take=-1, num_examples=3),
    ]
    # In ordered dataset interleave_cycle_length is set to 1 by default
    self.reader.read_files(
        instructions,
        read_config=read_config_lib.ReadConfig(),
        shuffle_files=False,
        disable_shuffling=True,
    )
    with self.assertRaisesWithPredicateMatch(ValueError,
                                             _CYCLE_LENGTH_ERROR_MESSAGE):
      self.reader.read_files(
          instructions,
          read_config=read_config_lib.ReadConfig(interleave_cycle_length=16),
          shuffle_files=False,
          disable_shuffling=True,
      )

  def test_ordering_guard(self):
    self._write_tfrecord('train', 4, 'abcdefghijkl')
    fname_pattern = 'mnist-train.tfrecord-0000%d-of-00004'
    instructions = [
        shard_utils.FileInstruction(
            filename=fname_pattern % 1, skip=0, take=-1, num_examples=3),
    ]
    reported_warnings = []
    with mock.patch('absl.logging.warning', reported_warnings.append):
      self.reader.read_files(
          instructions,
          read_config=read_config_lib.ReadConfig(
              interleave_cycle_length=16, enable_ordering_guard=False),
          shuffle_files=True,
          disable_shuffling=True,
      )
      expected_warning = _SHUFFLE_FILES_ERROR_MESSAGE + '\n' + _CYCLE_LENGTH_ERROR_MESSAGE
      self.assertIn(expected_warning, reported_warnings)


if __name__ == '__main__':
  testing.test_main()
