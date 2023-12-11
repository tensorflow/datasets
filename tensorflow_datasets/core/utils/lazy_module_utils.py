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

"""Lazy module utils."""

import builtins
import contextlib
import functools
import importlib
import logging
from typing import Any, Callable, ContextManager, Dict, Tuple

ContextManager = Callable[[], ContextManager[Any]]
ModuleApi = Dict[str, str]


class _EmptyModule:
  """Empty module used during mocking."""

  def __getattr__(self, _: str) -> Any:
    pass


def _lazy_module(
    name: str,
    globals_=None,
    locals_=None,
    fromlist: Tuple[str, ...] = (),
    level: int = 0,
    *,
    module_api: ModuleApi,
    context_manager: ContextManager,
):
  """Mock of `builtins.__import__`."""
  del globals_, locals_  # Unused
  if level:
    raise ValueError(f"Relative import statements not supported ({name}).")
  if not fromlist:
    root_name = name.split(".")[0]
    module_api[root_name] = name
  else:
    for element in fromlist:
      module_api[element] = name
  return _EmptyModule()


def module_getattr(
    name: str, module_api: ModuleApi, context_manager: ContextManager
) -> Any:
  if name not in module_api:
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
  module_name = module_api[name]
  with context_manager():
    module = importlib.import_module(module_name)
  return getattr(module, name)


@contextlib.contextmanager
def lazy_module(
    globals_, context_manager: ContextManager = contextlib.nullcontext
):
  """Context Manager which lazy loads modules.

  Their import is not executed immediately, but is postponed to the first
  call of one of their attributes.

  Usage:

  ```python
  from tensorflow_datasets.core.utils.lazy_module_utils import lazy_module

  with lazy_module(globals()):
    from tensorflow_datasets.testing import mock_data
  ```

  Args:
    globals_: pass globals() as an argument.
    context_manager: An optional context manager to execute when the module is
      actually imported.

  Yields:
    None
  """
  original_import = builtins.__import__
  module_api: ModuleApi = {}

  try:
    builtins.__import__ = functools.partial(
        _lazy_module, module_api=module_api, context_manager=context_manager
    )
    yield
  except Exception as exception:
    logging.exception(exception)
    raise exception
  finally:
    all_ = list(module_api)
    # Remove loaded _EmptyModules from globals().
    for element in module_api:
      if element in globals_:
        del globals_[element]
    # Overwrite __all__ / __dir__ / __getattr__ on the module.
    globals_["__all__"] = all_
    globals_["__dir__"] = lambda: all_
    globals_["__getattr__"] = functools.partial(
        module_getattr,
        module_api=module_api,
        context_manager=context_manager,
    )
    builtins.__import__ = original_import
