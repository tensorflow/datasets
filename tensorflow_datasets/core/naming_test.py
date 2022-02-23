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

"""Tests tensorflow_datasets.core.naming."""

import os
from absl.testing import parameterized

from etils import epath
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits


class NamingTest(parameterized.TestCase, testing.TestCase):

  @parameterized.parameters(
      ('HelloWorld', 'hello_world'),
      ('FooBARBaz', 'foo_bar_baz'),
      ('FooBar123', 'foo_bar123'),
      ('FooBar123Baz', 'foo_bar123_baz'),
      ('FooBar123baz', 'foo_bar123baz'),
  )
  def test_camelcase_to_snakecase(self, camel, snake):
    self.assertEqual(snake, naming.camelcase_to_snakecase(camel))

  @parameterized.parameters(
      ('HelloWorld', 'hello_world'),
      ('FooBar123', 'foo_bar123'),
      ('FooBar123Baz', 'foo_bar123_baz'),
      ('FooBar123baz', 'foo_bar123baz'),
  )
  def test_snake_to_camelcase(self, camel, snake):
    self.assertEqual(naming.snake_to_camelcase(snake), camel)
    # camelcase_to_snakecase is a no-op if the name is already snake_case.
    self.assertEqual(naming.camelcase_to_snakecase(snake), snake)

  @parameterized.parameters(
      (2, '00000-of-00002', '00001-of-00002'),
      (12345, '00000-of-12345', '12344-of-12345'),
      (654321, '000000-of-654321', '654320-of-654321'),
  )
  def test_sharded_filepaths(self, num_shards: int, expected_first_suffix: str,
                             expected_last_suffix: str):
    template = naming.ShardedFileTemplate(
        split='train',
        dataset_name='ds',
        data_dir='/path',
        filetype_suffix='tfrecord')
    names = template.sharded_filepaths(num_shards)
    path_template = '/path/ds-train.tfrecord-%s'
    self.assertEqual(
        os.fspath(names[0]), path_template % (expected_first_suffix))
    self.assertEqual(
        os.fspath(names[-1]), path_template % (expected_last_suffix))

  @parameterized.parameters(
      ('foo', 'foo-train'),
      ('Foo', 'foo-train'),
      ('FooBar', 'foo_bar-train'),
  )
  def test_filename_prefix_for_split(self, prefix, expected):
    split = splits.Split.TRAIN
    self.assertEqual(expected, naming.filename_prefix_for_split(prefix, split))

  def test_filenames_for_dataset_split(self):
    actual = naming.filenames_for_dataset_split(
        dataset_name='foo',
        split=splits.Split.TRAIN,
        num_shards=2,
        filetype_suffix='bar',
        data_dir='/path')
    self.assertEqual(
        actual,
        ['foo-train.bar-00000-of-00002', 'foo-train.bar-00001-of-00002'])

  def test_filepaths_for_dataset_split(self):
    actual = naming.filepaths_for_dataset_split(
        dataset_name='foo',
        split=splits.Split.TRAIN,
        num_shards=2,
        data_dir='/tmp/bar/',
        filetype_suffix='bar')
    self.assertEqual(actual, [
        '/tmp/bar/foo-train.bar-00000-of-00002',
        '/tmp/bar/foo-train.bar-00001-of-00002'
    ])

  def test_filepattern_for_dataset_split(self):
    self.assertEqual(
        '/tmp/bar/foo-test.bar*',
        naming.filepattern_for_dataset_split(
            dataset_name='foo',
            split=splits.Split.TEST,
            data_dir='/tmp/bar/',
            filetype_suffix='bar'))


