# coding=utf-8
# Copyright 2023 The TensorFlow Datasets Authors.
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
from typing import Any, Callable, Iterator, Optional, Tuple, Type, Union

from absl import flags

Callback = Callable[..., None]

ClassOrFunction = Union[Type[Any], Callable[..., Any]]

# This flag allows to use regular imports instead of lazy imports. This is
# important when generating the documentation for example, where we want the
# actual classes/functions/modules rather than LazyModules.
_USE_LAZY_IMPORTS = flags.DEFINE_boolean(
    "tfds_use_lazy_imports",
    True,
    "If False, all imports are regular imports without lazy imports.",
)


@dataclasses.dataclass
class LazyModule:
  """Module loaded lazily during first call."""

  module_name: str
  module: Optional[types.ModuleType] = None
  class_or_function: Optional[ClassOrFunction] = None
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
    return LazyModule(**kwargs)

  def _import_class_or_function(self, module_name: str) -> ClassOrFunction:
    """Imports when `module_name` is known to be a class or a function."""
    if "." not in module_name:
      raise ImportError("Cannot import a function that is not in a module.")
    # If the import is "from x.y import some_function", then we have:
    # * module_name = "x.y"
    # * function_name = "some_function"
    function_name = module_name.split(".")[-1]
    module_name = ".".join(module_name.split(".")[:-1])
    module = self._import_module(module_name)
    return getattr(module, function_name)

  def _import_module(self, module_name: str) -> types.ModuleType:
    """Imports module name when `module_name` is known to be a module."""
    try:
      start_import_time = time.perf_counter()
      module = importlib.import_module(module_name)
      import_time_ms = (time.perf_counter() - start_import_time) * 1000
      if self.success_callback is not None:
        self.success_callback(
            import_time_ms=import_time_ms,
            module=module,
            module_name=module_name,
        )
      return module
    except ImportError as exception:
      if self.error_callback is not None:
        self.error_callback(exception=exception, module_name=module_name)
      raise exception

  def __call__(self, *args: Any, **kwargs: Any) -> Any:
    """Overwrites __call__ if the LazyModule is a class or a function."""
    if self.class_or_function is None:  # Load on first call
      self.class_or_function = self._import_class_or_function(self.module_name)
    return self.class_or_function(*args, **kwargs)

  def __instancecheck__(self, instance):
    """Overwrites instance check for lazily-loaded classes."""
    if self.class_or_function is None:  # Load on first call
      self.class_or_function = self._import_class_or_function(self.module_name)
    return isinstance(instance, self.class_or_function)

  def __mro_entries__(self, bases):
    """Overwrites MRO entries for lazily-loaded classes.

    This is needed to not inherit from LazyModule.

    Args:
      bases: bases parameter of
        https://docs.python.org/3/reference/datamodel.html#resolving-mro-entries.

    Returns:
      The actual base class to inherit from.
    """
    if self.class_or_function is None:  # Load on first call
      self.class_or_function = self._import_class_or_function(self.module_name)
    return (self.class_or_function,)

  def __getattr__(self, name: str) -> Any:
    """Overwrites x.y if the LazyModule is a module."""
    if name in self.fromlist:
      module_name = f"{self.module_name}.{name}"
      return self.from_cache(
          module_name=module_name,
          module=self.module,
          fromlist=self.fromlist,
          error_callback=self.error_callback,
          success_callback=self.success_callback,
      )
    # Load on first call
    if self.module is None and self.class_or_function is None:
      try:
        self.module = self._import_module(self.module_name)
      # If we try to import a function/class rather than a module,
      # _import_module raises a ModuleNotFoundError.
      except ModuleNotFoundError:
        self.class_or_function = self._import_class_or_function(
            self.module_name
        )
    module_or_class_or_function = self.module or self.class_or_function
    return getattr(module_or_class_or_function, name)


