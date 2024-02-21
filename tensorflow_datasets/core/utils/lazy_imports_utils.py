# coding=utf-8
# Copyright 2022 The TensorFlow Datasets Authors.
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

"""Lazy import utils.
"""

from __future__ import annotations

import builtins
import contextlib
import dataclasses
import functools
import importlib
import time
import types
from typing import Any, Callable, Iterator, Optional, Tuple

from tensorflow_datasets.core.tf_compat import ensure_tf_version

Callback = Callable[..., None]


@dataclasses.dataclass
class LazyModule:
  """Module loaded lazily during first call."""

  module_name: str
  module: Optional[types.ModuleType] = None
  fromlist: Optional[Tuple[str, ...]] = ()
  error_callback: Optional[Callback] = None
  success_callback: Optional[Callback] = None

  @classmethod
  @functools.lru_cache(maxsize=None)
  def from_cache(cls, **kwargs):
    """Factory to cache all instances of module.

    Note: The cache is global to all instances of the
    `lazy_imports` context manager.

    Args:
      **kwargs: Init kwargs

    Returns:
      New object
    """
    return cls(**kwargs)

  def __getattr__(self, name: str) -> Any:
    if name in self.fromlist:
      module_name = f"{self.module_name}.{name}"
      return self.from_cache(module_name=module_name)
    if self.module is None:  # Load on first call
      try:
        start_import_time = time.perf_counter()
        self.module = importlib.import_module(self.module_name)
        import_time_ms = (time.perf_counter() - start_import_time) * 1000
        if self.success_callback is not None:
          self.success_callback(
              import_time_ms=import_time_ms,
              module=self.module,
              module_name=self.module_name)
      except ImportError as exception:
        if self.error_callback is not None:
          self.error_callback(exception=exception, module_name=self.module_name)
        raise exception
    return getattr(self.module, name)


@contextlib.contextmanager
def lazy_imports(error_callback: Optional[Callback] = None,
                 success_callback: Optional[Callback] = None) -> Iterator[None]:
  """Context Manager which lazy loads packages.

  Their import is not executed immediately, but is postponed to the first
  call of one of their attributes.

  Warning: mind current implementation's limitations:

  - You can only lazy load modules (`from x import y` will not work if `y` is a
    constant or a function or a class).
  - You cannot `import x.y` if `y` is not imported in the `x/__init__.py`.

  Usage:

  ```python
  from tensorflow_datasets.core.utils.lazy_imports_utils import lazy_imports

  with lazy_imports():
    import tensorflow as tf
  ```

  Args:
    error_callback: a callback to trigger when an import fails. The
      callback is passed kwargs containing: 1) exception (ImportError): the
      exception that was raised after the error; 2) module_name (str): the name
      of the imported module.
    success_callback: a callback to trigger when an import succeeds. The
      callback is passed kwargs containing: 1) import_time_ms (float): the
      import time (in milliseconds); 2) module (Any): the imported module;
      3) module_name (str): the name of the imported module.

  Yields:
    None
  """
  # Need to mock `__import__` (instead of `sys.meta_path`, as we do not want
  # to modify the `sys.modules` cache in any way)
  original_import = builtins.__import__
  try:
    builtins.__import__ = functools.partial(
        _lazy_import,
        error_callback=error_callback,
        success_callback=success_callback)
    yield
  finally:
    builtins.__import__ = original_import


def _lazy_import(
    name: str,
    globals_=None,
    locals_=None,
    fromlist: tuple[str, ...] = (),
    level: int = 0,
    *,
    error_callback: Optional[Callback],
    success_callback: Optional[Callback],
):
  """Mock of `builtins.__import__`."""
  del globals_, locals_  # Unused

  if level:
    raise ValueError(f"Relative import statements not supported ({name}).")

  if not fromlist:
    # import x.y.z
    # import x.y.z as z
    # In that case, Python would usually import the entirety of `x` if each
    # submodule is imported in its parent's `__init__.py`. So we do the same.
    root_name = name.split(".")[0]
    return LazyModule.from_cache(
        module_name=root_name,
        error_callback=error_callback,
        success_callback=success_callback)
  # from x.y.z import a, b
  return LazyModule.from_cache(
      module_name=name,
      fromlist=fromlist,
      error_callback=error_callback,
      success_callback=success_callback)


def tf_error_callback():
  print("\n\n***************************************************************")
  print("Failed to import TensorFlow. Please note that TensorFlow is not "
        "installed by default when you install TFDS. This allows you "
        "to choose to install either `tf-nightly` or `tensorflow`. "
        "Please install the most recent version of TensorFlow, by "
        "following instructions at https://tensorflow.org/install.")
  print("***************************************************************\n\n")


def tf_success_callback(**kwargs):
  ensure_tf_version(kwargs["module"])


with lazy_imports(
    error_callback=tf_error_callback, success_callback=tf_success_callback):
  import tensorflow as tf  # pylint: disable=g-import-not-at-top,unused-import

tensorflow = tf
