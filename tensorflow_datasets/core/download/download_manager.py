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

"""Download manager interface."""

from __future__ import annotations

from collections.abc import Iterator
import concurrent.futures
import dataclasses
import functools
import hashlib
import typing
from typing import Any
import uuid

from absl import logging
from etils import epath
from etils import epy
from tensorflow_datasets.core.utils.lazy_imports_utils import tree

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  import promise

  from tensorflow_datasets.core import utils
  from tensorflow_datasets.core.download import checksums
  from tensorflow_datasets.core.download import downloader
  from tensorflow_datasets.core.download import extractor
  from tensorflow_datasets.core.download import kaggle
  from tensorflow_datasets.core.download import resource as resource_lib
  from tensorflow_datasets.core.download import util
  from tensorflow_datasets.core.utils import shard_utils
  from tensorflow_datasets.core.utils import type_utils
  # pylint: enable=g-import-not-at-top

# pylint: disable=logging-fstring-interpolation

Tree = type_utils.Tree

Url = str | resource_lib.Resource
ExtractPath = epath.PathLike | resource_lib.Resource


def get_downloader(*args: Any, **kwargs: Any):
  return downloader.get_downloader(*args, **kwargs)


class NonMatchingChecksumError(Exception):
  """The downloaded file doesn't have expected checksum."""


# Even if `DownloadConfig` is immutable inside TFDS, we do not set `frozen=True`
# to allow user to set:
# dl_config = tfds.download.DownloadConfig()
# dl_config.beam_runner = ...
@dataclasses.dataclass(eq=False)
class DownloadConfig:
  """Configuration for `tfds.core.DatasetBuilder.download_and_prepare`.

  Attributes:
    extract_dir: `str`, directory where extracted files are stored. Defaults to
      "<download_dir>/extracted".
    manual_dir: `str`, read-only directory where manually downloaded/extracted
      data is stored. Defaults to `<download_dir>/manual`.
    download_mode: `tfds.GenerateMode`, how to deal with downloads or data that
      already exists. Defaults to `REUSE_DATASET_IF_EXISTS`, which will reuse
      both downloads and data if it already exists.
    compute_stats: `tfds.download.ComputeStats`, whether to compute statistics
      over the generated data. Defaults to `AUTO`.
    max_examples_per_split: `int`, optional max number of examples to write into
      each split (used for testing). If set to 0, only execute the
      `_split_generators` (download the original data), but skip
      `_generator_examples`.
    register_checksums: `bool`, defaults to False. If True, checksum of
      downloaded files are recorded.
    force_checksums_validation: `bool`, defaults to False. If True, raises an
      error if an URL do not have checksums.
    beam_runner: Runner to pass to `beam.Pipeline`, only used for datasets based
      on Beam for the generation.
    beam_options: `PipelineOptions` to pass to `beam.Pipeline`, only used for
      datasets based on Beam for the generation.
    try_download_gcs: `bool`, defaults to True. If True, prepared dataset will
      be downloaded from GCS, when available. If False, dataset will be
      downloaded and prepared from scratch.
    verify_ssl: `bool`, defaults to True. If True, will verify certificate when
      downloading dataset.
    override_max_simultaneous_downloads: `int`, optional max number of
      simultaneous downloads. If set, it will override dataset builder and
      downloader default values.
    num_shards: optional number of shards that should be created. If `None`,
      then the number of shards is computed based on the total size of the
      dataset and the min and max shard size.
    min_shard_size: optional minimum shard size in bytes. If `None`, 64 MB is
      used.
    max_shard_size: optional maximum shard size in bytes. If `None`, 1 GiB is
      used.
    ignore_duplicates: whether to ignore duplicated examples with the same key.
      If there are multiple examples with the same key, the first one is kept.
  """

  extract_dir: epath.PathLike | None = None
  manual_dir: epath.PathLike | None = None
  download_mode: util.GenerateMode = util.GenerateMode.REUSE_DATASET_IF_EXISTS
  compute_stats: util.ComputeStatsMode = util.ComputeStatsMode.SKIP
  max_examples_per_split: int | None = None
  register_checksums: bool = False
  force_checksums_validation: bool = False
  beam_runner: Any | None = None
  beam_options: Any | None = None
  try_download_gcs: bool = True
  verify_ssl: bool = True
  override_max_simultaneous_downloads: int | None = None
  num_shards: int | None = None
  min_shard_size: int = shard_utils.DEFAULT_MIN_SHARD_SIZE
  max_shard_size: int = shard_utils.DEFAULT_MAX_SHARD_SIZE
  ignore_duplicates: bool = False

  def get_shard_config(self) -> shard_utils.ShardConfig:
    return shard_utils.ShardConfig(
        num_shards=self.num_shards,
        min_shard_size=self.min_shard_size,
        max_shard_size=self.max_shard_size,
    )

  def replace(self, **kwargs: Any) -> DownloadConfig:
    """Returns a copy with updated attributes."""
    return dataclasses.replace(self, **kwargs)


