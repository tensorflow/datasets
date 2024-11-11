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

import collections
import os
import pathlib
from unittest import mock

from etils import epath
import pytest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core import constants
from tensorflow_datasets.core.utils import py_utils


class PyUtilsTest(testing.TestCase):

  def test_is_notebook(self):
    self.assertFalse(py_utils.is_notebook())

  def test_map_nested(self):
    """Test the mapping function."""

    def map_fn(x):
      return x * 10

    result = py_utils.map_nested(
        map_fn,
        {
            'a': 1,
            'b': {
                'c': 2,
                'e': [3, 4, 5],
            },
        },
    )
    self.assertEqual(
        result,
        {
            'a': 10,
            'b': {
                'c': 20,
                'e': [30, 40, 50],
            },
        },
    )

    result = py_utils.map_nested(map_fn, [1, 2, 3])
    self.assertEqual(result, [10, 20, 30])

    result = py_utils.map_nested(map_fn, 1)
    self.assertEqual(result, 10)

  def test_zip_nested(self):
    """Test the zip nested function."""

    arg0 = {
        'a': 1,
        'b': {
            'c': 2,
            'e': [3, 4, 5],
        },
    }
    arg1 = {
        'a': 10,
        'b': {
            'c': 20,
            'e': [30, 40, 50],
        },
    }

    result = py_utils.zip_nested(arg0, arg1)
    self.assertEqual(
        result,
        {
            'a': (1, 10),
            'b': {
                'c': (2, 20),
                'e': [(3, 30), (4, 40), (5, 50)],
            },
        },
    )

    result = py_utils.zip_nested(1, 2)
    self.assertEqual(result, (1, 2))

  def test_dict_only(self):
    def map_fn(x):
      return x[0] + x[1]

    arg0 = {
        'a': (1, 2),
        'b': {
            'c': 2,
            'e': [3, 4, 5],
        },
    }
    arg1 = {
        'a': (10, 20),
        'b': {
            'c': 20,
            'e': [30, 40, 50],
        },
    }

    result = py_utils.zip_nested(arg0, arg1, dict_only=True)
    self.assertEqual(
        result,
        {
            'a': ((1, 2), (10, 20)),
            'b': {
                'c': (2, 20),
                'e': ([3, 4, 5], [30, 40, 50]),
            },
        },
    )

    result = py_utils.map_nested(map_fn, result, dict_only=True)
    self.assertEqual(
        result,
        {
            'a': (1, 2, 10, 20),
            'b': {
                'c': 22,
                'e': [3, 4, 5, 30, 40, 50],
            },
        },
    )

  def test_flatten_nest_dict(self):
    nest_d = {
        'a': 1,
        'b/c': 2,
        'b': {
            'e': 3,
            'f': {'g': 4},
        },
    }
    flat_d = {
        'a': 1,
        'b/c': 2,
        'b/e': 3,
        'b/f/g': 4,
    }

    self.assertEqual(py_utils.flatten_nest_dict(nest_d), flat_d)
    self.assertEqual(py_utils.pack_as_nest_dict(flat_d, nest_d), nest_d)

    nest_d = {
        'a': 1,
        'b': {
            'c': 2,
            'd': 3,
            'e': 4,  # Extra key
        },
    }
    flat_d = {
        'a': 1,
        'b/c': 2,
        'b/d': 3,
    }
    expected = {'a': 1, 'b': {'c': 2, 'd': 3, 'e': None}}
    self.assertEqual(py_utils.pack_as_nest_dict(flat_d, nest_d), expected)

    with self.assertRaisesWithPredicateMatch(ValueError, 'Extra keys'):
      py_utils.pack_as_nest_dict(
          {
              'a': 1,
              'b/c': 2,
              'b/e': 3,
              'b/f/g': 4,
              'b/h': 5,  # Extra key
          },
          nest_d,
      )

    with self.assertRaisesWithPredicateMatch(
        ValueError, 'overwrite existing key:'
    ):
      py_utils.flatten_nest_dict({
          'a': {
              'b': 1,
          },
          'a/b': 2,  # Collision
      })

  def test_flatten_nest_dict_with_dict_list_dict(self):
    nest_d = {
        'conversation': [
            {'content': 'A = 5, B =10, A+B=?', 'role': 'user'},
            {'content': 'A + B = 5 + 10 = 15', 'role': 'assistant'},
        ],
    }
    flat_d = {
        'conversation/content': ['A = 5, B =10, A+B=?', 'A + B = 5 + 10 = 15'],
        'conversation/role': ['user', 'assistant'],
    }
    self.assertEqual(py_utils.flatten_nest_dict(nest_d), flat_d)
    self.assertEqual(py_utils.pack_as_nest_dict(flat_d, nest_d), nest_d)

  def test_reraise(self):
    class CustomError(Exception):

      def __init__(self, *args, **kwargs):  # pylint: disable=super-init-not-called
        pass  # Do not call super() to ensure this would work with bad code.

    with self.assertRaisesRegex(ValueError, 'Caught: '):
      with py_utils.try_reraise('Caught: '):
        raise ValueError

    with self.assertRaisesRegex(ValueError, 'Caught: With message'):
      with py_utils.try_reraise('Caught: '):
        raise ValueError('With message')

    with self.assertRaisesRegex(CustomError, 'Caught: 123'):
      with py_utils.try_reraise('Caught: '):
        raise CustomError(123)

    with self.assertRaisesRegex(CustomError, "('Caught: ', 123, {})"):
      with py_utils.try_reraise('Caught: '):
        raise CustomError(123, {})

    with self.assertRaisesRegex(Exception, 'Caught: '):
      with py_utils.try_reraise('Caught: '):
        ex = CustomError(123, {})
        ex.args = 'Not a tuple'
        raise ex

    with self.assertRaisesRegex(RuntimeError, 'Caught: message'):
      with py_utils.try_reraise('Caught: '):
        raise tf.errors.FailedPreconditionError(None, None, 'message')


