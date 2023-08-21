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

"""Tests tensorflow_datasets.core.naming."""

import os
from absl.testing import parameterized
from etils import epath
import pytest
from tensorflow_datasets import testing
from tensorflow_datasets.core import naming
from tensorflow_datasets.core import splits

_FILENAME_TEMPLATE_DEFAULT = naming.ShardedFileTemplate(data_dir='.')
_FILENAME_TEMPLATE_MNIST_DEFAULT = naming.ShardedFileTemplate(
    data_dir='/path',
    dataset_name='mnist',
    split='train',
    filetype_suffix='tfrecord',
)
_FILENAME_TEMPLATE_CUSTOM_NO_EXTRA = naming.ShardedFileTemplate(
    data_dir='/path', template='{SPLIT}.{SHARD_INDEX}'
)
_FILENAME_TEMPLATE_CUSTOM_FULL = naming.ShardedFileTemplate(
    data_dir='/path',
    template='{SPLIT}.{SHARD_INDEX}',
    dataset_name='mnist',
    split='train',
    filetype_suffix='tfrecord',
)


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
  def test_sharded_filepaths(
      self,
      num_shards: int,
      expected_first_suffix: str,
      expected_last_suffix: str,
  ):
    template = naming.ShardedFileTemplate(
        split='train',
        dataset_name='ds',
        data_dir='/path',
        filetype_suffix='tfrecord',
    )
    names = template.sharded_filepaths(num_shards)
    path_template = '/path/ds-train.tfrecord-%s'
    self.assertEqual(
        os.fspath(names[0]), path_template % (expected_first_suffix)
    )
    self.assertEqual(
        os.fspath(names[-1]), path_template % (expected_last_suffix)
    )

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
        data_dir='/path',
    )
    self.assertEqual(
        actual, ['foo-train.bar-00000-of-00002', 'foo-train.bar-00001-of-00002']
    )

  def test_filepaths_for_dataset_split(self):
    actual = naming.filepaths_for_dataset_split(
        dataset_name='foo',
        split=splits.Split.TRAIN,
        num_shards=2,
        data_dir='/tmp/bar/',
        filetype_suffix='bar',
    )
    self.assertEqual(
        actual,
        [
            '/tmp/bar/foo-train.bar-00000-of-00002',
            '/tmp/bar/foo-train.bar-00001-of-00002',
        ],
    )

  def test_filepattern_for_dataset_split(self):
    self.assertEqual(
        '/tmp/bar/foo-test.bar*',
        naming.filepattern_for_dataset_split(
            dataset_name='foo',
            split=splits.Split.TEST,
            data_dir='/tmp/bar/',
            filetype_suffix='bar',
        ),
    )


def test_dataset_name_and_kwargs_from_name_str():
  assert naming._dataset_name_and_kwargs_from_name_str('ds1') == ('ds1', {})
  assert naming._dataset_name_and_kwargs_from_name_str('ds1:1.2.*') == (
      'ds1',
      {'version': '1.2.*'},
  )
  assert naming._dataset_name_and_kwargs_from_name_str('ds1/config1') == (
      'ds1',
      {'config': 'config1'},
  )
  assert naming._dataset_name_and_kwargs_from_name_str('ds1/config1:1.*.*') == (
      'ds1',
      {'config': 'config1', 'version': '1.*.*'},
  )
  assert naming._dataset_name_and_kwargs_from_name_str(
      'ds1/config1/arg1=val1,arg2=val2'
  ) == ('ds1', {'config': 'config1', 'arg1': 'val1', 'arg2': 'val2'})
  assert naming._dataset_name_and_kwargs_from_name_str(
      'ds1/config1:1.2.3/arg1=val1,arg2=val2'
  ) == (
      'ds1',
      {'config': 'config1', 'version': '1.2.3', 'arg1': 'val1', 'arg2': 'val2'},
  )
  assert naming._dataset_name_and_kwargs_from_name_str('ds1/arg1=val1') == (
      'ds1',
      {'arg1': 'val1'},
  )


