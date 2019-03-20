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

"""Classes to specify download or extraction information."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import base64
import codecs
import hashlib
import itertools
import json
import os
import re

import enum
from six.moves import urllib
import tensorflow as tf

from tensorflow_datasets.core import api_utils
from tensorflow_datasets.core.download import util
from tensorflow_datasets.core.utils import py_utils


_hex_codec = codecs.getdecoder('hex_codec')


def _decode_hex(hexstr):
  """Returns binary digest, given str hex digest."""
  return _hex_codec(hexstr)[0]


class ExtractMethod(enum.Enum):
  """The extraction method to use to pre-process a downloaded file."""
  NO_EXTRACT = 1
  TAR = 2
  TAR_GZ = 3
  GZIP = 4
  ZIP = 5
  BZIP2 = 6


_EXTRACTION_METHOD_TO_EXTS = [
    (ExtractMethod.TAR_GZ, ['.tar.gz', '.tgz']),
    (ExtractMethod.TAR, ['.tar', '.tar.bz2', '.tbz2', '.tbz', '.tb2']),
    (ExtractMethod.ZIP, ['.zip']),
    (ExtractMethod.GZIP, ['.gz']),
    (ExtractMethod.BZIP2, ['.bz2']),
]

_KNOWN_EXTENSIONS = [
    ext_ for ext_ in itertools.chain(  # pylint: disable=g-complex-comprehension
        *[extensions_ for _, extensions_ in _EXTRACTION_METHOD_TO_EXTS])]

_NETLOC_COMMON_PREFIXES = [
    'www.',
    'storage.googleapis.com',
    'drive.google.com',
    'github.com',
]

_NETLOC_COMMON_SUFFIXES = [
    '.github.io',
    '.s3-website.eu-central-1.amazonaws.com',
    '.amazonaws.com',  # Must be kept after the other amazonaws.com subdomains.
]

_URL_COMMON_PARTS = [
    '_data_',
    '_dataset_',
    '_static_',
    '_of_',
    '-of-',
]


def _guess_extract_method(fname):
  """Guess extraction method, given file name (or path)."""
  for method, extensions in _EXTRACTION_METHOD_TO_EXTS:
    for ext in extensions:
      if fname.endswith(ext):
        return method
  return ExtractMethod.NO_EXTRACT


def _sanitize_url(url, max_length):
  """Sanitize and shorten url to fit in max_length.

  Function is stable: same input MUST ALWAYS give same result, accros changes
  in code as well. Different URLs might give same result.
  As much as possible, the extension should be kept.

  Heuristics are applied to only keep useful info from url.

  1- Drop generic [sub]domains.
    'www.cs.toronto.edu/...' -> 'cs.toronto.edu/...'
    'storage.googleapis.com/foo/...' -> 'foo/...'
    'drive.google.com/bar/...' -> 'bar/...'
    'github.com/baz/...' -> 'baz/...'

  2- Remove leading '0's from url components:
    'foo/train-00004-of-00010.tfrecords' -> 'foo/train-4-of-10.tfrecords'

  3- Truncate each component of url until total size fits or each component is
     left with 4 chars (or total size is <= limit):
     'MoveUnitToBorder_64x64_png/train-4-of-10.tfrecords'
     (here truncate components to 4 chars per component max)
      -> 'Move_64x6_png/trai-4-of-10.tfrecords'

  4- Truncate result, keeping prefix: 'abc_def_ghi_jkl' -> 'abc_def'

  Args:
    url: string, url to sanitize and shorten.
    max_length: int, max length of result.

  Returns:
    (string, string): sanitized and shorted url, file extension.
  """
  url = urllib.parse.urlparse(url)
  netloc = url.netloc
  for prefix in _NETLOC_COMMON_PREFIXES:
    if netloc.startswith(prefix):
      netloc = netloc[len(prefix):]
  for suffix in _NETLOC_COMMON_SUFFIXES:
    if netloc.endswith(suffix):
      netloc = netloc[:-len(suffix)]
  url = '%s%s%s%s' % (netloc, url.path, url.params, url.query)
  # Get the extension:
  for ext in _KNOWN_EXTENSIONS:
    if url.endswith(ext):
      extension = ext
      url = url[:-len(extension)]
      break
  else:
    url, extension = os.path.splitext(url)
  max_length -= len(extension)
  # Replace non authorized chars (including '/') by '_':
  url = re.sub(r'[^a-zA-Z0-9\.\-_]+', '_', url)
  # Remove parts with no info:
  for common_part in _URL_COMMON_PARTS:
    url = url.replace(common_part, '_')
  url = url.strip('_')
  # Remove leading zeros in groups of numbers:
  url = re.sub('(?<![0-9])0+(?=[0-9])', '', url)
  # Decrease max size of URL components:
  c_size = max(len(c) for c in re.split(r'[\.\-_]', url))
  while c_size > 4 and len(url) > max_length:
    c_size -= 1
    url = re.sub(r'[^\.\-_]{4,}', lambda match: match.group(0)[:c_size], url)
  return url[:max_length], extension


def _get_fname(url, fhash=None):
  """Returns name of downloaded file (not as downloaded, but as stored).

  The max length of linux and windows filenames is 255 chars.
  Windows however expects short paths (260 chars), so we limit the file name
  to an arbitrary 90 chars.

  Naming pattern: '${url}${checksum}'.
   - url: url sanitized and shortened to 46 chars.
   - checksum: base64url encoded sha256: 44 chars (removing trailing '=').
     - sha256 of the file if known.
     - sha256 of url otherwise.

  Args:
    url: string, url of the file.
    fhash: optional string (hex), defaults to None. The sha256 hexdigest of file
      when known. If not given, sha256 of url is used.

  Returns:
    string of 90 chars max.
  """
  checksum = fhash or hashlib.sha256(tf.compat.as_bytes(url)).hexdigest()
  checksum = base64.urlsafe_b64encode(_decode_hex(checksum))
  checksum = tf.compat.as_text(checksum)[:-1]
  name, extension = _sanitize_url(url, max_length=46)
  return '%s%s%s' % (name, checksum, extension)


class Resource(object):
  """Represents a resource to download, extract, or both."""

  @api_utils.disallow_positional_args()
  def __init__(self,
               url=None,
               extract_method=None,
               path=None):
    """Resource constructor.

    Args:
      url: `str`, the URL at which to download the resource.
      extract_method: `ExtractMethod` to be used to extract resource. If
        not set, will be guessed from downloaded file name `original_fname`.
      path: `str`, path of resource on local disk. Can be None if resource has
        not be downloaded yet. In such case, `url` must be set.
    """
    self.url = url
    self._sha256 = None
    self.path = path
    self._extract_method = extract_method
    self._fname = None
    self._original_fname = None  # Name of the file as downloaded.
    self._info = None  # The INFO dict, once known.

  @property
  def sha256(self):
    return self._sha256

  @sha256.setter
  def sha256(self, value):
    if self._sha256 != value:
      self._sha256 = value
      self._fname = None

  @property
  def fname(self):
    """Name of downloaded file (not as downloaded, but as stored)."""
    if self.path:
      return os.path.basename(self.path)
    if not self._fname:
      self._fname = _get_fname(self.url, self.sha256)
    return self._fname

  @property
  def extract_fname(self):
    """Name of extracted archive (file or directory)."""
    return '%s.%s' % (self.extract_method_name, self.fname)

  @property
  def extract_method(self):
    """Returns `ExtractMethod` to use on resource. Cannot be None."""
    if not self._extract_method:
      self._extract_method = _guess_extract_method(
          # no original_fname if extract is called directly (no URL).
          # We need to use the original_fname as much as possible for files
          # for which the url doesn't give extension (eg: drive).
          self._get_info() and self._get_original_fname() or self.fname)
    return self._extract_method

  @property
  def extract_method_name(self):
    """Returns the name (`str`) of the extraction method."""
    return ExtractMethod(self.extract_method).name

  @property
  def info_path(self):
    """Returns path (`str`) of INFO file associated with resource."""
    return '%s.INFO' % self.path

  def _get_info(self):
    """Returns info dict or None."""
    if not self._info:
      if not tf.io.gfile.exists(self.info_path):
        return None
      with tf.io.gfile.GFile(self.info_path) as info_f:
        self._info = json.load(info_f)
    return self._info

  def exists_locally(self):
    """Returns whether the resource exists locally, at `resource.path`."""
    # If INFO file doesn't exist, consider resource does NOT exist, as it would
    # prevent guessing the `extract_method`.
    return (self.path and tf.io.gfile.exists(self.path) and
            tf.io.gfile.exists(self.info_path))

  def _get_original_fname(self):
    # We rely on the INFO file because some urls (eg: drive) do not contain the
    # name of original file.
    info = self._get_info()
    if not info:
      raise AssertionError('INFO file %s doe not exist.' % self.info_path)
    return info['original_fname']

  # TODO(pierrot): one lock per info path instead of locking everything.
  @util.build_synchronize_decorator()
  def write_info_file(self, dataset_name, original_fname):
    """Write the INFO file next to local file.

    Although the method is synchronized, there is still a risk two processes
    running at the same time overlap here. Risk accepted, since potentially lost
    data (`dataset_name`) is only for human consumption.

    Args:
      dataset_name: data used to dl the file.
      original_fname: name of file as downloaded.
    """
    info = self._get_info() or {}
    urls = set(info.get('urls', []) + [self.url])
    dataset_names = info.get('dataset_names', [])
    if dataset_name:
      dataset_names.append(dataset_name)
    if 'original_fname' in info and info['original_fname'] != original_fname:
      raise AssertionError(
          '`original_fname` "%s" stored in %s does NOT match "%s".' % (
              info['original_fname'], self.info_path, original_fname))
    info = dict(urls=list(urls), dataset_names=list(set(dataset_names)),
                original_fname=original_fname)
    with py_utils.atomic_write(self.info_path, 'w') as info_f:
      json.dump(info, info_f, sort_keys=True)
    self._info = info
