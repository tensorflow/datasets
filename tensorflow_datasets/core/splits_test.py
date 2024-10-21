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

"""Tests for the Split API."""

import os
from etils import epath
from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import proto
from tensorflow_datasets.core import splits
from tensorflow_datasets.core.utils import shard_utils
import tensorflow_datasets.public_api as tfds

RANGE_TRAIN = list(range(0, 2000))
RANGE_TEST = list(range(3000, 3200))
RANGE_VAL = list(range(6000, 6010))


def _filename_template(
    split: str, dataset_name: str = 'ds_name', data_dir: str = '/path'
):
  return naming.ShardedFileTemplate(
      dataset_name=dataset_name,
      split=split,
      data_dir=data_dir,
      filetype_suffix='tfrecord',
  )


def test_multi_split_infos():
  split = 'train'
  split_infos = [
      tfds.core.SplitInfo(
          name=split,
          shard_lengths=[10, 10],
          num_bytes=100,
          filename_template=_filename_template(split=split, data_dir='/abc'),
      ),
      tfds.core.SplitInfo(
          name=split,
          shard_lengths=[1],
          num_bytes=20,
          filename_template=_filename_template(split=split, data_dir='/xyz'),
      ),
  ]
  multi_split_info = splits.MultiSplitInfo(name=split, split_infos=split_infos)
  assert multi_split_info.num_bytes == 120
  assert multi_split_info.num_examples == 21
  assert multi_split_info.num_shards == 3
  assert multi_split_info.shard_lengths == [10, 10, 1]
  assert multi_split_info.file_instructions == [
      shard_utils.FileInstruction(
          filename='/abc/ds_name-train.tfrecord-00000-of-00002',
          skip=0,
          take=-1,
          examples_in_shard=10,
      ),
      shard_utils.FileInstruction(
          filename='/abc/ds_name-train.tfrecord-00001-of-00002',
          skip=0,
          take=-1,
          examples_in_shard=10,
      ),
      shard_utils.FileInstruction(
          filename='/xyz/ds_name-train.tfrecord-00000-of-00001',
          skip=0,
          take=-1,
          examples_in_shard=1,
      ),
  ]
  assert (
      str(multi_split_info)
      == "MultiSplitInfo(name='train', split_infos=[<SplitInfo"
      ' num_examples=20, '
      'num_shards=2>, <SplitInfo num_examples=1, num_shards=1>])'
  )


class SplitDictTest(testing.TestCase):

  @property
  def split_dict(self):
    si = [
        tfds.core.SplitInfo(
            name='train',
            shard_lengths=[10, 10],
            num_bytes=0,
            filename_template=_filename_template('train'),
        ),
        tfds.core.SplitInfo(
            name='test',
            shard_lengths=[1],
            num_bytes=0,
            filename_template=_filename_template('test'),
        ),
    ]
    sd = splits.SplitDict(si)
    return sd

  def test_get(self):
    s = self.split_dict['train']
    self.assertEqual('train', s.name)
    self.assertEqual(2, s.num_shards)

  def test_from_proto(self):
    sd = splits.SplitDict.from_proto(
        filename_template=naming.ShardedFileTemplate(
            dataset_name='ds_name', data_dir='/path', filetype_suffix='tfrecord'
        ),
        repeated_split_infos=[
            proto.SplitInfo(name='validation', shard_lengths=[5], num_bytes=0)
        ],
    )
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
    sd = splits.SplitDict([])
    self.assertFalse(sd)  # Empty split is False
    si = [
        tfds.core.SplitInfo(
            name='train',
            shard_lengths=[5],
            num_bytes=0,
            filename_template=_filename_template('train'),
        )
    ]
    sd = splits.SplitDict(si)
    self.assertTrue(sd)  # Non-empty split is True

  def test_num_shards(self):
    si = tfds.core.SplitInfo(
        name='train',
        shard_lengths=[1, 2, 3],
        num_bytes=0,
        filename_template=_filename_template(split='train'),
    )
    sd = splits.SplitDict([si])
    self.assertEqual(sd['train'].num_shards, 3)

  def test_empty_split(self):
    sd = splits.SplitDict([])
    with self.assertRaisesWithPredicateMatch(KeyError, '`splits` is empty'):
      _ = sd['train']

  def test_merge_multiple(self):
    def split_info_for(name: str, shard_lengths, template) -> splits.SplitInfo:
      return splits.SplitInfo(
          name=name,
          shard_lengths=shard_lengths,
          num_bytes=0,
          filename_template=template,
      )

    template_a = naming.ShardedFileTemplate(
        dataset_name='ds_name', data_dir='/a', filetype_suffix='tfrecord'
    )
    split_info_a1 = split_info_for('train', [1, 2, 3], template_a)
    split_info_a2 = split_info_for('test', [1], template_a)
    split_info_a3 = split_info_for('banana', [1], template_a)
    split_dict_1 = splits.SplitDict(
        [split_info_a1, split_info_a2, split_info_a3]
    )

    template_b = naming.ShardedFileTemplate(
        dataset_name='ds_name', data_dir='/b', filetype_suffix='tfrecord'
    )
    split_info_b1 = split_info_for('train', [4, 5, 6], template_b)
    split_info_b2 = split_info_for('test', [3], template_b)
    split_dict_2 = splits.SplitDict([split_info_b1, split_info_b2])

    template_c = naming.ShardedFileTemplate(
        dataset_name='ds_name', data_dir='/c', filetype_suffix='tfrecord'
    )
    split_info_c1 = split_info_for('train', [8], template_c)
    split_info_c2 = split_info_for('train', [9], template_c)
    multi_split = splits.MultiSplitInfo(
        name='train', split_infos=[split_info_c1, split_info_c2]
    )
    split_dict_3 = splits.SplitDict([multi_split])

    merged = splits.SplitDict.merge_multiple(
        [split_dict_1, split_dict_2, split_dict_3]
    )
    assert len(merged.values()) == 3
    assert merged.get('train').split_infos == [
        split_info_a1,
        split_info_b1,
        split_info_c1,
        split_info_c2,
    ]
    assert merged.get('test').split_infos == [split_info_a2, split_info_b2]
    assert merged.get('banana').split_infos == [split_info_a3]


