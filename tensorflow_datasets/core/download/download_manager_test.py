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

"""Tests for tensorflow_datasets.core.download.download_manager."""

import collections
import hashlib
import json
import os
import pickle

from absl.testing import absltest
import promise

import tensorflow as tf

from tensorflow_datasets import testing
from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import checksums as checksums_lib
from tensorflow_datasets.core.download import download_manager as dm
from tensorflow_datasets.core.download import downloader
from tensorflow_datasets.core.download import extractor
from tensorflow_datasets.core.download import resource as resource_lib


ZIP = resource_lib.ExtractMethod.ZIP
TAR = resource_lib.ExtractMethod.TAR
NO_EXTRACT = resource_lib.ExtractMethod.NO_EXTRACT


def _sha256(str_):
  return hashlib.sha256(str_.encode('utf8')).hexdigest()


def _as_path(nested_paths):
  return tf.nest.map_structure(utils.as_path, nested_paths)


def _info_path(path):
  return path.with_name(f'{path.name}.INFO')


class PathDict(collections.UserDict):
  """Like `dict` but normalize path-like objects.

  It means `d[Path('/path/')]` and `d['/path/']` are equivalent.

  """

  def __getitem__(self, key):
    return super().__getitem__(os.fspath(key))

  def __setitem__(self, key, value):
    return super().__setitem__(os.fspath(key), utils.as_path(value))


class Artifact(object):
  # For testing only.

  def __init__(self, name, url=None):
    url = url or f'http://foo-bar.ch/{name}'
    content = f'content of {name}'
    self.url = url
    self.url_info = checksums_lib.UrlInfo(
        size=len(content),
        checksum=_sha256(content),
        filename=name,
    )
    self.file_name = resource_lib.get_dl_fname(url, self.url_info.checksum)
    self.file_path = utils.as_path(f'/dl_dir/{self.file_name}')
    self.url_name = resource_lib.get_dl_fname(url, _sha256(url))
    self.url_path = utils.as_path(f'/dl_dir/{self.url_name}')


