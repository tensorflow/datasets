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

"""Tests for the Split API."""

from tensorflow_datasets import testing
from tensorflow_datasets.core import proto
from tensorflow_datasets.core import splits
from tensorflow_datasets.core.utils import shard_utils
import tensorflow_datasets.public_api as tfds

RANGE_TRAIN = list(range(0, 2000))
RANGE_TEST = list(range(3000, 3200))
RANGE_VAL = list(range(6000, 6010))


class SplitDictTest(testing.TestCase):

  def test_num_shards(self):
    si = tfds.core.SplitInfo(name='train', shard_lengths=[1, 2, 3], num_bytes=0)
    sd = splits.SplitDict([si], dataset_name='ds_name')
    self.assertEqual(sd['train'].num_shards, 3)

  def test_empty_split(self):
    sd = splits.SplitDict([], dataset_name='ds_name')
    with self.assertRaisesWithPredicateMatch(KeyError, '`splits` is empty'):
      _ = sd['train']


class SplitsDictTest(testing.TestCase):

  @property
  def split_dict(self):
    si = [
        tfds.core.SplitInfo(name='train', shard_lengths=[10, 10], num_bytes=0),
        tfds.core.SplitInfo(name='test', shard_lengths=[1], num_bytes=0),
    ]
    sd = splits.SplitDict(si, dataset_name='ds_name')
    return sd

  def test_get(self):
    s = self.split_dict['train']
    self.assertEqual('train', s.name)
    self.assertEqual(2, s.num_shards)

  def test_from_proto(self):
    sd = splits.SplitDict.from_proto(
        'ds_name',
        [proto.SplitInfo(name='validation', shard_lengths=[5], num_bytes=0)])
    self.assertIn('validation', sd)
    self.assertNotIn('train', sd)
    self.assertNotIn('test', sd)

  def test_to_proto(self):
    sd = self.split_dict
    sdp = sd.to_proto()

    # Split order is preserved
    self.assertEqual('train', sdp[0].name)
    self.assertEqual([10, 10], sdp[0].shard_lengths)

    self.assertEqual('test', sdp[1].name)
    self.assertEqual([1], sdp[1].shard_lengths)

  def test_bool(self):
    sd = splits.SplitDict([], dataset_name='ds_name')
    self.assertFalse(sd)  # Empty split is False
    si = [tfds.core.SplitInfo(name='train', shard_lengths=[5], num_bytes=0)]
    sd = splits.SplitDict(si, dataset_name='ds_name')
    self.assertTrue(sd)  # Non-empty split is True


class SplitsTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(SplitsTest, cls).setUpClass()
    cls._builder = testing.DummyDatasetSharedGenerator(
        data_dir=testing.make_tmp_dir())
    cls._builder.download_and_prepare()

  def test_sub_split_num_examples(self):
    s = self._builder.info.splits
    self.assertEqual(s['train[75%:]'].num_examples, 5)
    self.assertEqual(s['train[:75%]'].num_examples, 15)
    self.assertEqual(
        s['train'].num_examples,
        s['train[75%:]'].num_examples + s['train[:75%]'].num_examples,
    )

    self.assertEqual(s['test[75%:]'].num_examples, 2)
    self.assertEqual(s['test[:75%]'].num_examples, 8)
    self.assertEqual(
        s['test'].num_examples,
        s['test[75%:]'].num_examples + s['test[:75%]'].num_examples,
    )

    self.assertEqual(s['all'].num_examples, s.total_num_examples)

  def test_sub_split_file_instructions(self):
    fi = self._builder.info.splits['train[75%:]'].file_instructions
    self.assertEqual(fi, [
        shard_utils.FileInstruction(
            filename='dummy_dataset_shared_generator-train.tfrecord-00000-of-00001',
            skip=15,
            take=-1,
            num_examples=5,
        )
    ])

  def test_sub_split_num_shards(self):
    self.assertEqual(self._builder.info.splits['train[75%:]'].num_shards, 1)

  def test_split_file_instructions(self):
    fi = self._builder.info.splits['train'].file_instructions
    self.assertEqual(fi, [
        shard_utils.FileInstruction(
            filename='dummy_dataset_shared_generator-train.tfrecord-00000-of-00001',
            skip=0,
            take=-1,
            num_examples=20,
        )
    ])

  def test_sub_split_filenames(self):
    self.assertEqual(self._builder.info.splits['train'].filenames, [
        'dummy_dataset_shared_generator-train.tfrecord-00000-of-00001',
    ])
    self.assertEqual(self._builder.info.splits['train[75%:]'].filenames, [
        'dummy_dataset_shared_generator-train.tfrecord-00000-of-00001',
    ])

  def test_sub_split_wrong_key(self):
    with self.assertRaisesWithPredicateMatch(ValueError,
                                             "Unknown split 'unknown'"):
      _ = self._builder.info.splits['unknown']

  def test_split_enum(self):
    self.assertEqual(repr(splits.Split.TRAIN), "Split('train')")
    self.assertIsInstance(splits.Split.TRAIN, splits.Split)