def test_dataset_name():
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
        ('ds1:1.0.0', (naming.DatasetName('ds1'), {'version': '1.0.0'})),
        ('ns1:ds1', (naming.DatasetName('ns1:ds1'), {})),
        (
            'hugging_face:abc',
            (naming.DatasetName(namespace='hugging_face', name='abc'), {}),
        ),
        (
            'ns_1-b:ds1',
            (naming.DatasetName(namespace='ns_1-b', name='ds1'), {}),
        ),
        (
            'ns1:ds1:1.0.0',
            (naming.DatasetName('ns1:ds1'), {'version': '1.0.0'}),
        ),
        (
            'ns1:ds1/conf:1.0.0',
            (
                naming.DatasetName('ns1:ds1'),
                {
                    'version': '1.0.0',
                    'config': 'conf',
                },
            ),
        ),
        (
            'grand-vision:katr/128x128:1.0.0',
            (
                naming.DatasetName('grand-vision:katr'),
                {
                    'version': '1.0.0',
                    'config': '128x128',
                },
            ),
        ),
        (
            'huggingface:swiss_judgment_prediction/all+mt',
            (
                naming.DatasetName('huggingface:swiss_judgment_prediction'),
                {
                    'config': 'all+mt',
                },
            ),
        ),
    ],
)
def test_parse_builder_name_kwargs(name, result):
  assert naming.parse_builder_name_kwargs(name) == result


def test_parse_builder_name_kwargs_with_kwargs():
  parse = naming.parse_builder_name_kwargs

  assert parse('ds1', data_dir='/abc') == (
      naming.DatasetName('ds1'),
      {'data_dir': '/abc'},
  )

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


def test_filename_info_with_custom_template():
  template = _FILENAME_TEMPLATE_CUSTOM_FULL
  filename = 'test.00042'
  file_info = naming.FilenameInfo.from_str(filename, filename_template=template)
  assert str(file_info) == filename
  assert file_info.dataset_name == 'mnist'
  assert file_info.split == 'test'
  assert file_info.filetype_suffix == 'tfrecord'
  assert file_info.shard_index == 42
  assert file_info.num_shards is None
  # This is not valid because the template is for the train split
  assert not naming.FilenameInfo.is_valid(filename, filename_template=template)
  assert naming.FilenameInfo.is_valid(
      filename, filename_template=template.replace(split='test')
  )


def test_filename_info_with_custom_template_missing_fields():
  template = _FILENAME_TEMPLATE_CUSTOM_NO_EXTRA
  filename = 'test.00042'
  assert naming.FilenameInfo.is_valid(filename, filename_template=template)
  file_info = naming.FilenameInfo.from_str(filename, filename_template=template)
  assert str(file_info) == filename
  assert file_info.dataset_name is None
  assert file_info.split == 'test'
  assert file_info.filetype_suffix is None
  assert file_info.shard_index == 42
  assert file_info.num_shards is None


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


def test_filename_info_invalid():
  filename = 'mnist-train.tfrecord-000-of-001'  # Wrong shard number
  assert not naming.FilenameInfo.is_valid(filename)
  with pytest.raises(ValueError, match='Could not parse filename'):
    naming.FilenameInfo.from_str(filename)


def test_filename_info_with_path():
  filename_info = naming.FilenameInfo.from_str(
      '/path/mnist-train.tfrecord-00032-of-01024'
  )
  assert filename_info == naming.FilenameInfo(
      dataset_name='mnist',
      split='train',
      filetype_suffix='tfrecord',
      shard_index=32,
      num_shards=1024,
      filename_template=_FILENAME_TEMPLATE_DEFAULT.replace(data_dir='/path'),
  )


