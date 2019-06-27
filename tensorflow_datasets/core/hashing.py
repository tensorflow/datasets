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

"""Stable hashing function using SipHash (https://131002.net/siphash/).

Note that the properties we are looking at here are:
 1- Good distribution of hashes;
 2- Speed;
 3- Availability as portable library, giving the same hash independently of
 platform.

Crypto level hashing is not a requirement.

Although SipHash being slower than alternatives (eg: CityHash), its
implementation is simpler and it has a pure Python implementation, making it
easier to distribute TFDS on Windows or MAC. The speed cost being only paid at
data preparation time, portability wins.

Python3 uses SipHash internally, but since it is not exposed and `hash` function
is not guaranteed to use SipHash in the future, we have to import libraries.

Changing the hash function should be done thoughfully, as it would change the
order of datasets (and thus sets of records when using slicing API). If done,
all datasets would need to have their major version bumped.

Note that if we were to find a dataset for which two different keys give the
same hash (collision), a solution could be to append the key to its hash.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import struct

import siphash
import six

_CSIPHASH_AVAILABLE = False
try:
  import csiphash  # pylint: disable=g-import-not-at-top
  _CSIPHASH_AVAILABLE = True
except ImportError:
  pass

# SipHash needs a 16 bits key.
_SECRET = b'\0' * 16


def _siphash(data):
  if _CSIPHASH_AVAILABLE:
    hash_bytes = csiphash.siphash24(_SECRET, data)
    # Equivalent to `int.from_bytes(hash_bytes, sys.byteorder)` in py3,
    # but py2 compatible:
    return struct.unpack('<Q', hash_bytes)[0]
  else:
    return siphash.SipHash24(_SECRET, data).hash()


def hash_key(key):
  """Returns 64 bits hash of given key.

  Args:
    key (bytes, string or anything convertible to a string): key to be hashed.
      If the key is a string, it will be encoded to bytes using utf-8.
      If the key is neither a string nor bytes, it will be converted to a str,
        then to bytes.
      This means that `"1"` (str) and `1` (int) will have the same hash. The
      intent of the hash being to shuffle keys, it is recommended that all keys
      of a given set to shuffle use a single type.

  Returns:
    64 bits integer, hash of key.
  """
  if not isinstance(key, (six.string_types, bytes)):
    key = str(key)
  if not isinstance(key, bytes):
    key = key.encode('utf-8')
  return _siphash(key)

