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

"""Wrapper around tqdm.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib

from tqdm import auto as tqdm_lib

tqdm = tqdm_lib.tqdm


@contextlib.contextmanager
def async_tqdm(*args, **kwargs):
  """Wrapper around Tqdm which can be updated in threads.

  Usage:

  ```
  with utils.async_tqdm(...) as pbar:
    # pbar can then be modified inside a thread
    # pbar.update_total(3)
    # pbar.update()
  ```

  Args:
    *args: args of tqdm
    **kwargs: kwargs of tqdm

  Yields:
    pbar: Async pbar which can be shared between threads.
  """
  with tqdm(*args, **kwargs) as pbar:
    pbar = _TqdmPbarAsync(pbar)
    yield pbar
    pbar.clear()  # pop pbar from the active list of pbar
    print()  # Avoid the next log to overlapp with the bar


class _TqdmPbarAsync(object):
  """Wrapper around Tqdm pbar which be shared between thread."""
  _tqdm_bars = []

  def __init__(self, pbar):
    self._lock = tqdm.get_lock()
    self._pbar = pbar
    self._tqdm_bars.append(pbar)

  def update_total(self, n=1):
    """Increment total pbar value."""
    with self._lock:
      self._pbar.total += n
      self.refresh()

  def update(self, n=1):
    """Increment current value."""
    with self._lock:
      self._pbar.update(n)
      self.refresh()

  def refresh(self):
    """Refresh all."""
    for pbar in self._tqdm_bars:
      pbar.refresh()

  def clear(self):
    """Remove the tqdm pbar from the update."""
    self._tqdm_bars.pop()

