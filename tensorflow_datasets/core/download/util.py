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

"""Utils functions.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import datetime
import functools
import hashlib
import random
import string
import threading

import enum
import pytz
from six.moves import urllib
import tensorflow as tf


class GenerateMode(enum.Enum):
  """Enum for the different version conflict resolution modes."""

  # The generations modes:
  #                          |     Cache     |    Dataset
  # -----------------------------------------------
  # Reuse dataset if exists  |     Reuse     |     Reuse
  # Reuse cache if exists    |     Reuse     |  New version
  # Force Re-Download        |  Re-download  |  New version

  # Generate a new version of the dataset from scratch (download included)
  FORCE_REDOWNLOAD = 'force_redownload'
  # Generate a new version of the dataset, but reuse cached downloads if
  # they exists
  REUSE_CACHE_IF_EXISTS = 'reuse_cache_if_exists'
  # Do nothing if the dataset already exists (default mode)
  REUSE_DATASET_IF_EXISTS = 'reuse_dataset_if_exists'


# TODO(epot): Move some of those functions into core.py_utils


def build_log(prefix):
  """Create a f-string compatible logging function with prefix."""

  def log(msg, *args, **kwargs):
    msg = '{}: {}'.format(prefix, msg.format(*args, **kwargs))
    tf.logging.info(msg)

  return log


def rchop(s, pattern):
  """Remove the substring from the end of the string."""
  if not s.endswith(pattern):
    raise ValueError('{} not found in {}'.format(pattern, s))
  return s[:-len(pattern)]


def lchop(s, pattern):
  """Remove the substring from the end of the string."""
  if not s.startswith(pattern):
    raise ValueError('{} not found in {}'.format(pattern, s))
  return s[len(pattern):]


def build_synchronize_decorator():
  """Returns a decorator which prevent concurents calls to functions.

  Usage:
    synchronized = build_synchronize_decorator()

    @synchronized
    def read_value():
      ...

    @synchronized
    def write_value(x):
      ...

  Returns:
    make_threadsafe (fct): The decorator which lock all functions to which it
      is applied under a same lock
  """
  lock = threading.Lock()

  def lock_decorator(fn):

    @functools.wraps(fn)
    def lock_decorated(*args, **kwargs):
      with lock:
        return fn(*args, **kwargs)

    return lock_decorated

  return lock_decorator


def replace_timezone(dt_obj, tzinfo, is_dst=False):
  """Wrapper function for the standard datetime.datetime.replace(tzinfo=) call.

  pytz timezone object cannot be specified as an argument to
  datetime.datetime.replace(tzinfo=).
  This function works for both pytz and non-pytz timezone objects.
  Note that this function does not convert time between timezones.  You need to
  use datetime.datetime.astimezone() for that purpose (astimezone() works with
  both pytz and non-pytz timezone objects).

  Args:
    dt_obj: datetime.datetime object. Can be either naive or timezone-aware.
    tzinfo: Timezone object, can be either pytz or not.
    is_dst: Whether the time is in daylight saving or not.
            Used only for pytz and effective only for ambiguous time at the end
              of daylight saving time.

  Returns:
    A datetime.datetime object with replaced timezone info.  Old timezone info
    (if exist) is simply discarded.
    In most cases, other fields are remain unchanged (i.e., no conversion is
    done).

  Raises:
    pytz.exceptions.AmbiguousTimeError if is_dst=None, and the time is
    ambiguous.
    pytz.exceptions.NonExistentTimeError if is_dst=None, and the time is
    non-existent.
  """

  if hasattr(tzinfo, 'localize'):
    return tzinfo.localize(dt_obj.replace(tzinfo=None), is_dst)
  else:
    return dt_obj.replace(tzinfo=tzinfo)   # pylint: disable=g-tzinfo-replace


def pb_to_datetime(pb):
  """Convert a Timestamp protobuff into a standard UTC datetime object."""
  return replace_timezone(
      pb.ToDatetime(),
      pytz.timezone('UTC'),
  )


# Bellow are helper function to compose the URI key with the right properties (
# human readable, unique to avoid collisions, sorted by date,...)


def escape_uri(uri):
  """Extract uri name (for more explicit key)."""
  def escape_str(str_):
    allowed_chars = string.ascii_letters + string.digits + '.-_'
    return ''.join(c if c in allowed_chars else '+' for c in str_)

  parse_results = urllib.parse.urlparse(uri)
  return '{}_{}'.format(
      escape_str(parse_results.netloc.split(':')[0]),
      escape_str(parse_results.path.split('/')[-1]),
  )


def hash_uri(uri):
  """Hash of the URI string."""
  # Should use base64 instead of hex for shorter string.
  uri = tf.compat.as_bytes(uri)  # Python 3 require explicit encoding
  return hashlib.sha256(uri).hexdigest()[:5]


def time_str():
  """Time string (current UTC datetime, precise to the second)."""
  curr_date = datetime.datetime.now()
  return curr_date.strftime('%Y%m%d_%H%M%S')


def random_str():
  """Random string (for unicity)."""
  txt = [random.choice(string.ascii_letters + string.digits) for _ in range(5)]
  return ''.join(txt)
