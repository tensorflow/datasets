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
from tensorflow_datasets.core.download import resource as resouce_lib


class _FakeResponse(object):

  def __init__(self, url, content, cookies=None, headers=None):
    self.url = url
    self.raw = io.BytesIO(content)
    self.cookies = cookies or {}
    self.headers = headers or {}

  def iter_content(self, chunk_size):
    del chunk_size
    for line in self.raw:
      yield line


class DownloaderTest(tf.test.TestCase):

  def setUp(self):
    self.addCleanup(tf.test.mock.patch.stopall)
    self.downloader = downloader.get_downloader(10, hashlib.sha256)
    self.tmp_dir = tempfile.mkdtemp(dir=tf.test.get_temp_dir())
    self.url = 'http://example.com/foo.tar.gz'
    self.resource = resouce_lib.Resource(url=self.url)
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
    promise = self.downloader.download(self.resource, self.tmp_dir)
    checksum, _ = promise.get()
    self.assertEqual(checksum, self.resp_checksum)
    with open(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.gfile.Exists(self.incomplete_path))

  def test_drive_no_cookies(self):
    resource = resouce_lib.Resource(
        url='https://drive.google.com/uc?export=download&id=a1b2bc3')
    promise = self.downloader.download(resource, self.tmp_dir)
    checksum, _ = promise.get()
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
    promise = self.downloader.download(self.resource, self.tmp_dir)
    with self.assertRaises(downloader.requests.exceptions.HTTPError):
      promise.get()


class GetFilenameTest(tf.test.TestCase):

  def test_no_headers(self):
    resp = _FakeResponse('http://foo.bar/baz.zip', b'content')
    res = downloader._get_filename(resp)
    self.assertEqual(res, 'baz.zip')

  def test_headers(self):
    cdisp = ('attachment;filename="hello.zip";'
             'filename*=UTF-8\'\'hello.zip')
    resp = _FakeResponse('http://foo.bar/baz.zip', b'content', headers={
        'content-disposition': cdisp,
    })
    res = downloader._get_filename(resp)
    self.assertEqual(res, 'hello.zip')

if __name__ == '__main__':
  tf.test.main()