class DownloadManager:
  """Manages the download and extraction of files, as well as caching.

  Downloaded files are cached under `download_dir`. The file name of downloaded
   files follows pattern "{sanitized_url}{content_checksum}.{ext}". Eg:
   'cs.toronto.edu_kriz_cifar-100-pythonJDF[...]I.tar.gz'.

  While a file is being downloaded, it is placed into a directory following a
  similar but different pattern:
  "{sanitized_url}{url_checksum}.tmp.{uuid}".

  When a file is downloaded, a "{fname}.INFO.json" file is created next to it.
  This INFO file contains the following information:
  {"dataset_names": ["name1", "name2"],
   "urls": ["http://url.of/downloaded_file"]}

  Extracted files/dirs are stored under `extract_dir`. The file name or
  directory name is the same as the original name, prefixed with the extraction
  method. E.g.
   "{extract_dir}/TAR_GZ.cs.toronto.edu_kriz_cifar-100-pythonJDF[...]I.tar.gz".

  The function members accept either plain value, or values wrapped into list
  or dict. Giving a data structure will parallelize the downloads.

  Example of usage:

  ```
  # Sequential download: str -> str
  train_dir = dl_manager.download_and_extract('https://abc.org/train.tar.gz')
  test_dir = dl_manager.download_and_extract('https://abc.org/test.tar.gz')

  # Parallel download: list -> list
  image_files = dl_manager.download(
      ['https://a.org/1.jpg', 'https://a.org/2.jpg', ...])

  # Parallel download: dict -> dict
  data_dirs = dl_manager.download_and_extract({
     'train': 'https://abc.org/train.zip',
     'test': 'https://abc.org/test.zip',
  })
  data_dirs['train']
  data_dirs['test']
  ```

  For more customization on the download/extraction (ex: passwords, output_name,
  ...), you can pass a `tfds.download.Resource` as argument.
  """

  def __init__(
      self,
      *,
      download_dir: epath.PathLike,
      extract_dir: epath.PathLike | None = None,
      manual_dir: epath.PathLike | None = None,
      manual_dir_instructions: str | None = None,
      url_infos: dict[str, checksums.UrlInfo] | None = None,
      dataset_name: str | None = None,
      force_download: bool = False,
      force_extraction: bool = False,
      force_checksums_validation: bool = False,
      register_checksums: bool = False,
      register_checksums_path: epath.PathLike | None = None,
      verify_ssl: bool = True,
      max_simultaneous_downloads: int | None = None,
  ):
    """Download manager constructor.

    Args:
      download_dir: Path to directory where downloads are stored.
      extract_dir: Path to directory where artifacts are extracted.
      manual_dir: Path to manually downloaded/extracted data directory.
      manual_dir_instructions: Human readable instructions on how to prepare
        contents of the manual_dir for this dataset.
      url_infos: Urls info for the checksums.
      dataset_name: Name of dataset this instance will be used for. If provided,
        downloads will contain which datasets they were used for.
      force_download: If True, always [re]download.
      force_extraction: If True, always [re]extract.
      force_checksums_validation: If True, raises an error if an URL do not have
        checksums.
      register_checksums: If True, dl checksums aren't checked, but stored into
        file.
      register_checksums_path: Path were to save checksums. Should be set if
        register_checksums is True.
      verify_ssl: `bool`, defaults to True. If True, will verify certificate
        when downloading dataset.
      max_simultaneous_downloads: `int`, optional max number of simultaneous
        downloads.

    Raises:
      FileNotFoundError: Raised if the register_checksums_path does not exist.
    """
    if register_checksums:
      if not register_checksums_path:
        raise ValueError(
            'When register_checksums=True, register_checksums_path should be'
            ' set.'
        )
      register_checksums_path = epath.Path(register_checksums_path)

    download_dir = epath.Path(download_dir).expanduser()
    if extract_dir:
      extract_dir = epath.Path(extract_dir).expanduser()
    else:
      extract_dir = download_dir / 'extracted'
    if manual_dir is not None:
      manual_dir = epath.Path(manual_dir).expanduser()

    self._download_dir: epath.Path = download_dir
    self._extract_dir: epath.Path = extract_dir
    self._manual_dir: epath.Path | None = manual_dir
    self._manual_dir_instructions = utils.dedent(manual_dir_instructions)
    self._download_dir.mkdir(parents=True, exist_ok=True)
    self._extract_dir.mkdir(parents=True, exist_ok=True)

    self._force_download = force_download
    self._force_extraction = force_extraction
    self._force_checksums_validation = force_checksums_validation
    self._register_checksums = register_checksums
    self._register_checksums_path = register_checksums_path
    self._verify_ssl = verify_ssl
    self._max_simultaneous_downloads = max_simultaneous_downloads
    self._dataset_name = dataset_name

    # All known URLs: {url: UrlInfo(size=, checksum=)}
    self._url_infos = checksums.get_all_url_infos()
    if url_infos is not None:
      self._url_infos.update(url_infos)

    # To record what is being used: {url: UrlInfo(size, checksum, filename)}
    self._recorded_url_infos: dict[str, checksums.UrlInfo] = {}
    # These attributes are lazy-initialized since they must be cleared when this
    # object is pickled for Beam. They are then recreated on each worker.
    self.__downloader = None
    self.__extractor = None
    # Executor to avoid blocking other download/extractions when running I/O
    # operations (reading/renaming download file).
    # Only use a single thread as the read/ops are locked by the
    # `build_synchronize_decorator`.
    # Note: This thread is in additions of the download and extraction
    # executors threads.
    self._executor = concurrent.futures.ThreadPoolExecutor(1)

  def __getstate__(self):
    """Remove un-pickleable attributes and return the state."""
    if self._register_checksums:
      # Currently, checksums registration from Beam not supported.
      raise NotImplementedError(
          '`register_checksums` must be disabled in a parallelized '
          'DownloadManager. Please open a PR if you would like this feature.'
      )
    state = self.__dict__.copy()
    state['_DownloadManager__downloader'] = None
    state['_DownloadManager__extractor'] = None
    state['_executor'] = None
    return state

  @property
  def _downloader(self):
    if not self.__downloader:
      self.__downloader = get_downloader(
          max_simultaneous_downloads=self._max_simultaneous_downloads
      )
    return self.__downloader

  @property
  def _extractor(self):
    if not self.__extractor:
      self.__extractor = extractor.get_extractor()
    return self.__extractor

  @property
  def downloaded_size(self):
    """Returns the total size of downloaded files."""
    return sum(url_info.size for url_info in self._recorded_url_infos.values())

  def _get_dl_path(self, url: str, sha256: str) -> epath.Path:
    return self._download_dir / resource_lib.get_dl_fname(url, sha256)

  @property
  def register_checksums(self):
    """Returns whether checksums are being computed and recorded to file."""
    return self._register_checksums

  @utils.build_synchronize_decorator()
  def _record_url_infos(self):
    """Store in file when recorded size/checksum of downloaded files."""
    checksums.save_url_infos(
        self._register_checksums_path,
        self._recorded_url_infos,
    )

  # Synchronize and memoize decorators ensure same resource will only be
  # processed once, even if passed twice to download_manager.
  @utils.build_synchronize_decorator()
  @utils.memoize()
  def _download(self, resource: Url) -> promise.Promise[epath.Path]:
    """Download resource, returns Promise->path to downloaded file.

    This function:

    1. Reuse cache (`_get_cached_path`) or download the file
    2. Register or validate checksums (`_register_or_validate_checksums`)
    3. Rename download to final path (`_rename_and_get_final_dl_path`)

    Args:
      resource: The URL to download.

    Returns:
      path: The path to the downloaded resource.
    """
    # Normalize the input
    if isinstance(resource, str):
      url = resource
    else:
      url = resource.url
    assert url is not None, 'URL is undefined from resource.'

    expected_url_info = self._url_infos.get(url)

    # 3 possible destinations for the path:
    # * In `manual_dir` (manually downloaded data)
    # * In `downloads/url_path` (checksum unknown)
    # * In `downloads/checksum_path` (checksum registered)
    manually_downloaded_path = _get_manually_downloaded_path(
        manual_dir=self._manual_dir,
        expected_url_info=expected_url_info,
    )
    url_path = self._get_dl_path(
        url, sha256=hashlib.sha256(url.encode('utf-8')).hexdigest()
    )
    checksum_path = (
        self._get_dl_path(url, sha256=expected_url_info.checksum)
        if expected_url_info
        else None
    )

    # Get the cached path and url_info (if they exists)
    dl_result = downloader.get_cached_path(
        manually_downloaded_path=manually_downloaded_path,
        checksum_path=checksum_path,
        url_path=url_path,
        expected_url_info=expected_url_info,
    )
    if dl_result.path and not self._force_download:  # Download was cached
      logging.info(
          f'Skipping download of {url}: File cached in {dl_result.path}'
      )
      # Still update the progression bar to indicate the file was downloaded
      self._downloader.increase_tqdm(dl_result)
      future = promise.Promise.resolve(dl_result)
    else:
      # Download in an empty tmp directory (to avoid name collisions)
      # `download_tmp_dir` is cleaned-up in `_rename_and_get_final_dl_path`
      dirname = f'{resource_lib.get_dl_dirname(url)}.tmp.{uuid.uuid4().hex}'
      download_tmp_dir = self._download_dir / dirname
      download_tmp_dir.mkdir()
      logging.info(f'Downloading {url} into {download_tmp_dir}...')
      future = self._downloader.download(
          url, download_tmp_dir, verify=self._verify_ssl
      )

    # Post-process the result
    return future.then(
        lambda dl_result: self._register_or_validate_checksums(  # pylint: disable=g-long-lambda
            url=url,
            path=dl_result.path,
            computed_url_info=dl_result.url_info,
            expected_url_info=expected_url_info,
            checksum_path=checksum_path,
            url_path=url_path,
        )
    )

  def _register_or_validate_checksums(
      self,
      path: epath.Path,
      url: str,
      expected_url_info: checksums.UrlInfo | None,
      computed_url_info: checksums.UrlInfo | None,
      checksum_path: epath.Path | None,
      url_path: epath.Path,
  ) -> epath.Path:
    """Validates/records checksums and renames final downloaded path."""
    # `path` can be:
    # * Manually downloaded
    # * (cached) checksum_path
    # * (cached) url_path
    # * `tmp_dir/file` (downloaded path)

    if computed_url_info:
      # Used both in `.downloaded_size` and `_record_url_infos()`
      self._recorded_url_infos[url] = computed_url_info

    if self._register_checksums:
      if not computed_url_info:
        raise ValueError(
            f'Cannot register checksums for {url}: no computed checksum. '
            '--register_checksums with manually downloaded data not supported.'
        )
      # Note:
      # * We save even if `expected_url_info == computed_url_info` as
      #   `expected_url_info` might have been loaded from another dataset.
      # * `register_checksums_path` was validated in `__init__` so this
      #   shouldn't fail.
      self._record_url_infos()

      # Checksum path should now match the new registered checksum (even if
      # checksums were previously registered)
      expected_url_info = computed_url_info
      checksum_path = self._get_dl_path(url, computed_url_info.checksum)
    else:
      # Eventually validate checksums
      # Note:
      # * If path is cached at `url_path` but cached
      #   `computed_url_info != expected_url_info`, a new download has
      #   been triggered (as _get_cached_path returns None)
      # * If path was downloaded but checksums don't match expected, then
      #   the download isn't cached (re-running build will retrigger a new
      #   download). This is expected as it might mean the downloaded file
      #   was corrupted. Note: The tmp file isn't deleted to allow inspection.
      _validate_checksums(
          url=url,
          path=path,
          expected_url_info=expected_url_info,
          computed_url_info=computed_url_info,
          force_checksums_validation=self._force_checksums_validation,
      )

    return self._rename_and_get_final_dl_path(
        url=url,
        path=path,
        expected_url_info=expected_url_info,
        computed_url_info=computed_url_info,
        checksum_path=checksum_path,
        url_path=url_path,
    )

  def _rename_and_get_final_dl_path(
      self,
      url: str,
      path: epath.Path,
      expected_url_info: checksums.UrlInfo | None,
      computed_url_info: checksums.UrlInfo | None,
      checksum_path: epath.Path | None,
      url_path: epath.Path,
  ) -> epath.Path:
    """Eventually rename the downloaded file if checksums were recorded."""
    # `path` can be:
    # * Manually downloaded
    # * (cached) checksum_path
    # * (cached) url_path
    # * `tmp_dir/file` (downloaded path)
    if self._manual_dir and path.is_relative_to(self._manual_dir):
      return path  # Manually downloaded data
    elif path == checksum_path:  # Path already at final destination
      assert computed_url_info == expected_url_info  # Sanity check
      return checksum_path  # pytype: disable=bad-return-type
    elif path == url_path:
      if checksum_path:
        # Checksums were registered: Rename -> checksums_path
        resource_lib.replace_info_file(path, checksum_path)
        return path.replace(checksum_path)
      else:
        # Checksums not registered: -> do nothing
        return path
    else:  # Path was downloaded in tmp dir
      dst_path = checksum_path or url_path
      resource_lib.write_info_file(
          url=url,
          path=dst_path,
          dataset_name=self._dataset_name,
          original_fname=path.name,
          url_info=computed_url_info,
      )
      path.replace(dst_path)
      path.parent.rmdir()  # Cleanup tmp dir (will fail if dir not empty)
      return dst_path

  @utils.build_synchronize_decorator()
  @utils.memoize()
  def _extract(self, resource: ExtractPath) -> promise.Promise[epath.Path]:
    """Extract a single archive, returns Promise->path to extraction result."""
    if not isinstance(resource, resource_lib.Resource):
      resource = resource_lib.Resource(path=resource)
    path = resource.path
    extract_method = resource.extract_method
    if extract_method == resource_lib.ExtractMethod.NO_EXTRACT:
      logging.info('Skipping extraction for %s (method=NO_EXTRACT).', path)
      return promise.Promise.resolve(path)
    method_name = resource_lib.ExtractMethod(extract_method).name
    extract_path = self._extract_dir / f'{method_name}.{path.name}'
    if not self._force_extraction and extract_path.exists():
      logging.info('Reusing extraction of %s at %s.', path, extract_path)
      return promise.Promise.resolve(extract_path)
    return self._extractor.extract(path, extract_method, extract_path)

  @utils.build_synchronize_decorator()
  @utils.memoize()
  def _download_extract(self, resource):
    """Download-extract `Resource` or url, returns Promise->path."""
    if isinstance(resource, str):
      resource = resource_lib.Resource(url=resource)

    def callback(path):
      resource.path = path
      return self._extract(resource)

    return self._download(resource).then(callback)

  def download_checksums(self, checksums_url):
    """Downloads checksum file from the given URL and adds it to registry."""
    checksums_path = self.download(checksums_url)
    self._url_infos.update(checksums.load_url_infos(checksums_path))

  def download_kaggle_data(self, competition_or_dataset: str) -> epath.Path:
    """Download data for a given Kaggle Dataset or competition.

    Note: This function requires the Kaggle CLI tool.
    Read the installation guide at https://www.kaggle.com/docs/api.

    Args:
      competition_or_dataset: Dataset name (`zillow/zecon`) or competition name
        (`titanic`)

    Returns:
      The path to the downloaded files.
    """
    return kaggle.download_kaggle_data(
        competition_or_dataset, self._download_dir
    )

  @typing.overload
  def download(self, url_or_urls: Url) -> epath.Path:
    ...

  @typing.overload
  def download(self, url_or_urls: dict[str, Url]) -> dict[str, epath.Path]:
    ...

  @typing.overload
  def download(self, url_or_urls: Tree[Url]) -> Tree[epath.Path]:
    ...

  def download(self, url_or_urls):
    """Download given url(s).

    Args:
      url_or_urls: url or `list`/`dict` of urls to download and extract. Each
        url can be a `str` or `tfds.download.Resource`.

    Returns:
      downloaded_path(s): `str`, The downloaded paths matching the given input
        url_or_urls.
    """
    # Add progress bar to follow the download state
    with self._downloader.tqdm():
      return _map_promise(self._download, url_or_urls)

  def iter_archive(
      self,
      resource: ExtractPath,
  ) -> Iterator[tuple[str, typing.BinaryIO]]:
    """Returns iterator over files within archive.

    **Important Note**: caller should read files as they are yielded.
    Reading out of order is slow.

    Args:
      resource: path to archive or `tfds.download.Resource`.

    Returns:
      Generator yielding tuple (path_within_archive, file_obj).
    """
    if not isinstance(resource, resource_lib.Resource):
      resource = resource_lib.Resource(path=resource)
    return extractor.iter_archive(resource.path, resource.extract_method)

  @typing.overload
  def extract(self, path_or_paths: ExtractPath) -> epath.Path:
    ...

  @typing.overload
  def extract(
      self, path_or_paths: dict[str, ExtractPath]
  ) -> dict[str, epath.Path]:
    ...

  @typing.overload
  def extract(self, path_or_paths: Tree[ExtractPath]) -> Tree[epath.Path]:
    ...

  def extract(self, path_or_paths):
    """Extract given path(s).

    Args:
      path_or_paths: path or `list`/`dict` of path of file to extract. Each path
        can be a `str` or `tfds.download.Resource`.  If not explicitly specified
        in `Resource`, the extraction method is deduced from downloaded file
        name.

    Returns:
      extracted_path(s): `str`, The extracted paths matching the given input
        path_or_paths.
    """
    # Add progress bar to follow the download state
    with self._extractor.tqdm():
      return _map_promise(self._extract, path_or_paths)

  @typing.overload
  def download_and_extract(self, url_or_urls: Url) -> epath.Path:
    ...

  @typing.overload
  def download_and_extract(
      self, url_or_urls: dict[str, Url]
  ) -> dict[str, epath.Path]:
    ...

  @typing.overload
  def download_and_extract(self, url_or_urls: Tree[Url]) -> Tree[epath.Path]:
    ...

  def download_and_extract(self, url_or_urls):
    """Download and extract given url_or_urls.

    Is roughly equivalent to:

    ```
    extracted_paths = dl_manager.extract(dl_manager.download(url_or_urls))
    ```

    Args:
      url_or_urls: url or `list`/`dict` of urls to download and extract. Each
        url can be a `str` or `tfds.download.Resource`.  If not explicitly
        specified in `Resource`, the extraction method will automatically be
        deduced from downloaded file name.

    Returns:
      extracted_path(s): `str`, extracted paths of given URL(s).
    """
    # Add progress bar to follow the download state
    with self._downloader.tqdm():
      with self._extractor.tqdm():
        return _map_promise(self._download_extract, url_or_urls)

  @property
  def download_dir(self) -> epath.Path:
    return self._download_dir

  @functools.cached_property
  def manual_dir(self) -> epath.Path:
    """Returns the directory containing the manually extracted data."""
    if not self._manual_dir:
      raise AssertionError('Manual directory not enabled.')
    if not self._manual_dir_instructions:
      raise ValueError(
          'To access `dl_manager.manual_dir`, please set '
          '`MANUAL_DOWNLOAD_INSTRUCTIONS` in your dataset.'
      )
    if not self._manual_dir.exists() or not list(self._manual_dir.iterdir()):
      raise AssertionError(
          f'Manual directory {self._manual_dir} does not exist or is empty. '
          'Create it and download/extract dataset artifacts in there using '
          f'instructions:\n{self._manual_dir_instructions}'
      )
    return self._manual_dir


