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

"""Tests for downloader."""

import hashlib
import io
import os
import tempfile
from typing import Optional
from unittest import mock

import pytest
import tensorflow as tf
from tensorflow_datasets import testing
from tensorflow_datasets.core.download import downloader
from tensorflow_datasets.core.download import resource as resource_lib
from tensorflow_datasets.core.download import util


class _FakeResponse(object):

  def __init__(self, url, content, cookies=None, headers=None, status_code=200):
    self.url = url
    self.raw = io.BytesIO(content)
    self.cookies = cookies or {}
    self.headers = headers or {'Content-length': 12345}
    self.status_code = status_code
    # For urllib codepath
    self.read = self.raw.read

  def __enter__(self):
    return self

  def __exit__(self, *args):
    return

  def iter_content(self, chunk_size):
    del chunk_size
    for line in self.raw:
      yield line


class DownloaderTest(testing.TestCase):

  def setUp(self):
    super(DownloaderTest, self).setUp()
    self.addCleanup(mock.patch.stopall)
    self.downloader = downloader.get_downloader(10, hashlib.sha256)
    self.tmp_dir = tempfile.mkdtemp(dir=tf.compat.v1.test.get_temp_dir())
    self.url = 'http://example.com/foo.tar.gz'
    self.resource = resource_lib.Resource(url=self.url)
    self.path = os.path.join(self.tmp_dir, 'foo.tar.gz')
    self.incomplete_path = '%s.incomplete' % self.path
    self.response = b'This \nis an \nawesome\n response!'
    self.resp_checksum = hashlib.sha256(self.response).hexdigest()
    self.cookies = {}
    mock.patch.object(
        downloader.requests.Session,
        'get',
        lambda *a, **kw: _FakeResponse(self.url, self.response, self.cookies),
    ).start()
    self.downloader._pbar_url = mock.MagicMock()
    self.downloader._pbar_dl_size = mock.MagicMock()
    mock.patch.object(
        downloader.urllib.request,
        'urlopen',
        lambda *a, **kw: _FakeResponse(self.url, self.response, self.cookies),
    ).start()

  def test_ok(self):
    promise = self.downloader.download(self.url, self.tmp_dir)
    future = promise.get()
    url_info = future.url_info
    self.assertEqual(self.path, os.fspath(future.path))
    self.assertEqual(url_info.checksum, self.resp_checksum)
    with tf.io.gfile.GFile(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.io.gfile.exists(self.incomplete_path))

  def test_drive_no_cookies(self):
    url = 'https://drive.google.com/uc?export=download&id=a1b2bc3'
    promise = self.downloader.download(url, self.tmp_dir)
    future = promise.get()
    url_info = future.url_info
    self.assertEqual(self.path, os.fspath(future.path))
    self.assertEqual(url_info.checksum, self.resp_checksum)
    with tf.io.gfile.GFile(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.io.gfile.exists(self.incomplete_path))

  def test_drive(self):
    self.cookies = {'foo': 'bar', 'download_warning_a': 'token', 'a': 'b'}
    self.test_drive_no_cookies()

  def test_http_error(self):
    error = downloader.requests.exceptions.HTTPError('Problem serving file.')
    mock.patch.object(
        downloader.requests.Session, 'get', side_effect=error
    ).start()
    promise = self.downloader.download(self.url, self.tmp_dir)
    with self.assertRaises(downloader.requests.exceptions.HTTPError):
      promise.get()

  def test_bad_http_status(self):
    mock.patch.object(
        downloader.requests.Session,
        'get',
        lambda *a, **kw: _FakeResponse(self.url, b'error', status_code=404),
    ).start()
    promise = self.downloader.download(self.url, self.tmp_dir)
    with self.assertRaises(util.DownloadError):
      promise.get()

  def test_ftp(self):
    url = 'ftp://username:password@example.com/foo.tar.gz'
    promise = self.downloader.download(url, self.tmp_dir)
    future = promise.get()
    url_info = future.url_info
    self.assertEqual(self.path, os.fspath(future.path))
    self.assertEqual(url_info.checksum, self.resp_checksum)
    with tf.io.gfile.GFile(self.path, 'rb') as result:
      self.assertEqual(result.read(), self.response)
    self.assertFalse(tf.io.gfile.exists(self.incomplete_path))

  def test_ftp_error(self):
    error = downloader.urllib.error.URLError('Problem serving file.')
    mock.patch.object(
        downloader.urllib.request,
        'urlopen',
        side_effect=error,
    ).start()
    url = 'ftp://example.com/foo.tar.gz'
    promise = self.downloader.download(url, self.tmp_dir)
    with self.assertRaises(downloader.urllib.error.URLError):
      promise.get()