class ReadInstructionTest(testing.TestCase):

  def setUp(self):
    super(ReadInstructionTest, self).setUp()
    self.splits = {
        'train':
            splits.SplitInfo(name='train', shard_lengths=[200], num_bytes=0),
        'test':
            splits.SplitInfo(name='train', shard_lengths=[101], num_bytes=0),
        'validation':
            splits.SplitInfo(name='train', shard_lengths=[30], num_bytes=0),
        'dev-train':
            splits.SplitInfo(name='train', shard_lengths=[5, 5], num_bytes=0),
    }

  def check_from_ri(self, ri, expected):
    res = ri.to_absolute(self.splits)
    expected_result = []
    for split_name, from_, to_ in expected:
      expected_result.append(
          splits._AbsoluteInstruction(split_name, from_, to_))
    self.assertEqual(res, expected_result)
    return ri

  def check_from_spec(self, spec, expected):
    ri = splits.ReadInstruction.from_spec(spec)
    return self.check_from_ri(ri, expected)

  def assertRaises(self, spec, msg, exc_cls=ValueError):
    with self.assertRaisesWithPredicateMatch(exc_cls, msg):
      ri = splits.ReadInstruction.from_spec(spec)
      ri.to_absolute(self.splits)

  def test_valid(self):
    # Simple split:
    ri = self.check_from_spec('train', [('train', None, None)])
    self.assertEqual(
        str(ri),
        "ReadInstruction('train')",
    )
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
        str(ri), "ReadInstruction('test[:99%]', rounding='closest')")
    # No overlap:
    self.check_from_spec('test[100%:]', [('test', 101, None)])
    # Percent slicing, pct1_dropremainder rounding:
    ri = splits.ReadInstruction(
        'train', to=20, unit='%', rounding='pct1_dropremainder')
    self.check_from_ri(ri, [('train', None, 40)])
    # test split has 101 examples.
    ri = splits.ReadInstruction(
        'test', to=100, unit='%', rounding='pct1_dropremainder')
    self.check_from_ri(ri, [('test', None, 100)])
    # No overlap using 'pct1_dropremainder' rounding:
    ri1 = splits.ReadInstruction(
        'test', to=99, unit='%', rounding='pct1_dropremainder')
    ri2 = splits.ReadInstruction(
        'test', from_=100, unit='%', rounding='pct1_dropremainder')
    self.check_from_ri(ri1, [('test', None, 99)])
    self.check_from_ri(ri2, [('test', 100, None)])
    # Empty:
    # Slices resulting in empty datasets are valid with 'closest' rounding:
    self.check_from_spec('validation[:1%]', [('validation', None, 0)])
    # New integer syntax
    self.check_from_spec('train[4_2:9_9]', [('train', 42, 99)])
    self.check_from_spec('train[:1_0%]', [('train', None, 20)])

    # Supports splits with '-' in name.
    ri = self.check_from_spec('dev-train', [('dev-train', None, None)])

  def test_add(self):
    ri1 = splits.ReadInstruction.from_spec('train[10:20]')
    ri2 = splits.ReadInstruction.from_spec('test[10:20]')
    ri3 = splits.ReadInstruction.from_spec('train[1:5]')
    ri = ri1 + ri2 + ri3
    self.assertEqual(
        str(ri),
        "ReadInstruction('train[10:20]')"
        "+ReadInstruction('test[10:20]')"
        "+ReadInstruction('train[1:5]')",
    )

  def test_invalid_rounding(self):
    with self.assertRaisesWithPredicateMatch(ValueError, 'Rounding should be'):
      splits.ReadInstruction('test', unit='%', rounding='unexisting')

  def test_invalid_unit(self):
    with self.assertRaisesWithPredicateMatch(ValueError, 'Unit should be'):
      splits.ReadInstruction('test', unit='kg', rounding='closest')

  def test_invalid_spec(self):
    # Invalid format:
    self.assertRaises('validation[:250%:2]',
                      'Unrecognized split format: \'validation[:250%:2]\'')
    # Unexisting split:
    self.assertRaises('imaginary', "Unknown split 'imaginary'")
    # Invalid boundaries abs:
    self.assertRaises('validation[:31]', 'incompatible with 30 examples')
    # Invalid boundaries %:
    self.assertRaises('validation[:250%]',
                      'percent slice boundaries should be in [-100, 100]')
    self.assertRaises('validation[-101%:]',
                      'percent slice boundaries should be in [-100, 100]')
    # pct1_dropremainder with < 100 examples
    with self.assertRaisesWithPredicateMatch(
        ValueError, 'with less than 100 elements is forbidden'):
      ri = splits.ReadInstruction(
          'validation', to=99, unit='%', rounding='pct1_dropremainder')
      ri.to_absolute(self.splits)