class GetClassPathUrlTest(testing.TestCase):

  def test_get_class_path(self):
    cls_path = py_utils.get_class_path(py_utils.NonMutableDict)
    self.assertEqual(cls_path, 'tfds.core.utils.py_utils.NonMutableDict')
    cls_path = py_utils.get_class_path(
        py_utils.NonMutableDict(), use_tfds_prefix=False
    )
    self.assertEqual(
        cls_path, 'tensorflow_datasets.core.utils.py_utils.NonMutableDict'
    )

  def test_get_class_url(self):
    cls_url = py_utils.get_class_url(py_utils.NonMutableDict)
    self.assertEqual(
        cls_url,
        (constants.SRC_BASE_URL + 'tensorflow_datasets/core/utils/py_utils.py'),
    )


def test_list_info_files(tmp_path: pathlib.Path):
  tmp_path.joinpath('test.tfrecord').touch()
  tmp_path.joinpath('test.riegeli').touch()
  tmp_path.joinpath('info.json').touch()

  # Have a info file in the sub-directory. Shouldn't be listed.
  tmp_path.joinpath('diff').mkdir()
  tmp_path.joinpath('diff/info.json').touch()
  info_files = py_utils.list_info_files(tmp_path)

  assert info_files == ['info.json']


def _flatten_with_path(v):
  return list(py_utils.flatten_with_path(v))


def test_flatten_with_path():
  """Test that the flatten function works as expected."""
  assert _flatten_with_path([{'foo': 42}]) == [((0, 'foo'), 42)]

  assert _flatten_with_path('value') == [((), 'value')]
  assert _flatten_with_path({'key': 'value'}) == [(('key',), 'value')]
  # Order doesn't matter
  ordered_dict1 = collections.OrderedDict(
      [('key1', 'value1'), ('key2', 'value2')]
  )
  ordered_dict2 = collections.OrderedDict(
      [('key2', 'value2'), ('key1', 'value1')]
  )
  expected_result = [(('key1',), 'value1'), (('key2',), 'value2')]
  assert _flatten_with_path(ordered_dict1) == expected_result
  assert _flatten_with_path(ordered_dict2) == expected_result

  complex_dict = {
      'key': 'value',
      'nested': {
          'subkey': ['subvalue0', 'subvalue1'],
          'subnested': {
              'subsubkey1': 'subsubvalue1',
              'subsubkey2': 'subsubvalue2',
          },
      },
      'key2': 'value2',
  }
  assert _flatten_with_path(complex_dict) == [
      (('key',), 'value'),
      (('key2',), 'value2'),
      (('nested', 'subkey', 0), 'subvalue0'),
      (('nested', 'subkey', 1), 'subvalue1'),
      (
          (
              'nested',
              'subnested',
              'subsubkey1',
          ),
          'subsubvalue1',
      ),
      (
          (
              'nested',
              'subnested',
              'subsubkey2',
          ),
          'subsubvalue2',
      ),
  ]
  # Order is consistent with tf.nest.flatten
  assert [v for _, v in _flatten_with_path(complex_dict)] == tf.nest.flatten(
      complex_dict
  )


def test_incomplete_file(tmp_path: pathlib.Path):
  tmp_path = epath.Path(tmp_path)
  filepath = tmp_path / 'test.txt'
  with py_utils.incomplete_file(filepath) as tmp_filepath:
    tmp_filepath.write_text('content')
    assert not filepath.exists()
  assert filepath.read_text() == 'content'
  assert not tmp_filepath.exists()  # Tmp file is deleted


@pytest.mark.parametrize(
    ['path', 'is_incomplete'],
    [
        ('/a/incomplete.a8c53d7beff74b2eb31b9b86c7d046cf.bcd', True),
        ('/a/incomplete-dataset.tfrecord-00000-of-00100', False),
        ('/a/prefix.incomplete.a8c53d7beff74b2eb31b9b86c7d046cf', False),
        ('/a/incomplete.a8c53d7beff74beb3.bcd', False),
    ],
)
def test_is_incomplete_file(path: str, is_incomplete: bool):
  assert py_utils.is_incomplete_file(epath.Path(path)) == is_incomplete


@pytest.mark.parametrize(
    ['name', 'expected'],
    [
        ('foobar', 'foobar'),
        ('FooBar', 'FooBar'),
        ('_foo-bar!', '_foo_bar_'),
    ],
)
def test_make_valid_name(name: str, expected: str):
  assert py_utils.make_valid_name(name) == expected


@pytest.mark.parametrize(
    ['path', 'subfolder', 'expected'],
    [
        ('/a/file.ext', None, '/a/foobar.file.ext'),
        ('/a/file.ext', 'sub', '/a/sub/foobar.file.ext'),
    ],
)
def test_tmp_file_name(path, subfolder, expected):
  with mock.patch.object(py_utils, '_tmp_file_prefix', return_value='foobar'):
    assert os.fspath(py_utils._tmp_file_name(path, subfolder)) == expected


if __name__ == '__main__':
  tf.test.main()
