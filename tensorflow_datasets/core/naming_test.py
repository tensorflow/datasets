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

"""Tests tensorflow_datasets.core.naming."""

from absl.testing import parameterized

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

  def test_sharded_filenames(self):
    prefix = '/tmp/foo'
    num_shards = 2
    expected = [
        '/tmp/foo-00000-of-00002',
        '/tmp/foo-00001-of-00002',
    ]
    self.assertEqual(expected, naming.sharded_filenames(prefix, num_shards))

  @parameterized.parameters(
      ('foo', 'foo-train'),
      ('Foo', 'foo-train'),
      ('FooBar', 'foo_bar-train'),
  )
  def test_filename_prefix_for_split(self, prefix, expected):
    split = splits.Split.TRAIN
    self.assertEqual(expected, naming.filename_prefix_for_split(prefix, split))

  def test_filenames_for_dataset_split(self):
    self.assertEqual([
        'foo-train-00000-of-00002',
        'foo-train-00001-of-00002',
    ],
                     naming.filenames_for_dataset_split(
                         dataset_name='foo',
                         split=splits.Split.TRAIN,
                         num_shards=2))

  def test_filepaths_for_dataset_split(self):
    self.assertEqual([
        '/tmp/bar/foo-train-00000-of-00002',
        '/tmp/bar/foo-train-00001-of-00002',
    ],
                     naming.filepaths_for_dataset_split(
                         dataset_name='foo',
                         split=splits.Split.TRAIN,
                         num_shards=2,
                         data_dir='/tmp/bar/'))

  def test_filepaths_for_dataset_split_with_suffix(self):
    self.assertEqual([
        '/tmp/bar/foo-train.bar-00000-of-00002',
        '/tmp/bar/foo-train.bar-00001-of-00002',
    ],
                     naming.filepaths_for_dataset_split(
                         dataset_name='foo',
                         split=splits.Split.TRAIN,
                         num_shards=2,
                         data_dir='/tmp/bar/',
                         filetype_suffix='bar'))

  def test_filepattern_for_dataset_split(self):
    self.assertEqual(
        '/tmp/bar/foo-test*',
        naming.filepattern_for_dataset_split(
            dataset_name='foo', split=splits.Split.TEST, data_dir='/tmp/bar/'))
    self.assertEqual(
        '/tmp/bar/foo-test.bar*',
        naming.filepattern_for_dataset_split(
            dataset_name='foo',
            split=splits.Split.TEST,
            filetype_suffix='bar',
            data_dir='/tmp/bar/'))


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
