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

import hashlib
import re
import threading

import promise
import tensorflow as tf
from tensorflow_datasets.core.download import download_manager as dm
from tensorflow_datasets.core.proto import download_generated_pb2 as download_pb2


def _get_promise_on_event(result=None, error=None):
  """Returns (event, Promise). Promise is fulfilled when `event.set()`."""
  event = threading.Event()
  def callback(resolve, reject):
    def inside():
      event.wait()
      if error is not None:
        reject(error)
      resolve(result)
    t = threading.Thread(target=inside)
    t.daemon = True
    t.start()
  return event, promise.Promise(callback)


def _sha256(str_):
  return hashlib.sha256(str_.encode('utf8')).hexdigest()


class GetExtractMethodTest(tf.test.TestCase):

  def test_(self):
    for method, path, expected_result in [
        (dm.AUTO_EXTRACT, 'path/to/bar.tar.gz', dm.TAR_GZ),
        (dm.AUTO_EXTRACT, 'path/to/bar.gz', dm.GZIP),
        (dm.AUTO_EXTRACT, 'path/to/bar.gz.strange', dm.NO_EXTRACT),
        (dm.NO_EXTRACT, 'path/to/bar.gz', dm.NO_EXTRACT),
        (dm.GZIP, 'path/to/bar.tar.gz', dm.GZIP),
    ]:
      res = dm._get_extract_method(download_pb2.ExtractInfo(
          path=path, extraction_method=method))
      self.assertEqual(res, expected_result, '(%s, %s)->%s instead of %s' % (
          method, path, res, expected_result))


class DownloadManagerTest(tf.test.TestCase):

  def setUp(self):
    self.addCleanup(tf.test.mock.patch.stopall)
    self.existing_paths = []
    self.made_dirs = []
    self.dl_results = {}
    self.extract_results = {}
    gfile = tf.test.mock.patch.object(
        tf, 'gfile',
        Exists=lambda path: path in self.existing_paths,
        MakeDirs=self.made_dirs.append,
        ListDirectory=lambda path: ['one_file'],
        )
    self.gfile = gfile.start()

  def _get_manager(self, force_download=False, force_extraction=False,
                   checksums=None):
    manager = dm.DownloadManager(
        'my_dataset', '/dl_dir', '/extract_dir', '/manual_dir',
        force_download=force_download, force_extraction=force_extraction,
        checksums=checksums)
    download = tf.test.mock.patch.object(
        manager._downloader, 'download',
        side_effect=lambda url_info, tmpdir_path: self.dl_results[url_info.url])
    self.downloader_download = download.start()
    extract = tf.test.mock.patch.object(
        manager._extractor, 'extract',
        side_effect=(
            lambda from_path, to_path, mtd: self.extract_results[from_path]))
    self.extractor_extract = extract.start()
    return manager

  def test_download(self):
    """One file in cache, one not."""
    urls = {
        'cached': download_pb2.UrlInfo(url='http://a.ch/a'),
        'new': download_pb2.UrlInfo(url='https://a.ch/b'),
    }
    urla_sha256 = _sha256('http://a.ch/a')
    urlb_sha256 = _sha256('https://a.ch/b')
    self.existing_paths.append('/dl_dir/url.%s' % urla_sha256)
    downloaded_b, self.dl_results['https://a.ch/b'] = _get_promise_on_event(
        'sha_b')
    manager = self._get_manager()
    res = manager.download(urls, async_=True)
    self.assertFalse(res.is_fulfilled)
    downloaded_b.set()
    downloads = res.get()
    self.assertEqual(downloads, {
        'cached': '/dl_dir/url.%s' % urla_sha256,
        'new': '/dl_dir/url.%s' % urlb_sha256,
    })

  def test_extract(self):
    """One file extracted, one file with NO_EXTRACT, one to extract."""
    files = {
        'cached': download_pb2.ExtractInfo(path='/dl_dir/a',
                                           extraction_method=dm.ZIP),
        'new': download_pb2.ExtractInfo(path='/dl_dir/b',
                                        extraction_method=dm.TAR),
    }
    self.existing_paths.append('/extract_dir/2.a')
    extracted_b, self.extract_results['/dl_dir/b'] = _get_promise_on_event()
    manager = self._get_manager()
    res = manager.extract(files, async_=True)
    self.assertFalse(res.is_fulfilled)
    extracted_b.set()
    self.assertEqual(res.get(), {
        'cached': '/extract_dir/2.a',
        'new': '/extract_dir/4.b',
    })

  def test_download_and_extract(self):
    urls = {'a': 'ftp://a/a',
            'b': 'ftp://b/b'}
    dl_a, self.dl_results['ftp://a/a'] = _get_promise_on_event('sha_a')
    dl_b, self.dl_results['ftp://b/b'] = _get_promise_on_event('sha_b')
    ext_a, self.extract_results['/dl_dir/a.12'] = _get_promise_on_event(
        '/extract_dir/a')
    ext_b, self.extract_results['/dl_dir/b.34'] = _get_promise_on_event(
        '/extract_dir/b')
    for event in [dl_a, dl_b, ext_a, ext_b]:
      event.set()
    manager = self._get_manager()
    res = manager.download_and_extract(urls)
    urla_sha256 = _sha256('ftp://a/a')
    urlb_sha256 = _sha256('ftp://b/b')
    self.assertEqual(res, {
        'a': '/dl_dir/url.%s' % urla_sha256,
        'b': '/dl_dir/url.%s' % urlb_sha256})

  def test_force_download_and_extract(self):
    url = 'http://a/b.tar.gz'
    self.existing_paths = ['/dl_dir/sha_a', '/extract_dir/5.sha_a']
    dl_a, self.dl_results[url] = _get_promise_on_event('sha_a')
    ext_a, self.extract_results['/dl_dir/sha_a'] = _get_promise_on_event()
    dl_a.set()
    ext_a.set()
    manager = self._get_manager(force_download=True, force_extraction=True,
                                checksums={url: 'sha_a'})
    res = manager.download_and_extract(url)
    self.assertEqual('/extract_dir/5.sha_a', res)
    # Rename after download:
    (from_, to), kwargs = self.gfile.Rename.call_args
    self.assertTrue(re.match('/dl_dir/tmp/[a-h0-9]{32}/one_file', from_))
    self.assertEqual('/dl_dir/sha_a', to)
    self.assertEqual(kwargs, {'overwrite': True})
    self.assertEqual(1, self.downloader_download.call_count)
    self.assertEqual(1, self.extractor_extract.call_count)

  def test_wrong_checksum(self):
    url = 'http://a/b.tar.gz'
    dl_a, self.dl_results[url] = _get_promise_on_event('sha_a')
    dl_a.set()
    manager = self._get_manager(checksums={url: 'sha_b'})
    with self.assertRaises(dm.NonMatchingChecksumError):
      manager.download(url)
    self.assertEqual(0, self.gfile.Rename.call_count)


if __name__ == '__main__':
  tf.test.main()