class SplitsTest(testing.TestCase):

  @classmethod
  def setUpClass(cls):
    super(SplitsTest, cls).setUpClass()
    tmp_dir = testing.make_tmp_dir()
    cls._builder = testing.DummyDatasetSharedGenerator(data_dir=tmp_dir)
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
    self.assertEqual(
        fi,
        [
            shard_utils.FileInstruction(
                filename=f'{self._builder.data_dir}/dummy_dataset_shared_generator-train.tfrecord-00000-of-00001',
                skip=15,
                take=-1,
                examples_in_shard=20,
            )
        ],
    )

  def test_sub_split_num_shards(self):
    self.assertEqual(self._builder.info.splits['train[75%:]'].num_shards, 1)

  def test_sub_split_shard_lengths(self):
    self.assertEqual(
        self._builder.info.splits['train[75%:]'].shard_lengths,
        [5],
    )

  def test_sub_split_to_proto(self):
    sp = self._builder.info.splits['train[75%:]'].to_proto()
    self.assertEqual('train[75%:]', sp.name)
    self.assertEqual([5], sp.shard_lengths)

  def test_split_file_instructions(self):
    fi = self._builder.info.splits['train'].file_instructions
    self.assertEqual(
        fi,
        [
            shard_utils.FileInstruction(
                filename=f'{self._builder.data_dir}/dummy_dataset_shared_generator-train.tfrecord-00000-of-00001',
                skip=0,
                take=-1,
                examples_in_shard=20,
            )
        ],
    )

  def test_sub_split_filenames(self):
    self.assertEqual(
        self._builder.info.splits['train'].filenames,
        [
            'dummy_dataset_shared_generator-train.tfrecord-00000-of-00001',
        ],
    )
    self.assertEqual(
        self._builder.info.splits['train[75%:]'].filenames,
        [
            'dummy_dataset_shared_generator-train.tfrecord-00000-of-00001',
        ],
    )

  def test_sub_split_wrong_key(self):
    with self.assertRaisesWithPredicateMatch(
        ValueError, "Unknown split 'unknown'"
    ):
      _ = self._builder.info.splits['unknown']

  def test_split_enum(self):
    self.assertEqual(repr(splits.Split.TRAIN), "Split('train')")
    self.assertIsInstance(splits.Split.TRAIN, splits.Split)


