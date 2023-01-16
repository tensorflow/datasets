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

"""Tests for tensorflow_datasets.core.test_utils."""

import pathlib

import pytest

import tensorflow as tf

from tensorflow_datasets.testing import test_case
from tensorflow_datasets.testing import test_utils


class RunInGraphAndEagerTest(test_case.TestCase):

  def test_run_in_graph_and_eager_modes(self):
    l = []

    def inc(self, with_brackets):
      del self  # self argument is required by run_in_graph_and_eager_modes.
      mode = 'eager' if tf.executing_eagerly() else 'graph'
      with_brackets = 'with_brackets' if with_brackets else 'without_brackets'
      l.append((with_brackets, mode))

    f = test_utils.run_in_graph_and_eager_modes(inc)
    f(self, with_brackets=False)
    f = test_utils.run_in_graph_and_eager_modes()(inc)
    f(self, with_brackets=True)

    self.assertEqual(len(l), 4)
    self.assertEqual(
        set(l),
        {
            ('with_brackets', 'graph'),
            ('with_brackets', 'eager'),
            ('without_brackets', 'graph'),
            ('without_brackets', 'eager'),
        },
    )

  def test_run_in_graph_and_eager_modes_setup_in_same_mode(self):
    modes = []
    mode_name = lambda: 'eager' if tf.executing_eagerly() else 'graph'

    class ExampleTest(test_case.TestCase):

      def runTest(self):
        pass

      def setUp(self):
        super(ExampleTest, self).setUp()
        modes.append('setup_' + mode_name())

      def subTest(self, msg, **params):
        modes.append('subtest_' + msg)
        return super().subTest(msg, **params)

      @test_utils.run_in_graph_and_eager_modes
      def testBody(self):
        modes.append('run_' + mode_name())

    e = ExampleTest()
    e.setUp()
    e.testBody()

    self.assertEqual(
        modes,
        [
            'setup_eager',
            'subtest_eager_mode',
            'run_eager',
            'subtest_graph_mode',
            'setup_graph',
            'run_graph',
        ],
    )

  def test_mock_tf(self):
    # pylint: disable=g-import-not-at-top,reimported
    import tensorflow as tf_lib1
    import tensorflow as tf_lib2

    # pylint: enable=g-import-not-at-top,reimported

    def f():
      pass

    original_exists = tf_lib1.io.gfile.exists
    original_list_dir = tf_lib1.io.gfile.listdir

    self.assertIs(tf_lib1.io.gfile.exists, original_exists)
    self.assertIs(tf_lib2.io.gfile.listdir, original_list_dir)

    with test_utils.mock_tf('tf.io.gfile', exists=f):
      # Both aliases should have been patched
      self.assertIs(tf_lib1.io.gfile.exists, f)
      self.assertIs(tf_lib2.io.gfile.exists, f)
      self.assertIs(tf_lib1.io.gfile.listdir, original_list_dir)
      self.assertIs(tf_lib2.io.gfile.listdir, original_list_dir)

    self.assertIsNot(tf_lib1.io.gfile.exists, f)
    self.assertIsNot(tf_lib2.io.gfile.exists, f)
    self.assertIs(tf_lib1.io.gfile.exists, original_exists)
    self.assertIs(tf_lib1.io.gfile.listdir, original_list_dir)
    self.assertIs(tf_lib2.io.gfile.exists, original_exists)
    self.assertIs(tf_lib2.io.gfile.listdir, original_list_dir)

    with test_utils.mock_tf('tf.io.gfile.exists', f):
      self.assertIs(tf_lib1.io.gfile.exists, f)
      self.assertIs(tf_lib2.io.gfile.exists, f)
      self.assertIs(tf_lib1.io.gfile.listdir, original_list_dir)
      self.assertIs(tf_lib2.io.gfile.listdir, original_list_dir)