def test_dataset_name_and_kwargs_from_name_str():
  assert naming._dataset_name_and_kwargs_from_name_str('ds1') == ('ds1', {})
  assert naming._dataset_name_and_kwargs_from_name_str('ds1:1.2.*') == (
      'ds1',
      {
          'version': '1.2.*'
      },
  )
  assert naming._dataset_name_and_kwargs_from_name_str('ds1/config1') == (
      'ds1', {
          'config': 'config1'
      })
  assert naming._dataset_name_and_kwargs_from_name_str('ds1/config1:1.*.*') == (
      'ds1', {
          'config': 'config1',
          'version': '1.*.*'
      })
  assert naming._dataset_name_and_kwargs_from_name_str(
      'ds1/config1/arg1=val1,arg2=val2') == ('ds1', {
          'config': 'config1',
          'arg1': 'val1',
          'arg2': 'val2'
      })
  assert naming._dataset_name_and_kwargs_from_name_str(
      'ds1/config1:1.2.3/arg1=val1,arg2=val2') == ('ds1', {
          'config': 'config1',
          'version': '1.2.3',
          'arg1': 'val1',
          'arg2': 'val2'
      })
  assert naming._dataset_name_and_kwargs_from_name_str('ds1/arg1=val1') == (
      'ds1', {
          'arg1': 'val1'
      })


def dataset_name():
  name = naming.DatasetName('ds1')
  assert name.name == 'ds1'
  assert name.namespace is None
  assert str(name) == 'ds1'
  assert repr(name) == "DatasetName('ds1')"

  name = naming.DatasetName('namespace123:ds1')
  assert name.name == 'ds1'
  assert name.namespace == 'namespace123'
  assert str(name) == 'namespace123:ds1'
  assert repr(name) == "DatasetName('namespace123:ds1')"

  name = naming.DatasetName(name='ds1', namespace='namespace123')
  assert name.name == 'ds1'
  assert name.namespace == 'namespace123'
  assert str(name) == 'namespace123:ds1'
  assert repr(name) == "DatasetName('namespace123:ds1')"

  name = naming.DatasetName(name='ds1')
  assert name.name == 'ds1'
  assert name.namespace is None
  assert str(name) == 'ds1'
  assert repr(name) == "DatasetName('ds1')"

  with pytest.raises(ValueError, match='Mixing args and kwargs'):
    name = naming.DatasetName('namespace123', name='abc')


@pytest.mark.parametrize(
    ['name', 'result'],
    [
        ('ds1', (naming.DatasetName('ds1'), {})),
        ('ds1:1.0.0', (naming.DatasetName('ds1'), {
            'version': '1.0.0'
        })),
        ('ns1:ds1', (naming.DatasetName('ns1:ds1'), {})),
        (
            'ns1:ds1:1.0.0',
            (naming.DatasetName('ns1:ds1'), {
                'version': '1.0.0'
            }),
        ),
        ('ns1:ds1/conf:1.0.0', (naming.DatasetName('ns1:ds1'), {
            'version': '1.0.0',
            'config': 'conf',
        })),
        ('grand-vision:katr/128x128:1.0.0',
         (naming.DatasetName('grand-vision:katr'), {
             'version': '1.0.0',
             'config': '128x128',
         })),
    ],
)
def test_parse_builder_name_kwargs(name, result):
  assert naming.parse_builder_name_kwargs(name) == result


def test_parse_builder_name_kwargs_with_kwargs():
  parse = naming.parse_builder_name_kwargs

  assert parse(
      'ds1', data_dir='/abc') == (naming.DatasetName('ds1'), {
          'data_dir': '/abc'
      })

  with pytest.raises(TypeError, match='got multiple values for keyword arg'):
    parse('ds1:1.0.0', version='1.0.0')  # Version defined twice

  with pytest.raises(ValueError, match='Parsing builder name string .* failed'):
    parse('ds/config:ns:1.0.0')


def test_is_valid_dataset_name():
  assert naming.is_valid_dataset_name('dataset123_abc')
  assert not naming.is_valid_dataset_name('dataset-abc')
  assert not naming.is_valid_dataset_name('dataset.old')


def test_naming_sorted():
  assert sorted([
      naming.DatasetName('zzz:aaa'),
      naming.DatasetName('aaa:zzz'),
      naming.DatasetName('aaa:aaa'),
  ]) == [
      naming.DatasetName('aaa:aaa'),
      naming.DatasetName('aaa:zzz'),
      naming.DatasetName('zzz:aaa'),
  ]


