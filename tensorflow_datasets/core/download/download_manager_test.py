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

from collections.abc import Sequence
import json
import os
import pickle
from unittest import mock

from absl.testing import parameterized
from etils import epath
import promise
from tensorflow_datasets import testing
from tensorflow_datasets.core.download import checksums as checksums_lib
from tensorflow_datasets.core.download import download_manager as dm
from tensorflow_datasets.core.download import downloader
from tensorflow_datasets.core.download import extractor
from tensorflow_datasets.core.download import resource as resource_lib

ZIP = resource_lib.ExtractMethod.ZIP
TAR = resource_lib.ExtractMethod.TAR
NO_EXTRACT = resource_lib.ExtractMethod.NO_EXTRACT

_DATASET_NAME = 'mnist'

_CHECKSUMS_DIR = epath.Path('/checksums')
_CHECKSUMS_PATH = _CHECKSUMS_DIR / 'checksums.tsv'

_MANUAL_DIR = epath.Path('/manual_dir')

_DOWNLOAD_DIR = epath.Path('/dl_dir')

_EXTRACT_DIR = epath.Path('/extract_dir')


class Artifact:
  # For testing only.

  def __init__(
      self, name: str, url: str | None = None, content: str | None = None
  ):
    self.name = name
    self.url = url or f'http://foo-bar.ch/{self.name}'
    self.content = content or f'content of {self.name}'

    self.url_info = checksums_lib.UrlInfo(
        size=len(self.content),
        checksum=checksums_lib.sha256(self.content),
        filename=self.name,
    )

    self.file_name = resource_lib.get_dl_fname(self.url, self.url_info.checksum)
    self.file_path = _DOWNLOAD_DIR / _DATASET_NAME / self.file_name

    self.url_name = resource_lib.get_dl_fname(self.url)
    self.url_path = _DOWNLOAD_DIR / _DATASET_NAME / self.url_name

    self.manual_path = _MANUAL_DIR / name
    extract_method = resource_lib.guess_extract_method(name)
    self.extract_path = _EXTRACT_DIR / f'{extract_method.name}.{self.file_name}'


