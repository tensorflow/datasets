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
import types
from typing import Any, Iterator, Optional, Tuple


@dataclasses.dataclass
class LazyModule:
  """Module loaded lazily during first call."""

  module_name: str
  module: Optional[types.ModuleType] = None
  fromlist: Optional[Tuple[str, ...]] = ()

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
      module_name = f'{self.module_name}.{name}'
      return self.from_cache(module_name=module_name)
    if self.module is None:  # Load on first call
      self.module = importlib.import_module(self.module_name)
    return getattr(self.module, name)


@contextlib.contextmanager
def lazy_imports() -> Iterator[None]:
  """Context Manager which lazy loads packages.

  Their import is not executed immediately, but is postponed to the first
  call of one of their attributes.

  Warning: mind current implementation's limitations:

  - You can only lazy load modules (`from x import y` will not work if `y` is a
    constant or a function or a class).
  - You cannot `import x.y` if `y` is not imported in the `x/__init__.py`.

  Usage:

  ```python
  from tensorflow_datasets.core import utils

  with utils.lazy_imports():
    import tensorflow as tf
  ```

  Yields:
    None
  """
  # Need to mock `__import__` (instead of `sys.meta_path`, as we do not want
  # to modify the `sys.modules` cache in any way)
  original_import = builtins.__import__
  try:
    builtins.__import__ = _lazy_import
    yield
  finally:
    builtins.__import__ = original_import


def _lazy_import(
    name: str,
    globals_=None,
    locals_=None,
    fromlist: tuple[str, ...] = (),
    level: int = 0,
):
  """Mock of `builtins.__import__`."""
  del globals_, locals_  # Unused

  if level:
    raise ValueError(f'Relative import statements not supported ({name}).')

  if not fromlist:
    # import x.y.z
    # import x.y.z as z
    # In that case, Python would usually import the entirety of `x` if each
    # submodule is imported in its parent's `__init__.py`. So we do the same.
    root_name = name.split('.')[0]
    return LazyModule.from_cache(module_name=root_name)
  else:
    # from x.y.z import a, b
    return LazyModule.from_cache(module_name=name, fromlist=fromlist)


with lazy_imports():
  import tensorflow as tf  # pylint: disable=g-import-not-at-top,unused-import

tensorflow = tf
