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

"""Download manager interface.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import contextlib
import os

import concurrent.futures
import six
from tensorflow import gfile

from tensorflow_datasets.core import utils
from tensorflow_datasets.core.download import local_backend
from tensorflow_datasets.core.download import util
from tensorflow_datasets.core.proto import download_generated_pb2 as download_pb2

# Number of thread to use to parallelize the extractions
_NUM_PARALLEL_DOWNLOADS = 50
_NUM_PARALLEL_EXTRACTS = 1

TAR_EXT = ['.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz2', '.tbz', '.tb2']
# Tuple to match extensions with extraction function.
ExtractFormat = collections.namedtuple('ExtractFormat', 'ext, fn')


class DownloadManager(object):
  """Class which manages the download and extraction of data.

  This has the following advantage:
   * Remove the boilerplate code common to each dataset as now the user only
     has to provide urls.
   * Allow multiple download backends (local and cloud). Otherwise the user
     may be tempted to use standard Python function (ex: tarfile) which may
     not be compatible with one of the backend.
   * Allow to launch multiple download in parallel.
   * Better ressources management (ex: a same url used by multiple
     datasets is downloaded/extracted only once).

  The function members accept either plain value, or values wrapped into list
  or dict. Giving a data structure will parallelize the downloads.

  Example:

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

  For more customization on the download/extraction (ex: passwords, output_name,
  ...), you can give UrlInfo() or ExtractInfo() instead of plain string.

  It is also possible to use the download manager to process a custom function
  with the same guaranties/features than download and extraction.

    # The "/vocab/en-fr" path is cached and can be reused accros run. If
    # the path already exists, the cached value is re-used
    vocab_dir = dl_manager.execute_and_cache(generate_vocab_fn, '/vocab/en-fr')

  """

  def __init__(self, cache_dir, manual_dir=None, mode=None):
    """Download manager constructor.

    Args:
      cache_dir: `str`, Cache directory where all downloads, extractions and
        other artifacts are stored.
      manual_dir: `str`, Directory containing manually downloaded data. Default
        to cache_dir.
      mode (GenerateMode): Mode to FORCE_REDOWNLOAD, REUSE_CACHE_IF_EXISTS or
        REUSE_DATASET_IF_EXISTS. Default to REUSE_DATASET_IF_EXISTS.
    """
    self._cache_dir = os.path.expanduser(cache_dir)
    self._manual_dir = os.path.expanduser(manual_dir or cache_dir)
    self._backend = local_backend.LocalBackend()

    # The generation mode to indicates if we re-use the cached download or
    # force re-downloading data.
    mode = mode or util.GenerateMode.REUSE_DATASET_IF_EXISTS
    self._mode = util.GenerateMode(mode)  # str to Enum

    # Create the root directory if not exists yet
    gfile.MakeDirs(self._cache_dir)

  # Public API

  def download(self, urls_info):
    """Downloads the given urls.

    If one of the download already exists, the cached value will be reused.

    Args:
      urls_info (UrlInfo): The url to download. If a string is passed, it will
        automatically be converted into UrlInfo object

    Returns:
      downloaded_filepaths (str): The downloaded files paths
    """

    # We may want to add a pack kwarg such to keep all downloads in the same
    # directory

    def _download(url_info):
      """Function applied for each individual download."""
      # Convert string to UrlInfo object
      url_info = to_url_info(url_info)

      # Download the url
      return self._process_and_cache_uri(
          uri=url_info.url,
          uri_info=url_info,
          process_trial_fn=self._download,
      )

    # Run the download function on each of the urls
    return _parallel_run(
        _download,
        urls_info,
        max_workers=_NUM_PARALLEL_DOWNLOADS,
    )

  def extract(self, extracts_info):
    """Extract the given path.

    If one of the extraction already exists, the cached value will be reused.

    Args:
      extracts_info (ExtractInfo): The path to extract. If a string is passed,
        it will automatically be converted into ExtractInfo object

    Returns:
      extracted_dirs (str): The downloaded files
    """

    def _extract(extract_info):
      """Function applied for each individual extraction."""
      # Convert string to UrlInfo object
      extract_info = to_extract_info(extract_info)

      # Create the extract uri from the path
      if not extract_info.path.startswith(self._cache_dir):
        raise ValueError(
            'Trying to extract a file ({}) which is not in the cache of the '
            'download manager ({})'.format(extract_info.path, self._cache_dir))
      extract_uri = util.lchop(extract_info.path, self._cache_dir)
      # TODO(epot): There is a risk to reach the max length of filename (256
      # characters in linux and 1k total on CNS)
      extract_uri = os.path.join('extract://', extract_uri.strip('/'))

      # Process an extraction
      return self._process_and_cache_uri(
          uri=extract_uri,
          uri_info=extract_info,
          process_trial_fn=self._extract,
      )

    # Run the extract function on each of the paths
    return _parallel_run(
        _extract,
        extracts_info,
        max_workers=_NUM_PARALLEL_EXTRACTS,
    )

  def download_and_extract(self, urls_info):
    """Convinience method to perform download+extract in a single command.

    As most downloads are imediatelly followed by an extraction, this
    function avoid some boilerplate code. It is equivalent to:
      extracted_dirs = dl_manager.extract(dl_manager.download(urls_info))

    Args:
      urls_info (UrlInfo): Same input as .download()

    Returns:
      extracted_dir (str): Same output as .extract()
    """
    # Maybe the input could accept a UrlExtractInfo(url_info, extract_info)
    # which would contains both UrlInfo and ExtractInfo as currently only
    # the url can be controlled through the arguments.
    return self.extract(self.download(urls_info))

  def execute_and_cache(self, process_fn, cache_key):
    """Execute the function and cache the associated path.

    This function executes the process_fn using a custom cached directory given
    by the key. This allow to use the download manager to cache and share
    additional data like vocabulary or other intermediate artifacts.

    The key are shared between datasets which allow re-using data from other
    datasets but also increase the risk of name collision. A good practice
    is to add the dataset name as prefix of the key.

      vocab_cache_key = os.path.join(self.name, 'vocab/en-fr')
      vocab_dir = dl_manager.execute_and_cache(
          generate_vocab_fn,
          cache_key=vocab_cache_key,
      )

    Args:
      process_fn (fct): Function with signature "(cache_dir) -> None" which
        takes as input a directory on which storing the additional data.
      cache_key (str): Key of the cache to store the data. If the key already
        exists, the process_fn isn't used and the previously cached dir is
        reused.

    Returns:
      cache_dir (str): The directory on which the additional data has been
        written.
    """
    # TODO(epot): Replace this and extract uri by the urijoin ?
    cache_uri = os.path.join('local://', cache_key.strip('/'))

    def inner_process(trial):
      # Create the directory on which generate the additional data
      gfile.MakeDirs(trial.output_path)
      # Call the function to process the additional data
      return process_fn(trial.output_path)

    return self._process_and_cache_uri(
        uri=cache_uri,
        uri_info=None,
        process_trial_fn=inner_process,
    )

  @property
  def manual_dir(self):
    """Returns the directory containing the manually extracted data."""
    if not gfile.Exists(self._manual_dir):
      raise AssertionError(
          'Manual directory {} does not exist. Create it and download/extract'
          'dataset artifacts in there.'.format(self._manual_dir)
      )
    return self._manual_dir

  # Internal functions

  def _process_and_cache_uri(self, uri, uri_info, process_trial_fn):
    """Internal function which manage the cache and launch the trials.

    Args:
      uri (str): Uri to search for in the cache
      uri_info (obj): Additional info for the uri (UrlInfo or ExtractInfo), will
        be saved with the trial
      process_trial_fn (fct): Function with the signature "(UriTrial) -> None"
        which is called if the uri isn't found in the cache

    Returns:
      output_path (str): The output from the Trial
    """

    # Maybe should normalize the uri so that semantically equivalent urls
    # are detected as the same (ex: "http://a.io/" and "http://a.io") and
    # stored in the same register. Or issue guidelines about the url format.

    # Either get the previous cached location or build a new trial
    trial = self._get_or_create_trial(uri=uri, uri_info=uri_info)

    if trial.status != download_pb2.UriTrial.COMPLETED:
      with self._process_trial_controllers(trial):
        process_trial_fn(trial)

    return trial.output_path  # Return cached or processed trial

  def _get_or_create_trial(self, uri, uri_info=None):
    """Create a new trial or get the previous one.

    The previous trials are recreated by looking at the content of the cached
    dir.

    Args:
      uri (str): Uri to create the trial for.
      uri_info (obj): Object containing additional info about the download
        or extraction (UrlInfo or ExtractInfo).

    Returns:
      trial (UriTrial): Result of the trial containing the destination, status,
        timestamp,...
    """
    # The generation is deterministic so generating keys for the same uri will
    # always gives the same result
    trial_id = '{}_{}'.format(
        util.escape_uri(uri),
        util.hash_uri(uri),
    )

    log = util.build_log(prefix=trial_id)

    # Generate a new trial to eventually use
    trial = download_pb2.UriTrial(
        id=trial_id,
        status=download_pb2.UriTrial.IN_PROGRESS,
        output_path=os.path.join(self._cache_dir, trial_id),
    )
    add_uri_info(trial, uri, uri_info)

    if gfile.Exists(trial.output_path):

      # If the directory exists, the previous trial was complete (as it was
      # renamed successfully from ".incomplete")
      if self._mode == util.GenerateMode.FORCE_REDOWNLOAD:
        log('Cleanup previous trial: {}', trial.output_path)
        gfile.DeleteRecursively(trial.output_path)
      else:
        log('Reusing previously cached data...')
        # Try to reuse the previous download
        trial.status = download_pb2.UriTrial.COMPLETED

        # For the downloads, the output_path contains the file
        # TODO(epot): Should instead write the meta-data on disk (in a
        # ._trial.json) and replace ListDirectory() by a version which filter
        # the metadata file.
        is_dl = not any(uri.startswith(p) for p in ('local://', 'extract://'))
        is_gz = (
            uri.startswith('extract://') and
            uri.endswith('.gz') and
            not uri.endswith('tar.gz')
        )
        if is_dl or is_gz:
          trial.output_path = get_download_filepath(trial)
    else:
      log('No cached value found.')

    return trial

  def _process_trial_controllers(self, trial):
    """Decorators to apply before and after the process_trial_fn."""
    return use_incomplete_dir(trial)

  def _download(self, trial):
    """Downloads a single url given by the trial (thread safe).

    Args:
      trial (UriTrial): Object containing info about download.

    Raises:
      ValueError: If the destination dir is not empty
    """
    log = util.build_log(prefix=trial.id)

    # Check the download dir is empty
    if (gfile.Exists(trial.output_path) and
        gfile.ListDirectory(trial.output_path)):
      raise ValueError('Download dir {} should be empty'.format(
          trial.output_path))

    gfile.MakeDirs(trial.output_path)

    log('Start downloading...')
    self._backend.download(trial)

    # TODO(epot): Compute the checksum

    # Update the output path
    trial.output_path = get_download_filepath(trial)

    log('Download complete at {}', trial.output_path)

  def _extract(self, trial):
    """Extract a single file given by the trial.

    Args:
      trial (UriTrial): Object containing info about the extraction.

    Raises:
      ValueError: If the format is incorrect
    """
    log = util.build_log(prefix=trial.id)

    src = trial.extract_info.path
    dst = trial.output_path

    rar_format = ExtractFormat(ext=TAR_EXT, fn=self._backend.extract_tar)
    zip_format = ExtractFormat(ext=['.zip'], fn=self._backend.extract_zip)
    gz_format = ExtractFormat(ext=['.gz'], fn=self._backend.extract_gzip)
    # Order matter as '.tar.gz' will call _extract_tar while '.gz' will
    # call _extract_gzip
    extraction_fns = collections.OrderedDict([
        (download_pb2.ExtractInfo.RAR, rar_format),
        (download_pb2.ExtractInfo.ZIP, zip_format),
        (download_pb2.ExtractInfo.GZ, gz_format),
    ])

    # Filetype explicitly defined
    if trial.extract_info.filetype != download_pb2.ExtractInfo.UNKNOWN:
      extract_filetype = trial.extract_info.filetype
      extract_fn = extraction_fns[extract_filetype]
    # Try to infer the filetype from the name
    else:
      for extract_filetype, extract_format in extraction_fns.items():
        if any(src.lower().endswith(ext) for ext in extract_format.ext):
          extract_fn = extract_format.fn
          break
      else:  # No break (unrecognized archive)
        raise ValueError(
            'Unsuported archive file {} for trial {}. If you think this is an '
            'error, you can try to explicitly define the type in the '
            'ExtractFileType'.format(src, trial.id))

    log('Extract {} with {}...', src, extract_fn.__name__)
    gfile.MakeDirs(dst)
    extract_fn(src, dst)

    if extract_filetype == download_pb2.ExtractInfo.GZ:
      trial.output_path = get_download_filepath(trial)


def to_url_info(value):
  """Convert the strings into UrlInfo."""
  if isinstance(value, six.string_types):
    return download_pb2.UrlInfo(url=value)
  elif isinstance(value, download_pb2.UrlInfo):
    return value
  else:
    raise ValueError('Could not convert {} to UrlInfo'.format(value))


def to_extract_info(value):
  """Convert the strings into ExtractInfo."""
  if isinstance(value, six.string_types):
    return download_pb2.ExtractInfo(path=value)
  elif isinstance(value, download_pb2.ExtractInfo):
    return value
  else:
    raise ValueError('Could not convert {} to UrlInfo'.format(value))


def add_uri_info(trial, uri, uri_info):
  """Add the uri info to the UriTrial."""
  # Add the eventual info
  if uri.startswith('local://'):
    pass
  elif uri.startswith('extract://'):
    trial.extract_info.CopyFrom(uri_info)
  else:
    trial.url_info.CopyFrom(uri_info)


def get_download_filepath(trial):
  """Extract the downloaded file from the completed trial."""
  # Get the downloaded file:
  files = list(gfile.ListDirectory(trial.output_path))
  if not files:  # Should have been catched before, but just in case
    raise ValueError('Download {} failed!'.format(trial.id))
  elif len(files) > 1:
    raise ValueError('Multiple files detected for {}.'.format(trial.id))

  # Update the output path
  filename = files[0]
  return os.path.join(trial.output_path, filename)


@contextlib.contextmanager
def use_incomplete_dir(trial):
  """Wrap the trial in a temporary .incomplete path while it is processed."""
  # Replace the output dir by a temporary dir
  output_path_original = trial.output_path
  # Should add random string to avoid collision with local download manager ?
  output_path_tmp = trial.output_path + '.incomplete'
  trial.output_path = output_path_tmp
  yield
  if not trial.output_path.startswith(output_path_tmp):
    raise ValueError(
        'The output path for {} has been modified to {} and do not match '
        'the original {}'.format(trial.id, trial.output_path, output_path_tmp))
  gfile.Rename(output_path_tmp, output_path_original)
  output_path_extension = util.lchop(trial.output_path, output_path_tmp)
  trial.output_path = output_path_original + output_path_extension


def _parallel_run(function, input_struct, max_workers=1):
  """Run the function on each element of data_struct using a pool of workers."""

  # Distribute the work in a pool
  launch_thread_pool = concurrent.futures.ThreadPoolExecutor
  with launch_thread_pool(max_workers=max_workers) as executor:

    def launch_worker(value):
      return executor.submit(function, value)

    output_struct = utils.map_nested(launch_worker, input_struct)

  # Gather all results once all workers have finished
  def gather_results(value):
    return value.result()

  return utils.map_nested(gather_results, output_struct)