# Gramar examples inspired from: https://tools.ietf.org/html/rfc6266#section-5
_CONTENT_DISPOSITION_FILENAME_PAIRS = [
    ("""attachment; filename=filename.txt""", 'filename.txt'),
    # Should strip space
    ("""attachment; filename=  filename.txt  """, 'filename.txt'),
    ("""attachment; filename=  filename.txt  ;""", 'filename.txt'),
    # If both encoded and ascii are present, only keep encoded
    (
        """attachment; filename="EURO rates"; filename*=utf-8''%e2%82%ac%20rates""",
        'EURO rates',
    ),
    (
        """attachment; filename=EURO rates; filename*=utf-8''%e2%82%ac%20rates""",
        'EURO rates',
    ),
    (
        """attachment; filename=EXAMPLE-Im ößä.dat; filename*=iso-8859-1''EXAMPLE-%20I%27m%20%F6%DF%E4.dat""",
        'EXAMPLE-Im ößä.dat',
    ),
    (
        """attachment;filename="hello.zip";filename*=UTF-8''hello.zip""",
        'hello.zip',
    ),
    (
        """attachment;filename=hello.zip;filename*=UTF-8''hello.zip""",
        'hello.zip',
    ),
    # Should be case insensitive
    ("""INLINE; FILENAME= "an example.html""", 'an example.html'),
    ("""Attachment; filename=example.html""", 'example.html'),
    # Only encoded not supported for now
    ("""attachment; filename*=UTF-8''filename.txt""", None),
    ("""attachment; filename*=iso-8859-1'en'%A3%20rates""", None),
    # Multi-line also supported
    (
        """attachment;
            filename="hello.zip";
            filename*=UTF-8''hello.zip""",
        'hello.zip',
    ),
    ("""attachment;filename*=UTF-8''hello.zip""", None),
    (
        """attachment;
            filename*= UTF-8''%e2%82%ac%20rates.zip""",
        None,
    ),
    # Give only file base name when directory path is given
    (
        'inline;filename=path/to/dir/f-name.png;filename*=UTF-8',
        'f-name.png',
    ),
]


@pytest.mark.parametrize(
    ('content_disposition', 'filename'), _CONTENT_DISPOSITION_FILENAME_PAIRS
)
def test_filename_from_content_disposition(
    content_disposition: str,
    filename: Optional[str],
):
  get_filename = downloader._filename_from_content_disposition
  assert get_filename(content_disposition) == filename


@pytest.mark.parametrize(
    ('content_disposition', 'filename'),
    [
        (
            # Filename should be parsed from the ascii name, not UTF-8
            """attachment;filename="hello.zip";filename*=UTF-8''other.zip""",
            'hello.zip',
        ),
        (
            # If ascii filename can't be parsed, filename parsed from url
            """attachment;filename*=UTF-8''other.zip""",
            'baz.zip',
        ),
        (
            # No headers, filename parsed from url
            None,
            'baz.zip',
        ),
    ],
)
def test_filename_from_headers(
    content_disposition: Optional[str],
    filename: Optional[str],
):
  if content_disposition:
    headers = {
        'content-disposition': content_disposition,
    }
  else:
    headers = None
  resp = _FakeResponse('http://foo.bar/baz.zip', b'content', headers=headers)
  assert downloader._get_filename(resp), filename
