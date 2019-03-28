# coding=utf-8
# Copyright 2019 The TensorFlow Datasets Authors.
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

from absl.testing import absltest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core.download import downloader
from tensorflow_datasets.core.download import resource as resource_lib


class _FakeResponse(object):

  def __init__(self, url, content, cookies=None, headers=None, status_code=200):
    self.url = url
    self.raw = io.BytesIO(content)
    self.cookies = cookies or {}
    self.headers = headers or {'Content-length': 12345}
    self.status_code = status_code

  def iter_content(self, chunk_size):
    del chunk_size
    for line in self.raw:
      yield line


class DownloaderTest(testing.TestCase):

  def setUp(self):
    self.addCleanup(absltest.mock.patch.stopall)
    self.downloader = downloader.get_downloader(10, hashlib.sha256)
    self.tmp_dir = tempfile.mkdtemp(dir=tf.compat.v1.test.get_temp_dir())
    self.url = 'http://example.com/foo.tar.gz'
    self.resource = resource_lib.Resource(url=self.url)
    self.path = os.path.join(self.tmp_dir, 'foo.tar.gz')
    self.incomplete_path = '%s.incomplete' % self.path
    self.response = b'This \nis an \nawesome\n response!'
    self.resp_checksum = hashlib.sha256(self.response).hexdigest()
    self.cookies = {}
    absltest.mock.patch.object(
        downloader.requests.Session,
        'get',
        lambda *a, **kw: _FakeResponse(self.url, self.response, self.cookies),
    ).start()
    self.downloader._pbar_url = absltest.mock.MagicMock()
    self.downloader._pbar_dl_size = absltest.mock.MagicMock()

    def write_fake_ftp_result(_, filename):
      with open(filename, 'wb') as result:
        result.write(self.response)

    absltest.mock.patch.object(
        downloader.urllib.request,
        'urlretrieve',
        write_fake_ftp_result,
    ).start()

  def test_ok(self):
    promise = self.downloader.download(self.url, self.tmp_dir)
    checksum, _ = promise.get()
    self.assertEqual(checksum, self.resp_checksum)
    with open(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.io.gfile.exists(self.incomplete_path))

  def test_drive_no_cookies(self):
    url = 'https://drive.google.com/uc?export=download&id=a1b2bc3'
    promise = self.downloader.download(url, self.tmp_dir)
    checksum, _ = promise.get()
    self.assertEqual(checksum, self.resp_checksum)
    with open(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.io.gfile.exists(self.incomplete_path))

  def test_drive(self):
    self.cookies = {'foo': 'bar', 'download_warning_a': 'token', 'a': 'b'}
    self.test_drive_no_cookies()

  def test_http_error(self):
    error = downloader.requests.exceptions.HTTPError('Problem serving file.')
    absltest.mock.patch.object(
        downloader.requests.Session, 'get', side_effect=error).start()
    promise = self.downloader.download(self.url, self.tmp_dir)
    with self.assertRaises(downloader.requests.exceptions.HTTPError):
      promise.get()

  def test_bad_http_status(self):
    absltest.mock.patch.object(
        downloader.requests.Session,
        'get',
        lambda *a, **kw: _FakeResponse(self.url, b'error', status_code=404),
    ).start()
    promise = self.downloader.download(self.url, self.tmp_dir)
    with self.assertRaises(downloader.DownloadError):
      promise.get()

  def test_kaggle_api(self):
    fname = 'a.csv'
    with testing.mock_kaggle_api(filenames=[fname, 'b.txt']):
      promise = self.downloader.download('kaggle://some-competition/a.csv',
                                         self.tmp_dir)
      _, dl_size = promise.get()
      self.assertEqual(dl_size, len(fname))
      with tf.io.gfile.GFile(os.path.join(self.tmp_dir, fname)) as f:
        self.assertEqual(fname, f.read())

  def test_ftp(self):
    url = 'ftp://username:password@example.com/foo.tar.gz'
    promise = self.downloader.download(url, self.tmp_dir)
    checksum, _ = promise.get()
    self.assertEqual(checksum, self.resp_checksum)
    with open(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.io.gfile.exists(self.incomplete_path))

  def test_ftp_error(self):
    error = downloader.urllib.error.URLError('Problem serving file.')
    absltest.mock.patch.object(
        downloader.urllib.request,
        'urlretrieve',
        side_effect=error,
    ).start()
    url = 'ftp://example.com/foo.tar.gz'
    promise = self.downloader.download(url, self.tmp_dir)
    with self.assertRaises(downloader.urllib.error.URLError):
      promise.get()


class GetFilenameTest(testing.TestCase):

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
  testing.test_main()
