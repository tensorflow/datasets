# coding=utf-8
# Copyright 2024 The TensorFlow Datasets Authors.
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

"""Some python utils function and classes."""

from __future__ import annotations

import base64
from collections.abc import Iterator, Sequence
import contextlib
import functools
import io
import itertools
import logging
import os
import re
import shutil
import sys
import textwrap
import threading
import typing
from typing import Any, Callable, NoReturn, Type, TypeVar
import uuid

from absl import logging as absl_logging
from etils import epath
from etils import epy
from tensorflow_datasets.core import constants
from tensorflow_datasets.core.utils import type_utils

with epy.lazy_imports():
  # pylint: disable=g-import-not-at-top
  from six.moves import urllib
  # pylint: enable=g-import-not-at-top


Tree = type_utils.Tree

# NOTE: When used on an instance method, the cache is shared across all
# instances and IS NOT per-instance.
# See
# https://stackoverflow.com/questions/14946264/python-lru-cache-decorator-per-instance
# For @property methods, use @memoized_property below.
memoize = functools.lru_cache

T = TypeVar('T')
U = TypeVar('U')

Fn = TypeVar('Fn', bound=Callable[..., Any])
# Regular expression to match strings that are not valid Python/TFDS names:
_INVALID_TFDS_NAME_CHARACTER = re.compile(r'[^a-zA-Z0-9_]')


def is_notebook() -> bool:
  """Returns True if running in a notebook (Colab, Jupyter) environment."""
  # Inspired from the tqdm autonotebook code
  try:
    # Use sys.module as we do not want to trigger import
    IPython = sys.modules['IPython']  # pylint: disable=invalid-name
    if 'IPKernelApp' not in IPython.get_ipython().config:
      return False  # Run in a IPython terminal
  except:  # pylint: disable=bare-except
    return False
  else:
    return True


# TODO(tfds): Should likely have a `logging_utils` wrapper around `absl.logging`
# so logging messages are displayed on Colab.


def print_notebook(*args: Any) -> None:
  """Like `print`/`logging.info`. Colab do not print stderr by default."""
  msg = ' '.join([str(x) for x in args])
  if is_notebook():
    print(msg)
  else:
    absl_logging.info(msg)


def warning(text: str) -> None:
  if is_notebook():
    print(text)
  else:
    absl_logging.warning(text)


@contextlib.contextmanager
def temporary_assignment(obj, attr, value):
  """Temporarily assign obj.attr to value."""
  original = getattr(obj, attr)
  setattr(obj, attr, value)
  try:
    yield
  finally:
    setattr(obj, attr, original)


def zip_dict(*dicts):
  """Iterate over items of dictionaries grouped by their keys."""
  for key in set(itertools.chain(*dicts)):  # set merge all keys
    # Will raise KeyError if the dict don't have the same keys
    yield key, tuple(d[key] for d in dicts)


@contextlib.contextmanager
def disable_logging():
  """Temporarily disable the logging."""
  logger = logging.getLogger()
  logger_disabled = logger.disabled
  logger.disabled = True
  try:
    yield
  finally:
    logger.disabled = logger_disabled


class NonMutableDict(dict[T, U]):
  """Dict where keys can only be added but not modified.

  Raises an error if a key is overwritten. The error message can be customized
  during construction. It will be formatted using {key} for the overwritten key.
  """

  def __init__(self, *args, **kwargs):
    self._error_msg = kwargs.pop(
        'error_msg',
        'Try to overwrite existing key: {key}',
    )
    if kwargs:
      raise ValueError('NonMutableDict cannot be initialized with kwargs.')
    super(NonMutableDict, self).__init__(*args, **kwargs)

  def __setitem__(self, key, value):
    if key in self.keys():
      raise ValueError(self._error_msg.format(key=key))
    return super(NonMutableDict, self).__setitem__(key, value)

  def update(self, other):  # pytype: disable=signature-mismatch  # overriding-parameter-count-checks
    if any(k in self.keys() for k in other):
      raise ValueError(self._error_msg.format(key=set(self) & set(other)))
    return super(NonMutableDict, self).update(other)


class classproperty(property):  # pylint: disable=invalid-name
  """Descriptor to be used as decorator for @classmethods."""

  def __get__(self, obj, objtype=None):
    return self.fget.__get__(None, objtype)()  # pytype: disable=attribute-error


