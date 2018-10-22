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

"""Local implementation of the download manager.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os
import tarfile
import zipfile

import six.moves.urllib as urllib
from tensorflow import gfile

from tensorflow_datasets.core.download import download_backend
from tensorflow_datasets.core.download import util


class LocalBackend(download_backend.DownloadBackendAbc):
  """Download manager which saves data locally."""

  def download(self, trial):
    """Download and extract the given url (thread safe)."""
    url = trial.url_info.url
    if any(url.startswith(u) for u in ('http://', 'https://')):
      download(url, trial.output_path)
    else:
      raise ValueError('Unsuported URI: {}'.format(url))

  def extract_zip(self, src, dst):
    """Extract the given file."""
    return extract_zip(src, dst)

  def extract_gzip(self, src, dst):
    """Extract the given file."""
    return extract_gzip(src, dst)

  def extract_tar(self, src, dst):
    """Extract the given file."""
    return extract_tar(src, dst)


def download(uri, dst_dir):
  """Download the given URI.

  Args:
    uri: URI to copy (or download) from.
    dst_dir: path to the directory that will be used.

  Returns:
    The path to the downloaded file.
  """
  # Download the URI
  # Should use context manager with Py3 (with urllib2.urlopen(uri) as response)
  response = urllib.request.urlopen(uri)
  filename = response.geturl().split('/')[-1]
  incomplete_path = os.path.join(dst_dir, '{}.incomplete'.format(filename))
  dst_path = os.path.join(dst_dir, filename)

  # TODO(epot): Could add a shared tqdm instance across parallel download
  # to display a single shared progression bar.

  # TODO(epot): Add Google Drive support (cf Ryan code)

  with gfile.Open(incomplete_path, 'wb') as f:
    f.write(response.read())
  gfile.Rename(incomplete_path, dst_path)

  return dst_path


def extract_tar(src, dst):
  """Extract the file to the destination directory."""
  read_type = 'r:gz' if src.endswith('gz') else 'r'  # .tgz and .gz
  with tarfile.open(src, read_type) as t:
    t.extractall(path=dst)


def extract_gzip(src, dst):
  """Extract the file to the destination directory."""
  # Automatically extract the name "abc.gz" => "abc"
  filename = os.path.basename(src)
  filename = util.rchop(filename, '.gz')
  new_path = os.path.join(dst, filename)
  with gzip.open(src, 'rb') as gz_file:
    with gfile.GFile(new_path, mode='wb') as new_file:
      for line in gz_file:
        new_file.write(line)


def extract_zip(src, dst):
  with zipfile.ZipFile(src) as f:
    f.extractall(dst)
