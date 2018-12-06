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

"""Tests for downloader."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import hashlib
import io
import os
import tempfile
import tensorflow as tf

from tensorflow_datasets.core.download import downloader
from tensorflow_datasets.core.proto import download_generated_pb2 as download_pb2


class _FakeResponse(object):

  def __init__(self, url, content, cookies):
    self.url = url
    self.raw = io.BytesIO(content)
    self.cookies = cookies

  def iter_content(self, chunk_size):
    del chunk_size
    for line in self.raw:
      yield line


class LocalDownloaderTest(tf.test.TestCase):

  def setUp(self):
    self.addCleanup(tf.test.mock.patch.stopall)
    self.downloader = downloader.get_downloader(10, hashlib.sha256)
    self.tmp_dir = tempfile.mkdtemp(dir=tf.test.get_temp_dir())
    self.url = 'http://example.com/foo.tar.gz'
    self.url_info = download_pb2.UrlInfo(url=self.url)
    self.path = os.path.join(self.tmp_dir, 'foo.tar.gz')
    self.incomplete_path = '%s.incomplete' % self.path
    self.response = b'This \nis an \nawesome\n response!'
    self.resp_checksum = hashlib.sha256(self.response).hexdigest()
    self.cookies = {}
    tf.test.mock.patch.object(
        downloader.requests.Session, 'get',
        lambda *a, **kw: _FakeResponse(self.url, self.response, self.cookies),
    ).start()

  def test_ok(self):
    promise = self.downloader.download(self.url_info, self.tmp_dir)
    checksum = promise.get()
    self.assertEqual(checksum, self.resp_checksum)
    with open(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.gfile.Exists(self.incomplete_path))

  def test_drive_no_cookies(self):
    url_info = download_pb2.UrlInfo(
        url='https://drive.google.com/uc?export=download&id=a1b2bc3')
    promise = self.downloader.download(url_info, self.tmp_dir)
    checksum = promise.get()
    self.assertEqual(checksum, self.resp_checksum)
    with open(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.gfile.Exists(self.incomplete_path))

  def test_drive(self):
    self.cookies = {'foo': 'bar', 'download_warning_a': 'token', 'a': 'b'}
    self.test_drive_no_cookies()

  def test_http_error(self):
    error = downloader.requests.exceptions.HTTPError('Problem serving file.')
    tf.test.mock.patch.object(
        downloader.requests.Session, 'get', side_effect=error).start()
    promise = self.downloader.download(self.url_info, self.tmp_dir)
    with self.assertRaises(downloader.requests.exceptions.HTTPError):
      promise.get()


if __name__ == '__main__':
  tf.test.main()