def test_filename_info_with_path_and_dash_in_split():
  filename_info = naming.FilenameInfo.from_str(
      '/path/c4-af-validation.tfrecord-00032-of-01024'
  )
  assert filename_info == naming.FilenameInfo(
      dataset_name='c4',
      split='af-validation',
      filetype_suffix='tfrecord',
      shard_index=32,
      num_shards=1024,
      filename_template=_FILENAME_TEMPLATE_DEFAULT.replace(data_dir='/path'),
  )


def test_filename_info_with_path_and_two_dashes_in_split():
  filename_info = naming.FilenameInfo.from_str(
      '/path/c4-bg-Latn-validation.tfrecord-00032-of-01024'
  )
  assert filename_info == naming.FilenameInfo(
      dataset_name='c4',
      split='bg-Latn-validation',
      filetype_suffix='tfrecord',
      shard_index=32,
      num_shards=1024,
      filename_template=_FILENAME_TEMPLATE_DEFAULT.replace(data_dir='/path'),
  )


def test_sharded_file_template_sharded_filepath():
  template = _FILENAME_TEMPLATE_MNIST_DEFAULT
  assert (
      os.fspath(template.sharded_filepath(shard_index=0, num_shards=1))
      == '/path/mnist-train.tfrecord-00000-of-00001'
  )
  assert (
      os.fspath(template.sharded_filepath(shard_index=0, num_shards=25))
      == '/path/mnist-train.tfrecord-00000-of-00025'
  )
  assert (
      os.fspath(template.sharded_filepath(shard_index=10, num_shards=25))
      == '/path/mnist-train.tfrecord-00010-of-00025'
  )


def test_sharded_file_template_empty_filetype_suffix():
  with pytest.raises(
      ValueError, match='Filetype suffix must be a non-empty string: .+'
  ):
    naming.ShardedFileTemplate(
        data_dir='/path', dataset_name='mnist', filetype_suffix=''
    )


def test_sharded_file_template_empty_split():
  with pytest.raises(ValueError, match='Split must be a non-empty string: .+'):
    naming.ShardedFileTemplate(
        data_dir='/path',
        dataset_name='mnist',
        filetype_suffix='tfrecord',
        split='',
    )


@pytest.mark.parametrize('split_name', [':', ',', '(())'])
def test_sharded_file_template_non_alphanumeric_split(split_name):
  match = (
      'Split name should contain at least one alphanumeric character. Given'
      f' split name: {split_name}'
  )
  with pytest.raises(
      ValueError,
      match=match,
  ):
    naming.ShardedFileTemplate(
        data_dir='/path',
        dataset_name='ds',
        filetype_suffix='',
        split=split_name,
    )


@pytest.mark.parametrize('split_name', ['train', '1', 'c', 'train_1', 'c:'])
def test_sharded_file_template_valid_split(split_name):
  naming.ShardedFileTemplate(
      data_dir='/path',
      dataset_name='mnist',
      filetype_suffix='tfrecord',
      split=split_name,
  )


def test_sharded_file_template_shard_index():
  builder_dir = epath.Path('/my/path')
  template = naming.ShardedFileTemplate(
      template='data/mnist-train.tfrecord-{SHARD_INDEX}', data_dir=builder_dir
  )
  assert (
      os.fspath(template.sharded_filepath(shard_index=12, num_shards=100))
      == '/my/path/data/mnist-train.tfrecord-00012'
  )
  assert (
      os.fspath(template.sharded_filepaths_pattern())
      == '/my/path/data/mnist-train.tfrecord*'
  )
  assert (
      os.fspath(template.sharded_filepaths_pattern(num_shards=100))
      == '/my/path/data/mnist-train.tfrecord@100'
  )


