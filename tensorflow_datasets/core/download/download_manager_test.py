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
    self.file_names = {}  # resource fname -> original file name
    def list_directory(path):
      fname = os.path.basename(path).rsplit('.', 2)[0]  # suffix is '.tmp.$uuid'
      return [self.file_names.get(fname, 'file_with_no_ext')]
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
    self.gfile_patch = tf.test.mock.patch.object(
        tf, 'gfile',
        Exists=lambda path: path in self.existing_paths,
        MakeDirs=self.made_dirs.append,
        # Used to get name of file as downloaded:
        ListDirectory=list_directory,
        Open=open_,
        Rename=tf.test.mock.Mock(side_effect=rename),
        )
    self.gfile = self.gfile_patch.start()

  def tearDown(self):
    self.gfile_patch.stop()

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
    afname = resource_lib.Resource(url='http://a.ch/a').fname
    bfname = resource_lib.Resource(url='https://a.ch/b').fname
    cfname = resource_lib.Resource(url='https://a.ch/c').fname
    _ = [self._add_file(path) for path in [
        '/dl_dir/%s' % afname,
        '/dl_dir/%s.INFO' % afname,
        '/dl_dir/%s' % cfname,
    ]]
    downloaded_b, self.dl_results['https://a.ch/b'] = _get_promise_on_event(
        ('sha_b', 10))
    downloaded_c, self.dl_results['https://a.ch/c'] = _get_promise_on_event(
        ('sha_c', 10))
    manager = self._get_manager()
    res = manager.download(urls, async_=True)
    self.assertFalse(res.is_fulfilled)
    downloaded_b.set()
    downloaded_c.set()
    downloads = res.get()
    self.assertEqual(downloads, {
        'cached': '/dl_dir/%s' % afname,
        'new': '/dl_dir/%s' % bfname,
        'info_deleted': '/dl_dir/%s' % cfname,
    })

  def test_extract(self):
    """One file already extracted, one file with NO_EXTRACT, one to extract."""
    resource_cached = resource_lib.Resource(path='/dl_dir/cached',
                                            extract_method=ZIP)
    resource_new = resource_lib.Resource(path='/dl_dir/new', extract_method=TAR)
    resource_noextract = resource_lib.Resource(path='/dl_dir/noextract',
                                               extract_method=NO_EXTRACT)
    files = {
        'cached': resource_cached,
        'new': resource_new,
        'noextract': resource_noextract,
    }
    self.existing_paths.append('/extract_dir/ZIP.%s' % resource_cached.fname)
    extracted_new, self.extract_results['/dl_dir/%s' % resource_new.fname] = (
        _get_promise_on_event('/extract_dir/TAR.new'))
    manager = self._get_manager()
    res = manager.extract(files, async_=True)
    self.assertFalse(res.is_fulfilled)
    extracted_new.set()
    self.assertEqual(res.get(), {
        'cached': '/extract_dir/ZIP.%s' % resource_cached.fname,
        'new': '/extract_dir/TAR.%s' % resource_new.fname,
        'noextract': '/dl_dir/%s' % resource_noextract.fname,
    })

  def test_extract_twice_parallel(self):
    # Make sure calling extract twice on same resource actually does the
    # extraction once.
    extracted_new, self.extract_results['/dl_dir/foo.tar'] = (
        _get_promise_on_event('/extract_dir/TAR.foo'))
    manager = self._get_manager()
    res1 = manager.extract('/dl_dir/foo.tar', async_=True)
    res2 = manager.extract('/dl_dir/foo.tar', async_=True)
    self.assertTrue(res1 is res2)
    extracted_new.set()
    self.assertEqual(res1.get(), '/extract_dir/TAR.foo')
    self.assertEqual(1, self.extractor_extract.call_count)

  def test_download_and_extract(self):
    url_a = 'http://a/a.zip'
    url_b = 'http://b/b'
    sha_contenta = _sha256('content from a.zip')
    sha_contentb = _sha256('content from b')
    resource_a = resource_lib.Resource(url=url_a)
    resource_a.sha256 = sha_contenta
    resource_b = resource_lib.Resource(url=url_b)
    resource_b.sha256 = sha_contentb
    self.file_names[resource_a.fname] = 'a.zip'
    dl_a, self.dl_results[url_a] = _get_promise_on_event((sha_contenta, 10))
    dl_b, self.dl_results[url_b] = _get_promise_on_event((sha_contentb, 10))
    ext_a, self.extract_results['/dl_dir/%s' % resource_a.fname] = (
        _get_promise_on_event('/extract_dir/ZIP.%s' % resource_a.fname))
    # url_b doesn't need any extraction.
    for event in [dl_a, dl_b, ext_a]:
      event.set()
    manager = self._get_manager()
    manager._checksums[url_a] = sha_contenta
    manager._checksums[url_b] = sha_contentb
    res = manager.download_and_extract({'a': url_a, 'b': url_b})
    self.assertEqual(res, {
        'a': '/extract_dir/ZIP.%s' % resource_a.fname,
        'b': '/dl_dir/%s' % resource_b.fname})

  def test_download_and_extract_already_downloaded(self):
    url_a = 'http://a/a.zip'
    resource_a = resource_lib.Resource(url=url_a)
    self.file_names[resource_a.fname] = 'a.zip'
    # File was already downloaded:
    self._add_file('/dl_dir/%s' % resource_a.fname)
    self._write_info('/dl_dir/%s.INFO' % resource_a.fname,
                     {'original_fname': 'a.zip'})
    ext_a, self.extract_results['/dl_dir/%s' % resource_a.fname] = (
        _get_promise_on_event('/extract_dir/ZIP.%s' % resource_a.fname))
    ext_a.set()
    manager = self._get_manager()
    res = manager.download_and_extract(url_a)
    self.assertEqual(res, '/extract_dir/ZIP.%s' % resource_a.fname)

  def test_force_download_and_extract(self):
    url = 'http://a/b.tar.gz'
    resource_ = resource_lib.Resource(url=url)
    resource_.sha256 = _sha256('content of file')
    # resource was already downloaded / extracted:
    self.existing_paths = ['/dl_dir/%s' % resource_.fname,
                           '/extract_dir/TAR_GZ.%s' % resource_.fname]
    self.file_names[resource_.fname] = 'b.tar.gz'
    self._write_info('/dl_dir/%s.INFO' % resource_.fname,
                     {'original_fname': 'b.tar.gz'})
    dl_a, self.dl_results[url] = _get_promise_on_event((resource_.sha256, 10))
    ext_a, self.extract_results['/dl_dir/%s' % resource_.fname] = (
        _get_promise_on_event('/extract_dir/TAR_GZ.%s' % resource_.fname))
    dl_a.set()
    ext_a.set()
    manager = self._get_manager(force_download=True, force_extraction=True,
                                checksums={url: resource_.sha256})
    res = manager.download_and_extract(url)
    self.assertEqual('/extract_dir/TAR_GZ.%s' % resource_.fname, res)
    # Rename after download:
    (from_, to), kwargs = self.gfile.Rename.call_args
    self.assertTrue(re.match(
        r'/dl_dir/%s\.tmp\.[a-h0-9]{32}/b.tar.gz' % resource_.fname, from_))
    self.assertEqual('/dl_dir/%s' % resource_.fname, to)
    self.assertEqual(kwargs, {'overwrite': True})
    self.assertEqual(1, self.downloader_download.call_count)
    self.assertEqual(1, self.extractor_extract.call_count)

  def test_wrong_checksum(self):
    url = 'http://a/b.tar.gz'
    sha_a = _sha256('content a')
    sha_b = _sha256('content b')
    dl_a, self.dl_results[url] = _get_promise_on_event((sha_a, 10))
    dl_a.set()
    manager = self._get_manager(checksums={url: sha_b})
    with self.assertRaises(dm.NonMatchingChecksumError):
      manager.download(url)
    self.assertEqual(0, self.extractor_extract.call_count)


if __name__ == '__main__':
  tf.test.main()