if typing.TYPE_CHECKING:
  # TODO(b/171883689): There is likely a better way to annotate descriptors

  def classproperty(fn: Callable[[Type[Any]], T]) -> T:  # pylint: disable=function-redefined
    return fn(type(None))

  def memoized_property(fn: Callable[[Any], T]) -> T:  # pylint: disable=function-redefined
    return fn(None)


def map_nested(function, data_struct, dict_only=False, map_tuple=False):
  """Apply a function recursively to each element of a nested data struct."""

  # Could add support for more exotic data_struct, like OrderedDict
  if isinstance(data_struct, dict):
    return {
        k: map_nested(function, v, dict_only, map_tuple)
        for k, v in data_struct.items()
    }
  elif not dict_only:
    types_ = [list]
    if map_tuple:
      types_.append(tuple)
    if isinstance(data_struct, tuple(types_)):
      mapped = [
          map_nested(function, v, dict_only, map_tuple) for v in data_struct
      ]
      if isinstance(data_struct, list):
        return mapped
      else:
        return tuple(mapped)
  # Singleton
  return function(data_struct)


def zip_nested(arg0, *args, **kwargs):
  """Zip data struct together and return a data struct with the same shape."""
  # Python 2 do not support kwargs only arguments
  dict_only = kwargs.pop('dict_only', False)
  assert not kwargs

  # Could add support for more exotic data_struct, like OrderedDict
  if isinstance(arg0, dict):
    return {
        k: zip_nested(*a, dict_only=dict_only) for k, a in zip_dict(arg0, *args)
    }
  elif not dict_only:
    if isinstance(arg0, list):
      return [zip_nested(*a, dict_only=dict_only) for a in zip(arg0, *args)]
  # Singleton
  return (arg0,) + args


def flatten_nest_dict(d: type_utils.TreeDict[T]) -> dict[str, T]:
  """Return the dict with all nested keys flattened joined with '/'."""
  # Use NonMutableDict to ensure there is no collision between features keys
  flat_dict = NonMutableDict()
  for k, v in d.items():
    if isinstance(v, dict):
      for k2, v2 in flatten_nest_dict(v).items():
        flat_dict[f'{k}/{k2}'] = v2
    elif isinstance(v, list) and v and isinstance(v[0], dict):
      for k2 in v[0]:
        flat_dict[f'{k}/{k2}'] = [v[i][k2] for i in range(len(v))]
    else:
      flat_dict[k] = v
  return flat_dict


# Note: Could use `tree.flatten_with_path` instead, but makes it harder for
# users to compile from source.
def flatten_with_path(
    structure: Tree[T],
) -> Iterator[tuple[tuple[str | int, ...], T]]:  # pytype: disable=invalid-annotation
  """Convert a TreeDict into a flat list of paths and their values.

  ```py
  flatten_with_path({'a': {'b': v}}) == [(('a', 'b'), v)]
  ```

  Args:
    structure: Nested input structure

  Yields:
    The `(path, value)` tuple. With path being the tuple of `dict` keys and
      `list` indexes
  """
  if isinstance(structure, dict):
    key_struct_generator = sorted(structure.items())
  elif isinstance(structure, (list, tuple)):
    key_struct_generator = enumerate(structure)
  else:
    key_struct_generator = None  # End of recursion

  if key_struct_generator is not None:
    for key, sub_structure in key_struct_generator:
      # Recurse into sub-structures
      for sub_path, sub_value in flatten_with_path(sub_structure):
        yield (key,) + sub_path, sub_value
  else:
    yield (), structure  # Leaf, yield value


def dedent(text):
  """Wrapper around `textwrap.dedent` which also `strip()` and handle `None`."""
  return textwrap.dedent(text).strip() if text else text


def indent(text: str, indent: str) -> str:  # pylint: disable=redefined-outer-name
  text = dedent(text)
  return text.replace('\n', '\n' + indent)