def test_sharded_file_template_sharded_filepath_shard_x_of_y():
  builder_dir = epath.Path('/my/path')
  template_explicit = naming.ShardedFileTemplate(
      template='data/mnist-train.tfrecord-{SHARD_INDEX}-of-{NUM_SHARDS}',
      data_dir=builder_dir,
  )
  assert (
      os.fspath(
          template_explicit.sharded_filepath(shard_index=12, num_shards=100)
      )
      == '/my/path/data/mnist-train.tfrecord-00012-of-00100'
  )

  template = naming.ShardedFileTemplate(
      template='data/mnist-train.tfrecord-{SHARD_X_OF_Y}', data_dir=builder_dir
  )
  assert (
      os.fspath(template.sharded_filepath(shard_index=12, num_shards=100))
      == '/my/path/data/mnist-train.tfrecord-00012-of-00100'
  )


def test_sharded_file_template_sharded_filepath_shard_x_of_y_more_digits():
  builder_dir = epath.Path('/my/path')
  template = naming.ShardedFileTemplate(
      template='data/{DATASET}-{SPLIT}.{FILEFORMAT}-{SHARD_X_OF_Y}',
      data_dir=builder_dir,
      dataset_name='mnist',
      filetype_suffix='tfrecord',
      split='train',
  )
  assert (
      os.fspath(template.sharded_filepath(shard_index=12, num_shards=1234567))
      == '/my/path/data/mnist-train.tfrecord-0000012-of-1234567'
  )


def test_sharded_file_template_no_template():
  builder_dir = epath.Path('/my/path')
  template = naming.ShardedFileTemplate(
      data_dir=builder_dir,
      dataset_name='imagenet',
      filetype_suffix='riegeli',
      split='test',
  )
  assert (
      os.fspath(template.sharded_filepath(shard_index=12, num_shards=100))
      == '/my/path/imagenet-test.riegeli-00012-of-00100'
  )


def test_sharded_file_template_no_template_incomplete():
  builder_dir = epath.Path('/my/path')
  template_without_split = naming.ShardedFileTemplate(
      data_dir=builder_dir, dataset_name='imagenet', filetype_suffix='riegeli'
  )
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
      split='test',
  )
  assert (
      os.fspath(template.sharded_filepath(shard_index=12, num_shards=100))
      == '/my/path/data/mnist-test.riegeli-00012'
  )


def test_replace_shard_suffix():
  assert (
      naming._replace_shard_suffix(
          filepath='/path/file-00001-of-01234', replacement='repl'
      )
      == '/path/filerepl'
  )
  assert (
      naming._replace_shard_suffix(
          filepath='/path/file00001-of-01234', replacement='repl'
      )
      == '/path/filerepl'
  )
  assert (
      naming._replace_shard_suffix(
          filepath='/path/file-00001', replacement='repl'
      )
      == '/path/filerepl'
  )


def test_replace_shard_suffix_folder_similar_to_shard():
  assert (
      naming._replace_shard_suffix(
          filepath='/path/i-look-like-a-shard-000001/file-00001-of-01234',
          replacement='repl',
      )
      == '/path/i-look-like-a-shard-000001/filerepl'
  )


def test_replace_shard_suffix_no_suffix_found():
  with pytest.raises(RuntimeError, match='Should do 1 shard suffix'):
    naming._replace_shard_suffix(filepath='/path/a/b', replacement='')


def test_filename_template_to_regex():
  assert (
      naming._filename_template_to_regex('{DATASET}')
      == r'(?P<dataset_name>[a-zA-Z][\w]*)'
  )
  assert naming._filename_template_to_regex(
      naming.DEFAULT_FILENAME_TEMPLATE
  ) == (
      r'(?P<dataset_name>[a-zA-Z][\w]*)'
      r'-(?P<split>(\w|-)+)'
      r'\.(?P<filetype_suffix>\w+)'
      r'-(?P<shard_index>\d{5,})-of-(?P<num_shards>\d{5,})'
  )


def test_filename_template_to_regex_unknown_variables():
  with pytest.raises(ValueError, match='Regex still contains variables.+'):
    naming._filename_template_to_regex('{XYZ}')