@pytest.mark.parametrize(
    'as_path_fn', [pathlib.Path, str]  # Test both PathLike and str
)
def test_mock_fs(as_path_fn):
  _p = as_path_fn  # pylint: disable=invalid-name
  fs = test_utils.MockFs()
  with fs.mock():
    fs.add_file(_p('/path/to/file1'), 'Content of file 1')
    fs.add_file(_p('/path/file.txt'), 'Content of file.txt')

    # Test `tf.io.gfile.exists`
    assert tf.io.gfile.exists(_p('/path/to/file1'))
    assert tf.io.gfile.exists(_p('/path/to/'))
    assert tf.io.gfile.exists(_p('/path/to'))
    assert tf.io.gfile.exists(_p('/path'))
    assert not tf.io.gfile.exists(_p('/pat'))
    assert not tf.io.gfile.exists(_p('/path/to/file1_nonexisting'))
    assert not tf.io.gfile.exists(_p('/path/to_file1_nonexisting'))

    # Test `tf.io.gfile.exists` (relative path)
    fs.add_file(_p('relative_path/to/file.txt'), 'Content')
    assert tf.io.gfile.exists(_p('relative_path/to/file.txt'))
    assert tf.io.gfile.exists(_p('relative_path/to/'))
    assert tf.io.gfile.exists(_p('relative_path/to'))
    assert tf.io.gfile.exists(_p('relative_path'))

    # Test `tf.io.gfile.GFile` (write and read mode)
    with tf.io.gfile.GFile(_p('/path/to/file2'), 'w') as f:
      f.write('Content of file 2 (old)')
    assert fs.read_file('/path/to/file2') == 'Content of file 2 (old)'
    with tf.io.gfile.GFile(_p('/path/to/file2'), 'w') as f:
      f.write('Content of file 2 (new)')
    assert fs.read_file('/path/to/file2') == 'Content of file 2 (new)'
    with tf.io.gfile.GFile(_p('/path/to/file2'), 'r') as f:
      assert f.read() == 'Content of file 2 (new)'

    # Test `tf.io.gfile.rename`
    assert fs.read_file('/path/to/file1') == 'Content of file 1'
    tf.io.gfile.rename(_p('/path/to/file1'), _p('/path/to/file1_moved'))
    assert not tf.io.gfile.exists('/path/to/file1')
    assert fs.read_file('/path/to/file1_moved') == 'Content of file 1'

    # Test `tf.io.gfile.listdir`
    assert set(tf.io.gfile.listdir(_p('/path/to'))) == set(
        tf.io.gfile.listdir(_p('/path/to/'))
    )
    assert set(tf.io.gfile.listdir(_p('/path/to'))) == {'file1_moved', 'file2'}
    assert set(tf.io.gfile.listdir(_p('/path'))) == {'file.txt', 'to'}

    # Test `MockFs.files`
    assert fs.read_file('/path/to/file2') == 'Content of file 2 (new)'
    assert fs.read_file('/path/to/file1_moved') == 'Content of file 1'
    assert fs.read_file('/path/file.txt') == 'Content of file.txt'
    assert fs.read_file('relative_path/to/file.txt') == 'Content'


def test_mock_fs_gcs():
  with test_utils.MockFs():
    tf.io.gfile.makedirs('gs://bucket/dir/subdir')
    assert tf.io.gfile.exists('gs://bucket/dir')
    assert tf.io.gfile.exists('gs://bucket/dir/subdir')

    with tf.io.gfile.GFile('gs://bucket/dir/file.txt', 'w') as f:
      f.write('Content of file')

    assert set(tf.io.gfile.listdir('gs://bucket/dir')) == {
        'file.txt',
        'subdir',
    }

    bs = 'big' + 'store'

    # Test
    # * gs
    # * absolute path
    # * relative path
    assert tf.io.gfile.glob('gs://bucket/*/file.txt') == [
        'gs://bucket/dir/file.txt',
    ]
    assert tf.io.gfile.glob(f'/{bs}/bucket/*/file.txt') == [
        f'/{bs}/bucket/dir/file.txt',
    ]
    assert tf.io.gfile.glob(f'{bs}/bucket/*/file.txt') == [
        f'{bs}/bucket/dir/file.txt',
    ]
