# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

import sys

import tensorflow.compat.v2 as tf

from tensorflow_datasets.testing import test_case
from tensorflow_datasets.testing import test_utils

tf.enable_v2_behavior()


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
    self.assertEqual(set(l), {
        ('with_brackets', 'graph'),
        ('with_brackets', 'eager'),
        ('without_brackets', 'graph'),
        ('without_brackets', 'eager'),
    })

  def test_run_in_graph_and_eager_modes_setup_in_same_mode(self):
    modes = []
    mode_name = lambda: 'eager' if tf.executing_eagerly() else 'graph'

    class ExampleTest(test_case.TestCase):

      def runTest(self):
        pass

      def setUp(self):
        super(ExampleTest, self).setUp()
        modes.append('setup_' + mode_name())

      @test_utils.run_in_graph_and_eager_modes
      def testBody(self):
        modes.append('run_' + mode_name())

    e = ExampleTest()
    e.setUp()
    e.testBody()

    self.assertEqual(modes[0:2], ['setup_eager', 'run_eager'])
    self.assertEqual(modes[2:], ['setup_graph', 'run_graph'])

  def test_mock_fs(self):
    if sys.version_info.major < 3:  # Disable test on Python2
      return

    fs = test_utils.MockFs()
    with fs.mock():
      fs.add_file('/path/to/file1', 'Content of file 1')
      fs.add_file('/path/file.txt', 'Content of file.txt')

      # Test `tf.io.gfile.exists`
      self.assertTrue(tf.io.gfile.exists('/path/to/file1'))
      self.assertFalse(tf.io.gfile.exists('/path/to/file1_nonexisting'))

      # Test `tf.io.gfile.GFile` (write and read mode)
      with tf.io.gfile.GFile('/path/to/file2', 'w') as f:
        f.write('Content of file 2 (old)')
      self.assertEqual(fs.files['/path/to/file2'], 'Content of file 2 (old)')
      with tf.io.gfile.GFile('/path/to/file2', 'w') as f:
        f.write('Content of file 2 (new)')
      self.assertEqual(fs.files['/path/to/file2'], 'Content of file 2 (new)')
      with tf.io.gfile.GFile('/path/to/file2', 'r') as f:
        self.assertEqual(f.read(), 'Content of file 2 (new)')

      # Test `tf.io.gfile.rename`
      self.assertEqual(fs.files['/path/to/file1'], 'Content of file 1')
      tf.io.gfile.rename('/path/to/file1', '/path/to/file1_moved')
      self.assertNotIn('/path/to/file1', fs.files)
      self.assertEqual(fs.files['/path/to/file1_moved'], 'Content of file 1')

      # Test `tf.io.gfile.listdir`
      self.assertCountEqual(
          tf.io.gfile.listdir('/path/to'), tf.io.gfile.listdir('/path/to/'))
      self.assertCountEqual(
          tf.io.gfile.listdir('/path/to'), ['file1_moved', 'file2'])
      self.assertCountEqual(tf.io.gfile.listdir('/path'), ['file.txt', 'to'])

      # Test `MockFs.files`
      self.assertEqual(fs.files, {
          '/path/to/file2': 'Content of file 2 (new)',
          '/path/to/file1_moved': 'Content of file 1',
          '/path/file.txt': 'Content of file.txt',
      })

if __name__ == '__main__':
  test_utils.test_main()