@pytest.mark.parametrize(
    ['name', 'result'],
    [
        ('mnist-train.tfrecord-00000-of-00001', True),
        ('xyz-train.tfrecord-00000-of-00001', False),
        ('mnist-xyz.tfrecord-00000-of-00001', False),
        ('mnist-train.xyz-00000-of-00001', False),
        ('mnist-train.tfrecord-a-of-b', False),
    ],
)
def test_sharded_file_template_is_valid_default_template(name, result):
  template = _FILENAME_TEMPLATE_MNIST_DEFAULT
  assert template.is_valid(name) == result


@pytest.mark.parametrize(
    ['name', 'result'],
    [
        ('train.1', False),
        ('train.00001', True),
        ('train-00001', False),
        ('train.tfrecord.00001', False),
        ('mnist-train.tfrecord-00000-of-00001', False),
    ],
)
def test_sharded_file_template_is_valid_custom_template(name, result):
  template = _FILENAME_TEMPLATE_CUSTOM_FULL
  assert template.is_valid(name) == result


@pytest.mark.parametrize(
    ['name', 'result'],
    [
        (
            'mnist-train.tfrecord-00000-of-00001',
            naming.FilenameInfo(
                dataset_name='mnist',
                split='train',
                filetype_suffix='tfrecord',
                shard_index=0,
                num_shards=1,
                filename_template=_FILENAME_TEMPLATE_MNIST_DEFAULT,
            ),
        ),
        (
            'mnist-train.tfrecord-00123-of-00456',
            naming.FilenameInfo(
                dataset_name='mnist',
                split='train',
                filetype_suffix='tfrecord',
                shard_index=123,
                num_shards=456,
                filename_template=_FILENAME_TEMPLATE_MNIST_DEFAULT,
            ),
        ),
        ('train1', None),
    ],
)
def test_sharded_file_template_parse_filename_info(name, result):
  template = _FILENAME_TEMPLATE_MNIST_DEFAULT
  assert template.parse_filename_info(name) == result


@pytest.mark.parametrize(
    ['name', 'result'],
    [
        (
            'train.00123',
            naming.FilenameInfo(
                dataset_name=None,
                split='train',
                filetype_suffix=None,
                shard_index=123,
                num_shards=None,
                filename_template=_FILENAME_TEMPLATE_CUSTOM_NO_EXTRA,
            ),
        ),
        ('mnist-train.tfrecord-00000-of-00001', None),
        ('train1', None),
    ],
)
def test_sharded_file_template_parse_filename_info_custom_template(
    name, result
):
  template = _FILENAME_TEMPLATE_CUSTOM_NO_EXTRA
  assert template.parse_filename_info(name) == result


@pytest.mark.parametrize(
    ['name', 'result'],
    [
        (
            'train.00123',
            naming.FilenameInfo(
                dataset_name='mnist',
                split='train',
                filetype_suffix='tfrecord',
                shard_index=123,
                num_shards=None,
                filename_template=_FILENAME_TEMPLATE_CUSTOM_FULL,
            ),
        ),
        (
            'test.00042',
            naming.FilenameInfo(
                dataset_name='mnist',
                split='test',
                filetype_suffix='tfrecord',
                shard_index=42,
                num_shards=None,
                filename_template=_FILENAME_TEMPLATE_CUSTOM_FULL,
            ),
        ),
        ('mnist-train.tfrecord-00000-of-00001', None),
        ('train1', None),
    ],
)
def test_sharded_file_template_parse_filename_info_custom_template_add_missing(
    name, result
):
  template = _FILENAME_TEMPLATE_CUSTOM_FULL
  assert template.parse_filename_info(name) == result


