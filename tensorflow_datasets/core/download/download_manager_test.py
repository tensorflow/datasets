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
import json
import os
import re
import tempfile
import threading

import promise
import tensorflow as tf
from tensorflow_datasets.core.download import download_manager as dm
from tensorflow_datasets.core.download import resource as resource_lib


ZIP = resource_lib.ExtractMethod.ZIP
TAR = resource_lib.ExtractMethod.TAR
NO_EXTRACT = resource_lib.ExtractMethod.NO_EXTRACT


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


class DownloadManagerTest(tf.test.TestCase):

  def _add_file(self, path, content='', mode='w'):
    """Returns open file handle."""
    temp_f = tempfile.NamedTemporaryFile(mode=mode, delete=False)
    self.files_content[path] = temp_f.name
    temp_f.write(content)
    temp_f.close()
    self.existing_paths.append(path)
    return temp_f

  def setUp(self):
    self.addCleanup(tf.test.mock.patch.stopall)
    self.existing_paths = []
    self.made_dirs = []
    self.dl_results = {}
    self.extract_results = {}
    self.file_names = {}  # url_sha -> original file name
    def list_directory(path):
      sha = os.path.basename(path).split('.')[0]
      return [self.file_names.get(sha, 'file_with_no_ext')]
    self.files_content = {}
    def open_(path, mode='r'):
      if 'w' in mode:
        self._add_file(path)
      return open(self.files_content[path], mode)
    def rename(from_, to, overwrite=False):
      del overwrite
      if from_ in self.files_content:
        self.existing_paths.append(to)
        self.existing_paths.remove(from_)
        self.files_content[to] = self.files_content.pop(from_)
    gfile = tf.test.mock.patch.object(
        tf, 'gfile',
        Exists=lambda path: path in self.existing_paths,
        MakeDirs=self.made_dirs.append,
        # Used to get name of file as downloaded:
        ListDirectory=list_directory,
        Open=open_,
        Rename=tf.test.mock.Mock(side_effect=rename),
        )
    self.gfile = gfile.start()

  def _write_info(self, path, info):
    content = json.dumps(info, sort_keys=True)
    self._add_file(path, content)

  def _get_manager(self, force_download=False, force_extraction=False,
                   checksums=None):
    manager = dm.DownloadManager(
        'my_dataset', '/dl_dir', '/extract_dir', '/manual_dir',
        force_download=force_download, force_extraction=force_extraction,
        checksums=checksums)
    download = tf.test.mock.patch.object(
        manager._downloader, 'download',
        side_effect=lambda resource, tmpdir_path: self.dl_results[resource.url])
    self.downloader_download = download.start()
    extract = tf.test.mock.patch.object(
        manager._extractor, 'extract',
        side_effect=lambda resource, dest: self.extract_results[resource.path])
    self.extractor_extract = extract.start()
    return manager

  def test_download(self):
    """One file in cache, one not."""
    urls = {
        'cached': resource_lib.Resource(url='http://a.ch/a'),
        'new': resource_lib.Resource(url='https://a.ch/b'),
        # INFO file of c has been deleted:
        'info_deleted': resource_lib.Resource(url='https://a.ch/c'),
    }
    urla_sha256 = _sha256('http://a.ch/a')
    urlb_sha256 = _sha256('https://a.ch/b')
    urlc_sha256 = _sha256('https://a.ch/c')
    self.existing_paths.extend([
        '/dl_dir/%s' % urla_sha256,
        '/dl_dir/%s.INFO' % urla_sha256,
        '/dl_dir/%s' % urlc_sha256,
    ])
    downloaded_b, self.dl_results['https://a.ch/b'] = _get_promise_on_event(
        'sha_b')
    downloaded_c, self.dl_results['https://a.ch/c'] = _get_promise_on_event(
        'sha_c')
    manager = self._get_manager()
    res = manager.download(urls, async_=True)
    self.assertFalse(res.is_fulfilled)
    downloaded_b.set()
    downloaded_c.set()
    downloads = res.get()
    self.assertEqual(downloads, {
        'cached': '/dl_dir/%s' % urla_sha256,
        'new': '/dl_dir/%s' % urlb_sha256,
        'info_deleted': '/dl_dir/%s' % urlc_sha256,
    })

  def test_extract(self):
    """One file already extracted, one file with NO_EXTRACT, one to extract."""
    files = {
        'cached': resource_lib.Resource(path='/dl_dir/cached',
                                        extract_method=ZIP),
        'new': resource_lib.Resource(path='/dl_dir/new', extract_method=TAR),
        'noextract': resource_lib.Resource(path='/dl_dir/noextract',
                                           extract_method=NO_EXTRACT),
    }
    self.existing_paths.append('/extract_dir/ZIP.cached')
    extracted_new, self.extract_results['/dl_dir/new'] = _get_promise_on_event(
        '/extract_dir/TAR.new')
    manager = self._get_manager()
    res = manager.extract(files, async_=True)
    self.assertFalse(res.is_fulfilled)
    extracted_new.set()
    self.assertEqual(res.get(), {
        'cached': '/extract_dir/ZIP.cached',
        'new': '/extract_dir/TAR.new',
        'noextract': '/dl_dir/noextract',
    })

  def test_download_and_extract(self):
    url_a = 'http://a/a.zip'
    url_b = 'http://b/b'
    url_a_sha = _sha256(url_a)
    url_b_sha = _sha256(url_b)
    self.file_names[url_a_sha] = 'a.zip'
    dl_a, self.dl_results[url_a] = _get_promise_on_event('sha_a')
    dl_b, self.dl_results[url_b] = _get_promise_on_event('sha_b')
    ext_a, self.extract_results['/dl_dir/%s' % url_a_sha] = (
        _get_promise_on_event('/extract_dir/ZIP.%s' % url_a_sha))
    # url_b doesn't need any extraction.
    for event in [dl_a, dl_b, ext_a]:
      event.set()
    manager = self._get_manager()
    res = manager.download_and_extract({'a': url_a, 'b': url_b})
    self.assertEqual(res, {
        'a': '/extract_dir/ZIP.%s' % url_a_sha,
        'b': '/dl_dir/%s' % url_b_sha})

  def test_download_and_extract_already_downloaded(self):
    url_a = 'http://a/a.zip'
    url_a_sha = _sha256(url_a)
    self.file_names[url_a_sha] = 'a.zip'
    # File was already downloaded:
    self.existing_paths.append('/dl_dir/%s' % url_a_sha)
    self._write_info('/dl_dir/%s.INFO' % url_a_sha, {'original_fname': 'a.zip'})
    ext_a, self.extract_results['/dl_dir/%s' % url_a_sha] = (
        _get_promise_on_event('/extract_dir/ZIP.%s' % url_a_sha))
    ext_a.set()
    manager = self._get_manager()
    res = manager.download_and_extract(url_a)
    self.assertEqual(res, '/extract_dir/ZIP.%s' % url_a_sha)

  def test_force_download_and_extract(self):
    url = 'http://a/b.tar.gz'
    url_sha = _sha256(url)
    # resource was already downloaded / extracted:
    self.existing_paths = ['/dl_dir/%s' % url_sha,
                           '/extract_dir/TAR_GZ.%s' % url_sha]
    self.file_names[url_sha] = 'b.tar.gz'
    self._write_info('/dl_dir/%s.INFO' % url_sha,
                     {'original_fname': 'b.tar.gz'})
    dl_a, self.dl_results[url] = _get_promise_on_event('sha_a')
    ext_a, self.extract_results['/dl_dir/%s' % url_sha] = (
        _get_promise_on_event('/extract_dir/TAR_GZ.%s' % url_sha))
    dl_a.set()
    ext_a.set()
    manager = self._get_manager(force_download=True, force_extraction=True,
                                checksums={url: 'sha_a'})
    res = manager.download_and_extract(url)
    self.assertEqual('/extract_dir/TAR_GZ.%s' % url_sha, res)
    # Rename after download:
    (from_, to), kwargs = self.gfile.Rename.call_args
    self.assertTrue(re.match(
        r'/dl_dir/%s\.tmp\.[a-h0-9]{32}/b.tar.gz' % url_sha, from_))
    self.assertEqual('/dl_dir/%s' % url_sha, to)
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
    self.assertEqual(0, self.extractor_extract.call_count)


if __name__ == '__main__':
  tf.test.main()
