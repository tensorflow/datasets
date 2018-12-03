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

"""Async download API with checksum verification. No business logic."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import hashlib
import io
import os

import concurrent.futures
import promise
import six.moves.urllib as urllib
from tensorflow import gfile

from tensorflow_datasets.core.download import util
from tensorflow_datasets.core.utils import py_utils


class HTTPError(Exception):
  """There was a problem retrieving resource."""

  def __init__(self, url, code, reason):
    msg = 'Failed retrieving %s: %s %s.' % (url, code, reason)
    Exception.__init__(self, msg)


@py_utils.memoize()
def get_downloader(*args, **kwargs):
  return _Downloader(*args, **kwargs)


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

  def download(self, url_info, destination_path):
    """Download url to given path. Returns Promise -> sha256 of downloaded file.

    Args:
      url_info: `UrlInfo`, resource to download.
      destination_path: `str`, path to directory where to download the resource.

    Returns:
      Promise obj -> `str` checksum of downloaded object.
    """
    url = url_info.url
    future = self._executor.submit(self._sync_download, url, destination_path)
    return promise.Promise.resolve(future)

  def _sync_download(self, url, destination_path):
    """Synchronous version of `download` method."""
    checksum = self._checksumer()
    try:
      with contextlib.closing(urllib.request.urlopen(url)) as response:
        fname = util.get_file_name(response.geturl())
        path = os.path.join(destination_path, fname)
        _copy_response_to_file(response, path, checksum)
    except urllib.error.HTTPError as err:
      raise HTTPError(url, err.code, err.reason)
    return checksum.hexdigest()


def _copy_response_to_file(response, path, checksum):
  """Copy response (stream) content to file at path, updates checksum."""
  with gfile.Open(path, 'wb') as file_:
    while True:
      block = response.read(io.DEFAULT_BUFFER_SIZE)
      if not block:
        break
      checksum.update(block)
      # TODO(pierrot): Test this is faster than doing checksum in the end
      # and document results here.
      file_.write(block)
