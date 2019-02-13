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

"""Async download API with checksum verification. No business logic."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import hashlib
import io
import os
import re

import concurrent.futures
import promise
import requests
import tensorflow as tf

from tensorflow_datasets.core import units
from tensorflow_datasets.core.download import util
from tensorflow_datasets.core.utils import py_utils

_DRIVE_URL = re.compile(r'^https://drive\.google\.com/')


@py_utils.memoize()
def get_downloader(*args, **kwargs):
  return _Downloader(*args, **kwargs)


def _get_filename(response):
  content_disposition = response.headers.get('content-disposition', None)
  if content_disposition:
    match = re.findall('filename="(.+?)"', content_disposition)
    if match:
      return match[0]
  return util.get_file_name(response.url)


class DownloadError(Exception):
  pass


class _Downloader(object):
  """Class providing async download API with checksum validation.

  Do not instantiate this class directly. Instead, call `get_downloader()`.
  """

  def __init__(self, max_simultaneous_downloads=50, checksumer=None):
    """Init _Downloader instance.

    Args:
      max_simultaneous_downloads: `int`, max number of simultaneous downloads.
      checksumer: `hashlib.HASH`. Defaults to `hashlib.sha256`.
    """
    self._executor = concurrent.futures.ThreadPoolExecutor(
        max_workers=max_simultaneous_downloads)
    self._checksumer = checksumer or hashlib.sha256
    self._pbar_url = None
    self._pbar_dl_size = None

  @contextlib.contextmanager
  def tqdm(self):
    """Add a progression bar for the current download."""
    async_tqdm = py_utils.async_tqdm
    with async_tqdm(total=0, desc='Dl Completed...', unit=' url') as pbar_url:
      with async_tqdm(total=0, desc='Dl Size...', unit=' MiB') as pbar_dl_size:
        self._pbar_url = pbar_url
        self._pbar_dl_size = pbar_dl_size
        yield

  def download(self, url_info, destination_path):
    """Download url to given path. Returns Promise -> sha256 of downloaded file.

    Args:
      url_info: `UrlInfo`, resource to download.
      destination_path: `str`, path to directory where to download the resource.

    Returns:
      Promise obj -> (`str`, int): (downloaded object checksum, size in bytes).
    """
    self._pbar_url.update_total(1)
    url = url_info.url
    future = self._executor.submit(self._sync_download, url, destination_path)
    return promise.Promise.resolve(future)

  def _get_drive_url(self, url, session):
    """Returns url, possibly with confirmation token."""
    response = session.get(url, stream=True)
    if response.status_code != 200:
      raise DownloadError(
          'Failed to get url %s. HTTP code: %d.' % (url, response.status_code))
    for k, v in response.cookies.items():
      if k.startswith('download_warning'):
        return url + '&confirm=' + v  # v is the confirm token
    # No token found, let's try with original URL:
    return url

  def _sync_file_copy(self, filepath, destination_path):
    out_path = os.path.join(destination_path, os.path.basename(filepath))
    tf.io.gfile.copy(filepath, out_path)
    hexdigest, size = py_utils.read_checksum_digest(
        out_path, checksum_cls=self._checksumer)
    return hexdigest, size

  def _sync_download(self, url, destination_path):
    """Synchronous version of `download` method."""
    try:
      # If url is on a filesystem that gfile understands, use copy. Otherwise,
      # use requests.
      if not url.startswith('http'):
        return self._sync_file_copy(url, destination_path)
    except tf.errors.UnimplementedError:
      pass
    session = requests.Session()
    if _DRIVE_URL.match(url):
      url = self._get_drive_url(url, session)
    response = session.get(url, stream=True)
    if response.status_code != 200:
      raise DownloadError(
          'Failed to get url %s. HTTP code: %d.' % (url, response.status_code))
    fname = _get_filename(response)
    path = os.path.join(destination_path, fname)
    size = 0

    size_mb = 0
    unit_mb = units.MiB
    self._pbar_dl_size.update_total(
        int(response.headers.get('Content-length', 0)) // unit_mb
    )
    with tf.io.gfile.GFile(path, 'wb') as file_:
      checksum = self._checksumer()
      for block in response.iter_content(chunk_size=io.DEFAULT_BUFFER_SIZE):
        size += len(block)

        # Update the progress bar
        size_mb += len(block)
        if size_mb > unit_mb:
          self._pbar_dl_size.update(size_mb // unit_mb)
          size_mb %= unit_mb

        checksum.update(block)
        file_.write(block)
    self._pbar_url.update(1)
    return checksum.hexdigest(), size
