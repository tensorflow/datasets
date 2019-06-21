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

"""Tests for tensorflow_datasets.core.tfrecords_reader."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools
import os

from absl.testing import absltest
import six

import tensorflow_datasets as tfds
from tensorflow_datasets import testing
from tensorflow_datasets.core import example_parser
from tensorflow_datasets.core import splits
from tensorflow_datasets.core import tfrecords_reader
from tensorflow_datasets.core import tfrecords_writer


class GetDatasetFilesTest(testing.TestCase):

  NAME2SHARD_LENGTHS = {
      'train': [3, 2, 3, 2, 3],  # 13 examples.
  }

  PATH_PATTERN = '/foo/bar/mnist-train.tfrecord-0000%d-of-00005'

  def _get_files(self, instruction):
    return tfrecords_reader._get_dataset_files(
        'mnist', '/foo/bar', instruction, self.NAME2SHARD_LENGTHS)

  def test_no_skip_no_take(self):
    instruction = tfrecords_reader._AbsoluteInstruction('train', None, None)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        {'skip': 0, 'take': -1, 'filename': self.PATH_PATTERN % i}
        for i in range(5)])

  def test_skip(self):
    # One file is not taken, one file is partially taken.
    instruction = tfrecords_reader._AbsoluteInstruction('train', 4, None)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        {'skip': 1, 'take': -1, 'filename': self.PATH_PATTERN % 1},
        {'skip': 0, 'take': -1, 'filename': self.PATH_PATTERN % 2},
        {'skip': 0, 'take': -1, 'filename': self.PATH_PATTERN % 3},
        {'skip': 0, 'take': -1, 'filename': self.PATH_PATTERN % 4},
    ])

  def test_take(self):
    # Two files are not taken, one file is partially taken.
    instruction = tfrecords_reader._AbsoluteInstruction('train', None, 6)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        {'skip': 0, 'take': -1, 'filename': self.PATH_PATTERN % 0},
        {'skip': 0, 'take': -1, 'filename': self.PATH_PATTERN % 1},
        {'skip': 0, 'take': 1, 'filename': self.PATH_PATTERN % 2},
    ])

  def test_skip_take1(self):
    # A single shard with both skip and take.
    instruction = tfrecords_reader._AbsoluteInstruction('train', 1, 2)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        {'skip': 1, 'take': 1, 'filename': self.PATH_PATTERN % 0},
    ])

  def test_skip_take2(self):
    # 2 elements in across two shards are taken in middle.
    instruction = tfrecords_reader._AbsoluteInstruction('train', 7, 9)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        {'skip': 2, 'take': -1, 'filename': self.PATH_PATTERN % 2},
        {'skip': 0, 'take': 1, 'filename': self.PATH_PATTERN % 3},
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
    instruction = tfrecords_reader._AbsoluteInstruction('train', None, None)
    with self.assertRaisesWithPredicateMatch(
        AssertionError, 'S3 tfrecords_reader cannot be used'):
      tfrecords_reader._get_dataset_files(
          'mnist', '/foo/bar', instruction, {'train': None})


class ReadInstructionTest(testing.TestCase):

  def setUp(self):
    self.splits = {
        'train': 200,
        'test': 101,
        'validation': 30,
    }

  def check_from_ri(self, ri, expected):
    res = ri.to_absolute(self.splits)
    expected_result = []
    for split_name, from_, to_ in expected:
      expected_result.append(tfrecords_reader._AbsoluteInstruction(
          split_name, from_, to_))
    self.assertEqual(res, expected_result)
    return ri

  def check_from_spec(self, spec, expected):
    ri = tfrecords_reader.ReadInstruction.from_spec(spec)
    return self.check_from_ri(ri, expected)

  def assertRaises(self, spec, msg):
    with self.assertRaisesWithPredicateMatch(AssertionError, msg):
      ri = tfrecords_reader.ReadInstruction.from_spec(spec)
      ri.to_absolute(self.splits)

  def test_valid(self):
    # Simple split:
    ri = self.check_from_spec('train', [('train', None, None)])
    self.assertEqual(
        str(ri),
        ("ReadInstruction(["
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
    ri = tfrecords_reader.ReadInstruction('train', to=20, unit='%',
                                          rounding='pct1_dropremainder')
    self.check_from_ri(ri, [('train', None, 40)])
    # test split has 101 examples.
    ri = tfrecords_reader.ReadInstruction('test', to=100, unit='%',
                                          rounding='pct1_dropremainder')
    self.check_from_ri(ri, [('test', None, 100)])
    # No overlap using 'pct1_dropremainder' rounding:
    ri1 = tfrecords_reader.ReadInstruction('test', to=99, unit='%',
                                           rounding='pct1_dropremainder')
    ri2 = tfrecords_reader.ReadInstruction('test', from_=100, unit='%',
                                           rounding='pct1_dropremainder')
    self.check_from_ri(ri1, [('test', None, 99)])
    self.check_from_ri(ri2, [('test', 100, None)])
    # Empty:
    # Slices resulting in empty datasets are valid with 'closest' rounding:
    self.check_from_spec('validation[:1%]', [('validation', None, 0)])

  def test_add(self):
    ri1 = tfrecords_reader.ReadInstruction.from_spec('train[10:20]')
    ri2 = tfrecords_reader.ReadInstruction.from_spec('test[10:20]')
    ri3 = tfrecords_reader.ReadInstruction.from_spec('train[1:5]')
    ri = ri1 + ri2 + ri3
    self.assertEqual(
        str(ri),
        ("ReadInstruction(["
         "_RelativeInstruction(splitname='train', from_=10, to=20, unit='abs',"
         " rounding='closest'), "
         "_RelativeInstruction(splitname='test', from_=10, to=20, unit='abs',"
         " rounding='closest'), "
         "_RelativeInstruction(splitname='train', from_=1, to=5, unit='abs',"
         " rounding='closest')])"))

  def test_add_invalid(self):
    # Mixed rounding:
    ri1 = tfrecords_reader.ReadInstruction('test', unit='%', to=10,
                                           rounding='pct1_dropremainder')
    ri2 = tfrecords_reader.ReadInstruction('test', unit='%', from_=90,
                                           rounding='closest')
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
    self.assertRaises('imaginary',
                      'Requested split "imaginary" does not exist')
    # Invalid boundaries abs:
    self.assertRaises('validation[:31]',
                      'incompatible with 30 examples')
    # Invalid boundaries %:
    self.assertRaises('validation[:250%]',
                      'Percent slice boundaries must be > -100 and < 100')
    self.assertRaises('validation[-101%:]',
                      'Percent slice boundaries must be > -100 and < 100')
    # pct1_dropremainder with < 100 examples
    with self.assertRaisesWithPredicateMatch(
        AssertionError, 'with less than 100 elements is forbidden'):
      ri = tfrecords_reader.ReadInstruction('validation', to=99, unit='%',
                                            rounding='pct1_dropremainder')
      ri.to_absolute(self.splits)


class ReaderTest(testing.TestCase):

  SPLIT_INFOS = [
      splits.SplitInfo(name='train', shard_lengths=[2, 3, 2, 3, 2]),  # 12 ex.
      splits.SplitInfo(name='test', shard_lengths=[2, 3, 2]),  # 7 ex.
  ]

  def setUp(self):
    super(ReaderTest, self).setUp()
    with absltest.mock.patch.object(example_parser,
                                    'ExampleParser', testing.DummyParser):
      self.reader = tfrecords_reader.Reader(self.tmp_dir, 'some_spec')

  def _write_tfrecord(self, split_name, shards_number, records):
    path = os.path.join(self.tmp_dir, 'mnist-%s.tfrecord' % split_name)
    writer = tfrecords_writer._TFRecordWriter(path, len(records), shards_number)
    for rec in records:
      writer.write(six.b(rec))
    with absltest.mock.patch.object(tfrecords_writer, '_get_number_shards',
                                    return_value=shards_number):
      writer.finalize()

  def _write_tfrecords(self):
    self._write_tfrecord('train', 5, 'abcdefghijkl')
    self._write_tfrecord('test', 3, 'mnopqrs')

  def test_nodata_instruction(self):
    # Given instruction corresponds to no data.
    with self.assertRaisesWithPredicateMatch(AssertionError,
                                             'corresponds to no data!'):
      self.reader.read('mnist', 'train[0:0]', self.SPLIT_INFOS)

  def test_noskip_notake(self):
    self._write_tfrecord('train', 5, 'abcdefghijkl')
    ds = self.reader.read('mnist', 'train', self.SPLIT_INFOS)
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(read_data, [six.b(l) for l in 'abcdefghijkl'])

  def test_overlap(self):
    self._write_tfrecord('train', 5, 'abcdefghijkl')
    ds = self.reader.read('mnist', 'train+train[:2]', self.SPLIT_INFOS)
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(read_data, [six.b(l) for l in 'abcdefghijklab'])

  def test_complex(self):
    self._write_tfrecord('train', 5, 'abcdefghijkl')
    self._write_tfrecord('test', 3, 'mnopqrs')
    ds = self.reader.read('mnist', 'train[1:-1]+test[:-50%]', self.SPLIT_INFOS)
    read_data = list(tfds.as_numpy(ds))
    self.assertEqual(read_data, [six.b(l) for l in 'bcdefghijkmno'])

  def test_shuffle_files(self):
    self._write_tfrecord('train', 5, 'abcdefghijkl')
    ds = self.reader.read('mnist', 'train', self.SPLIT_INFOS,
                          shuffle_files=True)
    shards = [  # The shards of the dataset:
        [b'a', b'b'],
        [b'c', b'd', b'e'],
        [b'f', b'g'],
        [b'h', b'i', b'j'],
        [b'k', b'l'],
    ]
    # The various orders in which the dataset can be read:
    expected_permutations = [tuple(sum(shard, []))
                             for shard in itertools.permutations(shards)]
    ds = ds.batch(12).repeat(100)
    read_data = set(tuple(e) for e in tfds.as_numpy(ds))
    for batch in read_data:
      self.assertIn(batch, expected_permutations)
    # There are theoritically 5! (=120) different arrangements, but we would
    # need too many repeats to be sure to get them.
    self.assertGreater(len(set(read_data)), 10)

  def test_4fold(self):
    self._write_tfrecord('train', 5, 'abcdefghijkl')
    instructions = [
        tfrecords_reader.ReadInstruction('train', from_=k, to=k+25, unit='%')
        for k in range(0, 100, 25)]
    tests = self.reader.read('mnist', instructions, self.SPLIT_INFOS)
    instructions = [
        (tfrecords_reader.ReadInstruction('train', to=k, unit='%') +
         tfrecords_reader.ReadInstruction('train', from_=k+25, unit='%'))
        for k in range(0, 100, 25)]
    trains = self.reader.read('mnist', instructions, self.SPLIT_INFOS)
    read_tests = [list(r) for r in tfds.as_numpy(tests)]
    read_trains = [list(r) for r in tfds.as_numpy(trains)]
    self.assertEqual(read_tests, [[b'a', b'b', b'c'],
                                  [b'd', b'e', b'f'],
                                  [b'g', b'h', b'i'],
                                  [b'j', b'k', b'l']])
    self.assertEqual(read_trains, [
        [b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l'],
        [b'a', b'b', b'c', b'g', b'h', b'i', b'j', b'k', b'l'],
        [b'a', b'b', b'c', b'd', b'e', b'f', b'j', b'k', b'l'],
        [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i']])


if __name__ == '__main__':
  testing.test_main()