def test_filename_info_with_small_shard_num():
  filename = 'mnist-test.tfrecord-00000-of-00001'
  assert naming.FilenameInfo.is_valid(filename)
  file_info = naming.FilenameInfo.from_str(filename)
  assert str(file_info) == filename
  assert file_info.dataset_name == 'mnist'
  assert file_info.split == 'test'
  assert file_info.filetype_suffix == 'tfrecord'
  assert file_info.shard_index == 0
  assert file_info.num_shards == 1


def test_filename_info_with_huge_shard_num():
  filenames = [
      'web_image_text-full.tfrecord-056234-of-104448',
      'web_image_text-full.tfrecord-56234-of-104448',  # backward compatible
  ]
  for filename in filenames:
    assert naming.FilenameInfo.is_valid(filename)
    file_info = naming.FilenameInfo.from_str(filename)
    assert str(file_info) == filenames[0]
    assert file_info.dataset_name == 'web_image_text'
    assert file_info.split == 'full'
    assert file_info.filetype_suffix == 'tfrecord'
    assert file_info.shard_index == 56234
    assert file_info.num_shards == 104448


@pytest.mark.parametrize(
    'filename',
    [
        'mnist-train.tfrecord-00000-of-00001',
        'mnist123-test.tfrecord-00032-of-01024',
        'mni23_st-test.riegeli-00032-of-01024',
    ],
)
def test_filename_info_valid(filename):
  assert naming.FilenameInfo.is_valid(filename)
  assert filename == str(naming.FilenameInfo.from_str(filename))


@pytest.mark.parametrize(
    'filename',
    [
        'mnist-train.tfrecord-000-of-001',  # Wrong shard number
        'mni-st-train.tfrecord-00000-of-00001',  # Wrong name
    ],
)
def test_filename_info_invalid(filename):
  assert not naming.FilenameInfo.is_valid(filename)
  with pytest.raises(ValueError, match='Filename .* does not follow pattern'):
    naming.FilenameInfo.from_str(filename)


def test_filename_info_with_path():
  filename_info = naming.FilenameInfo.from_str(
      '/path/mnist-train.tfrecord-00032-of-01024')
  assert filename_info == naming.FilenameInfo(
      dataset_name='mnist',
      split='train',
      filetype_suffix='tfrecord',
      shard_index=32,
      num_shards=1024)


def test_sharded_file_template_sharded_filepath():
  template = naming.ShardedFileTemplate(
      data_dir='/path',
      dataset_name='mnist',
      split='train',
      filetype_suffix='tfrecord')
  assert os.fspath(template.sharded_filepath(
      shard_index=0,
      num_shards=1)) == '/path/mnist-train.tfrecord-00000-of-00001'
  assert os.fspath(template.sharded_filepath(
      shard_index=0,
      num_shards=25)) == '/path/mnist-train.tfrecord-00000-of-00025'
  assert os.fspath(template.sharded_filepath(
      shard_index=10,
      num_shards=25)) == '/path/mnist-train.tfrecord-00010-of-00025'


def test_sharded_file_template_empty_filetype_suffix():
  with pytest.raises(
      ValueError, match='Filetype suffix must be a non-empty string: .+'):
    naming.ShardedFileTemplate(
        data_dir='/path', dataset_name='mnist', filetype_suffix='')


def test_sharded_file_template_empty_split():
  with pytest.raises(ValueError, match='Split must be a non-empty string: .+'):
    naming.ShardedFileTemplate(
        data_dir='/path',
        dataset_name='mnist',
        filetype_suffix='tfrecord',
        split='')