def pack_as_nest_dict(flat_d, nest_d):
  """Pack a 1-lvl dict into a nested dict with same structure as `nest_d`."""
  nest_out_d = {}
  for k, v in nest_d.items():
    if isinstance(v, dict):
      v_flat = flatten_nest_dict(v)
      sub_d = {k2: flat_d.pop(f'{k}/{k2}', None) for k2, _ in v_flat.items()}
      # Recursively pack the dictionary
      nest_out_d[k] = pack_as_nest_dict(sub_d, v)
    elif isinstance(v, list) and v and isinstance(v[0], dict):
      first_inner_key = list(v[0].keys())[0]
      list_size = len(flat_d[f'{k}/{first_inner_key}'])
      nest_out_d[k] = [{} for _ in range(list_size)]
      for k2 in v[0].keys():
        subvals = flat_d.pop(f'{k}/{k2}', [])
        assert (
            len(subvals) == len(v) == list_size
        ), f'{subvals}, {v}, {list_size}'
        for i in range(list_size):
          nest_out_d[k][i][k2] = subvals[i]
    else:
      nest_out_d[k] = flat_d.pop(k, None)
  if flat_d:  # At the end, flat_d should be empty
    raise ValueError(
        'Flat dict strucure do not match the nested dict. Extra keys: '
        f'{list(flat_d.keys())}'
    )
  return nest_out_d


@contextlib.contextmanager
def nullcontext(enter_result: T = None) -> Iterator[T]:
  """Backport of `contextlib.nullcontext`."""
  yield enter_result


def _tmp_file_prefix() -> str:
  return f'{constants.INCOMPLETE_PREFIX}{uuid.uuid4().hex}'


def _tmp_file_name(path: epath.PathLike) -> epath.Path:
  path = epath.Path(path)
  return path.parent / f'{_tmp_file_prefix()}.{path.name}'


@contextlib.contextmanager
def incomplete_file(
    path: epath.Path,
) -> Iterator[epath.Path]:
  """Writes to path atomically, by writing to temp file and renaming it."""
  tmp_path = _tmp_file_name(path)
  try:
    yield tmp_path
    tmp_path.replace(path)
  finally:
    # Eventually delete the tmp_path if exception was raised
    tmp_path.unlink(missing_ok=True)


@contextlib.contextmanager
def incomplete_files(
    path: epath.Path,
) -> Iterator[epath.Path]:
  """Writes to path atomically, by writing to temp file and renaming it."""
  tmp_file_prefix = _tmp_file_prefix()
  tmp_path = path.parent / f'{tmp_file_prefix}.{path.name}'
  try:
    yield tmp_path
    # Rename all tmp files to their final name.
    for tmp_file in path.parent.glob(f'{tmp_file_prefix}.*'):
      file_name = tmp_file.name.removeprefix(tmp_file_prefix + '.')
      tmp_file.replace(path.parent / file_name)
  finally:
    # Eventually delete the tmp_path if exception was raised
    for tmp_file in path.parent.glob(f'{tmp_file_prefix}.*'):
      tmp_file.unlink(missing_ok=True)


def is_incomplete_file(path: epath.Path) -> bool:
  """Returns whether the given filename suggests that it's incomplete."""
  return bool(
      re.search(
          rf'^{re.escape(constants.INCOMPLETE_PREFIX)}[0-9a-fA-F]{{32}}\..+$',
          path.name,
      )
  )


@contextlib.contextmanager
def atomic_write(path: epath.PathLike, mode: str):
  """Writes to path atomically, by writing to temp file and renaming it."""
  path = epath.Path(path)
  tmp_path = _tmp_file_name(path)
  with tmp_path.open(mode=mode) as file_:
    yield file_
  path.unlink(missing_ok=True)
  tmp_path.rename(path)


def reraise(
    e: Exception,
    prefix: str | None = None,
    suffix: str | None = None,
) -> NoReturn:
  """Reraise an exception with an additional message."""
  prefix = prefix or ''
  suffix = '\n' + suffix if suffix else ''

  # If unsure about modifying the function inplace, create a new exception
  # and stack it in the chain.
  if (
      # Exceptions with custom error message
      type(e).__str__ is not BaseException.__str__
      # This should never happens unless the user plays with Exception
      # internals
      or not hasattr(e, 'args')
      or not isinstance(e.args, tuple)
  ):
    msg = f'{prefix}{e}{suffix}'
    # Could try to dynamically create a
    # `type(type(e).__name__, (ReraisedError, type(e)), {})`, but should be
    # carefull when nesting `reraise` as well as compatibility with external
    # code.
    # Some base exception class (ImportError, OSError) and subclasses (
    # ModuleNotFoundError, FileNotFoundError) have custom `__str__` error
    # message. We re-raise those with same type to allow except in caller code.
    if isinstance(e, (ImportError, OSError)):
      exception = type(e)(msg)
    else:
      exception = RuntimeError(f'{type(e).__name__}: {msg}')
    raise exception from e
  # Otherwise, modify the exception in-place
  elif len(e.args) <= 1:
    exception_msg = e.args[0] if e.args else ''
    e.args = (f'{prefix}{exception_msg}{suffix}',)
    raise  # pylint: disable=misplaced-bare-raise
  # If there is more than 1 args, concatenate the message with other args
  else:
    e.args = tuple(
        p for p in (prefix,) + e.args + (suffix,) if not isinstance(p, str) or p
    )
    raise  # pylint: disable=misplaced-bare-raise