class GetDatasetFilesTest(testing.TestCase):

  SPLIT_INFOS = {
      'train':
          splits.SplitInfo(
              name='train',
              shard_lengths=[3, 2, 3, 2, 3],  # 13 examples.
              num_bytes=0,
          ),
  }

  PATH_PATTERN = 'mnist-train.tfrecord-0000%d-of-00005'

  def _get_files(self, instruction):
    file_instructions = splits._make_file_instructions_from_absolutes(
        name='mnist',
        split_infos=self.SPLIT_INFOS,
        absolute_instructions=[instruction],
    )
    return file_instructions

  def test_no_skip_no_take(self):
    instruction = splits._AbsoluteInstruction('train', None, None)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % i, skip=0, take=-1, num_examples=n)
        for i, n in enumerate([3, 2, 3, 2, 3])
    ])

  def test_skip(self):
    # One file is not taken, one file is partially taken.
    instruction = splits._AbsoluteInstruction('train', 4, None)
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
    instruction = splits._AbsoluteInstruction('train', None, 6)
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
    instruction = splits._AbsoluteInstruction('train', 1, 2)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 0, skip=1, take=1, num_examples=1),
    ])

  def test_skip_take2(self):
    # 2 elements in across two shards are taken in middle.
    instruction = splits._AbsoluteInstruction('train', 7, 9)
    files = self._get_files(instruction)
    self.assertEqual(files, [
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 2, skip=2, take=-1, num_examples=1),
        shard_utils.FileInstruction(
            filename=self.PATH_PATTERN % 3, skip=0, take=1, num_examples=1),
    ])

  def test_touching_boundaries(self):
    # Nothing to read.
    instruction = splits._AbsoluteInstruction('train', 0, 0)
    files = self._get_files(instruction)
    self.assertEqual(files, [])

    instruction = splits._AbsoluteInstruction('train', None, 0)
    files = self._get_files(instruction)
    self.assertEqual(files, [])

    instruction = splits._AbsoluteInstruction('train', 3, 3)
    files = self._get_files(instruction)
    self.assertEqual(files, [])

    instruction = splits._AbsoluteInstruction('train', 13, None)
    files = self._get_files(instruction)
    self.assertEqual(files, [])

  def test_missing_shard_lengths(self):
    with self.assertRaisesWithPredicateMatch(ValueError, 'Shard empty.'):
      split_info = [
          splits.SplitInfo(name='train', shard_lengths=[], num_bytes=0),
      ]
      splits.make_file_instructions('mnist', split_info, 'train')


if __name__ == '__main__':
  testing.test_main()