class ReadInstructionTest(testing.TestCase):

  def setUp(self):
    super(ReadInstructionTest, self).setUp()

    self.splits = {
        'train': splits.SplitInfo(
            name='train',
            shard_lengths=[200],
            num_bytes=0,
            filename_template=_filename_template('train'),
        ),
        'test': splits.SplitInfo(
            name='test',
            shard_lengths=[101],
            num_bytes=0,
            filename_template=_filename_template('test'),
        ),
        'validation': splits.SplitInfo(
            name='validation',
            shard_lengths=[30],
            num_bytes=0,
            filename_template=_filename_template('validation'),
        ),
        'dev-train': splits.SplitInfo(
            name='dev-train',
            shard_lengths=[5, 5],
            num_bytes=0,
            filename_template=_filename_template('dev-train'),
        ),
    }

  def check_from_ri(self, ri, expected):
    res = ri.to_absolute(self.splits)
    expected_result = []
    for split_name, from_, to_ in expected:
      expected_result.append(
          splits._AbsoluteInstruction(split_name, from_, to_)
      )
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
    self.check_from_spec(
        'train+test',
        [
            ('train', None, None),
            ('test', None, None),
        ],
    )
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
        str(ri), "ReadInstruction('test[:99%]', rounding='closest')"
    )
    self.check_from_spec('train[:0.5%]', [('train', None, 1)])
    # No overlap:
    self.check_from_spec('test[100%:]', [('test', 101, None)])
    # Percent slicing, pct1_dropremainder rounding:
    ri = splits.ReadInstruction(
        'train', to=20, unit='%', rounding='pct1_dropremainder'
    )
    self.check_from_ri(ri, [('train', None, 40)])
    # test split has 101 examples.
    ri = splits.ReadInstruction(
        'test', to=100, unit='%', rounding='pct1_dropremainder'
    )
    self.check_from_ri(ri, [('test', None, 100)])
    # No overlap using 'pct1_dropremainder' rounding:
    ri1 = splits.ReadInstruction(
        'test', to=99, unit='%', rounding='pct1_dropremainder'
    )
    ri2 = splits.ReadInstruction(
        'test', from_=100, unit='%', rounding='pct1_dropremainder'
    )
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
        (
            "ReadInstruction('train[10:20]')"
            "+ReadInstruction('test[10:20]')"
            "+ReadInstruction('train[1:5]')"
        ),
    )

  def test_invalid_rounding(self):
    with self.assertRaisesWithPredicateMatch(ValueError, 'Rounding should be'):
      splits.ReadInstruction('test', unit='%', rounding='unexisting')

  def test_invalid_unit(self):
    with self.assertRaisesWithPredicateMatch(ValueError, 'Unit should be'):
      splits.ReadInstruction('test', unit='kg', rounding='closest')

  def test_invalid_spec(self):
    # Invalid format:
    self.assertRaises(
        'validation[:250%:2]',
        "Unrecognized split format: 'validation[:250%:2]'",
    )
    # Unexisting split:
    self.assertRaises('imaginary', "Unknown split 'imaginary'")
    # Invalid boundaries abs:
    self.assertRaises('validation[:31]', 'incompatible with 30 examples')
    # Invalid boundaries %:
    self.assertRaises(
        'validation[:250%]', 'percent slice boundaries should be in [-100, 100]'
    )
    self.assertRaises(
        'validation[-101%:]',
        'percent slice boundaries should be in [-100, 100]',
    )
    # pct1_dropremainder with < 100 examples
    with self.assertRaisesWithPredicateMatch(
        ValueError, 'with less than 100 elements is forbidden'
    ):
      ri = splits.ReadInstruction(
          'validation', to=99, unit='%', rounding='pct1_dropremainder'
      )
      ri.to_absolute(self.splits)