@contextlib.contextmanager
def lazy_imports(
    error_callback: Optional[Callback] = None,
    success_callback: Optional[Callback] = None,
) -> Iterator[None]:
  """Context Manager which lazy loads packages.

  Their import is not executed immediately, but is postponed to the first
  call of one of their attributes.

  Warning: mind current implementation's limitations:

  - You cannot lazy load constants (`from x import y` will not work if `y` is a
    constant). You can only lazy load modules, functions and classes.
  - You cannot `import x.y` if `y` is not imported in the `x/__init__.py`.
  - `lazy_imports` was tested in the context of TFDS. Edge cases that do not
    appear in TFDS codebase may not be covered. Notably, we may not have
    implemented all dunder method in LazyMethod, but only those required for
    TFDS usage for now.

  Usage:

  ```python
  from tensorflow_datasets.core.utils.lazy_imports_utils import lazy_imports

  with lazy_imports():
    import tensorflow as tf
  ```

  Args:
    error_callback: a callback to trigger when an import fails. The callback is
      passed kwargs containing: 1) exception (ImportError): the exception that
      was raised after the error; 2) module_name (str): the name of the imported
      module.
    success_callback: a callback to trigger when an import succeeds. The
      callback is passed kwargs containing: 1) import_time_ms (float): the
      import time (in milliseconds); 2) module (ModuleType): the imported
      module; 3) module_name (str): the name of the imported module.

  Yields:
    None
  """
  # Need to mock `__import__` (instead of `sys.meta_path`, as we do not want
  # to modify the `sys.modules` cache in any way)
  original_import = builtins.__import__
  # `lazy_imports` often comes at the beginning so flags may not be parsed yet:
  try:
    use_lazy_imports = _USE_LAZY_IMPORTS.value
  except flags.UnparsedFlagAccessError:
    use_lazy_imports = True
  try:
    if use_lazy_imports:
      builtins.__import__ = functools.partial(
          _lazy_import,
          error_callback=error_callback,
          success_callback=success_callback,
      )
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
        success_callback=success_callback,
    )
  # from x.y.z import a, b
  return LazyModule.from_cache(
      module_name=name,
      fromlist=fromlist,
      error_callback=error_callback,
      success_callback=success_callback,
  )


def tf_error_callback(**kwargs):
  del kwargs
  print("\n\n***************************************************************")
  print(
      "Failed to import TensorFlow. Please note that TensorFlow is not "
      "installed by default when you install TFDS. This allows you "
      "to choose to install either `tf-nightly` or `tensorflow`. "
      "Please install the most recent version of TensorFlow, by "
      "following instructions at https://tensorflow.org/install."
  )
  print("***************************************************************\n\n")


MIN_TF_VERSION = "2.1.0"

_ensure_tf_version_called = False


# Ensure TensorFlow version is sufficiently recent. This needs to happen after
# TensorFlow was imported, as it is referenced.
def ensure_tf_version(**kwargs):
  """Ensures TensorFlow version is sufficient."""
  # Only check the first time.
  global _ensure_tf_version_called
  if _ensure_tf_version_called:
    return
  _ensure_tf_version_called = True

  tf_version = kwargs["module"].__version__
  if tf_version < MIN_TF_VERSION:
    raise ImportError(
        "This version of TensorFlow Datasets requires TensorFlow "
        f"version >= {MIN_TF_VERSION}; Detected an installation of version "
        f"{tf_version}. Please upgrade TensorFlow to proceed."
    )


def array_record_error_callback(**kwargs):
  del kwargs
  print("\n\n***************************************************************")
  print(
      "Failed to import ArrayRecord. This probably means that you are running"
      " on macOS or Windows. ArrayRecord currently does not work for your"
      " infrastructure, because it uses Python bindings in C++. We are actively"
      " working on this issue. Thanks for your understanding."
  )
  print("***************************************************************\n\n")


with lazy_imports(
    error_callback=tf_error_callback, success_callback=ensure_tf_version
):
  import tensorflow as tf  # pylint: disable=g-import-not-at-top,unused-import  # pytype: disable=import-error


with lazy_imports(error_callback=array_record_error_callback):
  from array_record.python import array_record_data_source  # pylint: disable=g-import-not-at-top,unused-import
  from array_record.python import array_record_module  # pylint: disable=g-import-not-at-top,unused-import

tensorflow = tf
