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

"""DownloadManager."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import contextlib
import gzip
import multiprocessing.dummy as mp
import os
import shutil
import tarfile
import zipfile

import requests
from six.moves import urllib
import tensorflow as tf
from tensorflow_datasets.core import file_format_adapter
import tqdm

__all__ = [
    "DownloadManager",
]

DEFAULT_DOWNLOAD_DIR = os.path.join("~", "tensorflow_datasets", "downloads")


def _extract_tar(filepath, output_path):
  with tarfile.open(filepath) as f:
    f.extractall(output_path)


def _extract_gzip(filepath, output_path):
  with gzip.open(filepath, "rb") as (
      in_f), tf.gfile.Open(output_path, "wb") as out_f:
    shutil.copyfileobj(in_f, out_f)


def _extract_zip(filepath, output_path):
  with zipfile.ZipFile(filepath) as f:
    f.extractall(output_path)


class DownloadManager(object):
  """Manager for downloads and file extractions."""
  # Tuples of (predicate_fn, extraction_fn)
  EXTRACTION_FNS = collections.OrderedDict([
      ("gz", (lambda filepath: filepath.endswith(".gz"), _extract_gzip)),
      ("tar", (tarfile.is_tarfile, _extract_tar)),
      ("zip", (zipfile.is_zipfile, _extract_zip)),
  ])

  def __init__(self, download_dir=None):
    """Constructs a DownloadManager.

    Args:
      download_dir (str): directory for downloads and extractions. Defaults to
        $HOME/tensorflow_datasets/downloads.
    """
    self._download_dir = os.path.expanduser(
        download_dir or DEFAULT_DOWNLOAD_DIR)

  def _create_download_dir(self):
    if not tf.gfile.Exists(self._download_dir):
      tf.gfile.MakeDirs(self._download_dir)

  def download(self, urls, output_filenames=None, num_threads=5):
    """Download urls.

    Args:
      urls (list<str>): URLs to download.
      output_filenames (list<str>): output filenames for urls. Defaults to
        a sanitized version of url. Will be prefixed by self._download_dir.
      num_threads (int): number of threads to use to download in parallel. If
        many of the urls are to the same host, be aware that too many
        simultaneous requests to that host may lead to downloads failing.

    Returns:
      output_filepaths (same length and order as urls)
    """
    self._create_download_dir()
    output_filenames = (output_filenames or
                        [_sanitize_url_for_path(url) for url in urls])
    output_filepaths = [os.path.join(self._download_dir, fname)
                        for fname in output_filenames]

    def _make_download_fn(url, output_filepath):
      """Creates a fn that downloads url to output_filepath."""

      def download():
        if tf.gfile.Exists(output_filepath):
          tf.logging.info("Skipping download because file exists: %s",
                          output_filepath)
          return
        tf.logging.info("Downloading %s", url)
        _download(url, output_filepath)

      return download

    download_fns = [_make_download_fn(url, output_filepath)
                    for url, output_filepath in zip(urls, output_filepaths)]
    _thread_parallelize(download_fns, num_threads)
    return output_filepaths

  def extract(self, filepath, output_name, filetype=None):
    """Extract filepath (gz, tar, etc.) according to extension or filetype."""
    self._create_download_dir()
    output_filepath = os.path.join(self._download_dir, output_name)
    if tf.gfile.Exists(output_filepath):
      tf.logging.info("Skipping extraction because file exists: %s",
                      output_filepath)
      return output_filepath
    if filetype:
      _, extraction_fn = self.EXTRACTION_FNS.get(filetype, (None, None))
      if extraction_fn is None:
        raise ValueError(
            "Unrecognized filetype %s. Available: %s" % (
                filetype, list(self.EXTRACTION_FNS)))
    else:
      extraction_fn = None
      for predicate_fn, extraction_fn_ in self.EXTRACTION_FNS.values():
        if predicate_fn(filepath):
          extraction_fn = extraction_fn_
          break
      if extraction_fn is None:
        raise ValueError(
            "Unrecognized filetype for file %s. Available: %s" % (
                filepath, list(self.EXTRACTION_FNS)))
    extraction_fn(filepath, output_filepath)
    return output_filepath


# TODO(rsepassi): See if there's a way to enable a report hook when downloading
# files in parallel. With the Pool, this errors.
# https://github.com/tqdm/tqdm/issues/323
@contextlib.contextmanager
def _download_progress_bar():
  """Makes tqdm progress bar and yields download report hook."""
  with tqdm.tqdm(unit="B", unit_scale=True) as bar:
    last_count = [0]

    def tqdm_update(count, block_size, total_size):
      if total_size is not None:
        bar.total = total_size
      bar.update((count - last_count[0]) * block_size)
      last_count[0] = count

    yield tqdm_update


def _download_from_google_drive(url, output_filepath):
  """Download from Google Drive, handling virus scan confirmation."""
  confirm_token = None
  session = requests.Session()
  headers = {"Range": "bytes=0-"}
  response = session.get(url, headers=headers, stream=True)

  # Find the download warning confirmation token if there is one
  for k, v in response.cookies.items():
    if k.startswith("download_warning"):
      confirm_token = v

  # If we need to confirm the download, re-request with the confirmation
  if confirm_token:
    params = {"confirm": confirm_token}
    response = session.get(url, headers=headers, params=params, stream=True)

  # For reference if a report hook is added:
  # content_len_hdr = response.headers.get("content-range")
  # total_length = content_len_hdr and int(content_len_hdr.split("/")[-1])
  chunk_size = 16 * 1024
  with tf.gfile.Open(output_filepath, "wb") as f:
    for chunk in response.iter_content(chunk_size):
      if chunk:
        f.write(chunk)
  return output_filepath


def _download(url, output_filepath):
  """Download url to output_filepath."""
  inprogress_filepath = file_format_adapter.incomplete_file(output_filepath)
  parsed_url = urllib.parse.urlparse(url)
  if parsed_url.scheme not in ["http", "https"]:
    raise ValueError("URL must start with http(s): %s" % url)
  try:
    if parsed_url.netloc == "drive.google.com":
      _download_from_google_drive(url, inprogress_filepath)
    else:
      urllib.request.urlretrieve(url, inprogress_filepath)
    tf.gfile.Rename(inprogress_filepath, output_filepath)
    bytes_downloaded = os.stat(output_filepath).st_size
    tf.logging.info("Downloaded %d bytes\nSRC: %s\nDEST: %s",
                    bytes_downloaded, url, output_filepath)
    return output_filepath
  finally:
    if tf.gfile.Exists(inprogress_filepath):
      tf.gfile.Remove(inprogress_filepath)


def _thread_parallelize(fns, num_threads):
  """Launch fns with up to num_threads threads."""
  num_threads = min(num_threads, len(fns))
  if num_threads <= 1:
    for fn in fns:
      fn()
    return
  pool = mp.Pool(num_threads)
  results = []
  for fn in fns:
    results.append(pool.apply_async(fn))
  for result in results:
    result.get()


def _sanitize_url_for_path(url):
  return urllib.parse.quote_plus(url.replace("/", "_")).replace("%", "_")
