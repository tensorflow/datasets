# coding=utf-8
# Copyright 2021 The TensorFlow Datasets Authors.
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

"""Stable hashing function using md5.

Note that the properties we are looking at here are:
 1- Good distribution of hashes (random uniformity);
 2- Speed;
 3- Availability as portable library, giving the same hash independently of
 platform.

Crypto level hashing is not a requirement.

A bit of history:
 - CityHash was first used. However the C implementation used complex
 instructions and was hard to compile on some platforms.
 - Siphash was chosen as a replacement, because although being slower,
 it has a simpler implementation and it has a pure Python implementation, making
 it easier to distribute TFDS on Windows or MAC. However, the used library
 (reference C implementation wrapped using cffi) crashed the python interpreter
 on py3 with tf1.13.
 - So md5, although being slower that the two above works everywhere and is
 still faster than a pure python implementation of siphash.

Changing the hash function should be done thoughfully, as it would change the
order of datasets (and thus sets of records when using slicing API). If done,
all datasets would need to have their major version bumped.

Note that if we were to find a dataset for which two different keys give the
same hash (collision), a solution could be to append the key to its hash.

The split name is being used as salt to avoid having the same keys in two splits
result in same order.
"""

import hashlib
from typing import Union

import numpy as np

HashKey = Union[str, bytes, int, np.ndarray]


def _to_bytes(data: HashKey) -> bytes:
  """Converts the key to bytes."""
  if isinstance(data, bytes):
    return data
  elif isinstance(data, str):
    # For windows compatibility, we normalize the key in case a
    # filepath is passed as key ('path\\to\\file' -> 'path/to/file')
    data = data.replace('\\', '/')
  elif isinstance(data, int):
    data = str(data)
  elif isinstance(data, np.ndarray) and data.size == 1:  # Singleton array
    return _to_bytes(data.item())
  else:
    raise TypeError(f'Invalid key type: {data!r} ({type(data)})')
  return data.encode('utf-8')


class Hasher(object):
  """Hasher: to initialize a md5 with salt."""

  def __init__(self, salt):
    self._md5 = hashlib.md5(_to_bytes(salt))

  def hash_key(self, key: HashKey) -> int:
    """Returns 128 bits hash of given key.

    Args:
      key (bytes, string or anything convertible to a string): key to be hashed.
        If the key is a string, it will be encoded to bytes using utf-8. If the
        key is neither a string nor bytes, it will be converted to a str, then
        to bytes. This means that `"1"` (str) and `1` (int) will have the same
        hash. The intent of the hash being to shuffle keys, it is recommended
        that all keys of a given set to shuffle use a single type.

    Returns:
      128 bits integer, hash of key.
    """
    md5 = self._md5.copy()
    md5.update(_to_bytes(key))
    return int(md5.hexdigest(), 16)