class GetDatasetFilesTest(testing.TestCase):
  PATH_PATTERN = '/path/mnist-train.tfrecord-0000%d-of-00005'

  def _get_files(self, instruction):
    split_infos = [
        splits.SplitInfo(
            name='train',
            shard_lengths=[3, 2, 3, 2, 3],  # 13 examples.
            num_bytes=0,
            filename_template=_filename_template(
                dataset_name='mnist', split='train'
            ),
        )
    ]
    splits_dict = splits.SplitDict(split_infos=split_infos)
    return splits_dict[instruction].file_instructions

  def test_no_skip_no_take(self):
    instruction = splits._AbsoluteInstruction('train', None, None)
    files = self._get_files(instruction)
    expected_files = []
    for i, n in enumerate([3, 2, 3, 2, 3]):
      expected_files.append(
          shard_utils.FileInstruction(
              filename=self.PATH_PATTERN % i,
              skip=0,
              take=-1,
              examples_in_shard=n,
          )
      )
    self.assertEqual(files, expected_files)

  def test_skip(self):
    # One file is not taken, one file is partially taken.
    instruction = splits._AbsoluteInstruction('train', 4, None)
    files = self._get_files(instruction)
    self.assertEqual(
        files,
        [
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 1,
                skip=1,
                take=-1,
                examples_in_shard=2,
            ),
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 2,
                skip=0,
                take=-1,
                examples_in_shard=3,
            ),
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 3,
                skip=0,
                take=-1,
                examples_in_shard=2,
            ),
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 4,
                skip=0,
                take=-1,
                examples_in_shard=3,
            ),
        ],
    )

  def test_take(self):
    # Two files are not taken, one file is partially taken.
    instruction = splits._AbsoluteInstruction('train', None, 6)
    files = self._get_files(instruction)
    self.assertEqual(
        files,
        [
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 0,
                skip=0,
                take=-1,
                examples_in_shard=3,
            ),
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 1,
                skip=0,
                take=-1,
                examples_in_shard=2,
            ),
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 2,
                skip=0,
                take=1,
                examples_in_shard=3,
            ),
        ],
    )

  def test_skip_take1(self):
    # A single shard with both skip and take.
    instruction = splits._AbsoluteInstruction('train', 1, 2)
    files = self._get_files(instruction)
    self.assertEqual(
        files,
        [
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 0,
                skip=1,
                take=1,
                examples_in_shard=3,
            ),
        ],
    )

  def test_skip_take2(self):
    # 2 elements in across two shards are taken in middle.
    instruction = splits._AbsoluteInstruction('train', 7, 9)
    files = self._get_files(instruction)
    self.assertEqual(
        files,
        [
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 2,
                skip=2,
                take=-1,
                examples_in_shard=3,
            ),
            shard_utils.FileInstruction(
                filename=self.PATH_PATTERN % 3,
                skip=0,
                take=1,
                examples_in_shard=2,
            ),
        ],
    )

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
    filename_template = _filename_template(split='train', dataset_name='mnist')
    split_infos = [
        splits.SplitInfo(
            name='train',
            shard_lengths=[],
            num_bytes=0,
            filename_template=filename_template,
        ),
    ]
    splits_dict = splits.SplitDict(split_infos=split_infos)
    files = splits_dict['train'].file_instructions
    self.assertEqual(files, [])


class SplitInfoTest(testing.TestCase):

  def test_file_spec(self):
    split_info = tfds.core.SplitInfo(
        name='train',
        shard_lengths=[1, 2, 3],
        num_bytes=42,
        filename_template=_filename_template(split='train'),
    )
    self.assertEqual(
        split_info.file_spec(
            file_format=tfds.core.file_adapters.FileFormat.TFRECORD
        ),
        '/path/ds_name-train.tfrecord@3',
    )

  def test_file_spec_missing_template(self):
    split_info = tfds.core.SplitInfo(
        name='train',
        shard_lengths=[1, 2, 3],
        num_bytes=42,
        filename_template=None,
    )
    with self.assertRaises(ValueError):
      split_info.file_spec(
          file_format=tfds.core.file_adapters.FileFormat.TFRECORD
      )

  def test_get_available_shards(self):
    tmp_dir = epath.Path(self.tmp_dir)
    train_shard1 = tmp_dir / 'ds-train.tfrecord-00000-of-00002'
    train_shard1.touch()
    train_shard_incorrect = tmp_dir / 'ds-train.tfrecord-00000-of-12345'
    train_shard_incorrect.touch()
    test_shard1 = tmp_dir / 'ds-test.tfrecord-00000-of-00001'
    test_shard1.touch()

    split_info = splits.SplitInfo(
        name='train',
        shard_lengths=[1, 2],
        num_bytes=42,
        filename_template=_filename_template(
            split='train', data_dir=os.fspath(tmp_dir), dataset_name='ds'
        ),
    )
    self.assertEqual(
        [train_shard1, train_shard_incorrect],
        split_info.get_available_shards(tmp_dir, strict_matching=False),
    )
    self.assertEqual(
        [train_shard1],
        split_info.get_available_shards(tmp_dir, strict_matching=True),
    )


if __name__ == '__main__':
  testing.test_main()