class DownloadManagerTest(testing.TestCase):
  """Download manager test.

  During tests, the `tf.io.gfile` API is mocked. Instead, files I/O are tracked
  through `fs` (`tfds.testing.MockFs`).

  The downloader/extrator results are mocked with:

    dl_results: Dict[str, UrlInfo], mapping `url` -> `downloader.download(url)`
    dl_fnames: Dict[str, str], mapping `url` -> `filename`, if the name
      cannot be extracted from the url (e.g. `https://a.org/download?id=123`)
    extract_results: Dict[str, str], mapping `path` -> `extractor.extract()`

  To check whether url/path are actually downloaded vs cached reused:

    downloaded_urls: Track calls of `downloader.download`
    extracted_paths: Track calls of `extractor.extract`
  """

  # ----- Downloader/Extractor patch -----

  def _make_downloader_mock(self):
    """`downloader.download` patch which creates the returns the path."""

    def _download(url, tmpdir_path, verify):
      del verify
      self.downloaded_urls.append(url)  # Record downloader.download() calls
      # If the name isn't explicitly provided, then it is extracted from the
      # url.
      filename = self.dl_fnames.get(url, os.path.basename(url))
      # Save the file in the tmp_dir
      self.fs.add_file(os.path.join(tmpdir_path, filename))
      return promise.Promise.resolve(self.dl_results[url])

    return absltest.mock.patch.object(
        downloader._Downloader, 'download', side_effect=_download)

  def _make_extractor_mock(self):
    """`extractor.extract` patch which creates the returns the path."""

    def _extract(path, method, dest):
      self.extracted_paths.append(path)  # Record downloader.download() calls
      self.fs.add_file(dest, f'Extracted dir from {path}')
      if not os.path.basename(dest).startswith(method.name):
        raise ValueError(
            f'Destination {dest} do not match extraction method {method}')
      return promise.Promise.resolve(self.extract_results[path])

    return absltest.mock.patch.object(
        extractor._Extractor, 'extract', side_effect=_extract).start()

  def setUp(self):
    super().setUp()

    # Input of the DownloadManager
    self.dl_results = {}
    self.dl_fnames = {}
    self.extract_results = PathDict()

    # Track calls to downloader/extractor
    self.downloaded_urls = []
    self.extracted_paths = []

    # Virtual file system
    self.fs = testing.MockFs()  # Dict file_path -> file_content

    # Start all mocks
    self.fs.__enter__()
    self._make_downloader_mock().start()
    self._make_extractor_mock().start()

    self.addCleanup(absltest.mock.patch.stopall)

  def tearDown(self):
    super().tearDown()
    self.fs.__exit__(None, None, None)

  def assertContainFiles(self, filepaths):
    self.assertCountEqual(_as_path(list(self.fs.files)), _as_path(filepaths))

  def _write_info(self, path, info):
    content = json.dumps(info)
    self.fs.add_file(path, content)

  def _get_manager(
      self,
      register_checksums=True,
      url_infos=None,
      dl_dir='/dl_dir',
      extract_dir='/extract_dir',
      **kwargs
  ):
    manager = dm.DownloadManager(
        dataset_name='mnist',
        download_dir=dl_dir,
        extract_dir=extract_dir,
        manual_dir='/manual_dir',
        register_checksums=register_checksums,
        register_checksums_path='/checksums/checksums.tsv',
        **kwargs
    )
    if url_infos:
      manager._url_infos = url_infos
    return manager

  def test_download(self):
    """One file in cache, one not."""
    a, b, c = [Artifact(i) for i in 'abc']
    # File `a` is cached
    self.fs.add_file(a.file_path)
    self.fs.add_file(_info_path(a.file_path))
    # INFO file of c has been deleted:
    self.fs.add_file(c.file_path)

    # A url is cached, so not downloaded.
    self.dl_results[b.url] = b.url_info
    self.dl_results[c.url] = c.url_info
    manager = self._get_manager(url_infos={
        art.url: art.url_info for art in (a, b, c)
    })
    downloads = manager.download({
        'cached': a.url,
        'new': b.url,
        'info_deleted': c.url,
    })
    expected = {
        'cached': a.file_path,
        'new': b.file_path,
        'info_deleted': c.file_path,
    }
    self.assertEqual(downloads, expected)
    # A isn't downloaded as already cached
    # C is re-downloaded as incomplete
    self.assertCountEqual(self.downloaded_urls, {b.url, c.url})
    self.assertEqual(  # Downloaded size include cached downloads
        manager.downloaded_size, sum([art.url_info.size for art in (a, b, c)]))

  def test_manually_downloaded(self):
    """One file is manually downloaded, one not."""
    a, b = [Artifact(i) for i in 'ab']

    a_file_path = '/manual_dir/a'
    # File a is manually downloaded
    self.fs.add_file(a_file_path)
    self.fs.add_file(b.file_path)

    self.dl_results[b.url] = b.url_info
    manager = self._get_manager(
        url_infos={
            art.url: art.url_info for art in (a, b)
        },
    )
    downloads = manager.download({
        'manual': a.url,
        'download': b.url,
    })
    expected = {
        'manual': utils.as_path(a_file_path),
        'download': b.file_path,
    }
    self.assertEqual(downloads, expected)

  def test_extract(self):
    """One file already extracted, one file with NO_EXTRACT, one to extract."""
    cached = resource_lib.Resource(path='/dl_dir/cached', extract_method=ZIP)
    new_ = resource_lib.Resource(path='/dl_dir/new', extract_method=TAR)
    no_extract = resource_lib.Resource(path='/dl_dir/noextract',
                                       extract_method=NO_EXTRACT)
    self.fs.add_file('/extract_dir/ZIP.cached')
    self.extract_results['/dl_dir/new'] = '/extract_dir/TAR.new'
    manager = self._get_manager()
    res = manager.extract({
        'cached': cached,
        'new': new_,
        'noextract': no_extract,
    })
    expected = _as_path({
        'cached': '/extract_dir/ZIP.cached',
        'new': '/extract_dir/TAR.new',
        'noextract': '/dl_dir/noextract',
    })
    self.assertEqual(res, expected)
    self.assertCountEqual(self.extracted_paths, [_as_path('/dl_dir/new')])

  def test_extract_twice_parallel(self):
    # Make sure calling extract twice on same resource actually does the
    # extraction once.
    self.extract_results['/dl_dir/foo.tar'] = '/extract_dir/TAR.foo'
    manager = self._get_manager()
    out1 = manager.extract(['/dl_dir/foo.tar', '/dl_dir/foo.tar'])
    out2 = manager.extract('/dl_dir/foo.tar')
    self.assertEqual(
        out1, _as_path(['/extract_dir/TAR.foo', '/extract_dir/TAR.foo'])
    )
    self.assertEqual(out2, _as_path('/extract_dir/TAR.foo'))
    # Result is memoize so extract has only been called once
    self.assertCountEqual(self.extracted_paths, [_as_path('/dl_dir/foo.tar')])

  def test_download_and_extract(self):
    a, b = Artifact('a.zip'), Artifact('b')
    self.dl_results[a.url] = a.url_info
    self.dl_results[b.url] = b.url_info
    self.extract_results[a.file_path] = f'/extract_dir/ZIP.{a.file_name}'
    # url_b doesn't need any extraction.

    # Result is the same after caching:
    manager = self._get_manager(url_infos={
        a.url: a.url_info,
        b.url: b.url_info,
    })
    res = manager.download_and_extract({'a': a.url, 'b': b.url})
    self.assertEqual(res, {
        'a': _as_path('/extract_dir/ZIP.%s' % a.file_name),
        'b': b.file_path,
    })

  def test_download_and_extract_archive_ext_in_fname(self):
    # Make sure extraction method is properly deduced from original fname, and
    # not from URL.
    a = Artifact('a', url='http://a?key=1234')
    self.dl_results[a.url] = a.url_info
    self.dl_fnames[a.url] = 'abc.zip'
    self.extract_results[a.file_path] = f'/extract_dir/ZIP.{a.file_name}'

    manager = self._get_manager(url_infos={
        a.url: a.url_info,
    })
    res = manager.download_and_extract({'a': a.url})
    self.assertEqual(res, _as_path({
        'a': '/extract_dir/ZIP.%s' % a.file_name,
    }))

  def test_download_and_extract_already_downloaded(self):
    a = Artifact('a')  # Extract can't be deduced from the url, but from .INFO
    # File was already downloaded:
    self.fs.add_file(a.file_path)
    self._write_info(_info_path(a.file_path), {'original_fname': 'a.zip'})
    self.extract_results[a.file_path] = f'/extract_dir/ZIP.{a.file_name}'
    manager = self._get_manager(url_infos={
        a.url: a.url_info,
    })
    res = manager.download_and_extract(a.url)
    self.assertEqual(res, _as_path(f'/extract_dir/ZIP.{a.file_name}'))
    # No url downloaded, but file extracted.
    self.assertCountEqual(self.downloaded_urls, [])
    self.assertCountEqual(self.extracted_paths, [a.file_path])

  def test_force_download_and_extract(self):
    a = Artifact('a.tar.gz')
    self.dl_results[a.url] = a.url_info
    self.extract_results[a.file_path] = f'/extract_dir/TAR_GZ.{a.file_name}'

    # Old content already exists
    self.fs.add_file(a.file_path, content='old content')
    self.fs.add_file(_info_path(a.file_path), content='old content')

    # Redownloading the data overwrite the content
    manager = self._get_manager(
        force_download=True,
        force_extraction=True,
        url_infos={
            a.url: a.url_info,
        })
    res = manager.download_and_extract(a.url)
    self.assertEqual(res, _as_path(f'/extract_dir/TAR_GZ.{a.file_name}'))

    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertCountEqual(self.extracted_paths, [a.file_path])
    self.assertNotEqual(a.file_path, 'old content')
    self.assertNotEqual(_info_path(a.file_path), '{}')
    self.assertNotEqual(f'/extract_dir/TAR_GZ.{a.file_name}', 'old content')

  def test_wrong_checksum(self):
    a = Artifact('a.tar.gz')
    sha_b = _sha256('content of another file')
    self.dl_results[a.url] = a.url_info
    manager = self._get_manager(
        register_checksums=False,
        url_infos={
            a.url: checksums_lib.UrlInfo(
                size=a.url_info.size,
                checksum=sha_b,
                filename=a.url_info.filename,
            ),
        },
    )
    with self.assertRaises(dm.NonMatchingChecksumError):
      manager.download(a.url)

  def test_pickle(self):
    dl_manager = self._get_manager(register_checksums=False)
    pickle.loads(pickle.dumps(dl_manager))

    dl_manager = self._get_manager(register_checksums=True)
    with self.assertRaisesRegex(
        NotImplementedError, '`register_checksums` must be disabled'):
      pickle.dumps(dl_manager)

  def test_force_checksums_validation(self):
    """Tests for download manager with checksums."""
    dl_manager = self._get_manager(
        force_checksums_validation=True,
        register_checksums=False,
    )

    a = Artifact('x')
    self.dl_results[a.url] = a.url_info
    with self.assertRaisesRegex(ValueError, 'Missing checksums url'):
      dl_manager.download(a.url)

  def test_download_cached(self):
    """Tests that the URL is downloaded only once."""
    a = Artifact('x')
    self.dl_results[a.url] = a.url_info

    # Download the URL
    dl_manager = self._get_manager(
        register_checksums=False,
    )
    self.assertEqual(dl_manager.download(a.url), a.url_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles([
        a.url_path, _info_path(a.url_path), '/checksums/checksums.tsv',
    ])

    # Reuse downloaded cache
    dl_manager = self._get_manager(
        register_checksums=False,
    )
    self.assertEqual(dl_manager.download(a.url), a.url_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles([
        a.url_path, _info_path(a.url_path), '/checksums/checksums.tsv',
    ])

    # Reuse downloaded cache, even if url_info is present
    dl_manager = self._get_manager(
        register_checksums=False,
        url_infos={a.url: a.url_info},
    )
    self.assertEqual(dl_manager.download(a.url), a.url_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles([
        a.url_path, _info_path(a.url_path), '/checksums/checksums.tsv'
    ])

    # Reuse downloaded cache and register the checksums
    dl_manager = self._get_manager(
        register_checksums=True,  # <<< Register checksums !!!
    )
    self.assertEqual(dl_manager.download(a.url), a.file_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    # The files have been renamed `url_path` -> `file_path`
    self.assertContainFiles([
        a.file_path, _info_path(a.file_path), '/checksums/checksums.tsv',
    ])

    # After checksums have been registered, `file_path` is used
    dl_manager = self._get_manager(
        register_checksums=False,
        url_infos={a.url: a.url_info},
    )
    self.assertEqual(dl_manager.download(a.url), a.file_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles([
        a.file_path, _info_path(a.file_path), '/checksums/checksums.tsv',
    ])

    # Registering checksums twice still reuse the cached `file_path`
    dl_manager = self._get_manager(
        register_checksums=True,  # <<< Re-register checksums...
        url_infos={a.url: a.url_info},  # ...but checksums already known
    )
    self.assertEqual(dl_manager.download(a.url), a.file_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])  # Still one download
    self.assertContainFiles([
        a.file_path, _info_path(a.file_path), '/checksums/checksums.tsv',
    ])

    # Checksums unknown, so `file_path` unknown, re-downloading
    dl_manager = self._get_manager(
        register_checksums=False,
    )
    self.assertEqual(dl_manager.download(a.url), a.url_path)
    self.assertCountEqual(self.downloaded_urls, [a.url, a.url])  # Re-download!!
    self.assertContainFiles([
        a.url_path, _info_path(a.url_path),
        # `file_path` still exists from previous download
        a.file_path, _info_path(a.file_path),
        '/checksums/checksums.tsv',
    ])

  def test_download_cached_checksums_error(self):
    """Tests that the download is cached, even if record_checksums fails."""
    a = Artifact('x')
    self.dl_results[a.url] = a.url_info

    class StoreChecksumsError(Exception):
      pass

    dl_manager = self._get_manager(
        register_checksums=True,
    )
    with absltest.mock.patch.object(
        checksums_lib, 'save_url_infos', side_effect=StoreChecksumsError()):
      with self.assertRaises(StoreChecksumsError):
        dl_manager.download(a.url)
    # Even after failure, the file was properly downloaded
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles([
        a.url_path, _info_path(a.url_path), '/checksums/checksums.tsv'
    ])

    # When the user retry, it should suceed without redownloading the file
    dl_manager = self._get_manager(
        register_checksums=True,
    )
    self.assertEqual(dl_manager.download(a.url), a.file_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    # The files have been renamed `url_path` -> `file_path`
    self.assertContainFiles([
        a.file_path, _info_path(a.file_path), '/checksums/checksums.tsv'
    ])

  def test_download_url_info_in_info_file_missmatch(self):
    """Tests failure when downloaded checksums and `.INFO` mismatch."""

    a = Artifact('x')
    self.dl_results[a.url] = a.url_info

    # Download the url once
    dl_manager = self._get_manager(register_checksums=False)
    dl_manager.download(a.url)

    # The second time, download the url with a different checksum
    self.dl_results[a.url] = checksums_lib.UrlInfo(
        size=a.url_info.size,
        checksum=_sha256('Other content'),
        filename=a.url_info.filename,
    )
    dl_manager = self._get_manager(
        register_checksums=False,
        force_download=True,
    )
    with self.assertRaisesRegexp(ValueError, 'contains a different checksum'):
      dl_manager.download(a.url)

    # If the url is re-downloaded with the same hash, no error is raised
    self.dl_results[a.url] = a.url_info
    dl_manager = self._get_manager(
        register_checksums=False,
        force_download=True,
    )
    dl_manager.download(a.url)

  def test_register_checksums_url_info_already_exists(self):
    a = Artifact('a.tar.gz')

    # File already downloaded to it's final path (with checksums)
    self.fs.add_file(a.file_path)
    self.fs.add_file(_info_path(a.file_path))

    # Download the file reuse existing path
    manager = self._get_manager(
        register_checksums=True,
        url_infos={a.url: a.url_info},  # Url_info already registered
    )
    res = manager.download(a.url)
    self.assertEqual(res, a.file_path)

    # Checksums are created and url recorded
    self.assertEqual(
        self.fs.files['/checksums/checksums.tsv'],
        f'{a.url}\t{a.url_info.size}\t{a.url_info.checksum}\t{a.url_info.filename}\n',
    )


if __name__ == '__main__':
  testing.test_main()
