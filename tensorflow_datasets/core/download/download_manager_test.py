# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
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

"""Tests for tensorflow_datasets.core.download.download_manager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import shutil
import tarfile
import time
import zipfile

import tensorflow as tf
from tensorflow import gfile
from tensorflow_datasets.core.download import download_manager
from tensorflow_datasets.core.download import util


class DownloadManagerBaseTest(tf.test.TestCase):

  def test_parallel_run(self):
    """Test the parallel_run function."""
    # _parallel_run should be like map, but execute things in parallel
    def process_fn(x):
      return x * 10

    result = download_manager._parallel_run(process_fn, {'a': 1, 'b': 2})
    self.assertEqual(result, {'a': 10, 'b': 20})

    result = download_manager._parallel_run(process_fn, [1, 2, 3])
    self.assertEqual(result, [10, 20, 30])

    result = download_manager._parallel_run(process_fn, 1)
    self.assertEqual(result, 10)

    timeouts = []
    def add_timeout(timeout):
      time.sleep(timeout)
      timeouts.append(timeout)
      return timeout * 10

    result = download_manager._parallel_run(
        add_timeout,
        [3, 2, 1, 0],
        max_workers=5,
    )
    # Results in same input order
    self.assertEqual(result, [30, 20, 10, 0])
    # But processed in revered order
    self.assertEqual(timeouts, [0, 1, 2, 3])

  def test_mode_reuse_cache(self):
    """Check that cache is reused in REUSE_CACHE_IF_EXISTS mode."""

    dl_manager_1 = download_manager.DownloadManager(
        cache_dir=tf.test.get_temp_dir(),
        mode=util.GenerateMode.REUSE_CACHE_IF_EXISTS,
    )
    dl_manager_2 = download_manager.DownloadManager(
        cache_dir=tf.test.get_temp_dir(),
        mode=util.GenerateMode.REUSE_CACHE_IF_EXISTS,
    )

    process_mock = tf.test.mock.Mock()
    key = '/unittest/test_mode_reuse_cache'

    # Execute the same processing twice
    output_dir_1 = dl_manager_1.execute_and_cache(process_mock, cache_key=key)
    output_dir_2 = dl_manager_2.execute_and_cache(process_mock, cache_key=key)

    # Results should be the same
    self.assertEqual(output_dir_1, output_dir_2)
    # The process function should have been called only once
    self.assertEqual(process_mock.call_count, 1)

  def test_mode_reuse_dataset(self):
    """Check that cache is reused in REUSE_DATASET_IF_EXISTS mode."""
    # REUSE_CACHE_IF_EXISTS and REUSE_DATASET_IF_EXISTS should act the same
    # way for the download

    dl_manager_1 = download_manager.DownloadManager(
        cache_dir=tf.test.get_temp_dir(),
        mode=util.GenerateMode.REUSE_DATASET_IF_EXISTS,
    )
    dl_manager_2 = download_manager.DownloadManager(
        cache_dir=tf.test.get_temp_dir(),
        mode=util.GenerateMode.REUSE_DATASET_IF_EXISTS,
    )

    process_mock = tf.test.mock.Mock()
    key = '/unittest/test_mode_reuse_dataset'

    # Execute the same processing twice
    output_dir_1 = dl_manager_1.execute_and_cache(process_mock, cache_key=key)
    output_dir_2 = dl_manager_2.execute_and_cache(process_mock, cache_key=key)

    # Results should be the same
    self.assertEqual(output_dir_1, output_dir_2)
    # The process function should have been called only once
    self.assertEqual(process_mock.call_count, 1)

  def test_mode_redownload(self):
    """Check that cache is NOT reused in FORCE_REDOWNLOAD mode."""

    dl_manager_1 = download_manager.DownloadManager(
        cache_dir=tf.test.get_temp_dir(),
        mode=util.GenerateMode.FORCE_REDOWNLOAD,
    )
    dl_manager_2 = download_manager.DownloadManager(
        cache_dir=tf.test.get_temp_dir(),
        mode=util.GenerateMode.FORCE_REDOWNLOAD,
    )

    process_mock = tf.test.mock.Mock()
    key = '/unittest/test_mode_redownload'

    # Execute the same processing twice
    dl_manager_1.execute_and_cache(process_mock, cache_key=key)
    dl_manager_2.execute_and_cache(process_mock, cache_key=key)

    # The process function should have been called twice
    self.assertEqual(process_mock.call_count, 2)


class DownloadManagerClassTest(tf.test.TestCase):

  @classmethod
  def setUpClass(cls):
    cache_dir = tf.test.get_temp_dir()

    # Create a dummy file
    dummy_dir = os.path.join(cache_dir, 'dummy')
    dummy_filepath = os.path.join(dummy_dir, 'dummy.txt')

    gfile.MakeDirs(dummy_dir)
    dummy_file_contents = 'hello world'
    with gfile.Open(dummy_filepath, 'w') as f:
      f.write(dummy_file_contents)

    # File containing compressed archives
    input_dir = os.path.join(cache_dir, 'to_extract')
    gfile.MakeDirs(input_dir)

    dl_manager = download_manager.DownloadManager(
        cache_dir=cache_dir,
        mode=util.GenerateMode.REUSE_CACHE_IF_EXISTS,
    )

    cls.dummy_dir = dummy_dir
    cls.dummy_filepath = dummy_filepath
    cls.dummy_file_contents = dummy_file_contents
    cls.input_dir = input_dir
    cls.dl_manager = dl_manager

  def _check_dir_contents(self, dirpath):
    with gfile.Open(os.path.join(dirpath, 'dummy.txt')) as f:
      self.assertEqual(self.dummy_file_contents, f.read().strip())

  @tf.test.mock.patch('six.moves.urllib.request.urlopen')
  def test_download(self, mock_urlopen):
    # Path urllib.request.urlopen to return some dummy message
    urlfile_mock = tf.test.mock.Mock()
    urlfile_mock.geturl.return_value = 'http://b.org/response.txt'
    urlfile_mock.read.return_value = 'Hello world'
    mock_urlopen.return_value = urlfile_mock

    with tf.test.mock.patch('six.moves.urllib.request.urlopen', mock_urlopen):
      output_file = self.dl_manager.download('https://a.org/query.txt')

    # Correct url called
    mock_urlopen.assert_called_with('https://a.org/query.txt')
    # Name correctly extracted
    self.assertEqual(os.path.basename(output_file), 'response.txt')
    # Content correctly fetched
    with gfile.Open(output_file, 'rb') as f:
      self.assertEqual(b'Hello world', f.read())

  def test_extract_zip(self):
    # Create zip
    zip_input = os.path.join(self.input_dir, 'foo.zip')
    with zipfile.ZipFile(zip_input, 'w') as zip_f:
      zip_f.write(self.dummy_filepath, arcname='dummy.txt')

    # Extract zip
    output_dir = self.dl_manager.extract(zip_input)
    self._check_dir_contents(output_dir)

  def test_extract_rar(self):
    # Create tar
    tar_input = os.path.join(self.input_dir, 'foo.tar')
    with tarfile.open(tar_input, 'w') as tar:
      tar.add(self.dummy_dir, arcname='foo')

    # Extract tar
    output_dir = self.dl_manager.extract(tar_input)
    self._check_dir_contents(os.path.join(output_dir, 'foo'))

  def test_extract_gzip(self):
    # Create gzip file
    gzip_input = os.path.join(self.input_dir, 'dummy.txt.gz')
    with gzip.open(gzip_input, 'wb') as gf:
      with gfile.Open(self.dummy_filepath, 'rb') as f:
        shutil.copyfileobj(f, gf)

    # Extract gzip
    output_path = self.dl_manager.extract(gzip_input)
    output_dir = os.path.dirname(output_path)
    self._check_dir_contents(output_dir)

  def test_execute_and_cache(self):

    def write_additional_data(cache_dir):
      with gfile.Open(os.path.join(cache_dir, 'dummy.txt'), 'w') as f:
        f.write('hello world')

    output_dir = self.dl_manager.execute_and_cache(
        write_additional_data, cache_key='/unittest/additional_data')
    self._check_dir_contents(output_dir)


if __name__ == '__main__':
  tf.test.main()