def _get_manually_downloaded_path(
    manual_dir: epath.Path | None,
    expected_url_info: checksums.UrlInfo | None,
) -> epath.Path | None:
  """Checks if file is already downloaded in manual_dir."""
  if not manual_dir:  # Manual dir not passed
    return None

  if not expected_url_info or not expected_url_info.filename:
    return None  # Filename unknown.

  manual_path = manual_dir / expected_url_info.filename
  if not manual_path.exists():  # File not manually downloaded
    return None

  return manual_path


def _validate_checksums(
    url: str,
    path: epath.Path,
    computed_url_info: checksums.UrlInfo | None,
    expected_url_info: checksums.UrlInfo | None,
    force_checksums_validation: bool,
) -> None:
  """Validate computed_url_info match expected_url_info."""
  # If force-checksums validations, both expected and computed url_info
  # should exists
  if force_checksums_validation:
    # Checksum of the downloaded file unknown (for manually downloaded file)
    if not computed_url_info:
      computed_url_info = checksums.compute_url_info(path)
    # Checksums have not been registered
    if not expected_url_info:
      raise ValueError(
          f'Missing checksums url: {url}, yet '
          '`force_checksums_validation=True`. '
          'Did you forget to register checksums?'
      )

  if (
      expected_url_info
      and computed_url_info
      and expected_url_info != computed_url_info
  ):
    msg = (
        f'Artifact {url}, downloaded to {path}, has wrong checksum:\n'
        f'* Expected: {expected_url_info}\n'
        f'* Got: {computed_url_info}\n'
        'To debug, see: '
        'https://www.tensorflow.org/datasets/overview#fixing_nonmatchingchecksumerror'
    )
    raise NonMatchingChecksumError(msg)


def _map_promise(map_fn, all_inputs):
  """Map the function into each element and resolve the promise."""
  all_promises = tree.map_structure(map_fn, all_inputs)  # Apply the function
  res = tree.map_structure(lambda p: p.get(), all_promises)  # Wait promises
  return res