def test_sharded_file_template_shard_index():
  builder_dir = epath.Path('/my/path')
  template = naming.ShardedFileTemplate(
      template='data/mnist-train.tfrecord-{SHARD_INDEX}', data_dir=builder_dir)
  assert os.fspath(template.sharded_filepath(
      shard_index=12,
      num_shards=100)) == '/my/path/data/mnist-train.tfrecord-00012'
  assert os.fspath(template.sharded_filepaths_pattern()
                  ) == '/my/path/data/mnist-train.tfrecord*'
  assert os.fspath(template.sharded_filepaths_pattern(
      num_shards=100)) == '/my/path/data/mnist-train.tfrecord@100'


def test_sharded_file_template_sharded_filepath_shard_x_of_y():
  builder_dir = epath.Path('/my/path')
  template_explicit = naming.ShardedFileTemplate(
      template='data/mnist-train.tfrecord-{SHARD_INDEX}-of-{NUM_SHARDS}',
      data_dir=builder_dir)
  assert os.fspath(
      template_explicit.sharded_filepath(shard_index=12, num_shards=100)
  ) == '/my/path/data/mnist-train.tfrecord-00012-of-00100'

  template = naming.ShardedFileTemplate(
      template='data/mnist-train.tfrecord-{SHARD_X_OF_Y}', data_dir=builder_dir)
  assert os.fspath(template.sharded_filepath(
      shard_index=12,
      num_shards=100)) == '/my/path/data/mnist-train.tfrecord-00012-of-00100'


def test_sharded_file_template_sharded_filepath_shard_x_of_y_more_digits():
  builder_dir = epath.Path('/my/path')
  template = naming.ShardedFileTemplate(
      template='data/{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}',
      data_dir=builder_dir,
      dataset_name='mnist',
      filetype_suffix='tfrecord',
      split='train',
  )
  assert os.fspath(
      template.sharded_filepath(shard_index=12, num_shards=1234567)
  ) == '/my/path/data/mnist-train.tfrecord-0000012-of-1234567'


def test_sharded_file_template_no_template():
  builder_dir = epath.Path('/my/path')
  template = naming.ShardedFileTemplate(
      data_dir=builder_dir,
      dataset_name='imagenet',
      filetype_suffix='riegeli',
      split='test')
  assert os.fspath(template.sharded_filepath(
      shard_index=12,
      num_shards=100)) == '/my/path/imagenet-test.riegeli-00012-of-00100'


def test_sharded_file_template_no_template_incomplete():
  builder_dir = epath.Path('/my/path')
  template_without_split = naming.ShardedFileTemplate(
      data_dir=builder_dir, dataset_name='imagenet', filetype_suffix='riegeli')
  with pytest.raises(KeyError):
    template_without_split.sharded_filepath(shard_index=12, num_shards=100)


def test_sharded_file_template_template_and_properties():
  builder_dir = epath.Path('/my/path')
  template = naming.ShardedFileTemplate(
      template='data/mnist-{SPLIT}.{FILEFORMAT}-{SHARD_INDEX}',
      data_dir=builder_dir,
      # dataset_name is ignored because the template doesn't have {DATASET}
      dataset_name='imagenet',
      filetype_suffix='riegeli',
      split='test')
  assert os.fspath(template.sharded_filepath(
      shard_index=12,
      num_shards=100)) == '/my/path/data/mnist-test.riegeli-00012'


def test_replace_shard_suffix():
  assert naming._replace_shard_suffix(
      filepath='/path/file-00001-of-01234',
      replacement='repl') == '/path/filerepl'
  assert naming._replace_shard_suffix(
      filepath='/path/file00001-of-01234',
      replacement='repl') == '/path/filerepl'
  assert naming._replace_shard_suffix(
      filepath='/path/file-00001', replacement='repl') == '/path/filerepl'


def test_replace_shard_suffix_folder_similar_to_shard():
  assert naming._replace_shard_suffix(
      filepath='/path/i-look-like-a-shard-000001/file-00001-of-01234',
      replacement='repl') == '/path/i-look-like-a-shard-000001/filerepl'


def test_replace_shard_suffix_no_suffix_found():
  with pytest.raises(RuntimeError, match='Should do 1 shard suffix'):
    naming._replace_shard_suffix(filepath='/path/a/b', replacement='')