@pytest.mark.parametrize(
    (
        'tfds_name',
        'namespace',
        'split_mapping',
        'data_dir',
        'ds_name',
        'version',
        'config',
    ),
    [
        # Dataset with a config and a version.
        ('ds/config:1.2.3', None, None, None, 'ds', '1.2.3', 'config'),
        # Dataset with a config and a version and a data_dir.
        ('ds/config:1.2.3', None, None, '/a/b', 'ds', '1.2.3', 'config'),
        # Test having a split mapping.
        ('ds/config:1.2.3', None, {'x': 'y'}, None, 'ds', '1.2.3', 'config'),
        # Dataset without a config but with a version.
        ('ds:1.2.3', None, None, None, 'ds', '1.2.3', None),
        # Dataset with a config but without a version.
        ('ds/config', None, None, None, 'ds', None, 'config'),
        # Dataset without a config and a version.
        ('ds', None, None, None, 'ds', None, None),
        # Dataset with a namespace.
        ('ns:ds/config:1.2.3', 'ns', None, '/a/b', 'ds', '1.2.3', 'config'),
    ],
)
def test_dataset_reference_from_tfds_name(
    tfds_name, namespace, split_mapping, data_dir, ds_name, version, config
):
  actual = naming.DatasetReference.from_tfds_name(
      tfds_name=tfds_name, split_mapping=split_mapping, data_dir=data_dir
  )
  assert actual == naming.DatasetReference(
      dataset_name=ds_name,
      namespace=namespace,
      version=version,
      config=config,
      split_mapping=split_mapping,
      data_dir=data_dir,
  )


@pytest.mark.parametrize(
    ('ds_name', 'namespace', 'version', 'config', 'tfds_name'),
    [
        ('ds', 'ns', '1.2.3', 'config', 'ns:ds/config:1.2.3'),
        ('ds', None, '1.2.3', 'config', 'ds/config:1.2.3'),
        ('ds', None, '1.2.3', None, 'ds:1.2.3'),
        ('ds', None, None, None, 'ds'),
    ],
)
def test_dataset_reference_tfds_name(
    ds_name, namespace, version, config, tfds_name
):
  reference = naming.DatasetReference(
      dataset_name=ds_name, namespace=namespace, version=version, config=config
  )
  assert reference.tfds_name() == tfds_name


def test_dataset_reference_tfds_name_without_version():
  reference = naming.DatasetReference(
      dataset_name='ds', version='1.2.3', config='config'
  )
  assert reference.tfds_name(include_version=False) == 'ds/config'


@pytest.mark.parametrize(
    ('tfds_name', 'data_dir', 'dataset_dir'),
    [
        ('ns:ds/config:1.2.3', '/a/b', '/a/b/ds/config/1.2.3'),
        ('ds/config:1.2.3', '/a/b', '/a/b/ds/config/1.2.3'),
        ('ds:1.2.3', '/a/b', '/a/b/ds/1.2.3'),
    ],
)
def test_dataset_reference_dataset_dir(tfds_name, data_dir, dataset_dir):
  reference = naming.DatasetReference.from_tfds_name(
      tfds_name=tfds_name, data_dir=data_dir
  )
  assert os.fspath(reference.dataset_dir()) == dataset_dir

  # Also test passing the data_dir to `.dataset_dir`
  reference = naming.DatasetReference.from_tfds_name(
      tfds_name=tfds_name, data_dir='/something/else'
  )
  assert os.fspath(reference.dataset_dir(data_dir=data_dir)) == dataset_dir


def test_dataset_reference_get_split():
  reference = naming.DatasetReference.from_tfds_name(
      'ds/config:1.2.3', split_mapping={'x': 'y'}
  )
  assert reference.get_split('x') == 'y'
  assert reference.get_split('y') == 'y'
  assert reference.get_split('z') == 'z'


def test_references_for():
  expected = {
      'one': naming.DatasetReference(
          dataset_name='ds1', version='1.2.3', config='config'
      ),
      'two': naming.DatasetReference(dataset_name='ds2', version='1.0.0'),
  }
  assert (
      naming.references_for({'one': 'ds1/config:1.2.3', 'two': 'ds2:1.0.0'})
      == expected
  )


def test_reference_for():
  expected = naming.DatasetReference(
      dataset_name='ds', version='1.2.3', config='config'
  )
  assert naming.reference_for('ds/config:1.2.3') == expected
