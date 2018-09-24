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

"""Tests for tensorflow_datasets.core.download_manager."""

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
from tensorflow_datasets.core import download_manager
from tensorflow_datasets.core import test_utils


class DownloadManagerTest(tf.test.TestCase):

  def test_thread_parallelize(self):

    timeouts = []

    def make_fn(timeout):
      def add_val():
        time.sleep(timeout)
        timeouts.append(timeout)
      return add_val

    download_manager._thread_parallelize([make_fn(i) for i in range(10)], 5)
    self.assertEqual(list(range(10)), sorted(timeouts))

  def test_download(self):
    with test_utils.tmp_dir(self.get_temp_dir()) as tmp_dir:
      dm = download_manager.DownloadManager(tmp_dir)

      output_filenames = ["a", "b", "c"]
      urls = ["http://%s.com/foo" % fname for fname in output_filenames]

      retrieved = []

      def mock_urlretrieve(url, filepath):
        retrieved.append(url)
        with tf.gfile.Open(filepath, "w") as f:
          f.write(output_filenames[len(retrieved) - 1])

      with tf.test.mock.patch("six.moves.urllib.request.urlretrieve",
                              mock_urlretrieve):
        output_paths = dm.download(urls, output_filenames, num_threads=1)
        self.assertEqual(retrieved, urls)
        self.assertEqual(
            [os.path.join(tmp_dir, fname) for fname in output_filenames],
            output_paths)
        for fname, path in zip(output_filenames, output_paths):
          with tf.gfile.Open(path) as f:
            self.assertEqual(fname, f.read())


class DownloadManagerExtractTest(tf.test.TestCase):

  @classmethod
  def setUpClass(cls):
    tmp_dir = test_utils.make_tmp_dir(tf.test.get_temp_dir())
    inner_dir = os.path.join(tmp_dir, "foo")
    tf.gfile.MakeDirs(inner_dir)
    dummy_fname = os.path.join(inner_dir, "dummy.txt")
    file_contents = "hello world"
    with tf.gfile.Open(dummy_fname, "w") as f:
      f.write(file_contents)

    cls.tmp_dir = tmp_dir
    cls.inner_dir = inner_dir
    cls.dummy_fname = dummy_fname
    cls.file_contents = file_contents

  @classmethod
  def tearDownClass(cls):
    test_utils.rm_tmp_dir(cls.tmp_dir)

  def setUp(self):
    extraction_dir = os.path.join(self.tmp_dir, "extractions")
    self.dm = download_manager.DownloadManager(extraction_dir)

  def _check_file_contents(self, fname):
    with tf.gfile.Open(fname) as f:
      self.assertEqual(self.file_contents, f.read().strip())

  def test_gzip(self):
    # Create gzip file
    gzip_output = self.dummy_fname + ".gz"
    with gzip.open(gzip_output, "wb") as (
        gf), tf.gfile.Open(self.dummy_fname, "rb") as f:
      shutil.copyfileobj(f, gf)

    # Extract gzip
    check_gzip = self.dm.extract(gzip_output, "check_gzip")
    self._check_file_contents(check_gzip)

  def test_tar(self):
    # Create tar
    tar_output = os.path.join(self.tmp_dir, "foo.tar")
    with tarfile.open(tar_output, "w") as tar:
      tar.add(self.inner_dir, arcname="foo")

    # Extract tar
    check_tar = self.dm.extract(tar_output, "check_tar")
    self._check_file_contents(os.path.join(check_tar, "foo", "dummy.txt"))

  def test_zip(self):
    # Create zip
    zip_output = os.path.join(self.tmp_dir, "foo.zip")
    with zipfile.ZipFile(zip_output, "w") as zip_f:
      zip_f.write(self.dummy_fname, arcname="dummy.txt")

    # Extract zip
    check_zip = self.dm.extract(zip_output, "check_zip")
    self._check_file_contents(os.path.join(check_zip, "dummy.txt"))


if __name__ == "__main__":
  tf.test.main()
