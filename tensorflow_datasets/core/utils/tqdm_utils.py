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

"""Wrapper around tqdm."""

import contextlib
import os

from tqdm import auto as tqdm_lib


class TqdmStream:
  """File-object-like abstraction which wrap`tqdm.write`.

  By default using `logging.info` inside a `tqdm` scope creates visual
  artifacts. This simple wrapper uses `tqdm.write` instead.

  Usage:

  ```python
  logger = logging.getLogger()
  logger.addHandler(logging.StreamHandler(TqdmStream()))

  for _ in tqdm.tqdm(range(10)):
    logger.info('No visual artifacts')
  ```

  """

  def write(self, x):
    tqdm_lib.tqdm.write(x, end='')

  def flush(self):
    pass

  def close(self):
    pass


class EmptyTqdm(object):
  """Dummy tqdm which doesn't do anything."""

  def __init__(self, *args, **kwargs):  # pylint: disable=unused-argument
    self._iterator = args[0] if args else None

  def __iter__(self):
    return iter(self._iterator)

  def __getattr__(self, _):
    """Return empty function."""

    def empty_fn(*args, **kwargs):  # pylint: disable=unused-argument
      return

    return empty_fn

  def __enter__(self):
    return self

  def __exit__(self, type_, value, traceback):
    return


_active = True
# Disable progression bar when TFDS is executed inside TF kokoro documentation
# infrastructure. Otherwise it creates visual artifacts in the notebook output
# of the documentation pages.
if 'TF_DOCS_INFRA_KOKORO' in os.environ:
  _active = False


def tqdm(*args, **kwargs):
  if _active:
    return tqdm_lib.tqdm(*args, **kwargs)
  else:
    return EmptyTqdm(*args, **kwargs)


def async_tqdm(*args, **kwargs):
  if _active:
    return _async_tqdm(*args, **kwargs)
  else:
    return EmptyTqdm(*args, **kwargs)


def display_progress_bar(enable: bool) -> None:
  """Controls whether Tqdm progress bar is enabled/disabled.

  Usage:

  ```
  tfds.display_progress_bar(enable=True)
  ```

  Args:
    enable: whether to display the progress bar.
  """
  # Replace tqdm
  global _active
  _active = enable


def disable_progress_bar():
  """Disables Tqdm progress bar.

  Usage:

  ```
  tfds.disable_progress_bar()
  ```

  """
  # Replace tqdm
  global _active
  _active = False


def enable_progress_bar():
  """Enables Tqdm progress bar.

  Usage:

  ```
  tfds.enable_progress_bar()
  ```

  """
  # Replace tqdm
  global _active
  _active = True


@contextlib.contextmanager
def _async_tqdm(*args, **kwargs):
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
  with tqdm_lib.tqdm(*args, **kwargs) as pbar:
    pbar = _TqdmPbarAsync(pbar)
    yield pbar
    pbar.clear()  # pop pbar from the active list of pbar


class _TqdmPbarAsync(object):
  """Wrapper around Tqdm pbar which be shared between thread."""
  _tqdm_bars = []

  def __init__(self, pbar):
    self._lock = tqdm_lib.tqdm.get_lock()
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