class DownloadManagerTest(testing.TestCase, parameterized.TestCase):
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

    def _download(url: str, tmpdir_path: epath.Path, verify: bool):
      del verify
      self.downloaded_urls.append(url)  # Record downloader.download() calls
      # If the name isn't explicitly provided, then it is extracted from the
      # url.
      filename = self.dl_fnames.get(url, os.path.basename(url))
      # Save the file in the tmp_dir
      path = tmpdir_path / filename
      self.fs.add_file(path)
      dl_result = downloader.DownloadResult(
          path=path,
          url_info=self.dl_results[url],
      )
      return promise.Promise.resolve(dl_result)

    return mock.patch.object(
        downloader._Downloader, 'download', side_effect=_download
    )

  def _make_extractor_mock(self):
    """`extractor.extract` patch which creates the returns the path."""

    def _extract(path, method, dest):
      self.extracted_paths.append(path)  # Record downloader.download() calls
      self.fs.add_file(dest, f'Extracted dir from {path}')
      if not os.path.basename(dest).startswith(method.name):
        raise ValueError(
            f'Destination {dest} do not match extraction method {method}'
        )
      return promise.Promise.resolve(self.extract_results[path])

    return mock.patch.object(
        extractor._Extractor, 'extract', side_effect=_extract
    ).start()

  def setUp(self):
    super().setUp()

    # Input of the DownloadManager
    self.dl_results = {}
    self.dl_fnames = {}
    self.extract_results = {}

    # Track calls to downloader/extractor
    self.downloaded_urls = []
    self.extracted_paths = []

    # Virtual file system
    self.fs = testing.MockFs()  # Dict file_path -> file_content

    # Start all mocks
    self.fs.__enter__()
    self._make_downloader_mock().start()
    self._make_extractor_mock().start()
    # Mock `_checksum_paths` (do not load the precomputed checksums)
    mock.patch.object(checksums_lib, '_checksum_paths', lambda: {}).start()

    _CHECKSUMS_DIR.mkdir(parents=True)

    self.addCleanup(mock.patch.stopall)

  def tearDown(self):
    super().tearDown()
    self.fs.__exit__(None, None, None)

  def assertContainFiles(self, filepaths: Sequence[epath.Path]):
    for path in filepaths:
      assert path.exists()

  def _write_info(self, path, info):
    content = json.dumps(info)
    self.fs.add_file(path, content)

  def _get_manager(
      self,
      register_checksums=True,
      url_infos=None,
      dl_dir=_DOWNLOAD_DIR,
      extract_dir=_EXTRACT_DIR,
      manual_dir=_MANUAL_DIR,
      **kwargs,
  ):
    manager = dm.DownloadManager(
        dataset_name=_DATASET_NAME,
        download_dir=dl_dir,
        extract_dir=extract_dir,
        manual_dir=manual_dir,
        register_checksums=register_checksums,
        register_checksums_path=_CHECKSUMS_PATH,
        **kwargs,
    )
    if url_infos:
      manager._url_infos = url_infos
    return manager

  def test_download(self):
    """One file in cache, one not."""
    a, b, c = [Artifact(i) for i in 'abc']
    # File `a` is cached
    self.fs.add_file(a.file_path)
    self.fs.add_file(resource_lib.get_info_path(a.file_path))
    # INFO file of c has been deleted:
    self.fs.add_file(c.file_path)

    # A url is cached, so not downloaded.
    self.dl_results[b.url] = b.url_info
    self.dl_results[c.url] = c.url_info
    manager = self._get_manager(
        url_infos={art.url: art.url_info for art in (a, b, c)}
    )
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
        manager.downloaded_size, sum([art.url_info.size for art in (a, b, c)])
    )

  def test_manually_downloaded(self):
    """One file is manually downloaded, one not."""
    a, b = [Artifact(i) for i in 'ab']

    # File a is manually downloaded
    self.fs.add_file(a.manual_path, content=a.content)
    self.fs.add_file(b.file_path)

    self.dl_results[b.url] = b.url_info
    manager = self._get_manager(
        register_checksums=False,  # Register with manual download not supported
        url_infos={art.url: art.url_info for art in (a, b)},
    )
    downloads = manager.download({'manual': a.url, 'download': b.url})
    expected = {'manual': a.manual_path, 'download': b.file_path}
    self.assertEqual(downloads, expected)

  def test_extract(self):
    """One file already extracted, one file with NO_EXTRACT, one to extract."""
    cached_download_path = _DOWNLOAD_DIR / 'cached'
    cached_resource = resource_lib.Resource(
        path=cached_download_path, extract_method=ZIP
    )
    new_download_path = _DOWNLOAD_DIR / 'new'
    new_resource = resource_lib.Resource(
        path=new_download_path, extract_method=TAR
    )
    no_extract_download_path = _DOWNLOAD_DIR / 'noextract'
    no_extract_resource = resource_lib.Resource(
        path=no_extract_download_path, extract_method=NO_EXTRACT
    )

    cached_extract_path = _EXTRACT_DIR / 'ZIP.cached'
    self.fs.add_file(cached_extract_path)
    new_extract_path = _EXTRACT_DIR / 'TAR.new'
    self.extract_results[new_download_path] = new_extract_path

    manager = self._get_manager()
    res = manager.extract({
        'cached': cached_resource,
        'new': new_resource,
        'noextract': no_extract_resource,
    })
    expected = {
        'cached': cached_extract_path,
        'new': new_extract_path,
        'noextract': no_extract_download_path,
    }
    self.assertEqual(res, expected)
    self.assertCountEqual(self.extracted_paths, [new_download_path])

  def test_extract_twice_parallel(self):
    # Make sure calling extract twice on same resource actually does the
    # extraction once.
    download_path = _DOWNLOAD_DIR / 'foo.tar'
    extract_path = _EXTRACT_DIR / 'TAR.foo'
    self.extract_results[download_path] = extract_path
    manager = self._get_manager()
    out1 = manager.extract([download_path, download_path])
    out2 = manager.extract(download_path)
    self.assertEqual(out1, [extract_path, extract_path])
    self.assertEqual(out2, extract_path)
    # Result is memoize so extract has only been called once
    self.assertCountEqual(self.extracted_paths, [download_path])

  def test_download_and_extract(self):
    a, b = Artifact('a.zip'), Artifact('b')
    self.dl_results[a.url] = a.url_info
    self.dl_results[b.url] = b.url_info
    self.extract_results[a.file_path] = a.extract_path
    # url_b doesn't need any extraction.

    # Result is the same after caching:
    manager = self._get_manager(
        url_infos={
            a.url: a.url_info,
            b.url: b.url_info,
        }
    )
    res = manager.download_and_extract({a.name: a.url, b.name: b.url})
    self.assertEqual(res, {a.name: a.extract_path, b.name: b.file_path})

  def test_download_and_extract_no_manual_dir(self):
    a, b = Artifact('a.zip'), Artifact('b')
    self.dl_results[a.url] = a.url_info
    self.dl_results[b.url] = b.url_info
    self.extract_results[a.file_path] = a.extract_path
    # url_b doesn't need any extraction.

    # Result is the same after caching:
    manager = self._get_manager(
        manual_dir=None,
        url_infos={
            a.url: a.url_info,
            b.url: b.url_info,
        },
    )
    res = manager.download_and_extract({a.name: a.url, b.name: b.url})
    self.assertEqual(res, {a.name: a.extract_path, b.name: b.file_path})

  def test_download_and_extract_archive_ext_in_fname(self):
    # Make sure extraction method is properly deduced from original fname, and
    # not from URL.
    a = Artifact('a', url='http://a?key=1234')
    self.dl_results[a.url] = a.url_info
    self.dl_fnames[a.url] = 'abc.zip'
    self.extract_results[a.file_path] = a.extract_path

    manager = self._get_manager(
        url_infos={
            a.url: a.url_info,
        }
    )
    res = manager.download_and_extract({'a': a.url})
    self.assertEqual(res, {'a': a.extract_path})


  def test_download_and_extract_already_downloaded(self):
    a = Artifact('a')  # Extract can't be deduced from the url, but from .INFO
    # File was already downloaded:
    self.fs.add_file(a.file_path)
    self._write_info(
        resource_lib.get_info_path(a.file_path), {'original_fname': 'a.zip'}
    )
    self.extract_results[a.file_path] = a.extract_path
    manager = self._get_manager(
        url_infos={
            a.url: a.url_info,
        }
    )
    res = manager.download_and_extract(a.url)
    self.assertEqual(res, a.extract_path)
    # No url downloaded, but file extracted.
    self.assertCountEqual(self.downloaded_urls, [])
    self.assertCountEqual(self.extracted_paths, [a.file_path])

  def test_force_download_and_extract(self):
    a = Artifact('a.tar.gz')
    self.dl_results[a.url] = a.url_info
    self.extract_results[a.file_path] = a.extract_path

    # Old content already exists
    self.fs.add_file(a.file_path, content='old content')
    self.fs.add_file(resource_lib.get_info_path(a.file_path), content='{}')

    # Redownloading the data overwrite the content
    manager = self._get_manager(
        force_download=True,
        force_extraction=True,
        url_infos={
            a.url: a.url_info,
        },
    )
    res = manager.download_and_extract(a.url)
    self.assertEqual(res, a.extract_path)

    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertCountEqual(self.extracted_paths, [a.file_path])
    self.assertNotEqual(a.file_path.read_text(), 'old content')
    self.assertNotEqual(
        resource_lib.get_info_path(a.file_path).read_text(), '{}'
    )
    self.assertNotEqual(a.extract_path.read_text(), 'old content')

  def test_wrong_checksum(self):
    a = Artifact('a.tar.gz')
    sha_b = checksums_lib.sha256('content of another file')
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
        NotImplementedError, '`register_checksums` must be disabled'
    ):
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
    self.assertContainFiles(
        [a.url_path, resource_lib.get_info_path(a.url_path)]
    )

    # Reuse downloaded cache
    dl_manager = self._get_manager(
        register_checksums=False,
    )
    self.assertEqual(dl_manager.download(a.url), a.url_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles(
        [a.url_path, resource_lib.get_info_path(a.url_path)]
    )

    # Reuse downloaded cache and register the checksums
    dl_manager = self._get_manager(
        register_checksums=True,  # <<< Register checksums !!!
    )
    self.assertEqual(dl_manager.download(a.url), a.file_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    # The files have been renamed `url_path` -> `file_path`
    self.assertContainFiles([
        a.file_path,
        resource_lib.get_info_path(a.file_path),
        _CHECKSUMS_PATH,
    ])

    # After checksums have been registered, `file_path` is used
    dl_manager = self._get_manager(
        register_checksums=False,
        url_infos={a.url: a.url_info},
    )
    self.assertEqual(dl_manager.download(a.url), a.file_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles([
        a.file_path,
        resource_lib.get_info_path(a.file_path),
        _CHECKSUMS_PATH,
    ])

    # Registering checksums twice still reuse the cached `file_path`
    dl_manager = self._get_manager(
        register_checksums=True,  # <<< Re-register checksums...
        url_infos={a.url: a.url_info},  # ...but checksums already known
    )
    self.assertEqual(dl_manager.download(a.url), a.file_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])  # Still one download
    self.assertContainFiles([
        a.file_path,
        resource_lib.get_info_path(a.file_path),
        _CHECKSUMS_PATH,
    ])

    # Checksums unknown, so `file_path` unknown, re-downloading
    dl_manager = self._get_manager(
        register_checksums=False,
    )
    self.assertEqual(dl_manager.download(a.url), a.url_path)
    self.assertCountEqual(self.downloaded_urls, [a.url, a.url])  # Re-download!!
    self.assertContainFiles([
        a.url_path,
        resource_lib.get_info_path(a.url_path),
        # `file_path` still exists from previous download
        a.file_path,
        resource_lib.get_info_path(a.file_path),
        _CHECKSUMS_PATH,
    ])

  def test_download_cached_url_info_added(self):
    a = Artifact('x')
    self.dl_results[a.url] = a.url_info

    # url_info unknown: File download in url_path
    dl_manager = self._get_manager(
        register_checksums=False,
    )
    self.assertEqual(dl_manager.download(a.url), a.url_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles(
        [a.url_path, resource_lib.get_info_path(a.url_path)]
    )

    # If url_info added:
    # * Reuse downloaded cache
    # * Rename url_path -> file_path
    dl_manager = self._get_manager(
        register_checksums=False,
        url_infos={a.url: a.url_info},
    )
    self.assertEqual(dl_manager.download(a.url), a.file_path)
    self.assertCountEqual(self.downloaded_urls, [a.url])
    self.assertContainFiles(
        [a.file_path, resource_lib.get_info_path(a.file_path)]
    )

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
        checksum=checksums_lib.sha256('Other content'),
        filename=a.url_info.filename,
    )
    dl_manager = self._get_manager(
        register_checksums=False,
        force_download=True,
    )
    with self.assertRaisesRegex(ValueError, 'contains a different "url_info"'):
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
    self.fs.add_file(resource_lib.get_info_path(a.file_path))

    # Download the file reuse existing path
    manager = self._get_manager(
        register_checksums=True,
        url_infos={a.url: a.url_info},  # Url_info already registered
    )
    res = manager.download(a.url)
    self.assertEqual(res, a.file_path)

    # Checksums are created and url recorded
    self.assertEqual(
        self.fs.read_file(_CHECKSUMS_PATH),
        f'{a.url}\t{a.url_info.size}\t{a.url_info.checksum}\t{a.url_info.filename}\n',
    )

  def test_download_cached_url_path_checksum_updated(self):
    old_a = Artifact('a.tar.gz')
    new_a = Artifact('a.tar.gz', content='New content')  # New checksums

    # Urls are equals, but not checksums
    self.assertEqual(old_a.url, new_a.url)
    self.assertNotEqual(old_a.url_info.checksum, new_a.url_info.checksum)

    self.dl_results[old_a.url] = old_a.url_info

    # Old file downloaded to it's url path (with old checksums)
    dl_manager = self._get_manager(
        register_checksums=False,
    )
    self.assertEqual(dl_manager.download(old_a.url), old_a.url_path)
    self.assertCountEqual(self.downloaded_urls, [old_a.url])
    self.assertContainFiles(
        [old_a.url_path, resource_lib.get_info_path(old_a.url_path)]
    )

    # The website has been updated with new content.
    self.dl_results[old_a.url] = new_a.url_info

    # url_info added but do not match cached download anymore
    # -> Redownload new content
    dl_manager = self._get_manager(
        register_checksums=False,
        url_infos={old_a.url: new_a.url_info},  # << Different checksum
    )
    self.assertEqual(dl_manager.download(old_a.url), new_a.file_path)
    # url redownloaded
    self.assertCountEqual(self.downloaded_urls, [old_a.url, old_a.url])
    self.assertContainFiles([
        # Old file still cached
        old_a.url_path,
        resource_lib.get_info_path(old_a.url_path),
        # Re-downloaded with new checksum
        new_a.file_path,
        resource_lib.get_info_path(new_a.file_path),
    ])

  @parameterized.parameters([(1,), (10,), (50,)])
  def test_max_simultaneous_downloads(self, max_simultaneous_downloads):
    dl_manager = self._get_manager(
        max_simultaneous_downloads=max_simultaneous_downloads
    )

    self.assertEqual(
        max_simultaneous_downloads,
        dl_manager._downloader._executor._max_workers,
    )


if __name__ == '__main__':
  testing.test_main()