@contextlib.contextmanager
def try_reraise(*args, **kwargs):
  """Context manager which reraise exceptions with an additional message.

  Contrary to `raise ... from ...` and `raise Exception().with_traceback(tb)`,
  this function tries to modify the original exception, to avoid nested
  `During handling of the above exception, another exception occurred:`
  stacktraces.

  Args:
    *args: Prefix to add to the exception message
    **kwargs: Prefix to add to the exception message

  Yields:
    None
  """
  try:
    yield
  except Exception as e:  # pylint: disable=broad-except
    reraise(e, *args, **kwargs)


def rgetattr(obj, attr, *args):
  """Get attr that handles dots in attr name."""

  def _getattr(obj, attr):
    return getattr(obj, attr, *args)

  return functools.reduce(_getattr, [obj] + attr.split('.'))


def has_sufficient_disk_space(needed_bytes, directory='.'):
  try:
    free_bytes = shutil.disk_usage(os.path.abspath(directory)).free
  except OSError:
    return True
  return needed_bytes < free_bytes


def get_class_path(cls, use_tfds_prefix=True):
  """Returns path of given class or object. Eg: `tfds.image.cifar.Cifar10`."""
  if not isinstance(cls, type):
    cls = cls.__class__
  module_path = cls.__module__
  if use_tfds_prefix and module_path.startswith('tensorflow_datasets'):
    module_path = 'tfds' + module_path[len('tensorflow_datasets') :]
  return '.'.join([module_path, cls.__name__])


def get_class_url(cls):
  """Returns URL of given class or object."""
  cls_path = get_class_path(cls, use_tfds_prefix=False)
  module_path, unused_class_name = cls_path.rsplit('.', 1)
  module_path = module_path.replace('.', '/')
  return constants.SRC_BASE_URL + module_path + '.py'


def build_synchronize_decorator() -> Callable[[Fn], Fn]:
  """Returns a decorator which prevents concurrent calls to functions.

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

  def lock_decorator(fn: Fn) -> Fn:
    @functools.wraps(fn)
    def lock_decorated(*args, **kwargs):
      with lock:
        return fn(*args, **kwargs)

    return lock_decorated

  return lock_decorator


def basename_from_url(url: str) -> str:
  """Returns file name of file at given url."""
  filename = urllib.parse.urlparse(url).path
  filename = os.path.basename(filename)
  # Replace `%2F` (html code for `/`) by `_`.
  # This is consistent with how Chrome rename downloaded files.
  filename = filename.replace('%2F', '_')
  return filename or 'unknown_name'


def list_info_files(dir_path: epath.PathLike) -> Sequence[str]:
  """Returns name of info files within dir_path."""
  path = epath.Path(dir_path)
  info_files = []
  for file_path in path.glob('*.json'):
    info_files.append(file_path.name)
  return info_files


def get_base64(
    write_fn: bytes | Callable[[io.BytesIO], None],
) -> str:
  """Extracts the base64 string of an object by writing into a tmp buffer."""
  if isinstance(write_fn, bytes):  # Value already encoded
    bytes_value = write_fn
  else:
    buffer = io.BytesIO()
    write_fn(buffer)
    bytes_value = buffer.getvalue()
  return base64.b64encode(bytes_value).decode('ascii')  # pytype: disable=bad-return-type


@contextlib.contextmanager
def add_sys_path(path: epath.PathLike) -> Iterator[None]:
  """Temporary add given path to `sys.path`."""
  path = os.fspath(path)
  try:
    sys.path.insert(0, path)
    yield
  finally:
    sys.path.remove(path)


def make_valid_name(name: str) -> str:
  """Sanitizes a string to follow the Python lexical definitions.

  The function removes all forbidden characters outside of A-Za-z0-9_ and
  replaces them with an underscore.

  Warning: if you want to convert a name to a valid TFDS name, prefer
  `conversion_utils.to_tfds_name` instead.

  Args:
    name: The input string to sanitize.

  Returns:
    The sanitized string.
  """
  return re.sub(_INVALID_TFDS_NAME_CHARACTER, '_', name)
